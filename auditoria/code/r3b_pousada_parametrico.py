# -*- coding: utf-8 -*-
"""
r3b_pousada_parametrico.py — R-3b: follow-up do achado novo da R-3
(docs/resultado_r3_rolagem.md sec.1.3 + caveat sec.3.4): o crescimento
tardio real ~+1H na familia modulada-POUSADA e (a) convergido? e
(b) bombeamento parametrico pelas oscilacoes residuais de chi, ou
instabilidade genuina do fundo pousado?

CONTEXTO. A R-3 encontrou, na janela tardia (a in [8000,18000]) do
fundo pousado (chi=0.932v, modulacao forte beta1(chi)=4.47), taxas
reais POSITIVAS: k_c=12500 -> todas as 4 ICs metricas a +0.98/H (e o
bloco delta-chi a +1.25/H); k_c=1250 -> uma IC (q E_f) a +1.05/H.
Abaixo do limiar pre-declarado de CRESCE (0.5*sigma_anc), logo MISTO —
mas e o PRIMEIRO crescimento tardio real do programa (R-1: 14/14
celulas beta-constantes diluiam). Hipotese nomeada (nivel 3, doc R-3):
bombeamento parametrico pelas oscilacoes residuais de chi do fundo
pousado (omega_chi/H ~ 4.4; anel residual |desl|~1e-2). Evidencia a
favor: o MESMO k_phys na fase rolante DECAI (nao e k_phys, e o estado
do fundo). Teste declarado no doc: reintegrar o fundo com as
oscilacoes amortecidas a mao — se o crescimento sumir, e parametrico
(fenomeno tipo-preheating da familia modulada); se persistir, a
familia pousada tem instabilidade tardia genuina e o R-4 herda a
questao com prioridade. CAVEAT sec.3.4: o halving da rodada R-3 cobriu
so k_c=1250 — o k do achado (12500) esta SEM controle de convergencia;
este script ABRE por ele.

DESENHO (mesma maquinaria da R-3, verbatim — reducao dependente do
tempo com C_dot, RK4, janelas e normas identicas; grade a=[100,20000]):
  Fundos:
    ORG = trajetoria original da Fase A/B (mesmo integrador da R-3);
    DAM = mesma trajetoria com friccao artificial no chi a partir do
          pouso: chidd += -Gamma(a)*H*chid, Gamma = 30 * degrau suave
          em a=2400 (largura 0.03 em ln a). Antes de a~2100 os dois
          fundos sao IDENTICOS (checado: R3b-CONT). O amortecimento e
          fisicamente um canal de decaimento do chi; a constraint
          Omega=0 segue imposta ponto a ponto (r via raiz), H via
          Friedmann — fundo autoconsistente. Conferencia r_fim/chi_fim
          nos DOIS fundos.
  Rodadas (todas com as 6 ICs, normas total e METRICA):
    A: ORG, k_c=12500, npts=20000  — baseline (reproducao da rodada
       oficial da R-3: criterio R3b-BASE);
    B: ORG, k_c=12500, npts=40000  — HALVING do k do achado (R3b-CONV);
    C: DAM, k_c=12500, npts=20000  — o teste A/B principal (R3b-PARAM);
    D: ORG, k_c=25000, npts=20000  — sonda de BANDA: se o mecanismo e
       ressonancia parametrica com omega_chi, o crescimento local deve
       concentrar-se onde k_phys(a) cruza omega_chi/2, i.e. a_band =
       2*k_c/omega_chi (aprox. sem massa; declarada). Para k_c=12500,
       a_band ~ 5100 (janela do POUSO — onde a R-3 mediu +2.3/H!);
       para 25000, a_band cai na TARDIA;
    E: DAM, k_c=25000, npts=20000  — A/B do braco de banda;
    F: DAM, k_c=1250,  npts=20000  — A/B do braco IR (original oficial:
       IC E_f a +1.05/H na tardia).
  Medidas de fundo: omega_chi medido por cruzamentos de zero de chid
  em a=[4000,18000] (ORG); amplitude de oscilacao por janela
  (max|desl| e max|chi-chi_fim|/chi_fim) nos DOIS fundos — prova de
  que o amortecimento funcionou (fator esperado >30 na tardia).

CRITERIOS PRE-DECLARADOS:
  R3b-BASE: a rodada A reproduz as taxas metricas oficiais da R-3
      (pouso [2.31,2.37,2.29,2.33], tardia [0.98,0.98,0.98,0.98]) com
      max|Delta| < 0.05. FALHA -> NAO INTERPRETAR (drift de
      arquivo/ambiente; diagnosticar antes).
  R3b-CONV (o caveat sec.3.4): max|A - B| das taxas metricas (ICs
      metricas, pouso+tardia) < 0.05 -> o achado sec.1.3 e CONVERGIDO.
      FALHA -> RETRATAR o achado como artefato de resolucao (reportar
      os deltas; o doc R-3 e emendado).
  R3b-CONT: pre e rolagem de C devem coincidir com A (max|Delta| das 6
      ICs < 0.1 nas duas janelas) — os fundos so divergem apos o
      amortecimento ligar. FALHA -> nao interpretar C (vazamento do
      amortecimento p/ tras; rever A_DAMP/LARG).
  R3b-PARAM (por braco amortecido, na TARDIA, taxa metrica maxima):
      t_org = braco original correspondente (A p/ C; D p/ E; oficial
      +1.05 p/ F). Se t_org < 0.3: braco N/A (original ja pequeno).
        t_dam < 0.3 E t_dam < 0.3*t_org  -> SOME   (parametrico);
        t_dam >= 0.7*t_org               -> PERSISTE (genuina);
        senao                            -> PARCIAL.
      AGREGADO: todos os bracos informativos SOME -> BOMBEAMENTO
      PARAMETRICO CONFIRMADO — o crescimento tardio da R-3 e
      tipo-preheating da familia modulada (transiente: a fonte decai
      ~a^-3/2; dano extra finito), e a familia pousada volta a
      "estavel modulo transiente de pouso". Algum PERSISTE ->
      INSTABILIDADE TARDIA GENUINA da familia modulada-pousada no(s)
      braco(s) — primeiro no-go dinamico real do programa; R-4 herda
      com prioridade maxima. Misto -> reportar mapa (duas componentes?).
  R3b-BANDA (diagnostico, sem criterio duro): perfil de taxa local
      (IC0, met, entre marcas) de D e A impresso com o cruzamento de
      banda marcado; leitura no doc. Se o pico local de D cair na
      faixa [0.7,1.4]*a_band, suporte adicional a hipotese.
  Ancoras (a in {5000,15000}, reduzida 3x3 com pre-escala + negK):
      impressas p/ TODOS os bracos — em particular, se sigma/H
      congelado do fundo DAM ~= do ORG enquanto a dinamica muda, mais
      uma prova de que o congelado nao ve o mecanismo; negK=1 esperado
      tambem no fundo amortecido (assinatura estrutural, nao
      oscilatoria — insumo Gate F).
  Controles herdados (declarado): GR-A/B e R3-PODER da R-3 valem
      (mesmas funcoes, mesma rota, mesmos k exceto 25000 — braco D/E e
      A/B diagnostico, nao veredito de saude isolado).

Requer sympy, numpy, scipy. ~8-15 min.
Uso (raiz do repo, venv ativo):
    python auditoria/code/r3b_pousada_parametrico.py
Saida em auditoria/code/out/r3b_pousada_parametrico.txt
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
MARCAS_B = [300, 760, 1250, 2100, 2600, 3200, 4000, 5000, 6800,
            8000, 10000, 12000, 15000, 18000]
ANCORAS_B = [5000.0, 15000.0]
A_MIN, A_MAX = 100.0, 20000.0
NPTS = 20000

K_MAIN, K_BANDA, K_IR = 12500.0, 25000.0, 1250.0
REF_OFICIAL = {"pouso": [2.31, 2.37, 2.29, 2.33],
               "tardia": [0.98, 0.98, 0.98, 0.98]}
REF_T_K1250 = 1.05  # IC q E_f, tardia met, rodada oficial R-3

# amortecimento artificial do chi (fundo DAM)
GAM0 = 30.0
A_DAMP = 2400.0
LARG = 0.03

# parametros do caso alvo (identicos a R-3 / Fase A/B)
MU = 1.0
MG2, MF2 = 1.0, MU
ME2 = MU / (1.0 + MU)
M2 = 1.0
B0V, B2V, B4V = 1.0, -0.4, 0.5
B10 = 1.0
RHO0 = 0.3
VST = 1.0

say("=" * 72)
say("R-3b — FAMILIA POUSADA: CONVERGENCIA + TESTE DO BOMBEAMENTO")
say("=" * 72)

# ------------------------------------------------------------------
# V1 + montagem + fatias (verbatim R-3)
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
# fundo (verbatim R-3, com friccao opcional gam0 no chi)
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


say("")
say("[fundo ORG] reintegrando a trajetoria original ...")
BG_ORG = integra_alvo()
say(f"    r_fim={BG_ORG['r'][-1]:.4f} (ref 0.4979), "
    f"chi/v_fim={BG_ORG['ch'][-1]/BG_ORG['v']:.3f} (ref 0.932)")
ok_org = (abs(BG_ORG['r'][-1] - 0.4979) < 0.005
          and abs(BG_ORG['ch'][-1] / BG_ORG['v'] - 0.932) < 0.005)
say(f"    [{'CONFERE' if ok_org else 'DIVERGE — abortar'}]")
if not ok_org:
    sys.exit(1)

say(f"[fundo DAM] mesma trajetoria com Gamma={GAM0:g} ligando em "
    f"a={A_DAMP:g} (largura {LARG:g} em ln a) ...")
BG_DAM = integra_alvo(gam0=GAM0)
say(f"    r_fim={BG_DAM['r'][-1]:.4f} (ref 0.4979), "
    f"chi/v_fim={BG_DAM['ch'][-1]/BG_DAM['v']:.3f} (ref 0.932)")
ok_dam = (abs(BG_DAM['r'][-1] - 0.4979) < 0.01
          and abs(BG_DAM['ch'][-1] / BG_DAM['v'] - 0.932) < 0.01)
say(f"    [{'CONFERE' if ok_dam else 'DIVERGE — abortar'}]")
if not ok_dam:
    sys.exit(1)

CTX_ORG = make_ctx(BG_ORG, "ORG")
CTX_DAM = make_ctx(BG_DAM, "DAM")

# ------------------------------------------------------------------
# medidas de fundo: omega_chi, amplitudes de oscilacao por janela
# ------------------------------------------------------------------


def osc_janela(rec, lo, hi):
    msk = (rec['a'] >= lo) & (rec['a'] <= hi)
    if not np.any(msk):
        return float('nan'), float('nan')
    ch_fim = rec['ch'][-1]
    d_max = float(np.max(np.abs(rec['desl'][msk])))
    a_osc = float(np.max(np.abs(rec['ch'][msk] - ch_fim)) / ch_fim)
    return d_max, a_osc


def mede_omega_chi(rec, lo=2600.0, hi=90000.0):
    """janela larga: o periodo da oscilacao pousada e ~1.4 em ln a
    (omega/H ~ 4.4), entao [4000,18000] teria ~1 periodo so — usar
    [2600, 90000] (~2.5 periodos, >=5 cruzamentos)."""
    msk = (rec['a'] >= lo) & (rec['a'] <= hi)
    N = rec['N'][msk]
    H = rec['H'][msk]
    chd = rec['chd'][msk]
    if len(N) < 10:
        return float('nan'), float('nan'), 0
    dt = np.diff(N) / H[:-1]
    tt = np.concatenate([[0.0], np.cumsum(dt)])
    tc = []
    for i in range(len(chd) - 1):
        if chd[i] == 0.0 or chd[i] * chd[i + 1] < 0:
            frac = abs(chd[i]) / max(abs(chd[i]) + abs(chd[i + 1]), 1e-300)
            tc.append(tt[i] + frac * (tt[i + 1] - tt[i]))
    if len(tc) < 4:
        return float('nan'), float('nan'), len(tc)
    dtc = np.diff(tc)
    om = np.pi / np.mean(dtc)
    i_mid = int(np.argmin(np.abs(rec['a'] - 12000.0)))
    return float(om), float(om / rec['H'][i_mid]), len(tc)


say("")
say("[fundo] medidas de oscilacao residual:")
OM_CHI, OM_SOBRE_H, N_CRUZ = mede_omega_chi(BG_ORG)
say(f"    omega_chi (ORG, {N_CRUZ} cruzamentos de chid em "
    f"a=[2600,90000]) = {OM_CHI:.2f}  ->  omega_chi/H = "
    f"{OM_SOBRE_H:.2f}  (doc R-3 estimava ~4.4)")
A_BAND = {kc: 2.0 * kc / OM_CHI if np.isfinite(OM_CHI) else float('nan')
          for kc in (K_MAIN, K_BANDA, K_IR)}
say(f"    a_band = 2 k_c / omega_chi (aprox. sem massa):  "
    + "  ".join(f"k={kc:g}: {A_BAND[kc]:.0f}" for kc in (K_MAIN, K_BANDA)))
say(f"    {'janela':<8} {'|desl| ORG':>11} {'|desl| DAM':>11} "
    f"{'Aosc ORG':>9} {'Aosc DAM':>9}")
for nome, lo, hi in JANELAS[2:]:
    dO, aO = osc_janela(BG_ORG, lo, hi)
    dD, aD = osc_janela(BG_DAM, lo, hi)
    say(f"    {nome:<8} {dO:11.2e} {dD:11.2e} {aO:9.2e} {aD:9.2e}")

# ------------------------------------------------------------------
# reducao + evolucao (verbatim R-3)
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


def constroi(ctx, kc, npts):
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


def roda(rotulo, ctx, kc, npts, trilhas_on=True, aband=None):
    say("")
    say(f"--- {rotulo}: fundo {ctx['rotulo']}, k_c={kc:g}, npts={npts} ---")
    Ns, Hs_arr, Ms = constroi(ctx, kc, npts)
    Kr, Cr, Wr, Krd, Crd, Ns_t, Hs_t = reduz_trilha(Ms, Ns, Hs_arr,
                                                    MULT, DYN)
    a_max_val = float(np.exp(Ns_t[-1]))
    if a_max_val < 0.99 * A_MAX:
        say(f"    [reducao] TRUNCADA em a={a_max_val:.0f}")
    aas_t = np.exp(Ns_t)
    # ancoras reduzidas (pre-escala; negK)
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
                              marcas_alvo=(MARCAS_B if trilhas_on
                                           else None))
    say("    taxas reais/H (norma total | norma METRICA), 6 ICs:")
    for nome, lo, hi in JANELAS:
        vf = [tx[nome] for tx in tf]
        vm = [tx[nome] for tx in tm]
        say(f"    {nome:<8}" + "".join(f"{v:+7.2f}" for v in vf)
            + "  |" + "".join(f"{v:+7.2f}" for v in vm))
    lnA_met = max(am_[i] for i in IDX_MET_IC)
    say(f"    lnA_met max = {lnA_met:.2f}")
    if trilhas_on and 0 in trl:
        say("    perfil local (IC0, met): a1->a2: taxa_loc/H"
            + (f"   [a_band ~ {aband:.0f}]" if aband else ""))
        ams = [am for am in MARCAS_B if trl[0].get(am)]
        for j in range(len(ams) - 1):
            a1, a2 = ams[j], ams[j + 1]
            v1, v2 = trl[0][a1], trl[0][a2]
            tloc = (v2[1] - v1[1]) / np.log(a2 / a1)
            flag = (" <-- banda" if (aband and a1 <= aband <= a2) else "")
            say(f"      {a1:6d}->{a2:6d}: {tloc:+7.2f}{flag}")
    return dict(tf=tf, tm=tm, lnA=lnA_met, a_max=a_max_val)


def met_vals(res, nome):
    return [res['tm'][i][nome] for i in IDX_MET_IC]


def met_max(res, nome):
    fin = [v for v in met_vals(res, nome) if np.isfinite(v)]
    return max(fin) if fin else float('nan')


# ------------------------------------------------------------------
# rodadas
# ------------------------------------------------------------------
say("")
say("=" * 72)
say("RODADAS A-F")
say("=" * 72)
RA = roda("A (baseline oficial)", CTX_ORG, K_MAIN, NPTS, aband=A_BAND[K_MAIN])
RB = roda("B (halving do achado)", CTX_ORG, K_MAIN, 2 * NPTS,
          trilhas_on=False)
RC = roda("C (teste A/B principal)", CTX_DAM, K_MAIN, NPTS,
          aband=A_BAND[K_MAIN])
RD = roda("D (sonda de banda)", CTX_ORG, K_BANDA, NPTS, aband=A_BAND[K_BANDA])
RE = roda("E (A/B da banda)", CTX_DAM, K_BANDA, NPTS, trilhas_on=False)
RF = roda("F (A/B do braco IR)", CTX_DAM, K_IR, NPTS, trilhas_on=False)

# ------------------------------------------------------------------
# vereditos
# ------------------------------------------------------------------
say("")
say("=" * 72)
say("VEREDITO R-3b (criterios pre-declarados no cabecalho)")
say("=" * 72)

# R3b-BASE
d_base = 0.0
for nome in ("pouso", "tardia"):
    for v_med, v_ref in zip(met_vals(RA, nome), REF_OFICIAL[nome]):
        if np.isfinite(v_med):
            d_base = max(d_base, abs(v_med - v_ref))
ok_base = d_base < 0.05
say(f"  R3b-BASE: max|A - oficial| = {d_base:.3f} (criterio < 0.05)  "
    f"[{'PASSA' if ok_base else 'FALHA — NAO INTERPRETAR'}]")

# R3b-CONV
d_conv = 0.0
for nome in ("pouso", "tardia"):
    for v1, v2 in zip(met_vals(RA, nome), met_vals(RB, nome)):
        if np.isfinite(v1) and np.isfinite(v2):
            d_conv = max(d_conv, abs(v1 - v2))
ok_conv = d_conv < 0.05
say(f"  R3b-CONV: max|A - B| = {d_conv:.4f} (criterio < 0.05)  "
    f"[{'PASSA — achado sec.1.3 CONVERGIDO' if ok_conv else 'FALHA — RETRATAR o achado (artefato de resolucao)'}]")

# R3b-CONT
d_cont = 0.0
for nome in ("pre", "rolagem"):
    for i in range(6):
        v1, v2 = RA['tm'][i][nome], RC['tm'][i][nome]
        if np.isfinite(v1) and np.isfinite(v2):
            d_cont = max(d_cont, abs(v1 - v2))
ok_cont = d_cont < 0.1
say(f"  R3b-CONT: max|A - C| em pre+rolagem = {d_cont:.4f} "
    f"(criterio < 0.1)  [{'PASSA' if ok_cont else 'FALHA — amortecimento vazou p/ tras'}]")


def param_arm(nome_arm, t_dam, t_org):
    if not np.isfinite(t_dam) or not np.isfinite(t_org):
        v = 'INDEFINIDO'
    elif t_org < 0.3:
        v = 'N/A (original ja pequeno)'
    elif t_dam < 0.3 and t_dam < 0.3 * t_org:
        v = 'SOME'
    elif t_dam >= 0.7 * t_org:
        v = 'PERSISTE'
    else:
        v = 'PARCIAL'
    say(f"    {nome_arm}: original {t_org:+.2f}/H -> amortecido "
        f"{t_dam:+.2f}/H  => {v}")
    return v


say("  R3b-PARAM (taxa metrica max na TARDIA):")
v1 = param_arm("C vs A  (k=12500)", met_max(RC, 'tardia'),
               met_max(RA, 'tardia'))
v2 = param_arm("E vs D  (k=25000)", met_max(RE, 'tardia'),
               met_max(RD, 'tardia'))
v3 = param_arm("F vs oficial (k=1250)", met_max(RF, 'tardia'),
               REF_T_K1250)
say("    (secundario, POUSO) C vs A: "
    f"{met_max(RC, 'pouso'):+.2f} vs {met_max(RA, 'pouso'):+.2f}")

say("")
verds = [v for v in (v1, v2, v3) if v in ('SOME', 'PERSISTE', 'PARCIAL')]
if ok_base and ok_conv and ok_cont:
    if verds and all(v == 'SOME' for v in verds):
        say("  >>> BOMBEAMENTO PARAMETRICO CONFIRMADO: o crescimento")
        say("  tardio da R-3 (sec.1.3) desaparece quando as oscilacoes")
        say("  residuais de chi sao amortecidas — e um fenomeno")
        say("  tipo-preheating da familia modulada (fonte decai ~a^-3/2;")
        say("  dano transiente finito), nao instabilidade do vacuo")
        say("  pousado. A familia modulada-pousada fica 'estavel modulo")
        say("  transiente de pouso'. O enunciado do cap.07 ganha o item")
        say("  na forma fraca; o R-4 mapeia o dano (lnA) incluindo esta")
        say("  componente.")
    elif any(v == 'PERSISTE' for v in verds):
        say("  >>> CRESCIMENTO PERSISTE sem oscilacoes no(s) braco(s)")
        say("  marcado(s): INSTABILIDADE TARDIA GENUINA da familia")
        say("  modulada-pousada — primeiro no-go dinamico real do")
        say("  programa (nivel linear, fronteira declarada). R-4 herda")
        say("  com prioridade maxima: mapear em k/celulas/trajetorias.")
    else:
        say("  >>> resultado PARCIAL/misto — duas componentes possiveis")
        say("  (parametrica + residual)? Reportar mapa acima; nao")
        say("  concluir mecanismo unico. Rota a>50000 (doc R-3 sec.1.3)")
        say("  vira o desempate.")
else:
    say("  >>> pre-condicoes falharam (BASE/CONV/CONT) — ver acima; nao")
    say("  interpretar os bracos A/B ate diagnosticar.")

say("")
say("  R3b-BANDA (diagnostico): a_band(k=12500) ~ "
    f"{A_BAND[K_MAIN]:.0f} (pouso), a_band(k=25000) ~ "
    f"{A_BAND[K_BANDA]:.0f} (tardia) — conferir os perfis locais de A e")
say("  D acima: pico local na faixa [0.7,1.4]*a_band apoia a hipotese;")
say("  leitura final no doc.")

os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
with open(os.path.join(HERE, "out", "r3b_pousada_parametrico.txt"),
          "w", encoding="utf-8") as fh:
    fh.write("\n".join(OUT))
say("")
say("concluido. saida em auditoria/code/out/r3b_pousada_parametrico.txt")
