# -*- coding: utf-8 -*-
"""
r12e_confronto_canais.py — R-12(e): ARBITRAGEM entre os dois canais que
discordam sobre c_s^2 em r -> 0.

O CONFLITO. Dois pipelines da MESMA reducao dao respostas diferentes:

  canal A (float64 + reescala D)  — o do R-10a/R-11/R-12a/R-12c:
      r ~ 1.7e-6:  c_s^2(kh=30) = -1.0103, (100) = -1.2609,
                   (300) = -0.5855, (1e3) = -0.6797, (3e4) = -0.6867
      => leitura: existe estrutura em kh e um "plato" em -0.687.

  canal B (mpmath dps=60, sem D, derivadas de 8a ordem) — o do R-12d:
      r = 1e-6:    c_s^2(kh=1e3 .. 1e6) = -0.9999964 (constante)
      r = 1e-12:   c_s^2 -> -1.0000000000
      => leitura: c_s^2 = -1 exato, sem estrutura em kh.

Como om2_ii = (Cdot2+W2)_ii/K2_ii e INVARIANTE por congruencia diagonal
CONSTANTE, a reescala D nao pode mudar o resultado exato: a diferenca
so pode ser (i) erro de precisao num dos canais ou (ii) bug num deles.

DESENHO DO TESTE (pre-declarado):
  1. V-TARDIO: os dois canais no regime BEM CONDICIONADO (era tardia,
     r ~ r_inf, cond(W_XX) ~ 10), onde o float64 e confiavel. Se
     discordarem ali, ha bug — e o teste para.
  2. V-DEGRAU: o canal B rodado em dps = 16, 20, 30, 40, 60 no ponto
     do conflito. Se os valores de dps baixo reproduzirem o canal A e
     migrarem monotonicamente para o valor de dps alto, a "estrutura
     em kh" do canal A e RUIDO DE PRECISAO e o canal B esta certo.
     Se o canal B for estavel em dps e o A tambem, ha bug estrutural.
  3. V-D: canal B COM a reescala D, dps = 60. Tem de dar o mesmo que
     sem D (invariancia). Falha => a invariancia esta sendo quebrada
     por algum passo nao-covariante da reducao.
  4. V-CAL2: o calibrador do espectador e reportado, MAS com a
     ressalva registrada no R-12d: dchi nao tem termo giroscopico, o
     canal Cdot nao entra nele, e portanto o calibrador NAO tem poder
     de deteccao sobre erros no Cdot. (Declaracao de cegueira do gate,
     conforme a regra proposta em 00_sintese_cruzada.md §2.)

CRITERIO DE DECISAO: vence o canal que (a) reproduza o outro no regime
bem condicionado e (b) seja estavel sob aumento de precisao.

Uso: python -u auditoria/code/r12e_confronto_canais.py
Saida em auditoria/code/out/r12e_confronto_canais.txt
"""
import importlib.util
import os
import sys
import time

import mpmath as mp
import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
DCODE = os.path.normpath(os.path.join(HERE, '..', '..', 'derivations', 'code'))
OUTD = os.path.join(HERE, 'out')
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
    print(f"[{time.time()-T0:7.1f}s] {line}", flush=True)
    OUT.append(line)


MULT = [0, 1, 2, 4]
DYN = [3, 5, 6]
B0V, B1V, B2V, B4V, MUV = 1, 1, sp.Rational(-2, 5), sp.Rational(1, 2), 1
ME2V = sp.Rational(1, 2)
UPPV = sp.Rational(3, 10)
D8 = [sp.Rational(1, 280), sp.Rational(-4, 105), sp.Rational(1, 5),
      sp.Rational(-4, 5), sp.Integer(0), sp.Rational(4, 5),
      sp.Rational(-1, 5), sp.Rational(4, 105), sp.Rational(-1, 280)]
M8 = 4

say("=" * 72)
say("R-12e — arbitragem entre os canais float64+D e mpmath")
say("=" * 72)

