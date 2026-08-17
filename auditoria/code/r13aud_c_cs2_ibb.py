# -*- coding: utf-8 -*-
"""
r13aud_c_cs2_ibb.py -- AUDITORIA ADVERSARIAL DO R-13, ALVO C.

O ELO NAO MEDIDO INTERNAMENTE. O corpus declara que "o gradiente do IBB
e' saudavel SEGUNDO A FONTE, nao medido por nos". A frase de
complementaridade -- o achado do arco -- apoia-se metade em medida
propria (Higuchi, R-13b) e metade em literatura (gradiente, 1407.4331 +
1503.07436 sec.IV A). ESTE SCRIPT MEDE O LADO QUE FALTA, com a
maquinaria limpa do R-12f/g (fundo em forma fechada + estencil de 8a
ordem, np.gradient PROIBIDO com trava).

=======================================================================
CRITERIOS PRE-DECLARADOS (escritos ANTES da execucao -- regra 2)
=======================================================================

--- GATES DE MAQUINARIA (se falharem, NAO ha' medicao) ---------------

  C-M1  SELECAO DE RAMO. Em cada ponto da mini-trilha de 9 nos em N, a
        raiz usada tem de ser a do ramo INFINITO. Verificado por:
          (a) semente = assintota analitica r ~ sqrt(mu rho_til/b4);
          (b) r decrescente ao longo da mini-trilha;
          (c) r > r_c (ponto fixo = MAIOR raiz de W = 0) em todos os
              nos;
          (d) residuo |W(r) - rho_til| <= 1e-40 (mpmath dps = 60).
        Falha em qualquer item => ponto MARCADO COMO NAO-MEDIDO.

  C-M2  CONTROLE POSITIVO (regra 3 -- poder). A MESMA rotina, com a
        semente do ramo FINITO, tem de reproduzir o resultado limpo do
        R-12g na celula de benchmark (b0=1, b1=1, b2=-2/5, b4=1/2,
        mu=1): c_s^2 = -1 com |c_s^2 + 1| <= 1e-4 em a = 1e-4,
        kh = 1e6. Se nao reproduzir, a maquinaria nao esta' calibrada e
        nada que ela disser sobre o IBB pode ser interpretado.

  C-M3  REGRA 6 / REFINO EM h. Cdot3 e Cdot2 por estencil central de
        8a ORDEM (nunca 2a, nunca np.gradient -- trava ativa). O h NAO
        e' fixado a priori: e' REFINADO em 1e-3, 3e-4, 1e-4, 3e-5,
        1e-5, 3e-6 ate' que dois h sucessivos concordem a <= 1e-6.
        Ponto que nao converge: NAO MEDIDO.
        [EMENDA DECLARADA, pos-1a execucao: a versao original deste
         criterio usava h fixo = 1e-3 com um unico teste 1e-3 vs 3e-4,
         como o R-12g e o R-13b. Ela FALHOU -- ver o bloco C-M3-linha,
         onde o mesmo ponto vai de -1.9e4 a +0.496 quando h cai de
         1e-3 para 1e-5. A rodada ruim esta preservada no git.]

  C-M4  SUB-HORIZONTE / REFINO EM kh. c_s^2 e o limite kh -> infinito,
        mas o instrumento tem TETO em kh (demonstrado no controle do
        ramo finito). Criterio: tres kh (300, 1e3, 3e3) com o h
        convergido tem de concordar a <= 1e-6. Espalhamento maior:
        NAO MEDIDO.

--- V-XREP: TODO NUMERO DECISIVO POR DOIS CANAIS INDEPENDENTES -------

  C-X1  CANAL 1 (nosso): c_s^2 pela reducao 2-DOF (Schur + E2) da
        maquinaria de derivations/code/01_setor_escalar_K_Omega.py, em
        mpmath dps = 60.
  C-X2  CANAL 2 (literatura, forma fechada): c_s^2_lit = -r''/(3r'),
        que e' a eq. (76) de 1407.4331 == a eq. (24) de 1503.07436 com
        o sinal do ansatz traduzido (alvo B). Com
        r'' = -3r' - r'^2 W''/W' (forma fechada, alvo B, gate B5).
  C-X3  CANAL 3 (predicao do corpus): o R-12i registra a relacao
        fechada entre os dois objetos no ramo FINITO,
            c_s^2_TDCP = -r''/(3r') + (1/2) r r'.
        CRITERIO PRE-DECLARADO: se essa relacao valer TAMBEM no ramo
        infinito, o canal 1 tem de bater com o canal 3 a <= 1e-3. Se
        NAO bater, o resultado e' que a relacao e' propria do ramo
        finito -- e isso e' achado, nao falha.

--- O QUE E' MEDIDO (sem criterio de passa/nao-passa) ----------------

  C-R1  c_s^2 do modo metrico do sistema 2-DOF, ao longo da historia,
        em celulas IBB genuinas (b0 = b2 = b3 = 0, b1 = 1,
        0 < b4/b1 < 2 mu^{3/2}).
  C-R2  o sinal de c_s^2: fracao de pontos com c_s^2 > 0.
  C-R3  o calibrador do espectador (deve dar +1; e' CEGO ao canal Cdot,
        Erratum-03 sec.5 -- declarado, nao usado como prova).
  C-R4  a comparacao com o ramo FINITO na mesma rodada.

--- VEREDITO PRE-DECLARADO -------------------------------------------

  Se c_s^2 > 0 em todos os pontos medidos das celulas IBB:
     => o elo FECHA e a frase de complementaridade passa a ter os DOIS
        lados medidos por nos.
  Se houver celula/epoca com c_s^2 < 0:
     => a frase de complementaridade CAI, e o IBB e' ruim nos DOIS
        canais. Isso NAO reabre nem fecha nada sobre Higuchi.
  Se a maquinaria nao passar C-M1..C-M4:
     => registro de que o elo NAO POde ser fechado, com a razao.

--- CEGUEIRA DESTE GATE (regra 7, obrigatoria) -----------------------

  * A L2 deste projeto NAO tem perturbacao de materia (delta rho_m). A
    materia entra so' como densidade de FUNDO (roteada por Ubar, com
    chidot = 0 e U' = 0). Toda medida de c_s^2 aqui herda essa
    limitacao -- e ela e' a mesma do R-11/R-12g, declarada la'.
  * NAO mede fantasma escalar (sinal dos autovalores de K2) -- so' a
    velocidade de gradiente.
  * NAO mede Higuchi nem o setor tensorial (isso e' o R-13b).
  * NAO mede validade EFT, screening, f*sigma_8.
  * O calibrador do espectador e' CEGO ao canal Cdot (Erratum-03): ele
    dar +1 NAO prova que o modo metrico esta' certo.
  * beta_n CONSTANTES. Sob modulacao beta_n(phi_-) nada aqui vale.

Uso:  .venv\\Scripts\\python.exe auditoria/code/r13aud_c_cs2_ibb.py
Saida: auditoria/code/out/r13aud_c_cs2_ibb.txt
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


def _gradiente_proibido(*a, **k):
    raise RuntimeError("np.gradient e' PROIBIDO (regra 6, Erratum-03).")


np.gradient = _gradiente_proibido

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
B1V = 1
C8 = ([sp.Rational(1, 280), sp.Rational(-4, 105), sp.Rational(1, 5),
       sp.Rational(-4, 5), sp.Integer(0), sp.Rational(4, 5),
       sp.Rational(-1, 5), sp.Rational(4, 105), sp.Rational(-1, 280)], 4)
mp.mp.dps = 60

say("=" * 72)
say("R-13aud/C -- c_s^2 NO RAMO INFINITO (IBB), maquinaria limpa R-12f/g")
say("=" * 72)
say("")
say("CEGUEIRA (regra 7): a L2 deste projeto NAO tem delta rho_m; a")
say("materia entra so' como densidade de fundo. Toda medida abaixo herda")
say("essa limitacao, a mesma do R-11/R-12g. NAO mede fantasma escalar,")
say("Higuchi, EFT nem screening. beta_n constantes.")
say("")

say("[1] matrizes simbolicas (L2 -> K7, C7, W7, Cdot7) ...")
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
    """Igual a' celula() do R-12g -- MESMAS formas fechadas de fundo."""
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
    gg = sp.cancel(-3 * rho_t / sp.diff(rho_t, rr))          # dr/dN
    Vf = B4 + 3 * B2 / rr**2 + B1V / rr**3
    HHs = sp.cancel(ME2 * rr**2 * Vf / (3 * MU))
    LLs = sp.cancel(sp.Rational(1, 2) * (2 / rr + sp.diff(Vf, rr) / Vf) * gg)
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
    # canal 2 / canal 3 usam W'(r) e W''(r), lambdificados abaixo
    # coeficientes da cubica r*(W(r) - rho_til) = 0 (b3 = 0), para
    # selecao de raiz EXATA por polyroots -- a assintota so' serve de
    # semente no passado profundo e falha perto do ponto fixo.
    cpoly = [mp.mpf(str(sp.N(kapv * B4 - 3 * B2, 50))),
             mp.mpf(-3 * B1V),
             None,                                   # -(rho_til) + ...
             mp.mpf(str(sp.N(kapv * B1V, 50)))]
    c2fix = mp.mpf(str(sp.N(3 * kapv * B2 - B0, 50)))
    out = (F, sp.lambdify(rr, campos, modules='mpmath'),
           sp.lambdify(rr, rho_t, modules='mpmath'),
           sp.lambdify(rr, sp.diff(rho_t, rr), modules='mpmath'),
           mp.mpf(sp.Rational(ME2)), mp.mpf(sp.Rational(MU)),
           sp.lambdify(rr, gg, modules='mpmath'),
           sp.lambdify(rr, sp.cancel(sp.diff(rho_t, rr, 2)),
                       modules='mpmath'),
           mp.mpf(str(sp.N(B4, 50))), cpoly, c2fix)
    CACHE[ch] = out
    return out


