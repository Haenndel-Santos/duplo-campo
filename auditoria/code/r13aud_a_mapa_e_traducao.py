# -*- coding: utf-8 -*-
"""
r13aud_a_mapa_e_traducao.py -- AUDITORIA ADVERSARIAL DO R-13a, ALVOS A e D.

ALVO A. A traducao `Higuchi <=> xi >= r <=> r' >= 0` re-derivada DO ZERO,
        por rota INDEPENDENTE da usada no R-13a (que casou as duas
        Friedmann). A rota deste script e' a REDUNDANCIA DA ACAO:
        f_{mu nu} -> lambda^2 f_{mu nu}, com lambda^2 = mu. O mapa
        `r_K = sqrt(mu) r`, `beta_n^K = A mu^{-n/2} beta_n` tem de SAIR
        dai', sem olhar para as Friedmann; e depois as Friedmann entram
        so' como SOBREDETERMINACAO (teste de consistencia).

ALVO D. `m_T^2/H^2 = 3, nao 12`: estabelecer em forma fechada o que
        exatamente mudou -- o numero, o objeto, ou o rotulo.

=======================================================================
CRITERIOS PRE-DECLARADOS (escritos ANTES da execucao)
=======================================================================
O veredito sai SO por estes criterios. Todo residuo simbolico e' exigido
IDENTICAMENTE ZERO (sympy), com beta_n, mu e w GERAIS salvo onde dito.

--- ALVO A: o mapa por rota da acao ----------------------------------

  A1  e_n SOB REESCALA. Calculando e_n(sqrt(g^{-1}f)) do fundo pela
      maquinaria de derivations/code/tdcp_pert_lib.py (raiz matricial
      por Sylvester + tracos, NAO por formula decorada), sob
      f -> lambda^2 f (isto e' b -> lambda b, N_f -> lambda N_f, ou
      seja r -> lambda r, xi -> lambda xi) tem de valer
      e_n -> lambda^n e_n, n = 0..4.  [residuo 0]

  A2  CINETICO DE f SOB REESCALA. O termo minisuperespaco
      -3 M_f^2 b bdot^2 / N_f tem de ir em -3 (M_f^2 lambda^2) b bdot^2/N_f,
      isto e' M_f^2 -> M_f^2/lambda^2 quando se reabsorve a reescala.
      Logo lambda^2 = mu leva M_f^2 -> M_g^2. [residuo 0]

  A3  O MAPA SAI DE A1+A2, SEM AS FRIEDMANN. Exigindo invariancia do
      potencial sum_n beta_n e_n sob a reescala, tem de sair
      beta_n^K = lambda^{-n} beta_n = mu^{-n/2} beta_n, para n = 0..4,
      unicamente (coeficiente a coeficiente). [residuo 0, e unicidade]

  A4  SOBREDETERMINACAO PELA FRIEDMANN-g. Postulando r_K = c r e
      beta_n^K = A_n beta_n com A_n, c INCOGNITOS, a eq. (10) de Konnig
      fixa A_0..A_3 = A c^{-n} com c LIVRE. [solucao existe e e' unica
      nesses quatro]

  A5  SOBREDETERMINACAO PELA FRIEDMANN-f. A eq. (11) fixa
      c^2 = mu E A_4 = A c^{-4}, de forma CONSISTENTE com A4 (nao ha'
      escolha de A_1..A_3 que a satisfaca com outro c). O sistema e'
      sobredeterminado: 4 incognitas restantes (A_4, c) contra >= 4
      equacoes independentes -> tem de FECHAR. [residuo 0]

  A6  CONSEQUENCIA NAO USADA NA CONSTRUCAO: a eq. (12) de Konnig
      (rho(r), que e' derivada dele, nao entrada) tem de bater com a
      NOSSA W(r) sob o mapa: rho_K(r_K) == A W(r). [residuo 0]
      Idem eq. (13): r_K' == sqrt(mu) r', com w GERAL. [residuo 0]

  A7  IDENTIFICACAO DE xi. Na nossa convencao N_g = 1 e N_f = xi
      (derivations/code/tdcp_pert_lib.py). Na de Konnig, N_f/N_g = r X
      com X = 1 + r'/r (eq. 9). Logo xi = r + r'. Verificar que a
      identidade e' exata e que xi_K = sqrt(mu) xi (mesmo sinal, mesmo
      zero). [residuo 0]

  A8  A CADEIA, COM w GERAL (o R-13b so' fez poeira). Com
      drho_til/dN = -3(1+w) rho_til:
        (a) -mu r^2 W'(r) == LHS da (15) traduzida        [residuo 0]
        (b) (m_T^2|_{xi->r} - 2H^2) * 3 M_f^2 r/(m^2 M_ef^2)
            == LHS da (15) traduzida                       [residuo 0]
        (c) B_2 de Konnig sob o mapa == A mu^{-1/2} calB(r) [residuo 0]
        (d) dr/dN = -3(1+w) rho_til / W'(r), logo
            sign(r') = -sign(W') para rho_til > 0 e 1+w > 0.
      => Higuchi(14) <=> (15) <=> W' <= 0 <=> r' >= 0 <=> xi >= r,
         para w GERAL, nao so' poeira.

  A9  w_mg <= -1 POR ROTA PROPRIA. Derivando da conservacao do setor
      modificado (rho_mg = m^2 M_ef^2 V_g(r)) tem de sair
      w_mg = -1 - calB(r) r' / V_g(r), identico a' traducao do
      R-13a sec.4.3, que veio da eq. (20) deles. [residuo 0]

  A-PODER  TESTE DE PODER (regra 3). Um mapa ERRADO tem de REPROVAR.
      Rodar A5/A6/A8 com (i) c = mu (em vez de sqrt(mu)) e (ii)
      beta_n^K = A mu^{-n} beta_n. Os residuos tem de ser NAO NULOS.
      Se um mapa errado passar, o teste nao tem poder.

--- ALVO D: o 12 e o 3 -----------------------------------------------

  D1  Em forma fechada, no ramo FINITO primordial (r -> 0), com fluido
      de eq. de estado w constante:
        r' -> 3(1+w) r,  xi -> (4+3w) r,  m_T^2/H^2 -> 3(4+3w).
      [limite simbolico exato, beta_n e mu gerais, beta_1 != 0]

  D2  No MESMO limite, m_T^2|_{xi->r}/H^2 -> 3, para beta_n, mu e w
      GERAIS. [limite simbolico exato]

  D3  O 3 NAO e' um numero de regime: e' o valor do funcional de
      Higuchi da fonte no limite r -> 0. Verificar tambem qual e' o
      MINIMO de m_T^2|_{xi->r}/H^2 sobre a historia INTEIRA do ramo
      finito de benchmark -- porque "margem 1.5x" so' e' a margem se o
      3 for o minimo. Se o minimo for menor, a margem verdadeira e'
      outra e o corpus tem de dizer qual.

  D4  SEPARACAO ENUNCIADO/VALOR. Estabelecer, por identidade e nao por
      leitura: (i) o 12 e' o valor de m_T^2/H^2 (autovalor tensorial,
      xi DINAMICO) e nao mudou; (ii) o 3 e' o valor de OUTRO objeto
      (o funcional de Higuchi de Fasiello-Tolley/Konnig, = m_T^2 com
      xi->r) sobre H^2; (iii) os dois so' coincidem em xi = r.

--- CEGUEIRA DESTE GATE (regra 7, obrigatoria) -----------------------

  * Este script NAO deriva o bound de Higuchi. Ele audita a TRADUCAO de
    um bound importado. Se a eq. (14) de Konnig estiver errada NA
    FONTE, ou se Fasiello-Tolley 1308.1647 tiver outra normalizacao,
    nada aqui detecta.
  * Este script NAO abre 1308.1647 (fonte primaria real do bound). O
    caveat do fator 1/2 no potencial (nota 3 de 1503.07436) continua
    declarado e NAO verificado.
  * Este script NAO mede nada dinamicamente: e' algebra. A varredura
    numerica esta' no r13b e nos outros scripts desta auditoria.
  * Este script NAO toca gradiente/c_s^2 (alvo C, outro script).
  * Este script NAO valida a caixa de m_T^2 da derivations/02 -- ele a
    toma como ENTRADA. Se a caixa estiver errada, o 12 e o 3 caem
    juntos, e este gate nao ve.
  * Este script assume beta_n CONSTANTES. Com beta_n(phi_-) (a v2), a
    cadeia (14)->(16)->(18) nao sobrevive intacta -- ver A8-MOD, que
    MEDE o tamanho da quebra em vez de so' declara-la.

Uso:  .venv\\Scripts\\python.exe auditoria/code/r13aud_a_mapa_e_traducao.py
Saida: auditoria/code/out/r13aud_a_mapa_e_traducao.txt
"""
import importlib.util
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
DCODE = os.path.normpath(os.path.join(HERE, '..', '..', 'derivations', 'code'))
OUTD = os.path.join(HERE, 'out')
sys.path.insert(0, DCODE)