say("[1] montando matrizes simbolicas ...")
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
SUBC = {Mg2: 1, m2: 1, rho_s: 0, Fb: 1, Fp: 0, Fpp: 0,
        b0: B0V, b1: B1V, b2: B2V, b3: 0, b4: B4V}
MATS = [M.subs(SUBC) for M in (K7, C7, W7, Cd7)]
F_MP = [sp.lambdify(LIVRES, M, modules='mpmath') for M in MATS]
F_NP = [sp.lambdify(LIVRES, M, modules='numpy') for M in MATS]

# ---- fundo exato como funcao de r (formas fechadas, sympy) ----
rr = sp.Symbol('r', positive=True)
kap = sp.Integer(1) / MUV
rho_til_s = ((kap * B4V - 3 * B2V) * rr**2 - 3 * B1V * rr
             + (3 * kap * B2V - B0V) + kap * B1V / rr)
gg_s = sp.cancel(-3 * rho_til_s / sp.diff(rho_til_s, rr))
Vf_s = B4V + 3 * B2V / rr**2 + B1V / rr**3
HH_s = sp.cancel(ME2V * rr**2 * Vf_s / (3 * MUV))
LL_s = sp.cancel(sp.Rational(1, 2) * (2 / rr + sp.diff(Vf_s, rr) / Vf_s)
                 * gg_s)
H_sy = sp.sqrt(HH_s)
Hd_sy = sp.cancel(HH_s * LL_s)
Hfd_sy = sp.cancel((Hd_sy - HH_s * gg_s / rr) / rr)
xid_sy = H_sy * sp.cancel(sp.diff(rr + gg_s, rr) * gg_s)
CAMPOS = [rho_til_s, sp.cancel(rr + gg_s), H_sy, sp.cancel(H_sy / rr),
          Hd_sy, Hfd_sy, xid_sy, sp.cancel(3 * HH_s - ME2V *
                                           (B0V + 3 * B1V * rr
                                            + 3 * B2V * rr**2)),
          H_sy * sp.cancel(sp.diff(Hd_sy, rr) * gg_s),
          H_sy * sp.cancel(sp.diff(Hfd_sy, rr) * gg_s),
          H_sy * sp.cancel(sp.diff(xid_sy, rr) * gg_s),
          gg_s]
FF_MP = sp.lambdify(rr, CAMPOS, modules='mpmath')
FF_NP = sp.lambdify(rr, CAMPOS, modules='numpy')
CUBICA = sp.Poly((kap * B4V - 3 * B2V) * rr**3 - 3 * B1V * rr**2, rr)
say("    prontas")


_FUN = sp.lambdify(rr, rho_til_s, modules='mpmath')
_DFUN = sp.lambdify(rr, sp.diff(rho_til_s, rr), modules='mpmath')
_RINF = None


def r_de_a(aval, chute=None):
    """r(a) exato: rho~(r) = (0.3 a^-3)/M_eff^2, resolvido por Newton
    em precisao corrente (o ramo finito e a MENOR raiz positiva)."""
    global _RINF
    if _RINF is None:
        x = mp.mpf('0.3')
        for _ in range(300):
            dx = _FUN(x) / _DFUN(x)
            x = x - dx
            if abs(dx) < abs(x) * mp.mpf(10)**(-mp.mp.dps + 6):
                break
        _RINF = x
    alvo = mp.mpf('0.3') * mp.mpf(aval)**-3 / mp.mpf(ME2V)
    x = chute if chute is not None else (
        mp.mpf(1) / alvo if alvo > 10 else _RINF * mp.mpf('0.999'))
    for _ in range(300):
        dx = (_FUN(x) - alvo) / _DFUN(x)
        nx = x - dx
        if nx <= 0:
            nx = x / 2
        x = nx
        if abs(dx) < abs(x) * mp.mpf(10)**(-mp.mp.dps + 6):
            break
    return x


