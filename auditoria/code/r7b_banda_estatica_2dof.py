# -*- coding: utf-8 -*-
"""
r7b_banda_estatica_2dof.py — R-7b: REEXECUCAO DA CASCATA (2/4). A
BANDA estatica e a reconstrucao de Phi_g no sistema 2-DOF corrigido.

CONTEXTO: erratum_02_reducao_numerica.md; maquinaria validada no
R-7a (gates G1/G2/G3, ancoras M2/M3). O R-4b antigo mediu
lnA_passagem (kh=20 -> 0.2) = +3.97 (beta1=1) e +3.62 (beta1=4.47)
no sistema espurio de 3 DOFs, e o R-5 usou a reconstrucao de Phi_g
(com o W_XX ERRADO do bug) para prever excesso ISW 2-8x em baixo-ell.
A reauditoria externa (corrigida) da DECAIMENTO (-6.9..-8.3 em
ln|Phi_g|; ICs metricas fisicas ~ -8). Este script refaz as duas
medidas no nosso pipeline corrigido.

PROTOCOLO (R-4b verbatim onde aplicavel):
  - fundos estaticos beta1=1 e 4.47; a=[100,80000], NPTS=24000;
    kh inicial 45 (k_c = 45 H(100) 100).
  - reducao corrigida E1+E2 (R-7a) -> (Etil = k^2 E_f, dchi);
    equilibracao D = diag(1,1/k,1,1,1/k,1/k^2,1).
  - 4 ICs fundamentais (Etil pos/vel, dchi pos/vel).
  - JANELAS em kh (12 faixas de 40 a 0.1) construidas por kh(a) =
    k_c/(a H(a)) monotono; taxa met por janela = Delta ln A_met /
    Delta t / H_mid, com A_met = envelope da componente Etil
    (unico escalar metrico fisico; no R-4b 'met' era o par
    (Psi_f, E_f) — Psi_f e vinculo, fora do espaco fisico).
  - lnA_PASSAGEM por IC: Delta ln A_met entre kh=20 e kh=0.2;
    reporta-se por IC e o maximo.
  - RECONSTRUCAO Phi_g (o elo do R-5): nos pontos da trilha,
    Psi_f* = (cx^T qdot2 - W3'[0,keep] q2)/W00;  q3 = (Psi_f*, q2);
    X* = W_XX^{-1}(C_dX^T q3dot - W_Xd q3);  Phi_g = X*[0]
    (blocos pos-absorcao CORRETOS; Psi_fdot* por gradiente na
    trajetoria salva). Medidas: Delta ln|Phi_g| na passagem e
    mediana |Phi_g| / A_met (comparar R-5A: 0.160 "sustentada";
    externa: Phi_g decai).

CONTROLES (pre-declarados):
  R7b-NULL (espectador GR-equivalente): a componente dchi e, com
      ancoras provadas no R-7a, um escalar canonico com friccao 3H e
      massa k^2/a^2+0.3 — sua passagem e o NULL interno:
      lnA_passagem(dchi) <= +0.5 (esperado negativo ~ GR -4.3).
  R7b-AUTOSIM: em beta1=1, k vs 3k. NOTA: o criterio antigo
      (|dif| < 0.5) pressupunha regime de crescimento dominado por um
      ramo (mix-insensivel). Em regime DECADENTE o lnA de passagem
      depende do estado de entrada em kh=20 (mix dos dois ramos
      overdamped, que evoluiu desde kh inicial diferente: 45 vs 135)
      e nao e invariante de k. O invariante que a autosimilaridade
      preve e o SINAL e a ordem: criterio v2 = ambos lnA_met < -4
      (decaimento forte consistente). A diferenca numerica e
      reportada.

CRITERIOS (pre-declarados):
  lnA_met_max >= +3.5  -> BANDA-VIVA (reproduz o antigo; contradiria
      r6d — investigar antes de qualquer uso).
  lnA_met_max <= 0     -> BANDA-MORTA: a amplificacao do R-4 era
      artefato do 3o DOF espurio; R-4b substituido.
  0 < lnA_met_max < 3.5 -> BANDA-REDUZIDA: quantificar e discutir.
  Phi_g: se Delta ln|Phi_g| < 0 na passagem (decaimento), o elo
      "banda -> Phi_g -> ISW" do R-5 cai tambem no nosso pipeline
      (insumo do R-7d).

Requer sympy, numpy. ~6-10 min (3 trilhas de 24000).
Uso (raiz do repo, venv ativo):
    python auditoria/code/r7b_banda_estatica_2dof.py
Saida em auditoria/code/out/r7b_banda_estatica_2dof.txt
"""
import importlib.util
import os
import sys
import time

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
A_MIN, A_MAX = 100.0, 80000.0
NPTS = 24000
G1_TOL = {'G': 1e-4, 'S': 1e-10}

