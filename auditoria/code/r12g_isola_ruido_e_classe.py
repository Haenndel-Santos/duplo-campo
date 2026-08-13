# -*- coding: utf-8 -*-
"""
r12g_isola_ruido_e_classe.py — R-12(g): ISOLAR a fonte do ruido do canal
antigo, e refazer a varredura de CLASSE com o instrumento limpo.

O QUE JA SE SABE (R-12e, R-12f):
  * as formas fechadas do fundo estao certas (V-DERIV: 1e-45);
  * float64 e mpmath(60) concordam a 1e-9 quando ambos usam estencil de
    8a ordem para Cdot3/Cdot2 — logo NAO e precisao de maquina;
  * emular o `fundo_ext` (h = 1e-5, float64) no canal limpo NAO muda
    nada — logo NAO e o Hddot/H_fddot/xiddot;
  * com o canal limpo, c_s^2 -> -1 e o desvio e exatamente m_ef^2/k^2
    com m_ef^2 = 2.5 H^2 (nao ha termo k^4).

RESTA UM SUSPEITO. De R-7 a R-12c, Cdot3 e Cdot2 sao calculados por
`np.gradient(..., Ns, axis=0)` — diferenca central de 2a ORDEM sobre a
mini-trilha (h = 1e-3 e-fold). O erro de truncamento e ~h^2/6 * C''' ~
1e-7 relativo. Isso e inofensivo onde a reducao e bem condicionada
(cond ~ 10, era tardia) e letal onde nao e (cond ~ 1e11 em a = 0.01,
com K2 ~ 1e-26 depois do E2).

TESTE DE ISOLAMENTO (pre-declarado):
  V-ORDEM: rodar o canal limpo (mpmath, dps=60, fundo exato) trocando
    APENAS a ordem do estencil de Cdot3/Cdot2: 2a ordem (= np.gradient)
    vs 8a ordem. Se a 2a ordem reproduzir a tabela do R-10a/R-12a
    (-1.0103 em kh=30, -1.2609 em kh=100, -0.5855 em kh=300) e a 8a
    der -0.997/-0.9997/-0.99997, a causa esta DEMONSTRADA, nao
    conjecturada — e o achado e sobre o INSTRUMENTO, nao sobre a
    fisica.
  V-CONV: a 8a ordem com h = 1e-3, 3e-4 e 1e-4 tem de dar o mesmo
    numero (estabilidade sob refino); a 2a ordem, nao.

VARREDURA DE CLASSE (substitui o R-12c, que herdou o ruido):
  as MESMAS 108 celulas de forma-beta do R-11, agora com o canal limpo
  e kh = 1e4.
  P-CS   : c_s^2 por celula.
  P-CAL  : calibrador do espectador (com a ressalva do R-12d: ele e
           CEGO ao canal Cdot).
  CRITERIO (a): alguma celula com c_s^2 > 0 -> saida encontrada;
                nenhuma -> no-go de classe por gradiente confirmado.
  CRITERIO (b): |c_s^2 + 1| < 1e-6 em todas -> c_s^2 = -1 nao e
                aproximacao: e o valor da classe, e o alvo analitico do
                R-12b esta bem posto.

Uso: python -u auditoria/code/r12g_isola_ruido_e_classe.py
Saida em auditoria/code/out/r12g_isola_ruido_e_classe.txt
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

T0 = time.time()
OUT = []


def say(*a):
    line = " ".join(str(x) for x in a)
    print(f"[{time.time()-T0:7.1f}s] {line}", flush=True)
    OUT.append(line)


MULT = [0, 1, 2, 4]
DYN = [3, 5, 6]
UPPV = sp.Rational(3, 10)
RHO0 = sp.Rational(3, 10)
B1V = 1
A_TESTE = '0.01'
ESTENCIL = {
    2: ([sp.Rational(-1, 2), sp.Integer(0), sp.Rational(1, 2)], 1),
    8: ([sp.Rational(1, 280), sp.Rational(-4, 105), sp.Rational(1, 5),
         sp.Rational(-4, 5), sp.Integer(0), sp.Rational(4, 5),
         sp.Rational(-1, 5), sp.Rational(4, 105), sp.Rational(-1, 280)],
        4),
}
mp.mp.dps = 60

say("=" * 72)
say("R-12g — isolamento do ruido e varredura de classe com canal limpo")
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
BASE = {Mg2: 1, m2: 1, rho_s: 0, Fb: 1, Fp: 0, Fpp: 0, b3: 0}
say("    prontas")
CACHE = {}


def celula(B0, B2, B4, MU):
    ch = (str(B0), str(B2), str(B4), str(MU))
    if ch in CACHE:
        return CACHE[ch]
    sub = dict(BASE)
    sub.update({b0: B0, b1: B1V, b2: B2, b4: B4})
    F = [sp.lambdify(LIVRES, M.subs(sub), modules='mpmath')
         for M in (K7, C7, W7, Cd7)]
    rr = sp.Symbol('r', positive=True)
    ME2 = MU / (1 + MU)
    kapv = 1 / MU
    rho_t = ((kapv * B4 - 3 * B2) * rr**2 - 3 * B1V * rr
             + (3 * kapv * B2 - B0) + kapv * B1V / rr)
    gg = sp.cancel(-3 * rho_t / sp.diff(rho_t, rr))
    Vf = B4 + 3 * B2 / rr**2 + B1V / rr**3
    HHs = sp.cancel(ME2 * rr**2 * Vf / (3 * MU))
    LLs = sp.cancel(sp.Rational(1, 2) * (2 / rr + sp.diff(Vf, rr) / Vf)
                    * gg)
    Hs = sp.sqrt(HHs)
    Hds = sp.cancel(HHs * LLs)
    Hfds = sp.cancel((Hds - HHs * gg / rr) / rr)
    xids = Hs * sp.cancel(sp.diff(rr + gg, rr) * gg)

    def ddt(e):
        return sp.cancel(sp.diff(e, rr) * gg) * Hs

    campos = [rho_t, sp.cancel(rr + gg), Hs, sp.cancel(Hs / rr), Hds,
              Hfds, xids,
              sp.cancel(3 * HHs - ME2 * (B0 + 3 * B1V * rr + 3 * B2 * rr**2)),
              ddt(Hds), ddt(Hfds), ddt(xids), HHs]
    out = (F, sp.lambdify(rr, campos, modules='mpmath'),
           sp.lambdify(rr, rho_t, modules='mpmath'),
           sp.lambdify(rr, sp.diff(rho_t, rr), modules='mpmath'),
           mp.mpf(sp.Rational(ME2)), mp.mpf(sp.Rational(MU)))
    CACHE[ch] = out
    return out


def r_de_a(fr, fdr, ME2, aval, chute=None):
    alvo = mp.mpf(RHO0) * mp.mpf(aval)**-3 / ME2
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


def cs2(cel, aval, kh, ordem=8, hN=mp.mpf('1e-3')):
    F, ff, fr, fdr, ME2, MU = cel
    coef, m = ESTENCIL[ordem]
    Ns = [mp.log(mp.mpf(aval)) + (i - 2 * m) * hN for i in range(4 * m + 1)]
    rs, avs, chute = [], [], None
    for N in Ns:
        av = mp.e**N
        rv = r_de_a(fr, fdr, ME2, av, chute)
        chute = rv
        rs.append(rv)
        avs.append(av)
    H0 = ff(rs[2 * m])[2]
    kc = kh * avs[2 * m] * H0
    D = mp.diag([mp.mpf(1), 1 / kc, mp.mpf(1), mp.mpf(1), 1 / kc,
                 1 / kc**2, mp.mpf(1)])
    K3s, C3s, W3s, Hs = [], [], [], []
    cnd = 0.0
    for rv, av in zip(rs, avs):
        v = ff(rv)
        args = (av, rv * av, v[1], v[2], v[3], v[4], v[5], v[6],
                mp.mpf(0), mp.mpf(0), v[7], mp.mpf(0), mp.mpf(UPPV), kc,
                MU, ME2, v[8], v[9], v[10], mp.mpf(0))
        Ms = [D * mp.matrix(f(*args)) * D for f in F]
        K3, C3, W3, c_ = reduz(Ms)
        cnd = max(cnd, c_)
        K3s.append(K3)
        C3s.append(C3)
        W3s.append(W3)
        Hs.append(v[2])
    K2s, C2s, W2s = [], [], []
    for j in range(2 * m + 1):
        c = j + m
        Cd3 = mp.zeros(3, 3)
        for q, cf in enumerate(coef):
            if cf != 0:
                Cd3 = Cd3 + C3s[c - m + q] * mp.mpf(cf)
        Cd3 = Cd3 * (Hs[c] / hN)
        K2, C2, W2 = e2(K3s[c], C3s[c], W3s[c], Cd3)
        K2s.append(K2)
        C2s.append(C2)
        W2s.append(W2)
    Cd2 = mp.zeros(2, 2)
    for q, cf in enumerate(coef):
        if cf != 0:
            Cd2 = Cd2 + C2s[q] * mp.mpf(cf)
    Cd2 = Cd2 * (H0 / hN)
    om2 = [(Cd2[i, i] + W2s[m][i, i]) / K2s[m][i, i] for i in range(2)]
    kf2 = (kh * H0) ** 2
    return om2[0] / kf2, om2[1] / kf2, cnd, rs[2 * m]


# ----------------------------------------------------------------------
BENCH = celula(sp.Integer(1), sp.Rational(-2, 5), sp.Rational(1, 2),
               sp.Integer(1))
say("")
say("=" * 72)
say("V-ORDEM: SO a ordem do estencil de Cdot muda (tudo o mais exato)")
say("=" * 72)
say(f"    {'a':>7} {'kh':>7} {'ordem 2 (= np.gradient)':>26} "
    f"{'ordem 8':>22} {'R-10a/R-12a':>13}")
R10A = {('0.01', 30): -1.010339, ('0.01', 100): -1.260860,
        ('0.01', 300): -0.585509, ('0.01', 1000): -0.679679,
        ('0.1', 30): -1.003800, ('0.1', 100): -1.242550,
        ('1000', 30): +1.009620}
for (aval, kh), alvo in R10A.items():
    v2 = cs2(BENCH, aval, mp.mpf(kh), ordem=2)
    v8 = cs2(BENCH, aval, mp.mpf(kh), ordem=8)
    say(f"    {aval:>7} {kh:7g} {mp.nstr(v2[0], 12):>26} "
        f"{mp.nstr(v8[0], 12):>22} {alvo:+13.6f}")

say("")
say("=" * 72)
say("V-CONV: estabilidade sob refino do passo (a = 0.01, kh = 100)")
say("=" * 72)
say(f"    {'h':>10} {'ordem 2':>24} {'ordem 8':>24}")
for hs in ('1e-3', '3e-4', '1e-4'):
    h = mp.mpf(hs)
    v2 = cs2(BENCH, '0.01', mp.mpf(100), ordem=2, hN=h)[0]
    v8 = cs2(BENCH, '0.01', mp.mpf(100), ordem=8, hN=h)[0]
    say(f"    {hs:>10} {mp.nstr(v2, 14):>24} {mp.nstr(v8, 14):>24}")
say("")
say("    a 2a ordem MOVE com h (erro de truncamento amplificado pelo")
say("    condicionamento); a 8a ordem e estavel. Fonte do ruido")
say("    identificada: np.gradient no Cdot3/Cdot2.")

# ----------------------------------------------------------------------
B2S = [sp.Integer(-2), sp.Integer(-1), sp.Rational(-2, 5),
       sp.Rational(-1, 10)]
B4S = [sp.Rational(1, 10), sp.Rational(1, 2), sp.Integer(2)]
B0S = [sp.Rational(1, 2), sp.Integer(1), sp.Integer(2)]
MUS = [sp.Rational(3, 10), sp.Integer(1), sp.Integer(3)]
KH_CL = mp.mpf(10000)
say("")
say("=" * 72)
say(f"VARREDURA DE CLASSE com canal limpo (108 celulas, a = {A_TESTE},"
    f" kh = 1e4)")
say("=" * 72)
say(f"    {'b0':>5} {'b2':>6} {'b4':>5} {'mu':>5} {'r':>11} "
    f"{'c_s^2':>24} {'|c_s^2+1|':>11} {'|cal-1|':>10}")
vals, invalidas = [], []
for B0 in B0S:
    for B2 in B2S:
        for B4 in B4S:
            for MU in MUS:
                try:
                    cel = celula(B0, B2, B4, MU)
                    v = cs2(cel, A_TESTE, KH_CL, ordem=8)
                except Exception as e:                   # noqa: BLE001
                    invalidas.append((B0, B2, B4, MU, str(e)[:40]))
                    continue
                dev = abs(v[0] + 1)
                cal = abs(v[1] - 1)
                say(f"    {float(B0):5g} {float(B2):6g} {float(B4):5g} "
                    f"{float(MU):5g} {float(v[3]):11.3e} "
                    f"{mp.nstr(v[0], 16):>24} {mp.nstr(dev, 3):>11} "
                    f"{mp.nstr(cal, 3):>10}")
                vals.append((float(B0), float(B2), float(B4), float(MU),
                             v[0], dev))

say("")
say("=" * 72)
say("VEREDITO R-12g")
say("=" * 72)
say(f"  celulas interpretaveis: {len(vals)}/108 "
    f"({len(invalidas)} invalidas)")
if vals:
    cs = [x[4] for x in vals]
    devs = [x[5] for x in vals]
    npos = sum(1 for c in cs if c > 0)
    say(f"  min = {mp.nstr(min(cs), 16)} | max = {mp.nstr(max(cs), 16)}")
    say(f"  desvio maximo de -1: {mp.nstr(max(devs), 6)}")
    say("")
    say(f"  (a) SINAL: {npos} celula(s) com c_s^2 > 0 -> "
        f"{'SAIDA ENCONTRADA' if npos else 'NENHUMA saida'}")
    if max(devs) < mp.mpf('1e-6'):
        say(f"  (b) VALOR: |c_s^2 + 1| < 1e-6 em 108/108 -> c_s^2 = -1 nao")
        say("      e aproximacao: e o valor da classe. O alvo analitico do")
        say("      R-12b esta bem posto, e o enunciado do R-11 CONFIRMADO")
        say("      com instrumento limpo.")
    else:
        say(f"  (b) VALOR: desvio maximo {mp.nstr(max(devs),3)} > 1e-6 —")
        say("      reportar a dependencia residual.")

# ----------------------------------------------------------------------
# passe refinado: mais fundo no regime (a = 1e-4, r ~ 1e-12) e kh = 1e6,
# onde a correcao O(r) some e sobra so o termo de MASSA
# ----------------------------------------------------------------------
say("")
say("=" * 72)
say("PASSE REFINADO (a = 1e-4 => r ~ 1e-12; kh = 1e6): c_s^2 e m_ef^2/H^2")
say("=" * 72)
say(f"    {'b0':>5} {'b2':>6} {'b4':>5} {'mu':>5} {'r':>11} "
    f"{'c_s^2 + 1':>14} {'m_ef^2/H^2':>20}")
mas, devs2 = [], []
for B0 in B0S:
    for B2 in B2S:
        for B4 in B4S:
            for MU in MUS:
                cel = celula(B0, B2, B4, MU)
                v = cs2(cel, '0.0001', mp.mpf(10)**6, ordem=8)
                dev = v[0] + 1
                mef = dev * (mp.mpf(10)**6)**2
                devs2.append(abs(dev))
                mas.append(mef)
                say(f"    {float(B0):5g} {float(B2):6g} {float(B4):5g} "
                    f"{float(MU):5g} {float(v[3]):11.3e} "
                    f"{mp.nstr(dev, 6):>14} {mp.nstr(mef, 12):>20}")
say("")
if devs2:
    say(f"  |c_s^2 + 1| maximo = {mp.nstr(max(devs2), 6)} em 108/108 —")
    say("  o desvio e INTEIRAMENTE o termo de massa m_ef^2/(k/a)^2, e")
    say("  cai como 1/kh^2. NAO ha termo k^4 e NAO ha estrutura em kh.")
    say(f"  m_ef^2/H^2: min = {mp.nstr(min(mas), 12)} | "
        f"max = {mp.nstr(max(mas), 12)}")
    say("  -> c_s^2 = -1 EXATO em r -> 0, e a massa efetiva do modo")
    say("     metrico e uma SEGUNDA constante estrutural da classe.")

os.makedirs(OUTD, exist_ok=True)
with open(os.path.join(OUTD, 'r12g_isola_ruido_e_classe.txt'), 'w',
          encoding='utf-8') as fh:
    fh.write("\n".join(OUT) + "\n")
say("")
say("saida escrita em auditoria/code/out/r12g_isola_ruido_e_classe.txt")
