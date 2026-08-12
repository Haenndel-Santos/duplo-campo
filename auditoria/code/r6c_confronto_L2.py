# -*- coding: utf-8 -*-
"""
r6c_confronto_L2.py — CONFRONTO DAS DUAS L2: a nossa (tdcp_pert_lib,
Gamma-Gamma covariante) vs a da reauditoria externa (ADM, pacote
TDCP_R6_reaudit_complete_2). Decide QUAL acao quadratica esta errada.

CONTEXTO (2026-08-12): r6b_degenerescencia_K mostrou que o nosso
K_red 3x3 tem autovalor negativo ESTAVEL (dps 15/30/60, h-sweep:
variacao fator 1.0) — nao e roundoff. A reauditoria externa obtem
det K_metric = 0 SIMBOLICO na L2 dela. Dois resultados exatos e
opostos => uma das duas L2 tem erro de algebra (as reducoes de ambas
usam o mesmo Schur; a parametrizacao dos 7 campos e IDENTICA, mesmos
nomes, mesmos fatores; RATES nossa ḃ = b·xi·H_f = convencao deles).

PRIOR EXTERNO RELEVANTE: no benchmark beta-constante (F'=F''=0) a
teoria e Hassan-Rosen puro + escalar espectador. Literatura (teorema
HR; Comelli-Crisostomi-Pilo FRW) => setor escalar metrico tem 1 DOF.
A L2 deles reproduz isso; a nossa da 2 (um de norma negativa). Mas o
prior nao decide algebra — este script decide.

METODO — teste de identidade POR PECAS com aritmetica racional EXATA:
  As L2 podem diferir por derivada total  d/dt[ q S q ]  (S simetrica):
     Delta K = 0   (invariante de IPP em forma de 1a ordem);
     Delta C = S   (simetrica);
     Delta W = -Sdot,  Sdot = aH dS/da + b xi H_f dS/db  (ponto fixo).
  Por peca (EH_g, EH_f, INT, CHI — cada peca e a MESMA densidade
  lagrangiana nas duas construcoes, entao a equivalencia vale peca a
  peca):
    T1: K_th - K_ours = 0 exatamente (subs racionais off-shell).
    T2: S := C_th - C_ours e simetrica.
    T3: (W_th - W_ours) + Sdot = 0.
  Betas SIMBOLICOS na reconstrucao deles (b0,b1,b2,b4 nossos simbolos)
  => a comparacao localiza tambem dentro da peca INT por beta.
  Off-shell: nenhuma relacao de fundo (Friedmann/ponto-fixo) e usada
  nos testes T1-T3 — pontos aleatorios racionais em
  (a,b,xi,H,H_f,Ub,b0,b1,b2,b4,k). Exato: zero e zero.

  T4 (consequencia): no ponto fixo beta1=1, K_red de cada engine com
  a MESMA reducao (absorcao Cdot + Schur, a nossa de producao):
  espectro e det do bloco (Psi_f,E_f). Reproduz det~0 deles e
  det<0 nosso, agora com causa localizada.

CRITERIOS (pre-declarados):
  T1 falha em alguma peca -> a discrepancia e CINETICA e nasce nessa
      peca; reportar entradas nao-nulas de Delta K (simbolicas se
      compactas). A peca culpada indica qual engine auditar no ramo
      seguinte (r6d: veredito GR do setor (Psi,E)).
  T1 passa e T2/T3 falham -> discrepancia em C/W alem de IPP; mesma
      logica de localizacao.
  Tudo passa -> as acoes SAO equivalentes e o erro esta nas reducoes;
      T4 vira o objeto central.

NOTA: os scripts externos vem do pacote enviado pelo autor
(TDCP_R6_reaudit_complete_2.zip, sessao ChatGPT de 2026-08-12),
preservados em auditoria/external/r6_reaudit_chatgpt/. O engine ADM
deles e importado; a funcao build deles e replicada verbatim abaixo
(com betas simbolicos), com atribuicao. Nao ha execucao de codigo
nao-inspecionado: o r6b_cubic_adm.py deles foi lido (adm_eh/zavg2/
esym conferidos; so define funcoes, main protegido).

Requer sympy, numpy, mpmath. ~3-8 min.
Uso (raiz do repo, venv ativo):
    python auditoria/code/r6c_confronto_L2.py
Saida em auditoria/code/out/r6c_confronto_L2.txt
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

EXT = os.path.normpath(os.path.join(
    HERE, '..', 'external', 'r6_reaudit_chatgpt', 'scripts',
    'r6b_cubic_adm.py'))

spec = importlib.util.spec_from_file_location("d1mod",
    os.path.join(DCODE, "01_setor_escalar_K_Omega.py"))
d1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(d1)

spec2 = importlib.util.spec_from_file_location("ext_adm", EXT)
ext = importlib.util.module_from_spec(spec2)
spec2.loader.exec_module(ext)

from tdcp_pert_lib import (t, a_s, b_s, xi_s, H_s, Hf_s, Hd_s, Hfd_s, xid_s,
                           chid_s, chidd_s, Mg2, Mf2, m2, Meff2,
                           b0, b1, b2, b3, b4, Fb, Fp, Fpp,
                           Ub, Up, Upp, rho_s, k as ksym, eps as oeps,
                           quadratic_matrices, lagrangian_GG,
                           interaction_lagrangian, chi_lagrangian,
                           scalar_metric_g, scalar_metric_f,
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

say("=" * 72)
say("R-6c — CONFRONTO DAS DUAS L2 (nossa Gamma-Gamma vs ADM externa)")
say("=" * 72)

# ------------------------------------------------------------------
# 1. L2 NOSSA, por pecas (replica d1.build_L2, separando as pecas)
# ------------------------------------------------------------------
say("[nossa] montando pecas EH_g, EH_f, INT, CHI ...")
Phi_gF = sp.Function('Phi_g')(t)
B_gF = sp.Function('B_g')(t)
Phi_fF = sp.Function('Phi_f')(t)
Psi_fF = sp.Function('Psi_f')(t)
B_fF = sp.Function('B_f')(t)
E_fF = sp.Function('E_f')(t)
dchiF = sp.Function('dchi')(t)
FUNCS = [Phi_gF, B_gF, Phi_fF, Psi_fF, B_fF, E_fF, dchiF]

aF, bF, xiF, bg_rules = make_bg_functions()
gmet = substitute_bg_functions(
    scalar_metric_g(Phi_gF, sp.Integer(0), B_gF, None), aF, bF, xiF)
fmet = substitute_bg_functions(
    scalar_metric_f(Phi_fF, Psi_fF, B_fF, E_fF), aF, bF, xiF)

PECAS_N = {}
PECAS_N['EH_g'] = lagrangian_GG(gmet, Mg2)
PECAS_N['EH_f'] = lagrangian_GG(fmet, Mf2)
PECAS_N['INT'] = interaction_lagrangian(gmet, fmet, dchi=dchiF)
PECAS_N['CHI'] = chi_lagrangian(gmet, dchi=dchiF)

SUB_N = {Mg2: 1, Mf2: 1, m2: 1, Meff2: sp.Rational(1, 2), rho_s: 0,
         Fb: 1, Fp: 0, Fpp: 0, b3: 0,
         Hd_s: 0, Hfd_s: 0, xid_s: 0, chid_s: 0, chidd_s: 0,
         Up: 0, Upp: sp.Rational(3, 10)}

MATS_N = {}
for nome, Lp in PECAS_N.items():
    L2p = z_average(eps_part(cut(Lp), 2))
    L2s, fields, vels = symbolize(L2p, FUNCS, bg_rules)
    if [str(f) for f in fields] != NOMES:
        raise RuntimeError(f"ordem de campos mudou em {nome}")
    K, C, W = quadratic_matrices(L2s, fields, vels)
    MATS_N[nome] = tuple(M.subs(SUB_N) for M in (K, C, W))
    say(f"    [nossa {nome}] K,C,W prontos")

# ------------------------------------------------------------------
# 2. L2 EXTERNA, por pecas — replica do build_symbolic_L2 do
#    r6c_gatef_adm_reaudit.py (pacote externo), com betas simbolicos
#    (b0,b1,b2,b4 nossos) no potencial. Engine: r6b_cubic_adm deles.
# ------------------------------------------------------------------
say("[externa] montando pecas via engine ADM deles ...")
eeps, ez, ek = ext.eps, ext.z, ext.k
cutE, cutME, inv_seriesE = ext.cut, ext.cutM, ext.inv_series
sqrt_det4E, mat_sqrtE, esymE, adm_ehE, zavg2E = \
    ext.sqrt_det4, ext.mat_sqrt, ext.esym, ext.adm_eh, ext.zavg2

aT, bT, xiT, HT, HfT, UbT, b1T = sp.symbols(
    'a b xi H H_f Ubar beta1', positive=True)
cz, sz = sp.cos(ek * ez), sp.sin(ek * ez)
Pg, Bg, Pf, Ps, Bf, Ef, D = sp.symbols('Phi_g B_g Phi_f Psi_f B_f E_f dchi')
Psd, Efd, Dd = sp.symbols('Psi_fdot E_fdot dchidot')

gE = sp.zeros(4, 4)
gE[0, 0] = -(1 + 2 * eeps * Pg * cz)
gE[0, 3] = gE[3, 0] = -aT * ek * eeps * Bg * sz
for i in (1, 2, 3):
    gE[i, i] = aT**2
gdE = sp.diag(2 * aT**2 * HT, 2 * aT**2 * HT, 2 * aT**2 * HT)

fE = sp.zeros(4, 4)
fE[0, 0] = -xiT**2 * (1 + 2 * eeps * Pf * cz)
fE[0, 3] = fE[3, 0] = -bT * xiT * ek * eeps * Bf * sz
fE[1, 1] = bT**2 * (1 - 2 * eeps * Ps * cz)
fE[2, 2] = fE[1, 1]
fE[3, 3] = bT**2 * (1 - 2 * eeps * Ps * cz - 2 * ek**2 * eeps * Ef * cz)
hbf = xiT * HfT
fdE = sp.zeros(3, 3)
fdE[0, 0] = 2 * bT**2 * hbf * (1 - 2 * eeps * Ps * cz) \
    - 2 * bT**2 * eeps * Psd * cz
fdE[1, 1] = fdE[0, 0]
fdE[2, 2] = 2 * bT**2 * hbf * (1 - 2 * eeps * Ps * cz
                               - 2 * ek**2 * eeps * Ef * cz) \
    - 2 * bT**2 * eeps * (Psd * cz + ek**2 * Efd * cz)

PECAS_E = {}
PECAS_E['EH_g'] = adm_ehE(gE, gdE, 1, 2)
say("    [externa EH_g] ok")
PECAS_E['EH_f'] = adm_ehE(fE, fdE, 1, 2)
say("    [externa EH_f] ok")

AE = mat_sqrtE(cutME(inv_seriesE(gE, 2) * fE, 2), 2)
e0E, e1E, e2E, e3E, e4E = esymE(AE, 2)
VE = cutE(b0 * e0E + b1 * e1E + b2 * e2E + b4 * e4E, 2)
PECAS_E['INT'] = cutE(-sp.Rational(1, 2) * sqrt_det4E(gE, 2) * VE, 2)
say("    [externa INT] ok")

giE = inv_seriesE(gE, 2)
dmE = [eeps * Dd * cz, 0, 0, -eeps * ek * D * sz]
kinE = 0
for mu in range(4):
    for nu in range(4):
        kinE += giE[mu, nu] * dmE[mu] * dmE[nu]
kinE = cutE(-kinE / 2, 2)
UpotE = UbT + sp.Rational(3, 20) * (eeps * D * cz)**2
PECAS_E['CHI'] = cutE(sqrt_det4E(gE, 2) * cutE(kinE - UpotE, 2), 2)
say("    [externa CHI] ok")

CAMPOS_E = [Pg, Bg, Pf, Ps, Bf, Ef, D]
VELS_E = [sp.Symbol(n + 'dot') for n in NOMES]
SUB_VE = {Psd: VELS_E[3], Efd: VELS_E[5], Dd: VELS_E[6]}
CANON = {HT: H_s, HfT: Hf_s, UbT: Ub, b1T: b1}

MATS_E = {}
for nome, Lp in PECAS_E.items():
    L2p = zavg2E(sp.expand(cutE(Lp, 2)).coeff(eeps, 2))
    L2p = sp.expand(L2p.subs(SUB_VE))
    K = sp.zeros(7, 7)
    C = sp.zeros(7, 7)
    W = sp.zeros(7, 7)
    for i in range(7):
        for j in range(7):
            K[i, j] = sp.diff(L2p, VELS_E[i], VELS_E[j])
            C[i, j] = sp.diff(L2p, VELS_E[i], CAMPOS_E[j])
            W[i, j] = -sp.diff(L2p, CAMPOS_E[i], CAMPOS_E[j])
    MATS_E[nome] = tuple(M.subs(CANON) for M in (K, C, W))
    say(f"    [externa {nome}] K,C,W prontos")

# ------------------------------------------------------------------
# 3. T1/T2/T3 — identidade por pecas, racional exato
# ------------------------------------------------------------------
LIVRES = [a_s, b_s, xi_s, H_s, Hf_s, Ub, b0, b1, b2, b4, ksym]
PONTOS = [
    dict(zip(LIVRES, map(sp.Rational,
        ('13/7', '5/3', '7/9', '3/11', '5/13', '-2/7',
         '2/5', '8/3', '-3/7', '5/6', '9/4')))),
    dict(zip(LIVRES, map(sp.Rational,
        ('3/2', '11/6', '2/5', '7/8', '1/6', '4/9',
         '-1/3', '5/7', '9/5', '-2/9', '6/5')))),
    dict(zip(LIVRES, map(sp.Rational,
        ('21/8', '4/7', '13/9', '5/12', '8/5', '1/10',
         '7/6', '-3/8', '2/11', '10/7', '3/4')))),
]


def sdot_fp(S):
    """Sdot no ponto fixo: aH dS/da + b xi H_f dS/db."""
    return sp.expand(a_s * H_s * sp.diff(S, a_s)
                     + b_s * xi_s * Hf_s * sp.diff(S, b_s))


def aval(M, pt):
    return M.subs(pt)


say("")
say("T1/T2/T3 — identidade por pecas (3 pontos racionais off-shell):")
say(f"{'peca':>6} {'T1 dK=0':>10} {'T2 S sim':>10} {'T3 dW+Sdot':>12}")
culpados = []
detalhe = {}
for nome in ('EH_g', 'EH_f', 'INT', 'CHI'):
    KN, CN, WN = MATS_N[nome]
    KE, CE, WE = MATS_E[nome]
    dK = sp.expand(KE - KN)
    S = sp.expand(CE - CN)
    dW = sp.expand(WE - WN)
    Sd = sdot_fp(S)
    asym = sp.expand(S - S.T)
    resT3 = sp.expand(dW + Sd)
    ok1 = ok2 = ok3 = True
    for pt in PONTOS:
        if any(x != 0 for x in aval(dK, pt)):
            ok1 = False
        if any(x != 0 for x in aval(asym, pt)):
            ok2 = False
        if any(x != 0 for x in aval(resT3, pt)):
            ok3 = False
    say(f"{nome:>6} {'PASSA' if ok1 else 'FALHA':>10} "
        f"{'PASSA' if ok2 else 'FALHA':>10} "
        f"{'PASSA' if ok3 else 'FALHA':>12}")
    if not (ok1 and ok2 and ok3):
        culpados.append(nome)
        detalhe[nome] = (dK, asym, resT3)

# ------------------------------------------------------------------
# 3b. localizacao fina das pecas culpadas
# ------------------------------------------------------------------
for nome in culpados:
    dK, asym, resT3 = detalhe[nome]
    say("")
    say(f"  --- localizacao {nome} ---")
    pt = PONTOS[0]
    for rot, M in (('dK', dK), ('S-S.T', asym), ('dW+Sdot', resT3)):
        nz = [(i, j) for i in range(7) for j in range(i, 7)
              if aval(M[i, j], pt) != 0]
        if not nz:
            say(f"    {rot}: zero")
            continue
        say(f"    {rot}: entradas nao-nulas {[(NOMES[i], NOMES[j]) for i, j in nz]}")
        for i, j in nz[:6]:
            expr = sp.factor(sp.simplify(M[i, j]))
            txt = sp.sstr(expr)
            if len(txt) > 300:
                txt = txt[:300] + " ..."
            say(f"      [{NOMES[i]},{NOMES[j]}] = {txt}")

# ------------------------------------------------------------------
# 4. T4 — consequencia no ponto fixo: K_red dos dois engines com a
#    MESMA reducao de producao (absorcao Cdot + Schur), mpmath dps=40
# ------------------------------------------------------------------
say("")
say("T4 — K_red no ponto fixo beta1=1 (mesma reducao nos dois):")
mp.mp.dps = 40


def fixo_r(B1):
    B0n, B2n, B4n = mp.mpf(1), mp.mpf('-0.4'), mp.mpf('0.5')
    kap = mp.mpf(1)
    rr = mp.polyroots([kap * B4n - 3 * B2n, -3 * B1,
                       3 * kap * B2n - B0n, kap * B1],
                      maxsteps=200, extraprec=100)
    reais = sorted(x.real for x in rr
                   if abs(mp.im(x)) < mp.mpf('1e-30') and mp.re(x) > 0)
    r = reais[0]
    Vf = B4n + 3 * B2n / r**2 + B1 / r**3
    H = mp.sqrt(mp.mpf('0.5') * r * r * Vf / 3)
    Ubv = 3 * H**2 - mp.mpf('0.5') * (B0n + 3 * B1 * r + 3 * B2n * r**2)
    return r, H, Ubv


def reduz_mp(K, C, W, Cd):
    n = 7
    K = K.copy()
    C = C.copy()
    W = W.copy()
    for i in MULT:
        for j in range(n):
            cij = C[i, j]
            cd = Cd[i, j]
            if i == j:
                W[i, i] += cd
            else:
                W[i, j] += cd
                W[j, i] += cd
                C[j, i] -= cij
        for j in range(n):
            C[i, j] = mp.mpf(0)
    WXX = mp.matrix(4, 4)
    for ii, i in enumerate(MULT):
        for jj, j in enumerate(MULT):
            WXX[ii, jj] = W[i, j]
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


for rot, MATS in (('nossa', MATS_N), ('externa', MATS_E)):
    KT = sum((MATS[n][0] for n in MATS), sp.zeros(7, 7))
    CT = sum((MATS[n][1] for n in MATS), sp.zeros(7, 7))
    WT = sum((MATS[n][2] for n in MATS), sp.zeros(7, 7))
    CdT = sp.zeros(7, 7)
    for i in range(7):
        for j in range(7):
            CdT[i, j] = sdot_fp(CT[i, j])
    r, H, Ubv = fixo_r(mp.mpf(1))
    aval_n = {a_s: sp.Float(mp.nstr(mp.mpf(3635), 35), 35)}
    av = mp.mpf(3635)
    subs = {a_s: sp.Float(str(av), 40), b_s: sp.Float(mp.nstr(r * av, 40), 40),
            xi_s: sp.Float(mp.nstr(r, 40), 40),
            H_s: sp.Float(mp.nstr(H, 40), 40),
            Hf_s: sp.Float(mp.nstr(H / r, 40), 40),
            Ub: sp.Float(mp.nstr(Ubv, 40), 40),
            b0: 1, b1: 1, b2: sp.Rational(-2, 5), b4: sp.Rational(1, 2),
            ksym: sp.Float(mp.nstr(45 * fixo_r(mp.mpf(1))[1] * 100, 40), 40)}

    def tomp(M):
        Mm = mp.matrix(7, 7)
        for i in range(7):
            for j in range(7):
                Mm[i, j] = mp.mpf(sp.sstr(sp.N(M[i, j].subs(subs), 40)))
        return Mm

    Kr = reduz_mp(tomp(KT), tomp(CT), tomp(WT), tomp(CdT))
    K2 = mp.matrix(2, 2)
    for ii, i in enumerate((0, 1)):
        for jj, j in enumerate((0, 1)):
            K2[ii, jj] = (Kr[i, j] + Kr[j, i]) / 2
    det2 = mp.det(K2)
    esc = max(abs(K2[i, j]) for i in range(2) for j in range(2))
    lam = mp.eigsy(K2, eigvals_only=True)
    say(f"  [{rot:>7}] bloco (Psi_f,E_f): K2 = "
        f"[[{mp.nstr(K2[0,0],8)}, {mp.nstr(K2[0,1],8)}], "
        f"[{mp.nstr(K2[1,0],8)}, {mp.nstr(K2[1,1],8)}]]")
    say(f"            det = {mp.nstr(det2, 8)}; det/esc^2 = "
        f"{mp.nstr(det2 / esc**2, 6)}; autovalores = "
        f"{mp.nstr(lam[0], 6)}, {mp.nstr(lam[1], 6)}")

# ------------------------------------------------------------------
say("")
say("=" * 72)
say("VEREDITO R-6c (criterios pre-declarados no cabecalho)")
say("=" * 72)
if not culpados:
    say("  T1/T2/T3 PASSARAM em todas as pecas: as duas L2 sao a MESMA")
    say("  acao (a menos de derivada total). O erro esta nas reducoes;")
    say("  T4 acima e o objeto a auditar.")
else:
    say(f"  Pecas com discrepancia REAL (alem de derivada total): "
        f"{culpados}")
    say("  A(s) peca(s) acima e(sao) o local do erro de algebra de uma")
    say("  das duas engines. Proximo ramo (r6d): veredito GR do setor")
    say("  (Psi,E) — a engine cuja peca EH reproduz GR esta certa.")

os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
with open(os.path.join(HERE, 'out', 'r6c_confronto_L2.txt'), 'w',
          encoding='utf-8') as fh:
    fh.write("\n".join(OUT) + "\n")
say("")
say("saida escrita em auditoria/code/out/r6c_confronto_L2.txt")
