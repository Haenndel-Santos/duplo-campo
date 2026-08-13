# -*- coding: utf-8 -*-
"""
r12a_forma_de_k.py — SONDA PREPARATORIA do R-12 (prova analitica de
c_s^2 em r -> 0): qual e a FORMA da dependencia em k?

MOTIVO (pre-declarado). O R-11 registrou c_s^2(kh=30) = -1.010 e
c_s^2(kh=100) = -1.261 e extrapolou o par SUPONDO que a diferenca vem
de um termo ~k^4 ("ja identificado no R-9a"), obtendo c_s^2 -> -0.986
~ -1. Mas dois pontos nao distinguem duas leituras:

   (H4)  om2/(k/a)^2 = c2 + d*kh^2         [termo k^4]  -> c2 = -0.985
   (Hm)  om2/(k/a)^2 = c_inf + B/kh^2      [termo de MASSA] -> c_inf = -1.286

A leitura (Hm) e a natural: om2 = c_s^2 (k/a)^2 + m_ef^2 e o que se
chama c_s^2 e o limite kh -> infinito. A leitura (H4) exige um termo
k^4 com coeficiente NEGATIVO e sem saturacao. As duas coincidem nos
dois pontos medidos e divergem em todo o resto — e mudam o ENUNCIADO
do no-go (-1 vs -9/7).

MEDIDA: om2_ef/(k/a)^2 do modo metrico (Etil) e do espectador (dchi)
numa grade larga de kh, em epoca profunda do regime r -> 0, nos dois
fundos beta-constantes. Mesma maquina do R-10a (E1+E2 corrigidas,
om2_ef = (Cdot+W)/K, reescala D).

CRITERIOS (pre-declarados):
  G-FORMA: ajustar os dados de kh in [30, 3000] as duas familias e
    comparar o residuo relativo maximo. Vence quem der residuo
    < 1e-3 com a outra acima de 1e-2. Se ambas falharem, a forma tem
    mais estrutura (rational em k^2) e o ajuste de 2 parametros e
    inadequado — reportar assim.
  G-SAT: se om2/(k/a)^2 satura num plato ao crescer kh, o plato E o
    c_s^2 (definicao padrao). Reportar o plato com 5 casas.
  G-CAL: o espectador tem de dar 1 em cada kh usado (calibrador). Todo
    kh com |cs2_dchi - 1| > 1e-3 e DESCARTADO do ajuste (metodo fora de
    validade ali) — separa saturacao fisica de perda de condicionamento.

FRONTEIRA: identica a do R-10a (beta-constante, materia so como rho de
fundo, sem radiacao, sistema 2-DOF reduzido). Esta sonda NAO e a
prova; ela so fixa o alvo que a prova simbolica (R-12b) tem de
reproduzir.

Uso (raiz do repo, venv ativo):
    python auditoria/code/r12a_forma_de_k.py
Saida em auditoria/code/out/r12a_forma_de_k.txt
"""
import importlib.util
import os
import sys
import time

import numpy as np
import sympy as sp

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
G1_TOL = 1e-10
MU = 1.0
ME2 = 0.5
B0V, B2V, B4V = 1.0, -0.4, 0.5
RHO0 = 0.3
KHS = [1.0, 3.0, 10.0, 30.0, 100.0, 300.0, 1000.0, 3000.0, 1e4, 3e4]
EPOCAS = [(0.01, 'r -> 0 (regime instavel)'),
          (0.1, 'r -> 0 (borda)'),
          (1000.0, 'r = r_inf (era tardia)')]

say("=" * 72)
say("R-12a — SONDA: a forma da dependencia em k de om2_ef/(k/a)^2")
say("=" * 72)

if not d1.gr_selfcheck():
    say("[!] V1 falhou — abortando")
    sys.exit(1)
say("[V1] GR selfcheck: PASSA")

L2s, fields, vels = d1.build_L2()
K7, C7, W7 = quadratic_matrices(L2s, fields, vels)
if [str(f) for f in fields] != NOMES:
    raise RuntimeError("ordem de campos mudou")