JANELAS_KH = [(40, 20), (20, 10), (10, 6), (6, 4), (4, 2.5), (2.5, 1.6),
              (1.6, 1), (1, 0.7), (0.7, 0.45), (0.45, 0.3), (0.3, 0.2),
              (0.2, 0.1)]
PASSAGEM = (20.0, 0.2)
REF_ANTIGO = {1.0: 3.97, 4.47: 3.62}

MU = 1.0
ME2 = 0.5
B0V, B2V, B4V = 1.0, -0.4, 0.5
RHO0 = 0.3

say("=" * 72)
say("R-7b — A BANDA ESTATICA E Phi_g NO SISTEMA 2-DOF CORRIGIDO")
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


def fundo_ext(a, B1V, h=1e-5):
    f = fundo_bconst(a, B1V)
    fp = fundo_bconst(a * np.exp(h), B1V)
    fm = fundo_bconst(a * np.exp(-h), B1V)
    H = f['H']
    f['Hdd'] = H * (fp['Hd'] - fm['Hd']) / (2 * h)
    f['Hfdd'] = H * (fp['Hfd'] - fm['Hfd']) / (2 * h)
    f['xidd'] = H * (fp['xid'] - fm['xid']) / (2 * h)
    return f


def matriz_D(kc):
    return np.diag([1.0, 1.0 / kc, 1.0, 1.0, 1.0 / kc, 1.0 / kc**2, 1.0])


def build_track(B1V, npts, kc):
    Ns = np.linspace(np.log(A_MIN), np.log(A_MAX), npts)
    Hs_arr = np.zeros(npts)
    Ms = {x: np.zeros((npts, 7, 7)) for x in ('K', 'C', 'W', 'CdS')}
    D = matriz_D(kc)
    for p, N in enumerate(Ns):
        a = np.exp(N)
        f = fundo_ext(a, B1V)
        Hs_arr[p] = f['H']
        args = (a, f['r'] * a, f['xi'], f['H'], f['Hf'],
                f['Hd'], f['Hfd'], f['xid'], 0.0, 0.0,
                f['Ub'], 0.0, 0.3, kc, 1.0, ME2,
                f['Hdd'], f['Hfdd'], f['xidd'], 0.0)
        bvals = (B0V, B1V, B2V, 0.0, B4V)
        z5 = (0.0,) * 5
        Ms['K'][p] = D @ monta(FK, args, bvals, z5, z5) @ D
        Ms['C'][p] = D @ monta(FC, args, bvals, z5, z5) @ D
        Ms['W'][p] = D @ monta(FW, args, bvals, z5, z5) @ D
        Ms['CdS'][p] = D @ monta(FCd, args, bvals, z5, z5) @ D
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
    """reducao E1+E2 + blocos para reconstrucao de Phi_g."""
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
    if g1_max >= G1_TOL[canal]:
        raise RuntimeError(f"G1 FALHOU (canal-{canal}): {g1_max:.2e}")
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
    """Phi_g(t) ao longo da trajetoria (blocos corrigidos)."""
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
    return phig, psi


def kh_de(Ns, Hs_arr, kc):
    return kc / (np.exp(Ns) * Hs_arr)


