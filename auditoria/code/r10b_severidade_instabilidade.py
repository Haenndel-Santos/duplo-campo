# -*- coding: utf-8 -*-
"""
r10b_severidade_instabilidade.py — BLOCO 1, sequencia do A1: QUAO
GRAVE e a instabilidade de gradiente do R-10a? Ela se auto-invalida
(saida de Akrami et al.) ou destroi o regime linear?

CONTEXTO: o R-10a (docs/resultado_r10a_gradiente.md) confirmou
c_s^2 ~ -1 no escalar metrico para r -> 0 (alto z), com cinetica
positiva (gradiente genuino), metodo calibrado e independente de
condicionamento. A questao seguinte, que decide o destino da
implementacao:
  - a taxa de crescimento e |c_s| k/a; modos sub-horizonte crescem;
  - se o crescimento levar as perturbacoes ao regime NAO-LINEAR, a
    teoria de perturbacao linear se auto-invalida — que e exatamente
    o argumento de Akrami et al. (arXiv:1503.07521) para salvar a
    viabilidade cosmologica da bimetrica;
  - mas isso corta os dois lados: se o linear nao vale em z alto,
    NENHUM C_ell pode ser calculado linearmente ali — e o programa
    observacional do cap. 09 muda de natureza.

MEDIDAS (pre-declaradas):
  S1 — perfil c_s^2(a) fino (25 epocas de a=1e-3 a a=5) em kh=30 e
    kh=100, para localizar a_cross (onde c_s^2 muda de sinal) e ter o
    perfil para integrar. Espectador como calibrador em cada ponto.
  S2 — para uma grade de modos comoveis, rotulados pelo instante de
    ENTRADA no horizonte a_ent (onde k = aH), o expoente de
    crescimento acumulado ate a_cross:
        lnA(k) = integral de |c_s| * (k/aH) dN,  de a_ent a a_cross,
    calculado so onde c_s^2 < 0 (fora disso nao ha crescimento de
    gradiente). Modos que nunca entram antes de a_cross nao crescem.
  S3 — o teste de auto-invalidacao: com amplitude primordial
    tipica delta_i ~ 1e-5 (2a: valor padrao de CMB, adotado como
    referencia declarada), o modo vira nao-linear quando
    lnA > ln(1/delta_i) ~ 11.5. Reportar o menor k (maior escala) que
    atinge isso — e a escala a partir da qual o tratamento linear se
    auto-invalida.
  S4 — quantos e-folds de instabilidade existem: N_inst = ln(a_cross
    / a_min_valido).

CRITERIOS (pre-declarados):
  lnA < 11.5 para TODOS os modos que entram antes de a_cross ->
    INSTABILIDADE BRANDA: cresce mas nao sai do linear; e uma
    correcao calculavel, e o C_ell continua fazivel (com este efeito
    dentro).
  lnA > 11.5 para modos com kh(a_cross) < 100 -> AUTO-INVALIDACAO:
    o linear morre em escalas de interesse observacional; vale a
    saida de Akrami et al. (a instabilidade nao e fisica no linear),
    MAS o programa observacional linear em z alto morre junto e o
    cap. 09 tem que ser reescrito.
  Caso intermediario -> quantificar a escala de corte.

FRONTEIRA: benchmark beta-constante; brinquedo sem radiacao (o mapa
a <-> z muda com radiacao — item (f)); delta_i = 1e-5 adotado como
referencia; |c_s| do proprio R-10a.

Requer sympy, numpy, scipy. ~3-5 min.
Uso (raiz do repo, venv ativo):
    python auditoria/code/r10b_severidade_instabilidade.py
Saida em auditoria/code/out/r10b_severidade_instabilidade.txt
"""
import importlib.util
import os
import sys
import time

import numpy as np
import sympy as sp
from scipy.interpolate import interp1d
from scipy.optimize import brentq

HERE = os.path.dirname(os.path.abspath(__file__))
DCODE = os.path.normpath(os.path.join(HERE, '..', '..', 'derivations', 'code'))
sys.path.insert(0, DCODE)