def args_de_r(rv, aval, kc, lib):
    """argumentos das matrizes no ponto de fundo (a, r) da trilha."""
    ff = FF_MP if lib == 'mp' else FF_NP
    (rho_t, xiv, H, Hf, Hd, Hfd, xid, Ubv, Hdd, Hfdd, xidd, gv) = ff(rv)
    zero = mp.mpf(0) if lib == 'mp' else 0.0
    a = aval
    return ((a, rv * a, xiv, H, Hf, Hd, Hfd, xid, zero, zero, Ubv, zero,
             (mp.mpf(UPPV) if lib == 'mp' else float(UPPV)), kc,
             (mp.mpf(MUV) if lib == 'mp' else float(MUV)),
             (mp.mpf(ME2V) if lib == 'mp' else float(ME2V)),
             Hdd, Hfdd, xidd, zero), H, gv)


def dmat(kc, lib, usa_D):
    d = [1, 1 / kc, 1, 1, 1 / kc, 1 / kc**2, 1] if usa_D \
        else [1, 1, 1, 1, 1, 1, 1]
    if lib == 'mp':
        return mp.diag([mp.mpf(x) for x in d])
    return np.diag([float(x) for x in d])


def reduz(Ms, lib):
    """E1 -> (K3, C3, W3) e cond(W_XX)."""
    K, C, W, Cd = Ms
    if lib == 'mp':
        Kx, Cx, Wx = mp.matrix(K), mp.matrix(C), mp.matrix(W)
    else:
        Kx, Cx, Wx = K.copy(), C.copy(), W.copy()
    mset = set(MULT)
    for i in MULT:
        for j in range(7):
            cd, cij = Cd[i, j], C[i, j]
            if i == j:
                Wx[i, i] += cd
            elif j in mset:
                Wx[i, j] += cd
            else:
                Wx[i, j] += cd
                Wx[j, i] += cd
                Cx[j, i] -= cij
        for j in range(7):
            Cx[i, j] = 0
    if lib == 'mp':
        WXX = mp.matrix([[(Wx[i, j] + Wx[j, i]) / 2 for j in MULT]
                         for i in MULT])
        WXXi = WXX**-1
        cnd = float(mp.mnorm(WXX) * mp.mnorm(WXXi))
        sb = lambda M, I, J: mp.matrix([[M[i, j] for j in J] for i in I])
    else:
        WXX = 0.5 * (Wx[np.ix_(MULT, MULT)] + Wx[np.ix_(MULT, MULT)].T)
        WXXi = np.linalg.inv(WXX)
        cnd = float(np.linalg.cond(WXX))
        sb = lambda M, I, J: M[np.ix_(I, J)]
    CX = sb(Cx, DYN, MULT)
    K3 = sb(Kx, DYN, DYN) + CX * WXXi * CX.T if lib == 'mp' else \
        sb(Kx, DYN, DYN) + CX @ WXXi @ CX.T
    if lib == 'mp':
        C3 = sb(Cx, DYN, DYN) - CX * WXXi * sb(Wx, MULT, DYN)
        W3 = sb(Wx, DYN, DYN) - sb(Wx, DYN, MULT) * WXXi * sb(Wx, MULT, DYN)
    else:
        C3 = sb(Cx, DYN, DYN) - CX @ WXXi @ sb(Wx, MULT, DYN)
        W3 = sb(Wx, DYN, DYN) - sb(Wx, DYN, MULT) @ WXXi @ sb(Wx, MULT, DYN)
    for j in range(3):
        K3[0, j] = 0
        K3[j, 0] = 0
    return K3, C3, W3, cnd


