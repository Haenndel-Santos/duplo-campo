# -*- coding: utf-8 -*-
"""
r3_faseB_evolucao_rolagem.py — R-3 da fila de reavaliacao
(docs/resultado_d2_evolucao.md sec.6; estado atualizado em
docs/resultado_r1_reavaliacao.md sec.5 e docs/resultado_r2_fantasma.md
sec.5): a FASE B da Investigacao 2 refeita por EVOLUCAO REAL na
trajetoria de rolagem.

CONTEXTO. A Fase B (investigacao2_faseB_pert.py) leu o espectro
CONGELADO ao longo do fundo de rolagem (g=2, m_chi^2=30, v*=1, celula
REF mu=1) e achou sigma/H subindo com o deslocamento ate 13.08 na
janela-alvo (a ~ [760,2050]) e pousando em 4.25 — dai "o no-go se
estende ao regime nao-fatorado". O D2 mostrou que NESTA CLASSE o
espectro congelado nao e arbitro de saude (matrizes comoveis nunca
assentam; no estacionario o congelado preve 3-6.8H e a dinamica real
dilui a -3/2 H), e a R-1 confirmou em 14/14 celulas estacionarias. O
sigma/H~13 da rolagem e SUSPEITO pelas mesmas razoes — mas a rolagem
tem ingrediente novo (F'!=0, chi_dot!=0, fundo genuinamente dependente
do tempo), entao a resposta NAO esta dada. Este script poe a MESMA
maquinaria validada do D2/R-1 (reducao dependente do tempo com termos
C_dot, RK4, controles) sobre a trajetoria da Fase A/B, agora em
convencao COMOVEL REAL (a e b=r*a verdadeiros; sem o reescalonamento
a->1 da leitura congelada).

FILA REORDENADA PELO AUTOR (2026-08-11, noite;
docs/gate_fantasma_estrutural.md sec.4): R-3 -> R-4 -> Gate F ->
cap.07. Alem da pergunta principal, o R-3 DECIDE se o modo de
condensacao delta-phi_- (= delta-chi nesta base; o candidato dinamico
mais proximo da narrativa do Cap.1) sobrevive a dinamica real — a
Fase B era congelada; sec.5 do doc do gate: "a identificacao segue
prematura (aguarda R-3)".

DESENHO:
  - k_c em {1250, 12500}: k_phys ~ {1, 10} no CENTRO da janela-alvo
    (sqrt(760*2050) ~ 1250). Redshift inerente a evolucao real: k_phys
    varia fator ~200 ao longo de a in [100, 20000] — declarado.
  - fundo: reintegracao da trajetoria da Fase A/B (mesmo integrador,
    conferencia r_fim=0.4979 e chi/v=0.932), registro denso + splines
    cubicas p/ taxas suaves (K_dot, C_dot exigem derivadas limpas;
    conferencia spline vs gradiente-de-registro impressa).
  - janelas de taxa (normalizadas pelo H do meio):
      pre      [150, 450]    (pre-rolagem; congelado ja diz ~3.2H)
      rolagem  [760, 2050]   (janela-alvo da Fase A; congelado ate 13)
      pouso    [2100, 6800]  (anel do pouso)
      tardia   [8000, 18000] (familia modulada pousada; anel residual
                              |desl|~1e-2 declarado)
  - bloco METRICO vs delta-chi separados: a espinodal da condensacao em
    delta-chi (U''<0 enquanto chi~0, so em k_phys < sqrt(15)~3.9) e
    FISICA e esperada — nao e o no-go. Criterios usam a norma do bloco
    metrico (Psi_f, E_f) nas ICs metricas; trilhas de composicao
    impressas p/ nao confundir os dois destinos.

CRITERIOS PRE-DECLARADOS:
  R3-GR-A (controle, k UV): GR + chi ROLANTE no mesmo pipeline (fiacao
      chid/chidd/Up/Upp que nenhum controle anterior exercitou), com
      k_phys^2 > 2*mu2 na rolagem: nenhuma janela com taxa > +0.1H.
      FALHA -> abortar (crescimento espurio).
  R3-GR-B (controle positivo, k IR): k_phys < sqrt(mu2)/2 no inicio da
      rolagem: taxa da janela de rolagem >= 0.3 * sigma_espinodal do
      fundo GR E taxa tardia <= +0.1H (cresce onde DEVE e satura no
      pouso). FALHA -> abortar (pipeline nao detecta crescimento real
      dirigido por rolagem — sem poder de detecao).
  R3-PODER (por k): matrizes reduzidas CONGELADAS no pico da janela
      (a~1800) evoluidas com coeficientes constantes devem crescer a
      >= 0.5 * sigma* congelado (analogo formal da sonda P2 do D2).
      FALHA -> nao interpretar este k.
  R3-ROLAGEM (por k; a pergunta central): taxa metrica maxima (ICs
      metricas, norma do bloco metrico) na janela de rolagem:
        < 0.5*sigma*  -> NAO-REALIZA (o sigma/H congelado da rolagem e
                         vacuo como dinamica, como no D2/R-1);
        >= 0.5*sigma* -> REALIZA (primeiro veredito congelado a
                         sobreviver ao watershed do D2 — a instabilidade
                         nao-fatorada e DINAMICA; reportar taxas).
  R3-TARDIA (por k): todas as ICs metricas com taxa metrica < 0 na
      janela tardia -> DILUI (primeiro teste dinamico da familia
      modulada-POUSADA — novo alem da R-1, que so cobriu estacionarios
      beta-constantes); alguma >= 0.5*sigma_anc(tardia) -> CRESCE;
      senao MISTO.
  R3-TRANSIENTE: lnA_met maximo (ICs metricas) — o dano transiente da
      rolagem; comparar com a faixa 3.9-14.6 da R-1 (baseline diferente,
      a>=100 aqui vs 0.2 la: comparavel so como ordem de grandeza;
      insumo do R-4).
  R3-SPINODAL (diagnostico, sem criterio): taxa da IC delta-chi no k IR
      durante pre+rolagem vs sigma espinodal do fundo bimetrico
      (d ln chi / dN) — o crescimento delta-chi-dominado deve acompanhar
      o fundo e SARAR no pouso (o "duas instabilidades, destinos
      opostos" da Fase B, agora em dinamica real).
  R3-MECANISMO (diagnostico, sem criterio; gate_fantasma_estrutural.md
      sec.5): TIPO do crescimento na rolagem pela comparacao entre os
      dois k (razao 10): taxa ~ prop. a k -> tipo-gradiente (como a
      transiente do D2/R-1); ~ k-independente -> tipo-massa (a
      bifurcacao do Cap.1 e de massa; a identificacao com a narrativa
      fundacional deixaria de ser prematura). Vale p/ o bloco metrico
      E p/ o modo de condensacao (espinodal presente so em
      k_phys^2 < |U''|~15 ja e assinatura tipo-massa).
  Ancoras congeladas (a in {800,1250,1800} janela; {5000,15000} pousado):
      sigma/H e kN_min da REDUZIDA 3x3 (o instrumento cuja previsao a
      evolucao testa) + sigma/H e CONTAGEM do QEP 7x7 nos MESMOS args
      comoveis (ponte com a Fase B: em a=1250, k_c=1250 <-> k_phys=1;
      tabela da Fase B da ~8-11 ai) + negK (trilha do fantasma
      estrutural do R-2 estendida ao regime nao-fatorado).
  R3-ESTRUTURA: linhas K dos multiplicadores devem ser nulas em toda a
      trajetoria (checado na reducao). Violacao real = achado maior
      (estrutura de vinculos quebrada no nao-fatorado) — reportar ponto
      e magnitude, truncar a janela valida, nao silenciar.
  Halving (k_c=1250, npts x2): max|Delta taxa met| em rolagem+tardia
      < 0.05.

Requer sympy, numpy, scipy. ~15-25 min.
Uso (raiz do repo, venv ativo):
    python auditoria/code/r3_faseB_evolucao_rolagem.py
Saida em auditoria/code/out/r3_faseB_evolucao_rolagem.txt
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

from tdcp_pert_lib import (t, a_s, b_s, xi_s, H_s, Hf_s, Hd_s, Hfd_s, xid_s,
                           chid_s, chidd_s, Mg2, Mf2, m2, Meff2,
                           b0, b1, b2, b3, b4, Fb, Fp, Fpp,
                           Ub, Up, Upp, rho_s, k as ksym,
                           quadratic_matrices, lagrangian_GG,
                           chi_lagrangian, scalar_metric_g,
                           substitute_bg_functions, make_bg_functions,
                           z_average, eps_part, cut, symbolize)

T0 = time.time()
OUT = []


def say(*a):
    line = " ".join(str(x) for x in a)
    print(f"[{time.time()-T0:7.1f}s] {line}")
    OUT.append(line)


NOMES = ['Phi_g', 'B_g', 'Phi_f', 'Psi_f', 'B_f', 'E_f', 'dchi']
MULT = [0, 1, 2, 4]
DYN = [3, 5, 6]           # reduzido: 0=Psi_f, 1=E_f, 2=dchi
IDX_MET_IC = [0, 1, 3, 4]  # ICs metricas (q e qd de Psi_f, E_f)
JANELAS = [("pre", 150.0, 450.0), ("rolagem", 760.0, 2050.0),
           ("pouso", 2100.0, 6800.0), ("tardia", 8000.0, 18000.0)]
ANCORAS = [800.0, 1250.0, 1800.0, 5000.0, 15000.0]
ANC_JAN = [800.0, 1250.0, 1800.0]
MARCAS = [150, 300, 500, 760, 1000, 1250, 1500, 1800, 2050,
          3000, 5000, 8000, 12000, 18000]
A_MIN, A_MAX = 100.0, 20000.0
NPTS = 20000
K_CS = [1250.0, 12500.0]

# parametros do caso alvo (identicos a Fase A/B)
MU = 1.0
MG2, MF2 = 1.0, MU
ME2 = MU / (1.0 + MU)
M2 = 1.0
B0V, B2V, B4V = 1.0, -0.4, 0.5
B10 = 1.0
RHO0 = 0.3
VST = 1.0

say("=" * 72)
say("R-3 — FASE B DA INVESTIGACAO 2 POR EVOLUCAO REAL NA ROLAGEM")
say("=" * 72)

# ------------------------------------------------------------------
# V1 — selfcheck GR da biblioteca
# ------------------------------------------------------------------
if not d1.gr_selfcheck():
    say("[!] V1 (GR selfcheck da biblioteca) falhou — abortando")
    sys.exit(1)
say("[V1] GR selfcheck da biblioteca: PASSA")

# ------------------------------------------------------------------
# montagem 7x7 + fatias com taxas livres (identico a Fase B)
# ------------------------------------------------------------------
L2s, fields, vels = d1.build_L2()
K7, C7, W7 = quadratic_matrices(L2s, fields, vels)
if [str(f) for f in fields] != NOMES:
    raise RuntimeError("ordem de campos mudou")
say("[montagem] K,C,W 7x7 prontos")

say("[fatias] {Fb,Fp,Fpp} x {b0..b4}, taxas livres (pode demorar) ...")
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
# fundo: integrador da Fase A/B (verbatim; registro mais denso)
# ------------------------------------------------------------------
say("[fundo] reintegrando a trajetoria alvo (g=2, m_chi^2=30, v*=1) ...")

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


def integra_alvo(g_end=2.0, mchi2=30.0, vst=1.0, a0=0.01, a1=1e5, dN=5e-4):
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
        chidd = (-3 * H * chd - dU_pot(ch, mu2, lam)
                 - M2 * ME2 * dbeta1(ch, vst) * (xi + 3 * r))
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
    # taxas por diferenca central sobre o registro (recurso da Fase B,
    # mantido so p/ conferencia contra as splines)
    dNr = np.gradient(rec['N'])
    rec['Hd_grad'] = rec['H'] * np.gradient(rec['H']) / dNr
    rec['Hfd_grad'] = rec['H'] * np.gradient(rec['Hfv']) / dNr
    rec['xid_grad'] = rec['H'] * np.gradient(rec['xi']) / dNr
    return rec


BG = integra_alvo()
say(f"[fundo] ok — r_fim={BG['r'][-1]:.4f} (Fase A: 0.4979), "
    f"chi/v_fim={BG['ch'][-1]/BG['v']:.3f} (Fase A: 0.932)")
ok_fundo = (abs(BG['r'][-1] - 0.4979) < 0.005
            and abs(BG['ch'][-1] / BG['v'] - 0.932) < 0.005)
say(f"  [{'FUNDO CONFERE' if ok_fundo else 'FUNDO DIVERGE — nao interpretar'}]")
if not ok_fundo:
    sys.exit(1)

# splines cubicas (taxas suaves p/ K_dot, C_dot)
SPL = {kk: CubicSpline(BG['N'], BG[kk])
       for kk in ('r', 'xi', 'H', 'Hfv', 'ch', 'chd', 'chidd')}
D_H = SPL['H'].derivative()
D_HF = SPL['Hfv'].derivative()
D_XI = SPL['xi'].derivative()
D_CH = SPL['ch'].derivative()

say("")
say("[V-FUNDO-TAXAS] spline vs gradiente-de-registro (Fase B):")
for a_chk in (800.0, 1500.0, 5000.0):
    i_chk = int(np.argmin(np.abs(BG['a'] - a_chk)))
    N_chk = BG['N'][i_chk]
    H_chk = float(SPL['H'](N_chk))
    Hd_spl = H_chk * float(D_H(N_chk))
    Hfd_spl = H_chk * float(D_HF(N_chk))
    xid_spl = H_chk * float(D_XI(N_chk))
    dH = abs(Hd_spl - BG['Hd_grad'][i_chk]) / max(abs(Hd_spl), 1e-12)
    dHf = abs(Hfd_spl - BG['Hfd_grad'][i_chk]) / max(abs(Hfd_spl), 1e-12)
    dxi = abs(xid_spl - BG['xid_grad'][i_chk]) / max(abs(xid_spl), 1e-12)
    say(f"    a={a_chk:7.0f}: |dHd|/Hd={dH:.2e} |dHfd|/Hfd={dHf:.2e} "
        f"|dxid|/xid={dxi:.2e}  (esperado <5e-2)")

# sigma espinodal do fundo bimetrico (p/ R3-SPINODAL)
Ns_sp = np.linspace(np.log(200.0), np.log(2050.0), 400)
sig_sp_bg = float(np.max(D_CH(Ns_sp) / SPL['ch'](Ns_sp)))
say(f"[fundo] sigma espinodal (max d ln chi/dN em a=[200,2050]) = "
    f"{sig_sp_bg:.2f} /H")


def bg_ponto(N):
    """valores comoveis reais no ponto N (splines)."""
    H = float(SPL['H'](N))
    ch = float(SPL['ch'](N))
    mu2, lam, U0 = BG['mu2'], BG['lam'], BG['U0']
    a = np.exp(N)
    return dict(
        a=a, r=float(SPL['r'](N)), xi=float(SPL['xi'](N)), H=H,
        Hf=float(SPL['Hfv'](N)), ch=ch, chd=float(SPL['chd'](N)),
        chidd=float(SPL['chidd'](N)),
        Hd=H * float(D_H(N)), Hfd=H * float(D_HF(N)),
        xid=H * float(D_XI(N)),
        Ubv=U_pot(ch, mu2, lam, U0) + RHO0 / a**3,
        Upv=dU_pot(ch, mu2, lam), Uppv=-mu2 + 3 * lam * ch * ch)


# ------------------------------------------------------------------
# maquinaria de reducao + evolucao (D2/R-1, com norma metrica)
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
    """reduz ponto a ponto; em falha, trunca e reporta (R3-ESTRUTURA)."""
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
            say(f"    [R3-ESTRUTURA] reducao falhou em a={np.exp(Ns[p]):.1f}: "
                f"{e}")
            say("    (se for linha K de multiplicador nao-nula: ACHADO — "
                "estrutura de vinculos quebrada; trilha truncada aqui)")
            p_fim = p
            break
    Ns_t, Hs_t = Ns[:p_fim], Hs_arr[:p_fim]
    Kr, Cr, Wr = Kr[:p_fim], Cr[:p_fim], Wr[:p_fim]
    Krd = np.gradient(Kr, Ns_t, axis=0) * Hs_t[:, None, None]
    Crd = np.gradient(Cr, Ns_t, axis=0) * Hs_t[:, None, None]
    return Kr, Cr, Wr, Krd, Crd, Ns_t, Hs_t


def evolui(Kr, Cr, Wr, Krd, Crd, Ns, Hs_arr, janelas, marcas_alvo=None,
           evec_base=None, imax=None, met_idx=(0, 1)):
    """RK4 com base completa de ICs; taxas por janela nas normas total
    e METRICA (campos reduzidos em met_idx; None = usar norma total);
    lnA nas duas; trilhas de composicao p/ ICs 0 e 2."""
    npts = len(Ns)
    nd = Kr.shape[1]
    aas = np.exp(Ns)
    Hmid = {}
    for nome, lo, hi in janelas:
        pm = int(np.argmin(np.abs(aas - np.sqrt(lo * hi))))
        Hmid[nome] = Hs_arr[pm]
    taxas_f, taxas_m, amps_f, amps_m, trilhas = [], [], [], [], {}
    for ic in range(2 * nd):
        q = np.zeros(nd)
        qd = np.zeros(nd)
        if ic < nd:
            q[ic] = 1.0
        else:
            qd[ic - nd] = 1.0
        tcum = 0.0
        amp_f = 0.0
        amp_m = 0.0
        reg = {nome: [None] * 6 for nome, _, _ in janelas}
        marcas = ({am: None for am in marcas_alvo}
                  if (marcas_alvo is not None and ic in (0, 2)) else None)
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
            if met_idx is None:
                n2_m = n2_f
            else:
                n2_m = sum(q[j]**2 + qd[j]**2 for j in met_idx)
            ln_f = np.log(max(np.sqrt(n2_f), 1e-300))
            ln_m = np.log(max(np.sqrt(n2_m), 1e-300))
            amp_f = max(amp_f, ln_f)
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
                        proj = float('nan')
                        if ic == 0 and evec_base is not None:
                            y = np.concatenate([q, qd])
                            try:
                                coef = np.linalg.solve(
                                    evec_base, y.astype(complex))
                                proj = abs(coef[imax]) / max(
                                    np.linalg.norm(y), 1e-300)
                            except np.linalg.LinAlgError:
                                pass
                        marcas[am] = (ln_f, ln_m, n2_m / max(n2_f, 1e-300),
                                      proj)
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
        amps_f.append(amp_f)
        amps_m.append(amp_m if ic in IDX_MET_IC else float('nan'))
        if marcas is not None:
            trilhas[ic] = marcas
    return taxas_f, taxas_m, amps_f, amps_m, trilhas


# ------------------------------------------------------------------
# R3-GR — controle GR + chi ROLANTE (fiacao chid/chidd/Up/Upp)
# ------------------------------------------------------------------
say("")
say("=" * 72)
say("R3-GR — controle: GR + chi rolante no mesmo pipeline")
say("=" * 72)
Phi_gF = sp.Function('Phi_g')(t)
B_gF = sp.Function('B_g')(t)
dchiF = sp.Function('dchi')(t)
aF, bF, xiF, bg_rules = make_bg_functions()
g_gr = substitute_bg_functions(
    scalar_metric_g(Phi_gF, sp.Integer(0), B_gF, None), aF, bF, xiF)
L2_gr = z_average(eps_part(cut(lagrangian_GG(g_gr, Mg2)
                               + chi_lagrangian(g_gr, dchi=dchiF)), 2))
L2s_gr, f_gr, v_gr = symbolize(L2_gr, [Phi_gF, B_gF, dchiF], bg_rules)
Kg, Cg, Wg = quadratic_matrices(L2s_gr, f_gr, v_gr)
FIX_GR = {Mg2: 1, rho_s: 0}
LIV_GR = (a_s, H_s, Hd_s, chid_s, chidd_s, Ub, Up, Upp, ksym)
KgF = sp.lambdify(LIV_GR, Kg.subs(FIX_GR), 'numpy')
CgF = sp.lambdify(LIV_GR, Cg.subs(FIX_GR), 'numpy')
WgF = sp.lambdify(LIV_GR, Wg.subs(FIX_GR), 'numpy')

# fundo GR: mesmo potencial duplo-poco + piso Lambda_GR (evita H->0)
# [fix 2026-08-12] LAM_GR 0.1 -> 3.0: com piso baixo, H despencava
# (2.2 -> 0.18) durante a rolagem ingreme (mu2=15) e y=dchi/dN atingia
# o limite de kination (y^2=6), abortando o integrador semi-explicito.
# Piso maior mantem 3H > omega_poco (rolagem sobreamortecida, y pequeno);
# o controle segue valido: criterios sao autocalibrados no fundo medido.
LAM_GR = 3.0
MU2_GR, V_GR = BG['mu2'], BG['v']
LAM4_GR, U0_GR = BG['lam'], BG['U0']


def fundo_gr():
    dN = 1e-4
    N0, N1 = np.log(0.01), np.log(50000.0)
    n = int((N1 - N0) / dN) + 1
    ch, y = 1e-3 * V_GR, 0.0
    Hprev = None
    rec = {kk: [] for kk in ('N', 'a', 'H', 'Hd', 'ch', 'chd', 'chidd')}
    for i in range(n):
        N = N0 + i * dN
        a = np.exp(N)
        rho_d = RHO0 / a**3
        resto = U_pot(ch, MU2_GR, LAM4_GR, U0_GR) + LAM_GR + rho_d
        den = 3.0 - 0.5 * y * y
        if den <= 0 or resto <= 0:
            raise RuntimeError(f"fundo GR abortou (H^2) em a={a:.3f}")
        H = np.sqrt(resto / den)
        chd = H * y
        chidd = -3 * H * chd - dU_pot(ch, MU2_GR, LAM4_GR)
        Hd = -0.5 * (chd * chd + rho_d)
        Hp = 0.0 if Hprev is None else (H - Hprev) / dN
        yp = chidd / (H * H) - (Hp / H) * y
        if i % 4 == 0:
            for kk, vv in (('N', N), ('a', a), ('H', H), ('Hd', Hd),
                           ('ch', ch), ('chd', chd), ('chidd', chidd)):
                rec[kk].append(vv)
        ch += dN * y
        y += dN * yp
        Hprev = H
    return {kk: np.array(vv) for kk, vv in rec.items()}


BGR = fundo_gr()
if BGR['ch'][-1] < 0.9 * V_GR:
    say("  [!] fundo GR nao completou a rolagem ate a=50000 — abortando")
    sys.exit(1)
i10 = int(np.argmax(BGR['ch'] >= 0.1 * V_GR))
i90 = int(np.argmax(BGR['ch'] >= 0.9 * V_GR))
a10, a90 = BGR['a'][i10], BGR['a'][i90]
sel_rol = (BGR['a'] >= a10) & (BGR['a'] <= a90)
sig_sp_gr = float(np.max(np.gradient(np.log(BGR['ch']), BGR['N'])[sel_rol]))
say(f"    fundo GR: rolagem chi/v 0.1->0.9 em a=[{a10:.2f}, {a90:.2f}]; "
    f"sigma espinodal = {sig_sp_gr:.2f}/H")
gr_hi = min(60 * a90, 45000.0)
# [fix 2026-08-12] janela tardia adaptativa: com o roll sobreamortecido
# (LAM_GR=3.0), a90~5200 e a janela fixa [10*a90, 40000] ficava vazia
# (lo>hi -> NaN -> FALHA espuria). Pos-roll basta [3*a90, 8*a90],
# clampado ao range integrado.
tard_lo = 3 * a90
tard_hi = min(8 * a90, 0.9 * gr_hi)
if tard_lo >= tard_hi:
    tard_lo = 0.6 * tard_hi
JAN_GR = [("pre", a10 / 10, a10 / 2), ("rolagem", a10, a90),
          ("tardia", tard_lo, tard_hi)]
K_UV = 1.5 * np.sqrt(2 * MU2_GR) * a90
K_IR = 0.5 * np.sqrt(MU2_GR) * a10
SGR = {kk: CubicSpline(BGR['N'], BGR[kk])
       for kk in ('H', 'Hd', 'ch', 'chd', 'chidd')}

ok_gr = True
for rot, kg, npts_g in (("UV", K_UV, 40000), ("IR", K_IR, 16000)):
    Ns_g = np.linspace(np.log(a10 / 20), np.log(gr_hi), npts_g)
    Hs_g = np.zeros(len(Ns_g))
    Ms_g = {x: np.zeros((len(Ns_g), 3, 3)) for x in 'KCW'}
    for p, N in enumerate(Ns_g):
        a = np.exp(N)
        H = float(SGR['H'](N))
        ch = float(SGR['ch'](N))
        Hs_g[p] = H
        Ubv = (U_pot(ch, MU2_GR, LAM4_GR, U0_GR) + LAM_GR + RHO0 / a**3)
        args = (a, H, float(SGR['Hd'](N)), float(SGR['chd'](N)),
                float(SGR['chidd'](N)), Ubv,
                dU_pot(ch, MU2_GR, LAM4_GR),
                -MU2_GR + 3 * LAM4_GR * ch * ch, kg)
        Ms_g['K'][p] = np.array(KgF(*args), float)
        Ms_g['C'][p] = np.array(CgF(*args), float)
        Ms_g['W'][p] = np.array(WgF(*args), float)
    Kr, Cr, Wr, Krd, Crd, Ns_t, Hs_t = reduz_trilha(
        Ms_g, Ns_g, Hs_g, [0, 1], [2])
    tf, tm, af_, am_, _ = evolui(Kr, Cr, Wr, Krd, Crd, Ns_t, Hs_t, JAN_GR,
                                 met_idx=None)
    linha = {}
    for nome, _, _ in JAN_GR:
        fin = [tx[nome] for tx in tf if np.isfinite(tx[nome])]
        linha[nome] = max(fin) if fin else float('nan')
    say(f"    GR {rot} (k_c={kg:.1f}): taxas max/H = "
        + "  ".join(f"{nome}:{linha[nome]:+.2f}" for nome, _, _ in JAN_GR))
    if rot == "UV":
        ok_a = (np.isfinite(linha['rolagem'])
                and all(v <= 0.1 for v in linha.values()
                        if np.isfinite(v)))
        say(f"    [R3-GR-A {'PASSA' if ok_a else 'FALHA'}] "
            "(criterio: nenhuma janela > +0.1H)")
        ok_gr = ok_gr and ok_a
    else:
        ok_b = (np.isfinite(linha['rolagem'])
                and linha['rolagem'] >= 0.3 * sig_sp_gr
                and linha['tardia'] <= 0.1)
        say(f"    [R3-GR-B {'PASSA' if ok_b else 'FALHA'}] (criterio: "
            f"rolagem >= 0.3*{sig_sp_gr:.2f} e tardia <= +0.1H)")
        ok_gr = ok_gr and ok_b
if not ok_gr:
    say("  [!] controle GR rolante falhou — abortando (pre-declarado)")
    sys.exit(1)

# ------------------------------------------------------------------
# trajetoria bimetrica: matrizes comoveis reais + reducao + evolucao
# ------------------------------------------------------------------


def constroi(kc, npts):
    Ns = np.linspace(np.log(A_MIN), np.log(A_MAX), npts)
    Hs_arr = np.zeros(npts)
    Ms = {x: np.zeros((npts, 7, 7)) for x in 'KCW'}
    for p, N in enumerate(Ns):
        f = bg_ponto(N)
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


def qep7_no_ponto(N, kc):
    f = bg_ponto(N)
    args = (f['a'], f['r'] * f['a'], f['xi'], f['H'], f['Hf'],
            f['Hd'], f['Hfd'], f['xid'], f['chd'], f['chidd'],
            f['Ubv'], f['Upv'], f['Uppv'], kc, MF2, ME2)
    bvals = (B0V, beta1(f['ch'], VST), B2V, 0.0, B4V)
    bp = (0.0, dbeta1(f['ch'], VST), 0.0, 0.0, 0.0)
    bpp = (0.0, 2.0 * B10 / VST**2, 0.0, 0.0, 0.0)
    Kn = monta(FK, args, bvals, bp, bpp)
    Cn = monta(FC, args, bvals, bp, bpp)
    Wn = monta(FW, args, bvals, bp, bpp)
    # [fix 2026-08-12] pre-escala: em comovel real K ~ a^3 (>=1e11 em
    # a>=5000) e a linearizacao do QEP mistura blocos K com identidade
    # ~1 — eig degrada e filtra tudo (pares vazio). O QEP e invariante
    # sob (K,C,W) -> s*(K,C,W); normalizar por max|K| conserta o
    # condicionamento. kN devolvido na escala ORIGINAL (kN*sK).
    sK = max(np.max(np.abs(Kn)), 1e-30)
    pares = d1.agrupa_pares(d1.qep_modes(Kn / sK, Cn / sK, Wn / sK))
    if not pares:
        return 0, float('nan'), float('nan')
    sig = max(abs(np.sqrt(complex(mm['omega2'])).imag)
              for mm in pares) / f['H']
    kNmin = min(mm['knorm'] for mm in pares) * sK
    return len(pares), sig, kNmin


def poder_congelado(Kr0, Cr0, Wr0, H0, seed=42):
    """R3-PODER: matrizes constantes devem realizar o sigma congelado.
    [fix 2026-08-12] QEP com pre-escala (ver qep7_no_ponto)."""
    sK = max(np.max(np.abs(Kr0)), 1e-30)
    pares = d1.agrupa_pares(d1.qep_modes(Kr0 / sK, Cr0 / sK, Wr0 / sK))
    if not pares:
        return float('nan'), float('nan')
    sig = max(abs(np.sqrt(complex(mm['omega2'])).imag)
              for mm in pares) / H0
    om_max = max(abs(np.sqrt(complex(mm['omega2']))) for mm in pares)
    if sig < 1e-3:
        return sig, float('nan')
    dt = 0.2 / max(om_max, sig * H0)
    Ttot = 6.0 / (sig * H0)
    nst = min(int(Ttot / dt) + 1, 5_000_000)
    rng = np.random.default_rng(seed)
    y = rng.standard_normal(6)
    y /= np.linalg.norm(y)
    q, qd = y[:3].copy(), y[3:].copy()
    Ki = np.linalg.inv(Kr0)
    A = Cr0 - Cr0.T
    B = Wr0

    def rhs(qq, vv):
        return -Ki @ (A @ vv + B @ qq)

    ln_meio = None
    for s in range(nst):
        k1q, k1v = qd, rhs(q, qd)
        k2q, k2v = qd + .5 * dt * k1v, rhs(q + .5 * dt * k1q,
                                           qd + .5 * dt * k1v)
        k3q, k3v = qd + .5 * dt * k2v, rhs(q + .5 * dt * k2q,
                                           qd + .5 * dt * k2v)
        k4q, k4v = qd + dt * k3v, rhs(q + dt * k3q, qd + dt * k3v)
        q = q + dt * (k1q + 2 * k2q + 2 * k3q + k4q) / 6
        qd = qd + dt * (k1v + 2 * k2v + 2 * k3v + k4v) / 6
        if s == nst // 2:
            ln_meio = np.log(max(np.sqrt(q @ q + qd @ qd), 1e-300))
    ln_fim = np.log(max(np.sqrt(q @ q + qd @ qd), 1e-300))
    taxa = (ln_fim - ln_meio) / (dt * (nst - nst // 2)) / H0
    return sig, taxa


def roda_k(kc, npts, com_trilhas=True):
    say("")
    say(f"--- k_c = {kc:g}  (k_phys = {kc/1250:g} em a=1250, centro da "
        "janela) ---")
    Ns, Hs_arr, Ms = constroi(kc, npts)
    say(f"    [matrizes] {npts} pontos construidos")
    Kr, Cr, Wr, Krd, Crd, Ns_t, Hs_t = reduz_trilha(
        Ms, Ns, Hs_arr, MULT, DYN)
    a_max_val = float(np.exp(Ns_t[-1]))
    say(f"    [reducao] valida ate a={a_max_val:.0f}"
        + ("" if a_max_val > 0.99 * A_MAX else "  <<< TRUNCADA"))
    aas_t = np.exp(Ns_t)

    # ancoras congeladas (reduzida 3x3 + 7x7) + negK
    sig_anc = {}
    say(f"    {'a':>7} {'sig/H red':>10} {'kN_min red':>11} {'negK':>5} "
        f"{'sig/H 7x7':>10} {'npar':>5} {'kN_min 7x7':>11}  k_phys")
    for a_anc in ANCORAS:
        if a_anc > a_max_val:
            continue
        p_anc = int(np.argmin(np.abs(aas_t - a_anc)))
        # [fix 2026-08-12] pre-escala do QEP (ver qep7_no_ponto) + guarda
        sK = max(np.max(np.abs(Kr[p_anc])), 1e-30)
        pares = d1.agrupa_pares(d1.qep_modes(Kr[p_anc] / sK,
                                             Cr[p_anc] / sK,
                                             Wr[p_anc] / sK))
        if not pares:
            say(f"    {a_anc:7.0f}  (QEP reduzido sem modos finitos mesmo "
                "pre-escalado — ancora pulada; investigar se recorrente)")
            continue
        sig_r = max(abs(np.sqrt(complex(mm['omega2'])).imag)
                    for mm in pares) / Hs_t[p_anc]
        kN_r = min(mm['knorm'] for mm in pares) * sK
        eigK = np.linalg.eigvalsh(0.5 * (Kr[p_anc] + Kr[p_anc].T))
        negK = int(np.sum(eigK < -1e-12))
        np7, sig7, kN7 = qep7_no_ponto(Ns_t[p_anc], kc)
        say(f"    {a_anc:7.0f} {sig_r:10.2f} {kN_r:+11.1e} {negK:5d} "
            f"{sig7:10.2f} {np7:5d} {kN7:+11.1e}  {kc/a_anc:7.2f}")
        sig_anc[a_anc] = sig_r
    disp_jan = [sig_anc[aa] for aa in ANC_JAN if aa in sig_anc]
    sig_star = max(disp_jan) if disp_jan else float('nan')
    sig_tard = sig_anc.get(15000.0, float('nan'))
    say(f"    sigma* (max congelado reduzido na janela) = {sig_star:.2f}/H; "
        f"ancora tardia = {sig_tard:.2f}/H")
    say("    (ponte Fase B: em a=1250, k_c=1250 <-> k_phys=1; tabela da "
        "Fase B ~8-11 ai)")

    # R3-PODER no pico da janela + automodo p/ projecao
    ancs_ok = [aa for aa in ANC_JAN if aa <= a_max_val]
    if ancs_ok:
        a_pico = max(ancs_ok)
        p_star = int(np.argmin(np.abs(aas_t - a_pico)))
        sig_p, taxa_p = poder_congelado(Kr[p_star], Cr[p_star], Wr[p_star],
                                        Hs_t[p_star])
        ok_poder = np.isfinite(taxa_p) and taxa_p >= 0.5 * sig_p
        say(f"    [R3-PODER] congelado em a={a_pico:.0f}: sigma={sig_p:.2f}/H,"
            f" taxa realizada={taxa_p:+.2f}/H  "
            f"[{'PASSA' if ok_poder else 'FALHA — nao interpretar este k'}]")
        Amat = np.block(
            [[np.zeros((3, 3)), np.eye(3)],
             [-np.linalg.solve(Kr[p_star], Wr[p_star]),
              -np.linalg.solve(Kr[p_star], Cr[p_star] - Cr[p_star].T)]])
        ev, evec = np.linalg.eig(Amat)
        imax = int(np.argmax(ev.real))
    else:
        say("    [R3-PODER] trilha truncada antes da janela — sem ancora; "
            "PODER indisponivel")
        ok_poder = False
        evec, imax = None, None

    # evolucao real
    tf, tm, af_, am_, trilhas = evolui(
        Kr, Cr, Wr, Krd, Crd, Ns_t, Hs_t, JANELAS,
        marcas_alvo=(MARCAS if com_trilhas else None),
        evec_base=evec, imax=imax)
    say("")
    say(f"    taxas reais/H (norma total | norma METRICA), 6 ICs "
        f"(0,1,2=q Psi_f,E_f,dchi; 3,4,5=qd):")
    for nome, lo, hi in JANELAS:
        vf = [tx[nome] for tx in tf]
        vm = [tx[nome] for tx in tm]
        say(f"    {nome:<8}" + "".join(f"{v:+7.2f}" for v in vf)
            + "  |" + "".join(f"{v:+7.2f}" for v in vm))
    lnA_met = max(am_[i] for i in IDX_MET_IC)
    say(f"    lnA_met max (ICs metricas) = {lnA_met:.2f}   "
        f"lnA_total max = {max(af_):.2f}")
    if com_trilhas:
        for ic in (0, 2):
            rot = "IC0 (q Psi_f)" if ic == 0 else "IC2 (q dchi)"
            say(f"    trilha {rot}: a: ln|y| ln|y_met| frac_met"
                + ("  proj" if ic == 0 else "")
                + "   (frac_met->0 = delta-chi-dominado)")
            for am in MARCAS:
                v = trilhas.get(ic, {}).get(am)
                if v:
                    extra = f"  {v[3]:.2e}" if ic == 0 else ""
                    say(f"      a={am:5d}: {v[0]:+8.2f} {v[1]:+8.2f} "
                        f"{v[2]:6.3f}{extra}")
    return dict(tf=tf, tm=tm, lnA_met=lnA_met, sig_star=sig_star,
                sig_tard=sig_tard, ok_poder=ok_poder, a_max=a_max_val)


say("")
say("=" * 72)
say("EVOLUCAO REAL — trajetoria de rolagem, convencao comovel real")
say("=" * 72)
RES = {}
for kc in K_CS:
    RES[kc] = roda_k(kc, NPTS)

# halving no k IR
say("")
say(f"R3-CONV — halving (k_c={K_CS[0]:g}, {2*NPTS} pts), rolagem+tardia")
res2 = roda_k(K_CS[0], 2 * NPTS, com_trilhas=False)
dmax = 0.0
for nome in ("rolagem", "tardia"):
    for i in IDX_MET_IC:
        v1 = RES[K_CS[0]]['tm'][i][nome]
        v2 = res2['tm'][i][nome]
        if np.isfinite(v1) and np.isfinite(v2):
            dmax = max(dmax, abs(v1 - v2))
ok_conv = dmax < 0.05
say(f"    max|Delta taxa met| = {dmax:.4f} (criterio < 0.05)  "
    f"[{'PASSA' if ok_conv else 'FALHA'}]")

# ------------------------------------------------------------------
# veredito
# ------------------------------------------------------------------
say("")
say("=" * 72)
say("VEREDITO R-3 (criterios pre-declarados no cabecalho)")
say("=" * 72)
say(f"  R3-GR-A/B: PASSAM   R3-CONV: {'PASSA' if ok_conv else 'FALHA'}")
verd = {}
for kc in K_CS:
    r = RES[kc]
    fin_rol = [r['tm'][i]['rolagem'] for i in IDX_MET_IC
               if np.isfinite(r['tm'][i]['rolagem'])]
    t_rol = max(fin_rol) if fin_rol else float('nan')
    t_tar = [r['tm'][i]['tardia'] for i in IDX_MET_IC]
    realiza = np.isfinite(t_rol) and t_rol >= 0.5 * r['sig_star']
    if all(np.isfinite(v) and v < 0.0 for v in t_tar):
        v_tar = 'DILUI'
    elif any(np.isfinite(v) and np.isfinite(r['sig_tard'])
             and v >= 0.5 * r['sig_tard'] for v in t_tar):
        v_tar = 'CRESCE'
    else:
        v_tar = 'MISTO'
    verd[kc] = (r['ok_poder'], realiza, v_tar)
    say(f"  k_c={kc:g}: PODER {'ok' if r['ok_poder'] else 'FALHOU'}; "
        f"rolagem max met {t_rol:+.2f} vs 0.5*sigma*={0.5*r['sig_star']:.2f} "
        f"-> {'REALIZA' if realiza else 'NAO-REALIZA'}; "
        f"tardia {['%+.2f' % v for v in t_tar]} -> {v_tar}; "
        f"lnA_met={r['lnA_met']:.2f}")
say("")
poder_ok = all(v[0] for v in verd.values())
if not poder_ok:
    say("  >>> R3-PODER falhou em algum k — NAO INTERPRETAR esse k; ver")
    say("  acima qual, e diagnosticar antes de qualquer enunciado.")
if poder_ok and not any(v[1] for v in verd.values()):
    say("  >>> O sigma/H ate ~13 da Fase B NAO se realiza dinamicamente:")
    say("  a extensao do no-go ao regime nao-fatorado e VACUA como")
    say("  veredito dinamico (fica como caracterizacao do espectro")
    say("  congelado). O quadro D2/R-1 se estende a rolagem.")
    if all(v[2] == 'DILUI' for v in verd.values()):
        say("  E MAIS: a janela tardia DILUI nos dois k — primeiro teste")
        say("  dinamico da familia modulada-POUSADA (alem da R-1, que so")
        say("  cobriu estacionarios beta-constantes): estavel.")
    say("  O dano real da rolagem e o transiente lnA_met acima (comparar")
    say("  com 3.9-14.6 da R-1 como ordem de grandeza; insumo do R-4).")
    say("  FRONTEIRA declarada: uma trajetoria (g=2, m30), celula REF,")
    say("  k_c={1250,12500} (k_phys~{1,10} no centro da janela; redshift")
    say("  fator ~200 no range), janelas declaradas, nivel linear.")
elif poder_ok:
    say("  >>> CRESCIMENTO METRICO REAL NA ROLAGEM da ordem do congelado:")
    say("  primeiro veredito congelado a SOBREVIVER ao watershed do D2 —")
    say("  a instabilidade nao-fatorada e DINAMICA. A Fase B volta a")
    say("  valer como no-go dinamico neste regime; reportar taxas e lnA")
    say("  acima e mapear (mais k, mais trajetorias) no R-4.")
say("")
say("  R3-SPINODAL (diagnostico): sigma espinodal do fundo = "
    f"{sig_sp_bg:.2f}/H; comparar com a trilha IC2 do k_c=1250 acima")
say("  (crescimento delta-chi-dominado deve acompanhar o fundo e sarar")
say("  no pouso — 'duas instabilidades, destinos opostos' em dinamica")
say("  real).")


def _max_fin(vals):
    fin = [v for v in vals if np.isfinite(v)]
    return max(fin) if fin else float('nan')


say("")
say("  R3-MECANISMO (diagnostico; gate_fantasma_estrutural.md sec.5 —")
say("  a bifurcacao do Cap.1 e de massa; a transiente do D2/R-1 e")
say("  tipo-gradiente):")
kA, kB = K_CS
mA = _max_fin([RES[kA]['tm'][i]['rolagem'] for i in IDX_MET_IC])
mB = _max_fin([RES[kB]['tm'][i]['rolagem'] for i in IDX_MET_IC])
cA = _max_fin([RES[kA]['tf'][i]['rolagem'] for i in (2, 5)])
cB = _max_fin([RES[kB]['tf'][i]['rolagem'] for i in (2, 5)])
say(f"    rolagem, bloco metrico:       {mA:+.2f}/H (k_c={kA:g}) vs "
    f"{mB:+.2f}/H (k_c={kB:g}; razao k=10)")
say(f"    rolagem, delta-chi (ICs 2,5): {cA:+.2f}/H vs {cB:+.2f}/H")
say("    leitura: taxa ~ prop. a k -> tipo-gradiente; ~ k-independente")
say("    -> tipo-massa; espinodal presente so no k IR ja e assinatura")
say("    tipo-massa do modo de condensacao.")

os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
with open(os.path.join(HERE, "out", "r3_faseB_evolucao_rolagem.txt"),
          "w", encoding="utf-8") as fh:
    fh.write("\n".join(OUT))
say("")
say("concluido. saida em auditoria/code/out/r3_faseB_evolucao_rolagem.txt")
