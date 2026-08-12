# -*- coding: utf-8 -*-
"""
r4c_confronto_epocas.py — R-4c (bloco 3 do R-4, opcoes B+C do autor):
o dano observavel da banda — era Lambda REAL (parcial) e entrada de
modos na era de MATERIA.

CONTEXTO (docs/resultado_r4b_forma.md; decisao do autor 2026-08-12:
B+C). O R-4b mediu a amplificacao de PASSAGEM COMPLETA da banda:
lnA ~ +3.6-4.0 por modo (limite inferior; ~e^6-7 com a cauda kh>20),
universal na classe. Mas a passagem completa leva ~4.6 e-folds de era
acelerada — e o universo real: (B) so teve ~0.7 e-fold de aceleracao
ate hoje (modos SAINDO do horizonte agora estao no MEIO da passagem —
o dano real e a integral PARCIAL); e (C) TODOS os modos de LSS
entraram no horizonte na era de materia — cruzando a banda de baixo
para cima num fundo dominado por poeira, regime NUNCA sondado (o
brinquedo com rho0=0.3 e Lambda-dominado desde a~0.7). A leitura de
mecanismo do R-4b sec.3 (nivel 3: a amplificacao acompanha a FRACAO
BIMETRICA do orcamento de energia — supressao pre-pouso quando U0
dominava) PREVE que a banda DESLIGA sob dominio de materia; o braco C
decide essa previsao no regime que importa para LSS.

DESENHO (maquinaria R-4b verbatim; sem modos de materia perturbada —
limitacao declarada do programa desde o D2: rho so no fundo):

  BRACO B (era Lambda real, integral parcial): fundo estatico beta1=1
    (representante da classe; universalidade AUTOSIM do R-4b), rodada
    unica identica a do R-4b (k_c = 45*H*100, a=[100,80000]).
    Janelas de 0.7 e-fold (Delta N_Lambda ~ aceleracao real ate hoje,
    z_acc~0.67) TERMINANDO onde o modo tem kh_hoje em
    {6,4,2.5,1.6,1,0.7,0.45,0.3,0.2}: lnA_parcial(kh_hoje) =
    Delta ln|y_met| liquido na janela (max ICs metricas). Leitura: um
    modo observado HOJE com kh_hoje acumulou isso na era acelerada
    real (kh_hoje=1 <-> k ~ H0: territorio ISW/baixo-ell). BASE: a
    mesma rodada reproduz a passagem completa do R-4b (+3.97 +- 0.4).

  BRACO C (entrada na era de materia): fundo beta-constante beta1=1
    com RHO0_C = 3e4 (equality em a_eq ~ 31.8; materia domina por
    ~4-6 e-folds no range). kh = k/(aH) SOBE ~a^(1/2) na materia
    (modos ENTRAM), pico ~ na equality, desce na era Lambda. Grade de
    k com kh_max (na equality) em {0.5, 1, 2, 4, 8} — da borda ao
    coracao da banda. MEDIDA por k: lnA_residencia = Delta ln|y_met|
    liquido entre kh cruzando 0.3 na subida e 0.3 na descida (a
    visita completa a banda, centrada na era de materia/equality) +
    janelas fixas (materia / equality / lambda) + fracao bimetrica
    f_bi = 1 - rho/(3 Mg^2 H^2) impressa nas bordas.
    NOTA NUMERICA declarada: materia profunda -> r ~ 1/rho minusculo
    -> matrizes em escalas extremas; a reducao ganha TRUNCAMENTO
    BILATERAL (pula o trecho invalido do inicio e reporta o range
    valido — que deve conter a residencia; se nao contiver, o braco
    reporta e nao conclui).

  BRACO C-GR (nulo): GR + poeira(RHO0_C) + Lambda(=3H_tarde^2 do
    bimetrico) + chi espectador, k com kh_max {1, 8}: a entrada no
    horizonte NAO amplifica em GR (esperado |lnA_residencia| <= 0.5).
    FALHA -> nao interpretar C.

CRITERIOS PRE-DECLARADOS:
  R4c-BASE: passagem completa do braco B = +3.97 +- 0.4 (continuidade
      com o R-4b). FALHA -> nao interpretar B.
  R4c-B: curva lnA_parcial(kh_hoje) — MEDIDA (sem passa/falha); o
      numero p/ o enunciado e o maximo da curva (pior escala hoje).
  R4c-C-NULL: bracos GR: |lnA_residencia| <= 0.5. FALHA -> abortar C.
  R4c-C (a previsao da fracao bimetrica, decidida):
      max_k lnA_residencia <= +0.5 -> SUPRESSAO-MATERIA: a banda
          desliga sob dominio de poeira — LSS passa ILESO pela
          entrada no brinquedo; o dano observavel total da banda fica
          confinado a era acelerada (R4c-B, pequeno) -> o confronto
          observacional e BRANDO e a classe sobrevive a banda;
      max_k lnA_residencia >= +2 -> ENTRADA-AMPLIFICA: candidato
          LETAL para LSS — levar aos vinculos com prioridade maxima
          (mapear em k/celulas antes de qualquer enunciado);
      intermediario -> reportar curva e decidir mapeamento.
  Diagnostico: correlacao lnA_residencia vs f_bi na residencia
      (a previsao mecanica: lnA cresce com f_bi).

Requer sympy, numpy, scipy. ~6-10 min.
Uso (raiz do repo, venv ativo):
    python auditoria/code/r4c_confronto_epocas.py
Saida em auditoria/code/out/r4c_confronto_epocas.txt
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
IDX_MET_IC = [0, 1, 3, 4]

# braco B
A_MIN_B, A_MAX_B = 100.0, 80000.0
NPTS_B = 24000
DN_LAMBDA = 0.7
KH_HOJE = [6.0, 4.0, 2.5, 1.6, 1.0, 0.7, 0.45, 0.3, 0.2]
KH_PASS = (20.0, 0.2)
LNA_REF_B = 3.97

# braco C
RHO0_C = 3.0e4
A_MIN_C, A_MAX_C = 0.05, 1500.0
NPTS_C = 24000
KH_MAXES = [0.5, 1.0, 2.0, 4.0, 8.0]
KH_RES = 0.3

MU = 1.0
MG2, MF2 = 1.0, MU
ME2 = MU / (1.0 + MU)
M2 = 1.0
B0V, B2V, B4V = 1.0, -0.4, 0.5
RHO0_STD = 0.3

say("=" * 72)
say("R-4c — O CONFRONTO POR EPOCAS: ERA LAMBDA PARCIAL (B) + ENTRADA")
say("NA ERA DE MATERIA (C)")
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


# ------------------------------------------------------------------
# fundo beta-constante com rho0 parametrizado
# ------------------------------------------------------------------
def fundo_bconst(a, B1V, rho0):
    kap = 1.0 / MU
    meff2 = ME2
    rho = rho0 * a**-3
    rho_til = rho / meff2
    rr = np.roots([kap * B4V - 3 * B2V, -3 * B1V,
                   3 * kap * B2V - B0V - rho_til, kap * B1V])
    reais = sorted(z.real for z in rr if abs(z.imag) < 1e-9 and z.real > 1e-12)
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
                Ub=3 * H2 - rho_int, fbi=rho_int / (3 * H2))


def builder_bconst(B1V, rho0, a_min, a_max):
    def build(kc, npts):
        Ns = np.linspace(np.log(a_min), np.log(a_max), npts)
        Hs_arr = np.zeros(npts)
        Ms = {x: np.zeros((npts, 7, 7)) for x in 'KCW'}
        for p, N in enumerate(Ns):
            a = np.exp(N)
            f = fundo_bconst(a, B1V, rho0)
            if f is None:
                Hs_arr[p] = float('nan')
                continue
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


# ------------------------------------------------------------------
# reducao com truncamento BILATERAL + evolucao (R-4b com dln)
# ------------------------------------------------------------------
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
    if not np.all(np.isfinite(WXX)) or np.linalg.cond(WXX) > 1e12:
        raise RuntimeError("W_XX mal condicionada")
    WXXi = np.linalg.inv(WXX)
    return (K[np.ix_(dyn, dyn)] + C[np.ix_(dyn, mult)] @ WXXi
            @ C[np.ix_(dyn, mult)].T,
            C[np.ix_(dyn, dyn)] - C[np.ix_(dyn, mult)] @ WXXi
            @ W[np.ix_(mult, dyn)],
            W[np.ix_(dyn, dyn)] - W[np.ix_(dyn, mult)] @ WXXi
            @ W[np.ix_(mult, dyn)])


def reduz_bilateral(Ms, Ns, Hs_arr, mult=None, dyn=None):
    """acha o maior bloco contiguo valido comecando no 1o ponto bom."""
    mult = MULT if mult is None else mult
    dyn = DYN if dyn is None else dyn
    nd = len(dyn)
    npts = len(Ns)
    Cdots = np.gradient(Ms['C'], Ns, axis=0) * \
        np.nan_to_num(Hs_arr)[:, None, None]
    ok = np.zeros(npts, bool)
    Kr = np.zeros((npts, nd, nd))
    Cr = np.zeros((npts, nd, nd))
    Wr = np.zeros((npts, nd, nd))
    for p in range(npts):
        if not np.isfinite(Hs_arr[p]):
            continue
        try:
            Kr[p], Cr[p], Wr[p] = reduz_ponto(
                Ms['K'][p], Ms['C'][p], Ms['W'][p], Cdots[p], mult, dyn)
            ok[p] = True
        except (RuntimeError, np.linalg.LinAlgError):
            ok[p] = False
    if not np.any(ok):
        return None
    p_ini = int(np.argmax(ok))
    p_fim = p_ini
    while p_fim < npts and ok[p_fim]:
        p_fim += 1
    sl = slice(p_ini, p_fim)
    Ns_t, Hs_t = Ns[sl], Hs_arr[sl]
    Kr, Cr, Wr = Kr[sl], Cr[sl], Wr[sl]
    Krd = np.gradient(Kr, Ns_t, axis=0) * Hs_t[:, None, None]
    Crd = np.gradient(Cr, Ns_t, axis=0) * Hs_t[:, None, None]
    return Kr, Cr, Wr, Krd, Crd, Ns_t, Hs_t


def evolui(Kr, Cr, Wr, Krd, Crd, Ns, Hs_arr, janelas, met_idx=(0, 1),
           nics=None):
    npts = len(Ns)
    nd = Kr.shape[1]
    aas = np.exp(Ns)
    if nics is None:
        nics = 2 * nd
    dlns_m, taxas_m = [], []
    for ic in range(nics):
        q = np.zeros(nd)
        qd = np.zeros(nd)
        if ic < nd:
            q[ic] = 1.0
        else:
            qd[ic - nd] = 1.0
        tcum = 0.0
        reg = {nome: [None] * 4 for nome, _, _ in janelas}
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
            if met_idx is None:
                n2_m = q @ q + qd @ qd
            else:
                n2_m = sum(q[j]**2 + qd[j]**2 for j in met_idx)
            ln_m = np.log(max(np.sqrt(n2_m), 1e-300))
            for nome, lo, hi in janelas:
                r = reg[nome]
                if r[0] is None and aa >= lo:
                    r[0], r[1] = ln_m, tcum
                if r[2] is None and aa >= hi:
                    r[2], r[3] = ln_m, tcum
        dl, tx = {}, {}
        for nome, lo, hi in janelas:
            r = reg[nome]
            if r[0] is not None and r[2] is not None and r[3] > r[1]:
                dl[nome] = r[2] - r[0]
                tx[nome] = (r[2] - r[0]) / (r[3] - r[1])
            else:
                dl[nome] = float('nan')
                tx[nome] = float('nan')
        dlns_m.append(dl)
        taxas_m.append(tx)
    return dlns_m, taxas_m


def dln_max(dlns, nome, idx=None):
    idx = IDX_MET_IC if idx is None else idx
    vs = [dlns[i].get(nome, float('nan')) for i in idx
          if i < len(dlns)]
    vs = [v for v in vs if np.isfinite(v)]
    return max(vs) if vs else float('nan')


# ------------------------------------------------------------------
# BRACO B — era Lambda real (integral parcial)
# ------------------------------------------------------------------
say("")
say("=" * 72)
say(f"BRACO B — era Lambda real: janelas de {DN_LAMBDA:g} e-fold por "
    "kh_hoje (fundo beta1=1)")
say("=" * 72)
fB = fundo_bconst(A_MIN_B, 1.0, RHO0_STD)
kcB = 45.0 * fB['H'] * A_MIN_B
buildB = builder_bconst(1.0, RHO0_STD, A_MIN_B, A_MAX_B)
Ns, Hs_arr, Ms = buildB(kcB, NPTS_B)
red = reduz_bilateral(Ms, Ns, Hs_arr)
KrB, CrB, WrB, KrdB, CrdB, NsB, HsB = red
aasB = np.exp(NsB)
khsB = kcB / (aasB * HsB)
say(f"    k_c={kcB:.1f}; range valido a=[{aasB[0]:.0f}, {aasB[-1]:.0f}]")


def a_de_kh(khs, aas, kh):
    if khs[0] <= kh or khs[-1] >= kh:
        return None
    return float(aas[int(np.argmax(khs <= kh))])


jansB = []
for khh in KH_HOJE:
    a_fim = a_de_kh(khsB, aasB, khh)
    if a_fim is None:
        continue
    a_ini = a_fim * np.exp(-DN_LAMBDA)
    if a_ini < aasB[0]:
        continue
    jansB.append((f"kh{khh:g}", a_ini, a_fim))
a_p1, a_p2 = a_de_kh(khsB, aasB, KH_PASS[0]), a_de_kh(khsB, aasB, KH_PASS[1])
if a_p1 is not None and a_p2 is not None:
    jansB.append(("passagem", a_p1, a_p2))
dlB, txB = evolui(KrB, CrB, WrB, KrdB, CrdB, NsB, HsB, jansB)
lnA_pass_B = dln_max(dlB, "passagem")
ok_base = np.isfinite(lnA_pass_B) and abs(lnA_pass_B - LNA_REF_B) < 0.4
say(f"    [R4c-BASE {'OK' if ok_base else 'FALHOU'}] passagem completa = "
    f"{lnA_pass_B:+.2f} (ref R-4b {LNA_REF_B:+.2f}, tol 0.4)")
say("")
say(f"    lnA_parcial ({DN_LAMBDA:g} e-fold terminando em kh_hoje):")
say(f"    {'kh_hoje':>8} {'lnA_parcial':>12}  (fator)")
curvaB = {}
for khh in KH_HOJE:
    v = dln_max(dlB, f"kh{khh:g}")
    curvaB[khh] = v
    if np.isfinite(v):
        say(f"    {khh:8.2f} {v:+12.2f}  (x{np.exp(v):.1f})")
vsB = [v for v in curvaB.values() if np.isfinite(v)]
B_max = max(vsB) if vsB else float('nan')
say(f"    B_max (pior escala hoje) = {B_max:+.2f}  "
    f"(amplitude x{np.exp(B_max):.1f})")

# ------------------------------------------------------------------
# BRACO C — entrada na era de materia
# ------------------------------------------------------------------
say("")
say("=" * 72)
say(f"BRACO C — entrada na era de materia (beta1=1, rho0={RHO0_C:g})")
say("=" * 72)
f_late = fundo_bconst(1e6, 1.0, RHO0_C)
a_eq = (RHO0_C / (3.0 * f_late['H']**2)) ** (1.0 / 3.0)
f_eq = fundo_bconst(a_eq, 1.0, RHO0_C)
aH_eq = a_eq * f_eq['H']
say(f"    a_eq ~ {a_eq:.1f}; H_eq = {f_eq['H']:.3f}; "
    f"f_bi(eq) = {f_eq['fbi']:.3f}")
buildC = builder_bconst(1.0, RHO0_C, A_MIN_C, A_MAX_C)

resC = {}
for khm in KH_MAXES:
    kc = khm * aH_eq
    say("")
    say(f"--- C: kh_max={khm:g} (k_c={kc:.1f}) ---")
    Ns, Hs_arr, Ms = buildC(kc, NPTS_C)
    red = reduz_bilateral(Ms, Ns, Hs_arr)
    if red is None:
        say("    [!] reducao sem bloco valido — braco pulado")
        continue
    Kr, Cr, Wr, Krd, Crd, Ns_t, Hs_t = red
    aas_t = np.exp(Ns_t)
    khs = kc / (aas_t * Hs_t)
    say(f"    range valido a=[{aas_t[0]:.2f}, {aas_t[-1]:.0f}]  "
        f"kh: {khs[0]:.3f} -> max {np.max(khs):.2f} -> {khs[-1]:.3f}")
    # residencia: kh cruza KH_RES subindo e descendo
    acima = khs >= KH_RES
    if not np.any(acima):
        say(f"    kh nunca atinge {KH_RES:g} — sem residencia; pulado")
        continue
    i_up = int(np.argmax(acima))
    i_dn = int(len(khs) - np.argmax(acima[::-1]) - 1)
    a_up = aas_t[max(i_up, 1)]
    a_dn = aas_t[min(i_dn, len(aas_t) - 2)]
    parcial = " (PARCIAL: comeca no limite do range)" if i_up == 0 else ""
    fb_up = fundo_bconst(a_up, 1.0, RHO0_C)['fbi']
    fb_dn = fundo_bconst(a_dn, 1.0, RHO0_C)['fbi']
    say(f"    residencia kh>={KH_RES:g}: a=[{a_up:.2f}, {a_dn:.0f}]"
        f"{parcial}; f_bi: {fb_up:.3f} -> {fb_dn:.3f}")
    jans = [("residencia", a_up, a_dn)]
    if a_up * 1.05 < 0.5 * a_eq:
        jans.append(("materia", a_up * 1.05, 0.5 * a_eq))
    jans.append(("equality", 0.5 * a_eq, min(2 * a_eq, a_dn)))
    if 2 * a_eq < a_dn:
        jans.append(("lambda", 2 * a_eq, a_dn))
    dl, tx = evolui(Kr, Cr, Wr, Krd, Crd, Ns_t, Hs_t, jans)
    say(f"    {'janela':<12} {'dln_met max':>12} {'taxa/H media':>13}")
    for nome, lo, hi in jans:
        v = dln_max(dl, nome)
        Hj = Hs_t[int(np.argmin(np.abs(aas_t - np.sqrt(lo * hi))))]
        tv = dln_max(tx, nome)
        say(f"    {nome:<12} {v:+12.2f} {tv/Hj if np.isfinite(tv) else float('nan'):+13.2f}")
    resC[khm] = dict(res=dln_max(dl, "residencia"), fb=(fb_up, fb_dn),
                     parcial=(i_up == 0))

# ------------------------------------------------------------------
# BRACO C-GR — nulo da entrada
# ------------------------------------------------------------------
say("")
say("--- C-GR (nulo): entrada no horizonte em GR + poeira + Lambda ---")
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
LAM_GR_C = 0.932

ok_cnull = True
for khm in (1.0, 8.0):
    kc = khm * aH_eq
    Ns = np.linspace(np.log(A_MIN_C), np.log(A_MAX_C), NPTS_C)
    Hs_arr = np.zeros(NPTS_C)
    Ms = {x: np.zeros((NPTS_C, 3, 3)) for x in 'KCW'}
    for p, N in enumerate(Ns):
        a = np.exp(N)
        rho_d = RHO0_C / a**3
        H = np.sqrt((LAM_GR_C + rho_d) / 3.0)
        Hs_arr[p] = H
        args = (a, H, -0.5 * rho_d, 0.0, 0.0,
                LAM_GR_C + rho_d, 0.0, 0.3, kc)
        Ms['K'][p] = np.array(KgF(*args), float)
        Ms['C'][p] = np.array(CgF(*args), float)
        Ms['W'][p] = np.array(WgF(*args), float)
    red = reduz_bilateral(Ms, Ns, Hs_arr, mult=[0, 1], dyn=[2])
    if red is None:
        say(f"    kh_max={khm:g}: reducao GR sem bloco valido — reportar")
        ok_cnull = False
        continue
    Kr, Cr, Wr, Krd, Crd, Ns_g, Hs_g = red
    aas_t = np.exp(Ns_g)
    khs = kc / (aas_t * Hs_g)
    acima = khs >= KH_RES
    i_up = int(np.argmax(acima))
    i_dn = int(len(khs) - np.argmax(acima[::-1]) - 1)
    jans = [("residencia", aas_t[max(i_up, 1)],
             aas_t[min(i_dn, len(aas_t) - 2)])]
    dl, _ = evolui(Kr, Cr, Wr, Krd, Crd, Ns_g, Hs_g, jans,
                   met_idx=None, nics=2)
    v = dln_max(dl, "residencia", idx=[0, 1])
    say(f"    kh_max={khm:g}: lnA_residencia GR = {v:+.2f}")
    if not (np.isfinite(v) and abs(v) <= 0.5):
        ok_cnull = False
say(f"  [R4c-C-NULL {'PASSA' if ok_cnull else 'FALHA — nao interpretar C'}]")

# ------------------------------------------------------------------
# veredito
# ------------------------------------------------------------------
say("")
say("=" * 72)
say("VEREDITO R-4c (criterios pre-declarados no cabecalho)")
say("=" * 72)
say(f"  R4c-BASE: {'OK' if ok_base else 'FALHOU'}   "
    f"R4c-C-NULL: {'PASSA' if ok_cnull else 'FALHA'}")
say("")
say(f"  R4c-B: lnA_parcial max (pior escala hoje) = {B_max:+.2f} "
    f"(x{np.exp(B_max):.1f} em amplitude) — curva completa acima.")
say("")
say("  R4c-C: lnA_residencia por kh_max:")
for khm, r in resC.items():
    say(f"    kh_max={khm:4g}: {r['res']:+.2f}"
        + ("  (parcial)" if r['parcial'] else "")
        + f"   f_bi na residencia: {r['fb'][0]:.3f}->{r['fb'][1]:.3f}")
vsC = [r['res'] for r in resC.values() if np.isfinite(r['res'])]
C_max = max(vsC) if vsC else float('nan')
say("")
if not ok_cnull or not resC:
    say("  >>> braco C sem interpretacao (NULL falhou ou sem bracos")
    say("  validos) — diagnosticar antes de qualquer enunciado.")
elif np.isfinite(C_max) and C_max <= 0.5:
    say(f"  >>> SUPRESSAO-MATERIA (C_max = {C_max:+.2f} <= +0.5): a banda")
    say("  DESLIGA sob dominio de poeira — modos entrando no horizonte")
    say("  na era de materia (LSS) passam ILESOS no brinquedo. A")
    say("  previsao da fracao bimetrica (R-4b sec.3) esta confirmada no")
    say("  regime decisivo. Com R4c-B pequeno, o dano observavel total")
    say("  da banda e BRANDO: confinado a escalas ~horizonte hoje")
    say("  (ISW/baixo-ell) com amplitude e^B_max. A classe SOBREVIVE a")
    say("  banda no dicionario minimo — enunciado do cap.07 na forma")
    say("  condicional-observacional.")
elif np.isfinite(C_max) and C_max >= 2.0:
    say(f"  >>> ENTRADA-AMPLIFICA (C_max = {C_max:+.2f} >= +2): modos de")
    say("  LSS sao amplificados na entrada — candidato LETAL. Mapear em")
    say("  k/celulas e levar aos vinculos com prioridade maxima antes")
    say("  de qualquer enunciado.")
else:
    say(f"  >>> intermediario (C_max = {C_max:+.2f}): reportar curva e")
    say("  decidir mapeamento fino com o autor.")
say("")
say("  diagnostico (previsao mecanica): lnA_residencia deve crescer com")
say("  f_bi — conferir tabela acima (f_bi minusculo na materia).")

os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
with open(os.path.join(HERE, "out", "r4c_confronto_epocas.txt"),
          "w", encoding="utf-8") as fh:
    fh.write("\n".join(OUT))
say("")
say("concluido. saida em auditoria/code/out/r4c_confronto_epocas.txt")