spec = importlib.util.spec_from_file_location(
    "d1mod", os.path.join(DCODE, "01_setor_escalar_K_Omega.py"))
d1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(d1)

from tdcp_pert_lib import (a_s, b_s, xi_s, H_s, Hf_s, Hd_s, Hfd_s, xid_s,
                           chid_s, chidd_s, Mg2, Mf2, m2, Meff2,
                           b0, b1, b2, b3, b4, Fb, Fp, Fpp,
                           Ub, Up, Upp, rho_s, k as ksym,
                           quadratic_matrices, dt_background)

T0 = time.time()
OUT = []


def say(*a):
    line = " ".join(str(x) for x in a)
    print(f"[{time.time()-T0:7.1f}s] {line}")
    OUT.append(line)


NOMES = ['Phi_g', 'B_g', 'Phi_f', 'Psi_f', 'B_f', 'E_f', 'dchi']
MULT = [0, 1, 2, 4]
DYN = [3, 5, 6]
EPOCAS = list(np.geomspace(1e-3, 5.0, 25))
KHS = [30.0, 100.0]
DELTA_I = 1e-5
LN_NL = np.log(1.0 / DELTA_I)
MU = 1.0
ME2 = 0.5
B0V, B2V, B4V = 1.0, -0.4, 0.5
RHO0 = 0.3

say("=" * 72)
say("R-10b — severidade da instabilidade de gradiente (A1, sequencia)")
say("=" * 72)

if not d1.gr_selfcheck():
    say("[!] V1 falhou")
    sys.exit(1)
L2s, fields, vels = d1.build_L2()
K7, C7, W7 = quadratic_matrices(L2s, fields, vels)
Hdd_s, Hfdd_s, xidd_s, chiddd_s = sp.symbols(
    'Hddot H_fddot xiddot chidddot')
Cd7 = sp.zeros(7, 7)
for i in range(7):
    for j in range(7):
        Cd7[i, j] = dt_background(
            C7[i, j], {Hd_s: Hdd_s, Hfd_s: Hfdd_s, xid_s: xidd_s,
                       chidd_s: chiddd_s})
LIVRES = (a_s, b_s, xi_s, H_s, Hf_s, Hd_s, Hfd_s, xid_s,
          chid_s, chidd_s, Ub, Up, Upp, ksym, Mf2, Meff2,
          Hdd_s, Hfdd_s, xidd_s, chiddd_s)
FIXOS = {Mg2: 1, m2: 1, rho_s: 0}
BETAS = (b0, b1, b2, b3, b4)


def fatias(M):
    Msub = M.subs(FIXOS)
    base_s = Msub.subs({Fb: 0, Fp: 0, Fpp: 0})
    out = {'base': sp.lambdify(LIVRES, base_s, modules='numpy')}
    for n, bn in enumerate(BETAS):
        bsub = {bm: (1 if mm == n else 0) for mm, bm in enumerate(BETAS)}
        Sl = Msub.subs({Fb: 1, Fp: 0, Fpp: 0}).subs(bsub) - base_s
        out[('Fb', n)] = sp.lambdify(LIVRES, Sl, modules='numpy')
    return out


FK, FC, FW, FCd = fatias(K7), fatias(C7), fatias(W7), fatias(Cd7)
say("[fatias] prontas")


def monta(fat, args, bvals):
    M = np.array(fat['base'](*args), float).copy()
    for n in range(5):
        if bvals[n]:
            M += bvals[n] * np.array(fat[('Fb', n)](*args), float)
    return M


