# -*- coding: utf-8 -*-
"""
r3c_pousada_mecanismo.py — R-3c: o mecanismo do crescimento tardio da
familia pousada (docs/resultado_r3b_pousada.md sec.2-3): e instabilidade
do PONTO FIXO, e alimentado pelo DESVIO residual (secular-fed), e e
especifico da MODULACAO ou da esquina beta1-grande?

CONTEXTO. A R-3b estabeleceu (2b): o crescimento tardio ~+1H do fundo
pousado e CONVERGIDO (halving no k do achado), NAO-PARAMETRICO (persiste
— e sobe — com as oscilacoes de chi amortecidas; a sonda de banda da
negativo) e IR (morre em k_phys >~ 2: k_c=25000 da +0.06 onde o
congelado diz 41.7). MAS o braco amortecido revelou lacuna de desenho:
com Gamma=30 a aproximacao sobreamortecida ao ponto fixo e LENTA
(lambda ~ m_eff^2/(Gamma+3)H ~ 0.7/H < 3/2 H do envelope original), e
na tardia o fundo amortecido esta MAIS LONGE do ponto fixo (desvio
secular 3.7e-2 vs oscilacao 1.6e-2 do original). Logo "PERSISTE" nao
distingue: (b) instabilidade genuina do vacuo pousado exato, ou
(c) crescimento alimentado por QUALQUER desvio residual do ponto fixo
(transiente de aproximacao de cauda longa). E ha um confundidor de
classe: o fundo pousado tem beta1_eff = beta1(chi_fim) = 4.47 — FORA
do retangulo da R-1 (beta1 <= 2); talvez a esquina beta1-grande da
familia BETA-CONSTANTE ja cresca, sem modulacao nenhuma.

DOIS DISCRIMINADORES (mesma maquinaria da R-3/R-3b, verbatim):

  BRACO G — beta-constante beta1=4.47: fundo algebrico do ramo finito
    (instrumento do D2/R-1: raiz cubica + taxas analiticas; dust
    rho0=0.3; mu=1, beta0=1, beta2=-0.4, beta4=0.5), SEM modulacao
    (Fp=Fpp=0) e com delta-chi espectador (chid=0, Up=0, Upp=0.3 —
    convencao D2/R-1). Mesma faixa a=[100,20000], mesmos k_c
    {12500, 1250} (H deste fundo ~1.12 ~ H do pousado ~1.14 -> k_phys/H
    comparaveis por construcao). O fundo e ESTATICO (dust ~1e-7 do
    potencial nesta faixa) — qualquer crescimento aqui e propriedade
    da familia beta-constante na esquina beta1-grande, nao da
    modulacao/pouso.
  BRACOS H/I/K — correlacao taxa-vs-desvio: variar Gamma muda o
    tamanho do desvio residual na tardia SEM mudar o ponto fixo:
      Gamma=10  -> aproximacao RAPIDA (lambda ~ 1.8/H > 3/2H): desvio
                   MINIMO na tardia (menor que o do proprio original);
      Gamma=100 -> aproximacao LENTA (lambda ~ 0.2/H): desvio MAXIMO.
    Com os pontos ja medidos (original Gamma=0 e Gamma=30 da R-3b,
    hardcoded abaixo com proveniencia), a curva taxa(desvio) fica com
    4 pontos em k_c=12500 (H: Gamma=10; I: Gamma=100) e 3 em k_c=1250
    (K: Gamma=100).

CRITERIOS PRE-DECLARADOS:
  R3c-CONT: pre e rolagem do braco H devem reproduzir as taxas
      metricas oficiais da R-3 (pre [-1.32,+2.05,+0.13,+0.55],
      rolagem [+0.37,+0.04,+0.47,+0.26]; max|Delta| < 0.1) — o
      amortecimento nao vaza para tras. FALHA -> nao interpretar H/I/K.
  R3c-BETA (braco G, taxa metrica max na tardia, dois k):
      >= 0.5 em algum k -> o crescimento tardio NAO e especifico da
          modulacao: e da esquina beta1-grande da familia
          beta-constante (a R-1 nao amostrou beta1>2 — o "primeiro
          crescimento tardio real" ganha outra genealogia; mapear a
          fronteira em beta1 vira item do R-4);
      <= 0.1 nos dois k -> ESPECIFICO do fundo modulado-pousado
          (modulacao F'!=0 e/ou estrutura do pouso);
      senao -> reportar (fronteira difusa).
      Diagnostico extra: se G crescer tambem nas OUTRAS janelas
      (fundo estatico), e instabilidade de familia em toda epoca —
      reportar por janela.
  R3c-DRIFT (k_c=12500; desvio = Aosc_tardia = max|chi-chi_fim|/chi_fim):
      contraste exigido: Aosc_max/Aosc_min >= 3 entre os 4 pontos
      (senao: contraste insuficiente, reportar sem veredito).
      taxa(desvio_max) >= 1.5 * taxa(desvio_min)  -> SECULAR-FED:
          o crescimento acompanha o desvio residual — transiente de
          aproximacao de cauda longa, nao instabilidade do vacuo; o
          enunciado do cap.07 ganha a forma fraca e o R-4 computa o
          dano integrado (lnA da cauda);
      max/min das taxas <= 1.4 com desvios variando >=3x -> PONTO-FIXO:
          instabilidade genuina do vacuo pousado — primeiro no-go
          dinamico real do programa (nivel linear, fronteira
          declarada); R-4 herda com prioridade maxima;
      senao -> MISTO (duas componentes? reportar).
      Secundario (k_c=1250, 3 pontos): mesma leitura, sem criterio
      duro (reportar).
  Ancoras (a in {5000,15000}): sigma/H congelado reduzido (pre-escala)
      + negK em todos os bracos (trilha estrutural; esperado negK=1
      tambem no beta-constante 4.47 — R-1 viu negK=1 universal ate
      beta1=2).

HARDCODES DECLARADOS (proveniencia: out/r3b_pousada_parametrico.txt,
commit da rodada oficial R-3b; e out/r3_faseB_evolucao_rolagem.txt):
  k=12500 tardia met: ORG(Gamma=0) +0.98 (Aosc 1.55e-2, |desl| 3.26e-2);
  DAM Gamma=30 +1.12 (Aosc 3.74e-2, |desl| 1.72e-2).
  k=1250 tardia met: ORG +1.05; Gamma=30 +1.87.
  Oficial k=12500: pre met [-1.32,+2.05,+0.13,+0.55]; rolagem met
  [+0.37,+0.04,+0.47,+0.26].

Requer sympy, numpy, scipy. ~5-10 min.
Uso (raiz do repo, venv ativo):
    python auditoria/code/r3c_pousada_mecanismo.py
Saida em auditoria/code/out/r3c_pousada_mecanismo.txt
"""
import importlib.util
import os
import sys
import time