Hdd_s, Hfdd_s, xidd_s, chiddd_s = sp.symbols(
    'Hddot H_fddot xiddot chidddot')
Cd7 = sp.zeros(7, 7)
for i in range(7):
    for j in range(7):
        Cd7[i, j] = dt_background(
            C7[i, j], {Hd_s: Hdd_s, Hfd_s: Hfdd_s, xid_s: xidd_s,
                       chidd_s: chiddd_s})
say("[montagem] K,C,W,CdS prontos")

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
    rho_til = (RHO0 * a**-3) / meff2
    rr = np.roots([kap * B4V - 3 * B2V, -3 * B1V,
                   3 * kap * B2V - B0V - rho_til, kap * B1V])
    reais = sorted(z.real for z in rr
                   if abs(z.imag) < 1e-9 and z.real > 1e-14)
    if not reais:
        return None
    r = reais[0]
    dW = kap * (2 * B4V * r - B1V / r**2) - 3 * B1V - 6 * B2V * r
    if abs(dW) < 1e-300:
        return None
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
    Hd = H2 * (0.5 * (2 / r + dVf / Vf) * drdN)
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
    esc = max(1.0, np.max(np.abs(K)))
    mset = set(MULT)
    for i in MULT:
        if np.max(np.abs(K[i, :])) > 1e-10 * esc:
            raise RuntimeError("K mult nao-nula")
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
    cnd = np.linalg.cond(WXX)
    WXXi = np.linalg.inv(WXX)
    CdX = C[np.ix_(DYN, MULT)]
    K3 = K[np.ix_(DYN, DYN)] + CdX @ WXXi @ CdX.T
    C3 = C[np.ix_(DYN, DYN)] - CdX @ WXXi @ W[np.ix_(MULT, DYN)]
    W3 = W[np.ix_(DYN, DYN)] - W[np.ix_(DYN, MULT)] @ WXXi \
        @ W[np.ix_(MULT, DYN)]
    return K3, C3, W3, cnd


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


def om2_no_ponto(a0, B1V, kh):
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
    g1, cnd = 0.0, 0.0
    try:
        for p in range(41):
            K3, C3, W3, c_ = e1(Ms['K'][p], Ms['C'][p], Ms['W'][p],
                                Ms['CdS'][p])
            cnd = max(cnd, c_)
            esc = np.max(np.abs(K3))
            g1 = max(g1, np.max(np.abs(K3[0, :])) / esc)
            K3[0, :] = 0.0
            K3[:, 0] = 0.0
            K3s[p], C3s[p], W3s[p] = K3, C3, W3
    except (RuntimeError, np.linalg.LinAlgError) as e:
        return dict(erro=str(e))
    if g1 >= G1_TOL:
        return dict(erro=f'G1={g1:.1e}')
    C3d = np.gradient(C3s, Ns, axis=0) * Hs[:, None, None]
    K2s = np.zeros((41, 2, 2))
    C2s = np.zeros((41, 2, 2))
    W2s = np.zeros((41, 2, 2))
    for p in range(41):
        K2s[p], C2s[p], W2s[p] = e2(K3s[p], C3s[p], W3s[p], C3d[p])
    C2d = np.gradient(C2s, Ns, axis=0) * Hs[:, None, None]
    om2 = [(C2d[20, i, i] + W2s[20, i, i]) / K2s[20, i, i]
           for i in range(2)]
    return dict(om2=om2, H=Hs[20], cond=cnd, r=f0['r'], erro=None)


def ajusta(khs, fs):
    """Retorna (par_H4, res_H4, par_Hm, res_Hm) por minimos quadrados."""
    kh = np.asarray(khs, float)
    y = np.asarray(fs, float)
    A4 = np.vstack([np.ones_like(kh), kh**2]).T
    p4, *_ = np.linalg.lstsq(A4, y, rcond=None)
    r4 = np.max(np.abs(A4 @ p4 - y) / np.abs(y))
    Am = np.vstack([np.ones_like(kh), kh**-2]).T
    pm, *_ = np.linalg.lstsq(Am, y, rcond=None)
    rm = np.max(np.abs(Am @ pm - y) / np.abs(y))
    return p4, r4, pm, rm