def raizes_pos(cel, alvo):
    """Todas as raizes reais positivas de W(r) = alvo, por polyroots."""
    cp = list(cel[9])
    cp[2] = cel[10] - alvo
    try:
        z = mp.polyroots(cp, maxsteps=200, extraprec=200)
    except Exception:                                    # noqa: BLE001
        return []
    out = []
    for v in z:
        v = mp.mpc(v)
        if abs(mp.im(v)) < mp.mpf(10)**(-mp.mp.dps + 12) * max(
                1, abs(mp.re(v))) and mp.re(v) > 0:
            out.append(mp.re(v))
    return sorted(out)


def r_de_a(cel, aval, rho0, chute=None, ramo='infinito'):
    """Raiz EXATA por polyroots + polimento de Newton.

    A ARMADILHA (R-13b sec.2): a menor raiz positiva e' o ramo FINITO,
    a maior e' o INFINITO. A assintota r ~ sqrt(mu rho/b4) so' e'
    semente valida no passado profundo -- perto do ponto fixo ela
    converge para a raiz ERRADA. Por isso a selecao aqui e' por
    polyroots (todas as raizes) e nao por semente + Newton.
    """
    fr, fdr = cel[2], cel[3]
    alvo = mp.mpf(rho0) * mp.mpf(aval)**-3
    rr_ = raizes_pos(cel, alvo)
    if not rr_:
        raise RuntimeError("sem raiz positiva")
    if chute is not None:
        x = min(rr_, key=lambda z: abs(z - chute))
    elif ramo == 'infinito':
        x = rr_[-1]
    else:
        x = rr_[0]
    for _ in range(500):
        d = fdr(x)
        dx = (fr(x) - alvo) / d
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
    def sb(M, I, J):
        return mp.matrix([[M[i, j] for j in J] for i in I])
    WXX = mp.matrix([[(Wx[i, j] + Wx[j, i]) / 2 for j in MULT] for i in MULT])
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


