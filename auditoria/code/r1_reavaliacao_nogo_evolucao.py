# -*- coding: utf-8 -*-
"""
r1_reavaliacao_nogo_evolucao.py — R-1 da fila de reavaliacao
(docs/resultado_d2_evolucao.md secao 6): as celulas do no-go
beta-constante sobrevivem como instabilidade DINAMICA, ou o veredito
congelado e vacuo em todo o espaco amostrado?

CONTEXTO. O D2 mostrou que na celula REF mu=1 o taquiao tardio
congelado nao e dinamico: evolucao real dilui (-3/2 H), crescimento so
transiente/limitado — o instrumento congelado descarta os termos
dominantes (matrizes comoveis ~ a^3). Este script aplica a MESMA
maquinaria validada (reducao dependente do tempo + RK4 + controles) a
uma AMOSTRA REPRESENTATIVA do espaco do no-go
(docs/no_go_beta_constante.md: beta1 in [0.2,2], beta2 in [-1,-0.05],
mu in {0.1..100}, beta0=1, beta4=0.5).

AMOSTRA (fronteira declarada): a linha mu da celula REF (1,-0.4) com
mu in {0.3,1,3,10,30,100}; a celula da lei de escala (0.5,-0.84) em
mu in {0.3,1}; a celula da fresta (0.2,-1.0) em mu in {0.1,1} (mu=0.1
e a celula do FANTASMA quase-nulo); e tres cantos (2,-0.05), (2,-1),
(0.2,-0.05) em mu=1. k_c=10 (k_phys=1 em a=10) em todas; k_c=100 na
REF mu=1 (ja coberta pelo D2, incluida para a tabela).

POR CELULA, reporta:
  - sigma/H CONGELADO em a=400 (o que o instrumento antigo afirma);
  - taxas REAIS (max sobre as 4 ICs do bloco metrico) nas tres
    janelas: primordial [0.3,1.5], transicao [15,45], tardia
    [400,1900], normalizadas pelo H do meio da janela;
  - amplificacao maxima ln|y| ao longo da trajetoria (o dano transiente
    total — mesmo instabilidade transiente pode invalidar teoria
    linear se lnA for grande);
  - assinatura de K_red em a=400 (n. de autovalores negativos —
    o fantasma ESTRUTURAL, que a evolucao linear nao testa; insumo
    do R-2);
  - VEREDITO: TARDIA-DILUI (todas as ICs metricas < 0) /
    TARDIA-CRESCE (alguma >= 0.5 sigma_congelado) / MISTO.

CRITERIOS PRE-DECLARADOS:
  R1-GR: controle GR sem crescimento espurio (janelas validas).
  R1-VEREDITO agregado: se NENHUMA celula amostrada tiver
      TARDIA-CRESCE, o no-go tardio congelado e vacuo em todo o
      espaco amostrado — o setor escalar tardio da F1 beta-constante
      e dinamicamente estavel no nivel linear (fronteira declarada;
      fantasma estrutural fora do alcance deste teste). Se alguma
      celula crescer: mapear e reportar — o no-go dinamico sobrevive
      parcialmente.

Requer sympy, numpy, scipy. ~5-8 min.
Uso: python auditoria/code/r1_reavaliacao_nogo_evolucao.py
Saida em auditoria/code/out/r1_reavaliacao_nogo_evolucao.txt
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
JANELAS = [("primordial", 0.3, 1.5), ("transicao", 15.0, 45.0),
           ("tardia", 400.0, 1900.0)]
RHO0 = 0.3

say("=" * 72)
say("R-1 — REAVALIACAO DO NO-GO BETA-CONSTANTE POR EVOLUCAO REAL")
say("=" * 72)


def fundo_em(a, B0V, B1V, B2V, B4V, mu):
    """ramo finito com taxas verdadeiras; None se nao houver fundo."""
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


def reduz_ponto(Kt, Ct, Wt, Cdot, mult, dyn):
    K = Kt.copy()
    C = Ct.copy()
    W = Wt.copy()
    n = K.shape[0]
    for i in mult:
        if np.max(np.abs(K[i, :])) > 1e-10 * max(1.0, np.max(np.abs(K))):
            raise RuntimeError(f"linha K do multiplicador {i} nao-nula")
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


def evolui_celula(Ms, Ns, Hs_arr, mult, dyn):
    npts = len(Ns)
    Cdots = np.gradient(Ms['C'], Ns, axis=0) * Hs_arr[:, None, None]
    nd = len(dyn)
    Kr = np.zeros((npts, nd, nd))
    Cr = np.zeros((npts, nd, nd))
    Wr = np.zeros((npts, nd, nd))
    for p in range(npts):
        Kr[p], Cr[p], Wr[p] = reduz_ponto(Ms['K'][p], Ms['C'][p],
                                          Ms['W'][p], Cdots[p], mult, dyn)
    Krd = np.gradient(Kr, Ns, axis=0) * Hs_arr[:, None, None]
    Crd = np.gradient(Cr, Ns, axis=0) * Hs_arr[:, None, None]
    aas = np.exp(Ns)
    Hmid = {}
    for nome, lo, hi in JANELAS:
        pm = int(np.argmin(np.abs(aas - np.sqrt(lo * hi))))
        Hmid[nome] = Hs_arr[pm]
    taxas = []
    amps = []
    for ic in range(2 * nd):
        q = np.zeros(nd)
        qd = np.zeros(nd)
        if ic < nd:
            q[ic] = 1.0
        else:
            qd[ic - nd] = 1.0
        tcum = 0.0
        amp = 0.0
        reg = {nome: [None] * 4 for nome, _, _ in JANELAS}
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
            ln = np.log(max(np.sqrt(q @ q + qd @ qd), 1e-300))
            amp = max(amp, ln)
            for nome, lo, hi in JANELAS:
                r = reg[nome]
                if r[0] is None and aa >= lo:
                    r[0], r[1] = ln, tcum
                if r[2] is None and aa >= hi:
                    r[2], r[3] = ln, tcum
        tx = {}
        for nome, lo, hi in JANELAS:
            r = reg[nome]
            if r[0] is not None and r[2] is not None and r[3] > r[1]:
                tx[nome] = (r[2] - r[0]) / (r[3] - r[1]) / Hmid[nome]
            else:
                tx[nome] = float('nan')
        taxas.append(tx)
        amps.append(amp)
    return taxas, amps, Kr, Cr, Wr


# ------------------------------------------------------------------
# controle GR (identico ao D2; barato)
# ------------------------------------------------------------------
say("")
say("R1-GR — controle GR+chi pelo mesmo pipeline")
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
FIX_GR = {Mg2: 1, rho_s: 0, chid_s: 0, chidd_s: 0,
          Up: 0, Upp: sp.Rational(3, 10)}
KgF = sp.lambdify((a_s, H_s, Hd_s, Ub, ksym), Kg.subs(FIX_GR), 'numpy')
CgF = sp.lambdify((a_s, H_s, Hd_s, Ub, ksym), Cg.subs(FIX_GR), 'numpy')
WgF = sp.lambdify((a_s, H_s, Hd_s, Ub, ksym), Wg.subs(FIX_GR), 'numpy')
Ns_gr = np.linspace(np.log(0.2), np.log(60.0), 8000)
Hs_gr = np.zeros(len(Ns_gr))
Ms_gr = {x: np.zeros((len(Ns_gr), 3, 3)) for x in 'KCW'}
for p, N in enumerate(Ns_gr):
    a = np.exp(N)
    H = np.sqrt(RHO0 / 3.0) * a**-1.5
    Hs_gr[p] = H
    args = (a, H, -1.5 * H * H, 3 * H * H, 10.0)
    for x, F in (('K', KgF), ('C', CgF), ('W', WgF)):
        Ms_gr[x][p] = np.array(F(*args), float)
taxas_gr, _, _, _, _ = (*evolui_celula(Ms_gr, Ns_gr, Hs_gr, [0, 1], [2]),)
vals = [tx['transicao'] for tx in taxas_gr]
ok_gr = all(v <= 0.1 for v in vals if np.isfinite(v))
say(f"    GR transicao: taxas/H = {[f'{v:+.2f}' for v in vals]}  "
    f"[{'PASSA' if ok_gr else 'FALHA'}]")
if not ok_gr:
    sys.exit(1)

# ------------------------------------------------------------------
# montagem bimetrica com betas e mu LIVRES
# ------------------------------------------------------------------
L2s, fields, vels = d1.build_L2()
K7, C7, W7 = quadratic_matrices(L2s, fields, vels)
if [str(f) for f in fields] != NOMES:
    raise RuntimeError("ordem de campos mudou")
FIXOS = {Mg2: 1, m2: 1, b3: 0, Fb: 1, Fp: 0, Fpp: 0,
         chid_s: 0, chidd_s: 0, rho_s: 0, Up: 0, Upp: sp.Rational(3, 10)}
LIVRES = (a_s, b_s, xi_s, H_s, Hf_s, Hd_s, Hfd_s, xid_s, Ub, ksym,
          b0, b1, b2, b4, Mf2, Meff2)
K7F = sp.lambdify(LIVRES, K7.subs(FIXOS), 'numpy')
C7F = sp.lambdify(LIVRES, C7.subs(FIXOS), 'numpy')
W7F = sp.lambdify(LIVRES, W7.subs(FIXOS), 'numpy')
say("[montagem+lambdify] prontos (betas e mu livres)")

CELULAS = [
    (1.0, -0.4, 0.3, 10.0), (1.0, -0.4, 1.0, 10.0),
    (1.0, -0.4, 3.0, 10.0), (1.0, -0.4, 10.0, 10.0),
    (1.0, -0.4, 30.0, 10.0), (1.0, -0.4, 100.0, 10.0),
    (0.5, -0.84, 0.3, 10.0), (0.5, -0.84, 1.0, 10.0),
    (0.2, -1.0, 0.1, 10.0), (0.2, -1.0, 1.0, 10.0),
    (2.0, -0.05, 1.0, 10.0), (2.0, -1.0, 1.0, 10.0),
    (0.2, -0.05, 1.0, 10.0),
    (1.0, -0.4, 1.0, 100.0),
]
B0V, B4V = 1.0, 0.5
NPTS = 16000

say("")
say(f"    {'b1':>5} {'b2':>6} {'mu':>6} {'k_c':>5} | {'sig_cong':>8} "
    f"{'prim':>6} {'trans':>6} {'tard':>6} {'lnA_max':>7} {'negK':>4}  veredito")
resultados = []
for B1V, B2V, mu, kc in CELULAS:
    Ns = np.linspace(np.log(0.2), np.log(2000.0), NPTS)
    Hs_arr = np.zeros(NPTS)
    Ms = {x: np.zeros((NPTS, 7, 7)) for x in 'KCW'}
    ok = True
    for p, N in enumerate(Ns):
        f = fundo_em(np.exp(N), B0V, B1V, B2V, B4V, mu)
        if f is None:
            ok = False
            break
        Hs_arr[p] = f['H']
        meff2 = mu / (1.0 + mu)
        args = (np.exp(N), f['r'] * np.exp(N), f['xi'], f['H'], f['Hf'],
                f['Hd'], f['Hfd'], f['xid'], f['Ub'], kc,
                B0V, B1V, B2V, B4V, mu, meff2)
        Ms['K'][p] = np.array(K7F(*args), float)
        Ms['C'][p] = np.array(C7F(*args), float)
        Ms['W'][p] = np.array(W7F(*args), float)
    if not ok:
        say(f"    {B1V:5.1f} {B2V:6.2f} {mu:6.1f} {kc:5.0f} | sem fundo valido — pulada")
        continue
    try:
        taxas, amps, Kr, Cr, Wr = evolui_celula(Ms, Ns, Hs_arr, MULT, DYN)
    except RuntimeError as e:
        say(f"    {B1V:5.1f} {B2V:6.2f} {mu:6.1f} {kc:5.0f} | reducao abortou: {e}")
        continue
    p400 = int(np.argmin(np.abs(np.exp(Ns) - 400.0)))
    pares = d1.agrupa_pares(d1.qep_modes(Kr[p400], Cr[p400], Wr[p400]))
    sig_c = max(abs(np.sqrt(complex(mm['omega2'])).imag)
                for mm in pares) / Hs_arr[p400]
    eigK = np.linalg.eigvalsh(0.5 * (Kr[p400] + Kr[p400].T))
    negK = int(np.sum(eigK < -1e-12))
    idx_met = [0, 1, 3, 4]
    t_prim = max(taxas[i]['primordial'] for i in idx_met)
    t_tran = max(taxas[i]['transicao'] for i in idx_met)
    t_tard = max(taxas[i]['tardia'] for i in idx_met)
    amp_max = max(amps[i] for i in idx_met)
    if all(np.isfinite(taxas[i]['tardia']) and taxas[i]['tardia'] < 0
           for i in idx_met):
        verd = 'TARDIA-DILUI'
    elif any(np.isfinite(taxas[i]['tardia'])
             and taxas[i]['tardia'] >= 0.5 * sig_c for i in idx_met):
        verd = 'TARDIA-CRESCE'
    else:
        verd = 'MISTO'
    say(f"    {B1V:5.1f} {B2V:6.2f} {mu:6.1f} {kc:5.0f} | {sig_c:8.2f} "
        f"{t_prim:+6.2f} {t_tran:+6.2f} {t_tard:+6.2f} {amp_max:7.2f} "
        f"{negK:4d}  {verd}")
    resultados.append(dict(b1=B1V, b2=B2V, mu=mu, kc=kc, sig=sig_c,
                           tard=t_tard, tran=t_tran, amp=amp_max,
                           negK=negK, verd=verd))

# ------------------------------------------------------------------
say("")
say("=" * 72)
say("VEREDITO R-1 (criterios pre-declarados)")
say("=" * 72)
cresce = [r for r in resultados if r['verd'] == 'TARDIA-CRESCE']
dilui = [r for r in resultados if r['verd'] == 'TARDIA-DILUI']
say(f"  celulas avaliadas: {len(resultados)}; TARDIA-DILUI: {len(dilui)}; "
    f"TARDIA-CRESCE: {len(cresce)}; MISTO: "
    f"{len(resultados) - len(dilui) - len(cresce)}")
if not cresce:
    say("")
    say("  >>> NENHUMA celula amostrada cresce no tardio: o no-go tardio")
    say("  congelado e VACUO em todo o espaco amostrado. No nivel linear")
    say("  dinamico, o setor escalar tardio da F1 beta-constante e")
    say("  ESTAVEL nas celulas testadas (fronteira declarada: amostra")
    say("  acima, k_c={10,100}, uma trajetoria por celula).")
    say("  O que resta do no-go: (i) a assinatura cinetica indefinida")
    say("  (coluna negK — o fantasma estrutural, presente onde negK>0),")
    say("  cuja letalidade e a pergunta do R-2; (ii) amplificacao")
    say("  transiente lnA_max (celulas com lnA grande tem a instabilidade")
    say("  de transicao relevante — comparar com a literatura no R-4).")
else:
    say("")
    say("  >>> celulas com crescimento tardio REAL encontradas — o no-go")
    say("  dinamico sobrevive parcialmente; mapa acima.")

os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
with open(os.path.join(HERE, "out", "r1_reavaliacao_nogo_evolucao.txt"),
          "w", encoding="utf-8") as fh:
    fh.write("\n".join(OUT))
say("")
say("concluido. saida em auditoria/code/out/r1_reavaliacao_nogo_evolucao.txt")
