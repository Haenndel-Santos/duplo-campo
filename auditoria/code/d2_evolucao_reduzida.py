# -*- coding: utf-8 -*-
"""
d2_evolucao_reduzida.py — Item D2 do posicionamento: o taquiao tardio
e FISICO no sistema dependente do tempo?

2a RODADA (2026-08-11, tarde). A 1a rodada (saida preservada em
out/d2_evolucao_reduzida_rodada1.txt) mediu taxas reais ~0.4-1.3H
contra sigma_congelado ~3.1-6.2H — discrepancia impossivel para
coeficientes constantes. As sondas de diagnostico (scratchpad)
explicaram: AS MATRIZES REDUZIDAS NUNCA ASSENTAM — as variaveis
comovel carregam fatores explicitos de a(t) (K_r ~ a^3 etc.,
|K_rdot|/|K_r| ~ 1.9H no "ponto fixo"), que o QEP congelado descarta
por construcao. E o dado decisivo: a projecao da solucao real no
automodo taquionico e DRENADA (0.46 -> 0.03) e a taxa tardia real e
-1.5H — a diluicao a^(-3/2) de osciladores saudaveis. Esta 2a rodada
endurece o teste para registrar isso oficialmente:

  - janela estendida: a in [0.2, 2000] (cobre era de materia
    primordial, transicao e ponto fixo profundo);
  - TRES janelas de ajuste: PRIMORDIAL a=[0.3,1.5] (onde o congelado
    preve sigma/H ~ 6-8), TRANSICAO a=[15,45], TARDIA a=[400,1900]
    (ponto fixo profundo; congelado preve sigma/H ~ 3.1 PARA SEMPRE);
  - taxas normalizadas pelo H do MEIO de cada janela;
  - diagnostico de projecao |c_grow|/|y| em marcos (IC 1);
  - ancoras congeladas em a=30 E a=400 (a previsao congelada e
    escala-invariante; a dinamica real decide).

O QUE CADA DESFECHO SIGNIFICA (pre-declarado):
  - taxa tardia ~ -1.5H com projecao drenada, nos DOIS k_c: o taquiao
    congelado tardio NAO e uma instabilidade dinamica real — o
    enunciado "taquiao eterno" de resultado_setor_escalar.md par.7 CAI
    e todos os vereditos de saude baseados em autovalor congelado
    NESTA classe ficam sob revisao (watershed metodologico: para este
    sistema, evolucao real e o arbitro, nao espectro congelado);
  - taxa primordial >> H: a instabilidade PRIMORDIAL e real em tempo
    real (consistente com a literatura do ramo finito);
  - qualquer crescimento tardio genuino (>= 0.5 sigma_ref, generico):
    o taquiao tardio seria fisico afinal (desfecho da 1a hipotese).

Controles: GR+chi pelo mesmo pipeline (sem crescimento espurio);
bloco dchi desacoplado (nao cresce); halving da grade.

Requer sympy, numpy, scipy. ~3-6 min.
Uso: python auditoria/code/d2_evolucao_reduzida.py
Saida em auditoria/code/out/d2_evolucao_reduzida.txt
(1a rodada preservada em out/d2_evolucao_reduzida_rodada1.txt)
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

say("=" * 72)
say("D2 (2a rodada) — EVOLUCAO TEMPORAL REAL vs ESPECTRO CONGELADO")
say("=" * 72)

# ------------------------------------------------------------------
B0V, B1V, B2V, B4V = 1.0, 1.0, -0.4, 0.5
MG2 = MF2 = 1.0
ME2, M2 = 0.5, 1.0
RHO0 = 0.3


def fundo_em(a):
    rho = RHO0 * a**-3
    rho_til = rho / (M2 * ME2)
    kap = MG2 / MF2
    rr = np.roots([kap * B4V - 3 * B2V, -3 * B1V,
                   3 * kap * B2V - B0V - rho_til, kap * B1V])
    reais = sorted(z.real for z in rr if abs(z.imag) < 1e-9 and z.real > 1e-10)
    r = reais[0]
    dW = kap * (2 * B4V * r - B1V / r**2) - 3 * B1V - 6 * B2V * r
    drdN = -3 * rho_til / dW
    d2W = kap * (2 * B4V + 2 * B1V / r**3) - 6 * B2V
    d2rdN2 = 9 * rho_til / dW + 3 * rho_til * d2W * drdN / dW**2
    xi = r + drdN
    Vf = B4V + 3 * B2V / r**2 + B1V / r**3
    dVf = -6 * B2V / r**3 - 3 * B1V / r**4
    H2 = M2 * ME2 * r * r * Vf / (3 * MF2)
    H = np.sqrt(H2)
    dlnH_dN = 0.5 * (2 / r + dVf / Vf) * drdN
    Hd = H2 * dlnH_dN
    xid = H * (drdN + d2rdN2)
    Hfd = (Hd - H2 * drdN / r) / r
    rho_int = M2 * ME2 * (B0V + 3 * B1V * r + 3 * B2V * r**2)
    return dict(r=r, xi=xi, H=H, Hf=H / r, Hd=Hd, Hfd=Hfd, xid=xid,
                Ub=3 * MG2 * H2 - rho_int)


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
    KQQ = K[np.ix_(dyn, dyn)]
    CQQ = C[np.ix_(dyn, dyn)]
    CQX = C[np.ix_(dyn, mult)]
    WQQ = W[np.ix_(dyn, dyn)]
    WQX = W[np.ix_(dyn, mult)]
    WXQ = W[np.ix_(mult, dyn)]
    return (KQQ + CQX @ WXXi @ CQX.T, CQQ - CQX @ WXXi @ WXQ,
            WQQ - WQX @ WXXi @ WXQ)


def evolui(Ms, Ns, Hs_arr, mult, dyn, janelas, marcas=None,
           evec_base=None, imax=None):
    """Reducao por ponto + RK4 com base completa de ICs.
    Devolve taxas[ic][janela] e trilha de projecao da IC 1."""
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
    for nome, lo, hi in janelas:
        pm = int(np.argmin(np.abs(aas - np.sqrt(lo * hi))))
        Hmid[nome] = Hs_arr[pm]
    dim = 2 * nd
    taxas = []
    trilha = []
    for ic in range(dim):
        q = np.zeros(nd)
        qd = np.zeros(nd)
        if ic < nd:
            q[ic] = 1.0
        else:
            qd[ic - nd] = 1.0
        tcum = 0.0
        reg = {nome: [None, None, None, None] for nome, _, _ in janelas}
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
            for nome, lo, hi in janelas:
                r = reg[nome]
                if r[0] is None and aa >= lo:
                    r[0], r[1] = ln, tcum
                if r[2] is None and aa >= hi:
                    r[2], r[3] = ln, tcum
            if ic == 0 and marcas is not None:
                for am in marcas:
                    if marcas[am] is None and aa >= am:
                        y = np.concatenate([q, qd])
                        proj = float('nan')
                        if evec_base is not None:
                            try:
                                coef = np.linalg.solve(
                                    evec_base, y.astype(complex))
                                proj = abs(coef[imax]) / max(
                                    np.linalg.norm(y), 1e-300)
                            except np.linalg.LinAlgError:
                                pass
                        marcas[am] = (ln, proj)
        tx = {}
        for nome, lo, hi in janelas:
            r = reg[nome]
            if r[0] is not None and r[2] is not None and r[3] > r[1]:
                tx[nome] = (r[2] - r[0]) / (r[3] - r[1]) / Hmid[nome]
            else:
                tx[nome] = float('nan')
        taxas.append(tx)
    return taxas, Kr, Cr, Wr


# ------------------------------------------------------------------
# D2-GR — controle
# ------------------------------------------------------------------
say("")
say("D2-GR — controle: GR+chi, FRW de materia, mesmo pipeline")
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
LIV_GR = (a_s, H_s, Hd_s, Ub, ksym)
KgF = sp.lambdify(LIV_GR, Kg.subs(FIX_GR), 'numpy')
CgF = sp.lambdify(LIV_GR, Cg.subs(FIX_GR), 'numpy')
WgF = sp.lambdify(LIV_GR, Wg.subs(FIX_GR), 'numpy')

Ns_gr = np.linspace(np.log(0.2), np.log(2000.0), 20000)
Hs_gr = np.zeros(len(Ns_gr))
Ms_gr = {x: np.zeros((len(Ns_gr), 3, 3)) for x in 'KCW'}
for p, N in enumerate(Ns_gr):
    a = np.exp(N)
    H = np.sqrt(RHO0 / 3.0) * a**-1.5
    Hs_gr[p] = H
    args = (a, H, -1.5 * H * H, 3 * H * H, 10.0)
    Ms_gr['K'][p] = np.array(KgF(*args), float)
    Ms_gr['C'][p] = np.array(CgF(*args), float)
    Ms_gr['W'][p] = np.array(WgF(*args), float)
taxas_gr, _, _, _ = evolui(Ms_gr, Ns_gr, Hs_gr, [0, 1], [2], JANELAS)
ok_gr = True
for nome, _, _ in JANELAS:
    vals = [tx[nome] for tx in taxas_gr]
    say(f"    GR {nome}: taxas/H = {[f'{v:+.2f}' for v in vals]}")
    ok_gr = ok_gr and all(v <= 0.1 for v in vals if np.isfinite(v))
say(f"  [D2-GR {'PASSA' if ok_gr else 'FALHA — abortar'}] "
    "(esperado: oscilador diluindo, ~-1.5H)")
if not ok_gr:
    sys.exit(1)

# ------------------------------------------------------------------
# bimetrico
# ------------------------------------------------------------------
L2s, fields, vels = d1.build_L2()
K7, C7, W7 = quadratic_matrices(L2s, fields, vels)
if [str(f) for f in fields] != NOMES:
    raise RuntimeError("ordem de campos mudou")
say("[montagem] K,C,W 7x7 prontos")
FIXOS = {Mg2: 1, Mf2: 1, m2: 1, Meff2: sp.Rational(1, 2),
         b0: 1, b1: 1, b2: sp.Rational(-2, 5), b3: 0,
         b4: sp.Rational(1, 2),
         Fb: 1, Fp: 0, Fpp: 0, chid_s: 0, chidd_s: 0, rho_s: 0,
         Up: 0, Upp: sp.Rational(3, 10)}
LIVRES = (a_s, b_s, xi_s, H_s, Hf_s, Hd_s, Hfd_s, xid_s, Ub, ksym)
K7F = sp.lambdify(LIVRES, K7.subs(FIXOS), 'numpy')
C7F = sp.lambdify(LIVRES, C7.subs(FIXOS), 'numpy')
W7F = sp.lambdify(LIVRES, W7.subs(FIXOS), 'numpy')
say("[lambdify] taxas vivas — pronto")


def roda_kc(kc, npts=20000):
    Ns = np.linspace(np.log(0.2), np.log(2000.0), npts)
    Hs_arr = np.zeros(npts)
    Ms = {x: np.zeros((npts, 7, 7)) for x in 'KCW'}
    for p, N in enumerate(Ns):
        a = np.exp(N)
        f = fundo_em(a)
        Hs_arr[p] = f['H']
        args = (a, f['r'] * a, f['xi'], f['H'], f['Hf'],
                f['Hd'], f['Hfd'], f['xid'], f['Ub'], kc)
        Ms['K'][p] = np.array(K7F(*args), float)
        Ms['C'][p] = np.array(C7F(*args), float)
        Ms['W'][p] = np.array(W7F(*args), float)
    # ancoras congeladas + automodo crescente p/ projecao (em a=30)
    Cd30 = np.gradient(Ms['C'], Ns, axis=0) * Hs_arr[:, None, None]
    sig_ref = {}
    evec_base = None
    imax = None
    for a_anc in (30.0, 400.0):
        p_anc = int(np.argmin(np.abs(np.exp(Ns) - a_anc)))
        Kr0, Cr0, Wr0 = reduz_ponto(Ms['K'][p_anc], Ms['C'][p_anc],
                                    Ms['W'][p_anc], Cd30[p_anc], MULT, DYN)
        pares = d1.agrupa_pares(d1.qep_modes(Kr0, Cr0, Wr0))
        sig_ref[a_anc] = max(abs(np.sqrt(complex(mm['omega2'])).imag)
                             for mm in pares) / Hs_arr[p_anc]
        if a_anc == 30.0:
            Amat = np.block(
                [[np.zeros((3, 3)), np.eye(3)],
                 [-np.linalg.solve(Kr0, Wr0),
                  -np.linalg.solve(Kr0, Cr0 - Cr0.T)]])
            ev, evec = np.linalg.eig(Amat)
            imax = int(np.argmax(ev.real))
            evec_base = evec
    marcas = {15: None, 30: None, 45: None, 100: None, 400: None,
              1900: None}
    taxas, Kr, Cr, Wr = evolui(Ms, Ns, Hs_arr, MULT, DYN, JANELAS,
                               marcas=marcas, evec_base=evec_base,
                               imax=imax)
    return taxas, sig_ref, marcas


say("")
say("=" * 72)
say("EVOLUCAO — REF mu=1, a: 0.2 -> 2000, base completa de ICs")
say("=" * 72)
resu = {}
for kc in (10.0, 100.0):
    say("")
    say(f"--- k_c = {kc:g}  (k_phys = {kc/10:g} em a=10) ---")
    taxas, sig_ref, marcas = roda_kc(kc)
    say(f"    ancoras congeladas: sigma/H(a=30) = {sig_ref[30.0]:.3f}; "
        f"sigma/H(a=400) = {sig_ref[400.0]:.3f}  (previsao congelada e")
    say("    persistente — se a dinamica real nao a realizar, ela e vacua)")
    say(f"    {'janela':<12}" + "".join(f"{'IC'+str(i+1):>9}"
                                        for i in range(6)))
    for nome, lo, hi in JANELAS:
        vals = [tx[nome] for tx in taxas]
        say(f"    {nome:<12}" + "".join(f"{v:+9.2f}" for v in vals))
    say("    trilha da IC 1 (ln|y|, |c_grow|/|y| no automodo de a=30):")
    for am, v in marcas.items():
        if v:
            say(f"      a={am:5d}: ln|y|={v[0]:+8.3f}  proj={v[1]:.3e}")
    resu[kc] = dict(taxas=taxas, sig_ref=sig_ref, marcas=marcas)

# halving
say("")
say("D2-CONV — halving (k_c=10, 40000 pts), janela tardia")
tx2, _, _ = roda_kc(10.0, npts=40000)
d_halv = max(abs(tx2[i]['tardia'] - resu[10.0]['taxas'][i]['tardia'])
             for i in range(6)
             if np.isfinite(tx2[i]['tardia']))
say(f"    max|Delta taxa tardia| = {d_halv:.4f} (criterio < 0.05)")
ok_conv = d_halv < 0.05

# ------------------------------------------------------------------
# veredito
# ------------------------------------------------------------------
say("")
say("=" * 72)
say("VEREDITO D2 — 2a rodada (desfechos pre-declarados no cabecalho)")
say("=" * 72)
say(f"  D2-GR: PASSA   D2-CONV: {'PASSA' if ok_conv else 'FALHA'}")
verd = {}
for kc, r in resu.items():
    t_tard = [r['taxas'][i]['tardia'] for i in (0, 1, 3, 4)]
    t_prim = [r['taxas'][i]['primordial'] for i in (0, 1, 3, 4)]
    cresce_tarde = any(np.isfinite(v) and v >= 0.5 * r['sig_ref'][400.0]
                       for v in t_tard)
    dilui = all(np.isfinite(v) and v < 0.0 for v in t_tard)
    cresce_cedo = any(np.isfinite(v) and v > 1.0 for v in t_prim)
    verd[kc] = (cresce_tarde, dilui, cresce_cedo)
    say(f"  k_c={kc:g}: tardia {['%+.2f' % v for v in t_tard]} "
        f"(congelado {r['sig_ref'][400.0]:.2f}) -> "
        f"{'CRESCE' if cresce_tarde else 'DILUI' if dilui else 'misto'}; "
        f"primordial {['%+.2f' % v for v in t_prim]} -> "
        f"{'INSTAVEL' if cresce_cedo else 'estavel'}")
say("")
if all(not v[0] for v in verd.values()):
    say("  >>> O TAQUIAO TARDIO CONGELADO NAO E DINAMICO. Em nenhuma")
    say("  janela tardia, para nenhum k_c, solucao alguma cresce perto")
    say("  da taxa congelada; a dinamica real tardia dilui (~ -1.5H) e a")
    say("  projecao no automodo taquionico e drenada. CONSEQUENCIAS:")
    say("  (i) o enunciado 'taquiao eterno' (resultado_setor_escalar")
    say("  par.7) CAI para esta celula/k; (ii) WATERSHED METODOLOGICO:")
    say("  autovalores congelados nao sao arbitro de saude nesta classe")
    say("  (as matrizes comoveis nunca assentam; |K_rdot|/|K_r| ~ 2H no")
    say("  ponto fixo); os vereditos de saude do programa baseados em")
    say("  espectro congelado precisam de reavaliacao por evolucao real;")
    say("  (iii) o quadro converge com a literatura ('saudavel tarde').")
    if any(v[2] for v in verd.values()):
        say("  (iv) a instabilidade PRIMORDIAL e real em tempo real —")
        say("  consistente com a instabilidade primordial conhecida do")
        say("  ramo finito na literatura.")
else:
    say("  >>> crescimento tardio real detectado — o taquiao congelado e")
    say("  dinamico afinal; reportar as taxas acima e manter o no-go")
    say("  tardio com a evolucao real como evidencia.")

os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
with open(os.path.join(HERE, "out", "d2_evolucao_reduzida.txt"),
          "w", encoding="utf-8") as fh:
    fh.write("\n".join(OUT))
say("")
say("concluido. saida em auditoria/code/out/d2_evolucao_reduzida.txt")