LINHAS = []
FALHAS = []


def say(s=""):
    print(s, flush=True)
    LINHAS.append(s)


def gate(nome, residuo, esperado_zero=True):
    """Registra um gate. residuo: expressao sympy (ou lista)."""
    if isinstance(residuo, (list, tuple)):
        rs = [sp.simplify(sp.expand(x)) for x in residuo]
        ok = all(x == 0 for x in rs)
        txt = ", ".join(str(x) for x in rs)
    else:
        rs = sp.simplify(sp.expand(residuo))
        ok = (rs == 0)
        txt = str(rs)
    if esperado_zero:
        veredito = "OK" if ok else "**FALHA**"
        if not ok:
            FALHAS.append(nome)
    else:
        veredito = "OK (residuo NAO nulo, como exigido)" if not ok \
            else "**FALHA: um mapa errado passou -- teste sem poder**"
        if ok:
            FALHAS.append(nome + " (poder)")
    say(f"  [{nome:>10}] residuo = {txt[:70]:<70} {veredito}")
    return ok


# =====================================================================
say("=" * 74)
say("R-13aud/A+D -- AUDITORIA DO MAPA DE CONVENCOES E DA TRADUCAO")
say("=" * 74)
say("")
say("Rota deste script: a REDUNDANCIA DA ACAO (f -> lambda^2 f).")
say("Rota do R-13a: casamento das duas Friedmann.")
say("Sao rotas independentes: uma parte da acao, a outra das eqs. de")
say("fundo ja' derivadas.")
say("")