resumo = []
for B1V in (1.0, 4.47):
    for a0, rot in EPOCAS:
        f0 = fundo(a0, B1V)
        say("")
        say("=" * 72)
        say(f"beta1={B1V:g} | a={a0:g} | r={f0['r']:.4e} | {rot}")
        say("=" * 72)
        say(f"    {'kh':>8} {'cs2_Etil':>14} {'cs2_dchi':>12} "
            f"{'|cal-1|':>9} {'cond':>9}")
        khs, fs = [], []
        for kh in KHS:
            res = om2_no_ponto(a0, B1V, kh)
            if res is None or res.get('erro'):
                say(f"    {kh:8g}  (erro: {res and res.get('erro')})")
                continue
            kfis2 = (kh * res['H'])**2
            cs_et = res['om2'][0] / kfis2
            cs_dc = res['om2'][1] / kfis2
            dev = abs(cs_dc - 1.0)
            marca = "" if dev <= 1e-3 else "   <- DESCARTADO (G-CAL)"
            say(f"    {kh:8g} {cs_et:+14.6f} {cs_dc:12.6f} {dev:9.1e} "
                f"{res['cond']:9.1e}{marca}")
            if dev <= 1e-3 and 30.0 <= kh <= 3000.0:
                khs.append(kh)
                fs.append(cs_et)
        if len(khs) >= 3:
            p4, r4, pm, rm = ajusta(khs, fs)
            say("")
            say(f"    [G-FORMA] kh usados no ajuste: {khs}")
            say(f"      (H4) c2 + d*kh^2 : c2 = {p4[0]:+.6f}, "
                f"d = {p4[1]:+.3e}  | residuo rel. max = {r4:.2e}")
            say(f"      (Hm) c_inf + B/kh^2: c_inf = {pm[0]:+.6f}, "
                f"B = {pm[1]:+.4f}  | residuo rel. max = {rm:.2e}")
            veredito = ("(Hm) MASSA" if rm < 1e-3 <= r4 else
                        "(H4) k^4" if r4 < 1e-3 <= rm else
                        "AMBAS OK (indistinguiveis nesta grade)"
                        if max(r4, rm) < 1e-3 else
                        "NENHUMA (forma tem mais estrutura)")
            say(f"      -> vencedor: {veredito}")
            if len(khs) >= 2:
                say(f"    [G-SAT] plato aparente (maior kh valido, "
                    f"kh={khs[-1]:g}): {fs[-1]:+.6f}")
            resumo.append((B1V, a0, f0['r'], p4[0], r4, pm[0], rm,
                           khs[-1], fs[-1], veredito))
        else:
            say("    [G-FORMA] pontos validos insuficientes")

say("")
say("=" * 72)
say("RESUMO")
say("=" * 72)
say(f"  {'beta1':>6} {'a':>8} {'r':>10} {'c2(H4)':>10} {'res':>8} "
    f"{'c_inf(Hm)':>10} {'res':>8} {'kh_max':>7} {'f(kh_max)':>11}")
for b, a0, r, c2, r4, ci, rm, khm, fm, ver in resumo:
    say(f"  {b:6g} {a0:8g} {r:10.2e} {c2:+10.5f} {r4:8.1e} "
        f"{ci:+10.5f} {rm:8.1e} {khm:7g} {fm:+11.6f}   {ver}")

os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
with open(os.path.join(HERE, 'out', 'r12a_forma_de_k.txt'), 'w',
          encoding='utf-8') as fh:
    fh.write("\n".join(OUT) + "\n")
say("")
say("saida escrita em auditoria/code/out/r12a_forma_de_k.txt")