def idx_kh(khs, alvo):
    return int(np.argmin(np.abs(khs - alvo)))


def analisa(B1V, kc_fator=1.0, rotulo=""):
    say("")
    say("=" * 72)
    say(f"FUNDO beta-constante beta1={B1V:g}{rotulo}")
    say("=" * 72)
    f0 = fundo_bconst(A_MIN, B1V)
    kc = 45.0 * f0['H'] * A_MIN * kc_fator
    say(f"    H(100)={f0['H']:.4f}; k_c={kc:.1f}")
    Ns, Hs_arr, Ms = build_track(B1V, NPTS, kc)
    red = reduz_full(Ns, Hs_arr, Ms, 'S')
    say(f"    [G1 OK canal-S] {red['g1']:.2e}")
    K2, C2, W2 = red['K2'], red['C2'], red['W2']
    traj = evolui_2dof(K2, C2, W2, Ns, Hs_arr)
    khs = kh_de(Ns, Hs_arr, kc)
    i20 = idx_kh(khs, PASSAGEM[0])
    i02 = idx_kh(khs, PASSAGEM[1])

    # taxa met por janela (componente Etil) — IC de posicao metrica
    say("")
    say("    taxas met por janela de kh (d lnA_met/dt/H_mid; "
        "IC Etil(pos) | max sobre 4 ICs):")
    say(f"    {'janela':>12} {'Etil(pos)':>10} {'max ICs':>10}")
    envs = {ic: envelope(traj[ic], 0, K2, W2, Hs_arr) for ic in range(4)}
    envs_chi = {ic: envelope(traj[ic], 1, K2, W2, Hs_arr) for ic in range(4)}
    for lo, hi in JANELAS_KH:
        ilo = idx_kh(khs, lo)
        ihi = idx_kh(khs, hi)
        if ilo >= ihi - 2:
            say(f"    {f'kh{lo}-{hi}':>12} {'—':>10} {'—':>10}")
            continue
        imid = (ilo + ihi) // 2
        dt_j = np.sum((Ns[ilo + 1:ihi + 1] - Ns[ilo:ihi])
                      / Hs_arr[ilo:ihi])
        txs = []
        for ic in range(4):
            A = envs[ic]
            if A[ilo] < 1e-250 or A[ihi] < 1e-250:
                txs.append(float('nan'))
                continue
            txs.append((np.log(A[ihi]) - np.log(A[ilo])) / dt_j
                       / Hs_arr[imid])
        t0 = txs[0]
        tmax = np.nanmax(txs)
        say(f"    {f'kh{lo}-{hi}':>12} {t0:+10.2f} {tmax:+10.2f}")

    # lnA de passagem por IC (met = Etil) + NULL (dchi)
    say("")
    say(f"    lnA_PASSAGEM (kh {PASSAGEM[0]:g} -> {PASSAGEM[1]:g}); "
        f"referencia antiga (3-DOF): {REF_ANTIGO.get(B1V, float('nan')):+.2f}")
    lnAs = []
    lnAs_chi = []
    for ic in range(4):
        A = envs[ic]
        ok = A[i20] > 1e-250 and A[i02] > 1e-250
        v = np.log(A[i02] / A[i20]) if ok else float('nan')
        lnAs.append(v)
        Achi = envs_chi[ic]
        okc = Achi[i20] > 1e-250 and Achi[i02] > 1e-250
        vc = np.log(Achi[i02] / Achi[i20]) if okc else float('nan')
        lnAs_chi.append(vc)
        say(f"      {IC_ROT[ic]:>10}: lnA_met = "
            f"{v:+8.3f}   lnA_dchi = {vc:+8.3f}")
    lnA_max = float(np.nanmax(lnAs))
    lnA_null = float(np.nanmax([lnAs_chi[1], lnAs_chi[3]]))
    ok_null = lnA_null <= 0.5
    say(f"    lnA_met max = {lnA_max:+.3f}; NULL (dchi) max = "
        f"{lnA_null:+.3f} ({'OK' if ok_null else 'FALHOU'} <= +0.5)")

    # Phi_g na passagem
    say("")
    say("    Phi_g reconstruido (blocos corrigidos), na passagem:")
    dphis = []
    razoes = []
    for ic in range(4):
        phig, psi = reconstrui_phig(traj[ic], red, Ns, Hs_arr)
        seg = np.abs(phig[i20:i02 + 1])
        segA = envs[ic][i20:i02 + 1]
        if np.max(seg) < 1e-250:
            say(f"      {IC_ROT[ic]:>10}: Phi_g ~ 0 (componente nula)")
            dphis.append(float('nan'))
            continue
        # envelope de |Phi_g| por maximos locais (oscilante):
        dln = np.log(max(seg[-1], 1e-300)) - np.log(max(seg[0], 1e-300))
        raz = float(np.median(seg / np.maximum(segA, 1e-300)))
        dphis.append(dln)
        razoes.append(raz)
        say(f"      {IC_ROT[ic]:>10}: Delta ln|Phi_g| = {dln:+8.3f}; "
            f"mediana |Phi_g|/A_met = {raz:.3f}")
    return dict(lnAs=lnAs, lnA_max=lnA_max, lnA_null=lnA_null,
                ok_null=ok_null, dphis=dphis, razoes=razoes, kc=kc)