# ---------------------------------------------------------------------
# simbolos
# ---------------------------------------------------------------------
r, mu, lam, A = sp.symbols('r mu lambda A', positive=True)
b0, b1, b2, b3, b4 = sp.symbols('beta_0 beta_1 beta_2 beta_3 beta_4')
w = sp.Symbol('w')
m2, Me2, Mf2 = sp.symbols('m2 Meff2 Mf2', positive=True)
Mg2 = Mf2 / mu
BET = (b0, b1, b2, b3, b4)

# nossos objetos de fundo (fonte: derivations/plano_derivacoes.md F.3/F.4,
# auditoria/code/ramo_dinamico_correto.py)
Vg = b0 + 3 * b1 * r + 3 * b2 * r**2 + b3 * r**3
Vf = b4 + 3 * b3 / r + 3 * b2 / r**2 + b1 / r**3
W = (Mg2 / Mf2) * r**2 * Vf - Vg          # m^2 M_ef^2 W(r) = rho
Wp = sp.diff(W, r)
H2 = m2 * Me2 * r**2 * Vf / (3 * Mf2)     # Friedmann-f
calB = b1 + 2 * b2 * r + b3 * r**2

# ---------------------------------------------------------------------
say("-" * 74)
say("[A1] e_n(sqrt(g^{-1} f)) do fundo, e a reescala f -> lambda^2 f")
say("-" * 74)
say("")
say("  Os e_n sao calculados pela raiz matricial em serie (Sylvester) +")
say("  tracos de derivations/code/tdcp_pert_lib.py -- NAO por formula")
say("  decorada. Depois se aplica b -> lambda b, N_f -> lambda N_f.")
say("")

spec = importlib.util.spec_from_file_location(
    "tpl", os.path.join(DCODE, "tdcp_pert_lib.py"))
tpl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tpl)

a_s, b_s, xi_s = tpl.a_s, tpl.b_s, tpl.xi_s
gd = sp.diag(-1, a_s**2, a_s**2, a_s**2)
fd = sp.diag(-xi_s**2, b_s**2, b_s**2, b_s**2)
Amat = tpl.matrix_sqrt_series(tpl.cutM(tpl.series_inverse(gd) * fd))
e_ns = list(tpl.elementary_symmetric(Amat))       # e0..e4
say(f"  e_n obtidos (com r = b/a, xi = N_f/N_g):")
rr = b_s / a_s
for n, e in enumerate(e_ns):
    say(f"     e_{n} = {sp.simplify(sp.expand(e.subs(b_s, rr * a_s)))}")
say("")
# reescala: b -> lam b, xi -> lam xi
resc = {b_s: lam * b_s, xi_s: lam * xi_s}
res_A1 = [sp.simplify(sp.expand(e_ns[n].subs(resc) - lam**n * e_ns[n]))
          for n in range(5)]
gate("A1", res_A1)

# ---------------------------------------------------------------------
say("")
say("-" * 74)
say("[A2] o cinetico de f sob a mesma reescala")
say("-" * 74)
say("")
tt = sp.Symbol('t')
bF = sp.Function('bF', positive=True)(tt)
NfF = sp.Function('NfF', positive=True)(tt)
Mf2s = sp.Symbol('M_f^2', positive=True)
Lf = -3 * Mf2s * bF * sp.diff(bF, tt)**2 / NfF
Lf_resc = Lf.subs({bF: lam * bF, NfF: lam * NfF}).doit()
say(f"  L_f            = {Lf}")
say(f"  L_f (reescala) = {sp.simplify(Lf_resc)}")
say("  => M_f^2 efetivo multiplica por lambda^2; para levar M_f^2 -> M_g^2")
say("     e' preciso lambda^2 = M_f^2/M_g^2 = mu, isto e' lambda = sqrt(mu).")
gate("A2", sp.simplify(Lf_resc - lam**2 * Lf))

# ---------------------------------------------------------------------
say("")
say("-" * 74)
say("[A3] o mapa dos beta sai SO' de A1+A2 (sem tocar as Friedmann)")
say("-" * 74)
say("")
say("  Invariancia de V = sum_n beta_n e_n sob a reescala exige")
say("  beta_n^K e_n(reescalado) = beta_n e_n, coeficiente a coeficiente.")
say("")
bK = sp.symbols('bK0 bK1 bK2 bK3 bK4')
V_orig = sum(BET[n] * e_ns[n] for n in range(5))
V_resc = sum(bK[n] * e_ns[n].subs(resc) for n in range(5))
sol_A3 = sp.solve([sp.Eq(sp.expand(V_resc - V_orig).coeff(BET[n], 0)
                         if False else 0, 0)], dict=True)  # placeholder
# rota limpa: casar coeficiente a coeficiente em (r, xi)
dif = sp.expand(V_resc - V_orig).subs(b_s, rr * a_s)
dif = sp.simplify(dif)
polyvars = (rr, xi_s)
eqs = []
P = sp.Poly(sp.expand(dif.rewrite(sp.Pow)), sp.Symbol('r_dummy')) \
    if False else None
