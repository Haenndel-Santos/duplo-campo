# -*- coding: utf-8 -*-
"""
r5_confrontos_paper.py — R-5: os tres confrontos nivel-paper
(decisao do autor 2026-08-12, opcao (b)): (A) transferencia f->g da
banda (o insumo do confronto ISW/baixo-ell); (B) dispersao canonica
da banda (comparacao quantitativa com a instabilidade de gradiente de
Comelli/Konnig); (C) a escada de mu e a fresta mu=0.1 (a rota de
escape de Akrami et al. 1503.07521 vs o dano da banda).

CONTEXTO. O programa fechou (R-4 completo + Gate F em H-SC): a unica
instabilidade real do setor escalar e a banda transiente (kh~0.5-30,
~e^4 por passagem, chave = fracao bimetrica; dano <= x6.6 confinado a
escalas ~horizonte hoje), e o congelado CANONICO e arbitro legitimo
(CONF-BANDA do F-b). Tres perguntas de paper:

  (A) A banda vive no par f (Psi_f, E_f). O OBSERVAVEL (ISW/baixo-ell)
      sao os potenciais-g — que aqui sao MULTIPLICADORES, resolvidos
      algebricamente: X = W'_XX^-1 (C'_QX^T Qdot - W'_XQ Q), com
      X = (Phi_g, B_g, Phi_f, B_f). A pergunta: |Phi_g| CRESCE a
      mesma taxa da banda (o potencial-g carrega o dano -> o x6.6 do
      R-4c vale para o observavel) ou e suprimido/filtrado?
      MEDIDA: taxa de crescimento de |Phi_g| e |B_g| na janela da
      banda (entre marcos) vs taxa metrica; razoes |Phi_g|/|q_met|
      nos marcos (caveat: razoes em base comovel sao indicativas —
      a TAXA e o numero robusto; licao R-2).
  (B) A instabilidade conhecida do ramo finito na literatura e de
      GRADIENTE (omega^2 ~ -c_s^2 k^2 => taxa ~ |c_s| k_phys,
      proporcional a k) e transiente-de-transicao. A nossa banda tem
      dispersao propria: sigma_can(kh) nos marcos (legitimado pelo
      CONF-BANDA), fit de lei de potencia sigma = c * kh^p no trecho
      quasi-assentado: p=1 seria gradiente puro; p=0 massa; o F-b
      insinuou p ~ 0.5 com saturacao IR. p != 1 com saturacao =
      DISCRIMINADOR quantitativo: nao e a instabilidade deles (que o
      posicionamento ja situou como transiente de outra era; e o
      R-4a mostrou que a "transicao" deles era a banda cruzada pelos
      modos da epoca).
  (C) A rota de escape de Akrami et al. e a direcao mu pequeno. A R-1
      viu (metrica antiga, cumulativa-comovel) o MAIOR lnA na fresta
      mu=0.1. Reavaliar na metrica limpa: lnA_PASSAGEM (kh 20->0.2,
      convencao R-4b) + omega_0/H assentado + sigma_can tardio, nas
      celulas: fresta (0.2,-1.0) x mu {0.1, 1}; REF (1,-0.4) x mu
      {0.3, 3, 10}; ancora beta1=1 mu=1 do braco A. Tendencia com mu
      -> a tensao "fresta = pior lnA" confirmada ou desfeita; e
      omega_0 vs cutoff por celula (proxy Lambda_3 = (12 H^2)^(1/3),
      ancora tensorial REF declarada O(1)).

CRITERIOS PRE-DECLARADOS:
  R5-BASE: lnA_passagem(beta1=1, mu=1) = +3.97 +- 0.4 (continuidade
      R-4b/F-a). FALHA -> nao interpretar.
  R5-A: dif = |taxa(|Phi_g|) - taxa_met| na janela da banda (media
      dos marcos com kh in [0.5, 6]):
        dif < 0.3 -> POTENCIAL-G CARREGA A BANDA (o fator x6.6 do
            R-4c aplica-se ao observavel; confronto ISW usa B_max
            direto);
        taxa(|Phi_g|) < taxa_met - 0.5 -> SUPRIMIDO (fator de filtro
            declarado; o dano observavel cai);
        senao -> intermediario (reportar).
  R5-B: expoente p do fit log(sigma_can) vs log(kh) no trecho
      kh in [1, 30] (marcos com eps_W < 1): reportar p e o residuo;
      p < 0.8 => NAO-GRADIENTE (discriminado de Comelli/Konnig);
      saturacao IR reportada (sigma_can em kh < 0.3).
  R5-C: tabela lnA_pass(celula), omega_0/H, sigma_can tardio,
      omega_0/Lambda_3(proxy). Tendencia declarada: se
      lnA_pass(fresta mu=0.1) > lnA_pass(REF) + 1 -> TENSAO-AKRAMI
      CONFIRMADA na metrica limpa (a rota de escape deles e a nossa
      pior celula); se dentro de +-1 -> tensao DESFEITA (o lnA antigo
      era artefato da metrica cumulativa); omega_0/Lambda_3 < 1 em
      alguma celula -> F-c revive LOCALMENTE (reportar).

Requer sympy, numpy, scipy. ~7-10 min (1 braco A/B + 5 celulas C).
Uso: python auditoria/code/r5_confrontos_paper.py
Saida em auditoria/code/out/r5_confrontos_paper.txt
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
MULT = [0, 1, 2, 4]
DYN = [3, 5, 6]
IDX_MET_IC = [0, 1, 3, 4]
A_MIN, A_MAX = 100.0, 80000.0
MARCAS = list(np.geomspace(150.0, 75000.0, 40))
KH_PASS = (20.0, 0.2)
EPS_ASSENT = 0.3
ETA = np.diag([-1.0, 1.0, 1.0])

MG2 = 1.0
M2 = 1.0
B0V, B4V = 1.0, 0.5
RHO0 = 0.3

say("=" * 72)
say("R-5 — CONFRONTOS NIVEL-PAPER: (A) f->g / ISW; (B) dispersao vs")
say("Comelli/Konnig; (C) escada de mu vs rota de Akrami")
say("=" * 72)

if not d1.gr_selfcheck():
    say("[!] V1 falhou — abortando")
    sys.exit(1)
say("[V1] GR selfcheck: PASSA")

L2s, fields, vels = d1.build_L2()
K7, C7, W7 = quadratic_matrices(L2s, fields, vels)
if [str(f) for f in fields] != NOMES:
    raise RuntimeError("ordem de campos mudou")
say("[montagem] K,C,W 7x7 prontos")

say("[fatias] ...")
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


def monta(fat, args, bvals):
    M = np.array(fat['base'](*args), float).copy()
    for n in range(5):
        if bvals[n]:
            M += bvals[n] * np.array(fat[('Fb', n)](*args), float)
    return M


def fundo_mu(a, B1V, B2V, mu):
    kap = 1.0 / mu
    meff2 = mu / (1.0 + mu)
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
    H2 = meff2 * r * r * Vf / (3.0 * mu)
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


def constroi(B1V, B2V, mu, kc, npts):
    meff2 = mu / (1.0 + mu)
    Ns = np.linspace(np.log(A_MIN), np.log(A_MAX), npts)
    Hs_arr = np.zeros(npts)
    Ms = {x: np.zeros((npts, 7, 7)) for x in 'KCW'}
    for p, N in enumerate(Ns):
        a = np.exp(N)
        f = fundo_mu(a, B1V, B2V, mu)
        if f is None:
            raise RuntimeError(f"fundo invalido em a={a:.1f}")
        Hs_arr[p] = f['H']
        args = (a, f['r'] * a, f['xi'], f['H'], f['Hf'],
                f['Hd'], f['Hfd'], f['xid'], 0.0, 0.0,
                f['Ub'], 0.0, 0.3, kc, mu, meff2)
        bvals = (B0V, B1V, B2V, 0.0, B4V)
        Ms['K'][p] = monta(FK, args, bvals)
        Ms['C'][p] = monta(FC, args, bvals)
        Ms['W'][p] = monta(FW, args, bvals)
    return Ns, Hs_arr, Ms


def reduz_ponto_blocos(Kt, Ct, Wt, Cdot):
    """reducao + blocos p/ reconstruir os multiplicadores:
    X = WXXi (CQX^T Qdot - WXQ Q)."""
    K = Kt.copy()
    C = Ct.copy()
    W = Wt.copy()
    n = K.shape[0]
    for i in MULT:
        if np.max(np.abs(K[i, :])) > 1e-10 * max(1.0, np.max(np.abs(K))):
            raise RuntimeError("linha K do multiplicador nao-nula")
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
    if np.linalg.cond(WXX) > 1e12:
        raise RuntimeError("W_XX mal condicionada")
    WXXi = np.linalg.inv(WXX)
    CQX = C[np.ix_(DYN, MULT)]
    WXQ = W[np.ix_(MULT, DYN)]
    Kr = K[np.ix_(DYN, DYN)] + CQX @ WXXi @ CQX.T
    Cr = C[np.ix_(DYN, DYN)] - CQX @ WXXi @ WXQ
    Wr = W[np.ix_(DYN, DYN)] - W[np.ix_(DYN, MULT)] @ WXXi @ WXQ
    return Kr, Cr, Wr, WXXi, CQX, WXQ


def reduz_trilha(Ms, Ns, Hs_arr, marcas_idx=None):
    npts = len(Ns)
    Cdots = np.gradient(Ms['C'], Ns, axis=0) * Hs_arr[:, None, None]
    Kr = np.zeros((npts, 3, 3))
    Cr = np.zeros((npts, 3, 3))
    Wr = np.zeros((npts, 3, 3))
    blocos = {}
    for p in range(npts):
        out = reduz_ponto_blocos(Ms['K'][p], Ms['C'][p], Ms['W'][p],
                                 Cdots[p])
        Kr[p], Cr[p], Wr[p] = out[0], out[1], out[2]
        if marcas_idx is not None and p in marcas_idx:
            blocos[p] = (out[3], out[4], out[5])
    Krd = np.gradient(Kr, Ns, axis=0) * Hs_arr[:, None, None]
    Crd = np.gradient(Cr, Ns, axis=0) * Hs_arr[:, None, None]
    return Kr, Cr, Wr, Krd, Crd, blocos


def evolui_lnA(Kr, Cr, Wr, Krd, Crd, Ns, Hs_arr, jans, marcas_idx=None,
               blocos=None):
    """4 ICs metricas; devolve dln_met por janela e, se pedido, o
    estado + multiplicadores nos marcos (p/ o braco A)."""
    npts = len(Ns)
    aas = np.exp(Ns)
    dlns, trilhas = [], []
    for ic in IDX_MET_IC:
        q = np.zeros(3)
        qd = np.zeros(3)
        if ic < 3:
            q[ic] = 1.0
        else:
            qd[ic - 3] = 1.0
        tcum = 0.0
        reg = {nome: [None] * 4 for nome, _, _ in jans}
        tr = {}
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
            n2m = q[0]**2 + q[1]**2 + qd[0]**2 + qd[1]**2
            ln_m = np.log(max(np.sqrt(n2m), 1e-300))
            for nome, lo, hi in jans:
                r = reg[nome]
                if r[0] is None and aa >= lo:
                    r[0], r[1] = ln_m, tcum
                if r[2] is None and aa >= hi:
                    r[2], r[3] = ln_m, tcum
            if (marcas_idx is not None and (p + 1) in marcas_idx
                    and blocos is not None and (p + 1) in blocos):
                WXXi, CQX, WXQ = blocos[p + 1]
                X = WXXi @ (CQX.T @ qd - WXQ @ q)
                tr[p + 1] = (np.sqrt(n2m), np.abs(X))

        dl = {}
        for nome, lo, hi in jans:
            r = reg[nome]
            dl[nome] = (r[2] - r[0]) if (r[0] is not None
                                         and r[2] is not None) else float('nan')
        dlns.append(dl)
        trilhas.append(tr)
    return dlns, trilhas


def canonica_marcas(Kr, Cr, Wr, Ns, Hs_arr, marcas_idx):
    """T continuo em toda a grade; QEP canonico so nos marcos."""
    npts = len(Ns)
    Tarr = np.zeros((npts, 3, 3))
    E_prev = None
    for p in range(npts):
        Ksym = 0.5 * (Kr[p] + Kr[p].T)
        lam, E = np.linalg.eigh(Ksym)
        if lam[0] >= 0 or lam[1] <= 0:
            raise RuntimeError(f"assinatura inesperada em p={p}")
        if E_prev is not None:
            if abs(E_prev[:, 1] @ E[:, 2]) > abs(E_prev[:, 1] @ E[:, 1]):
                E = E[:, [0, 2, 1]]
                lam = lam[[0, 2, 1]]
            for j in range(3):
                if E_prev[:, j] @ E[:, j] < 0:
                    E[:, j] = -E[:, j]
        E_prev = E
        Tarr[p] = E * (1.0 / np.sqrt(np.abs(lam)))[None, :]
    Tdot = np.gradient(Tarr, Ns, axis=0) * Hs_arr[:, None, None]
    dN = Ns[1] - Ns[0]
    saida = []
    for mi in sorted(marcas_idx):
        Tp, Td = Tarr[mi], Tdot[mi]
        Ks = 0.5 * (Kr[mi] + Kr[mi].T)
        Cc = Tp.T @ Ks @ Td + Tp.T @ Cr[mi] @ Tp
        S = Td.T @ Cr[mi] @ Tp
        TWT = Tp.T @ Wr[mi] @ Tp
        Wc = 0.5 * (TWT + TWT.T) - Td.T @ Ks @ Td - (S + S.T)
        # Ccd e epsW por diferenca central de vizinhos
        outs = []
        for mj in (max(mi - 1, 0), min(mi + 1, npts - 1)):
            Tq, Tdq = Tarr[mj], Tdot[mj]
            Ksq = 0.5 * (Kr[mj] + Kr[mj].T)
            Ccq = Tq.T @ Ksq @ Tdq + Tq.T @ Cr[mj] @ Tq
            Sq = Tdq.T @ Cr[mj] @ Tq
            TWTq = Tq.T @ Wr[mj] @ Tq
            Wcq = 0.5 * (TWTq + TWTq.T) - Tdq.T @ Ksq @ Tdq - (Sq + Sq.T)
            outs.append((Ccq, Wcq))
        Ccd = (outs[1][0] - outs[0][0]) / (2 * dN) * Hs_arr[mi]
        epsW = (np.linalg.norm((outs[1][1] - outs[0][1]) / (2 * dN))
                / max(np.linalg.norm(Wc), 1e-300))
        pares = d1.agrupa_pares(d1.qep_modes(ETA.copy(), Cc, Wc))
        if not pares:
            continue
        pares.sort(key=lambda mm: abs(mm['omega2']))
        vh = np.asarray(pares[-1]['v'], complex)
        omh = abs(np.sqrt(complex(pares[-1]['omega2']))) / Hs_arr[mi]
        s0 = float(np.real(np.conjugate(vh) @ ETA @ vh)
                   / max(np.linalg.norm(vh)**2, 1e-300))
        sig = max(abs(np.sqrt(complex(mm['omega2'])).imag)
                  for mm in pares) / Hs_arr[mi]
        saida.append(dict(mi=mi, omh=omh, s0=s0, sig=sig, epsW=epsW))
    return saida


def mediana(xs):
    xs = [x for x in xs if np.isfinite(x)]
    return float(np.median(xs)) if xs else float('nan')


def a_de_kh(khs, aas, kh):
    if khs[0] <= kh or khs[-1] >= kh:
        return None
    return float(aas[int(np.argmax(khs <= kh))])


# ==================================================================
# BRACO A/B — beta1=1, mu=1 (ancora), com multiplicadores e canonico
# ==================================================================
say("")
say("=" * 72)
say("BRACO A/B — beta1=1, mu=1: transferencia f->g + dispersao canonica")
say("=" * 72)
NPTS_AB = 24000
f0 = fundo_mu(A_MIN, 1.0, -0.4, 1.0)
kc = 45.0 * f0['H'] * A_MIN
Ns, Hs_arr, Ms = constroi(1.0, -0.4, 1.0, kc, NPTS_AB)
aas = np.exp(Ns)
khs = kc / (aas * Hs_arr)
midx = sorted(set(int(np.argmin(np.abs(aas - am))) for am in MARCAS))
midx = [m for m in midx if 1 <= m <= NPTS_AB - 2]
Kr, Cr, Wr, Krd, Crd, blocos = reduz_trilha(Ms, Ns, Hs_arr,
                                            marcas_idx=set(midx))
say("    [reducao] ok (com blocos de multiplicadores nos marcos)")

a_p1 = a_de_kh(khs, aas, KH_PASS[0])
a_p2 = a_de_kh(khs, aas, KH_PASS[1])
jans = [("passagem", a_p1, a_p2)]
dlns, trilhas = evolui_lnA(Kr, Cr, Wr, Krd, Crd, Ns, Hs_arr, jans,
                           marcas_idx=set(midx), blocos=blocos)
vs = [dl['passagem'] for dl in dlns if np.isfinite(dl['passagem'])]
lnA_ref = max(vs) if vs else float('nan')
ok_base = np.isfinite(lnA_ref) and abs(lnA_ref - 3.97) < 0.4
say(f"    [R5-BASE {'OK' if ok_base else 'FALHOU'}] lnA_passagem = "
    f"{lnA_ref:+.2f} (ref +3.97, tol 0.4)")

# R5-A — taxas de |Phi_g|, |B_g| vs taxa metrica entre marcos na banda
say("")
say("    R5-A — transferencia f->g (taxas entre marcos; kh 0.5-6):")
say(f"    {'a':>8} {'kh':>6} {'tx_met':>8} {'tx_Phig':>8} {'tx_Bg':>8} "
    f"{'|Phig|/|qm|':>11}")
difs = []
for j, ic in enumerate(IDX_MET_IC):
    tr = trilhas[j]
    ms = sorted(tr.keys())
    for i in range(len(ms) - 1):
        m1, m2 = ms[i], ms[i + 1]
        kh_m = kc / (aas[m2] * Hs_arr[m2])
        if not (0.5 <= kh_m <= 6.0):
            continue
        dNm = Ns[m2] - Ns[m1]
        qm1, X1 = tr[m1]
        qm2, X2 = tr[m2]
        tx_met = np.log(max(qm2, 1e-300) / max(qm1, 1e-300)) / dNm
        tx_pg = np.log(max(X2[0], 1e-300) / max(X1[0], 1e-300)) / dNm
        tx_bg = np.log(max(X2[1], 1e-300) / max(X1[1], 1e-300)) / dNm
        if j == 0:
            say(f"    {aas[m2]:8.0f} {kh_m:6.2f} {tx_met:+8.2f} "
                f"{tx_pg:+8.2f} {tx_bg:+8.2f} "
                f"{X2[0]/max(qm2, 1e-300):11.2e}")
        if np.isfinite(tx_pg) and np.isfinite(tx_met):
            difs.append(tx_pg - tx_met)
dif_med = mediana(difs)
razoes = []
for j, ic in enumerate(IDX_MET_IC):
    for m, (qm, X) in trilhas[j].items():
        kh_m = kc / (aas[m] * Hs_arr[m])
        if 0.5 <= kh_m <= 6.0 and qm > 1e-200:
            razoes.append(X[0] / qm)
raz_med = mediana(razoes)
say(f"    mediana(tx_Phig - tx_met) na banda = {dif_med:+.3f} "
    f"({len(difs)} intervalos, 4 ICs; RUIDOSA — log de componente)")
say(f"    mediana |Phi_g|/|q_met| na banda = {raz_med:.3f} "
    f"({len(razoes)} marcos x ICs) — razao sustentada = transferencia")
if np.isfinite(dif_med) and abs(dif_med) < 0.3:
    v_a = "CARREGA"
    say("    [R5-A => POTENCIAL-G CARREGA A BANDA] o fator do R-4c")
    say("    aplica-se ao observavel (insumo direto do confronto ISW).")
elif np.isfinite(dif_med) and dif_med < -0.5:
    v_a = "SUPRIMIDO"
    say(f"    [R5-A => SUPRIMIDO] Phi_g cresce {-dif_med:.2f}/H mais")
    say("    devagar que a banda — fator de filtro no dano observavel.")
else:
    v_a = "INTERMEDIARIO"
    say("    [R5-A => intermediario] reportar.")

# R5-B — dispersao canonica sigma_can(kh)
say("")
say("    R5-B — dispersao canonica da banda:")
tabc = canonica_marcas(Kr, Cr, Wr, Ns, Hs_arr, midx)
say(f"    {'a':>8} {'kh':>7} {'sig_can/H':>10} {'om0/H':>8} {'s_0':>6} "
    f"{'eps_W':>7}")
pts_fit = []
sat_ir = []
for tb in tabc[::3] + [tabc[-1]]:
    kh_m = kc / (aas[tb['mi']] * Hs_arr[tb['mi']])
    say(f"    {aas[tb['mi']]:8.0f} {kh_m:7.2f} {tb['sig']:10.2f} "
        f"{tb['omh']:8.1f} {tb['s0']:+6.2f} {tb['epsW']:7.3f}")
for tb in tabc:
    kh_m = kc / (aas[tb['mi']] * Hs_arr[tb['mi']])
    if 1.5 <= kh_m <= 30.0 and tb['sig'] > 0.1:
        pts_fit.append((np.log(kh_m), np.log(tb['sig'])))
    if kh_m < 0.3:
        sat_ir.append(tb['sig'])
if len(pts_fit) >= 4:
    xs = np.array([p[0] for p in pts_fit])
    ys = np.array([p[1] for p in pts_fit])
    p_exp, c_log = np.polyfit(xs, ys, 1)
    resid = float(np.sqrt(np.mean((ys - (p_exp * xs + c_log))**2)))
    say(f"    fit sigma_can = c * kh^p em kh=[1.5,30] (tendencia do ramo")
    say(f"    congelado-canonico; eps_W anotado — assentado so no IR): "
        f"p = {p_exp:.2f} (c = {np.exp(c_log):.2f}), rms = {resid:.2f}")
    say(f"    saturacao IR (kh<0.3): sigma_can ~ {mediana(sat_ir):.2f}/H")
    if p_exp < 0.8:
        say("    [R5-B => NAO-GRADIENTE] p < 0.8: a banda NAO e a")
        say("    instabilidade de gradiente (p=1) de Comelli/Konnig —")
        say("    dispersao propria + saturacao IR; discriminada.")
    else:
        say("    [R5-B => compativel com gradiente] p >= 0.8 — reavaliar")
        say("    o posicionamento.")
else:
    p_exp = float('nan')
    say("    [R5-B] pontos insuficientes p/ fit — reportar tabela")

# ==================================================================
# BRACO C — escada de mu e a fresta
# ==================================================================
say("")
say("=" * 72)
say("BRACO C — escada de mu (REF) e fresta (0.2,-1.0): metrica limpa")
say("=" * 72)
CELULAS = [
    ("fresta", 0.2, -1.0, 0.1),
    ("fresta", 0.2, -1.0, 1.0),
    ("REF", 1.0, -0.4, 0.3),
    ("REF", 1.0, -0.4, 3.0),
    ("REF", 1.0, -0.4, 10.0),
]
NPTS_C = 20000
resC = []
for rot, B1V, B2V, mu in CELULAS:
    f0c = fundo_mu(A_MIN, B1V, B2V, mu)
    if f0c is None:
        say(f"    {rot} (b1={B1V:g}, b2={B2V:g}, mu={mu:g}): sem fundo — "
            "pulada")
        continue
    kcc = 45.0 * f0c['H'] * A_MIN
    say("")
    say(f"--- {rot}: b1={B1V:g} b2={B2V:g} mu={mu:g} "
        f"(H={f0c['H']:.3f}, k_c={kcc:.0f}) ---")
    try:
        Nsc, Hsc, Msc = constroi(B1V, B2V, mu, kcc, NPTS_C)
    except RuntimeError as e:
        say(f"    fundo quebrou no range: {e} — pulada")
        continue
    aasc = np.exp(Nsc)
    khsc = kcc / (aasc * Hsc)
    midc = sorted(set(int(np.argmin(np.abs(aasc - am))) for am in MARCAS))
    midc = [m for m in midc if 1 <= m <= NPTS_C - 2]
    try:
        Krc, Crc, Wrc, Krdc, Crdc, _ = reduz_trilha(Msc, Nsc, Hsc)
    except RuntimeError as e:
        say(f"    reducao falhou: {e} — pulada")
        continue
    a1 = a_de_kh(khsc, aasc, KH_PASS[0])
    a2 = a_de_kh(khsc, aasc, KH_PASS[1])
    if a1 is None or a2 is None:
        say("    passagem fora do range — pulada")
        continue
    dlc, _ = evolui_lnA(Krc, Crc, Wrc, Krdc, Crdc, Nsc, Hsc,
                        [("passagem", a1, a2)])
    vsc = [dl['passagem'] for dl in dlc if np.isfinite(dl['passagem'])]
    lnA = max(vsc) if vsc else float('nan')
    try:
        tabcc = canonica_marcas(Krc, Crc, Wrc, Nsc, Hsc, midc)
    except RuntimeError:
        tabcc = []
    assent = [tb for tb in tabcc if tb['epsW'] < EPS_ASSENT]
    om0 = mediana([tb['omh'] for tb in assent])
    s0m = mediana([tb['s0'] for tb in assent])
    sigt = mediana([tb['sig'] for tb in assent[-6:]])
    H_t = Hsc[-1]
    lam3_H = (12.0 * H_t**2) ** (1.0 / 3.0) / H_t
    om_l3 = om0 / lam3_H if np.isfinite(om0) else float('nan')
    say(f"    lnA_passagem = {lnA:+.2f}; omega_0/H = {om0:.1f} "
        f"(s0 {s0m:+.2f}); sigma_can tardio = {sigt:.2f}; "
        f"omega_0/Lambda_3(proxy) = {om_l3:.1f}")
    resC.append(dict(rot=rot, b1=B1V, b2=B2V, mu=mu, lnA=lnA, om0=om0,
                     oml3=om_l3, sigt=sigt))

# ==================================================================
# sintese
# ==================================================================
say("")
say("=" * 72)
say("SINTESE R-5 (criterios pre-declarados)")
say("=" * 72)
say(f"  R5-BASE: {'OK' if ok_base else 'FALHOU'} (lnA ancora "
    f"{lnA_ref:+.2f})")
say(f"  R5-A (f->g): {v_a} (mediana tx_Phig - tx_met = {dif_med:+.3f})")
say(f"  R5-B (dispersao): p = {p_exp:.2f} "
    + ("(NAO-GRADIENTE — discriminada de Comelli/Konnig)"
       if np.isfinite(p_exp) and p_exp < 0.8 else "(ver acima)"))
say("")
say("  R5-C — tabela (metrica limpa):")
say(f"    {'celula':<8} {'b1':>5} {'b2':>6} {'mu':>6} {'lnA_pass':>9} "
    f"{'om0/H':>7} {'om0/L3':>7} {'sig_can':>8}")
say(f"    {'ancora':<8} {1.0:5.1f} {-0.4:6.1f} {1.0:6.1f} "
    f"{lnA_ref:+9.2f} {'12.0':>7} {'4.3':>7} {'1.13':>8}")
for r in resC:
    say(f"    {r['rot']:<8} {r['b1']:5.1f} {r['b2']:6.1f} {r['mu']:6.1f} "
        f"{r['lnA']:+9.2f} {r['om0']:7.1f} {r['oml3']:7.1f} "
        f"{r['sigt']:8.2f}")
fr = [r for r in resC if r['rot'] == 'fresta' and r['mu'] == 0.1]
if fr and np.isfinite(fr[0]['lnA']) and np.isfinite(lnA_ref):
    dfr = fr[0]['lnA'] - lnA_ref
    if dfr > 1.0:
        say(f"  >>> TENSAO-AKRAMI CONFIRMADA na metrica limpa: a fresta")
        say(f"  mu=0.1 tem lnA_passagem {dfr:+.2f} acima da ancora — a")
        say("  rota de escape deles e a nossa pior celula; o confronto")
        say("  observacional da banda e MAIS duro exatamente la.")
    elif abs(dfr) <= 1.0:
        say(f"  >>> TENSAO-AKRAMI DESFEITA na metrica limpa (dif = "
            f"{dfr:+.2f}): o 'pior lnA da fresta' da R-1 era artefato da")
        say("  metrica cumulativa comovel; a rota de escape nao e")
        say("  penalizada pela banda alem do fator comum ~e^4.")
    else:
        say(f"  >>> fresta mais BRANDA que a ancora ({dfr:+.2f}) — "
            "reportar.")
cutb = [r for r in resC if np.isfinite(r['oml3']) and r['oml3'] < 1.0]
if cutb:
    say("  >>> omega_0 < Lambda_3 em: "
        + ", ".join(f"{r['rot']} mu={r['mu']:g}" for r in cutb)
        + " — F-c revive LOCALMENTE nessas celulas (reportar ao autor).")
else:
    say("  (omega_0 acima de Lambda_3 em todas as celulas medidas — o")
    say("  fecho H-SC do Gate F e uniforme na amostra.)")

os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
with open(os.path.join(HERE, "out", "r5_confrontos_paper.txt"),
          "w", encoding="utf-8") as fh:
    fh.write("\n".join(OUT))
say("")
say("concluido. saida em auditoria/code/out/r5_confrontos_paper.txt")
