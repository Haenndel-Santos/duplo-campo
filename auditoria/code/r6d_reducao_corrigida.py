# -*- coding: utf-8 -*-
"""
r6d_reducao_corrigida.py — O BUG DA ABSORCAO: dobra de Cdot em W_XX.
Correcao da reducao numerica e efeito no espectro de K_red.

DIAGNOSTICO (r6c, 2026-08-12): as duas L2 (nossa Gamma-Gamma e ADM da
reauditoria externa) sao a MESMA acao (T1/T2/T3 exatos, off-shell).
Com a MESMA rotina de reducao, nossas matrizes dao det<0 no bloco
(Psi_f,E_f) e as deles dao det=0. Logo o erro esta na reducao aplicada
a matrizes com C[mult,:] != 0 — que e o caso da nossa L2 e nao da
deles.

O BUG (leitura do codigo): reduz_ponto (presente em d2_evolucao_
reduzida, gatef_a, gatef_b, r1, r2, r3*, r4*, r5) traduz o
matrix_ipp_row simbolico da lib para numerico, mas com dois desvios:
  (i)  usa Cdot PRE-COMPUTADO da C ORIGINAL (stale) em vez do Cdot da
       C corrente;
  (ii) nao pula a entrada quando a C corrente ja foi zerada pela
       antissimetrizacao do multiplicador anterior.
Com C_XX simetrica (verificado: T2 do r6c), o par (i)+(ii) faz cada
entrada OFF-DIAGONAL de W_XX receber Cdot DUAS vezes (uma por linha do
par) — o correto, pela derivada total d/dt(q S q) com S = -C_X
simetrica, e UMA vez. A lib simbolica (matrix_ipp_row) esta correta:
ela recalcula cdot da C corrente e pula cij==0; schur_eliminate exige
C[X,:]=0 e nem roda. O V1 (GR) nunca pegou o bug porque no setor g
C_XX tem estrutura que zera o efeito — medido aqui (D5).

CORRECAO (one-shot, S simetrica):
  C' = C + S,  S[i,:] = -C[i,:] (i in MULT), completada simetrica
       (bem-definida porque C_XX e simetrica);
  W' = W - Sdot,  Sdot[i,j] = -Cdot0[i,j], simetrica, contada UMA vez
       por par nao-ordenado;
  Schur usual em W'_XX.

MEDIDAS (pre-declaradas):
  D1 — simetria de C_XX na trilha: max|C_XX - C_XX^T|/max|C_XX|.
  D2 — tamanho do bug: max|W_XX_old - W_XX_novo|/escala(W_XX).
  D3 — espectro de K_red velho vs corrigido nos marcos (float64):
       lam0, lam1, lam2, det do bloco (Psi_f,E_f)/esc^2, e
       |v0.Psi_f|^2 da direcao quase-nula.
  D4 — precisao estendida (mpmath dps=40) em 3 epocas: lam0/lam1
       corrigido — colapsa para ~0 (nivel de arredondamento) ou fica?
  D5 — controle GR: bloco C_XX do setor g (Phi_g,B_g) — o bug era
       invisivel ao V1?

CRITERIOS (pre-declarados):
  det_corrigido/esc^2 <= 1e-25 (dps=40) nos marcos, com direcao nula
      ~ Psi_f -> BUG CONFIRMADO: o 3o DOF do Gate F e artefato da
      dobra de Cdot; a contagem fisica e 2 DOFs escalares e a cadeia
      Gate F-b (fantasma canonico, omega_0/H ~ 7-12, H-SC) cai.
      Consequencia em cascata: toda conclusao a jusante da reducao
      numerica (D2 dinamica reduzida, R-2, F-a/F-b, R-4b metrico,
      R-5 ISW) precisa de reexecucao com a reducao corrigida.
  det_corrigido/esc^2 >= 1e-6 estavel em dps -> a correcao nao explica
      o desacordo; reabrir a analise (nao esperado dado r6c).

Requer sympy, numpy, mpmath. ~2-4 min.
Uso (raiz do repo, venv ativo):
    python auditoria/code/r6d_reducao_corrigida.py
Saida em auditoria/code/out/r6d_reducao_corrigida.txt
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
sys.path.insert(0, DCODE)

spec = importlib.util.spec_from_file_location(
    "d1mod", os.path.join(DCODE, "01_setor_escalar_K_Omega.py"))
d1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(d1)

from tdcp_pert_lib import (t, a_s, b_s, xi_s, H_s, Hf_s, Hd_s, Hfd_s, xid_s,
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
A_MIN, A_MAX = 100.0, 80000.0
NPTS = 3000
MARCAS = list(np.geomspace(150.0, 75000.0, 12))
EPOCAS_HP = [150.0, 3635.0, 74992.0]

MU = 1.0
ME2 = 0.5
B0V, B2V, B4V = 1.0, -0.4, 0.5
RHO0 = 0.3

say("=" * 72)
say("R-6d — O BUG DA ABSORCAO (dobra de Cdot em W_XX) E A REDUCAO")
say("CORRIGIDA")
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

LIVRES = (a_s, b_s, xi_s, H_s, Hf_s, Hd_s, Hfd_s, xid_s,
          chid_s, chidd_s, Ub, Up, Upp, ksym, Mf2, Meff2)
FIXOS = {Mg2: 1, m2: 1, rho_s: 0}
BETAS = (b0, b1, b2, b3, b4)


def fatias(M):
    Msub = M.subs(FIXOS)
    base_s = Msub.subs({Fb: 0, Fp: 0, Fpp: 0})
    out = {'base': sp.lambdify(LIVRES, base_s, modules='numpy')}
    for tag, fsub in (('Fb', {Fb: 1, Fp: 0, Fpp: 0}),):
        for n, bn in enumerate(BETAS):
            bsub = {bm: (1 if mm == n else 0) for mm, bm in enumerate(BETAS)}
            Sl = Msub.subs(fsub).subs(bsub) - base_s
            out[(tag, n)] = sp.lambdify(LIVRES, Sl, modules='numpy')
    return out


FK, FC, FW = fatias(K7), fatias(C7), fatias(W7)
say("[fatias] prontas")


def monta(fat, args, bvals):
    M = np.array(fat['base'](*args), float).copy()
    for n in range(5):
        if bvals[n]:
            M += bvals[n] * np.array(fat[('Fb', n)](*args), float)
    return M


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


def build_track(B1V, npts):
    Ns = np.linspace(np.log(A_MIN), np.log(A_MAX), npts)
    Hs_arr = np.zeros(npts)
    Ms = {x: np.zeros((npts, 7, 7)) for x in 'KCW'}
    f0 = fundo_bconst(A_MIN, B1V)
    kc = 45.0 * f0['H'] * A_MIN
    for p, N in enumerate(Ns):
        a = np.exp(N)
        f = fundo_bconst(a, B1V)
        Hs_arr[p] = f['H']
        args = (a, f['r'] * a, f['xi'], f['H'], f['Hf'],
                f['Hd'], f['Hfd'], f['xid'], 0.0, 0.0,
                f['Ub'], 0.0, 0.3, kc, 1.0, ME2)
        bvals = (B0V, B1V, B2V, 0.0, B4V)
        for x, F in (('K', FK), ('C', FC), ('W', FW)):
            Ms[x][p] = monta(F, args, bvals)
    return Ns, Hs_arr, Ms, kc


def reduz_ponto_old(Kt, Ct, Wt, Cdot):
    """verbatim do gatef_b (o codigo em producao)."""
    K = Kt.copy()
    C = Ct.copy()
    W = Wt.copy()
    n = K.shape[0]
    for i in MULT:
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
    WXX = W[np.ix_(MULT, MULT)]
    WXXi = np.linalg.inv(WXX)
    return (K[np.ix_(DYN, DYN)] + C[np.ix_(DYN, MULT)] @ WXXi
            @ C[np.ix_(DYN, MULT)].T, W)


def reduz_ponto_novo(Kt, Ct, Wt, Cdot):
    """one-shot: S = -C_X simetrica; W' = W - Sdot com Sdot contada
    uma vez por par nao-ordenado."""
    K = Kt.copy()
    C = Ct.copy()
    W = Wt.copy()
    n = K.shape[0]
    mset = set(MULT)
    for i in MULT:
        for j in range(n):
            cd = Cdot[i, j]
            cij = Ct[i, j]
            if i == j:
                W[i, i] += cd
            elif j in mset:
                W[i, j] += cd            # par X-X: uma vez so
            else:
                W[i, j] += cd
                W[j, i] += cd
                C[j, i] -= cij
        C[i, :] = 0.0
    WXX = W[np.ix_(MULT, MULT)]
    WXX = 0.5 * (WXX + WXX.T)
    WXXi = np.linalg.inv(WXX)
    return (K[np.ix_(DYN, DYN)] + C[np.ix_(DYN, MULT)] @ WXXi
            @ C[np.ix_(DYN, MULT)].T, W)


def analisa(B1V):
    say("")
    say("=" * 72)
    say(f"FUNDO beta-constante beta1={B1V:g}")
    say("=" * 72)
    Ns, Hs_arr, Ms, kc = build_track(B1V, NPTS)
    aas = np.exp(Ns)
    Cdots = np.gradient(Ms['C'], Ns, axis=0) * Hs_arr[:, None, None]
    mark_idx = sorted(set(int(np.argmin(np.abs(aas - am))) for am in MARCAS))

    # D1 — simetria de C_XX
    asym = 0.0
    for p in range(NPTS):
        CXX = Ms['C'][p][np.ix_(MULT, MULT)]
        esc = max(np.max(np.abs(CXX)), 1e-300)
        asym = max(asym, np.max(np.abs(CXX - CXX.T)) / esc)
    say(f"    D1 — max|C_XX - C_XX^T|/max|C_XX| na trilha = {asym:.2e}")

    # D5 — bloco g (Phi_g,B_g)
    CG = Ms['C'][NPTS // 2][np.ix_([0, 1], [0, 1])]
    CdG = Cdots[NPTS // 2][np.ix_([0, 1], [0, 1])]
    say(f"    D5 — setor g: C[Phi_g,B_g]={CG[0,1]:.3e}, "
        f"C[B_g,Phi_g]={CG[1,0]:.3e}, Cdot off-diag={CdG[0,1]:.3e}")

    # D2/D3 — velho vs corrigido nos marcos
    say("")
    say("    D3 — espectro de K_red: VELHO vs CORRIGIDO")
    say(f"    {'a':>8} {'kh':>7} | {'lam0_old':>11} {'det2/esc2_old':>13} |"
        f" {'lam0_new':>11} {'det2/esc2_new':>13} {'|v0.Psi_f|^2':>12}")
    dW_rel_max = 0.0
    dets_new = []
    for mi in mark_idx:
        Kro, Wfull_o = reduz_ponto_old(Ms['K'][mi], Ms['C'][mi],
                                       Ms['W'][mi], Cdots[mi])
        Krn, Wfull_n = reduz_ponto_novo(Ms['K'][mi], Ms['C'][mi],
                                        Ms['W'][mi], Cdots[mi])
        WXo = Wfull_o[np.ix_(MULT, MULT)]
        WXn = Wfull_n[np.ix_(MULT, MULT)]
        dW_rel_max = max(dW_rel_max,
                         np.max(np.abs(WXo - WXn)) / np.max(np.abs(WXn)))
        lo = np.linalg.eigvalsh(0.5 * (Kro + Kro.T))
        Ksn = 0.5 * (Krn + Krn.T)
        ln, En = np.linalg.eigh(Ksn)
        i0 = int(np.argmin(np.abs(ln)))
        v0 = En[:, i0]
        fr = float(v0[0]**2 / (v0 @ v0))
        K2o = 0.5 * (Kro + Kro.T)[np.ix_([0, 1], [0, 1])]
        K2n = Ksn[np.ix_([0, 1], [0, 1])]
        d2o = np.linalg.det(K2o) / max(np.max(np.abs(K2o))**2, 1e-300)
        d2n = np.linalg.det(K2n) / max(np.max(np.abs(K2n))**2, 1e-300)
        dets_new.append(abs(d2n))
        kh = kc / (aas[mi] * Hs_arr[mi])
        say(f"    {aas[mi]:8.0f} {kh:7.2f} | {lo[0]:+11.3e} {d2o:+13.2e} |"
            f" {ln[i0]:+11.3e} {d2n:+13.2e} {fr:12.4f}")
    say(f"    D2 — max|W_XX_old - W_XX_novo|/esc = {dW_rel_max:.3e}")
    return dict(asym=asym, dW=dW_rel_max, dets_new=dets_new)


# ------------------------------------------------------------------
# D4 — precisao estendida da reducao corrigida (mpmath)
# ------------------------------------------------------------------
def compila_mp(B1V):
    sub = {Mg2: 1, m2: 1, rho_s: 0, Fb: 1, Fp: 0, Fpp: 0,
           b0: 1, b1: B1V, b2: sp.Rational(-2, 5), b3: 0,
           b4: sp.Rational(1, 2)}
    fs = []
    for M in (K7, C7, W7):
        Ms = sp.nsimplify(M.subs(sub))
        fs.append(sp.lambdify(LIVRES, Ms, modules='mpmath'))
    return fs


def fundo_mp(a, B1V):
    a = mp.mpf(a)
    kap = mp.mpf(1)
    meff2 = mp.mpf(1) / 2
    rho = mp.mpf('0.3') * a**-3
    rho_til = rho / meff2
    B1 = mp.mpf(str(B1V))
    B0n, B2n, B4n = mp.mpf(1), mp.mpf('-0.4'), mp.mpf('0.5')
    coef = [kap * B4n - 3 * B2n, -3 * B1,
            3 * kap * B2n - B0n - rho_til, kap * B1]
    rr = mp.polyroots(coef, maxsteps=200, extraprec=200)
    reais = sorted(z.real for z in rr
                   if abs(mp.im(z)) < mp.mpf('1e-20') and mp.re(z) > 0)
    r = reais[0]
    dW = kap * (2 * B4n * r - B1 / r**2) - 3 * B1 - 6 * B2n * r
    drdN = -3 * rho_til / dW
    d2W = kap * (2 * B4n + 2 * B1 / r**3) - 6 * B2n
    d2rdN2 = 9 * rho_til / dW + 3 * rho_til * d2W * drdN / dW**2
    xi = r + drdN
    Vf = B4n + 3 * B2n / r**2 + B1 / r**3
    dVf = -6 * B2n / r**3 - 3 * B1 / r**4
    H2 = meff2 * r * r * Vf / 3
    H = mp.sqrt(H2)
    dlnH_dN = mp.mpf(1) / 2 * (2 / r + dVf / Vf) * drdN
    Hd = H2 * dlnH_dN
    xid = H * (drdN + d2rdN2)
    Hfd = (Hd - H2 * drdN / r) / r
    rho_int = meff2 * (B0n + 3 * B1 * r + 3 * B2n * r**2)
    return dict(r=r, xi=xi, H=H, Hf=H / r, Hd=Hd, Hfd=Hfd, xid=xid,
                Ub=3 * H2 - rho_int)


def args_mp(N, B1V, kc):
    a = mp.exp(N)
    f = fundo_mp(a, B1V)
    return (a, f['r'] * a, f['xi'], f['H'], f['Hf'], f['Hd'], f['Hfd'],
            f['xid'], mp.mpf(0), mp.mpf(0), f['Ub'], mp.mpf(0),
            mp.mpf('0.3'), kc, mp.mpf(1), mp.mpf(1) / 2), f['H']


def reduz_novo_mp(K, C0, W, Cdot):
    n = 7
    C = C0.copy()
    W = W.copy()
    mset = set(MULT)
    for i in MULT:
        for j in range(n):
            cd = Cdot[i, j]
            cij = C0[i, j]
            if i == j:
                W[i, i] += cd
            elif j in mset:
                W[i, j] += cd
            else:
                W[i, j] += cd
                W[j, i] += cd
                C[j, i] -= cij
        for j in range(n):
            C[i, j] = mp.mpf(0)
    WXX = mp.matrix(4, 4)
    for ii, i in enumerate(MULT):
        for jj, j in enumerate(MULT):
            WXX[ii, jj] = (W[i, j] + W[j, i]) / 2
    WXXi = WXX**-1
    CdX = mp.matrix(3, 4)
    for ii, i in enumerate(DYN):
        for jj, j in enumerate(MULT):
            CdX[ii, jj] = C[i, j]
    Kdd = mp.matrix(3, 3)
    for ii, i in enumerate(DYN):
        for jj, j in enumerate(DYN):
            Kdd[ii, jj] = K[i, j]
    return Kdd + CdX * WXXi * CdX.T


def d4(B1V):
    say("")
    say(f"    D4 — reducao CORRIGIDA em mpmath dps=40 (beta1={B1V}):")
    mp.mp.dps = 40
    fK, fC, fW = compila_mp(sp.Rational(str(B1V)))
    kc = 45 * fundo_mp(A_MIN, B1V)['H'] * A_MIN
    h = mp.mpf('1e-6')
    for aval in EPOCAS_HP:
        N = mp.log(mp.mpf(aval))
        ar, H = args_mp(N, B1V, kc)
        K = mp.matrix(fK(*ar))
        C = mp.matrix(fC(*ar))
        W = mp.matrix(fW(*ar))
        ap, _ = args_mp(N + h, B1V, kc)
        am, _ = args_mp(N - h, B1V, kc)
        Cd = (mp.matrix(fC(*ap)) - mp.matrix(fC(*am))) / (2 * h) * H
        Kr = reduz_novo_mp(K, C, W, Cd)
        Ks = (Kr + Kr.T) / 2
        lam = mp.eigsy(Ks, eigvals_only=True)
        lam = sorted([lam[i] for i in range(3)], key=abs)
        K2 = mp.matrix(2, 2)
        for ii, i in enumerate((0, 1)):
            for jj, j in enumerate((0, 1)):
                K2[ii, jj] = Ks[i, j]
        det2 = mp.det(K2)
        esc = max(abs(K2[i, j]) for i in range(2) for j in range(2))
        say(f"      a={aval:8g}: lam(ord |.|) = {mp.nstr(lam[0],6)}, "
            f"{mp.nstr(lam[1],6)}, {mp.nstr(lam[2],6)}; "
            f"det2/esc^2 = {mp.nstr(det2/esc**2, 6)}")


res = {}
for B1V in (1.0, 4.47):
    res[B1V] = analisa(B1V)
    d4(B1V)

say("")
say("=" * 72)
say("VEREDITO R-6d (criterios pre-declarados no cabecalho)")
say("=" * 72)
for B1V in (1.0, 4.47):
    r = res[B1V]
    say(f"  beta1={B1V:g}: C_XX simetrica ({r['asym']:.1e}); "
        f"bug W_XX rel = {r['dW']:.2e}; "
        f"max|det2|/esc^2 corrigido (float64) = {max(r['dets_new']):.2e}")
say("")
say("  Ver D4 (dps=40) acima para o veredito final do det corrigido.")

os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
with open(os.path.join(HERE, 'out', 'r6d_reducao_corrigida.txt'), 'w',
          encoding='utf-8') as fh:
    fh.write("\n".join(OUT) + "\n")
say("")
say("saida escrita em auditoria/code/out/r6d_reducao_corrigida.txt")