def e2(K3, C3, W3, Cd3, lib):
    if lib == 'mp':
        Kx, Cx, Wx = mp.matrix(K3), mp.matrix(C3), mp.matrix(W3)
    else:
        Kx, Cx, Wx = K3.copy(), C3.copy(), W3.copy()
    for j in range(3):
        cij, cd = C3[0, j], Cd3[0, j]
        if j == 0:
            Wx[0, 0] += cd
        else:
            Wx[0, j] += cd
            Wx[j, 0] += cd
            Cx[j, 0] -= cij
    for j in range(3):
        Cx[0, j] = 0
    W00 = Wx[0, 0]
    keep = [1, 2]
    if lib == 'mp':
        K2, C2, W2 = mp.zeros(2, 2), mp.zeros(2, 2), mp.zeros(2, 2)
    else:
        K2, C2, W2 = (np.zeros((2, 2)), np.zeros((2, 2)), np.zeros((2, 2)))
    for ii, i in enumerate(keep):
        for jj, j in enumerate(keep):
            K2[ii, jj] = Kx[i, j] + Cx[i, 0] * Cx[j, 0] / W00
            C2[ii, jj] = Cx[i, j] - Cx[i, 0] * Wx[0, j] / W00
            W2[ii, jj] = Wx[i, j] - Wx[i, 0] * Wx[0, j] / W00
    return K2, C2, W2


def cs2(a0, kh, lib, usa_D, dps=None):
    """c_s^2 (metrico, espectador) em a = a0, modo kh.

    Trilha parametrizada por N = ln a (como o canal float64 original);
    r em cada ponto vem de Newton sobre a cubica. Derivadas em N por
    estencil central de 8a ordem; d/dt = H d/dN.
    """
    antigo = mp.mp.dps
    if lib == 'mp':
        mp.mp.dps = dps or 60
    try:
        hN = mp.mpf('1e-3') if lib == 'mp' else 1e-3
        lg = mp.log if lib == 'mp' else np.log
        ex = mp.exp if lib == 'mp' else np.exp
        N0 = lg(a0)
        Ns = [N0 + (i - 2 * M8) * hN for i in range(4 * M8 + 1)]
        rs, avs = [], []
        chute = None
        for N in Ns:
            av = ex(N)
            rv = r_de_a(av, chute)
            chute = rv
            rs.append(rv if lib == 'mp' else float(rv))
            avs.append(av)
        ff = FF_MP if lib == 'mp' else FF_NP
        H0 = ff(rs[2 * M8])[2]
        kc = kh * avs[2 * M8] * H0
        D = dmat(kc, lib, usa_D)
        K3s, C3s, W3s, Hs = [], [], [], []
        cnd = 0.0
        for rv, av in zip(rs, avs):
            args, H, _ = args_de_r(rv, av, kc, lib)
            Ms = []
            for f in (F_MP if lib == 'mp' else F_NP):
                M = f(*args)
                if lib == 'mp':
                    Ms.append(D * mp.matrix(M) * D)
                else:
                    Ms.append(D @ np.array(M, float) @ D)
            K3, C3, W3, c_ = reduz(Ms, lib)
            cnd = max(cnd, c_)
            K3s.append(K3)
            C3s.append(C3)
            W3s.append(W3)
            Hs.append(H)
        K2s, C2s, W2s = [], [], []
        for j in range(2 * M8 + 1):
            c = j + M8
            Cd3 = mp.zeros(3, 3) if lib == 'mp' else np.zeros((3, 3))
            for m, cf in enumerate(D8):
                if cf != 0:
                    Cd3 = Cd3 + C3s[c - M8 + m] * (
                        mp.mpf(cf) if lib == 'mp' else float(cf))
            Cd3 = Cd3 * (Hs[c] / hN)
            K2, C2, W2 = e2(K3s[c], C3s[c], W3s[c], Cd3, lib)
            K2s.append(K2)
            C2s.append(C2)
            W2s.append(W2)
        Cd2 = mp.zeros(2, 2) if lib == 'mp' else np.zeros((2, 2))
        for m, cf in enumerate(D8):
            if cf != 0:
                Cd2 = Cd2 + C2s[m] * (mp.mpf(cf) if lib == 'mp'
                                      else float(cf))
        Cd2 = Cd2 * (H0 / hN)
        c = M8
        om2 = [(Cd2[i, i] + W2s[c][i, i]) / K2s[c][i, i] for i in range(2)]
        kf2 = (kh * H0) ** 2
        return (om2[0] / kf2, om2[1] / kf2, cnd, rs[2 * M8])
    finally:
        if lib == 'mp':
            mp.mp.dps = antigo


