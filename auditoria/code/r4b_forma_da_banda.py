# -*- coding: utf-8 -*-
"""
r4b_forma_da_banda.py — R-4b (bloco 2 do R-4): a FORMA da banda de
amplificacao e o lnA de PASSAGEM por modo.

CONTEXTO (docs/resultado_r4a_mapa.md). O R-4a estabeleceu: a classe
beta-constante INTEIRA (beta1=1..4.47) tem amplificacao transiente de
banda no setor escalar tardio — modos com k_phys/H ~ 0.5-30 crescem a
~1-2/H (GR-limpa: R4a-NULL passou com o cruzamento dentro da janela),
cada modo por tempo finito ao redor do proprio cruzamento
(R4a-EXT: tardia2 dilui nos dois fundos). A viabilidade vira uma
questao observacional: o dano e^lnA por modo. Este script mede:

  (1) A FORMA da banda: taxa metrica em JANELAS DE k_phys/H (nao de
      a) — kh de 40 a 0.1 em 12 faixas — nos fundos estaticos
      beta1=1 e beta1=4.47. Em fundo estatico (de Sitter; dust ~1e-5
      do potencial em a>=100) a dinamica depende de kh, entao a forma
      e a mesma para qualquer k (auto-similaridade; VERIFICADA no
      braco R4b-AUTOSIM: mesmo fundo, k triplicado, mesma passagem).
      Separacao por componente: par Psi_f (ICs 0,3) vs par E_f
      (ICs 1,4) por faixa — a estrutura vista no R-4a (E_f cresce em
      kh alto; Psi_f perto do cruzamento).
  (2) O lnA DE PASSAGEM por modo: Delta ln|y_met| entre kh=20 e
      kh=0.2 (janela "passagem"; comeca em kh=20 para EXCLUIR a
      componente E_f de entrada em kh>~24 e a dependencia de IC — e
      uma medida por modo, nao por historia completa). Por IC metrica;
      reporta-se o maximo.
  (3) A MODULACAO POR EPOCA no fundo POUSADO: grade de 8 k escolhidos
      para cruzar (kh=1) em a_cross = {500, 1000, 1600, 2500, 4000,
      8000, 15000, 30000} — da pre-rolagem ao pos-pouso profundo.
      lnA_passagem(a_cross): a rolagem/pouso amplificam a banda?
      (O burst de pouso do R-3/R-3b sugere que sim, ~ +1H extra na
      janela do anel.)
  (4) R4b-NULL: GR + Lambda + chi espectador com a MESMA passagem
      completa (kh 40 -> 0.1): lnA_passagem <= +0.5 esperado
      (dilucao); FALHA -> nao interpretar (artefato de passagem).

DESENHO: maquinaria R-3/R-4a verbatim (reducao dependente do tempo,
RK4, normas); grade a=[100,80000] (estaticos/GR; kh inicial = 45
exato) e a=[20,80000] nos bracos do pousado (para os cruzamentos
cedo terem kh=20 dentro do range), npts=24000; janelas construidas em
a a partir das bordas de kh POR RODADA (kh(a) = k_c/(a H(a)),
monotono; janelas incompletas no range sao puladas e reportadas).
lnA em base comovel — caveat de base herdado (comparacoes RELATIVAS
entre bracos/faixas sao o que vale).

CRITERIOS PRE-DECLARADOS:
  R4b-NULL: GR, passagem completa: lnA_passagem <= +0.5 (esperado
      negativo). FALHA -> NAO INTERPRETAR o resto.
  R4b-AUTOSIM: |lnA_passagem(beta1=1, k) - lnA_passagem(beta1=1, 3k)|
      < 0.5 -> auto-similaridade confirmada (uma medida por fundo
      estatico basta). FALHA -> reportar e tratar lnA como
      k-dependente (mapa maior no proximo bloco).
  R4b-FORMA/LNA: mensuracao (sem veredito duro): tabelas de taxa(kh)
      por componente e lnA_passagem por fundo/epoca — os insumos do
      bloco observacional (dicionario de epocas = decisao do autor,
      fora deste script).
  Ancoras/negK: 5000, 15000, 40000, 70000 em todos os bracos (trilha
      estrutural continua).

HARDCODES/REFERENCIAS: nenhum novo — reproducoes internas: o braco
estatico 4.47 repete o EXT do R-4a (mesma fisica, janelas novas); o
pousado a_cross~11000 corresponde ao k_c=12500 ja medido (+0.98 na
janela em a).

Requer sympy, numpy, scipy. ~10-16 min (12 rodadas de 24000 pts).
Uso (raiz do repo, venv ativo):
    python auditoria/code/r4b_forma_da_banda.py
Saida em auditoria/code/out/r4b_forma_da_banda.txt
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
DYN = [3, 5, 6]
IDX_MET_IC = [0, 1, 3, 4]
A_MIN, A_MAX = 100.0, 80000.0
NPTS = 24000
ANCS = [5000.0, 15000.0, 40000.0, 70000.0]

KH_EDGES = [40.0, 20.0, 10.0, 6.0, 4.0, 2.5, 1.6, 1.0,
            0.7, 0.45, 0.3, 0.2, 0.1]
KH_PASS = (20.0, 0.2)
A_CROSS = [500.0, 1000.0, 1600.0, 2500.0, 4000.0, 8000.0,
           15000.0, 30000.0]
LAM_GR = 3.9

MU = 1.0
MG2, MF2 = 1.0, MU
ME2 = MU / (1.0 + MU)
M2 = 1.0
B0V, B2V, B4V = 1.0, -0.4, 0.5
B10 = 1.0
RHO0 = 0.3
VST = 1.0

say("=" * 72)
say("R-4b — A FORMA DA BANDA E O lnA DE PASSAGEM POR MODO")
say("=" * 72)

# ------------------------------------------------------------------
# V1 + montagem + fatias (verbatim)
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
# fundos (verbatim R-4a)
# ------------------------------------------------------------------
def fundo_bconst(a, B1V):
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


def Hf2_of(r, ch, vst):
    b1v = beta1(ch, vst)
    Vf = b1v + 3 * r * B2V + r**3 * B4V
    return M2 * ME2 * Vf / (3 * MF2 * r**3)


def H2_of(r, ch, chd, a, vst, mu2, lam, U0):
    b1v = beta1(ch, vst)
    Vg = B0V + 3 * r * b1v + 3 * r * r * B2V
    return (0.5 * chd * chd + U_pot(ch, mu2, lam, U0) + RHO0 / a**3
            + M2 * ME2 * Vg) / (3 * MG2)


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


def builder_rolagem(ctx, a_min=A_MIN):
    def build(kc, npts):
        Ns = np.linspace(np.log(a_min), np.log(A_MAX), npts)
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
            Ms['K'][p] = monta(FK, args, bvals, (0,) * 5, (0,) * 5)
            Ms['C'][p] = monta(FC, args, bvals, (0,) * 5, (0,) * 5)
            Ms['W'][p] = monta(FW, args, bvals, (0,) * 5, (0,) * 5)
        return Ns, Hs_arr, Ms
    return build


# ------------------------------------------------------------------
# reducao + evolucao (verbatim, com dln por janela devolvido)
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


def evolui(Kr, Cr, Wr, Krd, Crd, Ns, Hs_arr, janelas, met_idx=(0, 1)):
    """devolve taxas (total e met) E dln_met por janela, por IC."""
    npts = len(Ns)
    nd = Kr.shape[1]
    aas = np.exp(Ns)
    Hmid = {}
    for nome, lo, hi in janelas:
        pm = int(np.argmin(np.abs(aas - np.sqrt(lo * hi))))
        Hmid[nome] = Hs_arr[pm]
    taxas_f, taxas_m, dlns_m = [], [], []
    for ic in range(2 * nd):
        q = np.zeros(nd)
        qd = np.zeros(nd)
        if ic < nd:
            q[ic] = 1.0
        else:
            qd[ic - nd] = 1.0
        tcum = 0.0
        reg = {nome: [None] * 6 for nome, _, _ in janelas}
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
            for nome, lo, hi in janelas:
                r = reg[nome]
                if r[0] is None and aa >= lo:
                    r[0], r[1], r[4] = ln_f, tcum, ln_m
                if r[2] is None and aa >= hi:
                    r[2], r[3], r[5] = ln_f, tcum, ln_m
        tx_f, tx_m, dl_m = {}, {}, {}
        for nome, lo, hi in janelas:
            r = reg[nome]
            if r[0] is not None and r[2] is not None and r[3] > r[1]:
                tx_f[nome] = (r[2] - r[0]) / (r[3] - r[1]) / Hmid[nome]
                tx_m[nome] = (r[5] - r[4]) / (r[3] - r[1]) / Hmid[nome]
                dl_m[nome] = r[5] - r[4]
            else:
                tx_f[nome] = float('nan')
                tx_m[nome] = float('nan')
                dl_m[nome] = float('nan')
        taxas_f.append(tx_f)
        taxas_m.append(tx_m)
        dlns_m.append(dl_m)
    return taxas_f, taxas_m, dlns_m


def janelas_kh(kc, Ns, Hs_arr):
    """janelas em a a partir das bordas de kh; so as completas."""
    aas = np.exp(Ns)
    khs = kc / (aas * Hs_arr)
    a_of_kh = {}
    for kh in set(KH_EDGES) | set(KH_PASS):
        if khs[0] <= kh or khs[-1] >= kh:
            a_of_kh[kh] = None
        else:
            idx = int(np.argmax(khs <= kh))
            a_of_kh[kh] = float(aas[idx])
    jans = []
    puladas = []
    for j in range(len(KH_EDGES) - 1):
        hi_kh, lo_kh = KH_EDGES[j], KH_EDGES[j + 1]
        a_in, a_out = a_of_kh[hi_kh], a_of_kh[lo_kh]
        nome = f"kh{hi_kh:g}-{lo_kh:g}"
        if a_in is None or a_out is None:
            puladas.append(nome)
            continue
        jans.append((nome, a_in, a_out))
    a_p_in, a_p_out = a_of_kh[KH_PASS[0]], a_of_kh[KH_PASS[1]]
    tem_pass = a_p_in is not None and a_p_out is not None
    if tem_pass:
        jans.append(("passagem", a_p_in, a_p_out))
    return jans, puladas, tem_pass


def roda(rotulo, build, kc, met_idx=(0, 1), mult=None, dyn=None):
    say("")
    say(f"--- {rotulo}: k_c={kc:g} ---")
    mult = MULT if mult is None else mult
    dyn = DYN if dyn is None else dyn
    Ns, Hs_arr, Ms = build(kc, NPTS)
    jans, puladas, tem_pass = janelas_kh(kc, Ns, Hs_arr)
    if puladas:
        say(f"    janelas fora do range (puladas): {', '.join(puladas)}")
    Kr, Cr, Wr, Krd, Crd, Ns_t, Hs_t = reduz_trilha(Ms, Ns, Hs_arr,
                                                    mult, dyn)
    a_max_val = float(np.exp(Ns_t[-1]))
    if a_max_val < 0.99 * A_MAX:
        say(f"    [reducao] TRUNCADA em a={a_max_val:.0f}")
    aas_t = np.exp(Ns_t)
    if len(dyn) == 3:
        for a_anc in ANCS:
            if a_anc > a_max_val:
                continue
            p_anc = int(np.argmin(np.abs(aas_t - a_anc)))
            eigK = np.linalg.eigvalsh(0.5 * (Kr[p_anc] + Kr[p_anc].T))
            negK = int(np.sum(eigK < -1e-12))
            if negK != 1:
                say(f"    ancora a={a_anc:6.0f}: negK={negK}  <<< != 1")
    tf, tm, dl = evolui(Kr, Cr, Wr, Krd, Crd, Ns_t, Hs_t, jans,
                        met_idx=met_idx)
    nics = len(tf)
    idx_met = IDX_MET_IC if nics == 6 else list(range(nics))
    say(f"    {'janela':<12} {'a_in':>7} {'a_out':>7} "
        f"{'metMAX':>7} {'Psi(0,3)':>9} {'Ef(1,4)':>9}")
    for nome, lo, hi in jans:
        if nome == "passagem":
            continue
        vs = [tm[i][nome] for i in idx_met if np.isfinite(tm[i][nome])]
        vmax = max(vs) if vs else float('nan')
        if nics == 6:
            vpsi = max(x for x in (tm[0][nome], tm[3][nome])
                       if np.isfinite(x)) if np.isfinite(tm[0][nome]) \
                else float('nan')
            vef = max(x for x in (tm[1][nome], tm[4][nome])
                      if np.isfinite(x)) if np.isfinite(tm[1][nome]) \
                else float('nan')
        else:
            vpsi = vef = float('nan')
        say(f"    {nome:<12} {lo:7.0f} {hi:7.0f} {vmax:+7.2f} "
            f"{vpsi:+9.2f} {vef:+9.2f}")
    lnA_pass = float('nan')
    if tem_pass:
        dls = [dl[i]['passagem'] for i in idx_met
               if np.isfinite(dl[i]['passagem'])]
        lnA_pass = max(dls) if dls else float('nan')
        say(f"    lnA_passagem (kh 20 -> 0.2, max ICs metricas) = "
            f"{lnA_pass:+.2f}")
    else:
        say("    passagem incompleta no range — lnA_passagem indisponivel")
    return dict(tm=tm, dl=dl, lnA=lnA_pass, jans=jans)


# ------------------------------------------------------------------
# GR (null de passagem)
# ------------------------------------------------------------------
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


def build_gr(kc, npts):
    Ns = np.linspace(np.log(A_MIN), np.log(A_MAX), npts)
    Hs_arr = np.zeros(npts)
    Ms = {x: np.zeros((npts, 3, 3)) for x in 'KCW'}
    for p, N in enumerate(Ns):
        a = np.exp(N)
        rho_d = RHO0 / a**3
        H = np.sqrt((LAM_GR + rho_d) / 3.0)
        Hs_arr[p] = H
        args = (a, H, -0.5 * rho_d, 0.0, 0.0,
                LAM_GR + rho_d, 0.0, 0.3, kc)
        Ms['K'][p] = np.array(KgF(*args), float)
        Ms['C'][p] = np.array(CgF(*args), float)
        Ms['W'][p] = np.array(WgF(*args), float)
    return Ns, Hs_arr, Ms


# ------------------------------------------------------------------
# rodadas
# ------------------------------------------------------------------
say("")
say("=" * 72)
say("RODADAS")
say("=" * 72)

# kh inicial = 45 EXATO (H medido em a=A_MIN) — garante a janela
# kh40-20 e a passagem completas em todos os bracos estaticos/GR
H_GR0 = np.sqrt((LAM_GR + RHO0 / A_MIN**3) / 3.0)
RG = roda("GR-NULL (passagem completa)", build_gr, 45.0 * H_GR0 * A_MIN,
          met_idx=None, mult=[0, 1], dyn=[2])
ok_null = (not np.isfinite(RG['lnA'])) or RG['lnA'] <= 0.5
say(f"  [R4b-NULL {'PASSA' if ok_null else 'FALHA — NAO INTERPRETAR'}] "
    f"(lnA_passagem GR = {RG['lnA']:+.2f}; criterio <= +0.5)")

fb1 = fundo_bconst(A_MIN, 1.0)
fb4 = fundo_bconst(A_MIN, 4.47)
K1 = 45.0 * fb1['H'] * A_MIN
K4 = 45.0 * fb4['H'] * A_MIN
R1 = roda("estatico beta1=1", builder_bconst(1.0), K1)
R1b = roda("estatico beta1=1, k x3 (AUTOSIM)", builder_bconst(1.0),
           3.0 * K1)
R4 = roda("estatico beta1=4.47", builder_bconst(4.47), K4)

d_auto = abs(R1['lnA'] - R1b['lnA'])
ok_auto = np.isfinite(d_auto) and d_auto < 0.5
say("")
say(f"  [R4b-AUTOSIM {'PASSA' if ok_auto else 'FALHA'}] "
    f"|lnA(k) - lnA(3k)| = {d_auto:.2f} (criterio < 0.5)")

say("")
say("[fundo POUSADO] reintegrando a trajetoria original ...")
BG_ORG = integra_alvo()
ok_org = (abs(BG_ORG['r'][-1] - 0.4979) < 0.005
          and abs(BG_ORG['ch'][-1] / BG_ORG['v'] - 0.932) < 0.005)
say(f"    r_fim={BG_ORG['r'][-1]:.4f}, "
    f"chi/v_fim={BG_ORG['ch'][-1]/BG_ORG['v']:.3f}  "
    f"[{'CONFERE' if ok_org else 'DIVERGE'}]")
CTX = make_ctx(BG_ORG, "ORG")

# pousado: grade comeca em a=20 (pre-rolagem profunda) para que ate os
# bracos de cruzamento cedo (a_cross=500) tenham kh=20 dentro do range
# e a passagem completa seja mensuravel
RP = {}
for a_c in A_CROSS:
    N_c = np.log(a_c)
    H_c = float(CTX['spl']['H'](N_c))
    kc = a_c * H_c
    RP[a_c] = roda(f"pousado, cruzamento em a={a_c:g}",
                   builder_rolagem(CTX, a_min=20.0), kc)

# ------------------------------------------------------------------
# sintese
# ------------------------------------------------------------------
say("")
say("=" * 72)
say("SINTESE R-4b")
say("=" * 72)
say(f"  R4b-NULL: {'PASSA' if ok_null else 'FALHA'}   "
    f"R4b-AUTOSIM: {'PASSA' if ok_auto else 'FALHA'}")
say("")
say("  lnA_passagem (kh 20 -> 0.2), fundos estaticos:")
say(f"    beta1=1:    {R1['lnA']:+.2f}   (k x3: {R1b['lnA']:+.2f})")
say(f"    beta1=4.47: {R4['lnA']:+.2f}")
say("")
say("  lnA_passagem no POUSADO por epoca de cruzamento:")
say(f"    {'a_cross':>8} {'lnA_pass':>9}")
for a_c in A_CROSS:
    say(f"    {a_c:8.0f} {RP[a_c]['lnA']:+9.2f}")
say("")
say("  FORMA (comparar tabelas de taxa(kh) acima: beta1=1 vs 4.47 vs")
say("  pousado — universalidade e modulacao por epoca; leitura no doc).")
say("")
say("  Proximo (bloco observacional, com o autor): dicionario de epocas")
say("  do modelo-brinquedo -> historia cosmica real, e o confronto")
say("  e^lnA vs vinculos (Comelli/Konnig/Akrami). Este script entrega")
say("  os insumos: forma da banda + lnA por modo/epoca.")

os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
with open(os.path.join(HERE, "out", "r4b_forma_da_banda.txt"),
          "w", encoding="utf-8") as fh:
    fh.write("\n".join(OUT))
say("")
say("concluido. saida em auditoria/code/out/r4b_forma_da_banda.txt")