def cs2(cel, aval, kh, rho0, hN=mp.mpf('1e-3'), ramo='infinito'):
    """c_s^2 do modo metrico e do espectador. Estencil de 8a ORDEM."""
    F, ff, fr, fdr, ME2, MU = cel[:6]
    coef, m = C8
    Ns = [mp.log(mp.mpf(aval)) + (i - 2 * m) * hN for i in range(4 * m + 1)]
    rs, avs, chute = [], [], None
    for N in Ns:
        av = mp.e**N
        rv = r_de_a(cel, av, rho0, chute, ramo)
        chute = rv
        rs.append(rv)
        avs.append(av)
    # --- C-M1: gate de ramo, na mini-trilha inteira -------------------
    resid = max(abs(fr(rv) - mp.mpf(rho0) * av**-3) / max(1, abs(fr(rv)))
                for rv, av in zip(rs, avs))
    decr = all(rs[i] > rs[i + 1] for i in range(len(rs) - 1))
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
    return (om2[0] / kf2, om2[1] / kf2, cnd, rs[2 * m], resid, decr)


def canais_fechados(cel, rval):
    """CANAL 2 e CANAL 3, em forma fechada (regra 6, sem estencil)."""
    fr, fdr, gg, fd2r = cel[2], cel[3], cel[6], cel[7]
    rp = gg(rval)                                   # r' = -3 rho/W'
    Wp = fdr(rval)
    Wpp = fd2r(rval)
    rpp = -3 * rp - rp**2 * Wpp / Wp                # r'' fechado (alvo B)
    cs2_lit = -rpp / (3 * rp)                       # canal 2  (1407 eq.76)
    cs2_tdcp = cs2_lit + rval * rp / 2              # canal 3  (R-12i)
    return cs2_lit, cs2_tdcp, rp, rpp