mp.mp.dps = 60
PONTOS = [(1000.0, 'era tardia (bem condicionada)'),
          (0.316, 'borda'),
          (0.1, 'r ~ 1.7e-3'),
          (0.01, 'r ~ 1.7e-6 (o ponto do conflito)')]
KHS = [30.0, 100.0, 300.0, 1000.0, 10000.0]

say("")
say("=" * 72)
say("V-TARDIO / comparacao direta: float64+D  vs  mpmath(60)+D")
say("=" * 72)
say(f"    {'a':>8} {'r':>11} {'kh':>7} {'float64+D':>16} "
    f"{'mpmath60+D':>22} {'rel':>9} {'cond':>8}")
for aval, rot in PONTOS:
    for kh in KHS:
        try:
            f64 = cs2(aval, kh, 'np', True)
            m60 = cs2(mp.mpf(aval), mp.mpf(kh), 'mp', True, 60)
        except Exception as e:                      # noqa: BLE001
            say(f"    {aval:8g} {'—':>11} {kh:7g}  erro: {e}")
            continue
        rel = abs(float(m60[0]) - f64[0]) / max(abs(float(m60[0])), 1e-30)
        say(f"    {aval:8g} {float(m60[3]):11.3e} {kh:7g} "
            f"{float(f64[0]):+16.8f} "
            f"{mp.nstr(m60[0], 16):>22} {rel:9.1e} {f64[2]:8.1e}")

say("")
say("=" * 72)
say("V-D: invariancia por reescala diagonal constante (mpmath 60)")
say("=" * 72)
for kh in (30.0, 1000.0):
    com = cs2(mp.mpf('0.01'), mp.mpf(kh), 'mp', True, 60)[0]
    sem = cs2(mp.mpf('0.01'), mp.mpf(kh), 'mp', False, 60)[0]
    say(f"    kh={kh:7g}  com D = {mp.nstr(com, 20)}   sem D = "
        f"{mp.nstr(sem, 20)}   dif rel = "
        f"{mp.nstr(abs(com-sem)/abs(com), 3)}")

say("")
say("=" * 72)
say("V-DEGRAU: o mesmo ponto com precisao crescente (com D)")
say("=" * 72)
say(f"    {'kh':>7} " + " ".join(f"dps={d:<3}".rjust(24)
                                 for d in (16, 20, 30, 60)))
for kh in (30.0, 100.0, 300.0, 1000.0, 10000.0):
    vals = []
    for d in (16, 20, 30, 60):
        try:
            vals.append(mp.nstr(cs2(mp.mpf('0.01'), mp.mpf(kh),
                                    'mp', True, d)[0], 16))
        except Exception:                            # noqa: BLE001
            vals.append('erro')
    say(f"    {kh:7g} " + " ".join(v.rjust(24) for v in vals))

say("")
say("=" * 72)
say("V-CAL2: o calibrador do espectador no ponto do conflito")
say("=" * 72)
for kh in (30.0, 1000.0):
    f64 = cs2(0.01, kh, 'np', True)
    m60 = cs2(mp.mpf('0.01'), mp.mpf(kh), 'mp', True, 60)
    say(f"    kh={kh:7g}  cal(float64) = {f64[1]:.12f}   "
        f"cal(mpmath60) = {mp.nstr(m60[1], 14)}")
say("    NOTA: o espectador dchi nao tem termo giroscopico; C2 e Cdot2")
say("    sao nulos nesse canal. O calibrador portanto NAO tem poder de")
say("    deteccao sobre o canal Cdot nem sobre o condicionamento do")
say("    modo metrico. Declaracao de cegueira do gate.")

os.makedirs(OUTD, exist_ok=True)
with open(os.path.join(OUTD, 'r12e_confronto_canais.txt'), 'w',
          encoding='utf-8') as fh:
    fh.write("\n".join(OUT) + "\n")
say("")
say("saida escrita em auditoria/code/out/r12e_confronto_canais.txt")