res = {}
res[(1.0, 1)] = analisa(1.0)
res[(1.0, 3)] = analisa(1.0, kc_fator=3.0, rotulo=" (AUTOSIM: 3k)")
res[(4.47, 1)] = analisa(4.47)

say("")
say("=" * 72)
say("VEREDITO R-7b (criterios pre-declarados no cabecalho)")
say("=" * 72)
auto = abs(res[(1.0, 1)]['lnA_max'] - res[(1.0, 3)]['lnA_max'])
ok_auto = (res[(1.0, 1)]['lnA_max'] < -4.0
           and res[(1.0, 3)]['lnA_max'] < -4.0)
say(f"  R7b-AUTOSIM v2 (regime decadente): lnA(k) = "
    f"{res[(1.0, 1)]['lnA_max']:+.2f}, lnA(3k) = "
    f"{res[(1.0, 3)]['lnA_max']:+.2f} — ambos < -4: "
    f"{'OK' if ok_auto else 'FALHOU'} (dif numerica {auto:.2f}, "
    f"mix-dependente, reportada)")
for (B1V, fk), r in res.items():
    if fk != 1:
        continue
    say(f"  beta1={B1V:g}: lnA_met max = {r['lnA_max']:+.3f} "
        f"(antigo 3-DOF: {REF_ANTIGO[B1V]:+.2f}); NULL dchi "
        f"{r['lnA_null']:+.3f} ({'OK' if r['ok_null'] else 'FALHOU'}); "
        f"Delta ln|Phi_g| ICs: "
        + " ".join(f"{x:+.2f}" for x in r['dphis'] if np.isfinite(x)))
lnA_all = max(r['lnA_max'] for (b, fk), r in res.items() if fk == 1)
if lnA_all >= 3.5:
    say("  >>> BANDA-VIVA — contradiz r6d; investigar antes de usar.")
elif lnA_all <= 0.0:
    say("  >>> BANDA-MORTA: a amplificacao metrica do R-4 (lnA ~ +4)")
    say("  era artefato do 3o DOF espurio (bug do erratum-02). R-4b")
    say("  substituido. Se Delta ln|Phi_g| < 0, o elo do R-5 cai junto")
    say("  (insumo do R-7d).")
else:
    say(f"  >>> BANDA-REDUZIDA: lnA_max = {lnA_all:+.3f} — quantificar")
    say("  e discutir antes de qualquer uso observacional.")

os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
with open(os.path.join(HERE, 'out', 'r7b_banda_estatica_2dof.txt'), 'w',
          encoding='utf-8') as fh:
    fh.write("\n".join(OUT) + "\n")
say("")
say("saida escrita em auditoria/code/out/r7b_banda_estatica_2dof.txt")
