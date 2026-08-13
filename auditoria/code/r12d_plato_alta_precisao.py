# -*- coding: utf-8 -*-
"""
r12d_plato_alta_precisao.py — R-12(d): o PLATO sub-horizonte medido em
ALTA PRECISAO, como segundo canal (V-XREP) do R-12b simbolico.

MOTIVO. O R-12c fixou o plato em -0.6867 com dispersao 4.8e-4 entre
celulas — mas essa dispersao NAO e fisica: e o erro do np.gradient
(diferenca central de 2a ordem sobre 41 pontos, h ~ 1e-3 => erro
relativo ~ 1e-6 amplificado pelo mal-condicionamento). Para (i)
identificar a forma fechada do numero e (ii) decidir se a dispersao
entre celulas e real ou instrumental, e preciso um canal com erro
controlado. Este script troca:
    float64            -> mpmath com mp.dps = 60
    np.gradient (O(h^2)) -> diferenca central de 8a ordem em r
    trilha em ln a      -> parametrizacao EXATA pela raiz r, com
                           a(r) = (rho~(r0)/rho~(r))^(1/3) (que e so
                           rho~ ~ a^-3) e d/dN = g(r) d/dr
    Hddot, H_fddot, xiddot por diferenca finita -> FORMA FECHADA
                           (derivadas simbolicas do fundo em r)

Com dps = 60 e h/r = 1e-3, o erro de truncamento da derivada e ~1e-24
relativo: o unico limite passa a ser o condicionamento, que a
precisao estendida absorve.

MEDIDAS (pre-declaradas):
  D-PLATO: c_s^2 = om2/(k/a)^2 em kh in {1e3, 1e4, 1e5, 1e6, 1e8};
    o plato e o valor em kh = 1e8, e a convergencia e exibida.
  D-CAL  : o espectador tem de dar 1; reporta-se |cal - 1| como barra
    de erro efetiva do canal em cada ponto.
  D-R    : o plato em r = 1e-3, 1e-6, 1e-9, 1e-12 — o limite r -> 0 e
    lido pela estabilizacao dos digitos, nao por ajuste.
  D-CEL  : 4 celulas de forma-beta (incluindo os extremos da grade do
    R-11) — decide se a dispersao 4.8e-4 do R-12c e fisica ou
    instrumental.
  D-ID   : mp.identify sobre o plato, procurando forma fechada
    algebrica de baixo grau.

CRITERIO (pre-declarado):
  Se os platos das 4 celulas coincidirem em >= 8 digitos, a dispersao
  do R-12c e INSTRUMENTAL e o plato e constante de classe em sentido
  forte. Se diferirem em digitos com |cal - 1| pequeno, a dependencia
  e FISICA e tem de ser reportada.

FRONTEIRA: identica a do R-10a/R-11/R-12c.

Requer sympy, mpmath. Uso:
    python -u auditoria/code/r12d_plato_alta_precisao.py
Saida em auditoria/code/out/r12d_plato_alta_precisao.txt
"""
import importlib.util
import os
import sys
import time

import mpmath as mp
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

mp.mp.dps = 60
T0 = time.time()
OUT = []


def say(*a):
    line = " ".join(str(x) for x in a)
    print(f"[{time.time()-T0:7.1f}s] {line}", flush=True)
    OUT.append(line)


MULT = [0, 1, 2, 4]
DYN = [3, 5, 6]
# coeficientes de diferenca central de 8a ordem (m = 4)
D8 = [mp.mpf(1) / 280, mp.mpf(-4) / 105, mp.mpf(1) / 5, mp.mpf(-4) / 5,
      mp.mpf(0), mp.mpf(4) / 5, mp.mpf(-1) / 5, mp.mpf(4) / 105,
      mp.mpf(-1) / 280]