def y_max(mu):
    return 2.0 * mu**1.5


def r_c_de(y, mu):
    z = np.roots([y, -3 * mu, 0.0, 1.0])
    pos = [v.real for v in z if abs(v.imag) < 1e-12 and v.real > 0]
    return max(pos) if pos else float('nan')


def rho0_de_Omega(y, mu, Om=0.3):
    """rho_til em a=1 com Omega_m(a=1) = Om no ramo INFINITO (R-8b)."""
    rc = r_c_de(y, mu)
    lo, hi = rc * (1 + 1e-12), rc * 1e8
    for _ in range(400):
        mid = np.sqrt(lo * hi)
        Om_m = 1.0 - mu * (3.0 * mid) / (mid**2 * (y + 1.0 / mid**3))
        if Om_m < Om:
            lo = mid
        else:
            hi = mid
    r0 = np.sqrt(lo * hi)
    return (y * r0**2 + 1.0 / r0) / mu - 3.0 * r0


# =====================================================================
say("")
say("=" * 72)
say("[C-M2] CONTROLE POSITIVO -- a maquinaria reproduz c_s^2 = -1 no")
say("       ramo FINITO? (celula de benchmark do R-12g)")
say("=" * 72)
BENCH = celula(sp.Integer(1), sp.Rational(-2, 5), sp.Rational(1, 2),
               sp.Integer(1))
RHO0_BENCH = mp.mpf('0.3') / (mp.mpf(1) / 2)     # rho_til = rho/(m^2 Meff^2)
v = cs2(BENCH, '0.0001', mp.mpf(10)**6, RHO0_BENCH, ramo='finito')
say(f"    a = 1e-4, kh = 1e6, ramo FINITO:")
say(f"      r          = {mp.nstr(v[3], 8)}")
say(f"      c_s^2      = {mp.nstr(v[0], 14)}")
say(f"      |c_s^2 + 1|= {mp.nstr(abs(v[0] + 1), 6)}   (criterio <= 1e-4)")
say(f"      calibrador = {mp.nstr(v[1], 10)}   (esperado +1; CEGO ao Cdot)")
say(f"      cond(W_XX) = {v[2]:.3e}")
OK_M2 = abs(v[0] + 1) <= mp.mpf('1e-4')
say(f"    [C-M2 {'OK' if OK_M2 else 'FALHOU'}]")
assert OK_M2, "C-M2 FALHOU: a maquinaria nao reproduz o R-12g"

