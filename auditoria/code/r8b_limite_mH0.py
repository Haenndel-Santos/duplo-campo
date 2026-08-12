# -*- coding: utf-8 -*-
"""
r8b_limite_mH0.py — R-8b: o LIMITE sobre m_T/H0 dos vinculos de
crescimento/lensing — confronto com o postulado 30-300 H0 do corpus.

CONTEXTO: R-8a (resultado_r8a_quase_estatico.md) mediu mu/Sigma
subpercentuais no benchmark (m_T/H ~ 3.5) e identificou a alavanca:
o desvio escala ~ (m/aH)^2/kh^2. O corpus POSTULA m ~ 30-300 H0.
Este script trata m_T/H0 como LIVRE e deriva o limite observacional
— o confronto com o postulado vira RESULTADO, nao premissa.

A FAMILIA DE FUNDOS (o dial):
  beta_n -> s*beta_n (escala da interacao) + U0 (energia de vacuo do
  chi) escolhido por s para manter o H tardio IGUAL ao do benchmark
  (mesma historia de expansao; Omega_m(a0)=0.3 define "hoje").
  Algebra: as duas Friedmanns dao o MESMO cubico do fundo original
  com rho_til -> (rho_m + U0)/(s*meff^2); H^2 = s*meff^2 r^2 V_f/(3mu).
  s -> 0: GR + Lambda_chi (limite suave). s grande: r satura em
  r_inf < 1.25 e m_T ~ sqrt(s); U0 -> negativo grande — NOTA: o
  postulado m >> H0 EXIGE esse ajuste fino (vacuo-chi negativo
  cancelando a energia da interacao) — registrado como observacao
  estrutural.
  Raizes por CONTINUACAO (seed do a anterior / s anterior) — a
  selecao cega "menor raiz positiva" quebra quando rho_til_eff < 0.

m_T pela FORMULA DO PROJETO (derivations/02, caixa):
  m_T^2 = m^2 F M_eff^2 (1/M_g^2 + xi/(M_f^2 r^3)) r [b1+b2(xi+r)]
  (b3=0), avaliada em a0; eixo do resultado: m_T/H0.

SAUDE POR MEMBRO (gate — nunca derivar limites em familia doente):
  para cada s: mini-trilhas flat-gauge (maquinaria R-7f: reducao
  corrigida canal-S, G1<1e-10) em 3 epocas x kh {2, 30}:
  K2-positividade + W00 estavel. Violacao -> membro excluido do
  limite e reportado.

MU/SIGMA (pipeline R-8a, com correcao): razoes bimetrico/GR, gauge
Newtoniano, fonte em Phi_g. CORRECAO vs R-8a: o Ub bimetrico agora e
U0 = 3H^2 - rho_m - s*rho_int (o R-8a usava 3H^2 - rho_int, sem
subtrair rho_m — efeito <= 0.1% na era de materia, so afetava a=0.1;
linha de consistencia s=1 reportada).

JANELA OBSERVACIONAL (dicionario minimo, declarado):
  z in {0, 0.5, 1}; k in {0.05, 0.10, 0.15} h/Mpc;
  kh(z,k) = 3000*k[h/Mpc] * (a0 H0)/(a H(a)) — todos com kh >> 22
  (regiao QS-confiavel do R-8a).
  LIMITES ADOTADOS (valores de referencia, ordem de grandeza da
  literatura de parametrizacoes MG; o confronto fino com likelihoods
  reais e nivel-paper, declarado):
     |mu - 1| <= 0.15   e   |Sigma - 1| <= 0.10
  Sensibilidade reportada tambem para limites {0.05, 0.30}.

CRITERIOS (pre-declarados):
  O limite m*(lim) = maior m_T/H0 da familia com todos os pontos da
  janela dentro dos limites (interpolacao log em s).
  m* < 30    -> POSTULADO EXCLUIDO pela janela adotada.
  30 <= m* <= 300 -> POSTULADO PARCIALMENTE EXCLUIDO (faixa acima de
      m* cai); reportar a fracao.
  m* > 300   -> postulado compativel com crescimento (o teste vai
      para o C_ell/quase-horizonte).
  V-CONSIST: membro s=1 reproduz o R-8a (|d(mu)| < 2e-3 na era
      Lambda; era de materia difere pela correcao do Ub — reportar).

Requer sympy, numpy, scipy. ~6-12 min.
Uso (raiz do repo, venv ativo):
    python auditoria/code/r8b_limite_mH0.py
Saida em auditoria/code/out/r8b_limite_mH0.txt
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
                           interaction_lagrangian, chi_lagrangian,
                           scalar_metric_g, scalar_metric_f,
                           substitute_bg_functions, make_bg_functions,
                           z_average, eps_part, cut, symbolize,
                           dt_background)

T0 = time.time()
OUT = []


def say(*a):
    line = " ".join(str(x) for x in a)
    print(f"[{time.time()-T0:7.1f}s] {line}")
    OUT.append(line)


NOMES_N = ['Phi_g', 'Psi_g', 'Phi_f', 'Psi_f', 'B_f', 'E_f', 'dchi']
NOMES_F = ['Phi_g', 'B_g', 'Phi_f', 'Psi_f', 'B_f', 'E_f', 'dchi']
MULT = [0, 1, 2, 4]
DYN = [3, 5, 6]
G1_TOL = 1e-10

S_GRID = [0.25, 0.5, 1.0, 2.0, 3.0, 4.0, 5.0, 5.5, 6.0, 6.2]
Z_GRID = [0.0, 0.5, 1.0]
K_HMPC = [0.05, 0.10, 0.15]
LIMITES = {'mu': 0.15, 'Sig': 0.10}
LIM_SENS = [0.05, 0.30]
OMEGA_M0 = 0.3

MU_P = 1.0
ME2 = 0.5
B0V, B1V, B2V, B4V = 1.0, 1.0, -0.4, 0.5
RHO0 = 0.3

say("=" * 72)
say("R-8b — LIMITE SOBRE m_T/H0 DOS VINCULOS DE CRESCIMENTO")
say("=" * 72)

if not d1.gr_selfcheck():
    say("[!] V1 falhou — abortando")
    sys.exit(1)
say("[V1] GR selfcheck: PASSA")

# ------------------------------------------------------------------
# A. L2s simbolicas: Newtoniana (mu/Sigma) e flat (saude)
# ------------------------------------------------------------------
say("[montagem] L2 Newtoniana (mu/Sigma) ...")
Phi_gF = sp.Function('Phi_g')(t)
Psi_gF = sp.Function('Psi_g')(t)
B_gF = sp.Function('B_g')(t)
Phi_fF = sp.Function('Phi_f')(t)
Psi_fF = sp.Function('Psi_f')(t)
B_fF = sp.Function('B_f')(t)
E_fF = sp.Function('E_f')(t)
dchiF = sp.Function('dchi')(t)

aF, bF, xiF, bg_rules = make_bg_functions()
gN = substitute_bg_functions(
    scalar_metric_g(Phi_gF, Psi_gF, None, None), aF, bF, xiF)
fN = substitute_bg_functions(
    scalar_metric_f(Phi_fF, Psi_fF, B_fF, E_fF), aF, bF, xiF)
L2N = z_average(eps_part(cut(
    lagrangian_GG(gN, Mg2) + lagrangian_GG(fN, Mf2)
    + interaction_lagrangian(gN, fN, dchi=dchiF)
    + chi_lagrangian(gN, dchi=dchiF)), 2))
L2sN, fN_, vN_ = symbolize(L2N, [Phi_gF, Psi_gF, Phi_fF, Psi_fF,
                                 B_fF, E_fF, dchiF], bg_rules)
if [str(f) for f in fN_] != NOMES_N:
    raise RuntimeError("ordem N mudou")
_, _, W7N = quadratic_matrices(L2sN, fN_, vN_)

L2G = z_average(eps_part(cut(
    lagrangian_GG(gN, Mg2) + chi_lagrangian(gN, dchi=dchiF)), 2))
L2sG, fG_, vG_ = symbolize(L2G, [Phi_gF, Psi_gF, dchiF], bg_rules)
_, _, W3G = quadratic_matrices(L2sG, fG_, vG_)
say("[montagem] W7N, W3G prontas")

say("[montagem] L2 flat (saude) ...")
gF = substitute_bg_functions(
    scalar_metric_g(Phi_gF, sp.Integer(0), B_gF, None), aF, bF, xiF)
fF = substitute_bg_functions(
    scalar_metric_f(Phi_fF, Psi_fF, B_fF, E_fF), aF, bF, xiF)
L2F = z_average(eps_part(cut(
    lagrangian_GG(gF, Mg2) + lagrangian_GG(fF, Mf2)
    + interaction_lagrangian(gF, fF, dchi=dchiF)
    + chi_lagrangian(gF, dchi=dchiF)), 2))
L2sF, fF_, vF_ = symbolize(L2F, [Phi_gF, B_gF, Phi_fF, Psi_fF,
                                 B_fF, E_fF, dchiF], bg_rules)
if [str(f) for f in fF_] != NOMES_F:
    raise RuntimeError("ordem F mudou")
K7F, C7F, W7F = quadratic_matrices(L2sF, fF_, vF_)
Hdd_s, Hfdd_s, xidd_s, chiddd_s = sp.symbols(
    'Hddot H_fddot xiddot chidddot')
Cd7F = sp.zeros(7, 7)
for i in range(7):
    for j in range(7):
        Cd7F[i, j] = dt_background(
            C7F[i, j], {Hd_s: Hdd_s, Hfd_s: Hfdd_s, xid_s: xidd_s,
                        chidd_s: chiddd_s})
say("[montagem] K/C/W/CdS flat prontas")

LIVRES = (a_s, b_s, xi_s, H_s, Hf_s, Hd_s, Hfd_s, xid_s,
          chid_s, chidd_s, Ub, Up, Upp, ksym, Mf2, Meff2,
          Hdd_s, Hfdd_s, xidd_s, chiddd_s)
FIXOS = {Mg2: 1, m2: 1, rho_s: 0}
BETAS = (b0, b1, b2, b3, b4)


def fatias(M):
    Msub = M.subs(FIXOS)
    base_s = Msub.subs({Fb: 0, Fp: 0, Fpp: 0})
    out = {'base': sp.lambdify(LIVRES, base_s, modules='numpy')}
    for n, bn in enumerate(BETAS):
        bsub = {bm: (1 if mm == n else 0) for mm, bm in enumerate(BETAS)}
        Sl = Msub.subs({Fb: 1, Fp: 0, Fpp: 0}).subs(bsub) - base_s
        out[('Fb', n)] = sp.lambdify(LIVRES, Sl, modules='numpy')
    return out


FWN = fatias(W7N)
FWG = sp.lambdify(LIVRES, W3G.subs(FIXOS).subs(
    {Fb: 0, Fp: 0, Fpp: 0}), modules='numpy')
FKF, FCF, FWF, FCdF = (fatias(K7F), fatias(C7F), fatias(W7F),
                       fatias(Cd7F))
say("[fatias] prontas")


def monta(fat, args, bvals):
    M = np.array(fat['base'](*args), float).copy()
    for n in range(5):
        if bvals[n]:
            M += bvals[n] * np.array(fat[('Fb', n)](*args), float)
    return M


# ------------------------------------------------------------------
# B. familia de fundos (s, U0): cubico com continuacao
# ------------------------------------------------------------------
def raizes_r(rho_til_eff, seed):
    kap = 1.0 / MU_P
    rr = np.roots([kap * B4V - 3 * B2V, -3 * B1V,
                   3 * kap * B2V - B0V - rho_til_eff, kap * B1V])
    reais = [z.real for z in rr if abs(z.imag) < 1e-9 and z.real > 1e-12]
    if not reais:
        return None
    return min(reais, key=lambda x: abs(x - seed))


def fundo_s(a, s, U0, seed):
    """fundo da familia; continuacao pela seed. Retorna dict ou None."""
    meff2 = ME2
    rho_m = RHO0 * a**-3
    rte = (rho_m + U0) / (s * meff2)
    r = raizes_r(rte, seed)
    if r is None:
        return None
    kap = 1.0 / MU_P
    dW = kap * (2 * B4V * r - B1V / r**2) - 3 * B1V - 6 * B2V * r
    if abs(dW) < 1e-14:
        return None
    drdN = -3 * (rho_m / (s * meff2)) / dW
    d2W = kap * (2 * B4V + 2 * B1V / r**3) - 6 * B2V
    d2rdN2 = (9 * (rho_m / (s * meff2)) / dW
              + 3 * (rho_m / (s * meff2)) * d2W * drdN / dW**2)
    xi = r + drdN
    Vf = B4V + 3 * B2V / r**2 + B1V / r**3
    dVf = -6 * B2V / r**3 - 3 * B1V / r**4
    H2 = s * meff2 * r * r * Vf / (3.0 * MU_P)
    if H2 <= 0 or xi <= 0:
        return None
    H = np.sqrt(H2)
    dlnH_dN = 0.5 * (2 / r + dVf / Vf) * drdN
    Hd = H2 * dlnH_dN
    xid = H * (drdN + d2rdN2)
    Hfd = (Hd - H2 * drdN / r) / r
    rho_int = s * meff2 * (B0V + 3 * B1V * r + 3 * B2V * r**2)
    Ubv = 3 * H2 - rho_m - rho_int      # = U0 (consistencia)
    return dict(r=r, xi=xi, H=H, Hf=H / r, Hd=Hd, Hfd=Hfd, xid=xid,
                Ub=Ubv, rho=rho_m)


# alvo: H tardio do benchmark (rho=0, s=1, U0 implicito do toy)
_f_t = None
_seed = 0.3


def H_tardio(s, U0, seed):
    f = fundo_s(1e6, s, U0, seed)
    return (f['H'], f['r']) if f else (None, seed)


f_bench = None
for r_try in (0.3, 0.5):
    f_bench = fundo_s(1e6, 1.0, 0.0, r_try)
    if f_bench:
        break
H_STAR = f_bench['H']
say(f"[alvo] H_tardio do benchmark (s=1, U0=0) = {H_STAR:.6f}, "
    f"r_inf = {f_bench['r']:.4f}")


def resolve_U0(s, seed_r):
    """acha U0 com H_tardio(s,U0) = H_STAR.
    Retorna (U0, 'ok') ou (None, razao). Robusto a FOLD: a familia
    pode DEIXAR DE EXISTIR (raiz do cubico some) antes de H cair ate
    o alvo — nesse caso a razao e 'FOLD g=<valor na borda>'."""
    def g(U0):
        f = fundo_s(1e6, s, U0, seed_r)
        return (f['H'] - H_STAR) if f else np.nan

    grade = sorted(set(
        [0.0] + [sg * v for sg in (+1, -1)
                 for v in (0.25, 0.5, 1, 2, 4, 8, 16, 32, 64, 128)]))
    vals = [(U0, g(U0)) for U0 in grade]
    fin = [(U0, gv) for U0, gv in vals if np.isfinite(gv)]
    if not fin:
        return None, 'sem regiao valida'
    # zero exato na grade (o benchmark s=1, U0=0 e este caso)
    for u1, g1 in fin:
        if abs(g1) < 1e-9:
            return u1, 'ok'
    # sign change entre finitos consecutivos
    for (u1, g1), (u2, g2) in zip(fin[:-1], fin[1:]):
        if g1 * g2 < 0:
            try:
                return brentq(lambda u: g(u), u1, u2, xtol=1e-12), 'ok'
            except ValueError:
                pass
    # sem cruzamento na regiao amostrada: refinar as bordas de
    # existencia (fold) — a solucao pode estar COLADA na borda
    g_borda_pior = None
    for direcao in (-1, +1):
        # ponto finito extremo desse lado e vizinho NaN adjacente
        cand = [(U0, gv) for U0, gv in vals if np.isfinite(gv)]
        nans = [U0 for U0, gv in vals if not np.isfinite(gv)
                and (U0 < cand[0][0] if direcao < 0
                     else U0 > cand[-1][0])]
        if not nans:
            continue
        u_ok, g_ok = (cand[0] if direcao < 0 else cand[-1])
        u_bad = max(nans) if direcao < 0 else min(nans)
        for _ in range(80):
            mid = 0.5 * (u_ok + u_bad)
            if np.isfinite(g(mid)):
                u_ok = mid
            else:
                u_bad = mid
        g_edge = g(u_ok)
        if not np.isfinite(g_edge):
            continue
        if g_edge * g_ok < 0:
            try:
                u_star = brentq(lambda u: g(u),
                                min(u_ok, cand[0][0] if direcao < 0
                                    else cand[-1][0]),
                                max(u_ok, cand[0][0] if direcao < 0
                                    else cand[-1][0]), xtol=1e-12)
                return u_star, 'ok (colado no fold)'
            except ValueError:
                pass
        if g_borda_pior is None or abs(g_edge) < abs(g_borda_pior):
            g_borda_pior = g_edge
    if g_borda_pior is not None:
        return None, f'FOLD g_borda={g_borda_pior:+.4f}'
    g_min = min(gv for _, gv in fin)
    return None, f'sem cruzamento (g_min={g_min:+.4f})'


def acha_a0(s, U0, seed_r):
    """Omega_m(a0) = OMEGA_M0."""
    def om(a):
        f = fundo_s(a, s, U0, seed_r)
        if f is None:
            return np.nan
        return RHO0 * a**-3 / (3 * f['H']**2) - OMEGA_M0

    lo, hi = 0.05, 50.0
    if not (np.isfinite(om(lo)) and np.isfinite(om(hi))
            and om(lo) * om(hi) < 0):
        return None
    return brentq(om, lo, hi, xtol=1e-10)


def mT2_de(f, s):
    """formula do projeto (derivations/02, caixa), b3=0, F=1, m2=1."""
    r, xi = f['r'], f['xi']
    return (ME2 * (1.0 / 1.0 + xi / (MU_P * r**3)) * r
            * (s * B1V + s * B2V * (xi + r)))


# ------------------------------------------------------------------
# C. saude por membro (flat, canal-S, mini-trilhas)
# ------------------------------------------------------------------
def bg_ext_s(a, s, U0, seed, h=1e-5):
    f = fundo_s(a, s, U0, seed)
    if f is None:
        return None
    fp = fundo_s(a * np.exp(h), s, U0, f['r'])
    fm = fundo_s(a * np.exp(-h), s, U0, f['r'])
    if fp is None or fm is None:
        return None
    H = f['H']
    f['Hdd'] = H * (fp['Hd'] - fm['Hd']) / (2 * h)
    f['Hfdd'] = H * (fp['Hfd'] - fm['Hfd']) / (2 * h)
    f['xidd'] = H * (fp['xid'] - fm['xid']) / (2 * h)
    return f


def matriz_D(kc):
    return np.diag([1.0, 1.0 / kc, 1.0, 1.0, 1.0 / kc,
                    1.0 / kc**2, 1.0])


def e1_corr(Kt, Ct, Wt, Cdot):
    K = Kt.copy()
    C = Ct.copy()
    W = Wt.copy()
    n = 7
    esc = max(1.0, np.max(np.abs(K)))
    mset = set(MULT)
    for i in MULT:
        if np.max(np.abs(K[i, :])) > 1e-10 * esc:
            raise RuntimeError("K mult nao-nula")
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
    WXX = 0.5 * (W[np.ix_(MULT, MULT)] + W[np.ix_(MULT, MULT)].T)
    if np.linalg.cond(WXX) > 1e12:
        raise RuntimeError("W_XX mal condicionada")
    WXXi = np.linalg.inv(WXX)
    CdX = C[np.ix_(DYN, MULT)]
    K3 = K[np.ix_(DYN, DYN)] + CdX @ WXXi @ CdX.T
    C3 = C[np.ix_(DYN, DYN)] - CdX @ WXXi @ W[np.ix_(MULT, DYN)]
    W3 = W[np.ix_(DYN, DYN)] - W[np.ix_(DYN, MULT)] @ WXXi \
        @ W[np.ix_(MULT, DYN)]
    return K3, C3, W3


def e2_psi(K3, C3, W3, C3d):
    K = K3.copy()
    C = C3.copy()
    W = W3.copy()
    for j in range(3):
        cij = C3[0, j]
        cd = C3d[0, j]
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
    K2 = K[np.ix_(keep, keep)] + cx @ cx.T / W00
    return 0.5 * (K2 + K2.T), W00


def saude_ponto(s, U0, seed, a0, kh):
    f0 = fundo_s(a0, s, U0, seed)
    if f0 is None:
        return 'fundo-inv'
    kc = kh * a0 * f0['H']
    Ns = np.linspace(np.log(a0) - 0.025, np.log(a0) + 0.025, 41)
    Hs_arr = np.zeros(41)
    Ms = {x: np.zeros((41, 7, 7)) for x in ('K', 'C', 'W', 'CdS')}
    D = matriz_D(kc)
    sd = f0['r']
    for p, N in enumerate(Ns):
        a = np.exp(N)
        f = bg_ext_s(a, s, U0, sd)
        if f is None:
            return 'fundo-inv'
        sd = f['r']
        Hs_arr[p] = f['H']
        args = (a, f['r'] * a, f['xi'], f['H'], f['Hf'],
                f['Hd'], f['Hfd'], f['xid'], 0.0, 0.0,
                f['Ub'], 0.0, 0.3, kc, MU_P, ME2,
                f['Hdd'], f['Hfdd'], f['xidd'], 0.0)
        bvals = (s * B0V, s * B1V, s * B2V, 0.0, s * B4V)
        Ms['K'][p] = D @ monta(FKF, args, bvals) @ D
        Ms['C'][p] = D @ monta(FCF, args, bvals) @ D
        Ms['W'][p] = D @ monta(FWF, args, bvals) @ D
        Ms['CdS'][p] = D @ monta(FCdF, args, bvals) @ D
    K3s = np.zeros((41, 3, 3))
    C3s = np.zeros((41, 3, 3))
    W3s = np.zeros((41, 3, 3))
    g1 = 0.0
    try:
        for p in range(41):
            K3, C3, W3 = e1_corr(Ms['K'][p], Ms['C'][p], Ms['W'][p],
                                 Ms['CdS'][p])
            esc = np.max(np.abs(K3))
            g1 = max(g1, np.max(np.abs(K3[0, :])) / esc)
            K3[0, :] = 0.0
            K3[:, 0] = 0.0
            K3s[p], C3s[p], W3s[p] = K3, C3, W3
    except RuntimeError as e:
        return str(e)
    if g1 >= G1_TOL:
        return f'G1={g1:.0e}'
    C3d = np.gradient(C3s, Ns, axis=0) * Hs_arr[:, None, None]
    W00s = np.zeros(41)
    lam_min = np.inf
    for p in range(41):
        K2, W00s[p] = e2_psi(K3s[p], C3s[p], W3s[p], C3d[p])
        if 2 <= p <= 38:            # interior (bordas do gradiente)
            lam_min = min(lam_min, np.linalg.eigvalsh(K2)[0]
                          / np.max(np.abs(K2)))
    sinais = np.sign(W00s[2:-2])
    trocas = int(np.sum(sinais[1:] * sinais[:-1] < 0))
    # piso de ruido da mini-trilha: dN=1.25e-3 -> O(dN^2) ~ 1.6e-6
    # relativo em C3d/K2 (1a rodada: "violacao" de -9e-8 era isso)
    if lam_min <= -3e-6 or trocas > 0:
        return f'VIOLACAO lam={lam_min:.1e} trocas={trocas}'
    return 'ok'


# ------------------------------------------------------------------
# D. mu/Sigma (Newtoniano; correcao do Ub)
# ------------------------------------------------------------------
IDXN = {n: i for i, n in enumerate(NOMES_N)}
J7 = np.zeros(7)
J7[IDXN['Phi_g']] = 1.0
J3 = np.zeros(3)
J3[0] = 1.0


def matriz_DN(kc):
    D = np.ones(7)
    D[IDXN['B_f']] = 1.0 / kc
    D[IDXN['E_f']] = 1.0 / kc**2
    return np.diag(D)


def mu_sigma(s, U0, seed, a, kh):
    f = fundo_s(a, s, U0, seed)
    if f is None:
        return None
    kc = kh * a * f['H']
    args = (a, f['r'] * a, f['xi'], f['H'], f['Hf'],
            f['Hd'], f['Hfd'], f['xid'], 0.0, 0.0,
            f['Ub'], 0.0, 0.3, kc, MU_P, ME2,
            0.0, 0.0, 0.0, 0.0)
    bvals = (s * B0V, s * B1V, s * B2V, 0.0, s * B4V)
    Wbi = monta(FWN, args, bvals)
    D = matriz_DN(kc)
    Wt = D @ (0.5 * (Wbi + Wbi.T)) @ D
    if np.linalg.cond(Wt) > 1e10:
        return dict(singular=True)
    q = D @ np.linalg.solve(Wt, D @ J7)
    Ub_gr = 3.0 * f['H']**2 - f['rho']
    args_gr = (a, f['r'] * a, f['xi'], f['H'], f['Hf'],
               f['Hd'], f['Hfd'], f['xid'], 0.0, 0.0,
               Ub_gr, 0.0, 0.3, kc, MU_P, ME2,
               0.0, 0.0, 0.0, 0.0)
    Wgr = np.array(FWG(*args_gr), float)
    qg = np.linalg.solve(0.5 * (Wgr + Wgr.T), J3)
    return dict(singular=False,
                mu=q[IDXN['Phi_g']] / qg[0],
                Sig=(q[IDXN['Phi_g']] + q[IDXN['Psi_g']])
                / (qg[0] + qg[1]))


# ------------------------------------------------------------------
# E. o scan em s e o confronto
# ------------------------------------------------------------------
say("")
say("scan da familia (s -> m_T/H0):")
say(f"  {'s':>7} {'U0':>10} {'a0':>7} {'H0':>7} {'r(a0)':>7} "
    f"{'mT/H0':>7} {'saude':>8} | max|mu-1|, max|Sig-1| na janela")
membros = []
folds = []
r_seed = f_bench['r']
for s in S_GRID:
    U0, razao = resolve_U0(s, r_seed)
    if U0 is None:
        say(f"  {s:7.2f} {'—':>10}  ({razao})")
        folds.append((s, razao))
        continue
    a0 = acha_a0(s, U0, r_seed)
    if a0 is None:
        say(f"  {s:7.2f} {U0:10.3f}  (sem a0 com Omega_m=0.3)")
        continue
    f0 = fundo_s(a0, s, U0, r_seed)
    r_seed = fundo_s(1e6, s, U0, r_seed)['r']
    H0 = f0['H']
    mT = np.sqrt(max(mT2_de(f0, s), 0.0))
    # saude: 3 epocas x kh {2, 30}
    saude = 'ok'
    for a_chk in (0.3 * a0, a0, 100 * a0):
        for kh_chk in (2.0, 30.0):
            rr = saude_ponto(s, U0, f0['r'], a_chk, kh_chk)
            if rr != 'ok':
                saude = rr
                break
        if saude != 'ok':
            break
    # janela observacional
    dev_mu = 0.0
    dev_sg = 0.0
    pontos = []
    for z in Z_GRID:
        a = a0 / (1.0 + z)
        fz = fundo_s(a, s, U0, f0['r'])
        for k_h in K_HMPC:
            kh = 3000.0 * k_h * (a0 * H0) / (a * fz['H'])
            r = mu_sigma(s, U0, f0['r'], a, kh)
            if r is None or r.get('singular'):
                pontos.append((z, k_h, np.nan, np.nan))
                continue
            dev_mu = max(dev_mu, abs(r['mu'] - 1.0))
            dev_sg = max(dev_sg, abs(r['Sig'] - 1.0))
            pontos.append((z, k_h, r['mu'], r['Sig']))
    say(f"  {s:7.2f} {U0:10.3f} {a0:7.3f} {H0:7.4f} {f0['r']:7.4f} "
        f"{mT/H0:7.2f} {saude:>8} | {dev_mu:8.5f}  {dev_sg:8.5f}")
    membros.append(dict(s=s, U0=U0, a0=a0, H0=H0, mT_H0=mT / H0,
                        saude=saude, dev_mu=dev_mu, dev_sg=dev_sg,
                        pontos=pontos))

# V-CONSIST: s=1 vs R-8a (era Lambda: a=30*a0-ish ~ toy a>=3)
say("")
m1 = next((m for m in membros if m['s'] == 1.0), None)
if m1:
    r_c = mu_sigma(1.0, m1['U0'], 0.4, 30.0 * m1['a0'], 30.0)
    say(f"  V-CONSIST (s=1, era Lambda, kh=30): mu = {r_c['mu']:.6f} "
        f"(R-8a: 1.0000 na era Lambda, |d| < 2e-3 "
        f"{'OK' if abs(r_c['mu'] - 1.0) < 2e-3 else 'FALHOU'})")

# o limite
say("")
say("=" * 72)
say("VEREDITO R-8b (criterios pre-declarados no cabecalho)")
say("=" * 72)
sa = [m for m in membros if m['saude'] == 'ok']
doentes = [m for m in membros if m['saude'] != 'ok']
if doentes:
    say(f"  membros EXCLUIDOS por saude: "
        f"{[(m['s'], m['saude']) for m in doentes]}")
say(f"  tabela mu/Sigma por membro (janela z<=1, k=0.05-0.15 h/Mpc):"
    f" acima")


def limite_para(lim_mu, lim_sg):
    xs = [np.log(m['mT_H0']) for m in sa]
    ds = [max(m['dev_mu'] / lim_mu, m['dev_sg'] / lim_sg) for m in sa]
    if not xs:
        return float('nan')
    if max(ds) <= 1.0:
        return float('inf')
    if ds[0] > 1.0:
        return 0.0
    for i in range(1, len(xs)):
        if ds[i - 1] <= 1.0 < ds[i]:
            lx = xs[i - 1] + (xs[i] - xs[i - 1]) \
                * (np.log(1.0) - np.log(ds[i - 1])) \
                / (np.log(ds[i]) - np.log(ds[i - 1]))
            return float(np.exp(lx))
    return float(np.exp(xs[-1]))


m_star = limite_para(LIMITES['mu'], LIMITES['Sig'])
m_max = max((m['mT_H0'] for m in sa), default=float('nan'))
say("")
say(f"  ALCANCE DA FAMILIA (fold do fundo): m_T/H0 max ~ {m_max:.2f}")
if folds:
    say(f"  s sem solucao (alem do fold): "
        f"{[(sv, rz) for sv, rz in folds]}")
say(f"  LIMITE observacional (|mu-1|<={LIMITES['mu']:g}, |Sigma-1|<="
    f"{LIMITES['Sig']:g}): m_T/H0 <= "
    f"{'nao atingido no alcance' if np.isinf(m_star) else f'{m_star:.1f}'}")
for lim in LIM_SENS:
    mL = limite_para(lim, lim)
    say(f"  sensibilidade (limites {lim:g}/{lim:g}): "
        f"{'nao atingido' if np.isinf(mL) else f'{mL:.1f}'}")
say("")
if np.isfinite(m_max) and m_max < 30.0 and np.isinf(m_star):
    say("  >>> POSTULADO 30-300 H0 INALCANCAVEL NA FAMILIA (obstrucao")
    say("  ESTRUTURAL, nao observacional): mantendo a historia de")
    say(f"  expansao, o fundo DOBRA (fold) em m_T/H0 ~ {m_max:.1f} —")
    say("  r^2 V_f(r) tem minimo positivo (~0.3 em r=1) na forma-beta")
    say("  do benchmark, o que trava s <= 3 mu H*^2/(0.3 meff^2) ~ 6.")
    say("  Dentro do alcance, o crescimento e trivialmente satisfeito")
    say("  (desvios subpercentuais — tabela). Consequencias:")
    say("  (i) o postulado 30-300 H0 do corpus exige OUTRA forma-beta")
    say("  (V_f com zero em r finito) — nao e um dial continuo do")
    say("  benchmark; e uma ESCOLHA ESTRUTURAL a declarar na v2;")
    say("  (ii) na familia do benchmark, m_T ~ (2-6) H0: a fisica")
    say("  bimetrica vive no quase-horizonte -> R-8 completo e o")
    say("  teste decisivo (como ja apontava o R-8a).")
elif np.isinf(m_star):
    say("  >>> a janela adotada nao limita a familia no alcance;")
    say("  postulado nao testado por crescimento aqui.")
elif m_star < 30.0:
    say(f"  >>> POSTULADO EXCLUIDO pela janela adotada (m* = "
        f"{m_star:.1f} < 30).")
else:
    say(f"  >>> limite observacional m* = {m_star:.0f}; confronto com")
    say("  o postulado conforme a faixa (ver numeros).")
say("")
say("  NOTA ESTRUTURAL: membros com m >> H0 exigem U0 negativo grande")
say("  (vacuo-chi cancelando a energia da interacao) — o postulado")
say("  30-300 H0 do corpus IMPLICA esse ajuste fino; registrado como")
say("  insumo do cap. de fundamentos da v2.")
say("  LIMITES ADOTADOS sao referencias de ordem de grandeza da")
say("  literatura MG (declarado); confronto fino = nivel paper.")

os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
with open(os.path.join(HERE, 'out', 'r8b_limite_mH0.txt'), 'w',
          encoding='utf-8') as fh:
    fh.write("\n".join(OUT) + "\n")
say("")
say("saida escrita em auditoria/code/out/r8b_limite_mH0.txt")
