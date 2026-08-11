# -*- coding: utf-8 -*-
"""
investigacao2_faseB_pert.py — Investigacao 2, FASE B: perturbacoes ao
longo do fundo de rolagem (p_phi != 0).

CONTEXTO. A Fase A (docs/resultado_investigacao2_faseA.md) estabeleceu
o fundo: na trajetoria g=2, m_chi^2=30, v*=1 (celula REF mu=1), a
condensacao de phi_- desloca o fundo ORDEM 1 dos dois ramos
(|H - r H_f|/H ate 0.48, janela-alvo a ~ [760, 2050]), dirige r
(0.031 -> 0.498) e pousa de volta no ramo finito. Esta fase poe o QEP
7x7 (a MESMA maquinaria de todas as ancoras) sobre essa trajetoria,
com chid != 0, chidd != 0, Hdot/H_fdot/xidot != 0 e modulacao POR
COEFICIENTE beta_1(chi) via fatias {Fb,Fp,Fpp}x{beta_n} (tecnica
validada pelo T1 de modulacao_qep.py, agora com as taxas LIVRES).

TRES PERGUNTAS (criterios pre-declarados):

G2b-CONTAGEM — o fantasma BD volta no regime nao-fatorado?
    A remocao do modo BD depende do par de constraints
    (primaria+secundaria). No regime p_phi!=0 a secundaria e outra
    (nao-fatorada). Contagem de pares finitos no QEP:
      >= 4 pares em AMBOS os k no mesmo ponto  -> BD FALSIFICADO
         (Gate 2 Parte B falha por rota numerica — conclusivo);
      >= 4 em so um k -> SUSPEITO (reportar, nao concluir);
      3 em toda parte -> COMPATIVEL, mas NAO certifica (assimetria
         declarada em gate2_ghost.md par.4: fundo congelado e cego a
         remocao por constraint secundaria dependente do tempo).

G2b-SAUDE — o setor escalar sara na janela nao-fatorada?
    sigma/H e kN_min em k=1 E k=10, LEITURA DE TENDENCIA (a
    adiabaticidade chega a ~2.4 na janela — ponto congelado nao e
    juiz; regra herdada de evolucao_temporal_escalar.py). Referencias:
    os extremos da trajetoria (pre-rolagem ~ ramo finito com Lambda
    efetiva; pos-pouso ~ fundo estacionario modulado, da familia que o
    no-go ja cobriu).
      Se existir trecho da janela com espectro LIMPO (ambos os k):
         achado maior — o regime nao-fatorado e o unico lugar da F1
         onde o setor escalar sara; R2 ganha seu suporte interno.
      Se a janela for tao ou mais doente que os extremos: o no-go se
         ESTENDE ao regime nao-fatorado (2b, fronteira: UMA trajetoria,
         UMA celula — declarada) e R2 perde a ultima sonda interna a
         F1; o trilema empurra para fora da representacao.

G2b-BALANCO — o balanco quebra x EH se move?
    rI = |v'W_int v| / (|v'W_int v| + |v'W_EH v|) por modo (o
    diagnostico da C1: nos fundos estacionarios o taquiao de k=1 vive
    em rI ~ 0.5, cancelamento quase exato). p_phi != 0 muda o lado EH.
    Se rI se mover qualitativamente na janela, o mecanismo da doenca e
    deformavel pela dinamica — informacao de design mesmo se a saude
    nao mudar. (Diagnostico, nao criterio de passagem.)

MAIS: |<v,dchi>|^2 por modo — o G1-b revisitado no regime dinamico
(F' != 0 E chid != 0 acoplam delta-phi_- de verdade): a patologia
continua espectadora de delta-phi_-? E a identidade de Goldstone
(pi0/piL, com o termo -xid/xi do vetor T agora ativo).

VALIDACAO (pre-declarada; falha -> nao interpretar):
    V1: GR selfcheck da biblioteca.
    V2 (T1 estendido): fatias com taxas LIVRES reconstroem a matriz
        direta num ponto ROLANTE (chid,chidd,Hd,Hfd,xid != 0), com
        F global (Fb=1, Fp=0.1, Fpp=0.05) e betas constantes:
        max|dif| < 1e-8.
    V3: no ponto pre-rolagem (a=100, taxas pequenas), espectro com
        taxas vs taxas zeradas: mesmos numeros de pares e |Delta w2|
        relativo < 5% (checa a fiacao dos simbolos de taxa; se >5%,
        reportar como achado, nao abortar).

CAVEAT ESTRUTURAL (declarado): o QEP congela coeficientes em cada
ponto (d/dt C_sym desprezado; taxas entram nos COEFICIENTES, nao na
evolucao). Por isso: tendencia, nunca veredito pontual; k >> H e a
regiao mais confiavel; e a contagem so FALSIFICA (ver acima).

FUNDO: reintegrado inline (copia do integrador da Fase A, mesmos
parametros do caso alvo; ancora r(a=10)=0.332259 do controle ja
validada na Fase A; aqui conferimos r_fim=0.4979 e chi/v_fim=0.932
contra a saida da Fase A antes de usar).

Requer sympy, numpy, scipy. ~4-7 min (montagem 7x7 + 45 fatias com
taxas livres + integracao do fundo + ~18 pontos x 2 k de QEP).
Uso (raiz do repo, venv ativo):
    python auditoria/code/investigacao2_faseB_pert.py
Saida em auditoria/code/out/investigacao2_faseB_pert.txt
"""
import importlib.util
import os
import sys
import time

