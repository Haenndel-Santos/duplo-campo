# -*- coding: utf-8 -*-
"""
gatef_b_canonica.py — GATE F, etapa F-b: normalizacao canonica
dependente do tempo (docs/gate_fantasma_estrutural.md sec.2) — decide
H-CONSTRAINT / H-NORM / H-SC / (H-GHOST -> F-c) para a direcao K<0.

2a RODADA (2026-08-12): ARQUITETURA CORRIGIDA apos a autopsia da 1a
(preservada em out/gatef_b_canonica_rodada1.txt). Na 1a, o portao
V-EQUIV reprovou (como devia): a IC de VELOCIDADE bateu a 3.5e-4
entre os dois quadros (a dinamica canonica estava certa), mas as ICs
de POSICAO divergiram O(1)-O(10) — o padrao de decoerencia do modo
rapido entre DUAS integracoes independentes + sensibilidade do
mapeamento de IC a Tdot na borda. A dupla integracao era fragilidade
de desenho, nao fisica. A v2 elimina a classe inteira de erro:
  - UMA UNICA integracao, no quadro ORIGINAL (o integrador validado
    por halving desde o D2);
  - o quadro canonico e usado SO como diagnostico LOCAL, por
    transformacao nos marcos: x = T^-1 q; xd = T^-1 (qd - Tdot x);
  - a validacao vira o V-RES: o residuo da EOM canonica avaliado na
    trajetoria real transformada (tres pontos de grade por marco,
    derivada central) — valida exatamente o que os diagnosticos usam
    (C_can, W_can, Tdot), localmente, sem acumulacao.
Achados da 1a rodada que motivam medidas da v2 (registrados como
NAO-interpretados la): o modo pesado tardio parecia viver no eixo x0
com norma-eta ~ -0.98 a omega ~ 7-12 H, SEM hierarquia de vinculo
(R_can ~ 5-10 — o omega^2 ~ 1e9 comovel do R-2 era artefato de
normalizacao), e o congelado CANONICO parecia assentar (eps_W -> 0.01)
com sigma_can ~ 1.1-1.4 ~ as taxas reais da banda. A v2 mede tudo
isso com validacao propria.

CONSTRUCAO (a licao do D2 — nunca descartar termos de conexao):
  T(t) = E(t) |Lambda(t)|^(-1/2), com E,Lambda de eigh(K_red_sym) e
  CONTINUIDADE forcada (sinais + permutacao do par positivo; a
  direcao negativa nao cruza — negK=1 universal).
  K_can = eta = diag(-1,+1,+1) (exato);
  C_can = T'K Tdot + T'CT;
  W_can = sym(T'WT) - Tdot'K Tdot - (Tdot'CT + T'C'Tdot).

FUNDOS: estaticos beta1=1 e beta1=4.47 (par antes/depois com o F-a),
k_c = 45*H(100)*100, a=[100,80000], npts=24000.

VALIDACOES (pre-declaradas; falha -> NAO INTERPRETAR):
  V-ETA: max|T'KT - eta| < 1e-8 na grade inteira.
  V-RES (o portao central da v2): residuo relativo da EOM canonica
      sobre a trajetoria real transformada, mediana das 3 ICs
      fisicas por marco: max sobre os marcos < 0.1.
  V-EQUIV-GR: dupla integracao em GR (1 dof, T=1/sqrt(K)) < 0.05 —
      sanidade do pipeline (passou na 1a: 3.2e-5).

MEDIDAS (marcos ASSENTADOS: eps_W = |dW_can/dN|/|W_can| < 0.3 — no
quadro canonico K_can e constante, entao o congelado e legitimo onde
C_can/W_can assentam; a 1a rodada indicou assentamento tardio):
  F-b1a (hierarquia de vinculo): R_can = |om_h|/max(|om_2|,H) do QEP
      canonico: R_final >= 100 crescente -> leitura H-CONSTRAINT.
      (A 1a rodada indicou R ~ 5-10 — sem hierarquia; se confirmar,
      H-CONSTRAINT cai DE VERDADE, em coordenadas validas.)
  F-b1b (identidade): conteudo x0 do modo pesado, mediana > 0.9 nos
      marcos assentados.
  F-b1c (superficie): 4 ICs sobre a superficie adiabatica de x0
      construidas no 1o marco assentado, evoluidas no quadro ORIGINAL
      e transformadas: mediana delta_rel < 0.1; PODER abortivo (eixo
      leve x2 tem que reprovar, >= 0.3); DESAC diagnostico.
  F-b2 (escala invariante): omega_0/H nos marcos vs {H, m_T/H ~ 3.5,
      Lambda_3 ~ O(1)}; sqrt|W_can[0,0]|/H.
  F-b-NORMA: modo PROPAGANTE (|om|/H < 50, ~real) com norma-eta
      s = Re(v† eta v) < -0.1 nos marcos assentados?
  CONF-BANDA (bonus, reabilitacao do congelado): sigma_can/H tardio
      vs a taxa real da banda (R-4a: +0.93 em beta1=1; +1.06 em
      4.47): |dif| < 0.5 -> o congelado CANONICO preve a banda (fecha
      o aviso metodologico do paper).

RAMOS (pre-declarados, sec.3 do gate doc):
  b1a+b1b+b1c SIM (PODER ok) -> H-CONSTRAINT em coordenadas validas;
      gate fecha saudavel (fantasma = representacao).
  Sem hierarquia (b1a NAO) e omega_0/H >= 50 -> H-SC (fora do alcance
      quadratico).
  Sem hierarquia, omega_0/H < 50, e F-b-NORMA acha modo propagante
      s<0 -> FANTASMA FISICO NO ESPECTRO LINEAR, com energia
      invariante ~ omega_0 — o ramo F-c (interacoes / taxa de
      decaimento) ou a fronteira declarada do paper; decidir com o
      autor (o gate doc preve ambos).
  Senao -> H-NORM/misto: reportar e decidir com o autor.

Requer sympy, numpy, scipy. ~5-8 min.
Uso (raiz do repo, venv ativo):
    python auditoria/code/gatef_b_canonica.py
Saida em auditoria/code/out/gatef_b_canonica.txt
(1a rodada preservada em out/gatef_b_canonica_rodada1.txt)
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
A_MIN, A_MAX = 100.0, 80000.0
NPTS = 24000
MARCAS = list(np.geomspace(150.0, 75000.0, 40))
R_HIER = 10.0
EPS_ASSENT = 0.3
ETA = np.diag([-1.0, 1.0, 1.0])
REF_BANDA = {1.0: 0.93, 4.47: 1.06}  # R-4a, braco banda

MU = 1.0
MG2, MF2 = 1.0, MU
ME2 = MU / (1.0 + MU)
M2 = 1.0
B0V, B2V, B4V = 1.0, -0.4, 0.5
RHO0 = 0.3

say("=" * 72)
say("GATE F-b (v2) — QUADRO CANONICO COMO DIAGNOSTICO LOCAL: a energia")
say("invariante da direcao K<0")
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


def builder_bconst(B1V):
    def build(kc, npts):
        Ns = np.linspace(np.log(A_MIN), np.log(A_MAX), npts)
        Hs_arr = np.zeros(npts)
        Ms = {x: np.zeros((npts, 7, 7)) for x in 'KCW'}
        for p, N in enumerate(Ns):
            a = np.exp(N)
            f = fundo_bconst(a, B1V)
            if f is None:
                raise RuntimeError(f"fundo invalido em a={a:.1f}")
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


def reduz_ponto(Kt, Ct, Wt, Cdot, mult, dyn):
    K = Kt.copy()
    C = Ct.copy()
    W = Wt.copy()
    n = K.shape[0]
    for i in mult:
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


def reduz_trilha(Ms, Ns, Hs_arr, mult=None, dyn=None):
    mult = MULT if mult is None else mult
    dyn = DYN if dyn is None else dyn
    nd = len(dyn)
    npts = len(Ns)
    Cdots = np.gradient(Ms['C'], Ns, axis=0) * Hs_arr[:, None, None]
    Kr = np.zeros((npts, nd, nd))
    Cr = np.zeros((npts, nd, nd))
    Wr = np.zeros((npts, nd, nd))
    for p in range(npts):
        Kr[p], Cr[p], Wr[p] = reduz_ponto(
            Ms['K'][p], Ms['C'][p], Ms['W'][p], Cdots[p], mult, dyn)
    Krd = np.gradient(Kr, Ns, axis=0) * Hs_arr[:, None, None]
    Crd = np.gradient(Cr, Ns, axis=0) * Hs_arr[:, None, None]
    return Kr, Cr, Wr, Krd, Crd


def constroi_canonica(Kr, Cr, Wr, Ns, Hs_arr):
    npts = len(Ns)
    Tarr = np.zeros((npts, 3, 3))
    Tinv = np.zeros((npts, 3, 3))
    E_prev = None
    for p in range(npts):
        Ksym = 0.5 * (Kr[p] + Kr[p].T)
        lam, E = np.linalg.eigh(Ksym)
        if lam[0] >= 0 or lam[1] <= 0:
            raise RuntimeError(f"assinatura inesperada em p={p}: {lam}")
        if E_prev is not None:
            if abs(E_prev[:, 1] @ E[:, 2]) > abs(E_prev[:, 1] @ E[:, 1]):
                E = E[:, [0, 2, 1]]
                lam = lam[[0, 2, 1]]
            for j in range(3):
                if E_prev[:, j] @ E[:, j] < 0:
                    E[:, j] = -E[:, j]
        E_prev = E
        s = 1.0 / np.sqrt(np.abs(lam))
        Tarr[p] = E * s[None, :]
        Tinv[p] = (E * (1.0 / s)[None, :]).T
    Tdot = np.gradient(Tarr, Ns, axis=0) * Hs_arr[:, None, None]
    Ccan = np.zeros((npts, 3, 3))
    Wcan = np.zeros((npts, 3, 3))
    err_eta = 0.0
    for p in range(npts):
        Tp, Td = Tarr[p], Tdot[p]
        Ks = 0.5 * (Kr[p] + Kr[p].T)
        err_eta = max(err_eta, float(np.max(np.abs(Tp.T @ Ks @ Tp - ETA))))
        Ccan[p] = Tp.T @ Ks @ Td + Tp.T @ Cr[p] @ Tp
        S = Td.T @ Cr[p] @ Tp
        TWT = Tp.T @ Wr[p] @ Tp
        Wcan[p] = 0.5 * (TWT + TWT.T) - Td.T @ Ks @ Td - (S + S.T)
    Ccd = np.gradient(Ccan, Ns, axis=0) * Hs_arr[:, None, None]
    return Tarr, Tinv, Tdot, Ccan, Wcan, Ccd, err_eta


def evolui_estado(Kr, Cr, Wr, Krd, Crd, Ns, Hs_arr, q0, qd0, mark_idx,
                  p0=0):
    npts = len(Ns)
    q = q0.copy()
    qd = qd0.copy()
    saida = {}
    mset = set(int(m) for m in mark_idx if m > p0)
    for p in range(p0, npts - 1):
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
        if (p + 1) in mset:
            saida[p + 1] = (q.copy(), qd.copy())
    return saida


def qep_can(Cc, Wc):
    return d1.agrupa_pares(d1.qep_modes(ETA.copy(), Cc, Wc))


def mediana(xs):
    xs = [x for x in xs if np.isfinite(x)]
    return float(np.median(xs)) if xs else float('nan')


# ------------------------------------------------------------------
# analise por fundo (v2: integracao unica + diagnostico local)
# ------------------------------------------------------------------
def analisa(B1V):
    say("")
    say("=" * 72)
    say(f"FUNDO beta-constante beta1={B1V:g}")
    say("=" * 72)
    f0 = fundo_bconst(A_MIN, B1V)
    kc = 45.0 * f0['H'] * A_MIN
    Ns = np.linspace(np.log(A_MIN), np.log(A_MAX), NPTS)
    build = builder_bconst(B1V)
    _, Hs_arr, Ms = build(kc, NPTS)
    Kr, Cr, Wr, Krd, Crd = reduz_trilha(Ms, Ns, Hs_arr)
    say("    [reducao] ok; construindo o quadro canonico ...")
    Tarr, Tinv, Tdot, Cc, Wc, Ccd, err_eta = \
        constroi_canonica(Kr, Cr, Wr, Ns, Hs_arr)
    ok_eta = err_eta < 1e-8
    say(f"    [V-ETA {'OK' if ok_eta else 'FALHOU'}] max|T'KT - eta| = "
        f"{err_eta:.2e} (criterio < 1e-8)")
    aas = np.exp(Ns)
    mark_idx = sorted(set(int(np.argmin(np.abs(aas - am)))
                          for am in MARCAS))
    mark_idx = [m for m in mark_idx if 2 <= m <= NPTS - 3]
    req_idx = sorted(set(m + d for m in mark_idx for d in (-1, 0, 1)))

    def para_x(mi, q, qd):
        x = Tinv[mi] @ q
        xd = Tinv[mi] @ (qd - Tdot[mi] @ x)
        return x, xd

    # ICs fisicas — integracao UNICA no quadro original
    ics_fis = [("q_metrica", np.array([1.0, 0, 0]), np.zeros(3)),
               ("qd_metrica", np.zeros(3), np.array([1.0, 0, 0])),
               ("dir_fantasma", Tarr[0] @ np.array([1.0, 0, 0]),
                np.zeros(3))]
    estados = {}
    for rot, q0, qd0 in ics_fis:
        estados[rot] = evolui_estado(Kr, Cr, Wr, Krd, Crd, Ns, Hs_arr,
                                     q0, qd0, req_idx)

    # V-RES — residuo da EOM canonica na trajetoria real transformada
    res_por_marco = []
    for mi in mark_idx:
        rr_ics = []
        for rot, _, _ in ics_fis:
            sq = estados[rot]
            if not all(j in sq for j in (mi - 1, mi, mi + 1)):
                continue
            x_m, xd_m = para_x(mi - 1, *sq[mi - 1])
            x_0, xd_0 = para_x(mi, *sq[mi])
            x_p, xd_p = para_x(mi + 1, *sq[mi + 1])
            dNg = Ns[1] - Ns[0]
            dt_tot = dNg / Hs_arr[mi - 1] + dNg / Hs_arr[mi]
            xdd = (xd_p - xd_m) / dt_tot
            Acan = Cc[mi] - Cc[mi].T
            Bcan = Ccd[mi] + Wc[mi]
            res = ETA @ xdd + Acan @ xd_0 + Bcan @ x_0
            esc = max(np.linalg.norm(ETA @ xdd),
                      np.linalg.norm(Acan @ xd_0),
                      np.linalg.norm(Bcan @ x_0), 1e-300)
            rr_ics.append(np.linalg.norm(res) / esc)
        res_por_marco.append(mediana(rr_ics))
    vres = max([r for r in res_por_marco if np.isfinite(r)],
               default=float('nan'))
    ok_res = np.isfinite(vres) and vres < 0.1
    say(f"    [V-RES {'OK' if ok_res else 'FALHOU — NAO INTERPRETAR'}] "
        f"max mediana do residuo canonico nos marcos = {vres:.3f} "
        "(criterio < 0.1)")

    # QEP canonico nos marcos
    say("")
    say("    F-b1/F-b2 — QEP canonico nos marcos:")
    say(f"    {'a':>8} {'kh':>7} {'om0/H':>9} {'R_can':>8} "
        f"{'|v_h[0]|^2':>10} {'s_0':>6} {'sig_can/H':>10} {'eps_W':>8}")
    tab = []
    dN_grid = Ns[1] - Ns[0]
    for mi in mark_idx:
        pares = qep_can(Cc[mi], Wc[mi])
        if not pares:
            continue
        pares.sort(key=lambda mm: abs(mm['omega2']))
        vh = np.asarray(pares[-1]['v'], complex)
        omh = abs(np.sqrt(complex(pares[-1]['omega2'])))
        om2 = (abs(np.sqrt(complex(pares[-2]['omega2'])))
               if len(pares) >= 2 else float('nan'))
        R = omh / max(om2, Hs_arr[mi]) if np.isfinite(om2) else float('nan')
        cont0 = abs(vh[0])**2 / max(np.linalg.norm(vh)**2, 1e-300)
        s0 = float(np.real(np.conjugate(vh) @ ETA @ vh)
                   / max(np.linalg.norm(vh)**2, 1e-300))
        sig = max(abs(np.sqrt(complex(mm['omega2'])).imag)
                  for mm in pares) / Hs_arr[mi]
        dWn = np.linalg.norm(
            (Wc[min(mi + 1, NPTS - 1)] - Wc[max(mi - 1, 0)])
            / (2 * dN_grid))
        epsW = dWn / max(np.linalg.norm(Wc[mi]), 1e-300)
        pares_info = []
        for mm in pares:
            vv = np.asarray(mm['v'], complex)
            om_c = complex(np.sqrt(complex(mm['omega2'])))
            ss = float(np.real(np.conjugate(vv) @ ETA @ vv)
                       / max(np.linalg.norm(vv)**2, 1e-300))
            pares_info.append((abs(om_c), om_c, ss))
        tab.append(dict(a=aas[mi], kh=kc / (aas[mi] * Hs_arr[mi]),
                        omh=omh / Hs_arr[mi], R=R, cont0=cont0, s0=s0,
                        sig=sig, epsW=epsW, mi=mi, pares=pares_info))
    for tb in tab[::4] + ([tab[-1]] if tab else []):
        say(f"    {tb['a']:8.0f} {tb['kh']:7.2f} {tb['omh']:9.1f} "
            f"{tb['R']:8.1f} {tb['cont0']:10.3f} {tb['s0']:+6.2f} "
            f"{tb['sig']:10.2f} {tb['epsW']:8.3f}")

    tab_h = [tb for tb in tab if np.isfinite(tb['R']) and tb['R'] >= R_HIER]
    tab_s = [tb for tb in tab if np.isfinite(tb['epsW'])
             and tb['epsW'] < EPS_ASSENT]
    R_fim = tab[-1]['R'] if tab else float('nan')
    ok_b1a = np.isfinite(R_fim) and R_fim >= 100 and len(tab_h) >= 10
    cont_med = mediana([tb['cont0'] for tb in tab_s])
    ok_b1b = np.isfinite(cont_med) and cont_med > 0.9
    say(f"    [F-b1a {'SIM' if ok_b1a else 'NAO'}] hierarquia de vinculo: "
        f"R_final = {R_fim:.0f} (>=100); marcos com R>={R_HIER:g}: "
        f"{len(tab_h)}/{len(tab)}")
    say(f"    [F-b1b {'SIM' if ok_b1b else 'NAO'}] conteudo x0 do pesado "
        f"nos marcos ASSENTADOS (eps_W<{EPS_ASSENT:g}: {len(tab_s)} "
        f"marcos): mediana = {cont_med:.3f} (>0.9)")

    # F-b-NORMA nos marcos assentados
    neg_prop = []
    for tb in tab_s:
        Hm = Hs_arr[tb['mi']]
        for om_abs, om_c, ss in tb['pares']:
            if (om_abs / Hm < 50.0 and abs(om_c.imag) < 0.2 * max(
                    abs(om_c.real), 1e-30) and ss < -0.1):
                neg_prop.append((tb['a'], om_abs / Hm, ss))
    if neg_prop:
        say(f"    [F-b-NORMA] MODO PROPAGANTE COM NORMA-ETA NEGATIVA em "
            f"{len(neg_prop)} entradas de marcos assentados; ex.: "
            + "; ".join(f"a={aa:.0f} |om|/H={oh:.1f} s={ss:+.2f}"
                        for aa, oh, ss in neg_prop[:3]))
    else:
        say("    [F-b-NORMA] nenhum modo propagante com norma-eta negativa "
            "nos marcos assentados")

    # F-b1c — superficie no 1o marco assentado com >=8 assentados depois
    say("")
    med_sup, med_fake = [], []
    ok_sup = ok_poder = False
    L_max = float('nan')
    cand = [tb for tb in tab_s
            if sum(1 for u in tab_s if u['mi'] > tb['mi']) >= 8]
    if cand:
        p0 = cand[0]['mi']
        marcos_dep = [tb['mi'] for tb in tab_s if tb['mi'] > p0]
        A0 = Cc[p0] - Cc[p0].T
        B0 = Ccd[p0] + Wc[p0]

        def evolui_x_ic(x0, xd0):
            q0 = Tarr[p0] @ x0
            qd0 = Tarr[p0] @ xd0 + Tdot[p0] @ x0
            return evolui_estado(Kr, Cr, Wr, Krd, Crd, Ns, Hs_arr,
                                 q0, qd0, marcos_dep, p0=p0)

        def delta_set(jc, lightset, fixa_c=False):
            meds = []
            for tipo, li in lightset:
                ol = [i for i in range(3) if i != jc]
                x0 = np.zeros(3)
                xd0 = np.zeros(3)
                if tipo == 'q':
                    x0[li] = 1.0
                else:
                    xd0[li] = 1.0
                x0[jc] = -(B0[jc, ol] @ x0[ol]
                           + A0[jc, ol] @ xd0[ol]) / B0[jc, jc]
                if fixa_c:
                    ol0 = [i for i in range(3) if i != 0]
                    x0[0] = -(B0[0, ol0] @ x0[ol0]
                              + A0[0, ol0] @ xd0[ol0]) / B0[0, 0]
                sx = evolui_x_ic(x0, xd0)
                ds = []
                for mi in marcos_dep:
                    if mi not in sx:
                        continue
                    xx, xxd = para_x(mi, *sx[mi])
                    Am = Cc[mi] - Cc[mi].T
                    Bm = Ccd[mi] + Wc[mi]
                    ol2 = [i for i in range(3) if i != jc]
                    xstar = -(Bm[jc, ol2] @ xx[ol2]
                              + Am[jc, ol2] @ xxd[ol2]) / Bm[jc, jc]
                    esc = abs(xstar) + np.linalg.norm(xx[ol2]) + 1e-300
                    ds.append(abs(xx[jc] - xstar) / esc)
                meds.append(mediana(ds))
            return meds

        med_sup = delta_set(0, [('q', 1), ('q', 2), ('qd', 1), ('qd', 2)])
        med_fake = delta_set(2, [('q', 1), ('qd', 1)], fixa_c=True)
        ok_sup = all(np.isfinite(m) and m < 0.1 for m in med_sup)
        ok_poder = all(np.isfinite(m) and m >= 0.3 for m in med_fake)
        say(f"    [F-b1c-SUP {'SIM' if ok_sup else 'NAO'}] mediana "
            f"delta_rel (4 ICs na superficie de x0, desde "
            f"a~{aas[p0]:.0f}): "
            + " ".join(f"{m:.3f}" for m in med_sup) + " (<0.1)")
        say(f"    [F-b1c-PODER {'OK' if ok_poder else 'FALHOU'}] "
            "superficie FALSA (eixo leve x2): "
            + " ".join(f"{m:.3f}" for m in med_fake)
            + " (>=0.3 — tem que reprovar)")
        sx = evolui_x_ic(np.array([1.0, 0, 0]), np.zeros(3))
        Ls = []
        for mi in marcos_dep:
            if mi in sx:
                xx, _ = para_x(mi, *sx[mi])
                Ls.append(np.linalg.norm(xx[1:])
                          / max(np.linalg.norm(xx), 1e-300))
        L_max = max(Ls) if Ls else float('nan')
        say(f"    [F-b-DESAC] fracao leve max da IC pura-x0: {L_max:.3f} "
            "(<0.2 esperado; diagnostico)")
    else:
        say("    [!] marcos assentados insuficientes — superficie nao "
            "testavel")

    # F-b2 + CONF-BANDA
    say("")
    omh_fim = tab[-1]['omh'] if tab else float('nan')
    omh_s = mediana([tb['omh'] for tb in tab_s])
    w00_fim = np.sqrt(abs(Wc[-1][0, 0])) / Hs_arr[-1]
    sig_tarde = mediana([tb['sig'] for tb in tab_s[-8:]]) if tab_s \
        else float('nan')
    epsW_tarde = mediana([tb['epsW'] for tb in tab_s[-8:]]) if tab_s \
        else float('nan')
    conf = (np.isfinite(sig_tarde)
            and abs(sig_tarde - REF_BANDA[B1V]) < 0.5)
    say(f"    F-b2 — escala invariante: omega_0/H mediana assentada = "
        f"{omh_s:.1f}; final = {omh_fim:.1f}; sqrt|W_can[0,0]|/H = "
        f"{w00_fim:.1f}  (escalas: H=1, m_T/H~3.5, Lambda_3~O(1))")
    say(f"    [CONF-BANDA {'SIM' if conf else 'NAO'}] sigma_can tardio = "
        f"{sig_tarde:.2f} vs taxa real da banda {REF_BANDA[B1V]:+.2f} "
        f"(|dif|<0.5); eps_W tardio = {epsW_tarde:.3f}")
    return dict(ok_eta=ok_eta, ok_res=ok_res, vres=vres,
                ok_b1a=ok_b1a, ok_b1b=ok_b1b, ok_sup=ok_sup,
                ok_poder=ok_poder, neg_prop=len(neg_prop),
                omh_fim=omh_fim, omh_s=omh_s, R_fim=R_fim,
                cont=cont_med, sig_tarde=sig_tarde,
                epsW_tarde=epsW_tarde, conf=conf,
                n_assent=len(tab_s))


# ------------------------------------------------------------------
# V-EQUIV-GR (1 dof; sanidade do pipeline — dupla integracao SO em GR)
# ------------------------------------------------------------------
say("")
say("V-EQUIV-GR — normalizacao canonica em GR (1 dof):")
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
LAM_GR = 3.9
NsG = np.linspace(np.log(A_MIN), np.log(A_MAX), NPTS)
HsG = np.zeros(NPTS)
MsG = {x: np.zeros((NPTS, 3, 3)) for x in 'KCW'}
kcG = 45.0 * np.sqrt((LAM_GR + RHO0 / A_MIN**3) / 3.0) * A_MIN
for p, N in enumerate(NsG):
    a = np.exp(N)
    rho_d = RHO0 / a**3
    H = np.sqrt((LAM_GR + rho_d) / 3.0)
    HsG[p] = H
    args = (a, H, -0.5 * rho_d, 0.0, 0.0, LAM_GR + rho_d, 0.0, 0.3, kcG)
    MsG['K'][p] = np.array(KgF(*args), float)
    MsG['C'][p] = np.array(CgF(*args), float)
    MsG['W'][p] = np.array(WgF(*args), float)
KrG, CrG, WrG, KrdG, CrdG = reduz_trilha(MsG, NsG, HsG,
                                         mult=[0, 1], dyn=[2])
TG = 1.0 / np.sqrt(np.abs(KrG[:, 0, 0]))
TdG = np.gradient(TG, NsG) * HsG
KcG = np.ones((NPTS, 1, 1))
CcG = np.zeros((NPTS, 1, 1))
WcG = np.zeros((NPTS, 1, 1))
for p in range(NPTS):
    CcG[p, 0, 0] = KrG[p, 0, 0] * TG[p] * TdG[p] + CrG[p, 0, 0] * TG[p]**2
    WcG[p, 0, 0] = (WrG[p, 0, 0] * TG[p]**2 - KrG[p, 0, 0] * TdG[p]**2
                    - 2 * CrG[p, 0, 0] * TG[p] * TdG[p])
KcdG = np.zeros_like(KcG)
CcdG = np.gradient(CcG, NsG, axis=0) * HsG[:, None, None]
aasG = np.exp(NsG)
mkG = sorted(set(int(np.argmin(np.abs(aasG - am))) for am in MARCAS))
q0G = np.array([1.0])
s_q = evolui_estado(KrG, CrG, WrG, KrdG, CrdG, NsG, HsG,
                    q0G, np.zeros(1), mkG)
x0G = np.array([q0G[0] / TG[0]])
xd0G = np.array([-TdG[0] * x0G[0] / TG[0]])
s_x = evolui_estado(KcG, CcG, WcG, KcdG, CcdG, NsG, HsG,
                    x0G, xd0G, mkG)
errsG = []
for mi in mkG:
    if mi in s_q and mi in s_x:
        qd_, _ = s_q[mi]
        xx, _ = s_x[mi]
        errsG.append(abs(qd_[0] - TG[mi] * xx[0])
                     / max(abs(qd_[0]), 1e-300))
errG = max(errsG) if errsG else float('nan')
ok_gr_eq = np.isfinite(errG) and errG < 0.05
say(f"  [V-EQUIV-GR {'OK' if ok_gr_eq else 'FALHOU'}] max err = "
    f"{errG:.3e} (criterio < 0.05)")

RES = {}
for B1V in (1.0, 4.47):
    RES[B1V] = analisa(B1V)

# ------------------------------------------------------------------
# veredito
# ------------------------------------------------------------------
say("")
say("=" * 72)
say("VEREDITO GATE F-b v2 (criterios pre-declarados no cabecalho)")
say("=" * 72)
say(f"  V-EQUIV-GR: {'OK' if ok_gr_eq else 'FALHOU'}")
for B1V, r in RES.items():
    say(f"  beta1={B1V:g}: ETA {'ok' if r['ok_eta'] else 'FALHOU'}; "
        f"RES {'ok' if r['ok_res'] else 'FALHOU'} ({r['vres']:.3f}); "
        f"b1a {'SIM' if r['ok_b1a'] else 'NAO'} (R_fim {r['R_fim']:.0f}); "
        f"b1b {'SIM' if r['ok_b1b'] else 'NAO'} ({r['cont']:.2f}); "
        f"b1c-SUP {'SIM' if r['ok_sup'] else 'NAO'} "
        f"(PODER {'ok' if r['ok_poder'] else 'FALHOU'}); "
        f"neg-prop {r['neg_prop']}; om0/H ~ {r['omh_s']:.1f}; "
        f"CONF-BANDA {'SIM' if r['conf'] else 'NAO'} "
        f"(sig_can {r['sig_tarde']:.2f}, epsW {r['epsW_tarde']:.3f})")
say("")
todos = list(RES.values())
gates_ok = (ok_gr_eq and all(r['ok_eta'] and r['ok_res'] for r in todos))
if not gates_ok:
    say("  >>> VALIDACAO FALHOU (ETA/RES/GR) — nao interpretar; corrigir")
    say("  a construcao antes de qualquer ramo.")
elif all(r['ok_b1a'] and r['ok_b1b'] and r['ok_sup'] and r['ok_poder']
         for r in todos):
    say("  >>> H-CONSTRAINT CONFIRMADA EM COORDENADAS VALIDAS: hierarquia")
    say("  real + identidade + superficie quasi-invariante (PODER")
    say("  discriminando). Contagem efetiva tardia = 2; o fantasma e")
    say("  artefato de representacao. GATE F FECHA saudavel; F-c")
    say("  desnecessario.")
elif (all(not r['ok_b1a'] for r in todos)
      and all(r['neg_prop'] > 0 for r in todos)
      and all(r['omh_s'] < 50 for r in todos)):
    say("  >>> SEM hierarquia de vinculo (H-CONSTRAINT cai em coordenadas")
    say("  validas — o 'quer ser vinculo' do R-2 era artefato da base")
    say("  comovel) E existe MODO PROPAGANTE COM NORMA-ETA NEGATIVA a")
    say("  omega_0 ~ 7-12 H (invariante), acima de m_T e Lambda_3 mas nao")
    say("  alem de todo alcance: FANTASMA NO ESPECTRO LINEAR CANONICO.")
    say("  Ramos restantes do gate: F-c (estimativa de interacoes/decay)")
    say("  ou fronteira declarada no paper — DECISAO DO AUTOR (o gate doc")
    say("  preve ambos). Nota: com CONF-BANDA, o congelado canonico e")
    say("  arbitro legitimo — este e um enunciado de espectro, nao de")
    say("  instabilidade dinamica linear (a evolucao real e estavel no")
    say("  IR profundo e transiente na banda — D2/R-1/R-4).")
elif all(not r['ok_b1a'] and r['omh_s'] >= 50 for r in todos):
    say("  >>> H-SC: direcao negativa alem das escalas EFT — fora do")
    say("  alcance quadratico; setor nao exclui a F1.")
else:
    say("  >>> quadro misto — reportar tabelas e decidir com o autor.")
say("")
say("  CONF-BANDA (reabilitacao do congelado CANONICO): ver acima — se")
say("  SIM nos dois fundos, o aviso metodologico do paper ganha")
say("  resolucao: congelado comovel NAO e arbitro (D2), congelado")
say("  CANONICO (K constante, W assentada) E — e preve a banda.")

os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
with open(os.path.join(HERE, "out", "gatef_b_canonica.txt"),
          "w", encoding="utf-8") as fh:
    fh.write("\n".join(OUT))
say("")
say("concluido. saida em auditoria/code/out/gatef_b_canonica.txt")