import numpy as np
import sympy as sp
from scipy.interpolate import CubicSpline
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
                           quadratic_matrices)

T0 = time.time()
OUT = []


def say(*a):
    line = " ".join(str(x) for x in a)
    print(f"[{time.time()-T0:7.1f}s] {line}")
    OUT.append(line)


NOMES = ['Phi_g', 'B_g', 'Phi_f', 'Psi_f', 'B_f', 'E_f', 'dchi']
MULT = [0, 1, 2, 4]
DYN = [3, 5, 6]
IDX_MET_IC = [0, 1, 3, 4]
JANELAS = [("pre", 150.0, 450.0), ("rolagem", 760.0, 2050.0),
           ("pouso", 2100.0, 6800.0), ("tardia", 8000.0, 18000.0)]
MARCAS_C = [300, 760, 1250, 2100, 3200, 5000, 6800, 8000, 10000,
            12000, 15000, 18000]
ANCORAS_B = [5000.0, 15000.0]
A_MIN, A_MAX = 100.0, 20000.0
NPTS = 20000

K_MAIN, K_IR = 12500.0, 1250.0
B1_POUSADO = 4.47  # beta1(chi_fim) do fundo pousado

# hardcodes da R-3/R-3b (proveniencia no cabecalho)
REF = dict(
    org_t12500=0.98, org_aosc=1.55e-2, org_desl=3.26e-2,
    g30_t12500=1.12, g30_aosc=3.74e-2, g30_desl=1.72e-2,
    org_t1250=1.05, g30_t1250=1.87,
    pre_met=[-1.32, 2.05, 0.13, 0.55],
    rol_met=[0.37, 0.04, 0.47, 0.26])

# amortecimento (mesma rampa da R-3b)
A_DAMP = 2400.0
LARG = 0.03
GAM_H, GAM_I = 10.0, 100.0

# parametros (identicos a R-3/R-3b)
MU = 1.0
MG2, MF2 = 1.0, MU
ME2 = MU / (1.0 + MU)
M2 = 1.0
B0V, B2V, B4V = 1.0, -0.4, 0.5
B10 = 1.0
RHO0 = 0.3
VST = 1.0

say("=" * 72)
say("R-3c — MECANISMO DO CRESCIMENTO TARDIO DA FAMILIA POUSADA")
say("=" * 72)

# ------------------------------------------------------------------
# V1 + montagem + fatias (verbatim R-3/R-3b)
# ------------------------------------------------------------------
if not d1.gr_selfcheck():
    say("[!] V1 (GR selfcheck da biblioteca) falhou — abortando")
    sys.exit(1)
say("[V1] GR selfcheck da biblioteca: PASSA")

L2s, fields, vels = d1.build_L2()
K7, C7, W7 = quadratic_matrices(L2s, fields, vels)
if [str(f) for f in fields] != NOMES:
    raise RuntimeError("ordem de campos mudou")
say("[montagem] K,C,W 7x7 prontos")

say("[fatias] {Fb,Fp,Fpp} x {b0..b4}, taxas livres ...")
LIVRES = (a_s, b_s, xi_s, H_s, Hf_s, Hd_s, Hfd_s, xid_s,
          chid_s, chidd_s, Ub, Up, Upp, ksym, Mf2, Meff2)
FIXOS = {Mg2: 1, m2: 1, rho_s: 0}
BETAS = (b0, b1, b2, b3, b4)


def fatias(M):
    Msub = M.subs(FIXOS)
    base_s = Msub.subs({Fb: 0, Fp: 0, Fpp: 0})
    out = {'base': sp.lambdify(LIVRES, base_s, modules='numpy')}
    for tag, fsub in (('Fb', {Fb: 1, Fp: 0, Fpp: 0}),
                      ('Fp', {Fb: 0, Fp: 1, Fpp: 0}),
                      ('Fpp', {Fb: 0, Fp: 0, Fpp: 1})):
        for n, bn in enumerate(BETAS):
            bsub = {bm: (1 if mm == n else 0) for mm, bm in enumerate(BETAS)}
            Sl = Msub.subs(fsub).subs(bsub) - base_s
            out[(tag, n)] = sp.lambdify(LIVRES, Sl, modules='numpy')
    return out


FK, FC, FW = fatias(K7), fatias(C7), fatias(W7)
say("[fatias] prontas")


