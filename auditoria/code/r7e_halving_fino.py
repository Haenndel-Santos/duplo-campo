# -*- coding: utf-8 -*-
"""
r7e_halving_fino.py — R-7e HALVING FINO (fecha o A4 do kh=10): as taxas +1.8..+11.6 H da
janela de deslocamento sao crescimento REAL do campo ou artefato do
envelope com omega^2(t) variavel?

CONTEXTO: r7e_faseB_2dof deu estrutura LIMPA (W00 sem trocas, negK=0
em 4/4 modos — sem FJ-quebra, sem fantasma) mas taxas de envelope
grandes e quase IC-independentes na janela, e E3 (cross-check do
fundo) reprovou (dif 1.39). O envelope de la usa
A = sqrt(q^2 + qd^2/(om2(t)+H^2)) com om2 = |W/K| — se om2 despenca
na janela, A infla SEM o campo crescer (a classe de artefato de
normalizacao que ja derrubou R-2 e F-b). Este script decide com
medidas robustas.

RODADA FINA: so kh=10 (o modo cujo A4 reprovou a 14000/7000:
dG=0.687), agora em NPTS 28000 vs 14000. Criterio identico
(dG < 0.3). Demais medidas herdadas.

MEDIDAS (originais da autopsia), mesmos 4 modos (kh_janela 10/3/1/0.3),
mesma trilha (Heun, NPTS=14000, canal-S, G1<1e-10):
  A1 — perfil de om2 por componente na janela: min/max e numero de
       cruzamentos de zero de W2_ii (o detector do artefato).
  A2 — GANHO DE CAMPO na janela com NORMALIZACAO CONGELADA:
       A_c = sqrt(q^2 + qd^2/(om2_c + H_c^2)) com om2_c, H_c FIXOS
       (valores do centro da janela) — uma unica normalizacao por
       modo/componente. G_win = ln[max A_c pos] - ln[max A_c pre],
       pre = [a_lo/1.35, a_lo], pos = [a_hi, 1.35 a_hi].
  A3 — taxa movel (0.25 e-fold) de ln A_c na janela (comparavel a
       taxa do r7e, agora sem normalizacao variavel).
  A4 — halving (NPTS 7000) em kh=10 e kh=0.3: |dG_win| < 0.3.
  A5 — fundos Euler vs Heun: max |dr|, |dch|/v, |dH|/H na janela
       (explica o E3; o lnA de passagem cruza a janela).
  A6 — Phi_g: ganho na janela (blocos corrigidos) — o numero
       observavel-adjacente.

CRITERIOS (pre-declarados):
  G_win < +0.5 em todos os modos/ICs (A2, confirmado por A4)
      -> ARTEFATO-DE-ENVELOPE: a janela e quieta; combinado com a
      estrutura limpa do r7e -> FASE-B-SA (o sigma/H ~ 13 antigo
      cai de vez).
  G_win >= +0.5 robusto em algum modo -> JANELA-AMPLIFICA: ha
      amplificacao transiente REAL na janela de deslocamento do
      sistema fisico 2-DOF (nao e fantasma: K2>0; nao e persistente:
      pos-pouso decai) — quantificar G_win(kh); relevancia
      observacional so no R-8 (dicionario de epocas).
  A4 falha -> reportar sem veredito (resolucao insuficiente).

Requer sympy, numpy, scipy. ~15-25 min.
Uso (raiz do repo, venv ativo):
    python auditoria/code/r7e_autopsia_janela.py
Saida em auditoria/code/out/r7e_autopsia_janela.txt
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
NPTS = 28000
G1_TOL = 1e-10
KH_JANELA = [10.0]
KH_HALV = (10.0,)
DESL_CORTE = 0.05

MU = 1.0
MG2V, MF2V = 1.0, MU
ME2 = MU / (1.0 + MU)
M2 = 1.0
B0V, B2V, B4V = 1.0, -0.4, 0.5
B10 = 1.0
RHO0 = 0.3
VST = 1.0

say("=" * 72)
say("R-7e AUTOPSIA — a janela amplifica o CAMPO ou so o envelope?")
say("=" * 72)

if not d1.gr_selfcheck():
    say("[!] V1 falhou — abortando")
    sys.exit(1)
say("[V1] GR selfcheck: PASSA")

L2s, fields, vels = d1.build_L2()
K7, C7, W7 = quadratic_matrices(L2s, fields, vels)
say("[montagem] K,C,W 7x7 prontos")

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


def integra(metodo, g_end=2.0, mchi2=30.0, a0=0.01, a1=1e5, dN=5e-4):
    """metodo: 'heun' ou 'euler' (para o A5)."""
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
        if metodo == 'heun':
            chp = ch + dN * d1c
            chdp = chd + dN * d1d
            d2c, d2d, r2, _, _, _, _ = rhs_fundo(
                N + dN, chp, chdp, r1, (r1 - r) / dN if i else rp,
                mu2, lam, U0)
            rp_c = (r2 - r) / (2 * dN) if i else (r2 - r1) / dN
            d1c, d1d, r1, H1, Hf1, xi1, chidd1 = rhs_fundo(
                N, ch, chd, r, rp_c, mu2, lam, U0)
            dch = 0.5 * dN * (d1c + d2c)
            dchd = 0.5 * dN * (d1d + d2d)
            rp_novo = (r2 - r1) / dN
        else:
            dch = dN * d1c
            dchd = dN * d1d
            rp_novo = rp
        if i % max(1, n // 20000) == 0:
            for kk, vv in (('N', N), ('a', np.exp(N)), ('r', r1),
                           ('xi', xi1), ('H', H1), ('Hfv', Hf1),
                           ('ch', ch), ('chd', chd), ('chidd', chidd1),
                           ('desl', (H1 - r1 * Hf1) / H1)):
                rec[kk].append(vv)
        ch += dch
        chd += dchd
        if metodo == 'euler':
            r_new = acha_raiz(r1, ch, chd, np.exp(N + dN), mu2, lam, U0)
            rp_novo = (r_new - r1) / dN if r_new else rp
        rp = rp_novo
        r = r1
    rec = {kk: np.array(vv) for kk, vv in rec.items()}
    rec['v'] = v
    rec['mu2'] = mu2
    rec['lam'] = lam
    rec['U0'] = U0
    return rec


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
            raise RuntimeError("linha K de multiplicador nao-nula")
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
    return K3, C3, W3


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


def reduz(Ns, Hs_arr, Ms):
    npts = len(Ns)
    Cdots = Ms['CdS']
    K3s = np.zeros((npts, 3, 3))
    C3s = np.zeros((npts, 3, 3))
    W3s = np.zeros((npts, 3, 3))
    g1_max = 0.0
    for p in range(npts):
        K3, C3, W3 = e1_corrigida(Ms['K'][p], Ms['C'][p], Ms['W'][p],
                                  Cdots[p])
        esc = np.max(np.abs(K3))
        g1_max = max(g1_max, np.max(np.abs(K3[0, :])) / esc)
        K3[0, :] = 0.0
        K3[:, 0] = 0.0
        K3s[p], C3s[p], W3s[p] = K3, C3, W3
    if g1_max >= G1_TOL:
        raise RuntimeError(f"G1 FALHOU: {g1_max:.2e}")
    C3d = np.gradient(C3s, Ns, axis=0) * Hs_arr[:, None, None]
    K2s = np.zeros((npts, 2, 2))
    C2s = np.zeros((npts, 2, 2))
    W2s = np.zeros((npts, 2, 2))
    for p in range(npts):
        K2s[p], C2s[p], W2s[p], _ = e2_psif(K3s[p], C3s[p], W3s[p],
                                            C3d[p])
    if npts > 6:
        for M in (K2s, C2s, W2s):
            M[0] = M[2]
            M[1] = M[2]
            M[-1] = M[-3]
            M[-2] = M[-3]
    return K2s, C2s, W2s


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


# ------------------------------------------------------------------
say("")
say("[fundos] integrando Heun e Euler (A5) ...")
BG_H = integra('heun')
BG_E = integra('euler')
say(f"    Heun:  r_fim={BG_H['r'][-1]:.4f}, chi/v={BG_H['ch'][-1]/BG_H['v']:.4f}")
say(f"    Euler: r_fim={BG_E['r'][-1]:.4f}, chi/v={BG_E['ch'][-1]/BG_E['v']:.4f}")

CTX = make_ctx(BG_H)
CTX_E = make_ctx(BG_E)

desl = BG_H['desl']
mask_w = np.abs(desl) > DESL_CORTE
a_w = BG_H['a'][mask_w]
a_wlo, a_whi = float(a_w.min()), float(a_w.max())
a_mid = np.sqrt(a_wlo * a_whi)
H_mid = float(CTX['spl']['H'](np.log(a_mid)))
say(f"    janela: a em [{a_wlo:.0f}, {a_whi:.0f}]; a_mid={a_mid:.0f}")

# A5 — diferenca dos fundos na janela
Nw = np.linspace(np.log(a_wlo), np.log(a_whi), 400)
dr_m = max(abs(float(CTX['spl']['r'](N)) - float(CTX_E['spl']['r'](N)))
           for N in Nw)
dch_m = max(abs(float(CTX['spl']['ch'](N)) - float(CTX_E['spl']['ch'](N)))
            for N in Nw) / BG_H['v']
dH_m = max(abs(float(CTX['spl']['H'](N)) - float(CTX_E['spl']['H'](N)))
           / float(CTX['spl']['H'](N)) for N in Nw)
say(f"    A5 — Heun vs Euler na janela: max|dr|={dr_m:.2e}, "
    f"max|dch|/v={dch_m:.2e}, max|dH|/H={dH_m:.2e}")
say("    (isto dimensiona o E3 do r7e: lnA de passagem cruza a janela")
say("     e herda a diferenca de fundo — sensibilidade reportada)")

resultados = {}
for khw in KH_JANELA:
    kc = khw * a_mid * H_mid
    say("")
    say("=" * 72)
    say(f"MODO kh(janela) = {khw:g}  (k_c = {kc:.1f})")
    say("=" * 72)
    runs = {NPTS: None}
    if khw in KH_HALV:
        runs[NPTS // 2] = None
    for npts in runs:
        Ns, Hs_arr, Ms = build_track(CTX, npts, kc)
        K2, C2, W2 = reduz(Ns, Hs_arr, Ms)
        traj = evolui(K2, C2, W2, Ns, Hs_arr)
        runs[npts] = (Ns, Hs_arr, K2, W2, traj)
    Ns, Hs_arr, K2, W2, traj = runs[NPTS]
    aas = np.exp(Ns)
    i_wlo = int(np.argmin(np.abs(aas - a_wlo)))
    i_whi = int(np.argmin(np.abs(aas - a_whi)))
    i_mid = int(np.argmin(np.abs(aas - a_mid)))
    i_pre = int(np.argmin(np.abs(aas - a_wlo / 1.35)))
    i_pos = int(np.argmin(np.abs(aas - a_whi * 1.35)))

    # A1 — perfil de om2
    say("    A1 — om2 = W2_ii/K2_ii na janela (min, max, cruzamentos "
        "de zero):")
    for comp, rot in ((0, 'Etil'), (1, 'dchi')):
        om2 = W2[i_wlo:i_whi, comp, comp] / K2[i_wlo:i_whi, comp, comp]
        s = np.sign(om2)
        cz = int(np.sum(s[1:] * s[:-1] < 0))
        say(f"        {rot:>5}: [{np.min(om2):+.3e}, {np.max(om2):+.3e}]"
            f"  cruzamentos = {cz}")

    # A2/A3 — ganho com normalizacao CONGELADA no centro da janela
    say("    A2 — G_win (norm. congelada no centro; pre->pos janela) e")
    say("    A3 — taxa movel max de ln A_c na janela:")
    G_max = -np.inf
    for ic in range(4):
        for comp, rot in ((0, 'Etil'), (1, 'dchi')):
            om2_c = abs(W2[i_mid, comp, comp] / K2[i_mid, comp, comp])
            H_c = Hs_arr[i_mid]
            q = traj[ic][:, comp]
            qd = traj[ic][:, comp + 2]
            Ac = np.sqrt(q * q + qd * qd / (om2_c + H_c**2))
            if np.max(Ac) < 1e-250:
                continue
            pre = np.max(Ac[i_pre:i_wlo + 1])
            pos = np.max(Ac[i_whi:i_pos + 1])
            G = float(np.log(max(pos, 1e-300) / max(pre, 1e-300)))
            best = -np.inf
            j0 = i_wlo
            for j in range(i_wlo, i_whi):
                while Ns[j] - Ns[j0] > 0.25:
                    j0 += 1
                if j0 == j or Ac[j0] < 1e-250 or Ac[j] < 1e-250:
                    continue
                if Ns[j] - Ns[j0] < 0.2:
                    continue
                best = max(best, (np.log(Ac[j]) - np.log(Ac[j0]))
                           / (Ns[j] - Ns[j0]))
            G_max = max(G_max, G)
            say(f"        {IC_ROT[ic]:>10}/{rot:<5} G_win = {G:+7.2f}"
                f"   taxa_movel = {best:+7.2f}")

    # A4 — halving
    dG_h = float('nan')
    if khw in KH_HALV:
        Nsh, Hsh, K2h, W2h, trajh = runs[NPTS // 2]
        aash = np.exp(Nsh)
        ih_pre = int(np.argmin(np.abs(aash - a_wlo / 1.35)))
        ih_wlo = int(np.argmin(np.abs(aash - a_wlo)))
        ih_whi = int(np.argmin(np.abs(aash - a_whi)))
        ih_pos = int(np.argmin(np.abs(aash - a_whi * 1.35)))
        ih_mid = int(np.argmin(np.abs(aash - a_mid)))
        dG_h = 0.0
        for ic in range(4):
            for comp in (0, 1):
                om2_c = abs(W2[i_mid, comp, comp] / K2[i_mid, comp, comp])
                H_c = Hs_arr[i_mid]

                def gwin(tr, Ac_idx):
                    q = tr[:, comp]
                    qd = tr[:, comp + 2]
                    Ac = np.sqrt(q * q + qd * qd / (om2_c + H_c**2))
                    pre = np.max(Ac[Ac_idx[0]:Ac_idx[1] + 1])
                    pos = np.max(Ac[Ac_idx[2]:Ac_idx[3] + 1])
                    return float(np.log(max(pos, 1e-300)
                                        / max(pre, 1e-300)))

                G1v = gwin(traj[ic], (i_pre, i_wlo, i_whi, i_pos))
                G2v = gwin(trajh[ic], (ih_pre, ih_wlo, ih_whi, ih_pos))
                dG_h = max(dG_h, abs(G1v - G2v))
        say(f"    A4 — halving: max |dG_win| = {dG_h:.3f} "
            f"({'OK' if dG_h < 0.3 else 'FALHOU'} < 0.3)")

    resultados[khw] = dict(G_max=G_max, dG=dG_h)

say("")
say("=" * 72)
say("VEREDITO AUTOPSIA (criterios pre-declarados no cabecalho)")
say("=" * 72)
amplifica = False
halv_ok = True
for khw in KH_JANELA:
    r = resultados[khw]
    say(f"  kh={khw:g}: G_win max = {r['G_max']:+.2f}"
        + (f"; halving dG = {r['dG']:.3f}" if np.isfinite(r['dG'])
           else ""))
    if r['G_max'] >= 0.5:
        amplifica = True
    if np.isfinite(r['dG']) and r['dG'] >= 0.3:
        halv_ok = False
if not halv_ok:
    say("  >>> A4 FALHOU — resolucao insuficiente; sem veredito.")
elif amplifica:
    say("  >>> JANELA-AMPLIFICA: ha amplificacao transiente REAL do")
    say("  campo na janela de deslocamento (norm. congelada, robusta a")
    say("  halving). NAO e fantasma (K2>0, r7e) e NAO e persistente")
    say("  (pos-pouso decai). As taxas de envelope do r7e eram")
    say("  parcialmente normalizacao, parcialmente isto — os G_win")
    say("  acima sao os numeros certos. Relevancia observacional:")
    say("  so no R-8 (dicionario de epocas).")
else:
    say("  >>> ARTEFATO-DE-ENVELOPE: a janela e quieta (G_win < 0.5")
    say("  em todos os modos). Com a estrutura limpa do r7e:")
    say("  FASE-B-SA — o sigma/H ~ 13 antigo cai de vez.")

os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
with open(os.path.join(HERE, 'out', 'r7e_halving_fino.txt'), 'w',
          encoding='utf-8') as fh:
    fh.write("\n".join(OUT) + "\n")
say("")
say("saida escrita em auditoria/code/out/r7e_autopsia_janela.txt")