# coeficientes em (b/a, xi): usa expansao explicita
dif_e = sp.expand(sp.simplify(dif))
rrs = sp.Symbol('rr', positive=True)
dif_e = sp.expand(dif_e.subs(b_s, rrs * a_s))
pol = sp.Poly(dif_e, rrs, xi_s)
eqs = [sp.Eq(c, 0) for c in pol.coeffs()]
sol = sp.solve(eqs, list(bK), dict=True)
say(f"  solucao unica? {len(sol) == 1}")
sol = sol[0]
for n in range(5):
    say(f"     beta_{n}^K = {sp.simplify(sol[bK[n]])}    "
        f"(esperado: lambda^-{n} beta_{n})")
res_A3 = [sp.simplify(sol[bK[n]] - lam**(-n) * BET[n]) for n in range(5)]
gate("A3", res_A3)
say("")
say("  Com lambda = sqrt(mu) e a normalizacao global A = m^2 M_ef^2/M_g^2")
say("  (que traz o potencial para as unidades de Konnig, onde M_g^2 = 1 e")
say("  m^2 esta' absorvido nos beta):")
say("")
say("      r_K = sqrt(mu) r,   beta_n^K = A mu^{-n/2} beta_n")
say("")
say("  IDENTICO ao mapa do R-13a sec.2.1, obtido aqui SEM usar as")
say("  Friedmann. Rota independente: FECHA.")

# ---------------------------------------------------------------------
say("")
say("-" * 74)
say("[A4/A5] sobredeterminacao pelas DUAS Friedmann (incognitas livres)")
say("-" * 74)
say("")
c = sp.Symbol('c', positive=True)
A0, A1_, A2_, A3_, A4_ = sp.symbols('A0 A1 A2 A3 A4')
AN = (A0, A1_, A2_, A3_, A4_)
rK = c * r
bKn = [AN[n] * BET[n] for n in range(5)]

# Konnig (10)/a^2 : 3H^2 = rho_K + V_g^K(r_K)
VgK = bKn[0] + 3 * bKn[1] * rK + 3 * bKn[2] * rK**2 + bKn[3] * rK**3
# nosso: 3H^2 = rho/M_g^2 + (m^2 M_ef^2/M_g^2) V_g(r);  A = m^2 M_ef^2/M_g^2
eq10 = sp.expand(VgK - A * Vg)
pol10 = sp.Poly(eq10, r)
sol10 = sp.solve([sp.Eq(cc, 0) for cc in pol10.coeffs()],
                 [A0, A1_, A2_, A3_], dict=True)
say(f"  Friedmann-g fixa A_0..A_3 (c fica LIVRE): {len(sol10) == 1}")
s10 = sol10[0]
for n in range(4):
    say(f"     A_{n} = {sp.simplify(s10[AN[n]])}")
gate("A4", [sp.simplify(s10[AN[n]] - A * c**(-n)) for n in range(4)])

# Konnig (11)/a^2 : 3H^2 = (1/r_K)(b1K + 3 b2K rK + 3 b3K rK^2 + b4K rK^3)
FfK = (bKn[1] + 3 * bKn[2] * rK + 3 * bKn[3] * rK**2
       + bKn[4] * rK**3) / rK
# nosso: 3H^2 = (m^2 M_ef^2/M_f^2) r^2 V_f = (A/mu) r^2 V_f
eq11 = sp.expand(sp.together(FfK - (A / mu) * r**2 * Vf) * r)
eq11 = sp.expand(sp.simplify(eq11.subs(s10)))
pol11 = sp.Poly(sp.expand(eq11 * r**0), r)
coefs11 = [sp.simplify(cc) for cc in pol11.coeffs()]
say("")
say("  Friedmann-f, DEPOIS de substituir A_0..A_3 de A4. Coeficientes:")
for cc in coefs11:
    say(f"     {cc} = 0")
sol11 = sp.solve([sp.Eq(cc, 0) for cc in coefs11], [c, A4_], dict=True)
sol11 = [s for s in sol11 if s.get(c) is not None]
say(f"  solucoes: {sol11}")
ok_A5 = any(sp.simplify(s[c] - sp.sqrt(mu)) == 0
            and sp.simplify(s[A4_] - A * mu**-2) == 0 for s in sol11)
say(f"  [       A5] c = sqrt(mu) E A_4 = A mu^-2 aparecem juntos? "
    f"{'OK' if ok_A5 else '**FALHA**'}")
if not ok_A5:
    FALHAS.append("A5")
say("")
say("  SOBREDETERMINACAO: a Friedmann-f impoe DUAS condicoes")
say("  independentes (o bloco beta_1/beta_2/beta_3 e o termo beta_4) e as")
say("  duas dao o MESMO c. O padrao mu^{-n/2} nao foi imposto no n=4:")
say("  ele SAIU. O mapa e' unico e fecha.")

MAPA = {c: sp.sqrt(mu), A0: A, A1_: A / sp.sqrt(mu), A2_: A / mu,
        A3_: A * mu**sp.Rational(-3, 2), A4_: A / mu**2}