def monta(fat, args, bvals, bp, bpp):
    M = np.array(fat['base'](*args), float).copy()
    for n in range(5):
        if bvals[n]:
            M += bvals[n] * np.array(fat[('Fb', n)](*args), float)
        if bp[n]:
            M += bp[n] * np.array(fat[('Fp', n)](*args), float)
        if bpp[n]:
            M += bpp[n] * np.array(fat[('Fpp', n)](*args), float)
    return M


# ------------------------------------------------------------------
# fundo de rolagem com amortecimento (verbatim R-3b) + fundo
# beta-constante (verbatim R-1)
# ------------------------------------------------------------------
a_, b_, ch_ = sp.symbols('a b chi', positive=True)
pa_, pb_, pch_ = sp.symbols('p_a p_b p_chi', real=True)
Mg2s, Mf2s, Me2s, m2s = sp.symbols('Mg2 Mf2 Meff2 m2', positive=True)
b0s, b2s, b4s = sp.symbols('beta_0 beta_2 beta_4', real=True)
Hs_, Hfs_, chds_ = sp.symbols('H H_f chidot', real=True)
b10s, vsts = sp.symbols('b1_0 v_star', positive=True)
b1_conc = b10s * (1 + ch_**2 / vsts**2)
rr_ = b_ / a_
Vgc_s = b0s + 3 * rr_ * b1_conc + 3 * rr_**2 * b2s
Vfc_s = b1_conc + 3 * rr_ * b2s + rr_**3 * b4s
Hg_sym = (-pa_**2 / (12 * Mg2s * a_) + pch_**2 / (2 * a_**3)
          + m2s * Me2s * a_**3 * Vgc_s)
Hf_sym = -pb_**2 / (12 * Mf2s * b_) + m2s * Me2s * a_**3 * Vfc_s
CANON = [(a_, pa_), (b_, pb_), (ch_, pch_)]
Om_sym = sp.expand(sum(sp.diff(Hg_sym, q) * sp.diff(Hf_sym, p)
                       - sp.diff(Hg_sym, p) * sp.diff(Hf_sym, q)
                       for q, p in CANON))
Om_v = sp.expand(Om_sym.subs({pa_: -6 * Mg2s * a_**2 * Hs_,
                              pb_: -6 * Mf2s * b_**2 * Hfs_,
                              pch_: a_**3 * chds_}))
Om_fn = sp.lambdify((a_, b_, ch_, chds_, Hs_, Hfs_,
                     Mg2s, Mf2s, Me2s, m2s, b0s, b2s, b4s, b10s, vsts),
                    Om_v, modules='math')


def beta1(ch, vst):
    return B10 * (1.0 + ch * ch / (vst * vst))


def dbeta1(ch, vst):
    return 2.0 * B10 * ch / (vst * vst)


def U_pot(ch, mu2, lam, U0):
    return -0.5 * mu2 * ch * ch + 0.25 * lam * ch**4 + U0


def dU_pot(ch, mu2, lam):
    return -mu2 * ch + lam * ch**3


def H2_of(r, ch, chd, a, vst, mu2, lam, U0):
    b1v = beta1(ch, vst)
    Vg = B0V + 3 * r * b1v + 3 * r * r * B2V
    return (0.5 * chd * chd + U_pot(ch, mu2, lam, U0) + RHO0 / a**3
            + M2 * ME2 * Vg) / (3 * MG2)


def Hf2_of(r, ch, vst):
    b1v = beta1(ch, vst)
    Vf = b1v + 3 * r * B2V + r**3 * B4V
    return M2 * ME2 * Vf / (3 * MF2 * r**3)


def Om_num(r, ch, chd, a, vst, mu2, lam, U0):
    H2 = H2_of(r, ch, chd, a, vst, mu2, lam, U0)
    Hf2 = Hf2_of(r, ch, vst)
    if H2 <= 0 or Hf2 <= 0:
        return float('nan')
    return Om_fn(a, r * a, ch, chd, np.sqrt(H2), np.sqrt(Hf2),
                 MG2, MF2, ME2, M2, B0V, B2V, B4V, B10, vst)


def acha_raiz(r_prev, ch, chd, a, vst, mu2, lam, U0):
    for fator in (0.08, 0.25, 0.6):
        lo, hi = r_prev * (1 - fator), r_prev * (1 + fator)
        grade = np.linspace(lo, hi, 61)
        vals = np.array([Om_num(x, ch, chd, a, vst, mu2, lam, U0)
                         for x in grade])
        fin = np.isfinite(vals)
        for i in range(len(grade) - 1):
            if fin[i] and fin[i + 1] and vals[i] * vals[i + 1] < 0:
                try:
                    return brentq(
                        lambda x: Om_num(x, ch, chd, a, vst, mu2, lam, U0),
                        grade[i], grade[i + 1], xtol=1e-14)
                except ValueError:
                    continue
    return None


def raiz_cubica(a, ch, chd, vst, mu2, lam, U0):
    b1v = beta1(ch, vst)
    rho_tot = 0.5 * chd * chd + U_pot(ch, mu2, lam, U0) + RHO0 / a**3
    rt = rho_tot / (M2 * ME2)
    kap = MG2 / MF2
    rr = np.roots([kap * B4V - 3 * B2V, -3 * b1v,
                   3 * kap * B2V - B0V - rt, kap * b1v])
    reais = sorted(x.real for x in rr if abs(x.imag) < 1e-9 and x.real > 1e-12)
    return reais[0] if reais else None