def fundo(a, B1V):
    kap = 1.0 / MU
    meff2 = ME2
    rho = RHO0 * a**-3
    rho_til = rho / meff2
    rr = np.roots([kap * B4V - 3 * B2V, -3 * B1V,
                   3 * kap * B2V - B0V - rho_til, kap * B1V])
    reais = sorted(z.real for z in rr
                   if abs(z.imag) < 1e-9 and z.real > 1e-14)
    if not reais:
        return None
    r = reais[0]
    dW = kap * (2 * B4V * r - B1V / r**2) - 3 * B1V - 6 * B2V * r
    drdN = -3 * rho_til / dW
    d2W = kap * (2 * B4V + 2 * B1V / r**3) - 6 * B2V
    d2rdN2 = 9 * rho_til / dW + 3 * rho_til * d2W * drdN / dW**2
    xi = r + drdN
    Vf = B4V + 3 * B2V / r**2 + B1V / r**3
    dVf = -6 * B2V / r**3 - 3 * B1V / r**4
    H2 = meff2 * r * r * Vf / (3.0 * MU)
    if H2 <= 0 or xi <= 0:
        return None
    H = np.sqrt(H2)
    dlnH_dN = 0.5 * (2 / r + dVf / Vf) * drdN
    Hd = H2 * dlnH_dN
    xid = H * (drdN + d2rdN2)
    Hfd = (Hd - H2 * drdN / r) / r
    rho_int = meff2 * (B0V + 3 * B1V * r + 3 * B2V * r**2)
    return dict(r=r, xi=xi, H=H, Hf=H / r, Hd=Hd, Hfd=Hfd, xid=xid,
                Ub=3 * H2 - rho_int)


def fundo_ext(a, B1V, h=1e-5):
    f = fundo(a, B1V)
    if f is None:
        return None
    fp, fm = fundo(a * np.exp(h), B1V), fundo(a * np.exp(-h), B1V)
    if fp is None or fm is None:
        return None
    H = f['H']
    f['Hdd'] = H * (fp['Hd'] - fm['Hd']) / (2 * h)
    f['Hfdd'] = H * (fp['Hfd'] - fm['Hfd']) / (2 * h)
    f['xidd'] = H * (fp['xid'] - fm['xid']) / (2 * h)
    return f


def matriz_D(kc):
    return np.diag([1.0, 1.0 / kc, 1.0, 1.0, 1.0 / kc, 1.0 / kc**2, 1.0])


def e1(Kt, Ct, Wt, Cdot):
    K, C, W = Kt.copy(), Ct.copy(), Wt.copy()
    mset = set(MULT)
    for i in MULT:
        for j in range(7):
            cd, cij = Cdot[i, j], Ct[i, j]
            if i == j:
                W[i, i] += cd
            elif j in mset:
                W[i, j] += cd
            else:
                W[i, j] += cd
                W[j, i] += cd
                C[j, i] -= cij
        C[i, :] = 0.0
    WXX = 0.5 * (W[np.ix_(MULT, MULT)] + W[np.ix_(MULT, MULT)].T)
    WXXi = np.linalg.inv(WXX)
    CdX = C[np.ix_(DYN, MULT)]
    K3 = K[np.ix_(DYN, DYN)] + CdX @ WXXi @ CdX.T
    C3 = C[np.ix_(DYN, DYN)] - CdX @ WXXi @ W[np.ix_(MULT, DYN)]
    W3 = W[np.ix_(DYN, DYN)] - W[np.ix_(DYN, MULT)] @ WXXi \
        @ W[np.ix_(MULT, DYN)]
    return K3, C3, W3


def e2(K3, C3, W3, C3d):
    K, C, W = K3.copy(), C3.copy(), W3.copy()
    for j in range(3):
        cij, cd = C3[0, j], C3d[0, j]
        if j == 0:
            W[0, 0] += cd
        else:
            W[0, j] += cd
            W[j, 0] += cd
            C[j, 0] -= cij
    C[0, :] = 0.0
    W00 = W[0, 0]
    keep = [1, 2]
    cx = C[np.ix_(keep, [0])]
    wx = W[np.ix_(keep, [0])]
    K2 = K[np.ix_(keep, keep)] + cx @ cx.T / W00
    C2 = C[np.ix_(keep, keep)] - cx @ W[np.ix_([0], keep)] / W00
    W2 = W[np.ix_(keep, keep)] - wx @ W[np.ix_([0], keep)] / W00
    return 0.5 * (K2 + K2.T), C2, 0.5 * (W2 + W2.T)