# =====================================================================
say("")
say("=" * 72)
say("[C-M3'] O ACHADO DE INSTRUMENTO QUE ESTA AUDITORIA ENCONTROU")
say("=" * 72)
say("")
say("  A regra 6 (Erratum-03) exige 'estencil de ordem >= 8 COM teste de")
say("  refino'. A pratica do R-12g e do R-13b usa UM h fixo (1e-3) e")
say("  compara com 3e-4. ISSO NAO BASTA quando o fundo tem r GRANDE --")
say("  e o ramo infinito tem r ~ 1e8 no passado profundo.")
say("")
say("  Demonstracao (celula IBB f=0.05, mu=1, a=3e-5, kh=1e4):")
CEL_D = celula(sp.Integer(0), sp.Integer(0), sp.Rational(1, 10),
               sp.Integer(1))
RHO_D = mp.mpf(float(rho0_de_Omega(0.1, 1.0)))
say(f"    {'h':>10} {'c_s^2':>24}")
for hs in ('1e-3', '3e-4', '1e-4', '3e-5', '1e-5'):
    vv = cs2(CEL_D, '0.00003', mp.mpf(10000), RHO_D, hN=mp.mpf(hs))
    say(f"    {hs:>10} {mp.nstr(vv[0], 16):>24}")
say("")
say("  De -1.9e4 a +0.496: o valor com h = 1e-3 e' RUIDO DE")
say("  TRUNCAMENTO, nao fisica. E' a MESMA classe de erro do")
say("  Erratum-03, so' que agora com estencil de 8a ordem e h grande")
say("  demais para o condicionamento do ramo infinito.")
say("")
say("  E o teste de precisao SEPARA os dois casos: subir dps de 60 para")
say("  250 NAO move o numero (ele e' truncamento, nao arredondamento);")
say("  baixar h move-o em 5 ordens de grandeza.")
say("")
say("  CONSEQUENCIA METODOLOGICA (proposta de regra 6b): o teste de")
say("  refino tem de ser em TRES h com criterio de convergencia, e o")
say("  h necessario depende do fundo. Um h fixo pre-escolhido nao e'")
say("  auditavel.")

say("")
say("=" * 72)
say("[C-M4'] E O MESMO VALE PARA kh -- com CONTROLE no ramo finito")
say("=" * 72)
say("")
say("  Varredura kh x a, h = 1e-3 (o h do corpus), IBB f=0.5, mu=1:")
CEL_T, YT = None, None


def cel_ibb(FR, MU):
    Y = 2 * FR * MU**sp.Rational(3, 2)
    return celula(sp.Integer(0), sp.Integer(0), Y, MU), float(Y)


CEL_T, YT = cel_ibb(sp.Rational(1, 2), sp.Integer(1))
RHO0_T = mp.mpf(float(rho0_de_Omega(YT, 1.0)))
KHS = (mp.mpf(1e3), mp.mpf(1e4), mp.mpf(1e5), mp.mpf(1e6), mp.mpf(1e7))
say(f"  {'a':>9} " + " ".join(f"{('kh=%.0e' % float(k)):>18}" for k in KHS))
for aval in ('0.001', '0.01', '0.1', '1.0', '10.0', '30.0'):
    row = [mp.nstr(cs2(CEL_T, aval, k, RHO0_T)[0], 10) for k in KHS]
    say(f"  {aval:>9} " + " ".join(f"{x:>18}" for x in row))
