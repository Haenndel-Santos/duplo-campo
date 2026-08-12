# -*- coding: utf-8 -*-
"""
r7c_banda_pousado_2dof.py — R-7c: REEXECUCAO DA CASCATA (3/4). A
banda no fundo DINAMICO/POUSADO (modulacao beta1(phi-)) no sistema
2-DOF corrigido.

CONTEXTO: erratum_02; maquinaria validada no R-7a; banda estatica ja
MORTA no R-7b (lnA -8.4 vs +4 antigo). Falta a epoca dinamica: o
R-4b/R-4c antigo mediu lnA_passagem no pousado por epoca de
cruzamento (a_cross 500..30000) e obteve -0.2..+4.8 no sistema
espurio; a reauditoria externa corrigida obteve -12.3..-14.3 (ICs
metricas fisicas). Este script refaz no nosso pipeline.

FUNDO (R-4b verbatim): rolagem/pouso com beta1(phi-) = B10(1 +
phi-^2/v*^2), g_end=2.0, mchi2=30.0, v*=1.0; reintegrado e conferido
contra as ancoras (r_fim ~ 0.4979; phi-/v ~ 0.932). Modulacao entra
pelas fatias Fp/Fpp com bp = beta1'(phi-), bpp = beta1'' (constante —
modulacao quadratica => F''' = 0 e o canal-S e EXATO tambem aqui;
verificado no R-7a que C7 nao contem Upp).

REDUCAO: E1+E2 corrigidas (R-7a/R-7b), equilibracao D, canal-S como
producao; V-XREP (G3) contra canal-G na trilha DINAMICA — primeira
validacao de representacao dupla fora do fundo estatico. NOTA: no
fundo rolante E_f e dchi NAO desacoplam (F' != 0 acopla) — a fisica
de mistura e real e fica.

MEDIDAS (pre-declaradas), por a_cross em {500,1000,1600,2500,4000,
8000,15000,30000}, kc = a_cross*H(a_cross) (cruzamento kh=1),
trilha a=[20,80000], NPTS=14000 (comparavel a externa; halving do
integrador ja certificado no R-7a via Richardson):
  - mapa cinetico: nenhum autovalor de K2 negativo na trilha
    interpretada (20 <= a <= 8e4);
  - lnA_PASSAGEM (kh 20 -> 0.2) da componente Etil (envelope), por
    IC; se kh_final > 0.2 a passagem e PARCIAL (reportada com
    bandeira, como no antigo para a_cross=30000);
  - Delta ln|Phi_g| na passagem (blocos corrigidos);
  - tabela comparativa: antigo (3-DOF) vs externa (2-DOF) vs este.

CRITERIOS (pre-declarados):
  G1 (canal-S) < 1e-10; G3 (V-XREP interior) < 1e-3 na trilha
      dinamica (mais frouxo que o estatico: o fundo vem de splines de
      uma integracao, nao de formula fechada; reportar valor).
  todos lnA_pass < 0  -> POUSADO-BANDA-MORTA: o R-4 dinamico inteiro
      (amplificacao por epoca, "supressao-materia" do R-4c) era
      artefato; R-4 COMPLETO substituido.
  algum lnA_pass >= +3.5 -> BANDA-VIVA dinamica (investigar).
  intermediario -> quantificar.

Requer sympy, numpy, scipy. ~10-18 min (8 trilhas de 14000).
Uso (raiz do repo, venv ativo):
    python auditoria/code/r7c_banda_pousado_2dof.py
Saida em auditoria/code/out/r7c_banda_pousado_2dof.txt
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
                           quadratic_matrices, dt_background)

T0 = time.time()
OUT = []


def say(*a):
    line = " ".join(str(x) for x in a)
    print(f"[{time.time()-T0:7.1f}s] {line}")
    OUT.append(line)


NOMES = ['Phi_g', 'B_g', 'Phi_f', 'Psi_f', 'B_f', 'E_f', 'dchi']
MULT = [0, 1, 2, 4]
DYN = [3, 5, 6]
A_MINP, A_MAX = 20.0, 80000.0
NPTS = 14000
G1_TOL = 1e-10
G3_TOL = 1e-3
KH_PASS = (20.0, 0.2)
A_CROSS = [500.0, 1000.0, 1600.0, 2500.0, 4000.0, 8000.0,
           15000.0, 30000.0]
REF_ANTIGO = {500: -0.21, 1000: 3.26, 1600: 1.57, 2500: 3.17,
              4000: 4.80, 8000: 4.03, 15000: 4.52,
              30000: float('nan')}
REF_EXTERNA = {500: -12.94, 1000: -14.27, 1600: -13.21, 2500: -14.01,
               4000: -14.33, 8000: -13.52, 15000: -12.33,
               30000: float('nan')}

MU = 1.0
MG2V, MF2V = 1.0, MU
ME2 = MU / (1.0 + MU)
M2 = 1.0
B0V, B2V, B4V = 1.0, -0.4, 0.5
B10 = 1.0
RHO0 = 0.3
VST = 1.0

say("=" * 72)
say("R-7c — BANDA NO POUSADO (beta1(phi-)) NO SISTEMA 2-DOF CORRIGIDO")
say("=" * 72)

if not d1.gr_selfcheck():
    say("[!] V1 falhou — abortando")
    sys.exit(1)
say("[V1] GR selfcheck da biblioteca: PASSA")

L2s, fields, vels = d1.build_L2()
K7, C7, W7 = quadratic_matrices(L2s, fields, vels)
if [str(f) for f in fields] != NOMES:
    raise RuntimeError("ordem de campos mudou")
say("[montagem] K,C,W 7x7 prontos")

say("[canal-S] dt_background(C7) simbolico ...")
Hdd_s, Hfdd_s, xidd_s, chiddd_s = sp.symbols(
    'Hddot H_fddot xiddot chidddot')
EXTRA_RATES = {Hd_s: Hdd_s, Hfd_s: Hfdd_s, xid_s: xidd_s,
               chidd_s: chiddd_s}
Cd7 = sp.zeros(7, 7)
for i in range(7):
    for j in range(7):
        Cd7[i, j] = dt_background(C7[i, j], EXTRA_RATES)
say("[canal-S] pronto")

LIVRES = (a_s, b_s, xi_s, H_s, Hf_s, Hd_s, Hfd_s, xid_s,
          chid_s, chidd_s, Ub, Up, Upp, ksym, Mf2, Meff2,
          Hdd_s, Hfdd_s, xidd_s, chiddd_s)
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


FK, FC, FW, FCd = fatias(K7), fatias(C7), fatias(W7), fatias(Cd7)
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
# fundo pousado (R-4b verbatim)
# ------------------------------------------------------------------
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
    return M2 * ME2 * Vf / (3 * MF2V * r**3)


def H2_of(r, ch, chd, a, vst, mu2, lam, U0):
    b1v = beta1(ch, vst)
    Vg = B0V + 3 * r * b1v + 3 * r * r * B2V
    return (0.5 * chd * chd + U_pot(ch, mu2, lam, U0) + RHO0 / a**3
            + M2 * ME2 * Vg) / (3 * MG2V)


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


def Om_num(r, ch, chd, a, vst, mu2, lam, U0):
    H2 = H2_of(r, ch, chd, a, vst, mu2, lam, U0)
    Hf2 = Hf2_of(r, ch, vst)
    if H2 <= 0 or Hf2 <= 0:
        return float('nan')
    return Om_fn(a, r * a, ch, chd, np.sqrt(H2), np.sqrt(Hf2),
                 MG2V, MF2V, ME2, M2, B0V, B2V, B4V, B10, vst)


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
    kap = MG2V / MF2V
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
        den = 3 * MG2V - 0.5 * y * y
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
                dHf=spl['Hfv'].derivative(), dr=spl['r'].derivative(),
                dchd=spl['chd'].derivative(),
                dchidd=spl['chidd'].derivative(), rotulo=rotulo)


def bg_ponto(ctx, N):
    """NOTA de consistencia de canal (achado da 1a rodada deste
    script, preservada no historico git): o fundo e integrado por
    Euler explicito (dN=5e-4), entao (i) o chidd ARMAZENADO
    (analitico, da EOM) e a derivada do spline de chd diferem em
    O(erro do integrador) na rolagem rapida, e (ii) o xi ARMAZENADO
    usa rp = Delta r/dN (1a ordem), quebrando a identidade
    bdot = b xi H_f que o canal-S (RATES da lib) assume, em relacao a
    derivada do spline de r. O V-XREP pegou isso (G3 6e-3..7e-2, 8/8
    bracos bloqueados). Correcao: as quantidades derivadas usadas
    pelas matrizes/Cdot passam a ser DERIVADAS DOS SPLINES dos
    valores (chidd = H chd_spl'; xi = H(1 + r_spl'/r)/H_f, que fecha
    a identidade bdot = b xi H_f por construcao). A diferenca para os
    valores Euler da EOM e erro de fidelidade do FUNDO, identico nos
    dois canais, e nao contamina o teste da reducao."""
    spl = ctx['spl']
    rec = ctx['rec']
    H = float(spl['H'](N))
    ch = float(spl['ch'](N))
    r = float(spl['r'](N))
    Hf = float(spl['Hfv'](N))
    mu2, lam, U0 = rec['mu2'], rec['lam'], rec['U0']
    a = np.exp(N)
    xi_c = H * (1.0 + float(ctx['dr'](N)) / r) / Hf
    return dict(
        a=a, r=r, xi=xi_c, H=H,
        Hf=Hf, ch=ch, chd=float(spl['chd'](N)),
        chidd=H * float(ctx['dchd'](N)),
        Hd=H * float(ctx['dH'](N)), Hfd=H * float(ctx['dHf'](N)),
        chiddd=H * float(ctx['dchidd'](N)),
        Ubv=U_pot(ch, mu2, lam, U0) + RHO0 / a**3,
        Upv=dU_pot(ch, mu2, lam), Uppv=-mu2 + 3 * lam * ch * ch)


def bg_ext(ctx, N, h=1e-4):
    """xid/xidd por estencil sobre xi_c(N) (funcao lisa de splines);
    Hdd/Hfdd por estencil sobre Hd/Hfd."""
    f = bg_ponto(ctx, N)
    fp = bg_ponto(ctx, N + h)
    fm = bg_ponto(ctx, N - h)
    H = f['H']
    xi_l = (fp['xi'] - fm['xi']) / (2 * h)          # dxi/dN
    xi_ll = (fp['xi'] - 2 * f['xi'] + fm['xi']) / h**2
    f['xid'] = H * xi_l
    f['xidd'] = f['Hd'] * xi_l + H * H * xi_ll
    f['Hdd'] = H * (fp['Hd'] - fm['Hd']) / (2 * h)
    f['Hfdd'] = H * (fp['Hfd'] - fm['Hfd']) / (2 * h)
    return f


def matriz_D(kc):
    return np.diag([1.0, 1.0 / kc, 1.0, 1.0, 1.0 / kc, 1.0 / kc**2, 1.0])


def build_track_pousado(ctx, npts, kc):
    Ns = np.linspace(np.log(A_MINP), np.log(A_MAX), npts)
    Hs_arr = np.zeros(npts)
    Ms = {x: np.zeros((npts, 7, 7)) for x in ('K', 'C', 'W', 'CdS')}
    D = matriz_D(kc)
    for p, N in enumerate(Ns):
        f = bg_ext(ctx, N)
        Hs_arr[p] = f['H']
        args = (f['a'], f['r'] * f['a'], f['xi'], f['H'], f['Hf'],
                f['Hd'], f['Hfd'], f['xid'], f['chd'], f['chidd'],
                f['Ubv'], f['Upv'], f['Uppv'], kc, MF2V, ME2,
                f['Hdd'], f['Hfdd'], f['xidd'], f['chiddd'])
        bvals = (B0V, beta1(f['ch'], VST), B2V, 0.0, B4V)
        bp = (0.0, dbeta1(f['ch'], VST), 0.0, 0.0, 0.0)
        bpp = (0.0, 2.0 * B10 / VST**2, 0.0, 0.0, 0.0)
        Ms['K'][p] = D @ monta(FK, args, bvals, bp, bpp) @ D
        Ms['C'][p] = D @ monta(FC, args, bvals, bp, bpp) @ D
        Ms['W'][p] = D @ monta(FW, args, bvals, bp, bpp) @ D
        Ms['CdS'][p] = D @ monta(FCd, args, bvals, bp, bpp) @ D
    return Ns, Hs_arr, Ms


# ------------------------------------------------------------------
# reducao corrigida (R-7b verbatim)
# ------------------------------------------------------------------
def e1_corrigida(Kt, Ct, Wt, Cdot):
    K = Kt.copy()
    C = Ct.copy()
    W = Wt.copy()
    n = K.shape[0]
    esc = max(1.0, np.max(np.abs(K)))
    mset = set(MULT)
    for i in MULT:
        if np.max(np.abs(K[i, :])) > 1e-10 * esc:
            raise RuntimeError(f"linha K do multiplicador {NOMES[i]} "
                               "nao-nula")
        for j in range(n):
            cd = Cdot[i, j]
            cij = Ct[i, j]
            if i == j:
                W[i, i] += cd
            elif j in mset:
                W[i, j] += cd
            else:
                W[i, j] += cd
                W[j, i] += cd
                C[j, i] -= cij
        C[i, :] = 0.0
    WXX = W[np.ix_(MULT, MULT)]
    WXX = 0.5 * (WXX + WXX.T)
    if np.linalg.cond(WXX) > 1e12:
        raise RuntimeError("W_XX mal condicionada")
    WXXi = np.linalg.inv(WXX)
    CdX = C[np.ix_(DYN, MULT)]
    K3 = K[np.ix_(DYN, DYN)] + CdX @ WXXi @ CdX.T
    C3 = C[np.ix_(DYN, DYN)] - CdX @ WXXi @ W[np.ix_(MULT, DYN)]
    W3 = W[np.ix_(DYN, DYN)] - W[np.ix_(DYN, MULT)] @ WXXi \
        @ W[np.ix_(MULT, DYN)]
    return K3, C3, W3, WXXi, CdX, W[np.ix_(MULT, DYN)]


def e2_psif(K3, C3, W3, C3dot):
    K = K3.copy()
    C = C3.copy()
    W = W3.copy()
    for j in range(3):
        cij = C3[0, j]
        cd = C3dot[0, j]
        if j == 0:
            W[0, 0] += cd
        else:
            W[0, j] += cd
            W[j, 0] += cd
            C[j, 0] -= cij
    C[0, :] = 0.0
    W00 = W[0, 0]
    keep = [1, 2]
    cx = C[np.ix_(keep, [0])]
    wx = W[np.ix_(keep, [0])]
    K2 = K[np.ix_(keep, keep)] + cx @ cx.T / W00
    C2 = C[np.ix_(keep, keep)] - cx @ W[np.ix_([0], keep)] / W00
    W2 = W[np.ix_(keep, keep)] - wx @ W[np.ix_([0], keep)] / W00
    return (0.5 * (K2 + K2.T), C2, 0.5 * (W2 + W2.T), W00,
            cx[:, 0].copy(), W[0, [1, 2]].copy())


def reduz_full(Ns, Hs_arr, Ms, canal):
    npts = len(Ns)
    if canal == 'G':
        Cdots = np.gradient(Ms['C'], Ns, axis=0) * Hs_arr[:, None, None]
    else:
        Cdots = Ms['CdS']
    K3s = np.zeros((npts, 3, 3))
    C3s = np.zeros((npts, 3, 3))
    W3s = np.zeros((npts, 3, 3))
    WXXi_s = np.zeros((npts, 4, 4))
    CdX_s = np.zeros((npts, 3, 4))
    WXd_s = np.zeros((npts, 4, 3))
    g1_max = 0.0
    for p in range(npts):
        K3, C3, W3, WXXi, CdX, WXd = e1_corrigida(
            Ms['K'][p], Ms['C'][p], Ms['W'][p], Cdots[p])
        esc = np.max(np.abs(K3))
        g1_max = max(g1_max, np.max(np.abs(K3[0, :])) / esc)
        K3[0, :] = 0.0
        K3[:, 0] = 0.0
        K3s[p], C3s[p], W3s[p] = K3, C3, W3
        WXXi_s[p], CdX_s[p], WXd_s[p] = WXXi, CdX, WXd
    C3d = np.gradient(C3s, Ns, axis=0) * Hs_arr[:, None, None]
    K2s = np.zeros((npts, 2, 2))
    C2s = np.zeros((npts, 2, 2))
    W2s = np.zeros((npts, 2, 2))
    W00s = np.zeros(npts)
    cx_s = np.zeros((npts, 2))
    w0k_s = np.zeros((npts, 2))
    for p in range(npts):
        K2s[p], C2s[p], W2s[p], W00s[p], cx_s[p], w0k_s[p] = \
            e2_psif(K3s[p], C3s[p], W3s[p], C3d[p])
    if npts > 6:
        for M in (K2s, C2s, W2s):
            M[0] = M[2]
            M[1] = M[2]
            M[-1] = M[-3]
            M[-2] = M[-3]
    return dict(K2=K2s, C2=C2s, W2=W2s, W00=W00s, cx=cx_s, w0k=w0k_s,
                WXXi=WXXi_s, CdX=CdX_s, WXd=WXd_s, g1=g1_max)


def evolui_2dof(K2, C2, W2, Ns, Hs_arr):
    npts = len(Ns)
    K2d = np.gradient(K2, Ns, axis=0) * Hs_arr[:, None, None]
    C2d = np.gradient(C2, Ns, axis=0) * Hs_arr[:, None, None]
    traj = {}
    for ic in range(4):
        q = np.zeros(2)
        qd = np.zeros(2)
        if ic < 2:
            q[ic] = 1.0
        else:
            qd[ic - 2] = 1.0
        hist = np.zeros((npts, 4))
        hist[0] = [q[0], q[1], qd[0], qd[1]]
        for p in range(npts - 1):
            dN = Ns[p + 1] - Ns[p]
            dt = dN / Hs_arr[p]
            Ki = np.linalg.inv(K2[p])
            A = K2d[p] + C2[p] - C2[p].T
            B = C2d[p] + W2[p]

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
            hist[p + 1] = [q[0], q[1], qd[0], qd[1]]
        traj[ic] = hist
    return traj


IC_ROT = ['Etil(pos)', 'dchi(pos)', 'Etil(vel)', 'dchi(vel)']


def envelope(hist, comp, K2, W2, Hs_arr):
    q = hist[:, comp]
    qd = hist[:, comp + 2]
    om2 = np.abs(W2[:, comp, comp] / K2[:, comp, comp])
    return np.sqrt(q * q + qd * qd / (om2 + Hs_arr**2))


def reconstrui_phig(hist, red, Ns, Hs_arr):
    npts = len(Ns)
    q2 = hist[:, :2]
    qd2 = hist[:, 2:]
    psi = np.zeros(npts)
    for p in range(npts):
        psi[p] = (red['cx'][p] @ qd2[p] - red['w0k'][p] @ q2[p]) \
            / red['W00'][p]
    psid = np.gradient(psi, Ns) * Hs_arr
    phig = np.zeros(npts)
    for p in range(npts):
        q3 = np.array([psi[p], q2[p][0], q2[p][1]])
        q3d = np.array([psid[p], qd2[p][0], qd2[p][1]])
        X = red['WXXi'][p] @ (red['CdX'][p].T @ q3d - red['WXd'][p] @ q3)
        phig[p] = X[0]
    return phig


# ------------------------------------------------------------------
say("")
say("[fundo POUSADO] reintegrando a trajetoria original ...")
BG = integra_alvo()
ok_org = (abs(BG['r'][-1] - 0.4979) < 0.005
          and abs(BG['ch'][-1] / BG['v'] - 0.932) < 0.005)
say(f"    r_fim={BG['r'][-1]:.4f}, chi/v_fim={BG['ch'][-1]/BG['v']:.3f}  "
    f"[{'CONFERE' if ok_org else 'DIVERGE'}]")
if not ok_org:
    say("[!] fundo divergiu das ancoras — abortando")
    sys.exit(1)
CTX = make_ctx(BG, "ORG")

resultados = {}
for a_c in A_CROSS:
    N_c = np.log(a_c)
    H_c = float(CTX['spl']['H'](N_c))
    kc = a_c * H_c
    say("")
    say("=" * 72)
    say(f"POUSADO — cruzamento em a_cross={a_c:g} (k_c={kc:.1f})")
    say("=" * 72)
    Ns, Hs_arr, Ms = build_track_pousado(CTX, NPTS, kc)
    red = reduz_full(Ns, Hs_arr, Ms, 'S')
    redG = reduz_full(Ns, Hs_arr, Ms, 'G')
    ok1 = red['g1'] < G1_TOL
    say(f"    [G1 {'OK' if ok1 else 'FALHOU'} canal-S] {red['g1']:.2e} "
        f"(< {G1_TOL:g}); canal-G {redG['g1']:.2e} (informativo)")
    dmax = 0.0
    for Mg, Msy in ((redG['K2'], red['K2']), (redG['C2'], red['C2']),
                    (redG['W2'], red['W2'])):
        esc = np.max(np.abs(Msy), axis=(1, 2), keepdims=True)
        dmax = max(dmax, float(np.max((np.abs(Mg - Msy) / esc)[2:-2])))
    ok3 = dmax < G3_TOL
    say(f"    [G3 {'OK' if ok3 else 'FALHOU'}] V-XREP interior = "
        f"{dmax:.2e} (< {G3_TOL:g}) — trilha DINAMICA")
    if not (ok1 and ok3):
        say("    >>> NAO INTERPRETAR este braco")
        resultados[a_c] = None
        continue
    K2, C2, W2 = red['K2'], red['C2'], red['W2']
    neg = int(sum(np.linalg.eigvalsh(K2[p])[0] <= 0
                  for p in range(NPTS)))
    say(f"    mapa cinetico: autovalores K2 negativos = {neg}/{NPTS}")
    traj = evolui_2dof(K2, C2, W2, Ns, Hs_arr)
    khs = kc / (np.exp(Ns) * Hs_arr)
    i20 = int(np.argmin(np.abs(khs - KH_PASS[0])))
    kh_fim = khs[-1]
    parcial = kh_fim > KH_PASS[1]
    i02 = NPTS - 1 if parcial else int(np.argmin(np.abs(khs - KH_PASS[1])))
    lnAs = []
    dphis = []
    for ic in range(4):
        A = envelope(traj[ic], 0, K2, W2, Hs_arr)
        ok = A[i20] > 1e-250 and A[i02] > 1e-250
        v = np.log(A[i02] / A[i20]) if ok else float('nan')
        lnAs.append(v)
        phig = reconstrui_phig(traj[ic], red, Ns, Hs_arr)
        seg = np.abs(phig[i20:i02 + 1])
        if np.max(seg) > 1e-250:
            dphis.append(np.log(max(seg[-1], 1e-300))
                         - np.log(max(seg[0], 1e-300)))
        else:
            dphis.append(float('nan'))
    rot_p = " (PARCIAL ate kh=%.2f)" % kh_fim if parcial else ""
    say(f"    lnA_passagem por IC{rot_p}:")
    for ic in range(4):
        say(f"      {IC_ROT[ic]:>10}: lnA_met = {lnAs[ic]:+8.3f}   "
            f"Delta ln|Phi_g| = {dphis[ic]:+8.3f}")
    lnA_met_max = float(np.nanmax([lnAs[0], lnAs[2]]))
    resultados[a_c] = dict(lnAs=lnAs, dphis=dphis, neg=neg,
                           lnA_met=lnA_met_max, parcial=parcial,
                           g3=dmax)

say("")
say("=" * 72)
say("VEREDITO R-7c (criterios pre-declarados no cabecalho)")
say("=" * 72)
say(f"  {'a_cross':>8} {'antigo3DOF':>11} {'externa':>9} "
    f"{'este(2DOF)':>11} {'negK':>5} {'nota':>8}")
todos_neg = True
algum_vivo = False
n_ok = 0
for a_c in A_CROSS:
    r = resultados.get(a_c)
    if r is None:
        say(f"  {a_c:8.0f} {'—':>11} {'—':>9} {'—':>11}")
        continue
    n_ok += 1
    nota = "PARCIAL" if r['parcial'] else ""
    say(f"  {a_c:8.0f} {REF_ANTIGO[int(a_c)]:+11.2f} "
        f"{REF_EXTERNA[int(a_c)]:+9.2f} {r['lnA_met']:+11.3f} "
        f"{r['neg']:5d} {nota:>8}")
    if np.isfinite(r['lnA_met']):
        if r['lnA_met'] >= 0:
            todos_neg = False
        if r['lnA_met'] >= 3.5:
            algum_vivo = True
if n_ok == 0:
    say("  >>> SEM VEREDITO: nenhum braco passou os gates (G1/G3) —")
    say("  nao ha numeros interpretaveis nesta rodada.")
elif algum_vivo:
    say("  >>> BANDA-VIVA dinamica — investigar antes de usar.")
elif todos_neg:
    say(f"  >>> POUSADO-BANDA-MORTA ({n_ok}/{len(A_CROSS)} bracos")
    say("  interpretaveis): nenhuma epoca de cruzamento amplifica; o")
    say("  R-4 dinamico (amplificacao por epoca e a 'supressao-")
    say("  materia' do R-4c) era artefato do 3o DOF espurio. R-4")
    say("  COMPLETO substituido pela reexecucao.")
else:
    say("  >>> intermediario — quantificar por epoca (tabela acima).")

os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
with open(os.path.join(HERE, 'out', 'r7c_banda_pousado_2dof.txt'), 'w',
          encoding='utf-8') as fh:
    fh.write("\n".join(OUT) + "\n")
say("")
say("saida escrita em auditoria/code/out/r7c_banda_pousado_2dof.txt")