def cs2_no_ponto(a0, B1V, kh):
    f0 = fundo(a0, B1V)
    if f0 is None:
        return None
    kc = kh * a0 * f0['H']
    Ns = np.linspace(np.log(a0) - 0.02, np.log(a0) + 0.02, 41)
    Hs = np.zeros(41)
    Ms = {x: np.zeros((41, 7, 7)) for x in ('K', 'C', 'W', 'CdS')}
    D = matriz_D(kc)
    for p, N in enumerate(Ns):
        a = np.exp(N)
        f = fundo_ext(a, B1V)
        if f is None:
            return None
        Hs[p] = f['H']
        args = (a, f['r'] * a, f['xi'], f['H'], f['Hf'], f['Hd'],
                f['Hfd'], f['xid'], 0.0, 0.0, f['Ub'], 0.0, 0.3,
                kc, 1.0, ME2, f['Hdd'], f['Hfdd'], f['xidd'], 0.0)
        bvals = (B0V, B1V, B2V, 0.0, B4V)
        Ms['K'][p] = D @ monta(FK, args, bvals) @ D
        Ms['C'][p] = D @ monta(FC, args, bvals) @ D
        Ms['W'][p] = D @ monta(FW, args, bvals) @ D
        Ms['CdS'][p] = D @ monta(FCd, args, bvals) @ D
    K3s = np.zeros((41, 3, 3))
    C3s = np.zeros((41, 3, 3))
    W3s = np.zeros((41, 3, 3))
    try:
        for p in range(41):
            K3, C3, W3 = e1(Ms['K'][p], Ms['C'][p], Ms['W'][p],
                            Ms['CdS'][p])
            K3[0, :] = 0.0
            K3[:, 0] = 0.0
            K3s[p], C3s[p], W3s[p] = K3, C3, W3
    except (np.linalg.LinAlgError, RuntimeError):
        return None
    C3d = np.gradient(C3s, Ns, axis=0) * Hs[:, None, None]
    K2s = np.zeros((41, 2, 2))
    C2s = np.zeros((41, 2, 2))
    W2s = np.zeros((41, 2, 2))
    for p in range(41):
        K2s[p], C2s[p], W2s[p] = e2(K3s[p], C3s[p], W3s[p], C3d[p])
    C2d = np.gradient(C2s, Ns, axis=0) * Hs[:, None, None]
    kf2 = (kh * Hs[20])**2
    return dict(cs2=(C2d[20, 0, 0] + W2s[20, 0, 0]) / K2s[20, 0, 0] / kf2,
                cal=(C2d[20, 1, 1] + W2s[20, 1, 1]) / K2s[20, 1, 1] / kf2,
                H=Hs[20], r=f0['r'])