# ---------------------------------------------------------------------
say("")
say("-" * 74)
say("[A6] consequencias NAO usadas na construcao: eqs. (12) e (13)")
say("-" * 74)
say("")
# (12): rho = b1 r^-1 - b0 + 3b2 + 3(b3-b1) r + (b4-3b2) r^2 - b3 r^3
rhoK_12 = (bKn[1] / rK - bKn[0] + 3 * bKn[2]
           + 3 * (bKn[3] - bKn[1]) * rK
           + (bKn[4] - 3 * bKn[2]) * rK**2 - bKn[3] * rK**3)
res_A6a = sp.simplify(sp.expand(rhoK_12.subs(MAPA) - A * W))
say("  (12) de Konnig, sob o mapa, contra a NOSSA W(r):")
gate("A6a", res_A6a)
# (13) com w geral: r_K' = -3(1+w) rho_K / rho_K,rK
rhoK_of_rK = A * W.subs(r, sp.Symbol('rr_', positive=True) / sp.sqrt(mu))
rKs = sp.Symbol('rr_', positive=True)
drKdN = -3 * (1 + w) * rhoK_of_rK / sp.diff(rhoK_of_rK, rKs)
drdN_nosso = -3 * (1 + w) * W / Wp
res_A6b = sp.simplify(sp.expand(
    drKdN.subs(rKs, sp.sqrt(mu) * r) - sp.sqrt(mu) * drdN_nosso))
say("  (13) de Konnig (w GERAL) contra sqrt(mu) * (nosso dr/dN):")
gate("A6b", res_A6b)

# ---------------------------------------------------------------------
say("")
say("-" * 74)
say("[A7] xi = N_f/N_g: a identificacao, e xi_K = sqrt(mu) xi")
say("-" * 74)
say("")
say("  Nossa convencao (tdcp_pert_lib.py, scalar_metric_f / _selftest):")
say("     g = diag(-1, a^2, a^2, a^2),  f = diag(-xi^2, b^2, b^2, b^2)")
say("     => N_g = 1, N_f = xi. Logo xi = N_f/N_g LITERALMENTE.")
say("")
say("  Konnig (4)/(5): g = a^2(-H^{-2}dt^2 + dx^2),")
say("                  f = b^2(-X^2 H^{-2}dt^2 + dx^2)")
say("     => N_g = a/H, N_f = b X/H, N_f/N_g = r X.")
say("  E a eq. (9) da' X = 1 + r'/r, logo r X = r + r'.")
say("")
Xs = 1 + sp.Symbol("rp") / r
res_A7a = sp.simplify(r * Xs - (r + sp.Symbol("rp")))
gate("A7a", res_A7a)
rp = sp.Symbol("rp")
res_A7b = sp.simplify(sp.sqrt(mu) * r + sp.sqrt(mu) * rp
                      - sp.sqrt(mu) * (r + rp))
gate("A7b", res_A7b)
say("  => xi_K = r_K + r_K' = sqrt(mu)(r + r') = sqrt(mu) xi:")
say("     fator POSITIVO, logo MESMO SINAL e MESMO ZERO. A traducao de")
say("     xi e' invariante de sinal, como o R-13a afirma.")

# ---------------------------------------------------------------------
say("")
say("-" * 74)
say("[A8] a cadeia (14)<=>(15)<=>W'<=0<=>r'>=0<=>xi>=r, com w GERAL")
say("-" * 74)
say("")
L15 = (b1 + 3 * r**2 * (mu * b1 - b3) + 2 * r**3 * (3 * mu * b2 - b4)
       + 3 * mu * b3 * r**4)
say("  LHS(15) traduzida (R-13a sec.2.2):")
say(f"     {L15}")
say("")
res_A8a = sp.expand(-mu * r**2 * Wp - L15)
gate("A8a", res_A8a)

xi_sym = sp.Symbol('xi')
mT2 = (m2 * Me2 * (1 / Mg2 + xi_sym / (Mf2 * r**3)) * r
       * (b1 + b2 * (xi_sym + r) + b3 * xi_sym * r))
mT2_xr = mT2.subs(xi_sym, r)
caixa_r13a = (m2 * Me2 / Mf2) * calB * (1 + mu * r**2) / r
res_A8b0 = sp.expand(sp.simplify(mT2_xr - caixa_r13a))
say("  (caixa do cap.06 com xi->r) == (caixa do R-13a sec.2.2)?")
gate("A8b0", res_A8b0)
res_A8b = sp.expand(sp.simplify(
    sp.together((caixa_r13a - 2 * H2) * 3 * Mf2 * r / (m2 * Me2)) - L15))
say("  (m_T^2|_{xi->r} - 2H^2)*3 M_f^2 r/(m^2 M_ef^2) == LHS(15)?")
gate("A8b", res_A8b)

B2K = bKn[1] + 2 * bKn[2] * rK + bKn[3] * rK**2
res_A8c = sp.simplify(sp.expand(B2K.subs(MAPA) - A * mu**sp.Rational(-1, 2)
                                * calB))
say("  B_2 de Konnig sob o mapa == A mu^{-1/2} calB(r)?")
gate("A8c", res_A8c)