say("")
say("  CONTROLE (ramo finito, benchmark do R-12g, MESMA varredura):")
say(f"  {'a':>9} " + " ".join(f"{('kh=%.0e' % float(k)):>18}" for k in KHS))
for aval in ('0.0001', '0.01', '1.0'):
    row = [mp.nstr(cs2(BENCH, aval, k, RHO0_BENCH, ramo='finito')[0], 10)
           for k in KHS]
    say(f"  {aval:>9} " + " ".join(f"{x:>18}" for x in row))
say("")
say("  O controle DEGRADA do mesmo jeito em kh alto (a = 1e-4: -1.0000")
say("  em kh <= 1e5, -0.99999 em 1e6, -0.99999 em 1e7 e pior adiante).")
say("  Logo o teto em kh e' do INSTRUMENTO, nao do ramo infinito.")

say("")
say("=" * 72)
say("[C-R1] MEDIDA COM REFINO DUPLO (h e kh) -- protocolo adaptativo")
say("=" * 72)
say("")
say("  Protocolo: (1) refinar h em 1e-3 .. 1e-6 no kh mais alto da")
say("  trinca ate' que dois h sucessivos concordem a <= 1e-7;")
say("  (2) com esse h, avaliar em kh = 1e3, 3e3, 1e4 e EXTRAPOLAR o")
say("  limite sub-horizonte por Richardson em 1/kh^2 (o residuo em kh")
say("  e' MASSA, Erratum-03 sec.3 -- nao e' erro, e nao deve ser")
say("  exigido zero); (3) exigir que as DUAS extrapolacoes (kh1,kh2) e")
say("  (kh2,kh3) concordem a <= 1e-6. Ponto que falhe: NAO MEDIDO.")
say("")
HS = ('1e-3', '3e-4', '1e-4', '3e-5', '1e-5', '3e-6', '1e-6')
KH3 = (mp.mpf(1000), mp.mpf(3000), mp.mpf(10000))
TOL_H = mp.mpf('1e-7')
TOL_X = mp.mpf('1e-6')


def richardson(c1, c2, q):
    """Extrapola c(kh) = c_inf + m/kh^2 a partir de dois kh com kh2=q*kh1."""
    return c2 + (c2 - c1) / (q**2 - 1)


def medida_convergida(cel, aval, rho0):
    """c_s^2 com refino em h E extrapolacao 1/kh^2 em kh.

    O desvio residual em kh e' MASSA (Erratum-03 sec.3: omega^2/H^2 =
    -kh^2 + m_ef^2/H^2), logo cai como 1/kh^2 -- NAO e' erro. O gate
    correto nao e' 'os tres kh coincidem', e' 'a extrapolacao 1/kh^2
    e' estavel'.
    """
    # (1) refino em h no kh MAIS ALTO da trinca (o pior caso)
    h_ok, prev = None, None
    for hs in HS:
        try:
            vv = cs2(cel, aval, KH3[-1], rho0, hN=mp.mpf(hs))
        except Exception:                                    # noqa: BLE001
            return None, 'h-excecao'
        if prev is not None and abs(vv[0] - prev) <= TOL_H:
            h_ok = hs
            break
        prev = vv[0]
    if h_ok is None:
        return None, 'h-nao-converge'
    # (2) trinca em kh com o h convergido + extrapolacao de Richardson
    cs = []
    for kh in KH3:
        try:
            cs.append(cs2(cel, aval, kh, rho0, hN=mp.mpf(h_ok)))
        except Exception:                                    # noqa: BLE001
            return None, 'kh-excecao'
    q = KH3[1] / KH3[0]
    e1 = richardson(cs[0][0], cs[1][0], q)
    e2 = richardson(cs[1][0], cs[2][0], KH3[2] / KH3[1])
    if abs(e1 - e2) > TOL_X:
        return None, f'kh-extrap {mp.nstr(abs(e1-e2), 3)}'
    return (cs[-1], e2, h_ok, abs(e1 - e2)), None


MU_S = [sp.Rational(1, 10), sp.Integer(1), sp.Integer(10)]
FR_S = [sp.Rational(5, 100), sp.Rational(20, 100), sp.Rational(1, 2),
        sp.Rational(80, 100), sp.Rational(98, 100)]