M8 = 4
CELULAS = [
    ('benchmark  ', 1, 1, sp.Rational(-2, 5), sp.Rational(1, 2), 1),
    ('b2=-2,b4=.1', 1, 1, sp.Integer(-2), sp.Rational(1, 10), 1),
    ('b0=2,mu=3  ', 2, 1, sp.Rational(-1, 10), sp.Integer(2), 3),
    ('b0=.5,mu=.3', sp.Rational(1, 2), 1, sp.Integer(-1), sp.Rational(1, 2),
     sp.Rational(3, 10)),
]
KHS = [mp.mpf(10)**e for e in (3, 4, 5, 6, 8)]
RS = [mp.mpf(10)**-e for e in (3, 6, 9, 12)]

say("=" * 72)
say(f"R-12d — plato sub-horizonte em alta precisao (mp.dps = {mp.mp.dps})")
say("=" * 72)

say("[1] montando L2 e as matrizes simbolicas ...")
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
FIXOS = {Mg2: 1, m2: 1, rho_s: 0, Fb: 1, Fp: 0, Fpp: 0}
say("    prontas")


def compila(B0, B1, B2, B4, MU):
    """Devolve (fmats, ffundo) compilados em mpmath para uma celula."""
    sub = dict(FIXOS)
    sub.update({b0: B0, b1: B1, b2: B2, b3: 0, b4: B4})
    fs = [sp.lambdify(LIVRES, M.subs(sub), modules='mpmath')
          for M in (K7, C7, W7, Cd7)]
    # ---- fundo exato como funcao de r (formas fechadas) ----
    rr = sp.Symbol('r', positive=True)
    kap = sp.Rational(1, 1) / MU
    ME2 = MU / (1 + MU)
    rho_til = ((kap * B4 - 3 * B2) * rr**2 - 3 * B1 * rr
               + (3 * kap * B2 - B0) + kap * B1 / rr)
    gg = sp.cancel(-3 * rho_til / sp.diff(rho_til, rr))
    Vf = B4 + 3 * B2 / rr**2 + B1 / rr**3
    HH = sp.cancel(ME2 * rr**2 * Vf / (3 * MU))
    LL = sp.cancel(sp.Rational(1, 2) * (2 / rr + sp.diff(Vf, rr) / Vf) * gg)

    def dNr(e):
        return sp.cancel(gg * sp.diff(e, rr))

    H = sp.sqrt(HH)
    Hd = sp.cancel(HH * LL)                       # Hdot
    Hfd = sp.cancel((Hd - HH * gg / rr) / rr)     # H_fdot
    xid = H * dNr(rr + gg)                        # xidot
    Hdd = H * dNr(Hd)
    Hfdd = H * dNr(Hfd)
    xidd = H * sp.cancel(sp.diff(xid, rr) * gg)
    Ubv = sp.cancel(3 * HH - ME2 * (B0 + 3 * B1 * rr + 3 * B2 * rr**2))
    xiv = sp.cancel(rr + gg)
    campos = [rho_til, xiv, H, sp.cancel(H / rr), Hd, Hfd, xid, Ubv,
              Hdd, Hfdd, xidd, HH]
    ff = sp.lambdify(rr, campos, modules='mpmath')
    return fs, ff, float(ME2), float(MU)


def matrizes(fs, ff, rv, r0, rho0, kc, ME2, MU, UPP):
    """K,C,W,Cdot 7x7 (mpmath) no ponto de fundo r = rv da trilha."""
    (rho_til, xiv, H, Hf, Hd, Hfd, xid, Ubv, Hdd, Hfdd, xidd,
     HH) = ff(rv)
    a = (rho0 / rho_til) ** (mp.mpf(1) / 3)
    args = (a, rv * a, xiv, H, Hf, Hd, Hfd, xid, mp.mpf(0), mp.mpf(0),
            Ubv, mp.mpf(0), UPP, kc, mp.mpf(MU), mp.mpf(ME2),
            Hdd, Hfdd, xidd, mp.mpf(0))
    out = []
    for f in fs:
        M = f(*args)
        if isinstance(M, mp.matrix):
            out.append(mp.matrix(M))
        else:
            out.append(mp.matrix([[M[i][j] for j in range(7)]
                                  for i in range(7)]))
    return out