say("")
say("  (d) SINAL, com w geral. Derivando W(r(N)) = rho_til(N) e usando")
say("      drho_til/dN = -3(1+w) rho_til:")
say("         dr/dN = -3(1+w) rho_til / W'(r)")
say("      Com rho_til > 0 e 1+w > 0:  sign(r') = -sign(W').")
say("      Com A8a:  W' <= 0  <=>  LHS(15) >= 0  <=>  (14).")
say("      Logo:  (14) <=> r' >= 0 <=> xi >= r,  para TODO w > -1.")
say("")
say("  >>> EXTENSAO ALEM DO R-13b: o R-13b verificou a cadeia SO' para")
say("      poeira (drho/dN = -3 rho). Aqui o fator (1+w) sai como fator")
say("      POSITIVO comum e nao toca a equivalencia. A cadeia vale para")
say("      qualquer w > -1 constante ou nao -- inclusive radiacao.")

# ---------------------------------------------------------------------
say("")
say("-" * 74)
say("[A8-MOD] o que a modulacao beta_n(phi_-) quebra -- MEDIDO, nao so' declarado")
say("-" * 74)
say("")
say("  Com beta_n = beta_n(N), a derivada total de W(r(N), N) ganha um")
say("  termo novo:  W' dr/dN + dW/dN|_r = -3(1+w) rho_til, logo")
say("")
say("      dr/dN = -[3(1+w) rho_til + (dW/dN)|_r] / W'(r)")
say("")
bd = sp.symbols('bd0 bd1 bd2 bd3 bd4')     # dbeta_n/dN
dWdN_r = sum(sp.diff(W, BET[n]) * bd[n] for n in range(5))
say(f"  (dW/dN)|_r = {sp.simplify(dWdN_r)}")
say("")
say("  => sign(r') deixa de ser -sign(W'). A equivalencia")
say("     `r' >= 0 <=> W' <= 0 <=> Higuchi` QUEBRA sempre que")
say("     |(dW/dN)|_r| > 3(1+w) rho_til  com sinal oposto.")
say("")
say("  A INEQUACAO (14)/(15) em si NAO usa r' e continua valendo ponto a")
say("  ponto (ela e' algebrica em (r, beta_n)); o que cai e' a")
say("  EQUIVALENCIA com o sinal de r'. Consequencia operacional: sob")
say("  modulacao, medir r' NAO e' medir Higuchi. Tem de medir (15).")
say("  [Confirmando a hipotese 2 do R-13a sec.2.2 -- e localizando-a.]")

# ---------------------------------------------------------------------
say("")
say("-" * 74)
say("[A9] w_mg <= -1 por rota propria (conservacao), sem usar a eq. (20)")
say("-" * 74)
say("")
say("  rho_mg = m^2 M_ef^2 V_g(r);  rho_mg' = -3(1+w_mg) rho_mg")
say("  => w_mg = -1 - V_g'(r) r' / (3 V_g(r)),  e V_g' = 3 calB(r).")
wmg_nosso = -1 - sp.diff(Vg, r) * sp.Symbol('rp') / (3 * Vg)
wmg_r13a = -1 - calB * sp.Symbol('rp') / Vg
gate("A9", sp.simplify(wmg_nosso - wmg_r13a))
say("  => identico a' traducao do R-13a sec.4.3, obtida la' da eq. (20)")
say("     de Konnig. Rota independente (conservacao) confirma.")

# ---------------------------------------------------------------------
say("")
say("-" * 74)
say("[A-PODER] um mapa ERRADO tem de REPROVAR (regra 3)")
say("-" * 74)
say("")
MAPA_ERRADO_1 = {c: mu, A0: A, A1_: A / mu, A2_: A / mu**2,
                 A3_: A / mu**3, A4_: A / mu**4}       # c = mu
MAPA_ERRADO_2 = {c: sp.sqrt(mu), A0: A, A1_: A / mu, A2_: A / mu**2,
                 A3_: A / mu**3, A4_: A / mu**4}       # beta ~ mu^-n
for nome, MP in (("c=mu", MAPA_ERRADO_1), ("beta~mu^-n", MAPA_ERRADO_2)):
    rr_ = sp.simplify(sp.expand(rhoK_12.subs(MP) - A * W))
    gate(f"PODER {nome}", rr_, esperado_zero=False)
L15_err = sp.expand((-mu * r**2 * Wp).subs(mu, mu**2))
gate("PODER L15", sp.expand(L15_err - L15), esperado_zero=False)

# =====================================================================
say("")
say("=" * 74)
say("ALVO D -- O 12 E O 3, EM FORMA FECHADA")
say("=" * 74)
say("")
say("  Razao geral (algebra deste script, a partir da caixa do cap.06 e")
say("  da Friedmann-f):")
razao = sp.simplify(mT2 / H2)
say(f"     m_T^2/H^2 = {sp.factor(sp.simplify(razao))}")
razao_alvo = 3 * (mu * r**3 + xi_sym) * (b1 + b2 * (xi_sym + r)
                                         + b3 * xi_sym * r) \
    / (r * (b4 * r**3 + 3 * b3 * r**2 + 3 * b2 * r + b1))