def integra_alvo(g_end=2.0, mchi2=30.0, vst=1.0, a0=0.01, a1=1e5, dN=5e-4,
                 gam0=0.0):
    v = g_end * vst
    mu2 = 0.5 * mchi2
    lam = mu2 / (v * v)
    U0 = 0.25 * mu2 * v * v
    N0, N1 = np.log(a0), np.log(a1)
    n = int((N1 - N0) / dN) + 1
    ch, y = 1e-3 * v, 0.0
    r = raiz_cubica(a0, ch, 0.0, vst, mu2, lam, U0)
    rp = 3.0 * r
    Hprev = None
    lnAD = np.log(A_DAMP)
    rec = {kk: [] for kk in ('N', 'a', 'r', 'xi', 'H', 'Hfv', 'ch', 'chd',
                             'chidd', 'desl')}
    for i in range(n):
        N = N0 + i * dN
        a = np.exp(N)
        b1v = beta1(ch, vst)
        Vg = B0V + 3 * r * b1v + 3 * r * r * B2V
        resto = U_pot(ch, mu2, lam, U0) + RHO0 / a**3 + M2 * ME2 * Vg
        den = 3 * MG2 - 0.5 * y * y
        if den <= 0 or resto <= 0:
            raise RuntimeError(f"fundo abortou (H^2) em a={a:.3f}")
        H = np.sqrt(resto / den)
        chd = H * y
        Hf2 = Hf2_of(r, ch, vst)
        if Hf2 <= 0:
            raise RuntimeError(f"fundo abortou (H_f^2) em a={a:.3f}")
        Hfv = np.sqrt(Hf2)
        xi = H * (1.0 + rp / r) / Hfv
        gam = 0.0
        if gam0:
            gam = gam0 * 0.5 * (1.0 + np.tanh((N - lnAD) / LARG))
        chidd = (-3 * H * chd - dU_pot(ch, mu2, lam)
                 - M2 * ME2 * dbeta1(ch, vst) * (xi + 3 * r)
                 - gam * H * chd)
        Hp = 0.0 if Hprev is None else (H - Hprev) / dN
        yp = chidd / (H * H) - (Hp / H) * y
        if i % max(1, n // 20000) == 0:
            for kk, vv in (('N', N), ('a', a), ('r', r), ('xi', xi),
                           ('H', H), ('Hfv', Hfv), ('ch', ch), ('chd', chd),
                           ('chidd', chidd), ('desl', (H - r * Hfv) / H)):
                rec[kk].append(vv)
        ch += dN * y
        y += dN * yp
        r_new = acha_raiz(r, ch, H * y, np.exp(N + dN), vst, mu2, lam, U0)
        if r_new is None:
            raise RuntimeError(f"fundo perdeu a raiz em a={np.exp(N+dN):.3f}")
        rp = (r_new - r) / dN
        r = r_new
        Hprev = H
    rec = {kk: np.array(vv) for kk, vv in rec.items()}
    rec['v'] = v
    rec['vst'] = vst
    rec['mu2'] = mu2
    rec['lam'] = lam
    rec['U0'] = U0
    return rec


def make_ctx(rec, rotulo):
    spl = {kk: CubicSpline(rec['N'], rec[kk])
           for kk in ('r', 'xi', 'H', 'Hfv', 'ch', 'chd', 'chidd')}
    return dict(rec=rec, spl=spl, dH=spl['H'].derivative(),
                dHf=spl['Hfv'].derivative(), dxi=spl['xi'].derivative(),
                rotulo=rotulo)


def bg_ponto(ctx, N):
    spl = ctx['spl']
    rec = ctx['rec']
    H = float(spl['H'](N))
    ch = float(spl['ch'](N))
    mu2, lam, U0 = rec['mu2'], rec['lam'], rec['U0']
    a = np.exp(N)
    return dict(
        a=a, r=float(spl['r'](N)), xi=float(spl['xi'](N)), H=H,
        Hf=float(spl['Hfv'](N)), ch=ch, chd=float(spl['chd'](N)),
        chidd=float(spl['chidd'](N)),
        Hd=H * float(ctx['dH'](N)), Hfd=H * float(ctx['dHf'](N)),
        xid=H * float(ctx['dxi'](N)),
        Ubv=U_pot(ch, mu2, lam, U0) + RHO0 / a**3,
        Upv=dU_pot(ch, mu2, lam), Uppv=-mu2 + 3 * lam * ch * ch)


def fundo_bconst(a, B1V):
    """ramo finito beta-constante com taxas analiticas (R-1 verbatim,
    mu=1)."""
    kap = 1.0 / MU
    meff2 = ME2
    rho = RHO0 * a**-3
    rho_til = rho / meff2
    rr = np.roots([kap * B4V - 3 * B2V, -3 * B1V,
                   3 * kap * B2V - B0V - rho_til, kap * B1V])
    reais = sorted(z.real for z in rr if abs(z.imag) < 1e-9 and z.real > 1e-10)
    if not reais:
        return None
    r = reais[0]
    dW = kap * (2 * B4V * r - B1V / r**2) - 3 * B1V - 6 * B2V * r
    if abs(dW) < 1e-14:
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
    dlnH_dN = 0.5 * (2 / r + dVf / Vf) * drdN
    Hd = H2 * dlnH_dN
    xid = H * (drdN + d2rdN2)
    Hfd = (Hd - H2 * drdN / r) / r
    rho_int = meff2 * (B0V + 3 * B1V * r + 3 * B2V * r**2)
    return dict(r=r, xi=xi, H=H, Hf=H / r, Hd=Hd, Hfd=Hfd, xid=xid,
                Ub=3 * H2 - rho_int)


# ------------------------------------------------------------------
# builders de matrizes
# ------------------------------------------------------------------
def builder_rolagem(ctx):
    def build(kc, npts):
        Ns = np.linspace(np.log(A_MIN), np.log(A_MAX), npts)
        Hs_arr = np.zeros(npts)
        Ms = {x: np.zeros((npts, 7, 7)) for x in 'KCW'}
        for p, N in enumerate(Ns):
            f = bg_ponto(ctx, N)
            Hs_arr[p] = f['H']
            args = (f['a'], f['r'] * f['a'], f['xi'], f['H'], f['Hf'],
                    f['Hd'], f['Hfd'], f['xid'], f['chd'], f['chidd'],
                    f['Ubv'], f['Upv'], f['Uppv'], kc, MF2, ME2)
            bvals = (B0V, beta1(f['ch'], VST), B2V, 0.0, B4V)
            bp = (0.0, dbeta1(f['ch'], VST), 0.0, 0.0, 0.0)
            bpp = (0.0, 2.0 * B10 / VST**2, 0.0, 0.0, 0.0)
            Ms['K'][p] = monta(FK, args, bvals, bp, bpp)
            Ms['C'][p] = monta(FC, args, bvals, bp, bpp)
            Ms['W'][p] = monta(FW, args, bvals, bp, bpp)
        return Ns, Hs_arr, Ms
    return build


def builder_bconst(B1V):
    def build(kc, npts):
        Ns = np.linspace(np.log(A_MIN), np.log(A_MAX), npts)
        Hs_arr = np.zeros(npts)
        Ms = {x: np.zeros((npts, 7, 7)) for x in 'KCW'}
        for p, N in enumerate(Ns):
            a = np.exp(N)
            f = fundo_bconst(a, B1V)
            if f is None:
                raise RuntimeError(f"fundo beta-constante invalido em "
                                   f"a={a:.1f}")
            Hs_arr[p] = f['H']
            args = (a, f['r'] * a, f['xi'], f['H'], f['Hf'],
                    f['Hd'], f['Hfd'], f['xid'], 0.0, 0.0,
                    f['Ub'], 0.0, 0.3, kc, MF2, ME2)
            bvals = (B0V, B1V, B2V, 0.0, B4V)
            bp = (0.0, 0.0, 0.0, 0.0, 0.0)
            bpp = (0.0, 0.0, 0.0, 0.0, 0.0)
            Ms['K'][p] = monta(FK, args, bvals, bp, bpp)
            Ms['C'][p] = monta(FC, args, bvals, bp, bpp)
            Ms['W'][p] = monta(FW, args, bvals, bp, bpp)
        return Ns, Hs_arr, Ms
    return build


# ------------------------------------------------------------------
# reducao + evolucao (verbatim R-3/R-3b)
# ------------------------------------------------------------------
def reduz_ponto(Kt, Ct, Wt, Cdot, mult, dyn):
    K = Kt.copy()
    C = Ct.copy()
    W = Wt.copy()
    n = K.shape[0]
    for i in mult:
        if np.max(np.abs(K[i, :])) > 1e-10 * max(1.0, np.max(np.abs(K))):
            raise RuntimeError(
                f"linha K do multiplicador {i} nao-nula "
                f"(max {np.max(np.abs(K[i, :])):.2e} vs escala "
                f"{np.max(np.abs(K)):.2e})")
        for j in range(n):
            cij = C[i, j]
            cd = Cdot[i, j]
            if i == j:
                W[i, i] += cd
            else:
                W[i, j] += cd
                W[j, i] += cd
                C[j, i] -= cij
        C[i, :] = 0.0
    WXX = W[np.ix_(mult, mult)]
    if np.linalg.cond(WXX) > 1e12:
        raise RuntimeError("W_XX mal condicionada")
    WXXi = np.linalg.inv(WXX)
    return (K[np.ix_(dyn, dyn)] + C[np.ix_(dyn, mult)] @ WXXi
            @ C[np.ix_(dyn, mult)].T,
            C[np.ix_(dyn, dyn)] - C[np.ix_(dyn, mult)] @ WXXi
            @ W[np.ix_(mult, dyn)],
            W[np.ix_(dyn, dyn)] - W[np.ix_(dyn, mult)] @ WXXi
            @ W[np.ix_(mult, dyn)])


def reduz_trilha(Ms, Ns, Hs_arr, mult, dyn):
    npts = len(Ns)
    Cdots = np.gradient(Ms['C'], Ns, axis=0) * Hs_arr[:, None, None]
    nd = len(dyn)
    Kr = np.zeros((npts, nd, nd))
    Cr = np.zeros((npts, nd, nd))
    Wr = np.zeros((npts, nd, nd))
    p_fim = npts
    for p in range(npts):
        try:
            Kr[p], Cr[p], Wr[p] = reduz_ponto(
                Ms['K'][p], Ms['C'][p], Ms['W'][p], Cdots[p], mult, dyn)
        except RuntimeError as e:
            say(f"    [ESTRUTURA] reducao falhou em a={np.exp(Ns[p]):.1f}: "
                f"{e} — trilha truncada")
            p_fim = p
            break
    Ns_t, Hs_t = Ns[:p_fim], Hs_arr[:p_fim]
    Kr, Cr, Wr = Kr[:p_fim], Cr[:p_fim], Wr[:p_fim]
    Krd = np.gradient(Kr, Ns_t, axis=0) * Hs_t[:, None, None]
    Crd = np.gradient(Cr, Ns_t, axis=0) * Hs_t[:, None, None]
    return Kr, Cr, Wr, Krd, Crd, Ns_t, Hs_t


def evolui(Kr, Cr, Wr, Krd, Crd, Ns, Hs_arr, janelas, marcas_alvo=None,
           met_idx=(0, 1)):
    npts = len(Ns)
    nd = Kr.shape[1]
    aas = np.exp(Ns)
    Hmid = {}
    for nome, lo, hi in janelas:
        pm = int(np.argmin(np.abs(aas - np.sqrt(lo * hi))))
        Hmid[nome] = Hs_arr[pm]
    taxas_f, taxas_m, amps_m, trilhas = [], [], [], {}
    for ic in range(2 * nd):
        q = np.zeros(nd)
        qd = np.zeros(nd)
        if ic < nd:
            q[ic] = 1.0
        else:
            qd[ic - nd] = 1.0
        tcum = 0.0
        amp_m = 0.0
        reg = {nome: [None] * 6 for nome, _, _ in janelas}
        marcas = ({am: None for am in marcas_alvo}
                  if (marcas_alvo is not None and ic == 0) else None)
        for p in range(npts - 1):
            dN = Ns[p + 1] - Ns[p]
            dt = dN / Hs_arr[p]
            Ki = np.linalg.inv(Kr[p])
            A = Krd[p] + Cr[p] - Cr[p].T
            B = Crd[p] + Wr[p]

            def rhs(qq, vv):
                return -Ki @ (A @ vv + B @ qq)

            k1q, k1v = qd, rhs(q, qd)
            k2q, k2v = qd + .5 * dt * k1v, rhs(q + .5 * dt * k1q,
                                               qd + .5 * dt * k1v)
            k3q, k3v = qd + .5 * dt * k2v, rhs(q + .5 * dt * k2q,
                                               qd + .5 * dt * k2v)
            k4q, k4v = qd + dt * k3v, rhs(q + dt * k3q, qd + dt * k3v)
            q = q + dt * (k1q + 2 * k2q + 2 * k3q + k4q) / 6
            qd = qd + dt * (k1v + 2 * k2v + 2 * k3v + k4v) / 6
            tcum += dt
            aa = aas[p + 1]
            n2_f = q @ q + qd @ qd
            n2_m = sum(q[j]**2 + qd[j]**2 for j in met_idx)
            ln_f = np.log(max(np.sqrt(n2_f), 1e-300))
            ln_m = np.log(max(np.sqrt(n2_m), 1e-300))
            if ic in IDX_MET_IC:
                amp_m = max(amp_m, ln_m)
            for nome, lo, hi in janelas:
                r = reg[nome]
                if r[0] is None and aa >= lo:
                    r[0], r[1], r[4] = ln_f, tcum, ln_m
                if r[2] is None and aa >= hi:
                    r[2], r[3], r[5] = ln_f, tcum, ln_m
            if marcas is not None:
                for am in marcas:
                    if marcas[am] is None and aa >= am:
                        marcas[am] = (ln_f, ln_m,
                                      n2_m / max(n2_f, 1e-300))
        tx_f, tx_m = {}, {}
        for nome, lo, hi in janelas:
            r = reg[nome]
            if r[0] is not None and r[2] is not None and r[3] > r[1]:
                tx_f[nome] = (r[2] - r[0]) / (r[3] - r[1]) / Hmid[nome]
                tx_m[nome] = (r[5] - r[4]) / (r[3] - r[1]) / Hmid[nome]
            else:
                tx_f[nome] = float('nan')
                tx_m[nome] = float('nan')
        taxas_f.append(tx_f)
        taxas_m.append(tx_m)
        amps_m.append(amp_m if ic in IDX_MET_IC else float('nan'))
        if marcas is not None:
            trilhas[ic] = marcas
    return taxas_f, taxas_m, amps_m, trilhas


def roda(rotulo, build, kc, npts, trilhas_on=False):
    say("")
    say(f"--- {rotulo}: k_c={kc:g}, npts={npts} ---")
    Ns, Hs_arr, Ms = build(kc, npts)
    Kr, Cr, Wr, Krd, Crd, Ns_t, Hs_t = reduz_trilha(Ms, Ns, Hs_arr,
                                                    MULT, DYN)
    a_max_val = float(np.exp(Ns_t[-1]))
    if a_max_val < 0.99 * A_MAX:
        say(f"    [reducao] TRUNCADA em a={a_max_val:.0f}")
    aas_t = np.exp(Ns_t)
    for a_anc in ANCORAS_B:
        if a_anc > a_max_val:
            continue
        p_anc = int(np.argmin(np.abs(aas_t - a_anc)))
        sK = max(np.max(np.abs(Kr[p_anc])), 1e-30)
        pares = d1.agrupa_pares(d1.qep_modes(Kr[p_anc] / sK,
                                             Cr[p_anc] / sK,
                                             Wr[p_anc] / sK))
        eigK = np.linalg.eigvalsh(0.5 * (Kr[p_anc] + Kr[p_anc].T))
        negK = int(np.sum(eigK < -1e-12))
        if pares:
            sig_r = max(abs(np.sqrt(complex(mm['omega2'])).imag)
                        for mm in pares) / Hs_t[p_anc]
            say(f"    ancora a={a_anc:6.0f}: sigma/H cong (red) = "
                f"{sig_r:5.2f}  negK={negK}")
        else:
            say(f"    ancora a={a_anc:6.0f}: QEP sem modos finitos "
                f"(pre-escalado)  negK={negK}")
    tf, tm, am_, trl = evolui(Kr, Cr, Wr, Krd, Crd, Ns_t, Hs_t, JANELAS,
                              marcas_alvo=(MARCAS_C if trilhas_on
                                           else None))
    say("    taxas reais/H (norma total | norma METRICA), 6 ICs:")
    for nome, lo, hi in JANELAS:
        vf = [tx[nome] for tx in tf]
        vm = [tx[nome] for tx in tm]
        say(f"    {nome:<8}" + "".join(f"{v:+7.2f}" for v in vf)
            + "  |" + "".join(f"{v:+7.2f}" for v in vm))
    say(f"    lnA_met max = {max(am_[i] for i in IDX_MET_IC):.2f}")
    if trilhas_on and 0 in trl:
        say("    perfil local (IC0, met): a1->a2: taxa_loc/H")
        ams = [am for am in MARCAS_C if trl[0].get(am)]
        for j in range(len(ams) - 1):
            a1, a2 = ams[j], ams[j + 1]
            v1, v2 = trl[0][a1], trl[0][a2]
            tloc = (v2[1] - v1[1]) / np.log(a2 / a1)
            say(f"      {a1:6d}->{a2:6d}: {tloc:+7.2f}")
    return dict(tf=tf, tm=tm, a_max=a_max_val)


def met_vals(res, nome):
    return [res['tm'][i][nome] for i in IDX_MET_IC]


def met_max(res, nome):
    fin = [v for v in met_vals(res, nome) if np.isfinite(v)]
    return max(fin) if fin else float('nan')


def osc_janela(rec, lo, hi):
    msk = (rec['a'] >= lo) & (rec['a'] <= hi)
    if not np.any(msk):
        return float('nan'), float('nan')
    ch_fim = rec['ch'][-1]
    d_max = float(np.max(np.abs(rec['desl'][msk])))
    a_osc = float(np.max(np.abs(rec['ch'][msk] - ch_fim)) / ch_fim)
    return d_max, a_osc


# ------------------------------------------------------------------
# fundos
# ------------------------------------------------------------------
say("")
say("[fundo G] beta-constante beta1=4.47 — validade e escalas:")
fG = fundo_bconst(12000.0, B1_POUSADO)
if fG is None:
    say("    [!] SEM RAMO FINITO em beta1=4.47 — o fundo pousado nao tem")
    say("    contraparte beta-constante (achado por si; braco G morre).")
    G_OK = False
else:
    G_OK = True
    say(f"    a=12000: r={fG['r']:.4f}  H={fG['H']:.4f}  xi={fG['xi']:.4f}"
        f"  (pousado: r~0.50, H~1.14)")

say(f"[fundo H] rolagem com Gamma={GAM_H:g} (aproximacao rapida) ...")
BG_H = integra_alvo(gam0=GAM_H)
say(f"    r_fim={BG_H['r'][-1]:.4f}, chi/v_fim={BG_H['ch'][-1]/BG_H['v']:.3f}"
    "  (ref ~0.498/0.932-0.939; tolerancia 0.015 — o proprio drift e o"
    " objeto)")
say(f"[fundo I] rolagem com Gamma={GAM_I:g} (aproximacao lenta) ...")
BG_I = integra_alvo(gam0=GAM_I)
say(f"    r_fim={BG_I['r'][-1]:.4f}, chi/v_fim={BG_I['ch'][-1]/BG_I['v']:.3f}")
for rot, bg in (("Gamma=10", BG_H), ("Gamma=100", BG_I)):
    dP, aP = osc_janela(bg, 2100.0, 6800.0)
    dT, aT = osc_janela(bg, 8000.0, 18000.0)
    say(f"    {rot}: pouso |desl|={dP:.2e} Aosc={aP:.2e};  "
        f"tardia |desl|={dT:.2e} Aosc={aT:.2e}")
say(f"    (hardcodes R-3b: ORG tardia Aosc={REF['org_aosc']:.2e} "
    f"|desl|={REF['org_desl']:.2e}; Gamma=30 Aosc={REF['g30_aosc']:.2e} "
    f"|desl|={REF['g30_desl']:.2e})")

CTX_H = make_ctx(BG_H, "G10")
CTX_I = make_ctx(BG_I, "G100")

# ------------------------------------------------------------------
# rodadas
# ------------------------------------------------------------------
say("")
say("=" * 72)
say("RODADAS")
say("=" * 72)
RG1 = RG2 = None
if G_OK:
    RG1 = roda("G1 (beta-const 4.47)", builder_bconst(B1_POUSADO),
               K_MAIN, NPTS, trilhas_on=True)
    RG2 = roda("G2 (beta-const 4.47)", builder_bconst(B1_POUSADO),
               K_IR, NPTS)
RH = roda(f"H (Gamma={GAM_H:g})", builder_rolagem(CTX_H), K_MAIN, NPTS)
RI = roda(f"I (Gamma={GAM_I:g})", builder_rolagem(CTX_I), K_MAIN, NPTS,
          trilhas_on=True)
RK = roda(f"K (Gamma={GAM_I:g})", builder_rolagem(CTX_I), K_IR, NPTS)

# ------------------------------------------------------------------
# vereditos
# ------------------------------------------------------------------
say("")
say("=" * 72)
say("VEREDITO R-3c (criterios pre-declarados no cabecalho)")
say("=" * 72)

# R3c-CONT (braco H vs oficial)
d_cont = 0.0
for nome, ref in (("pre", REF['pre_met']), ("rolagem", REF['rol_met'])):
    for v_med, v_ref in zip(met_vals(RH, nome), ref):
        if np.isfinite(v_med):
            d_cont = max(d_cont, abs(v_med - v_ref))
ok_cont = d_cont < 0.1
say(f"  R3c-CONT: max|H - oficial| em pre+rolagem = {d_cont:.3f} "
    f"(criterio < 0.1)  [{'PASSA' if ok_cont else 'FALHA — nao interpretar H/I/K'}]")

# R3c-BETA
say("")
if G_OK:
    tG1 = met_max(RG1, 'tardia')
    tG2 = met_max(RG2, 'tardia')
    say(f"  R3c-BETA: beta-const 4.47 tardia met max: {tG1:+.2f}/H "
        f"(k=12500), {tG2:+.2f}/H (k=1250)")
    say("      (outras janelas do G1/G2 acima — fundo estatico: "
        "crescimento em toda epoca = instabilidade de familia)")
    fin_g = [x for x in (tG1, tG2) if np.isfinite(x)]
    tGmax = max(fin_g) if fin_g else float('nan')
    if np.isfinite(tGmax) and tGmax >= 0.5:
        say("      >>> CRESCE SEM MODULACAO: o fenomeno e da esquina")
        say("      beta1-grande da familia beta-constante (a R-1 so foi")
        say("      ate beta1=2). O 'crescimento da familia pousada' ganha")
        say("      outra genealogia; mapear a fronteira em beta1 no R-4.")
        verd_beta = 'ESQUINA-BETA1'
    elif (tG1 <= 0.1 if np.isfinite(tG1) else True) and \
         (tG2 <= 0.1 if np.isfinite(tG2) else True):
        say("      >>> DILUI sem modulacao: o crescimento tardio e")
        say("      ESPECIFICO do fundo modulado-pousado (F'!=0 e/ou")
        say("      estrutura do pouso).")
        verd_beta = 'MODULACAO'
    else:
        say("      >>> intermediario — fronteira difusa; reportar.")
        verd_beta = 'DIFUSO'
else:
    verd_beta = 'SEM-FUNDO'
    say("  R3c-BETA: sem ramo finito em beta1=4.47 — ver [fundo G] acima.")

# R3c-DRIFT
say("")
say("  R3c-DRIFT (k_c=12500) — curva taxa(desvio):")
_, aoscH = osc_janela(BG_H, 8000.0, 18000.0)
_, aoscI = osc_janela(BG_I, 8000.0, 18000.0)
pontos = [("ORG   (G=0)  ", REF['org_aosc'], REF['org_t12500']),
          (f"H     (G={GAM_H:g}) ", aoscH, met_max(RH, 'tardia')),
          ("R3b-C (G=30) ", REF['g30_aosc'], REF['g30_t12500']),
          (f"I     (G={GAM_I:g})", aoscI, met_max(RI, 'tardia'))]
for rot, ao, tx in pontos:
    say(f"    {rot}: Aosc_tardia={ao:.2e}  taxa_met={tx:+.2f}/H")
fin_p = [(ao, tx) for _, ao, tx in pontos
         if np.isfinite(ao) and np.isfinite(tx)]
ao_min, tx_min = min(fin_p, key=lambda x: x[0])
ao_max, tx_max = max(fin_p, key=lambda x: x[0])
taxas_all = [tx for _, tx in fin_p]
contraste = ao_max / max(ao_min, 1e-12)
say(f"    contraste de desvio: {contraste:.1f}x "
    f"(exigido >= 3); taxa(desvio min)={tx_min:+.2f}, "
    f"taxa(desvio max)={tx_max:+.2f}")
if contraste < 3.0:
    verd_drift = 'CONTRASTE-INSUFICIENTE'
    say("      >>> contraste insuficiente — sem veredito; reportar.")
elif tx_min < 0.3 <= 0.5 <= tx_max:
    verd_drift = 'SECULAR-FED'
    say("      >>> o crescimento DESLIGA no desvio minimo (taxa "
        f"{tx_min:+.2f}) e vive no desvio maximo ({tx_max:+.2f}):")
    say("      SECULAR-FED — transiente de aproximacao de cauda longa,")
    say("      nao instabilidade do vacuo. Enunciado do cap.07 na forma")
    say("      fraca; R-4 computa o dano integrado da cauda (lnA ate o")
    say("      desvio morrer).")
elif tx_min >= 0.3 and tx_max >= 1.5 * tx_min:
    verd_drift = 'SECULAR-FED'
    say("      >>> taxa ACOMPANHA o desvio (proporcionalidade):")
    say("      SECULAR-FED — como acima, com componente de base a")
    say("      quantificar (reportar).")
elif (tx_min >= 0.3 and min(taxas_all) > 0
      and max(taxas_all) <= 1.4 * min(taxas_all)):
    verd_drift = 'PONTO-FIXO'
    say("      >>> taxa ~ CONSTANTE com desvio variando "
        f"{contraste:.0f}x: INSTABILIDADE DO PONTO FIXO — genuina.")
    say("      Primeiro no-go dinamico real do programa (nivel linear,")
    say("      fronteira declarada); R-4 herda com prioridade maxima.")
else:
    verd_drift = 'MISTO'
    say("      >>> nem desliga, nem proporcional, nem constante — MISTO")
    say("      (duas componentes?); reportar mapa e desenhar desempate.")
say("")
say("  secundario (k_c=1250, 3 pontos):")
say(f"    ORG (G=0): taxa={REF['org_t1250']:+.2f}  "
    f"R3b-F (G=30): {REF['g30_t1250']:+.2f}  "
    f"K (G={GAM_I:g}): {met_max(RK, 'tardia'):+.2f}")
say("")
say(f"  RESUMO: R3c-BETA = {verd_beta}; R3c-DRIFT = {verd_drift}"
    + ("" if ok_cont else "; CONT FALHOU"))

os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
with open(os.path.join(HERE, "out", "r3c_pousada_mecanismo.txt"),
          "w", encoding="utf-8") as fh:
    fh.write("\n".join(OUT))
say("")
say("concluido. saida em auditoria/code/out/r3c_pousada_mecanismo.txt")