for B1V in (1.0, 4.47):
    say("")
    say("=" * 72)
    say(f"FUNDO beta1={B1V:g}")
    say("=" * 72)
    aas = []
    cs30 = []
    cs100 = []
    Hs_l = []
    say("    S1 — perfil c_s^2(a):")
    say(f"    {'a':>9} {'r':>10} {'cs2(30)':>9} {'cs2(100)':>9} "
        f"{'calib':>8}")
    for a0 in EPOCAS:
        r30 = cs2_no_ponto(a0, B1V, 30.0)
        r100 = cs2_no_ponto(a0, B1V, 100.0)
        if r30 is None or r100 is None:
            continue
        aas.append(a0)
        cs30.append(r30['cs2'])
        cs100.append(r100['cs2'])
        Hs_l.append(r30['H'])
        if a0 in EPOCAS[::3] or (0.3 < a0 < 2.0):
            say(f"    {a0:9.3g} {r30['r']:10.3e} {r30['cs2']:+9.4f} "
                f"{r100['cs2']:+9.4f} {r30['cal']:8.5f}")
    aas = np.array(aas)
    cs30 = np.array(cs30)
    cs100 = np.array(cs100)
    Hs_l = np.array(Hs_l)
    Ns_l = np.log(aas)

    # a_cross (onde cs2 muda de sinal), por kh
    def acha_cross(cs):
        f = interp1d(Ns_l, cs, kind='cubic')
        for i in range(len(Ns_l) - 1):
            if cs[i] < 0 <= cs[i + 1]:
                return float(np.exp(brentq(lambda x: f(x),
                                           Ns_l[i], Ns_l[i + 1])))
        return float('nan')

    a_cr30 = acha_cross(cs30)
    a_cr100 = acha_cross(cs100)
    say("")
    say(f"    a_cross (c_s^2 = 0): kh=30 -> a = {a_cr30:.4f} "
        f"(r = {fundo(a_cr30, B1V)['r']:.4f}); "
        f"kh=100 -> a = {a_cr100:.4f}")
    say(f"    S4 — e-folds de instabilidade cobertos pela varredura: "
        f"N_inst = {np.log(a_cr30 / aas[0]):.1f} "
        f"(de a={aas[0]:.1e} a a_cross)")

    # S2/S3 — crescimento por modo comovel
    fH = interp1d(Ns_l, np.log(Hs_l), kind='cubic')
    fcs = interp1d(Ns_l, np.abs(np.minimum(cs30, 0.0)), kind='cubic')
    say("")
    say("    S2/S3 — crescimento acumulado por modo (rotulado pelo a")
    say("    de entrada no horizonte, k = aH):")
    say(f"    {'a_ent':>9} {'kh(a_cross)':>12} {'lnA':>9} "
        f"{'e^lnA':>10} {'linear?':>9}")
    k_nl = None
    for a_ent in np.geomspace(aas[0] * 1.5, a_cr30 * 0.9, 9):
        N_ent = np.log(a_ent)
        kcom = a_ent * float(np.exp(fH(N_ent)))
        Ng = np.linspace(N_ent, np.log(a_cr30), 400)
        khg = kcom / (np.exp(Ng) * np.exp(fH(Ng)))
        integ = np.abs(fcs(Ng)) ** 0.5 * khg
        lnA = float(np.trapezoid(integ, Ng))
        kh_cr = kcom / (a_cr30 * float(np.exp(fH(np.log(a_cr30)))))
        lin = lnA < LN_NL
        if not lin and k_nl is None:
            k_nl = (a_ent, kh_cr, lnA)
        say(f"    {a_ent:9.3g} {kh_cr:12.1f} {lnA:9.2f} "
            f"{np.exp(min(lnA, 300)):10.2e} "
            f"{'sim' if lin else 'NAO':>9}")
    say("")
    if k_nl is None:
        say("    >>> INSTABILIDADE BRANDA neste fundo: nenhum modo que")
        say("    entra antes de a_cross sai do regime linear com")
        say(f"    delta_i = {DELTA_I:.0e}.")
    else:
        say(f"    >>> AUTO-INVALIDACAO: o modo que entra em a = "
            f"{k_nl[0]:.3g} (kh(a_cross) = {k_nl[1]:.0f}) ja cresce")
        say(f"    lnA = {k_nl[2]:.1f} > {LN_NL:.1f} = ln(1/delta_i).")
        say("    Modos menores que esse violam |Phi| << 1 antes do fim")
        say("    da era instavel: a perturbacao LINEAR se auto-invalida")
        say("    (a saida de Akrami et al. 1503.07521 se aplica), MAS")
        say("    o mesmo argumento proibe calcular C_ell linearmente em")
        say("    z alto nessas escalas.")

say("")
say("=" * 72)
say("VEREDITO R-10b")
say("=" * 72)
say("  Ver por fundo acima. A leitura conjunta com o R-10a esta em")
say("  docs/resultado_r10a_gradiente.md (a ser atualizado com estes")
say("  numeros).")

os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
with open(os.path.join(HERE, 'out', 'r10b_severidade_instabilidade.txt'),
          'w', encoding='utf-8') as fh:
    fh.write("\n".join(OUT) + "\n")
say("")
say("saida escrita em auditoria/code/out/r10b_severidade_instabilidade.txt")