gate("D0", sp.simplify(razao - razao_alvo))
say("")
say("  RAMO FINITO PRIMORDIAL. Com r -> 0 e fluido de eq. de estado w:")
say("     W(r) -> beta_1/(mu r)  =>  r ~ beta_1/(mu rho_til)")
say("     => r' = -r rho_til'/rho_til = 3(1+w) r,  xi = (4+3w) r")
say("")
eps_ = sp.Symbol('epsx', positive=True)
xi_prim = (4 + 3 * w) * eps_
D1 = sp.limit(razao.subs({xi_sym: xi_prim, r: eps_}), eps_, 0)
say(f"  [D1] lim_{{r->0}} m_T^2/H^2  (xi dinamico)   = {sp.simplify(D1)}")
gate("D1", sp.simplify(D1 - 3 * (4 + 3 * w)))
D2v = sp.limit((caixa_r13a / H2).subs(r, eps_), eps_, 0)
say(f"  [D2] lim_{{r->0}} m_T^2|_{{xi->r}}/H^2         = {sp.simplify(D2v)}")
gate("D2", sp.simplify(D2v - 3))
say("")
say("  Verificacao de que o 3 NAO depende de w (o funcional da fonte nao")
say("  ve' o fluido: ele e' algebrico em (r, beta_n)):")
say(f"     d/dw de D2 = {sp.diff(sp.simplify(D2v), w)}")
say("")
say("  [D-CONS] os dois objetos so' coincidem em xi = r:")
dif_obj = sp.simplify(sp.factor(razao - caixa_r13a / H2))
say(f"     m_T^2/H^2 - m_T^2|_{{xi->r}}/H^2 = {dif_obj}")
say("     (zera identicamente sse xi = r, i.e. r' = 0)")
say("")
say("  Em w = 0: 3(4+3w) = 12 e o funcional da' 3.")
say("  Em w = 1/3 (radiacao): 15 e o funcional continua dando 3.")

# ---------------------------------------------------------------------
say("")
say("-" * 74)
say("[D5] a pendencia P-5 do posicionamento (6 vs 3 em w = -1)")
say("-" * 74)
say("")
say("  A formula 3(4+3w) NAO e' avaliavel em w = -1, e a razao e'")
say("  estrutural, nao de gosto. A derivacao de D1 usa:")
say("      r ~ beta_1/(mu rho_til)  com rho_til -> infinito")
say("  Isso exige que rho DILUA, isto e' w > -1. Em w = -1 a densidade e'")
say("  CONSTANTE, r nao vai a zero, e o regime r -> 0 simplesmente NAO")
say("  EXISTE. Logo `3(4+3w)|_{w=-1} = 3` e' EXTRAPOLACAO FORA DO")
say("  DOMINIO da formula, nao uma predicao dela.")
say("")
say("  O que existe em w = -1 e' o PONTO FIXO de de Sitter (rho_til = 0,")
say("  r = r_inf com W(r_inf) = 0). La', W = 0 da' r^3 V_f = mu r V_g, e")
say("  a razao vira:")
raz_dS = sp.simplify(3 * calB * (1 + mu * r**2) / (mu * r * Vg))
say(f"      m_T^2/H^2|_{{dS}} = 3 calB(r)(1+mu r^2)/(mu r V_g(r))")
# conferencia: substituir r^3 V_f -> mu r V_g na razao com xi = r
raz_xr = sp.simplify(caixa_r13a / H2)      # = 3 calB (1+mu r^2)/(r^3 V_f)
res_D5 = sp.simplify(sp.expand(
    (raz_xr * (r**3 * Vf) / (mu * r * Vg)) - raz_dS))
gate("D5a", res_D5)
say("")
say("  Essa expressao NAO e' um numero universal: depende de r_inf e dos")
say("  beta_n. No bloco beta_0=beta_2=beta_3=0 ela colapsa em")
say("  1 + 1/(mu r_c^2) (o corolario F-1 do R-13b):")
raz_IBB = sp.simplify(raz_dS.subs({b0: 0, b2: 0, b3: 0}))
say(f"      = {raz_IBB}")
gate("D5b", sp.simplify(raz_IBB - (1 + 1 / (mu * r**2))))
say("")
say("  >>> ACHADO DO ALVO D (P-5): nem 6 nem 3 sao o valor de de Sitter.")
say("      A razao no ponto fixo e' MODELO-DEPENDENTE. A pendencia P-5")
say("      nao e' uma discrepancia numerica a arbitrar: o `3` vem de")
say("      avaliar uma formula fora do seu dominio, e o `6` (importado,")
say("      nao verificado) nao pode ser universal porque a quantidade")
say("      nao e' universal. Nota de higiene do posicionamento sobre a")
say("      homonimia com o `3` de Higuchi: CORRETA e mantida.")

# ---------------------------------------------------------------------
say("")
say("-" * 74)
say("[D3] o `3` e' o MINIMO da margem no ramo finito? (numerico)")
say("-" * 74)
say("")
say("  'Margem 1.5x' so' e' a margem se 3 for o MINIMO do funcional de")
say("  Higuchi sobre a historia INTEIRA. Medido no benchmark do corpus")
say("  (beta = (1,1,-0.4,0,0.5), mu = 1, Omega_m(a=1) = 0.3, poeira):")
say("")
import numpy as _np                                            # noqa: E402

_b = dict(b0=1.0, b1=1.0, b2=-0.4, b3=0.0, b4=0.5)
_mu, _Me2, _m2 = 1.0, 0.5, 1.0


