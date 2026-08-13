# -*- coding: utf-8 -*-
"""
r12f_veredito_instrumento.py — R-12(f): VEREDITO sobre o instrumento, e
o perfil de c_s^2 refeito com o fundo em forma fechada.

O QUE O R-12e ACHOU. Os canais float64 e mpmath(60) CONCORDAM (a 1e-9)
quando ambos usam derivadas de fundo em FORMA FECHADA — e nenhum dos
dois reproduz a tabela do R-10a/R-11. A diferenca, portanto, nao e
precisao de maquina: e o calculo de Hddot, H_fddot e xiddot.

A HIPOTESE A TESTAR AQUI. O `fundo_ext` usado de R-10a a R-12c calcula
    Hddot = H*(Hd(a e^h) - Hd(a e^-h))/(2h),  h = 1e-5
por diferenca central em float64. O cancelamento catastrofico desse
passo tem erro relativo ~ eps/(2h) ~ 5e-12 no melhor caso, e MUITO
pior onde Hd ~ 0 (era tardia, onde g -> 0). Esse erro entra em Cdot7 e
e depois amplificado pelo condicionamento da reducao (cond(W_XX) ~
1e11 em a = 0.01). 5e-12 x 1e11 ~ O(1): suficiente para produzir a
"estrutura em kh" do R-12a e o desvio de -1.010 vs -0.997 do R-10a.

GATES (pre-declarados):
  V-DERIV: as formas fechadas de Hddot, H_fddot, xiddot batem com
    diferencas finitas de ALTA ORDEM em mpmath (8a ordem, h = 1e-8,
    dps = 60) em 4 epocas. Este gate e o que autoriza tudo o mais: se
    reprovar, o erro e MEU e nao do repositorio.
  V-RUIDO: reproduzir o `fundo_ext` (h = 1e-5, float64) DENTRO do
    canal de alta precisao, mantendo todo o resto exato. Se isso
    sozinho reproduzir os numeros do R-10a, a causa esta isolada e
    demonstrada, nao apenas conjecturada.
  V-PERFIL: c_s^2(a) e c_s^2(kh) refeitos com o instrumento limpo.
  V-ACROSS: a epoca de troca de sinal a_cross, refeita.

Uso: python -u auditoria/code/r12f_veredito_instrumento.py
Saida em auditoria/code/out/r12f_veredito_instrumento.txt
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
B0V, B2V, B4V, MUV = 1, sp.Rational(-2, 5), sp.Rational(1, 2), 1
ME2V = sp.Rational(1, 2)
UPPV = sp.Rational(3, 10)
RHO0 = sp.Rational(3, 10)
D8C = [sp.Rational(1, 280), sp.Rational(-4, 105), sp.Rational(1, 5),
       sp.Rational(-4, 5), sp.Integer(0), sp.Rational(4, 5),
       sp.Rational(-1, 5), sp.Rational(4, 105), sp.Rational(-1, 280)]
M8 = 4
mp.mp.dps = 60

say("=" * 72)
say("R-12f — veredito sobre o instrumento (fundo em forma fechada)")
say("=" * 72)

say("[1] matrizes simbolicas ...")
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


def monta_celula(B1V):
    sub = {Mg2: 1, m2: 1, rho_s: 0, Fb: 1, Fp: 0, Fpp: 0,
           b0: B0V, b1: B1V, b2: B2V, b3: 0, b4: B4V}
    F = [sp.lambdify(LIVRES, M.subs(sub), modules='mpmath')
         for M in (K7, C7, W7, Cd7)]
    rr = sp.Symbol('r', positive=True)
    kapv = sp.Integer(1) / MUV
    rho_t = ((kapv * B4V - 3 * B2V) * rr**2 - 3 * B1V * rr
             + (3 * kapv * B2V - B0V) + kapv * B1V / rr)
    gg = sp.cancel(-3 * rho_t / sp.diff(rho_t, rr))
    Vf = B4V + 3 * B2V / rr**2 + B1V / rr**3
    HHs = sp.cancel(ME2V * rr**2 * Vf / (3 * MUV))
    LLs = sp.cancel(sp.Rational(1, 2) * (2 / rr + sp.diff(Vf, rr) / Vf)
                    * gg)
    Hs = sp.sqrt(HHs)
    Hds = sp.cancel(HHs * LLs)
    Hfds = sp.cancel((Hds - HHs * gg / rr) / rr)
    xids = Hs * sp.cancel(sp.diff(rr + gg, rr) * gg)

    def ddt(e):                       # d/dt = H * g * d/dr
        return sp.cancel(sp.diff(e, rr) * gg) * Hs

    campos = [rho_t, sp.cancel(rr + gg), Hs, sp.cancel(Hs / rr), Hds,
              Hfds, xids,
              sp.cancel(3 * HHs - ME2V * (B0V + 3 * B1V * rr
                                          + 3 * B2V * rr**2)),
              ddt(Hds), ddt(Hfds), ddt(xids), gg]
    ff = sp.lambdify(rr, campos, modules='mpmath')
    fr = sp.lambdify(rr, rho_t, modules='mpmath')
    fdr = sp.lambdify(rr, sp.diff(rho_t, rr), modules='mpmath')
    return F, ff, fr, fdr


def r_de_a(fr, fdr, aval, chute=None):
    alvo = mp.mpf(RHO0) * mp.mpf(aval)**-3 / mp.mpf(ME2V)
    x = chute if chute is not None else (
        mp.mpf(1) / alvo if alvo > 10 else mp.mpf('0.3'))
    for _ in range(400):
        dx = (fr(x) - alvo) / fdr(x)
        nx = x - dx
        if nx <= 0:
            nx = x / 2
        x = nx
        if abs(dx) < abs(x) * mp.mpf(10)**(-mp.mp.dps + 6):
            break
    return x


# ----------------------------------------------------------------------
# V-DERIV: as formas fechadas contra diferencas de alta ordem em mpmath
# ----------------------------------------------------------------------
F1, FF1, FR1, FDR1 = monta_celula(1)
say("")
say("=" * 72)
say("V-DERIV: forma fechada de Hddot/H_fddot/xiddot vs diferenca de")
say("         8a ordem em mpmath (h = 1e-8 em N, dps = 60)")
say("=" * 72)
say(f"    {'a':>9} {'|dHddot|':>12} {'|dH_fddot|':>12} {'|dxiddot|':>12}")
pior = mp.mpf(0)
for aval in ('1000', '0.316', '0.1', '0.01'):
    av = mp.mpf(aval)
    hN = mp.mpf('1e-8')
    r0 = r_de_a(FR1, FDR1, av)
    base = FF1(r0)
    H0 = base[2]
    fech = [base[8], base[9], base[10]]
    num = [mp.mpf(0)] * 3
    for m, cf in enumerate(D8C):
        if cf == 0:
            continue
        rm = r_de_a(FR1, FDR1, av * mp.e**((m - M8) * hN), r0)
        vv = FF1(rm)
        for q, idx in enumerate((4, 5, 6)):      # Hd, Hfd, xid
            num[q] += mp.mpf(cf) * vv[idx]
    fd = [H0 * x / hN for x in num]
    devs = [abs(fech[q] - fd[q]) / abs(fech[q]) for q in range(3)]
    pior = max(pior, max(devs))
    say(f"    {aval:>9} " + " ".join(f"{mp.nstr(d, 4):>12}" for d in devs))
if pior > mp.mpf('1e-20'):
    say(f"[V-DERIV] REPROVADO — desvio maximo {mp.nstr(pior,3)}. As formas")
    say("          fechadas estao erradas; nada abaixo vale. Abortando.")
    with open(os.path.join(OUTD, 'r12f_veredito_instrumento.txt'), 'w',
              encoding='utf-8') as fh:
        fh.write("\n".join(OUT) + "\n")
    sys.exit(1)
say(f"[V-DERIV] APROVADO — desvio maximo {mp.nstr(pior, 3)}. As formas")
say("          fechadas do fundo estao corretas.")


# ----------------------------------------------------------------------
# pipeline (mpmath), com opcao de emular o fundo_ext em float64
# ----------------------------------------------------------------------
def reduz(Ms):
    K, C, W, Cd = Ms
    Kx, Cx, Wx = mp.matrix(K), mp.matrix(C), mp.matrix(W)
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
    sb = lambda M, I, J: mp.matrix([[M[i, j] for j in J] for i in I])
    WXX = mp.matrix([[(Wx[i, j] + Wx[j, i]) / 2 for j in MULT]
                     for i in MULT])
    WXXi = WXX**-1
    cnd = float(mp.mnorm(WXX) * mp.mnorm(WXXi))
    CX = sb(Cx, DYN, MULT)
    K3 = sb(Kx, DYN, DYN) + CX * WXXi * CX.T
    C3 = sb(Cx, DYN, DYN) - CX * WXXi * sb(Wx, MULT, DYN)
    W3 = sb(Wx, DYN, DYN) - sb(Wx, DYN, MULT) * WXXi * sb(Wx, MULT, DYN)
    for j in range(3):
        K3[0, j] = 0
        K3[j, 0] = 0
    return K3, C3, W3, cnd


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
    K2, C2, W2 = mp.zeros(2, 2), mp.zeros(2, 2), mp.zeros(2, 2)
    for ii, i in enumerate(keep):
        for jj, j in enumerate(keep):
            K2[ii, jj] = Kx[i, j] + Cx[i, 0] * Cx[j, 0] / W00
            C2[ii, jj] = Cx[i, j] - Cx[i, 0] * Wx[0, j] / W00
            W2[ii, jj] = Wx[i, j] - Wx[i, 0] * Wx[0, j] / W00
    return K2, C2, W2


def cs2(F, ff, fr, fdr, aval, kh, ruido=False):
    """c_s^2 (metrico, espectador). ruido=True emula o fundo_ext do
    R-10a: Hddot/H_fddot/xiddot por diferenca central com h = 1e-5
    ARREDONDADA A float64 antes da subtracao."""
    hN = mp.mpf('1e-3')
    av0 = mp.mpf(aval)
    Ns = [mp.log(av0) + (i - 2 * M8) * hN for i in range(4 * M8 + 1)]
    rs, avs, chute = [], [], None
    for N in Ns:
        av = mp.e**N
        rv = r_de_a(fr, fdr, av, chute)
        chute = rv
        rs.append(rv)
        avs.append(av)
    H0 = ff(rs[2 * M8])[2]
    kc = kh * avs[2 * M8] * H0
    D = mp.diag([mp.mpf(1), 1 / kc, mp.mpf(1), mp.mpf(1), 1 / kc,
                 1 / kc**2, mp.mpf(1)])
    K3s, C3s, W3s, Hs = [], [], [], []
    cnd = 0.0
    for rv, av in zip(rs, avs):
        v = ff(rv)
        Hdd, Hfdd, xidd = v[8], v[9], v[10]
        if ruido:
            hh = mp.mpf('1e-5')
            rp = r_de_a(fr, fdr, av * mp.e**hh, rv)
            rm = r_de_a(fr, fdr, av * mp.e**-hh, rv)
            vp, vm = ff(rp), ff(rm)
            f64 = lambda x: mp.mpf(float(x))
            Hdd = f64(v[2]) * (f64(vp[4]) - f64(vm[4])) / (2 * hh)
            Hfdd = f64(v[2]) * (f64(vp[5]) - f64(vm[5])) / (2 * hh)
            xidd = f64(v[2]) * (f64(vp[6]) - f64(vm[6])) / (2 * hh)
        args = (av, rv * av, v[1], v[2], v[3], v[4], v[5], v[6],
                mp.mpf(0), mp.mpf(0), v[7], mp.mpf(0), mp.mpf(UPPV), kc,
                mp.mpf(MUV), mp.mpf(ME2V), Hdd, Hfdd, xidd, mp.mpf(0))
        Ms = [D * mp.matrix(f(*args)) * D for f in F]
        K3, C3, W3, c_ = reduz(Ms)
        cnd = max(cnd, c_)
        K3s.append(K3)
        C3s.append(C3)
        W3s.append(W3)
        Hs.append(v[2])
    K2s, C2s, W2s = [], [], []
    for j in range(2 * M8 + 1):
        c = j + M8
        Cd3 = mp.zeros(3, 3)
        for m, cf in enumerate(D8C):
            if cf != 0:
                Cd3 = Cd3 + C3s[c - M8 + m] * mp.mpf(cf)
        Cd3 = Cd3 * (Hs[c] / hN)
        K2, C2, W2 = e2(K3s[c], C3s[c], W3s[c], Cd3)
        K2s.append(K2)
        C2s.append(C2)
        W2s.append(W2)
    Cd2 = mp.zeros(2, 2)
    for m, cf in enumerate(D8C):
        if cf != 0:
            Cd2 = Cd2 + C2s[m] * mp.mpf(cf)
    Cd2 = Cd2 * (H0 / hN)
    c = M8
    om2 = [(Cd2[i, i] + W2s[c][i, i]) / K2s[c][i, i] for i in range(2)]
    kf2 = (kh * H0) ** 2
    return om2[0] / kf2, om2[1] / kf2, cnd, rs[2 * M8]


# ----------------------------------------------------------------------
say("")
say("=" * 72)
say("V-RUIDO: injetar SO o fundo_ext (h=1e-5, float64) no canal limpo")
say("=" * 72)
say("    (se isto sozinho reproduzir o R-10a, a causa esta isolada)")
say(f"    {'a':>7} {'kh':>7} {'limpo':>16} {'com fundo_ext':>16} "
    f"{'R-10a/R-12a':>13} {'cond':>9}")
R10A = {(0.01, 30): -1.010339, (0.01, 100): -1.260860,
        (0.01, 300): -0.585509, (0.01, 1000): -0.679679,
        (0.1, 30): -1.003800, (0.1, 100): -1.242550,
        (1000.0, 30): +1.009620, (1000.0, 100): +1.009800}
for (aval, kh), alvo in R10A.items():
    lim = cs2(F1, FF1, FR1, FDR1, aval, mp.mpf(kh))
    rui = cs2(F1, FF1, FR1, FDR1, aval, mp.mpf(kh), ruido=True)
    say(f"    {aval:7g} {kh:7g} {mp.nstr(lim[0], 12):>16} "
        f"{mp.nstr(rui[0], 12):>16} {alvo:+13.6f} {lim[2]:9.1e}")

say("")
say("=" * 72)
say("V-PERFIL: c_s^2(kh) com o instrumento limpo, em r -> 0")
say("=" * 72)
say(f"    {'a':>8} {'r':>11} " +
    " ".join(f"kh={kh:g}".rjust(20) for kh in (30, 100, 1000, 10000)))
for aval in ('0.01', '0.001', '0.0001'):
    linha, rv = [], None
    for kh in (30, 100, 1000, 10000):
        v = cs2(F1, FF1, FR1, FDR1, aval, mp.mpf(kh))
        linha.append(mp.nstr(v[0], 16))
        rv = v[3]
    say(f"    {aval:>8} {float(rv):11.3e} " +
        " ".join(x.rjust(20) for x in linha))
say("")
say("    o desvio de -1 escala como 1/kh^2 => om2 = -k^2/a^2 + m_ef^2,")
say("    isto e: c_s^2 = -1 EXATO e o resto e MASSA, nao termo k^4.")
say(f"    {'a':>8} {'m_ef^2/H^2 (de kh=1e3)':>26} {'(de kh=1e4)':>22}")
for aval in ('0.01', '0.001', '0.0001'):
    v3 = cs2(F1, FF1, FR1, FDR1, aval, mp.mpf(1000))[0]
    v4 = cs2(F1, FF1, FR1, FDR1, aval, mp.mpf(10000))[0]
    say(f"    {aval:>8} {mp.nstr((v3 + 1) * 1000**2, 12):>26} "
        f"{mp.nstr((v4 + 1) * 10000**2, 12):>22}")

say("")
say("=" * 72)
say("V-ACROSS: a epoca de troca de sinal, com o instrumento limpo")
say("=" * 72)
say(f"    {'a':>9} {'r':>11} {'c_s^2 (kh=1e4)':>22}")
for aval in ('0.1', '0.316', '0.5', '0.574', '0.7', '1.0', '2.0'):
    v = cs2(F1, FF1, FR1, FDR1, aval, mp.mpf(10000))
    say(f"    {aval:>9} {float(v[3]):11.3e} {mp.nstr(v[0], 14):>22}")


def raiz_across():
    lo, hi = mp.mpf('0.3'), mp.mpf('2.0')
    flo = cs2(F1, FF1, FR1, FDR1, lo, mp.mpf(10000))[0]
    for _ in range(40):
        mid = mp.sqrt(lo * hi)
        fm = cs2(F1, FF1, FR1, FDR1, mid, mp.mpf(10000))[0]
        if (fm < 0) == (flo < 0):
            lo, flo = mid, fm
        else:
            hi = mid
        if hi / lo - 1 < mp.mpf('1e-8'):
            break
    return mp.sqrt(lo * hi)


ac = raiz_across()
say("")
say(f"    a_cross (limpo, kh=1e4) = {mp.nstr(ac, 10)}   "
    f"[R-10b, canal antigo: 0.574]")
say(f"    com a ancora a0 = 0.931 do R-8b: z_cross = "
    f"{mp.nstr(mp.mpf('0.931')/ac - 1, 8)}   [R-10b: 0.62]")

os.makedirs(OUTD, exist_ok=True)
with open(os.path.join(OUTD, 'r12f_veredito_instrumento.txt'), 'w',
          encoding='utf-8') as fh:
    fh.write("\n".join(OUT) + "\n")
say("")
say("saida escrita em auditoria/code/out/r12f_veredito_instrumento.txt")
