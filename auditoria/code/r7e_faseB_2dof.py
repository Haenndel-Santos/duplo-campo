# -*- coding: utf-8 -*-
"""
r7e_faseB_2dof.py — R-7e: FASE B CORRIGIDA. A janela de deslocamento
(regime nao-fatorado) no sistema 2-DOF, com fundo Heun (2a ordem) e
rastreio da estrutura de vinculos (W00).

CONTEXTO: erratum_02 + R-7a/b/c. A Investigacao 2 Fase B (2026-08-11,
investigacao2_faseB_pert.py) mediu sigma/H ate 13.08 na janela de
deslocamento (|H - r H_f|/H ate 0.48, a ~ [760, 2050]) e "contagem 3
em toda parte" — mas com DOIS instrumentos hoje sabidamente
comprometidos: QEP CONGELADO (invalidado como veredito dinamico pelo
D-2) sobre o sistema de 3 DOFs ESPURIO (erratum-02). A pergunta
fisica real continua aberta e e a ultima ameaca interna em pe: no
regime nao-fatorado, onde a estrutura de vinculos HR e estressada,
(i) a eliminacao de Psi_f continua valida (W00 != 0)? (ii) aparece
direcao cinetica negativa? (iii) ha crescimento real sustentado?

FUNDO (upgrade declarado): o integra_alvo original e Euler explicito
(dN=5e-4) — o V-XREP do R-7c pegou a inconsistencia das taxas
armazenadas (~1e-3). Aqui o fundo passa a HEUN (preditor-corretor,
2a ordem) no estado (chi, chidot):
    dchi/dN = chidot/H;  dchidot/dN = chiddot_EOM/H,
com (r, H, H_f) algebricos por avaliacao (r por raiz de Omega — chd
agora e estado, sem circularidade) e rp centrado no passo. M0
(metrica de consistencia): max |chidd_EOM - H d(spl_chd)/dN|/escala
— Euler ~O(dN), Heun ~O(dN^2); exigencia: queda >= 30x.
Ancoras: r_fim ~ 0.4979, chi/v ~ 0.932 (tolerancia 0.005).

JANELA: identificada do proprio fundo por |desl| = |H - r H_f|/H >
0.05 (Fase A: a ~ [760, 2050]); reportada. Modos: kh no CENTRO da
janela em {10, 3, 1, 0.3} (k = kh * a_mid * H(a_mid)).

MEDIDAS (pre-declaradas), por modo, trilha a=[20,80000], NPTS=14000,
reducao corrigida canal-S + V-XREP (G3 < 1e-3 interior):
  E1 — estrutura na janela: min |W00|/esc(W3); numero de trocas de
       sinal de W00 na trilha; max cond(W_XX); autovalores K2
       negativos (contagem na trilha inteira e na janela).
  E2 — dinamica: evolucao das 4 ICs; taxa max de envelope na janela
       (max d lnA/dt/H sobre janelas moveis de 0.25 e-fold, por
       componente) — confronto direto com o sigma/H ~ 13 antigo; e
       taxa pos-pouso (referencia: familia estacionaria decai).
  E3 — cross-check R-7c: braco a_cross=4000 refeito no fundo Heun:
       |lnA_heun - lnA_euler_spline| < 0.5 (a conclusao do R-7c nao
       pode depender do integrador do fundo).

CRITERIOS (pre-declarados):
  G1/G3 falham em algum modo -> NAO INTERPRETAR o modo.
  W00 troca de sinal na janela -> FJ-QUEBRA: achado ESTRUTURAL real
      (a eliminacao de Psi_f falha ali; exige FJ com troca de
      vinculo, fora deste script) — reportar local, sem veredito de
      saude.
  Sem troca de W00 e negK=0 e taxa max na janela < +0.5 sustentada
      (>= 0.25 e-fold) -> FASE-B-SA: o "sigma/H ~ 13" era artefato
      dos instrumentos; o no-go nao-fatorado cai; saude interna
      completa-se na trajetoria REF.
  Taxa sustentada >= +0.5 ou negK > 0 -> SUSPEITO: reportar com
      halving antes de qualquer leitura (nao concluir aqui).
  FRONTEIRA declarada: UMA trajetoria (g=2, m30, v*=1), celula REF —
      mesma fronteira da Fase A/B original.

Requer sympy, numpy, scipy. ~12-20 min.
Uso (raiz do repo, venv ativo):
    python auditoria/code/r7e_faseB_2dof.py
Saida em auditoria/code/out/r7e_faseB_2dof.txt
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
KH_JANELA = [10.0, 3.0, 1.0, 0.3]
DESL_CORTE = 0.05
TAXA_CORTE = 0.5
SUST_EFOLD = 0.25

MU = 1.0
MG2V, MF2V = 1.0, MU
ME2 = MU / (1.0 + MU)
M2 = 1.0
B0V, B2V, B4V = 1.0, -0.4, 0.5
B10 = 1.0
RHO0 = 0.3
VST = 1.0

say("=" * 72)
say("R-7e — FASE B CORRIGIDA: janela de deslocamento no 2-DOF, fundo")
say("Heun, rastreio de W00")
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
# fundo pousado — HEUN (2a ordem), estado (chi, chidot)
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


def H_de(r, ch, chd, a, mu2, lam, U0):
    b1v = beta1(ch, VST)
    Vg = B0V + 3 * r * b1v + 3 * r * r * B2V
    resto = 0.5 * chd * chd + U_pot(ch, mu2, lam, U0) + RHO0 / a**3 \
        + M2 * ME2 * Vg
    if resto <= 0:
        return None
    return np.sqrt(resto / (3 * MG2V))


def Om_num(r, ch, chd, a, mu2, lam, U0):
    H = H_de(r, ch, chd, a, mu2, lam, U0)
    Hf2 = Hf2_of(r, ch, VST)
    if H is None or Hf2 <= 0:
        return float('nan')
    return Om_fn(a, r * a, ch, chd, H, np.sqrt(Hf2),
                 MG2V, MF2V, ME2, M2, B0V, B2V, B4V, B10, VST)


def acha_raiz(r_prev, ch, chd, a, mu2, lam, U0):
    for fator in (0.08, 0.25, 0.6):
        lo, hi = r_prev * (1 - fator), r_prev * (1 + fator)
        grade = np.linspace(lo, hi, 61)
        vals = np.array([Om_num(x, ch, chd, a, mu2, lam, U0)
                         for x in grade])
        fin = np.isfinite(vals)
        for i in range(len(grade) - 1):
            if fin[i] and fin[i + 1] and vals[i] * vals[i + 1] < 0:
                try:
                    return brentq(
                        lambda x: Om_num(x, ch, chd, a, mu2, lam, U0),
                        grade[i], grade[i + 1], xtol=1e-14)
                except ValueError:
                    continue
    return None


def raiz_cubica(a, ch, chd, mu2, lam, U0):
    b1v = beta1(ch, VST)
    rho_tot = 0.5 * chd * chd + U_pot(ch, mu2, lam, U0) + RHO0 / a**3
    rt = rho_tot / (M2 * ME2)
    kap = MG2V / MF2V
    rr = np.roots([kap * B4V - 3 * B2V, -3 * b1v,
                   3 * kap * B2V - B0V - rt, kap * b1v])
    reais = sorted(x.real for x in rr if abs(x.imag) < 1e-9 and x.real > 1e-12)
    return reais[0] if reais else None


def rhs_fundo(N, ch, chd, r_seed, rp_est, mu2, lam, U0):
    """dch/dN, dchd/dN, r, H, Hf, xi no ponto."""
    a = np.exp(N)
    r = acha_raiz(r_seed, ch, chd, a, mu2, lam, U0)
    if r is None:
        raise RuntimeError(f"raiz perdida em a={a:.3f}")
    H = H_de(r, ch, chd, a, mu2, lam, U0)
    Hf = np.sqrt(Hf2_of(r, ch, VST))
    xi = H * (1.0 + rp_est / r) / Hf
    chidd = (-3 * H * chd - dU_pot(ch, mu2, lam)
             - M2 * ME2 * dbeta1(ch, VST) * (xi + 3 * r))
    return chd / H, chidd / H, r, H, Hf, xi, chidd


def integra_heun(g_end=2.0, mchi2=30.0, a0=0.01, a1=1e5, dN=5e-4):
    v = g_end * VST
    mu2 = 0.5 * mchi2
    lam = mu2 / (v * v)
    U0 = 0.25 * mu2 * v * v
    N0, N1 = np.log(a0), np.log(a1)
    n = int((N1 - N0) / dN) + 1
    ch, chd = 1e-3 * v, 0.0
    r = raiz_cubica(a0, ch, chd, mu2, lam, U0)
    rp = 0.0
    rec = {kk: [] for kk in ('N', 'a', 'r', 'xi', 'H', 'Hfv', 'ch', 'chd',
                             'chidd', 'desl')}
    for i in range(n):
        N = N0 + i * dN
        d1c, d1d, r1, H1, Hf1, xi1, chidd1 = rhs_fundo(
            N, ch, chd, r, rp, mu2, lam, U0)
        # preditor
        chp = ch + dN * d1c
        chdp = chd + dN * d1d
        d2c, d2d, r2, H2, Hf2v, xi2, _ = rhs_fundo(
            N + dN, chp, chdp, r1, (r1 - r) / dN if i else rp,
            mu2, lam, U0)
        # rp centrado do passo (consistente 2a ordem)
        rp_c = (r2 - r) / (2 * dN) if i else (r2 - r1) / dN
        # corretor com rp centrado
        d1c, d1d, r1, H1, Hf1, xi1, chidd1 = rhs_fundo(
            N, ch, chd, r, rp_c, mu2, lam, U0)
        if i % max(1, n // 20000) == 0:
            for kk, vv in (('N', N), ('a', np.exp(N)), ('r', r1),
                           ('xi', xi1), ('H', H1), ('Hfv', Hf1),
                           ('ch', ch), ('chd', chd), ('chidd', chidd1),
                           ('desl', (H1 - r1 * Hf1) / H1)):
                rec[kk].append(vv)
        ch = ch + 0.5 * dN * (d1c + d2c)
        chd = chd + 0.5 * dN * (d1d + d2d)
        rp = (r2 - r1) / dN
        r = r1
    rec = {kk: np.array(vv) for kk, vv in rec.items()}
    rec['v'] = v
    rec['mu2'] = mu2
    rec['lam'] = lam
    rec['U0'] = U0
    return rec


def consistencia_M0(rec):
    """max |chidd_EOM - H d(spl_chd)/dN| / escala, regiao rolante."""
    spl_chd = CubicSpline(rec['N'], rec['chd'])
    dchd = spl_chd.derivative()
    Ns = rec['N']
    mask = (rec['a'] > 100) & (rec['a'] < 20000)
    num = np.abs(rec['chidd'][mask]
                 - rec['H'][mask] * dchd(Ns[mask]))
    esc = np.max(np.abs(rec['chidd'][mask])) + 1e-300
    return float(np.max(num) / esc)


def make_ctx(rec):
    spl = {kk: CubicSpline(rec['N'], rec[kk])
           for kk in ('r', 'xi', 'H', 'Hfv', 'ch', 'chd', 'chidd')}
    return dict(rec=rec, spl=spl, dH=spl['H'].derivative(),
                dHf=spl['Hfv'].derivative(), dr=spl['r'].derivative(),
                dchd=spl['chd'].derivative(),
                dchidd=spl['chidd'].derivative())


def bg_ponto(ctx, N):
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
    f = bg_ponto(ctx, N)
    fp = bg_ponto(ctx, N + h)
    fm = bg_ponto(ctx, N - h)
    H = f['H']
    xi_l = (fp['xi'] - fm['xi']) / (2 * h)
    xi_ll = (fp['xi'] - 2 * f['xi'] + fm['xi']) / h**2
    f['xid'] = H * xi_l
    f['xidd'] = f['Hd'] * xi_l + H * H * xi_ll
    f['Hdd'] = H * (fp['Hd'] - fm['Hd']) / (2 * h)
    f['Hfdd'] = H * (fp['Hfd'] - fm['Hfd']) / (2 * h)
    return f


def matriz_D(kc):
    return np.diag([1.0, 1.0 / kc, 1.0, 1.0, 1.0 / kc, 1.0 / kc**2, 1.0])


def build_track(ctx, npts, kc):
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
    condW = np.linalg.cond(WXX)
    if condW > 1e12:
        raise RuntimeError("W_XX mal condicionada")
    WXXi = np.linalg.inv(WXX)
    CdX = C[np.ix_(DYN, MULT)]
    K3 = K[np.ix_(DYN, DYN)] + CdX @ WXXi @ CdX.T
    C3 = C[np.ix_(DYN, DYN)] - CdX @ WXXi @ W[np.ix_(MULT, DYN)]
    W3 = W[np.ix_(DYN, DYN)] - W[np.ix_(DYN, MULT)] @ WXXi \
        @ W[np.ix_(MULT, DYN)]
    return K3, C3, W3, condW


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
    return 0.5 * (K2 + K2.T), C2, 0.5 * (W2 + W2.T), W00


def reduz(Ns, Hs_arr, Ms, canal):
    npts = len(Ns)
    if canal == 'G':
        Cdots = np.gradient(Ms['C'], Ns, axis=0) * Hs_arr[:, None, None]
    else:
        Cdots = Ms['CdS']
    K3s = np.zeros((npts, 3, 3))
    C3s = np.zeros((npts, 3, 3))
    W3s = np.zeros((npts, 3, 3))
    g1_max = 0.0
    cond_max = 0.0
    for p in range(npts):
        K3, C3, W3, condW = e1_corrigida(
            Ms['K'][p], Ms['C'][p], Ms['W'][p], Cdots[p])
        esc = np.max(np.abs(K3))
        g1_max = max(g1_max, np.max(np.abs(K3[0, :])) / esc)
        cond_max = max(cond_max, condW)
        K3[0, :] = 0.0
        K3[:, 0] = 0.0
        K3s[p], C3s[p], W3s[p] = K3, C3, W3
    C3d = np.gradient(C3s, Ns, axis=0) * Hs_arr[:, None, None]
    K2s = np.zeros((npts, 2, 2))
    C2s = np.zeros((npts, 2, 2))
    W2s = np.zeros((npts, 2, 2))
    W00s = np.zeros(npts)
    w00rel = np.zeros(npts)
    for p in range(npts):
        K2s[p], C2s[p], W2s[p], W00s[p] = e2_psif(
            K3s[p], C3s[p], W3s[p], C3d[p])
        w00rel[p] = abs(W00s[p]) / np.max(np.abs(W3s[p]))
    if npts > 6:
        for M in (K2s, C2s, W2s):
            M[0] = M[2]
            M[1] = M[2]
            M[-1] = M[-3]
            M[-2] = M[-3]
        W00s[0] = W00s[1] = W00s[2]
        W00s[-1] = W00s[-2] = W00s[-3]
    return dict(K2=K2s, C2=C2s, W2=W2s, W00=W00s, w00rel=w00rel,
                g1=g1_max, cond=cond_max)


def evolui(K2, C2, W2, Ns, Hs_arr):
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


def taxa_movel(A, Ns, Hs_arr, i_lo, i_hi, larg=0.25):
    """max taxa media sobre janelas moveis de `larg` e-folds."""
    best = -np.inf
    j0 = i_lo
    for j in range(i_lo, i_hi):
        while Ns[j] - Ns[j0] > larg:
            j0 += 1
        if j0 == j or A[j0] < 1e-250 or A[j] < 1e-250:
            continue
        dNw = Ns[j] - Ns[j0]
        if dNw < larg * 0.8:
            continue
        tx = (np.log(A[j]) - np.log(A[j0])) / dNw
        best = max(best, tx)
    return best


# ------------------------------------------------------------------
say("")
say("[fundo HEUN] integrando ...")
BG = integra_heun()
ok_anc = (abs(BG['r'][-1] - 0.4979) < 0.005
          and abs(BG['ch'][-1] / BG['v'] - 0.932) < 0.005)
say(f"    r_fim={BG['r'][-1]:.4f}, chi/v_fim={BG['ch'][-1]/BG['v']:.3f}  "
    f"[{'CONFERE' if ok_anc else 'DIVERGE'}]")
M0 = consistencia_M0(BG)
say(f"    M0 (consistencia chidd vs spline) = {M0:.3e}")
say("    referencia Euler (R-7c, mesma metrica): ~1e-3 — exigencia de")
say("    queda >= 30x => M0 < 3e-5" +
    ("  [OK]" if M0 < 3e-5 else "  [FALHOU]"))
if not ok_anc:
    say("[!] ancoras divergiram — abortando")
    sys.exit(1)
CTX = make_ctx(BG)

# janela de deslocamento
desl = BG['desl']
mask_w = np.abs(desl) > DESL_CORTE
a_w = BG['a'][mask_w]
a_wlo, a_whi = (float(a_w.min()), float(a_w.max())) if a_w.size else \
    (float('nan'), float('nan'))
say(f"    janela |desl|>{DESL_CORTE:g}: a em [{a_wlo:.0f}, {a_whi:.0f}]; "
    f"max|desl| = {np.max(np.abs(desl)):.3f} "
    f"(Fase A: [760, 2050], 0.48)")
a_mid = np.sqrt(a_wlo * a_whi)
H_mid = float(CTX['spl']['H'](np.log(a_mid)))

resultados = {}
for khw in KH_JANELA:
    kc = khw * a_mid * H_mid
    say("")
    say("=" * 72)
    say(f"MODO kh(janela) = {khw:g}  (k_c = {kc:.1f})")
    say("=" * 72)
    Ns, Hs_arr, Ms = build_track(CTX, NPTS, kc)
    red = reduz(Ns, Hs_arr, Ms, 'S')
    redG = reduz(Ns, Hs_arr, Ms, 'G')
    ok1 = red['g1'] < G1_TOL
    dmax = 0.0
    for Mg, Msy in ((redG['K2'], red['K2']), (redG['C2'], red['C2']),
                    (redG['W2'], red['W2'])):
        esc = np.max(np.abs(Msy), axis=(1, 2), keepdims=True)
        dmax = max(dmax, float(np.max((np.abs(Mg - Msy) / esc)[2:-2])))
    ok3 = dmax < G3_TOL
    say(f"    [G1 {'OK' if ok1 else 'FALHOU'}] {red['g1']:.2e}; "
        f"[G3 {'OK' if ok3 else 'FALHOU'}] V-XREP {dmax:.2e}")
    if not (ok1 and ok3):
        say("    >>> NAO INTERPRETAR este modo")
        resultados[khw] = None
        continue
    aas = np.exp(Ns)
    i_wlo = int(np.argmin(np.abs(aas - a_wlo)))
    i_whi = int(np.argmin(np.abs(aas - a_whi)))

    # E1 — estrutura
    W00 = red['W00']
    sinais = np.sign(W00)
    trocas = int(np.sum(sinais[1:] * sinais[:-1] < 0))
    trocas_w = int(np.sum(sinais[i_wlo + 1:i_whi]
                          * sinais[i_wlo:i_whi - 1] < 0))
    w00_min_w = float(np.min(red['w00rel'][i_wlo:i_whi]))
    K2 = red['K2']
    neg_tot = int(sum(np.linalg.eigvalsh(K2[p])[0] <= 0
                      for p in range(NPTS)))
    neg_w = int(sum(np.linalg.eigvalsh(K2[p])[0] <= 0
                    for p in range(i_wlo, i_whi)))
    say(f"    E1 — W00: trocas de sinal = {trocas} (janela: {trocas_w}); "
        f"min|W00|/esc na janela = {w00_min_w:.2e}")
    say(f"         cond(W_XX) max = {red['cond']:.2e}; K2 negativos: "
        f"{neg_tot}/{NPTS} (janela: {neg_w})")

    # E2 — dinamica
    traj = evolui(K2, red['C2'], red['W2'], Ns, Hs_arr)
    say(f"    E2 — taxa max de envelope na janela (janelas moveis de "
        f"{SUST_EFOLD:g} e-fold) e taxa pos-pouso:")
    tx_max = -np.inf
    i_pos = int(np.argmin(np.abs(aas - A_MAX / np.exp(0.5))))
    for ic in range(4):
        for comp, rot in ((0, 'Etil'), (1, 'dchi')):
            A = envelope(traj[ic], comp, K2, red['W2'], Hs_arr)
            if np.max(A) < 1e-250:
                continue
            txw = taxa_movel(A, Ns, Hs_arr, i_wlo, i_whi, SUST_EFOLD)
            seg = np.log(np.maximum(A[i_pos:], 1e-300))
            txp = float(np.polyfit(Ns[i_pos:], seg, 1)[0])
            tx_max = max(tx_max, txw)
            say(f"      {IC_ROT[ic]:>10}/{rot:<5} taxa_janela = "
                f"{txw:+7.2f}  taxa_pos-pouso = {txp:+7.2f}")
    resultados[khw] = dict(trocas=trocas, trocas_w=trocas_w,
                           w00_min=w00_min_w, neg=neg_tot, neg_w=neg_w,
                           tx_max=tx_max, g3=dmax)

# E3 — cross-check R-7c no fundo Heun (a_cross=4000)
say("")
say("=" * 72)
say("E3 — cross-check R-7c (a_cross=4000) no fundo Heun")
say("=" * 72)
N_c = np.log(4000.0)
kc = 4000.0 * float(CTX['spl']['H'](N_c))
Ns, Hs_arr, Ms = build_track(CTX, NPTS, kc)
red = reduz(Ns, Hs_arr, Ms, 'S')
K2 = red['K2']
traj = evolui(K2, red['C2'], red['W2'], Ns, Hs_arr)
khs = kc / (np.exp(Ns) * Hs_arr)
i20 = int(np.argmin(np.abs(khs - 20.0)))
i02 = int(np.argmin(np.abs(khs - 0.2)))
A = envelope(traj[0], 0, K2, red['W2'], Hs_arr)
lnA_heun = float(np.log(A[i02] / A[i20]))
dif_e3 = abs(lnA_heun - (-11.403))
say(f"    lnA_passagem Etil(pos) fundo Heun = {lnA_heun:+.3f} "
    f"(R-7c Euler+spline: -11.403; dif {dif_e3:.3f} "
    f"{'OK' if dif_e3 < 0.5 else 'FALHOU'} < 0.5)")

say("")
say("=" * 72)
say("VEREDITO R-7e (criterios pre-declarados no cabecalho)")
say("=" * 72)
say(f"  fundo Heun: ancoras CONFEREM; M0 = {M0:.2e}")
ok_all = True
quebra = False
suspeito = False
for khw in KH_JANELA:
    r = resultados.get(khw)
    if r is None:
        ok_all = False
        say(f"  kh={khw:g}: NAO INTERPRETADO (gates)")
        continue
    say(f"  kh={khw:g}: W00 trocas {r['trocas']} (janela {r['trocas_w']});"
        f" negK {r['neg']} (janela {r['neg_w']}); taxa max janela "
        f"{r['tx_max']:+.2f}")
    if r['trocas_w'] > 0:
        quebra = True
    if r['neg'] > 0 or r['tx_max'] >= TAXA_CORTE:
        suspeito = True
say(f"  E3 cross-check: dif = {dif_e3:.3f} "
    f"({'OK' if dif_e3 < 0.5 else 'FALHOU'})")
if quebra:
    say("  >>> FJ-QUEBRA na janela: a eliminacao de Psi_f falha ali —")
    say("  achado estrutural real; exige FJ com troca de vinculo antes")
    say("  de qualquer enunciado de saude na janela.")
elif suspeito:
    say("  >>> SUSPEITO: ha taxa sustentada >= +0.5 ou direcao K2")
    say("  negativa — repetir com halving antes de qualquer leitura.")
elif ok_all:
    say("  >>> FASE-B-SA: sem troca de W00, sem direcao cinetica")
    say("  negativa, sem crescimento sustentado na janela de")
    say("  deslocamento. O 'sigma/H ~ 13' da Fase B antiga era")
    say("  artefato (QEP congelado + 3-DOF espurio). Com R-7a/b/c,")
    say("  a saude interna da trajetoria REF esta completa.")
    say("  Fronteira declarada: uma trajetoria, uma celula (como a")
    say("  Fase B original); ramo algebrico segue pendente (deferido).")

os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
with open(os.path.join(HERE, 'out', 'r7e_faseB_2dof.txt'), 'w',
          encoding='utf-8') as fh:
    fh.write("\n".join(OUT) + "\n")
say("")
say("saida escrita em auditoria/code/out/r7e_faseB_2dof.txt")