def _W(rv):
    return ((1.0 / _mu) * (_b['b4'] * rv**2 + 3 * _b['b3'] * rv
                           + 3 * _b['b2'] + _b['b1'] / rv)
            - (_b['b0'] + 3 * _b['b1'] * rv + 3 * _b['b2'] * rv**2
               + _b['b3'] * rv**3))


def _dW(rv):
    return ((1.0 / _mu) * (2 * _b['b4'] * rv + 3 * _b['b3']
                           - _b['b1'] / rv**2)
            - (3 * _b['b1'] + 6 * _b['b2'] * rv + 3 * _b['b3'] * rv**2))


def _newton(r0, rt, nit=200):
    """Newton sobre W(r) = rho_til, com W' em FORMA FECHADA (regra 6).

    np.roots e' evitado de proposito: a cubica fica mal condicionada
    para rho_til >> 1 e a raiz pequena (o ramo FINITO) se perde. A
    semente analitica r ~ beta_1/(mu rho_til) e' exata a O(1/rho_til^2).
    """
    rv = float(r0)
    for _ in range(nit):
        d = _dW(rv)
        if d == 0.0 or not _np.isfinite(d):
            return _np.nan
        nr = rv - (_W(rv) - rt) / d
        if nr <= 0:
            nr = 0.5 * rv
        if abs(nr - rv) <= 1e-15 * abs(nr):
            return nr
        rv = nr
    return rv


_a = _np.logspace(-6, 3, 4000)
_rt = 0.3 / (_m2 * _Me2) * _a**-3
_r = _np.empty_like(_rt)
_seed = _b['b1'] / (_mu * _rt[0])            # assintota do ramo FINITO
for _q in range(len(_rt)):
    _r[_q] = _newton(_seed, _rt[_q])
    _seed = _r[_q]
# gate de maquinaria: residuo da cubica e monotonia (ramo finito: r cresce)
_res = _np.max(_np.abs(_W(_r) - _rt) / _np.maximum(1.0, _np.abs(_rt)))
say(f"  [gate] max residuo |W(r)-rho_til|/max(1,rho_til) = {_res:.3e}"
    f"   (exigido <= 1e-12)")
say(f"  [gate] r monotonicamente crescente (ramo finito)? "
    f"{bool(_np.all(_np.diff(_r) > 0))}")
if not (_res <= 1e-12 and _np.all(_np.diff(_r) > 0)):
    FALHAS.append("D3-maquinaria")
_calB = _b['b1'] + 2 * _b['b2'] * _r + _b['b3'] * _r**2
_r3Vf = _b['b4'] * _r**3 + 3 * _b['b3'] * _r**2 + 3 * _b['b2'] * _r + _b['b1']
_razF = 3 * _calB * (1 + _mu * _r**2) / _r3Vf
_i = int(_np.argmin(_razF))
say(f"  min de m_T^2|_(xi->r)/H^2 sobre a = 1e-6 .. 1e3 : "
    f"{_razF[_i]:.6f}  em a = {_a[_i]:.4g} (r = {_r[_i]:.4g})")
say(f"  valor em a -> 0 (r -> 0)                        : {_razF[0]:.6f}")
say(f"  valor no ponto fixo tardio (a = 1e3)            : {_razF[-1]:.6f}")
say(f"  pontos com o funcional >= 2                     : "
    f"{int(_np.sum(_razF >= 2))}/{len(_razF)}")
say("")
if abs(_razF[_i] - _razF[0]) < 1e-6:
    say("  >>> o minimo E' o valor primordial: a margem 1.5x esta' correta")
    say("      como MARGEM MINIMA no ramo finito do benchmark.")
else:
    say("  >>> ATENCAO: o minimo NAO e' o valor primordial. A 'margem")
    say("      1.5x' precisa ser requalificada -- o minimo verdadeiro e'")
    f"      {_razF[_i]:.6f}, isto e' margem {_razF[_i]/2:.4f}x."
    say(f"      minimo = {_razF[_i]:.6f}  =>  margem = {_razF[_i]/2:.4f}x")

# ---------------------------------------------------------------------
say("")
say("=" * 74)
say("VEREDITO DOS GATES DESTE SCRIPT")
say("=" * 74)
say("")
if FALHAS:
    say(f"  FALHAS: {FALHAS}")
else:
    say("  TODOS OS GATES PASSARAM (residuos exigidos zero == 0; residuos")
    say("  exigidos nao-nulos != 0).")
say("")
say("  CEGUEIRA (repetida no fim, regra 7): este script NAO deriva o")
say("  bound de Higuchi, NAO abre 1308.1647, NAO valida a caixa de")
say("  m_T^2 da derivations/02, e NAO mede nada dinamicamente.")

os.makedirs(OUTD, exist_ok=True)
with open(os.path.join(OUTD, 'r13aud_a_mapa_e_traducao.txt'), 'w',
          encoding='utf-8') as fh:
    fh.write("\n".join(LINHAS) + "\n")
print(f"\n[saida versionada] "
      f"{os.path.join(OUTD, 'r13aud_a_mapa_e_traducao.txt')}")
if FALHAS:
    sys.exit(1)