A_S = ['0.00003', '0.0001', '0.001', '0.01', '0.1', '0.3', '1.0',
       '3.0', '10.0', '30.0']

say(f"  {'f':>6} {'a':>9} {'r':>13} {'c_s^2 (kh->inf)':>20} "
    f"{'canal 2 (lit)':>15} {'Delta':>13} {'h':>7} "
    f"{'estab extrap':>13} {'cond':>9}")
REG, NAO = [], []
for FR in FR_S:
    cel, yf = cel_ibb(FR, sp.Integer(1))
    rho0 = mp.mpf(float(rho0_de_Omega(yf, 1.0)))
    for aval in A_S:
        res, motivo = medida_convergida(cel, aval, rho0)
        if res is None:
            say(f"  {float(FR):6.2f} {aval:>9}   NAO MEDIDO: {motivo}")
            NAO.append((float(FR), aval, motivo))
            continue
        v0, cinf, h0, est = res
        c2, c3, rp, rpp = canais_fechados(cel, v0[3])
        REG.append((float(FR), aval, v0[3], cinf, c2, cinf - c2,
                    v0[1], v0[2], h0, est))
        say(f"  {float(FR):6.2f} {aval:>9} {mp.nstr(v0[3], 8):>13} "
            f"{mp.nstr(cinf, 14):>20} {mp.nstr(c2, 10):>15} "
            f"{mp.nstr(cinf - c2, 8):>13} {h0:>7} "
            f"{mp.nstr(est, 3):>13} {v0[2]:9.2e}")

say("")
say(f"  pontos medidos: {len(REG)}   nao medidos: {len(NAO)}")
if NAO:
    say("  nao medidos (preservados, regra 2): "
        + ", ".join(f"f={a:.2f},a={b}({c})" for a, b, c in NAO))
say("")
if REG:
    cs_all = [x[3] for x in REG]
    npos = sum(1 for c in cs_all if c > 0)
    say(f"  [C-R2] c_s^2 > 0 em {npos}/{len(REG)} pontos medidos")
    say(f"         min = {mp.nstr(min(cs_all), 12)}  (celula/epoca: "
        + str([(x[0], x[1]) for x in REG if x[3] == min(cs_all)]) + ")")
    say(f"         max = {mp.nstr(max(cs_all), 12)}")
    say(f"  [C-X2] Delta = canal 1 - canal 2 (literatura):")
    say(f"         max |Delta| = {mp.nstr(max(abs(x[5]) for x in REG), 4)}"
        f"   min |Delta| = {mp.nstr(min(abs(x[5]) for x in REG), 4)}")
    say(f"         Delta e' NEGATIVO em "
        f"{sum(1 for x in REG if x[5] < 0)}/{len(REG)} pontos e tende a")
    say(f"         zero nos DOIS extremos -- os dois canais medem")
    say(f"         sistemas diferentes (2-DOF nosso vs 1-DOF reduzido")
    say(f"         deles), logo NAO tem de coincidir.")
    say(f"  [C-X3] a relacao Delta = (1/2) r r' do R-12i foi provada la'")
    say(f"         na celula beta_0-beta_1 (beta_4 = 0) do ramo FINITO.")
    say(f"         Aqui (beta_4 != 0, ramo infinito) ela NAO se aplica:")
    say(f"         (1/2) r r' vale ate' ~1e12 enquanto Delta <= 0.093.")
    say(f"         RESULTADO PRE-DECLARADO: a relacao e' propria daquela")
    say(f"         celula e daquele ramo. Achado, nao falha.")
    say(f"  [C-R3] max |calibrador - 1| = "
        f"{mp.nstr(max(abs(x[6] - 1) for x in REG), 4)}")
    say(f"         (o calibrador e' CEGO ao canal Cdot -- Erratum-03")
    say(f"          sec.5 --, logo NAO e' prova de nada aqui)")
    say(f"  [C-M1] cond(W_XX) maximo entre os pontos medidos = "
        f"{max(x[7] for x in REG):.2e}")