import numpy as np
import sympy as sp
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
IDX_F = [2, 3, 4, 5]
IDX_MULT = [0, 1]
IDX_DCHI = 6
TOL_SIG = 0.05
TOL_KN = 1e-9
BETAS = (b0, b1, b2, b3, b4)

say("=" * 72)
say("INVESTIGACAO 2 — FASE B: perturbacoes no fundo de rolagem")
say("=" * 72)

# ------------------------------------------------------------------
# V1 + montagem
# ------------------------------------------------------------------
if not d1.gr_selfcheck():
    say("[!] V1 (GR) falhou — abortando")
    sys.exit(1)

L2s, fields, vels = d1.build_L2()
K7, C7, W7 = quadratic_matrices(L2s, fields, vels)
if [str(f) for f in fields] != NOMES:
    raise RuntimeError("ordem de campos mudou")
say("[montagem] K,C,W 7x7 prontos")

# ------------------------------------------------------------------
# fatias com as TAXAS LIVRES
# ------------------------------------------------------------------
say("[fatias] {Fb,Fp,Fpp} x {b0..b4}, taxas livres (pode demorar) ...")
LIVRES = (a_s, b_s, xi_s, H_s, Hf_s, Hd_s, Hfd_s, xid_s,
          chid_s, chidd_s, Ub, Up, Upp, ksym, Mf2, Meff2)
FIXOS = {Mg2: 1, m2: 1, rho_s: 0}


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
# fundo: copia inline do integrador da Fase A (caso alvo g=2, m30)
# ------------------------------------------------------------------
say("[fundo] reintegrando a trajetoria alvo (g=2, m_chi^2=30, v*=1) ...")

MU = 1.0
MG2, MF2 = 1.0, MU
ME2 = MU / (1.0 + MU)
M2 = 1.0
B0V, B2V, B4V = 1.0, -0.4, 0.5
B10 = 1.0
RHO0 = 0.3

