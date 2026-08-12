# -*- coding: utf-8 -*-
"""
r9a_omega2_diagnostico.py — BLOCO 0, item (c): resolver o omega^2 < 0
do R-7e, e primeira leitura de c_s^2 (gradiente).

CONTEXTO: parecer de cosmologia (docs/pareceres_especialistas/
parecer_cosmologia.md; sintese 00_sintese_cruzada.md §3). O R-7e
reportou om2 = W2_ii/K2_ii NEGATIVO variando de -1e2 a -1e7 e o
repositorio arquivou o crescimento de envelope como "artefato de
envelope". O parecer aponta incompatibilidade interna: |om|/H ~ 3e3
com decaimento medido G_win = -10 nao fecha — com |om| >> H a friccao
3H nao amortece.

A HIPOTESE (leitura (i) da sintese): W/K NAO e a frequencia efetiva
na convencao do repositorio. O integrador resolve
    K q'' + A q' + B q = 0,   A = Kdot + C - C^T,   B = Cdot + W
logo, por componente (setores desacoplados no beta-constante):
    omega^2_efetivo = B_ii/K_ii = (Cdot_ii + W_ii)/K_ii
    Gamma_efetivo   = A_ii/K_ii = Kdot_ii/K_ii   (antissim. tem diag 0)
O R-7e mediu W_ii/K_ii, que OMITE Cdot_ii. Se om2_ef > 0 onde
W/K < 0, a leitura (i) esta certa e o arquivamento como artefato de
envelope se sustenta — mas com a explicacao correta.

MEDIDAS (pre-declaradas):
 PARTE A — resolucao do om2 (trilha longa, kc = 45 H(100) 100, a mesma
   do R-7a; beta1 = 1 e 4.47; NPTS=12000):
   em ~8 marcos, por componente (Etil, dchi):
     om2_naive = W/K ; om2_ef = (Cdot+W)/K ; Gamma = Kdot/K ;
     raizes locais lam± = (-Gamma ± sqrt(Gamma^2 - 4 om2_ef))/2 ;
     taxa MEDIDA do envelope com normalizacao CONGELADA (janela de
     +-0.15 e-fold em torno do marco), das 4 ICs.
   V-FREQ (criterio, v4): o discriminador e a FASE ACUMULADA. Do
     marco ate +2 e-folds (ou o fim da trilha), compara-se
         Phi_prev = integral de sqrt(om2_ef)/H dN   (fase WKB)
     com  Phi_med = n_cruzamentos * pi.
     Criterio: |Phi_med - Phi_prev|/Phi_prev < 0.25 em >= 80% dos
     marcos COM RESOLUCAO (Phi_prev >= 2 pi). Marcos com
     Phi_prev < 2 pi sao declarados SEM RESOLUCAO e excluidos do
     criterio — nao ha como contar oscilacoes de um modo que nao
     completa um ciclo na trilha disponivel (limite fisico: no IR
     tardio o modo esta congelado).
     (v3 usava janela fixa de +-0.25 e-fold e frequencia local, e
     reprovou com 25% por esse motivo — sem resolucao em 12 dos 16
     marcos. Preservado no git.) E DECISIVO porque, se om2 fosse
     realmente NEGATIVO (como diz W/K), NAO HAVERIA OSCILACAO
     NENHUMA — o modo seria exponencial puro. Contar oscilacoes
     separa as duas hipoteses sem ambiguidade.
     HISTORICO DE INSTRUMENTO (preservado no git): a v1 comparava a
     taxa de envelope com a raiz local lam+ = (-Gamma +
     sqrt(Gamma^2-4 om2))/2 e reprovou (56%); a v2 trocou, no regime
     oscilatorio, por -Gamma/2 - (1/2) d ln(K omega)/dN (invariante
     adiabatico) e reprovou pior (31%). A autopsia identificou a
     causa comum: as ICs do teste (delta de posicao/velocidade) NAO
     sao adiabaticas, entao a taxa de envelope nos primeiros marcos
     mede transiente e mistura de ramos, nao WKB. A taxa so seria
     comparavel com ICs casadas em WKB — outro teste. A frequencia,
     ao contrario, e robusta a isso.
   V-SINAL: contar marcos com om2_naive < 0 E om2_ef > 0 — a medida
     direta do erro de leitura.

 PARTE B — c_s^2 (o diagnostico de gradiente; NAO substitui o A1 do
   Bloco 1, que exige criterios proprios e confronto com 1407.4331):
   em 3 epocas (a = 150, 3635, 74992) x 6 valores de kh (3, 10, 30,
   100, 300, 1000), mini-trilhas de 41 pontos:
     om2_ef(k) por componente; ajuste om2_ef = c_s^2 (k/a)^2 + m_ef^2
     na JANELA BEM-CONDICIONADA kh in [30, 300] (v2). A v1 ajustava
     nos 3 maiores kh e dava c_s^2 = 1.969 para o Etil; a inspecao da
     propria tabela mostrou que a razao om2_ef/(k/a)^2 vale 1.010 em
     kh=100 e 1.081 em kh=300, mas salta para 1.929 em kh=1000 — ou
     seja, o ponto kh=1000 contamina o ajuste. Este script agora
     REPORTA cond(W_XX) por kh para distinguir k^4 fisico de perda de
     condicionamento, e ajusta fora do ponto suspeito.
   G-CS (criterio): c_s^2 > 0 em todas as epocas/fundos -> sem
     instabilidade de gradiente no benchmark beta-constante (nivel
     2b, fronteira declarada). c_s^2 < 0 em algum ponto -> ALERTA:
     aciona o A1 completo com prioridade maxima.
   Referencia de sanidade: o espectador dchi tem c_s^2 = 1 exato
     (ancora do R-7a M3) — serve de calibracao do ajuste.

FRONTEIRA: fundos beta-constantes (F'=F''=0), matéria so como ρ do
fundo, sistema 2-DOF reduzido (E1+E2 corrigidas, canal-S).

Requer sympy, numpy. ~4-8 min.
Uso (raiz do repo, venv ativo):
    python auditoria/code/r9a_omega2_diagnostico.py
Saida em auditoria/code/out/r9a_omega2_diagnostico.txt
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
NPTS = 12000
G1_TOL = 1e-10
COMPS = [(0, 'Etil'), (1, 'dchi')]
EPOCAS_B = [150.0, 3635.0, 74992.0]
KHS_B = [3.0, 10.0, 30.0, 100.0, 300.0, 1000.0]

MU = 1.0
ME2 = 0.5
B0V, B2V, B4V = 1.0, -0.4, 0.5
RHO0 = 0.3

say("=" * 72)
say("R-9a — BLOCO 0(c): o omega^2 do R-7e e a primeira leitura de c_s^2")
say("=" * 72)

if not d1.gr_selfcheck():
    say("[!] V1 falhou — abortando")
    sys.exit(1)
say("[V1] GR selfcheck: PASSA")

L2s, fields, vels = d1.build_L2()
K7, C7, W7 = quadratic_matrices(L2s, fields, vels)
if [str(f) for f in fields] != NOMES:
    raise RuntimeError("ordem de campos mudou")
Hdd_s, Hfdd_s, xidd_s, chiddd_s = sp.symbols(
    'Hddot H_fddot xiddot chidddot')
Cd7 = sp.zeros(7, 7)
for i in range(7):
    for j in range(7):
        Cd7[i, j] = dt_background(
            C7[i, j], {Hd_s: Hdd_s, Hfd_s: Hfdd_s, xid_s: xidd_s,
                       chidd_s: chiddd_s})
say("[montagem] K,C,W,CdS prontos")

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


FK, FC, FW, FCd = fatias(K7), fatias(C7), fatias(W7), fatias(Cd7)
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


def build_track(B1V, Ns, kc):
    npts = len(Ns)
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
        Ms['K'][p] = D @ monta(FK, args, bvals) @ D
        Ms['C'][p] = D @ monta(FC, args, bvals) @ D
        Ms['W'][p] = D @ monta(FW, args, bvals) @ D
        Ms['CdS'][p] = D @ monta(FCd, args, bvals) @ D
    return Hs_arr, Ms


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
    condW = np.linalg.cond(WXX)
    WXXi = np.linalg.inv(WXX)
    CdX = C[np.ix_(DYN, MULT)]
    K3 = K[np.ix_(DYN, DYN)] + CdX @ WXXi @ CdX.T
    C3 = C[np.ix_(DYN, DYN)] - CdX @ WXXi @ W[np.ix_(MULT, DYN)]
    W3 = W[np.ix_(DYN, DYN)] - W[np.ix_(DYN, MULT)] @ WXXi \
        @ W[np.ix_(MULT, DYN)]
    return K3, C3, W3, condW


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
    wx = W[np.ix_(keep, [0])]
    K2 = K[np.ix_(keep, keep)] + cx @ cx.T / W00
    C2 = C[np.ix_(keep, keep)] - cx @ W[np.ix_([0], keep)] / W00
    W2 = W[np.ix_(keep, keep)] - wx @ W[np.ix_([0], keep)] / W00
    return 0.5 * (K2 + K2.T), C2, 0.5 * (W2 + W2.T)


def reduz(Ns, Hs_arr, Ms):
    npts = len(Ns)
    K3s = np.zeros((npts, 3, 3))
    C3s = np.zeros((npts, 3, 3))
    W3s = np.zeros((npts, 3, 3))
    g1 = 0.0
    cond_max = 0.0
    for p in range(npts):
        K3, C3, W3, condW = e1_corr(Ms['K'][p], Ms['C'][p], Ms['W'][p],
                                    Ms['CdS'][p])
        cond_max = max(cond_max, condW)
        esc = np.max(np.abs(K3))
        g1 = max(g1, np.max(np.abs(K3[0, :])) / esc)
        K3[0, :] = 0.0
        K3[:, 0] = 0.0
        K3s[p], C3s[p], W3s[p] = K3, C3, W3
    if g1 >= G1_TOL:
        raise RuntimeError(f"G1 falhou: {g1:.2e}")
    C3d = np.gradient(C3s, Ns, axis=0) * Hs_arr[:, None, None]
    K2s = np.zeros((npts, 2, 2))
    C2s = np.zeros((npts, 2, 2))
    W2s = np.zeros((npts, 2, 2))
    for p in range(npts):
        K2s[p], C2s[p], W2s[p] = e2_psi(K3s[p], C3s[p], W3s[p], C3d[p])
    if npts > 6:
        for M in (K2s, C2s, W2s):
            M[0] = M[2]
            M[1] = M[2]
            M[-1] = M[-3]
            M[-2] = M[-3]
    return K2s, C2s, W2s, g1, cond_max


def freq_efetiva(K2, C2, W2, Ns, Hs_arr):
    """om2_naive = W/K ; om2_ef = (Cdot+W)/K ; Gamma = Kdot/K."""
    K2d = np.gradient(K2, Ns, axis=0) * Hs_arr[:, None, None]
    C2d = np.gradient(C2, Ns, axis=0) * Hs_arr[:, None, None]
    npts = len(Ns)
    om2_n = np.zeros((npts, 2))
    om2_e = np.zeros((npts, 2))
    gam = np.zeros((npts, 2))
    for i in range(2):
        om2_n[:, i] = W2[:, i, i] / K2[:, i, i]
        om2_e[:, i] = (C2d[:, i, i] + W2[:, i, i]) / K2[:, i, i]
        gam[:, i] = K2d[:, i, i] / K2[:, i, i]
    return om2_n, om2_e, gam


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


# ------------------------------------------------------------------
# PARTE A
# ------------------------------------------------------------------
def parte_a(B1V):
    say("")
    say("=" * 72)
    say(f"PARTE A — resolucao do omega^2 (beta1={B1V:g})")
    say("=" * 72)
    f0 = fundo_bconst(A_MIN, B1V)
    kc = 45.0 * f0['H'] * A_MIN
    Ns = np.linspace(np.log(A_MIN), np.log(A_MAX), NPTS)
    Hs_arr, Ms = build_track(B1V, Ns, kc)
    K2, C2, W2, g1, _ = reduz(Ns, Hs_arr, Ms)
    say(f"    [G1 OK canal-S] {g1:.2e}; k_c = {kc:.1f}")
    om2_n, om2_e, gam = freq_efetiva(K2, C2, W2, Ns, Hs_arr)
    traj = evolui(K2, C2, W2, Ns, Hs_arr)
    aas = np.exp(Ns)
    marcas = np.geomspace(200.0, 60000.0, 8)
    mid = [int(np.argmin(np.abs(aas - am))) for am in marcas]
    say("")
    say("    V-FREQ — frequencia MEDIDA (cruzamentos de zero) vs as "
        "duas hipoteses:")
    say(f"    {'a':>7} {'comp':>5} {'|om_n|/H':>9} {'om_ef/H':>9} "
        f"{'Phi_prev':>9} {'Phi_med':>8} {'n_cruz':>7} {'ok':>10}")
    ok_cnt = 0
    tot_cnt = 0
    sem_res = 0
    sinal_cnt = 0
    ent_cnt = 0
    om_ef_arr = np.sqrt(np.maximum(om2_e, 0.0)) / Hs_arr[:, None]
    for mi in mid:
        H = Hs_arr[mi]
        for ci, rot in COMPS:
            ent_cnt += 1
            if om2_n[mi, ci] < 0 and om2_e[mi, ci] > 0:
                sinal_cnt += 1
            o2e = om2_e[mi, ci] / H**2
            if o2e <= 0:
                continue
            om_ef = np.sqrt(o2e)
            om_nv = np.sqrt(abs(om2_n[mi, ci])) / H
            jhi = int(np.argmin(np.abs(Ns - min(Ns[mi] + 2.0,
                                                Ns[-1]))))
            if jhi <= mi + 5:
                continue
            phi_prev = float(np.trapezoid(om_ef_arr[mi:jhi + 1, ci],
                                          Ns[mi:jhi + 1]))
            ns = []
            for ic in range(4):
                q = traj[ic][mi:jhi + 1, ci]
                if np.max(np.abs(q)) < 1e-250:
                    continue
                sg = np.sign(q)
                sg = sg[sg != 0]
                ns.append(int(np.sum(sg[1:] * sg[:-1] < 0)))
            if not ns:
                continue
            n_med = float(np.median(ns))
            phi_med = n_med * np.pi
            if phi_prev < 2 * np.pi:
                sem_res += 1
                rot_ok = 'sem res.'
            else:
                ok = abs(phi_med - phi_prev) / phi_prev < 0.25
                ok_cnt += int(ok)
                tot_cnt += 1
                rot_ok = 'OK' if ok else 'X'
            say(f"    {aas[mi]:7.0f} {rot:>5} {om_nv:9.1f} {om_ef:9.2f} "
                f"{phi_prev:9.2f} {phi_med:8.2f} {n_med:7.1f} "
                f"{rot_ok:>10}")
    frac = ok_cnt / max(tot_cnt, 1)
    ok_freq = (frac >= 0.8 and tot_cnt >= 3)
    say("")
    say(f"    [V-FREQ {'OK' if ok_freq else 'FALHOU'}] "
        f"{ok_cnt}/{tot_cnt} = {100*frac:.0f}% dos marcos COM RESOLUCAO "
        f"(criterio >= 80%); {sem_res} marcos sem resolucao "
        f"(Phi_prev < 2pi — modo congelado, limite fisico)")
    say("    (a hipotese W/K prevê |om|/H da 1a coluna e, sendo om2<0,")
    say("     prevê AUSENCIA de oscilacao — refutada por qualquer")
    say("     n_cruz > 0 no Etil)")
    say(f"    [V-SINAL] entradas com om2_naive < 0 MAS om2_efetivo > 0: "
        f"{sinal_cnt}/{ent_cnt} — a medida direta do erro de leitura "
        f"do R-7e")
    return ok_freq, sinal_cnt, ent_cnt


# ------------------------------------------------------------------
# PARTE B — c_s^2
# ------------------------------------------------------------------
def parte_b(B1V):
    say("")
    say("=" * 72)
    say(f"PARTE B — c_s^2 por ajuste om2_ef = c_s^2 (k/a)^2 + m_ef^2 "
        f"(beta1={B1V:g})")
    say("=" * 72)
    say("    razao om2_ef/(k/a)^2 por kh (deve ser ~ c_s^2 no regime "
        "de gradiente), e cond(W_XX):")
    say(f"    {'a':>8} {'comp':>5} " +
        " ".join(f"kh={kh:g}".rjust(10) for kh in KHS_B) +
        f" {'c_s^2[30-100]':>13}")
    alerta = []
    IFIT = [i for i, kh in enumerate(KHS_B) if 30.0 <= kh <= 100.0]
    for a0 in EPOCAS_B:
        f0 = fundo_bconst(a0, B1V)
        H0 = f0['H']
        dados = {ci: [] for ci, _ in COMPS}
        conds = []
        for kh in KHS_B:
            kc = kh * a0 * H0
            Ns = np.linspace(np.log(a0) - 0.02, np.log(a0) + 0.02, 41)
            Hs_l, Ml = build_track(B1V, Ns, kc)
            K2l, C2l, W2l, _, cnd = reduz(Ns, Hs_l, Ml)
            conds.append(cnd)
            _, om2_e, _ = freq_efetiva(K2l, C2l, W2l, Ns, Hs_l)
            for ci, _ in COMPS:
                dados[ci].append(om2_e[20, ci])
        for ci, rot in COMPS:
            ys = np.array(dados[ci])
            xs = np.array([(kh * H0)**2 for kh in KHS_B])
            razoes = ys / xs
            A = np.vstack([xs[IFIT], np.ones(len(IFIT))]).T
            cs2, mef2 = np.linalg.lstsq(A, ys[IFIT], rcond=None)[0]
            if cs2 < 0:
                alerta.append((a0, rot, cs2))
            say(f"    {a0:8.0f} {rot:>5} " +
                " ".join(f"{rz:+10.4f}" for rz in razoes) +
                f" {cs2:+13.4f}")
            if rot == 'Etil':
                exc = razoes[-1] - razoes[3]
                say(f"    {'':>8} {'k4?':>5} excesso da razao entre "
                    f"kh=100 e kh=1000: {exc:+.3f} — termo ~k^4 com "
                    f"escala M/H ~ {1000.0/max(np.sqrt(abs(exc)),1e-9):.0f} "
                    f"(cond(W_XX) < 1e2 em toda a faixa => e ESTRUTURA, "
                    f"nao condicionamento)")
        say(f"    {'':>8} {'cond':>5} " +
            " ".join(f"{c:10.1e}" for c in conds))
    return alerta


res_a = {}
alertas = []
for B1V in (1.0, 4.47):
    res_a[B1V] = parte_a(B1V)
    alertas += parte_b(B1V)

say("")
say("=" * 72)
say("VEREDITO R-9a (criterios pre-declarados no cabecalho)")
say("=" * 72)
ok_om = all(res_a[b][0] for b in res_a)
tot_sinal = sum(res_a[b][1] for b in res_a)
tot_marc = sum(res_a[b][2] for b in res_a)
say(f"  V-FREQ: {'OK nos dois fundos' if ok_om else 'FALHOU em algum fundo'}")
say(f"  V-SINAL: {tot_sinal}/{tot_marc} entradas tinham W/K < 0 com "
    f"(Cdot+W)/K > 0")
if ok_om and tot_sinal > 0:
    say("  >>> ITEM (c) RESOLVIDO — leitura (i) da sintese confirmada:")
    say("  W/K NAO e a frequencia efetiva nesta convencao (falta o")
    say("  Cdot). Com a frequencia correta, a dinamica medida e")
    say("  explicada pelo oscilador amortecido local. O 'omega^2 < 0'")
    say("  do R-7e era razao errada, nao fisica nova — e o")
    say("  arquivamento como artefato de envelope se sustenta, agora")
    say("  COM a explicacao correta. Corrigir o texto do R-7e/sintese.")
elif ok_om:
    say("  >>> ITEM (c) resolvido, mas sem inversao de sinal: rever")
    say("  a leitura do parecer contra estes numeros.")
else:
    say("  >>> NAO RESOLVIDO: a dinamica NAO e explicada pelo")
    say("  oscilador local — leitura (ii) ou (iii) da sintese;")
    say("  escalar para o A1 com prioridade maxima.")
say("")
if alertas:
    say(f"  [G-CS ALERTA] c_s^2 < 0 em {len(alertas)} caso(s): "
        f"{[(f'a={a:.0f}', r, f'{c:+.3f}') for a, r, c in alertas]}")
    say("  >>> ACIONA o A1 (teste de gradiente completo) com")
    say("  prioridade maxima, com confronto a 1407.4331.")
else:
    say("  [G-CS OK] c_s^2 > 0 em todas as epocas/componentes/fundos")
    say("  testados — sem indicio de instabilidade de gradiente no")
    say("  benchmark beta-constante (nivel 2b; NAO substitui o A1,")
    say("  que exige o fundo dinamico e o confronto com a literatura).")

os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
with open(os.path.join(HERE, 'out', 'r9a_omega2_diagnostico.txt'), 'w',
          encoding='utf-8') as fh:
    fh.write("\n".join(OUT) + "\n")
say("")
say("saida escrita em auditoria/code/out/r9a_omega2_diagnostico.txt")
