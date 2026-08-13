# -*- coding: utf-8 -*-
"""
r12c_varredura_plato.py — R-12(c): a varredura de forma-beta do R-11
REFEITA sobre a grandeza certa (o PLATO sub-horizonte), nas MESMAS 108
celulas.

MOTIVO. O R-11 mediu c_s^2 num unico kh (= 30) e concluiu constancia
estrutural com desvio-padrao 6e-6. A sonda R-12a mostrou que kh = 30
cai num transiente NAO-MONOTONICO da funcao om2/(k/a)^2 e que o valor
sub-horizonte (kh -> oo) e outro (~ -0.687, nao -1.010). A constancia
observada pelo R-11 e real, mas e a constancia do VALOR EM kh=30 — o
que nao e c_s^2. Esta varredura repete a grade com a definicao padrao
(limite sub-horizonte) e decide se o enunciado DE CLASSE sobrevive.

GRADE (identica ao R-11, F1: beta_3 = 0):
  beta_2 in {-2, -1, -0.4, -0.1} x beta_4 in {0.1, 0.5, 2.0}
  x beta_0 in {0.5, 1.0, 2.0} x mu in {0.3, 1.0, 3.0}, beta_1 = 1,
  a = 0.01 (r -> 0).

MEDIDAS (pre-declaradas):
  P-CS  : c_s^2 = valor em KH_PLATO = 3e4, por celula.
  P-CONV: |f(3e4) - f(1e4)| / |f(3e4)| — se > 1e-2 a celula NAO
          atingiu o plato na grade e e reportada como nao-convergida
          (nao entra na estatistica do plato).
  P-CAL : c_s^2 do espectador em cada kh usado (tem que dar 1); celula
          com desvio > 1e-3 e descartada como nao-interpretavel.
  P-30  : o valor em kh = 30 (a grandeza do R-11), para exibir lado a
          lado quanto ele difere do plato.

CRITERIOS (pre-declarados):
  (a) SINAL: alguma celula viavel e convergida com plato > 0 ->
      SAIDA ENCONTRADA (a forma-beta salva a implementacao); todas
      negativas -> o no-go de classe por gradiente SOBREVIVE a
      correcao de definicao.
  (b) CONSTANCIA: desvio-padrao do plato / |mediana| < 1e-3 ->
      constante estrutural da classe (agora sobre a grandeza certa).
      Entre 1e-3 e 1e-1 -> quase-constante, reportar a dependencia.
      > 1e-1 -> NAO e constante de classe; o enunciado do R-11 tem de
      ser enfraquecido de "constante estrutural" para "negativo em
      toda a grade".
  (c) O R-11 fica CORRIGIDO em qualquer caso quanto ao VALOR: -1.010
      e o valor em kh = 30, nao c_s^2.

FRONTEIRA: identica a do R-11 (um ponto de epoca por celula, beta_1
fixo, beta_3 = 0, materia so como rho de fundo, sem radiacao).

Requer sympy, numpy. ~15-30 min.
Uso: python auditoria/code/r12c_varredura_plato.py
Saida em auditoria/code/out/r12c_varredura_plato.txt
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


MULT = [0, 1, 2, 4]
DYN = [3, 5, 6]
A_TESTE = 0.01
KHS = [30.0, 1e4, 3e4]
KH_PLATO = 3e4
RHO0 = 0.3
B1V = 1.0
B2S = [-2.0, -1.0, -0.4, -0.1]
B4S = [0.1, 0.5, 2.0]
B0S = [0.5, 1.0, 2.0]
MUS = [0.3, 1.0, 3.0]
CAL_TOL = 1e-3
CONV_TOL = 1e-2

say("=" * 72)
say("R-12c — varredura de forma-beta sobre o PLATO sub-horizonte")
say("=" * 72)

if not d1.gr_selfcheck():
    say("[!] V1 falhou — abortando")
    sys.exit(1)
say("[V1] GR selfcheck: PASSA")

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


def fundo(a, B0V, B2V, B4V, mu):
    kap = 1.0 / mu
    meff2 = mu / (1.0 + mu)
    rho_til = (RHO0 * a**-3) / meff2
    rr = np.roots([kap * B4V - 3 * B2V, -3 * B1V,
                   3 * kap * B2V - B0V - rho_til, kap * B1V])
    reais = sorted(z.real for z in rr
                   if abs(z.imag) < 1e-9 and z.real > 1e-16)
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
    H2 = meff2 * r * r * Vf / (3.0 * mu)
    if H2 <= 0 or xi <= 0:
        return None
    H = np.sqrt(H2)
    Hd = H2 * (0.5 * (2 / r + dVf / Vf) * drdN)
    xid = H * (drdN + d2rdN2)
    Hfd = (Hd - H2 * drdN / r) / r
    rho_int = meff2 * (B0V + 3 * B1V * r + 3 * B2V * r**2)
    return dict(r=r, xi=xi, H=H, Hf=H / r, Hd=Hd, Hfd=Hfd, xid=xid,
                Ub=3 * H2 - rho_int, meff2=meff2)


def fundo_ext(a, B0V, B2V, B4V, mu, h=1e-5):
    f = fundo(a, B0V, B2V, B4V, mu)
    if f is None:
        return None
    fp = fundo(a * np.exp(h), B0V, B2V, B4V, mu)
    fm = fundo(a * np.exp(-h), B0V, B2V, B4V, mu)
    if fp is None or fm is None:
        return None
    H = f['H']
    f['Hdd'] = H * (fp['Hd'] - fm['Hd']) / (2 * h)
    f['Hfdd'] = H * (fp['Hfd'] - fm['Hfd']) / (2 * h)
    f['xidd'] = H * (fp['xid'] - fm['xid']) / (2 * h)
    return f


def matriz_D(kc):
    return np.diag([1.0, 1.0 / kc, 1.0, 1.0, 1.0 / kc, 1.0 / kc**2, 1.0])


def cs2_celula(B0V, B2V, B4V, mu, kh):
    f0 = fundo(A_TESTE, B0V, B2V, B4V, mu)
    if f0 is None:
        return None
    kc = kh * A_TESTE * f0['H']
    Ns = np.linspace(np.log(A_TESTE) - 0.02, np.log(A_TESTE) + 0.02, 41)
    Hs = np.zeros(41)
    Ms = {x: np.zeros((41, 7, 7)) for x in ('K', 'C', 'W', 'CdS')}
    D = matriz_D(kc)
    for p, N in enumerate(Ns):
        a = np.exp(N)
        f = fundo_ext(a, B0V, B2V, B4V, mu)
        if f is None:
            return None
        Hs[p] = f['H']
        args = (a, f['r'] * a, f['xi'], f['H'], f['Hf'], f['Hd'],
                f['Hfd'], f['xid'], 0.0, 0.0, f['Ub'], 0.0, 0.3,
                kc, mu, f['meff2'], f['Hdd'], f['Hfdd'], f['xidd'], 0.0)
        bvals = (B0V, B1V, B2V, 0.0, B4V)
        Ms['K'][p] = D @ monta(FK, args, bvals) @ D
        Ms['C'][p] = D @ monta(FC, args, bvals) @ D
        Ms['W'][p] = D @ monta(FW, args, bvals) @ D
        Ms['CdS'][p] = D @ monta(FCd, args, bvals) @ D
    K3s = np.zeros((41, 3, 3))
    C3s = np.zeros((41, 3, 3))
    W3s = np.zeros((41, 3, 3))
    mset = set(MULT)
    cnd = 0.0
    try:
        for p in range(41):
            K, C, W = (Ms['K'][p].copy(), Ms['C'][p].copy(),
                       Ms['W'][p].copy())
            Cd = Ms['CdS'][p]
            for i in MULT:
                for j in range(7):
                    cd, cij = Cd[i, j], Ms['C'][p][i, j]
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
            cnd = max(cnd, np.linalg.cond(WXX))
            WXXi = np.linalg.inv(WXX)
            CdX = C[np.ix_(DYN, MULT)]
            K3 = K[np.ix_(DYN, DYN)] + CdX @ WXXi @ CdX.T
            C3 = C[np.ix_(DYN, DYN)] - CdX @ WXXi @ W[np.ix_(MULT, DYN)]
            W3 = W[np.ix_(DYN, DYN)] - W[np.ix_(DYN, MULT)] @ WXXi \
                @ W[np.ix_(MULT, DYN)]
            K3[0, :] = 0.0
            K3[:, 0] = 0.0
            K3s[p], C3s[p], W3s[p] = K3, C3, W3
    except (RuntimeError, np.linalg.LinAlgError):
        return None
    C3d = np.gradient(C3s, Ns, axis=0) * Hs[:, None, None]
    K2s = np.zeros((41, 2, 2))
    C2s = np.zeros((41, 2, 2))
    W2s = np.zeros((41, 2, 2))
    for p in range(41):
        K, C, W = K3s[p].copy(), C3s[p].copy(), W3s[p].copy()
        for j in range(3):
            cij, cd = C3s[p][0, j], C3d[p][0, j]
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
        K2s[p], C2s[p], W2s[p] = 0.5 * (K2 + K2.T), C2, 0.5 * (W2 + W2.T)
    C2d = np.gradient(C2s, Ns, axis=0) * Hs[:, None, None]
    kfis2 = (kh * Hs[20])**2
    om2 = [(C2d[20, i, i] + W2s[20, i, i]) / K2s[20, i, i]
           for i in range(2)]
    return dict(cs_et=om2[0] / kfis2, cs_dc=om2[1] / kfis2, r=f0['r'],
                cond=cnd, K2=K2s[20, 0, 0])


linhas = []
descartadas = []
invalidas = []
nao_conv = []
say("")
say(f"    {'b0':>5} {'b2':>6} {'b4':>5} {'mu':>5} {'r':>10} "
    f"{'cs2(kh=30)':>12} {'cs2(1e4)':>12} {'PLATO(3e4)':>12} "
    f"{'conv':>8} {'|cal-1|':>9}")
for B0V in B0S:
    for B2V in B2S:
        for B4V in B4S:
            for mu in MUS:
                vals = {}
                cal = 0.0
                ok = True
                for kh in KHS:
                    res = cs2_celula(B0V, B2V, B4V, mu, kh)
                    if res is None:
                        ok = False
                        break
                    vals[kh] = res['cs_et']
                    cal = max(cal, abs(res['cs_dc'] - 1.0))
                    rr = res['r']
                if not ok:
                    invalidas.append((B0V, B2V, B4V, mu))
                    continue
                if cal > CAL_TOL:
                    descartadas.append((B0V, B2V, B4V, mu, cal))
                    continue
                plato = vals[KH_PLATO]
                conv = abs(plato - vals[1e4]) / abs(plato)
                marca = ""
                if conv > CONV_TOL:
                    nao_conv.append((B0V, B2V, B4V, mu, conv))
                    marca = " <- NAO CONVERGIDA"
                say(f"    {B0V:5g} {B2V:6g} {B4V:5g} {mu:5g} {rr:10.2e} "
                    f"{vals[30.0]:+12.5f} {vals[1e4]:+12.5f} "
                    f"{plato:+12.5f} {conv:8.1e} {cal:9.1e}{marca}")
                linhas.append((B0V, B2V, B4V, mu, rr, vals[30.0], plato,
                               conv))

say("")
say("=" * 72)
say("VEREDITO R-12c (criterios pre-declarados)")
say("=" * 72)
tot = len(B0S) * len(B2S) * len(B4S) * len(MUS)
say(f"  celulas: {tot} na grade | {len(linhas)} interpretaveis | "
    f"{len(invalidas)} fundo invalido | {len(descartadas)} fora da "
    f"calibracao")
conv_ok = [x for x in linhas if x[7] <= CONV_TOL]
say(f"  convergidas ao plato: {len(conv_ok)}/{len(linhas)}")
if conv_ok:
    pl = np.array([x[6] for x in conv_ok])
    p30 = np.array([x[5] for x in conv_ok])
    say("")
    say(f"  [P-CS] plato: min {pl.min():+.6f} | max {pl.max():+.6f} | "
        f"mediana {np.median(pl):+.6f} | desvio-padrao {pl.std():.3e}")
    say(f"         dispersao relativa = {pl.std()/abs(np.median(pl)):.3e}")
    say(f"  [P-30] kh=30 (a grandeza do R-11): min {p30.min():+.6f} | "
        f"max {p30.max():+.6f} | dp {p30.std():.3e}")
    npos = int((pl > 0).sum())
    say("")
    say(f"  (a) SINAL: {npos} celula(s) com plato > 0 de "
        f"{len(conv_ok)}")
    if npos == 0:
        say("      -> NENHUMA saida: o no-go de classe por gradiente")
        say("         SOBREVIVE a correcao de definicao.")
    else:
        say("      -> SAIDA ENCONTRADA: refazer a cascata nessas celulas.")
    disp = pl.std() / abs(np.median(pl))
    if disp < 1e-3:
        say(f"  (b) CONSTANCIA: dispersao {disp:.1e} < 1e-3 -> o plato e")
        say("      CONSTANTE ESTRUTURAL da classe.")
    elif disp < 1e-1:
        say(f"  (b) CONSTANCIA: dispersao {disp:.1e} -> quase-constante;")
        say("      reportar a dependencia residual.")
    else:
        say(f"  (b) CONSTANCIA: dispersao {disp:.1e} > 1e-1 -> o plato NAO")
        say("      e constante de classe; o enunciado do R-11 tem de ser")
        say("      enfraquecido para 'negativo em toda a grade'.")
    say(f"  (c) VALOR: mediana do plato = {np.median(pl):+.6f}; a mediana")
    say(f"      em kh=30 = {np.median(p30):+.6f}. O '-1.010' do R-11 e o")
    say("      segundo numero, nao c_s^2.")

os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
with open(os.path.join(HERE, 'out', 'r12c_varredura_plato.txt'), 'w',
          encoding='utf-8') as fh:
    fh.write("\n".join(OUT) + "\n")
say("")
say("saida escrita em auditoria/code/out/r12c_varredura_plato.txt")