a_, b_, ch_ = sp.symbols('a b chi', positive=True)
pa_, pb_, pch_ = sp.symbols('p_a p_b p_chi', real=True)
Mg2s, Mf2s, Me2s, m2s = sp.symbols('Mg2 Mf2 Meff2 m2', positive=True)
b0s, b2s, b4s = sp.symbols('beta_0 beta_2 beta_4', real=True)
Hs, Hfs, chds = sp.symbols('H H_f chidot', real=True)
b10s, vsts = sp.symbols('b1_0 v_star', positive=True)
b1_conc = b10s * (1 + ch_**2 / vsts**2)
rr_ = b_ / a_
Vgc_s = b0s + 3 * rr_ * b1_conc + 3 * rr_**2 * b2s
Vfc_s = b1_conc + 3 * rr_ * b2s + rr_**3 * b4s
Hg_s = (-pa_**2 / (12 * Mg2s * a_) + pch_**2 / (2 * a_**3)
        + m2s * Me2s * a_**3 * Vgc_s)
Hf_s2 = -pb_**2 / (12 * Mf2s * b_) + m2s * Me2s * a_**3 * Vfc_s
CANON = [(a_, pa_), (b_, pb_), (ch_, pch_)]
Om_sym = sp.expand(sum(sp.diff(Hg_s, q) * sp.diff(Hf_s2, p)
                       - sp.diff(Hg_s, p) * sp.diff(Hf_s2, q)
                       for q, p in CANON))
Om_v = sp.expand(Om_sym.subs({pa_: -6 * Mg2s * a_**2 * Hs,
                              pb_: -6 * Mf2s * b_**2 * Hfs,
                              pch_: a_**3 * chds}))