def sub(M, idx, jdx):
    return mp.matrix([[M[i, j] for j in jdx] for i in idx])


def e1(K, C, W, Cd):
    Kx = mp.matrix(K)
    Cx = mp.matrix(C)
    Wx = mp.matrix(W)
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
    WXX = sub(Wx, MULT, MULT)
    WXX = (WXX + WXX.T) * mp.mpf('0.5')
    WXXi = WXX**-1
    CX = sub(Cx, DYN, MULT)
    K3 = sub(Kx, DYN, DYN) + CX * WXXi * CX.T
    C3 = sub(Cx, DYN, DYN) - CX * WXXi * sub(Wx, MULT, DYN)
    W3 = sub(Wx, DYN, DYN) - sub(Wx, DYN, MULT) * WXXi * sub(Wx, MULT, DYN)
    for j in range(3):
        K3[0, j] = 0
        K3[j, 0] = 0
    return K3, C3, W3


def e2(K3, C3, W3, Cd3):
    Kx, Cx, Wx = mp.matrix(K3), mp.matrix(C3), mp.matrix(W3)
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
    K2 = sub(Kx, keep, keep)
    C2 = sub(Cx, keep, keep)
    W2 = sub(Wx, keep, keep)
    for ii, i in enumerate(keep):
        for jj, j in enumerate(keep):
            K2[ii, jj] += Cx[i, 0] * Cx[j, 0] / W00
            C2[ii, jj] -= Cx[i, 0] * Wx[0, j] / W00
            W2[ii, jj] -= Wx[i, 0] * Wx[0, j] / W00
    K2 = (K2 + K2.T) * mp.mpf('0.5')
    W2 = (W2 + W2.T) * mp.mpf('0.5')
    return K2, C2, W2


def deriv(vals, h, g, H):
    """d/dt = H * d/dN = H * g * d/dr, por diferenca central de 8a ordem.

    O fator H e o que o np.gradient(...)*Hs faz no canal float64. Omiti-lo
    NAO e detectado pelo calibrador do espectador: dchi nao tem termo
    giroscopico, logo C2 e Cdot2 sao nulos nesse canal e c_s^2(dchi) = 1
    sai certo de qualquer jeito. Registrado como limite de deteccao do
    calibrador (o gate nao ve o canal Cdot).
    """
    n = vals[0].rows
    out = mp.zeros(n, vals[0].cols)
    for c, v in zip(D8, vals):
        if c != 0:
            out += v * c
    return out * (H * g / h)


def cs2(fs, ff, r0, kh, ME2, MU, UPP=mp.mpf('0.3')):
    """c_s^2 do modo metrico e do espectador em r0, no modo kh."""
    h = r0 * mp.mpf('1e-3')
    rho0 = ff(r0)[0]
    H0 = ff(r0)[2]
    kc = kh * H0                          # a(r0) = 1 por construcao
    # grade de 17 pontos (derivada aninhada: C3 -> Cd3 -> C2 -> Cd2)
    pts = [r0 + (i - 2 * M8) * h for i in range(4 * M8 + 1)]
    K3s, C3s, W3s = [], [], []
    for rv in pts:
        K, C, W, Cd = matrizes(fs, ff, rv, r0, rho0, kc, ME2, MU, UPP)
        K3, C3, W3 = e1(K, C, W, Cd)
        K3s.append(K3)
        C3s.append(C3)
        W3s.append(W3)
    K2s, C2s, W2s = [], [], []
    for j in range(2 * M8 + 1):           # pontos centrais
        c = j + M8
        # d/dt = H g d/dr — Cdot3 pelo mesmo estencil de 8a ordem
        gval = _g(ff, pts[c], h)
        Cd3 = deriv(C3s[c - M8:c + M8 + 1], h, gval, ff(pts[c])[2])
        K2, C2, W2 = e2(K3s[c], C3s[c], W3s[c], Cd3)
        K2s.append(K2)
        C2s.append(C2)
        W2s.append(W2)
    gval0 = _g(ff, r0, h)
    Cd2 = deriv(C2s, h, gval0, H0)
    c = M8
    om2 = [(Cd2[i, i] + W2s[c][i, i]) / K2s[c][i, i] for i in range(2)]
    kf2 = (kh * H0) ** 2
    return om2[0] / kf2, om2[1] / kf2


