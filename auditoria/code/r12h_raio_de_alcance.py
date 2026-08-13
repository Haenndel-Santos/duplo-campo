# -*- coding: utf-8 -*-
"""
r12h_raio_de_alcance.py — R-12(h): o RAIO DE ALCANCE do Erratum-03.

PERGUNTA. O Erratum-03 (docs/resultado_r12_instrumento_e_cs2.md) mostrou
que Cdot3/Cdot2 por `np.gradient` (2a ordem) corrompe c_s^2 na primeira
casa em a = 0.01 (cond ~ 1e11). A cadeia defeituosa esta em TODA a
cascata R-1..R-12c. A pergunta que decide o que precisa ser refeito e:

    o defeito morde no DOMINIO onde a cascata R-7/R-8 rodou
    (a in [100, 8e4], kh in [0.2, 20], cond ~ 10)?

Dois agravantes a cobrir:
  (i)  nos scripts ANTIGOS (R-1 a R-8b) o proprio Cdot7 tambem e
       np.gradient de 2a ordem — o defeito entra DUAS vezes. Do R-10a
       em diante o Cdot7 passou a ser simbolico (dt_background).
  (ii) as grandezas que sustentam os enunciados do R-7 nao sao c_s^2:
       sao os SINAIS dos autovalores de K2 (no-ghost), o sinal de W00
       (sobrevivencia do vinculo) e os lnA de passagem (banda morta).
       O teste tem de ser sobre elas.

DESENHO (pre-declarado):
  Um unico harness limpo (fundo em forma fechada + mpmath dps=40) com
  tres variantes de Cdot, medidas no MESMO ponto:
    A8 : Cdot7 simbolico + Cdot3/Cdot2 de 8a ordem   (referencia)
    A2 : Cdot7 simbolico + Cdot3/Cdot2 de 2a ordem   (= R-10a..R-12c)
    N2 : Cdot7 de 2a ordem + Cdot3/Cdot2 de 2a ordem (= R-1..R-8b)
  Grade: a in {100, 1000, 1e4, 8e4} (dominio do R-7/R-8) x
         kh in {0.2, 1, 5, 20} (faixa de passagem do R-7b/c),
         mais a in {0.01} x kh = 30 como controle positivo (onde ja
         sabemos que morde).

  Por ponto: cond(W_XX); autovalores de K2 (com SINAL); W00; om2 das
  duas componentes. Desvio relativo de A2 e N2 contra A8.

GATES (pre-declarados):
  G-SINAL : em nenhum ponto do dominio R-7/R-8 o SINAL de um autovalor
            de K2 ou de W00 pode diferir entre A8, A2 e N2. Se diferir,
            os enunciados ESTRUTURAIS do R-7 (no-ghost, W00 nunca cruza
            zero) estao em risco e precisam ser refeitos.
  G-QUANT : desvio relativo maximo de om2 e dos autovalores de K2 no
            dominio R-7/R-8:
              <= 1e-2  -> cascata R-7/R-8 QUANTITATIVAMENTE SEGURA
                          (as margens la sao de 10+ unidades log);
              1e-2..1  -> refazer as tabelas de precisao;
              >= 1     -> refazer os vereditos.
  G-CTRL  : no ponto de controle (a=0.01, kh=30) o desvio TEM de ser
            grande (~1e-2 em om2). Se nao for, o harness nao esta
            reproduzindo o defeito e o teste nao vale.

FRONTEIRA: benchmark beta-constante beta1=1, mesma classe F1 dos
demais. Este script NAO refaz nenhum resultado do R-7; ele so mede se
seria necessario.

Uso: python -u auditoria/code/r12h_raio_de_alcance.py
Saida em auditoria/code/out/r12h_raio_de_alcance.txt
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
B0V, B1V, B2V, B4V, MUV = 1, 1, sp.Rational(-2, 5), sp.Rational(1, 2), 1
ME2V = sp.Rational(1, 2)
UPPV = sp.Rational(3, 10)
RHO0 = sp.Rational(3, 10)
C2ND = [sp.Rational(-1, 2), sp.Integer(0), sp.Rational(1, 2)]
C8TH = [sp.Rational(1, 280), sp.Rational(-4, 105), sp.Rational(1, 5),
        sp.Rational(-4, 5), sp.Integer(0), sp.Rational(4, 5),
        sp.Rational(-1, 5), sp.Rational(4, 105), sp.Rational(-1, 280)]
M = 4                       # meia-largura do estencil de 8a ordem
NPT = 6 * M + 1             # trilha (derivada tripla aninhada)
mp.mp.dps = 40

say("=" * 72)
say("R-12h — raio de alcance do Erratum-03")
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
SUB = {Mg2: 1, m2: 1, rho_s: 0, Fb: 1, Fp: 0, Fpp: 0,
       b0: B0V, b1: B1V, b2: B2V, b3: 0, b4: B4V}
F = [sp.lambdify(LIVRES, X.subs(SUB), modules='mpmath')
     for X in (K7, C7, W7, Cd7)]

rr = sp.Symbol('r', positive=True)
rho_t = ((B4V - 3 * B2V) * rr**2 - 3 * B1V * rr
         + (3 * B2V - B0V) + B1V / rr)
gg = sp.cancel(-3 * rho_t / sp.diff(rho_t, rr))
Vf = B4V + 3 * B2V / rr**2 + B1V / rr**3
HHs = sp.cancel(ME2V * rr**2 * Vf / (3 * MUV))
LLs = sp.cancel(sp.Rational(1, 2) * (2 / rr + sp.diff(Vf, rr) / Vf) * gg)
Hsy = sp.sqrt(HHs)
Hds = sp.cancel(HHs * LLs)
Hfds = sp.cancel((Hds - HHs * gg / rr) / rr)
xids = Hsy * sp.cancel(sp.diff(rr + gg, rr) * gg)
ddt = lambda e: Hsy * sp.cancel(sp.diff(e, rr) * gg)
CAMPOS = [rho_t, sp.cancel(rr + gg), Hsy, sp.cancel(Hsy / rr), Hds,
          Hfds, xids,
          sp.cancel(3 * HHs - ME2V * (B0V + 3 * B1V * rr + 3 * B2V * rr**2)),
          ddt(Hds), ddt(Hfds), ddt(xids)]
FF = sp.lambdify(rr, CAMPOS, modules='mpmath')
FR = sp.lambdify(rr, rho_t, modules='mpmath')
FDR = sp.lambdify(rr, sp.diff(rho_t, rr), modules='mpmath')
say("    prontas")


def r_de_a(aval, chute=None):
    alvo = mp.mpf(RHO0) * mp.mpf(aval)**-3 / mp.mpf(ME2V)
    x = chute if chute is not None else (
        mp.mpf(1) / alvo if alvo > 10 else mp.mpf('0.3'))
    for _ in range(400):
        dx = (FR(x) - alvo) / FDR(x)
        nx = x - dx
        if nx <= 0:
            nx = x / 2
        x = nx
        if abs(dx) < abs(x) * mp.mpf(10)**(-mp.mp.dps + 6):
            break
    return x


def sb(X, I, J):
    return mp.matrix([[X[i, j] for j in J] for i in I])


def e1(K, C, W, Cd):
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
    K2 = (K2 + K2.T) * mp.mpf('0.5')
    W2 = (W2 + W2.T) * mp.mpf('0.5')
    return K2, C2, W2, W00


def deriv(vals, c, centro, h, Hval):
    m = (len(c) - 1) // 2
    out = mp.zeros(vals[0].rows, vals[0].cols)
    for q, cf in enumerate(c):
        if cf != 0:
            out = out + vals[centro - m + q] * mp.mpf(cf)
    return out * (Hval / h)


def ponto(aval, kh, modo, hN=mp.mpf('1e-3')):
    """modo: 'A8', 'A2', 'N2'."""
    coef = C8TH if modo == 'A8' else C2ND
    cd7_num = (modo == 'N2')
    Ns = [mp.log(mp.mpf(aval)) + (i - 3 * M) * hN for i in range(NPT)]
    rs, avs, chute = [], [], None
    for N in Ns:
        av = mp.e**N
        rv = r_de_a(av, chute)
        chute = rv
        rs.append(rv)
        avs.append(av)
    c0 = 3 * M
    H0 = FF(rs[c0])[2]
    kc = kh * avs[c0] * H0
    D = mp.diag([mp.mpf(1), 1 / kc, mp.mpf(1), mp.mpf(1), 1 / kc,
                 1 / kc**2, mp.mpf(1)])
    Ks, Cs, Ws, Cds, Hs = [], [], [], [], []
    for rv, av in zip(rs, avs):
        v = FF(rv)
        args = (av, rv * av, v[1], v[2], v[3], v[4], v[5], v[6],
                mp.mpf(0), mp.mpf(0), v[7], mp.mpf(0), mp.mpf(UPPV), kc,
                mp.mpf(MUV), mp.mpf(ME2V), v[8], v[9], v[10], mp.mpf(0))
        Ms = [D * mp.matrix(f(*args)) * D for f in F]
        Ks.append(Ms[0])
        Cs.append(Ms[1])
        Ws.append(Ms[2])
        Cds.append(Ms[3])
        Hs.append(v[2])
    # Cdot7: simbolico ou numerico (2a ordem), conforme o modo
    idx1 = range(M, NPT - M) if not cd7_num else range(1, NPT - 1)
    K3s, C3s, W3s, cnd = {}, {}, {}, 0.0
    for c in range(M, NPT - M):
        cd7 = Cds[c] if not cd7_num else deriv(Cs, C2ND, c, hN, Hs[c])
        K3, C3, W3, cc = e1(Ks[c], Cs[c], Ws[c], cd7)
        cnd = max(cnd, cc)
        K3s[c], C3s[c], W3s[c] = K3, C3, W3
    K2s, C2s, W2s, W00s = {}, {}, {}, {}
    m = (len(coef) - 1) // 2
    for c in range(2 * M, NPT - 2 * M):
        seq = [C3s[j] for j in range(c - m, c + m + 1)]
        Cd3 = deriv(seq, coef, m, hN, Hs[c])
        K2, C2, W2, W00 = e2(K3s[c], C3s[c], W3s[c], Cd3)
        K2s[c], C2s[c], W2s[c], W00s[c] = K2, C2, W2, W00
    seq = [C2s[j] for j in range(c0 - m, c0 + m + 1)]
    Cd2 = deriv(seq, coef, m, hN, Hs[c0])
    om2 = [(Cd2[i, i] + W2s[c0][i, i]) / K2s[c0][i, i] for i in range(2)]
    lam = mp.eigsy(mp.matrix(K2s[c0]), eigvals_only=True)
    return dict(om2=om2, lam=[lam[0], lam[1]], W00=W00s[c0], cond=cnd,
                r=rs[c0], H=H0)


def rel(x, y):
    return float(abs(x - y) / max(abs(y), mp.mpf('1e-300')))


GRADE = [(a, kh) for a in ('100', '1000', '10000', '80000')
         for kh in (0.2, 1.0, 5.0, 20.0)]
CTRL = [('0.01', 30.0)]

say("")
say("=" * 72)
say("DOMINIO R-7/R-8  (a in [100, 8e4], kh in [0.2, 20])")
say("=" * 72)
say(f"    {'a':>7} {'kh':>5} {'cond':>8} {'lamK2 min (A8)':>17} "
    f"{'sinais A8/A2/N2':>17} {'d(om2) A2':>10} {'d(om2) N2':>10} "
    f"{'d(lam) N2':>10}")
piores = {'om2_A2': 0.0, 'om2_N2': 0.0, 'lam_A2': 0.0, 'lam_N2': 0.0,
          'W00_N2': 0.0}
sinal_ok = True
for aval, kh in GRADE:
    try:
        r8 = ponto(aval, mp.mpf(kh), 'A8')
        r2 = ponto(aval, mp.mpf(kh), 'A2')
        rn = ponto(aval, mp.mpf(kh), 'N2')
    except Exception as e:                            # noqa: BLE001
        say(f"    {aval:>7} {kh:5g}  erro: {str(e)[:50]}")
        continue
    sg = lambda d: ''.join('+' if x > 0 else '-'
                           for x in (d['lam'][0], d['lam'][1], d['W00']))
    s8, s2, sn = sg(r8), sg(r2), sg(rn)
    if not (s8 == s2 == sn):
        sinal_ok = False
    d_om2_A2 = max(rel(r2['om2'][i], r8['om2'][i]) for i in range(2))
    d_om2_N2 = max(rel(rn['om2'][i], r8['om2'][i]) for i in range(2))
    d_lam_A2 = max(rel(r2['lam'][i], r8['lam'][i]) for i in range(2))
    d_lam_N2 = max(rel(rn['lam'][i], r8['lam'][i]) for i in range(2))
    d_w00 = rel(rn['W00'], r8['W00'])
    piores['om2_A2'] = max(piores['om2_A2'], d_om2_A2)
    piores['om2_N2'] = max(piores['om2_N2'], d_om2_N2)
    piores['lam_A2'] = max(piores['lam_A2'], d_lam_A2)
    piores['lam_N2'] = max(piores['lam_N2'], d_lam_N2)
    piores['W00_N2'] = max(piores['W00_N2'], d_w00)
    say(f"    {aval:>7} {kh:5g} {r8['cond']:8.1e} "
        f"{mp.nstr(min(r8['lam']), 8):>17} {s8+'/'+s2+'/'+sn:>17} "
        f"{d_om2_A2:10.1e} {d_om2_N2:10.1e} {d_lam_N2:10.1e}")

say("")
say("=" * 72)
say("G-CTRL — controle positivo (onde ja sabemos que morde)")
say("=" * 72)
for aval, kh in CTRL:
    r8 = ponto(aval, mp.mpf(kh), 'A8')
    r2 = ponto(aval, mp.mpf(kh), 'A2')
    rn = ponto(aval, mp.mpf(kh), 'N2')
    kf2 = (mp.mpf(kh) * r8['H'])**2
    say(f"    a={aval} kh={kh:g} cond={r8['cond']:.1e}")
    say(f"      c_s^2:  A8 = {mp.nstr(r8['om2'][0]/kf2, 12)} | "
        f"A2 = {mp.nstr(r2['om2'][0]/kf2, 12)} | "
        f"N2 = {mp.nstr(rn['om2'][0]/kf2, 12)}")
    d = max(rel(r2['om2'][0], r8['om2'][0]), rel(rn['om2'][0], r8['om2'][0]))
    ctrl_ok = d > 1e-3
    say(f"      desvio relativo maximo = {d:.1e}  -> controle "
        f"{'OK' if ctrl_ok else 'FALHOU (harness nao reproduz o defeito)'}")

say("")
say("=" * 72)
say("FRONTEIRA EM kh NA ERA TARDIA (a = 1000) — onde o defeito volta")
say("=" * 72)
say("    (o R-7b/c passa kh de 20 a 0.2, mas o R-9a Parte B foi ate")
say("     kh = 1000; a fronteira nao e so em a)")
say(f"    {'kh':>7} {'c_s^2 A8':>18} {'c_s^2 A2':>18} {'c_s^2 N2':>18} "
    f"{'d(om2) A2':>10}")
kh_seguro = None
for kh in (20.0, 30.0, 100.0, 300.0, 1000.0):
    r8 = ponto('1000', mp.mpf(kh), 'A8')
    r2 = ponto('1000', mp.mpf(kh), 'A2')
    rn = ponto('1000', mp.mpf(kh), 'N2')
    kf2 = (mp.mpf(kh) * r8['H'])**2
    d = rel(r2['om2'][0], r8['om2'][0])
    if d <= 1e-2:
        kh_seguro = kh
    say(f"    {kh:7g} {mp.nstr(r8['om2'][0]/kf2, 12):>18} "
        f"{mp.nstr(r2['om2'][0]/kf2, 12):>18} "
        f"{mp.nstr(rn['om2'][0]/kf2, 12):>18} {d:10.1e}")
say("")
say(f"    -> na era tardia o defeito fica abaixo de 1e-2 ate kh ~ "
    f"{kh_seguro:g}; acima disso morde.")
say("    Consequencia: as passagens do R-7b/c (kh 20 -> 0.2) estao")
say("    dentro da regiao segura; a Parte B do R-9a (kh ate 1000) NAO.")

say("")
say("=" * 72)
say("VEREDITO R-12h")
say("=" * 72)
say(f"  [G-SINAL] sinais de (lamK2_1, lamK2_2, W00) identicos nas tres")
say(f"            variantes em todo o dominio R-7/R-8: "
    f"{'SIM' if sinal_ok else 'NAO'}")
if sinal_ok:
    say("            -> os enunciados ESTRUTURAIS do R-7 (no-ghost;")
    say("               W00 nunca cruza zero) NAO dependem do defeito.")
else:
    say("            -> ALERTA: algum sinal muda; refazer o R-7a/R-7f.")
say("")
say(f"  [G-QUANT] desvio relativo maximo no dominio R-7/R-8:")
say(f"            om2  : A2 = {piores['om2_A2']:.1e} | "
    f"N2 = {piores['om2_N2']:.1e}")
say(f"            lamK2: A2 = {piores['lam_A2']:.1e} | "
    f"N2 = {piores['lam_N2']:.1e}")
say(f"            W00  : N2 = {piores['W00_N2']:.1e}")
pior = max(piores.values())
if pior <= 1e-2:
    say(f"            pior = {pior:.1e} <= 1e-2 -> a cascata R-7/R-8 e")
    say("            QUANTITATIVAMENTE SEGURA (as margens la sao de 10+")
    say("            unidades log). Nao ha o que refazer por este motivo.")
elif pior < 1:
    say(f"            pior = {pior:.1e} -> refazer as TABELAS de precisao")
    say("            do R-7/R-8 (vereditos provavelmente intactos).")
else:
    say(f"            pior = {pior:.1e} -> refazer os VEREDITOS.")

os.makedirs(OUTD, exist_ok=True)
with open(os.path.join(OUTD, 'r12h_raio_de_alcance.txt'), 'w',
          encoding='utf-8') as fh:
    fh.write("\n".join(OUT) + "\n")
say("")
say("saida escrita em auditoria/code/out/r12h_raio_de_alcance.txt")