Om_fn = sp.lambdify((a_, b_, ch_, chds, Hs, Hfs,
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
        if i % max(1, n // 6000) == 0:
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
    # taxas por diferenca central sobre o registro
    dNr = np.gradient(rec['N'])
    rec['Hd'] = rec['H'] * np.gradient(rec['H']) / dNr
    rec['Hfd'] = rec['H'] * np.gradient(rec['Hfv']) / dNr
    rec['xid'] = rec['H'] * np.gradient(rec['xi']) / dNr
    return rec


BG = integra_alvo()
say(f"[fundo] ok — r_fim={BG['r'][-1]:.4f} (Fase A: 0.4979), "
    f"chi/v_fim={BG['ch'][-1]/BG['v']:.3f} (Fase A: 0.932)")
ok_fundo = (abs(BG['r'][-1] - 0.4979) < 0.005
            and abs(BG['ch'][-1] / BG['v'] - 0.932) < 0.005)
say(f"  [{'FUNDO CONFERE' if ok_fundo else 'FUNDO DIVERGE — nao interpretar'}]")


# ------------------------------------------------------------------
# avaliacao de um ponto da trajetoria
# ------------------------------------------------------------------
def args_do_ponto(i, kv, taxas=True):
    """LIVRES = (a,b,xi,H,Hf,Hd,Hfd,xid,chid,chidd,Ub,Up,Upp,k,Mf2,Meff2)
    com a RESCALADA para 1 (k comovel na convencao da D1)."""
    ch = BG['ch'][i]
    mu2, lam, U0 = BG['mu2'], BG['lam'], BG['U0']
    Ubv = U_pot(ch, mu2, lam, U0) + RHO0 / BG['a'][i]**3
    fac = 1.0 if taxas else 0.0
    return (1.0, BG['r'][i], BG['xi'][i], BG['H'][i], BG['Hfv'][i],
            fac * BG['Hd'][i], fac * BG['Hfd'][i], fac * BG['xid'][i],
            fac * BG['chd'][i], fac * BG['chidd'][i],
            Ubv, dU_pot(ch, mu2, lam), -mu2 + 3 * lam * ch * ch,
            kv, MF2, ME2)


def matrizes_do_ponto(i, kv, taxas=True):
    ch = BG['ch'][i]
    vst = BG['vst']
    args = args_do_ponto(i, kv, taxas)
    bvals = (B0V, beta1(ch, vst), B2V, 0.0, B4V)
    bp = (0.0, dbeta1(ch, vst), 0.0, 0.0, 0.0)
    bpp = (0.0, 2.0 * B10 / vst**2, 0.0, 0.0, 0.0)
    Kn = monta(FK, args, bvals, bp, bpp)
    Cn = monta(FC, args, bvals, bp, bpp)
    Wn = monta(FW, args, bvals, bp, bpp)
    Wb = np.array(FW['base'](*args), float)
    return Kn, Cn, Wn, Wn - Wb, Wb


def classifica(w2, kN, H_val):
    om = np.sqrt(complex(w2))
    taxa = abs(om.imag) / H_val
    if taxa > TOL_SIG:
        return 'TAQUIAO', taxa
    if kN < -TOL_KN:
        return 'FANTASMA', taxa
    return 'limpo', taxa


def orbita_M4(bb, xi, Hf, kv, xid):
    return np.array([
        [-xid / xi,     -1.0, 0.0,      0.0],
        [xi * Hf,        0.0, 0.0,      0.0],
        [xi / bb,        0.0, 0.0,      bb / (xi * kv)],
        [0.0,            0.0, 1.0 / kv, 0.0]], dtype=float)


# ------------------------------------------------------------------
# V2 — T1 estendido: fatias reconstroem a direta num ponto ROLANTE
# ------------------------------------------------------------------
say("")
say("V2 — T1 estendido (ponto rolante, F global, betas constantes)")
i_test = int(np.argmin(np.abs(BG['a'] - 1500.0)))
argsT = args_do_ponto(i_test, 1.0, taxas=True)
bconst = (B0V, 1.7, B2V, 0.0, B4V)
K_rec = monta(FK, argsT, bconst,
              tuple(0.1 * x for x in bconst), tuple(0.05 * x for x in bconst))
subsT = dict(FIXOS)
subsT.update({s: v for s, v in zip(LIVRES, argsT)})
subsT.update({Fb: 1.0, Fp: 0.1, Fpp: 0.05,
              b0: bconst[0], b1: bconst[1], b2: bconst[2],
              b3: 0.0, b4: bconst[4]})
K_dir = np.array(sp.Matrix(K7).subs(subsT).evalf(), float)
difT = np.max(np.abs(K_rec - K_dir))
ok_v2 = difT < 1e-8
say(f"    max|K_fatias - K_direta| = {difT:.2e}  "
    f"[{'PASSA' if ok_v2 else 'FALHA'}]")
if not ok_v2:
    say("    !! abortando — fatias nao reconstroem com taxas livres")
    sys.exit(1)

# ------------------------------------------------------------------
# V3 — taxas vs congelado no ponto pre-rolagem
# ------------------------------------------------------------------
say("")
say("V3 — a=100 (pre-rolagem): espectro taxas-ligadas vs congelado")
i100 = int(np.argmin(np.abs(BG['a'] - 100.0)))
ok_v3 = True
for kv in (1.0, 10.0):
    esp = {}
    for lbl, tx in (('taxas', True), ('congelado', False)):
        Kn, Cn, Wn, _, _ = matrizes_do_ponto(i100, kv, taxas=tx)
        pares = d1.agrupa_pares(d1.qep_modes(Kn, Cn, Wn))
        esp[lbl] = sorted([mm['omega2'].real for mm in pares])
    n1, n2 = len(esp['taxas']), len(esp['congelado'])
    say(f"    k={kv:g}: pares {n1} vs {n2}; w2 "
        + " | ".join(f"{x:+.3e}/{y:+.3e}" for x, y in
                     zip(esp['taxas'], esp['congelado'])))
    if n1 != n2:
        ok_v3 = False
    else:
        for x, y in zip(esp['taxas'], esp['congelado']):
            den = max(abs(x), abs(y), 1e-12)
            if abs(x - y) / den > 0.05:
                ok_v3 = False
say(f"  [V3 {'PASSA' if ok_v3 else 'DIVERGE >5% — reportado como achado, '
    'nao abortivo (taxas ja importam no pre-rolagem)'}]")

# ------------------------------------------------------------------
# varredura ao longo da trajetoria
# ------------------------------------------------------------------
say("")
say("=" * 72)
say("VARREDURA — QEP ao longo da trajetoria (leitura de tendencia)")
say("=" * 72)
say("  janela-alvo da Fase A: a ~ [760, 2050]; extremos como referencia")

AS = [100, 300, 500, 700, 800, 900, 1000, 1200, 1500, 1800, 2050,
      2500, 3466, 6787, 13291, 26025, 50962, 99000]
KG = [1.0, 10.0]

registros = []
for a_al in AS:
    i = int(np.argmin(np.abs(BG['a'] - a_al)))
    a_i = BG['a'][i]
    H_i = BG['H'][i]
    r_i = BG['r'][i]
    xi_i = BG['xi'][i]
    ch_i = BG['ch'][i]
    desl_i = BG['desl'][i]
    adiab = (abs(BG['chidd'][i] / (3 * H_i * BG['chd'][i]))
             if abs(BG['chd'][i]) > 1e-12 else 0.0)
    say("")
    say(f"  a={a_i:9.1f}  r={r_i:.4f} xi={xi_i:.4f} chi/v={ch_i/BG['v']:.3f} "
        f"desl={desl_i:+.2e} |Hd/H^2|={abs(BG['Hd'][i])/H_i**2:.3f} "
        f"adiab={adiab:.2f}")
    for kv in KG:
        Kn, Cn, Wn, Wint, Wbase = matrizes_do_ponto(i, kv)
        pares = d1.agrupa_pares(d1.qep_modes(Kn, Cn, Wn))
        pares.sort(key=lambda mm: abs(mm['omega2']))
        npar = len(pares)
        M4 = orbita_M4(r_i, xi_i, BG['Hfv'][i], kv, BG['xid'][i])
        col_norms = np.linalg.norm(M4, axis=0)
        linha = []
        sig_max, kN_min = 0.0, np.inf
        for mm in pares:
            v = mm['v']
            w2 = mm['omega2']
            kN = mm['knorm']
            cls, taxa = classifica(w2, kN, H_i)
            sig_max = max(sig_max, taxa)
            kN_min = min(kN_min, kN)
            p_chi = float(abs(v[IDX_DCHI])**2)
            v_f = np.array([v[j] for j in IDX_F])
            try:
                c = np.linalg.solve(M4, v_f)
                chat = np.abs(c * col_norms)**2
                tot = chat.sum() if chat.sum() > 0 else 1.0
                pi0 = (chat[0] + chat[1]) / tot
                piL = (chat[2] + chat[3]) / tot
            except np.linalg.LinAlgError:
                pi0 = piL = float('nan')
            wI = float(np.real(np.conjugate(v) @ Wint @ v))
            wB = float(np.real(np.conjugate(v) @ Wbase @ v))
            den = abs(wI) + abs(wB)
            rI = abs(wI) / den if den > 0 else float('nan')
            linha.append(f"      w2={w2.real:+.3e}"
                         f"{'' if abs(w2.imag) < 1e-6*max(1.0, abs(w2.real)) else f' {w2.imag:+.2e}i'}"
                         f" kN={kN:+.2e} [{cls:8s}] dchi={p_chi:.3f} "
                         f"pi0={pi0:.2f} piL={piL:.2f} rI={rI:.2f}")
        say(f"    k={kv:g}: {npar} par(es)"
            + ("  <<< CONTAGEM != 3" if npar != 3 else ""))
        for ln in linha:
            say(ln)
        registros.append(dict(a=a_i, k=kv, npar=npar, sig=sig_max,
                              kNmin=kN_min, desl=desl_i))

# ------------------------------------------------------------------
# sintese de tendencia + veredito
# ------------------------------------------------------------------
say("")
say("=" * 72)
say("SINTESE DE TENDENCIA")
say("=" * 72)
say(f"    {'a':>9} {'desl':>10} " +
    " ".join(f"{'n(k='+str(int(kv))+')':>7} {'sig/H':>7} {'kN_min':>9}"
             for kv in KG))
for a_al in AS:
    regs = [rg for rg in registros if abs(rg['a'] - a_al) < 0.5 * a_al]
    regs_a = {rg['k']: rg for rg in regs
              if abs(rg['a'] - min(regs, key=lambda x: abs(x['a']-a_al))['a']) < 1e-9}
    if len(regs_a) < 2:
        continue
    r1, r10 = regs_a[1.0], regs_a[10.0]
    say(f"    {r1['a']:9.1f} {r1['desl']:+10.2e} "
        f"{r1['npar']:7d} {r1['sig']:7.2f} {r1['kNmin']:+9.1e} "
        f"{r10['npar']:7d} {r10['sig']:7.2f} {r10['kNmin']:+9.1e}")

say("")
say("VEREDITO FASE B (criterios pre-declarados)")
say("-" * 72)
JAN = (760.0, 2050.0)
in_jan = [rg for rg in registros if JAN[0] <= rg['a'] <= JAN[1]]
fora = [rg for rg in registros if rg['a'] < 200 or rg['a'] > 20000]

bd4 = {}
for rg in registros:
    if rg['npar'] >= 4:
        bd4.setdefault(rg['a'], set()).add(rg['k'])
bd_conf = [aa for aa, ks in bd4.items() if len(ks) >= 2]
if bd_conf:
    say(f"  G2b-CONTAGEM: >=4 pares em AMBOS os k em a={bd_conf} —")
    say("      CANDIDATO A BD CONFIRMADO NA ROTA NUMERICA: o Gate 2")
    say("      Parte B FALHA no regime nao-fatorado (conclusivo pela")
    say("      assimetria declarada). Investigar composicao do 4o modo.")
elif bd4:
    say(f"  G2b-CONTAGEM: >=4 pares em um unico k em a={sorted(bd4)} —")
    say("      SUSPEITO (nao conclusivo); demais pontos com 3.")
else:
    say("  G2b-CONTAGEM: 3 pares em todos os pontos/k — COMPATIVEL com")
    say("      remocao do BD; NAO certifica (cegueira declarada do QEP")
    say("      congelado a constraints dependentes do tempo).")

sig_jan = max((rg['sig'] for rg in in_jan), default=float('nan'))
sig_fora = max((rg['sig'] for rg in fora), default=float('nan'))
kN_jan = min((rg['kNmin'] for rg in in_jan), default=float('nan'))
limpo_jan = [rg['a'] for rg in in_jan
             if rg['sig'] <= TOL_SIG and rg['kNmin'] >= -TOL_KN]
say(f"  G2b-SAUDE: janela max sig/H = {sig_jan:.2f}, kN_min = {kN_jan:+.1e};")
say(f"      extremos max sig/H = {sig_fora:.2f}")
if limpo_jan:
    say(f"      PONTOS LIMPOS NA JANELA: a={sorted(set(limpo_jan))} —")
    say("      trecho saudavel no regime nao-fatorado: achado maior; exige")
    say("      confirmacao (mais k, mais trajetorias) antes de qualquer")
    say("      enquadramento. R2 ganha sua sonda interna.")
else:
    say("      nenhum ponto limpo na janela (nos k testados): o no-go se")
    say("      ESTENDE ao regime nao-fatorado NESTA trajetoria/celula")
    say("      (fronteira declarada: uma trajetoria, uma celula, k=1 e 10,")
    say("      leitura congelada ponto a ponto). R2 perde a ultima sonda")
    say("      interna a F1 — o trilema empurra para fora da representacao.")
say("  G2b-BALANCO: ver colunas rI acima (diagnostico — comparar com o")
say("      rI~0.5 do cancelamento estacionario da C1).")

os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
with open(os.path.join(HERE, "out", "investigacao2_faseB_pert.txt"),
          "w", encoding="utf-8") as fh:
    fh.write("\n".join(OUT))
say("")
say("concluido. saida em auditoria/code/out/investigacao2_faseB_pert.txt")
