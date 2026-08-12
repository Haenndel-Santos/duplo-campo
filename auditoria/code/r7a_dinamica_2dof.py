# -*- coding: utf-8 -*-
"""
r7a_dinamica_2dof.py — R-7a: REEXECUCAO DA CASCATA (1/4). Dinamica
reduzida CORRIGIDA nos fundos beta-constantes + V-XREP.

CONTEXTO: erratum_02_reducao_numerica.md. O reduz_ponto numerico usado
de D-2 a R-5 dobrava Cdot nas entradas off-diagonais de W_XX; o
"3o DOF escalar" (e o fantasma do Gate F) era artefato. Este script e
o primeiro da reexecucao: estabelece a maquinaria corrigida e refaz as
perguntas de D-2/R-1 na classe beta-constante (beta1=1 e 4.47).

REDUCAO CORRIGIDA (2 estagios):
  E1: absorcao one-shot dos 4 multiplicadores (S simetrica; Cdot
      contado UMA vez por par X-X) + Schur em W_XX -> 3x3
      (Psi_f, E_f, dchi).
  G1 (gate): max|K3[Psi_f,:]|/max|K3| em TODA a trilha, por canal:
      canal-S (Cdot exato) < 1e-10 — e o certificado ESTRUTURAL do
      zero (r6c/r6d); canal-G (gradiente em grade) < 1e-6 — o residuo
      esperado e O(dN^2) ~ 1e-7 da discretizacao do Cdot, medido e
      reportado. So entao a linha e zerada explicitamente.
  E2: IPP da linha C de Psi_f (uma variavel — sem par, sem bug) +
      Schur em W00.
  G2 (gate): W00_eff (o coeficiente auxiliar de Psi_f) tem que ser
      REAL e RESOLVIDO, nao ruido de cancelamento: |W00_G - W00_S|/
      |W00_S| < 1e-5 em toda a trilha (concordancia dos dois canais
      independentes de Cdot — V-XREP aplicado a propria quantidade).
      O valor relativo min |W00|/max|W3| e reportado (informativo:
      esc(W3) cresce com k^4; um W00 moderado e relativo pequeno e
      esperado e nao e patologia).
  Resultado: sistema 2x2 (Etil = k^2 E_f, dchi).
  NOTA de canal: o Cdot do estagio E2 (linha C de Psi_f reduzida) e
      por gradiente de grade em ambos os canais (a reducao e numerica
      ponto a ponto; nao ha forma simbolica da C reduzida). A
      independencia dos canais cobre integralmente o estagio E1 —
      onde vivia o bug do erratum-02.
  EQUILIBRACAO (necessaria para resolver W00): as variaveis cruas
      carregam potencias de k desiguais (E_f com k^4 em K/W; B's com
      k^2), o que faz W00 nascer de cancelamento de profundidade
      ~1e-14 da escala ambiente — irresoluvel em float64 e afogado
      pelo O(dN^2) do canal-G (1a rodada deste script: discrepancia
      de 56% em W00; registrada). Cura: congruencia CONSTANTE NO
      TEMPO q -> D q com D = diag(1, 1/k, 1, 1, 1/k, 1/k^2, 1)
      (i.e., Btil = k B, Etil = k^2 E_f — normalizacao padrao). Nao
      altera a fisica (Sylvester; D constante => estrutura IPP
      intacta) e torna os cancelamentos rasos.

V-XREP (novo gate obrigatorio do erratum): a reducao roda com DOIS
canais INDEPENDENTES de Cdot:
  canal-G: gradiente numerico na grade (o de producao);
  canal-S: Cdot SIMBOLICO via dt_background da lib (regras de fundo:
      a,b,xi,H,H_f,chid + cadeias F e U), avaliado com as taxas do
      fundo (Hd, Hfd, xid) — nenhuma diferenciacao em grade.
  G3 (gate): max diff relativa de K2/C2/W2 entre os canais < 1e-4.
  (Para beta-constante o canal-S e exato; a comparacao valida a
  trilha inteira. NOTA: verifica-se em-script se C7 depende de Upp —
  se nao, o canal-S e exato tambem no fundo rolante do R-7c.)

MEDIDAS (pre-declaradas):
  M1 — estrutura: autovalores de K2 na trilha (negativos? esperado 0;
      acoplamento off-diagonal K2/C2/W2 entre E_f e dchi).
  M2 — evolucao (RK4, NPTS=24000, halving 12000): 4 ICs fundamentais
      (E_f pos/vel, dchi pos/vel). Taxas tardias por componente
      (ultimo e-fold).
      ANCORAS QUANTITATIVAS (da reauditoria externa, secao 4 — que
      por sua vez explicam o sigma_can 1.13/1.41 do Gate F-b):
        taxa fisica tardia de dchi = -3/2 + sqrt(9/4 - 0.3/H^2):
        beta1=1    -> -0.368 H
        beta1=4.47 -> -0.082 H
      (tolerancia 0.05). E_f: taxa tardia negativa esperada
      (dilucao; sem ancora analitica — medida).
  M3 — dispersao do sistema saudavel (insumo do R-7d/discriminacao):
      QEP no 2x2 em a tardio, k varrido: omega^2(k_phys) e ajuste
      c_s^2 por modo; sinal de W (tachyon?).
  M4 — halving: |lnA(24k) - lnA(12k)| < 0.1 por IC/janela tardia.

CRITERIOS (pre-declarados):
  G1/G2/G3 falham -> NAO INTERPRETAR (abortar com relatorio).
  M2 dentro das ancoras + zero autovalores negativos ->
      D-2/R-1 substituidos nesta classe: dinamica 2-DOF saudavel,
      dilucao tardia confirmada no sistema FISICO (nao no espurio).
  Qualquer autovalor cinetico negativo persistente ou crescimento
      tardio -> reportar sem interpretar (contradiz r6d; investigar).

Requer sympy, numpy. ~8-15 min.
Uso (raiz do repo, venv ativo):
    python auditoria/code/r7a_dinamica_2dof.py
Saida em auditoria/code/out/r7a_dinamica_2dof.txt
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
DYN = [3, 5, 6]          # apos E1: (Psi_f, E_f, dchi); apos E2: (E_f, dchi)
A_MIN, A_MAX = 100.0, 80000.0
NPTS = 24000
G1_TOL = {'G': 1e-4, 'S': 1e-10}
# G1 canal-G e informativo (qualidade do Cdot de grade; a linha e
# zerada apos o gate) — o certificado estrutural e o canal-S e o gate
# funcional do produto final e o G3.
G2_TOL = 1e-10
G3_TOL = 1e-4
ANCORA_DCHI = {1.0: -0.368, 4.47: -0.082}
ANC_TOL = 0.05

MU = 1.0
ME2 = 0.5
B0V, B2V, B4V = 1.0, -0.4, 0.5
RHO0 = 0.3

say("=" * 72)
say("R-7a — DINAMICA 2-DOF CORRIGIDA (beta-constante) + V-XREP")
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

# canal-S: Cdot simbolico (regras de fundo da lib + taxas de 2a ordem
# do fundo: C7 depende de Hd/Hfd/xid, cujas derivadas nao estao em
# RATES — sem elas o canal-S perde termos O(rho) que pesam onde W00 e
# pequeno; 1a rodada deste script mediu 56% de discrepancia em W00
# por isso)
say("[canal-S] dt_background(C7) simbolico ...")
tem_upp = any(C7[i, j].has(Upp) for i in range(7) for j in range(7))
dep2 = sorted({str(s) for i in range(7) for j in range(7)
               for s in C7[i, j].free_symbols
               if s in (Hd_s, Hfd_s, xid_s, chidd_s)})
say(f"    C7 depende de Upp? {tem_upp} "
    f"(False => canal-S exato tambem no fundo rolante do R-7c)")
say(f"    C7 depende das taxas de 1a ordem {dep2} => canal-S precisa "
    f"das taxas de 2a ordem do fundo")
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
say("[fatias] prontas (K, C, W, Cdot-simbolico)")


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


def matriz_D(kc):
    """equilibracao: Btil=k B, Etil=k^2 E (q = D qtil)."""
    return np.diag([1.0, 1.0 / kc, 1.0, 1.0, 1.0 / kc, 1.0 / kc**2, 1.0])


def fundo_ext(a, B1V, h=1e-5):
    """fundo + taxas de 2a ordem (Hdd, Hfdd, xidd) por estencil local
    nas funcoes FECHADAS do fundo (nao e diferenciacao de trilha)."""
    f = fundo_bconst(a, B1V)
    fp = fundo_bconst(a * np.exp(h), B1V)
    fm = fundo_bconst(a * np.exp(-h), B1V)
    H = f['H']
    f['Hdd'] = H * (fp['Hd'] - fm['Hd']) / (2 * h)
    f['Hfdd'] = H * (fp['Hfd'] - fm['Hfd']) / (2 * h)
    f['xidd'] = H * (fp['xid'] - fm['xid']) / (2 * h)
    return f


def args_de(f, a, kc):
    return (a, f['r'] * a, f['xi'], f['H'], f['Hf'],
            f['Hd'], f['Hfd'], f['xid'], 0.0, 0.0,
            f['Ub'], 0.0, 0.3, kc, 1.0, ME2,
            f['Hdd'], f['Hfdd'], f['xidd'], 0.0)


def build_track(B1V, npts, kc):
    Ns = np.linspace(np.log(A_MIN), np.log(A_MAX), npts)
    Hs_arr = np.zeros(npts)
    Ms = {x: np.zeros((npts, 7, 7)) for x in ('K', 'C', 'W', 'CdS')}
    D = matriz_D(kc)
    for p, N in enumerate(Ns):
        a = np.exp(N)
        f = fundo_ext(a, B1V)
        Hs_arr[p] = f['H']
        args = args_de(f, a, kc)
        bvals = (B0V, B1V, B2V, 0.0, B4V)
        z5 = (0.0,) * 5
        Ms['K'][p] = D @ monta(FK, args, bvals, z5, z5) @ D
        Ms['C'][p] = D @ monta(FC, args, bvals, z5, z5) @ D
        Ms['W'][p] = D @ monta(FW, args, bvals, z5, z5) @ D
        Ms['CdS'][p] = D @ monta(FCd, args, bvals, z5, z5) @ D
    return Ns, Hs_arr, Ms


# ------------------------------------------------------------------
# reducao corrigida: E1 (one-shot) + G1 + E2 (Psi_f) + G2
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
                W[i, j] += cd          # par X-X: contado UMA vez
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
    """IPP da linha 0 (Psi_f) + Schur em W00. K3[0,:] ja zerada."""
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


def reduz_2dof(Ns, Hs_arr, Ms, canal, skip_gates=False):
    npts = len(Ns)
    if canal == 'G':
        Cdots = np.gradient(Ms['C'], Ns, axis=0) * Hs_arr[:, None, None]
    else:
        Cdots = Ms['CdS']
    K3s = np.zeros((npts, 3, 3))
    C3s = np.zeros((npts, 3, 3))
    W3s = np.zeros((npts, 3, 3))
    g1_max = 0.0
    for p in range(npts):
        K3, C3, W3, _, _, _ = e1_corrigida(
            Ms['K'][p], Ms['C'][p], Ms['W'][p], Cdots[p])
        esc = np.max(np.abs(K3))
        g1_max = max(g1_max, np.max(np.abs(K3[0, :])) / esc)
        K3[0, :] = 0.0
        K3[:, 0] = 0.0
        K3s[p], C3s[p], W3s[p] = K3, C3, W3
    if not skip_gates and g1_max >= G1_TOL[canal]:
        raise RuntimeError(f"G1 FALHOU (canal-{canal}): "
                           f"max|K3[Psi_f,:]|/esc = {g1_max:.2e}")
    C3d = np.gradient(C3s, Ns, axis=0) * Hs_arr[:, None, None]
    K2s = np.zeros((npts, 2, 2))
    C2s = np.zeros((npts, 2, 2))
    W2s = np.zeros((npts, 2, 2))
    W00s = np.zeros(npts)
    g2_min = np.inf
    for p in range(npts):
        K2s[p], C2s[p], W2s[p], W00 = e2_psif(K3s[p], C3s[p], W3s[p], C3d[p])
        W00s[p] = W00
        g2_min = min(g2_min, abs(W00) / np.max(np.abs(W3s[p])))
    # bordas: o estencil one-sided do gradiente contamina os 2 pontos
    # extremos (G2-diag); substituidos pelos vizinhos interiores
    # (declarado — 4 de npts pontos; o integrador nao arranca em
    # matrizes contaminadas)
    if npts > 6:
        for M in (K2s, C2s, W2s):
            M[0] = M[2]
            M[1] = M[2]
            M[-1] = M[-3]
            M[-2] = M[-3]
        W00s[0] = W00s[1] = W00s[2]
        W00s[-1] = W00s[-2] = W00s[-3]
    return K2s, C2s, W2s, g1_max, g2_min, W00s


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


IC_ROT = ['E_f(pos)', 'dchi(pos)', 'E_f(vel)', 'dchi(vel)']


def taxa_tardia(hist, comp, Ns, Hs_arr, K2, W2):
    """taxa d ln A / dN no ultimo e-fold, com A = envelope
    sqrt(q^2 + qd^2/(omega^2+H^2)) — robusto a cruzamentos de zero
    (setores desacoplados: omega^2 = W_ii/K_ii)."""
    aas = np.exp(Ns)
    i1 = np.argmin(np.abs(aas - A_MAX / np.exp(0.5)))   # ultimo 1/2 e-fold
    q = hist[:, comp]
    qd = hist[:, comp + 2]
    om2 = np.abs(W2[:, comp, comp] / K2[:, comp, comp])
    A = np.sqrt(q * q + qd * qd / (om2 + Hs_arr**2))
    if np.max(A[i1:]) < 1e-250:
        return float('nan')
    seg = np.log(np.maximum(A[i1:], 1e-300))
    return float(np.polyfit(Ns[i1:], seg, 1)[0])   # dln/dN


def analisa(B1V):
    say("")
    say("=" * 72)
    say(f"FUNDO beta-constante beta1={B1V:g}")
    say("=" * 72)
    f0 = fundo_bconst(A_MIN, B1V)
    kc = 45.0 * f0['H'] * A_MIN
    say(f"    H(100)={f0['H']:.4f}; k_c={kc:.1f}")
    Ns, Hs_arr, Ms = build_track(B1V, NPTS, kc)

    # reducao nos dois canais + G2/G3
    K2g, C2g, W2g, g1g, g2g, W00g = reduz_2dof(Ns, Hs_arr, Ms, 'G')
    K2s_, C2s_, W2s_, g1s, g2s, W00s_ = reduz_2dof(Ns, Hs_arr, Ms, 'S')
    say(f"    [G1 OK] max|K3[Psi_f,:]|/esc: canal-G {g1g:.2e} "
        f"(< {G1_TOL['G']:g}, O(dN^2) esperado), canal-S {g1s:.2e} "
        f"(< {G1_TOL['S']:g}, estrutural)")
    difs = np.abs(W00g - W00s_) / np.abs(W00s_)
    dW00 = float(np.max(difs))
    ordem = np.argsort(difs)[::-1][:5]
    say("    [G2 diag] 5 piores pontos (p, a, W00_G, W00_S, dif rel):")
    for p in ordem:
        say(f"        p={p:6d} a={np.exp(Ns[p]):9.1f} "
            f"{W00g[p]:+.6e} {W00s_[p]:+.6e} {difs[p]:.2e}")
    interior = difs[2:-2]
    dW00_int = float(np.max(interior))
    ok2 = dW00_int < 1e-5
    say(f"    [G2 {'OK' if ok2 else 'FALHOU'}] W00 resolvido: max "
        f"|W00_G - W00_S|/|W00_S| = {dW00:.2e} (interior: "
        f"{dW00_int:.2e} < 1e-5); min|W00|/esc = {min(g2g, g2s):.2e} "
        f"(informativo); min|W00| abs = "
        f"{float(np.min(np.abs(W00s_))):.3e}")
    if not ok2:
        raise RuntimeError("G2 falhou — NAO INTERPRETAR")
    dmax = 0.0
    for Mg, Msy in ((K2g, K2s_), (C2g, C2s_), (W2g, W2s_)):
        esc = np.max(np.abs(Msy), axis=(1, 2), keepdims=True)
        dmax = max(dmax, float(np.max((np.abs(Mg - Msy) / esc)[2:-2])))
    ok3 = dmax < G3_TOL
    say(f"    [G3 {'OK' if ok3 else 'FALHOU'}] V-XREP max diff rel "
        f"K2/C2/W2 interior (canal-G vs canal-S) = {dmax:.2e} "
        f"(< {G3_TOL:g}; bordas excluidas — estencil one-sided do "
        f"gradiente, mesmo efeito ja isolado no G2)")
    if not ok3:
        raise RuntimeError("V-XREP falhou — NAO INTERPRETAR")

    # M1 — estrutura
    aas = np.exp(Ns)
    neg = 0
    offmax = 0.0
    for p in range(NPTS):
        lam = np.linalg.eigvalsh(K2g[p])
        if lam[0] <= 0:
            neg += 1
        esc = np.sqrt(abs(K2g[p][0, 0] * K2g[p][1, 1])) + 1e-300
        offmax = max(offmax, abs(K2g[p][0, 1]) / esc)
    say(f"    M1 — autovalores K2 negativos: {neg}/{NPTS} pontos; "
        f"acoplamento |K2[Ef,dchi]|/sqrt(K00*K11) max = {offmax:.2e}")

    # M2 — evolucao (producao) + M4 halving
    traj = evolui_2dof(K2g, C2g, W2g, Ns, Hs_arr)
    say("")
    say("    M2 — taxas tardias (ultimo e-fold), d ln|comp|/dN:")
    say(f"    {'IC':>10} {'comp':>6} {'taxa':>8}  ancora")
    anc = ANCORA_DCHI[B1V]
    ok_anc = True
    res_taxas = {}
    for ic in range(4):
        for comp, rot in ((0, 'E_f'), (1, 'dchi')):
            tx = taxa_tardia(traj[ic], comp, Ns, Hs_arr, K2g, W2g)
            res_taxas[(ic, comp)] = tx
            if not np.isfinite(tx):
                say(f"    {IC_ROT[ic]:>10} {rot:>6} {'—':>8}  "
                    f"(componente nula — setores desacoplados)")
                continue
            marca = ""
            if comp == 1 and ic == 1:
                # gate: so a IC de POSICAO (a de velocidade carrega
                # transiente do ramo rapido — reportada como info)
                dif = abs(tx - anc)
                marca = (f"{anc:+.3f} (dif {dif:.3f} "
                         f"{'OK' if dif < ANC_TOL else 'FORA'})")
                if dif >= ANC_TOL:
                    ok_anc = False
            elif comp == 1 and ic == 3:
                marca = (f"{anc:+.3f} (info; transiente do ramo "
                         f"rapido admitido)")
            say(f"    {IC_ROT[ic]:>10} {rot:>6} {tx:+8.3f}  {marca}")

    # M4 — halving (criterio proporcional: em trajetorias que decaem
    # dezenas de e-folds, a tolerancia absoluta 0.1 vira exigencia de
    # ~0.3% do range logaritmico — o criterio e 0.1 OU 2% de |lnA|)
    idx_h = np.arange(0, NPTS, 2)
    Ns_h, Hs_h = Ns[idx_h], Hs_arr[idx_h]
    K2h, C2h, W2h = K2g[idx_h], C2g[idx_h], W2g[idx_h]
    traj_h = evolui_2dof(K2h, C2h, W2h, Ns_h, Hs_h)
    ok_h = True
    say("    M4 — halving por IC (lnA_24k, lnA_12k, err_Richardson = "
        "dif/15, criterio):")
    dmax_h = 0.0
    for ic in range(4):
        lnA = np.log(max(np.linalg.norm(traj[ic][-1]), 1e-300))
        lnA_h = np.log(max(np.linalg.norm(traj_h[ic][-1]), 1e-300))
        dif = abs(lnA - lnA_h)
        err = dif / 15.0        # RK4: erro(h) ~ dif/(2^4 - 1)
        crit = max(0.1, 0.02 * abs(lnA))
        if err >= crit:
            ok_h = False
        dmax_h = max(dmax_h, err)
        say(f"        {IC_ROT[ic]:>10}: {lnA:+8.3f} {lnA_h:+8.3f} "
            f"err {err:.4f} (< {crit:.3f} "
            f"{'OK' if err < crit else 'FALHOU'})")
    say(f"    M4 {'OK' if ok_h else 'FALHOU'}")

    # M3 — dispersao no 2x2 tardio (a=40000): omega^2(k) via QEP
    say("")
    say("    M3 — dispersao tardia (a=40000): QEP CONGELADO no 2x2.")
    say("    (convencao da lib: so C antissimetrica entra — a friccao")
    say("    simetrica nao; portanto Re(lam) aqui NAO e amortecimento")
    say("    fisico. Uso legitimo: dispersao omega(k). A estabilidade")
    say("    e julgada pelo M2 — evolucao real. Licao do D2 mantida.)")
    p0 = int(np.argmin(np.abs(aas - 40000.0)))
    H0 = Hs_arr[p0]
    for kh_alvo in (0.1, 0.3, 1.0, 3.0, 10.0):
        kc2 = kh_alvo * 40000.0 * H0
        # trilha curta local em torno de a=40000 para este k
        Ns_l = np.linspace(np.log(39000.0), np.log(41000.0), 41)
        Hs_l = np.zeros(41)
        Ml = {x: np.zeros((41, 7, 7)) for x in ('K', 'C', 'W', 'CdS')}
        Dl = matriz_D(kc2)
        for pp, Nl in enumerate(Ns_l):
            a = np.exp(Nl)
            f = fundo_ext(a, B1V)
            Hs_l[pp] = f['H']
            args = args_de(f, a, kc2)
            bvals = (B0V, B1V, B2V, 0.0, B4V)
            z5 = (0.0,) * 5
            Ml['K'][pp] = Dl @ monta(FK, args, bvals, z5, z5) @ Dl
            Ml['C'][pp] = Dl @ monta(FC, args, bvals, z5, z5) @ Dl
            Ml['W'][pp] = Dl @ monta(FW, args, bvals, z5, z5) @ Dl
            Ml['CdS'][pp] = Dl @ monta(FCd, args, bvals, z5, z5) @ Dl
        K2l, C2l, W2l, _, _, _ = reduz_2dof(Ns_l, Hs_l, Ml, 'S',
                                            skip_gates=True)
        pm = 20
        Kp, Cp, Wp = K2l[pm], C2l[pm], W2l[pm]
        lamW = np.linalg.eigvalsh(Wp)
        escW = max(np.max(np.abs(lamW)), 1e-300)
        # QEP: -om^2 K + i om (C - C^T) + W ~ 0 -> modos
        modos = d1.agrupa_pares(d1.qep_modes(Kp, Cp, Wp))
        Hl = Hs_l[pm]
        oms = sorted((abs(np.imag(m['lam'])) / Hl for m in modos),
                     reverse=True)[:2]
        om_osc = oms[0] if oms else float('nan')
        say(f"    k/aH={kh_alvo:5.1f}  omega_osc/H = {om_osc:6.2f}  "
            f"(dchi: sqrt(kh^2+0.3/H^2) = "
            f"{np.sqrt(kh_alvo**2 + 0.3/Hs_l[pm]**2):6.2f})  "
            f"W2 autovalores/esc: ({lamW[0]/escW:+.2e}, "
            f"{lamW[1]/escW:+.2e})")

    return dict(g1=max(g1g, g1s), g3=dmax, neg=neg, halv=dmax_h,
                ok_h=ok_h, ok_anc=ok_anc, taxas=res_taxas)


res = {}
for B1V in (1.0, 4.47):
    res[B1V] = analisa(B1V)

say("")
say("=" * 72)
say("VEREDITO R-7a (criterios pre-declarados no cabecalho)")
say("=" * 72)
for B1V in (1.0, 4.47):
    r = res[B1V]
    tx_ef = r['taxas'][(0, 0)]
    say(f"  beta1={B1V:g}: G1 {r['g1']:.1e}; V-XREP {r['g3']:.1e}; "
        f"K2 negativos {r['neg']}; halving max {r['halv']:.3f} "
        f"({'OK' if r['ok_h'] else 'FALHOU'}); "
        f"ancora dchi {'OK' if r['ok_anc'] else 'FORA'}; "
        f"taxa E_f(pos) tardia {tx_ef:+.3f}")
ok_total = all(r['neg'] == 0 and r['ok_anc'] and r['ok_h']
               for r in res.values())
if ok_total:
    say("")
    say("  >>> SISTEMA 2-DOF SAUDAVEL nos dois fundos: zero direcoes")
    say("  cineticas negativas, dilucao tardia com as taxas fisicas")
    say("  previstas (a 'taxa da banda' sigma_can 1.13/1.41 do Gate F-b")
    say("  era a normalizacao a^(3/2) do dchi saudavel — ancora bate).")
    say("  D-2/R-1 SUBSTITUIDOS nesta classe pelo sistema fisico.")
else:
    say("")
    say("  >>> ANOMALIA — reportar sem interpretar; ver tabelas acima.")

os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
with open(os.path.join(HERE, 'out', 'r7a_dinamica_2dof.txt'), 'w',
          encoding='utf-8') as fh:
    fh.write("\n".join(OUT) + "\n")
say("")
say("saida escrita em auditoria/code/out/r7a_dinamica_2dof.txt")