def _g(ff, rv, h):
    """g(r) = dr/dN = -3 rho~/rho~'  (rho~' por diferenca de 8a ordem)."""
    num = mp.mpf(0)
    for i, cf in enumerate(D8):
        if cf != 0:
            num += cf * ff(rv + (i - M8) * h)[0]
    return -3 * ff(rv)[0] / (num / h)


say("")
resumo = []
for nome, B0, B1, B2, B4, MU in CELULAS:
    fs, ff, ME2, MUf = compila(sp.nsimplify(B0), sp.nsimplify(B1),
                               sp.nsimplify(B2), sp.nsimplify(B4),
                               sp.nsimplify(MU))
    say("=" * 72)
    say(f"CELULA {nome}: b0={B0}, b1={B1}, b2={B2}, b4={B4}, mu={MU}")
    say("=" * 72)
    say(f"    {'r':>10} {'kh':>8} {'c_s^2':>32} {'|cal-1|':>10}")
    for r0 in RS:
        linha = None
        for kh in KHS:
            try:
                et, dc = cs2(fs, ff, r0, kh, ME2, MUf)
            except Exception as e:                       # noqa: BLE001
                say(f"    {mp.nstr(r0,3):>10} {mp.nstr(kh,3):>8}  erro: {e}")
                continue
            cal = abs(dc - 1)
            say(f"    {mp.nstr(r0,3):>10} {mp.nstr(kh,3):>8} "
                f"{mp.nstr(et, 25):>32} {mp.nstr(cal,3):>10}")
            linha = (r0, kh, et, cal)
        if linha:
            resumo.append((nome, linha[0], linha[2], linha[3]))
    say("")

say("=" * 72)
say("RESUMO — plato (kh = 1e8) por celula e por r")
say("=" * 72)
for nome, r0, val, cal in resumo:
    say(f"  {nome}  r={mp.nstr(r0,3):>10}  c_s^2 = {mp.nstr(val, 30)}"
        f"   |cal-1| = {mp.nstr(cal,3)}")

if resumo:
    alvo = resumo[-1][2]
    say("")
    say("[D-ID] identificacao do plato (mp.identify):")
    for cand in (alvo, -alvo, 1 / alvo, alvo**2):
        ident = mp.identify(cand, ['sqrt(2)', 'sqrt(3)', 'sqrt(5)',
                                   'sqrt(6)', 'sqrt(7)'])
        say(f"       {mp.nstr(cand, 25)}  ->  {ident}")
    say("[D-ID] polinomio minimo candidato (pslq sobre 1, x, x^2, x^3):")
    for grau in (2, 3, 4):
        vec = [alvo**i for i in range(grau + 1)]
        rel = mp.pslq(vec, maxcoeff=10**8, maxsteps=10**5)
        say(f"       grau {grau}: {rel}")

os.makedirs(OUTD, exist_ok=True)
with open(os.path.join(OUTD, 'r12d_plato_alta_precisao.txt'), 'w',
          encoding='utf-8') as fh:
    fh.write("\n".join(OUT) + "\n")
say("")
say("saida escrita em auditoria/code/out/r12d_plato_alta_precisao.txt")