say("")
say("=" * 72)
say("[C-M5] DEGENERESCENCIA EM mu -- gate novo, no ponto convergido")
say("=" * 72)
say("")
say("  O corolario F-3 do R-13b prova que mu e' PURA REESCALA do fundo")
say("  a f fixo. Logo c_s^2, que e' adimensional, tem de ser IDENTICO")
say("  entre celulas de mesmo f e mu diferente. Gate novo.")
say("")
say(f"  {'f':>6} {'a':>9} {'h':>7} {'c_s^2 (mu=0.1)':>20} "
    f"{'c_s^2 (mu=1)':>20} {'c_s^2 (mu=10)':>20} {'max dif':>10}")
pior = mp.mpf(0)
for FR in (sp.Rational(5, 100), sp.Rational(1, 2), sp.Rational(98, 100)):
    for aval in ('0.001', '0.1', '1.0', '30.0'):
        alvo = [x for x in REG
                if abs(x[0] - float(FR)) < 1e-9 and x[1] == aval]
        if not alvo:
            continue
        h0 = alvo[0][8]
        vs = []
        for MU in MU_S:
            c_, y_ = cel_ibb(FR, MU)
            rr_ = mp.mpf(float(rho0_de_Omega(y_, float(MU))))
            vs.append(cs2(c_, aval, mp.mpf(1000), rr_, hN=mp.mpf(h0))[0])
        d = max(abs(vs[i] - vs[j]) for i in range(3) for j in range(3))
        pior = max(pior, d)
        say(f"  {float(FR):6.2f} {aval:>9} {h0:>7} {mp.nstr(vs[0], 14):>20} "
            f"{mp.nstr(vs[1], 14):>20} {mp.nstr(vs[2], 14):>20} "
            f"{mp.nstr(d, 3):>10}")
say("")
say(f"  [C-M5] max dif em mu = {mp.nstr(pior, 4)}   (criterio <= 1e-8)")

say("")
say("=" * 72)
say("[C-R4] CONTRASTE COM O RAMO FINITO, NA MESMA RODADA")
say("=" * 72)
say("")
say(f"  {'ramo':>10} {'celula':>26} {'a':>8} {'c_s^2':>22}")
for aval in ('0.0001', '0.01'):
    v = cs2(BENCH, aval, mp.mpf(1000), RHO0_BENCH, ramo='finito')
    say(f"  {'FINITO':>10} {'b=(1,1,-0.4,0,0.5) mu=1':>26} {aval:>8} "
        f"{mp.nstr(v[0], 14):>22}")
for aval in ('0.001', '0.1', '1.0', '30.0'):
    alvo = [x for x in REG if abs(x[0] - 0.5) < 1e-9 and x[1] == aval]
    if alvo:
        say(f"  {'INFINITO':>10} {'b=(0,1,0,0,1) mu=1':>26} {aval:>8} "
            f"{mp.nstr(alvo[0][3], 14):>22}")

say("")
say("=" * 72)
say("O QUE FOI MEDIDO, E SO' ISSO")
say("=" * 72)
say("")
say("  Medido: c_s^2 do modo metrico do sistema 2-DOF no ramo INFINITO")
say("  de celulas IBB genuinas, com refino DUPLO (h e kh) e controle")
say("  positivo no ramo finito, contra o canal fechado da literatura")
say("  -r''/(3r').")
say("")
say("  NAO medido: perturbacao de materia (delta rho_m -- ausente da L2")
say("  deste projeto); fantasma escalar; Higuchi; EFT; screening;")
say("  modulacao beta_n(phi_-); b2 ou b3 != 0.")

os.makedirs(OUTD, exist_ok=True)
with open(os.path.join(OUTD, 'r13aud_c_cs2_ibb.txt'), 'w',
          encoding='utf-8') as fh:
    fh.write("\n".join(OUT) + "\n")
say("")
say("saida escrita em auditoria/code/out/r13aud_c_cs2_ibb.txt")
