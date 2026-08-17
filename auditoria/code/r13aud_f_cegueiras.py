# -*- coding: utf-8 -*-
"""
r13aud_f_cegueiras.py -- AUDITORIA ADVERSARIAL DO R-13b, ALVO F.

O R-13b declara que NAO MEDE GRADIENTE. O alvo F pede: liste o que MAIS
ele nao consegue ver, e diga se alguma dessas cegueiras MORDE o veredito.

Este script nao se limita a listar: MEDE o tamanho das cegueiras que sao
mensuraveis, para que "morde / nao morde" seja conclusao e nao opiniao.

=======================================================================
CRITERIOS PRE-DECLARADOS (escritos ANTES da execucao)
=======================================================================

  F1  MODULACAO beta_n(phi_-) -- A CEGUEIRA QUE PODE MORDER.
      Com beta_n dependentes do tempo, dr/dN ganha um termo:
          dr/dN = -[3(1+w) rho_til + (dW/dN)|_r] / W'(r)
      e como W' > 0 no ramo infinito (teorema E1), o sinal de r' passa
      a depender do numerador. CRITERIO: derivar em FORMA FECHADA o
      limiar de d(beta_1)/dN acima do qual r' >= 0, para a subclasse
      F1 (so' beta_1 modulado), e MEDI-LO em celulas concretas. Se o
      limiar for atingivel por uma modulacao lenta (|dln beta_1/dN|
      da ordem de 1), a cegueira MORDE o veredito para a v2.

      [EMENDA DECLARADA, pos-execucao. O criterio acima estava MAL
       POSTO e a 1a leitura que fiz dele foi ERRADA -- registro aqui,
       nao escondo. Ele identifica "cegueira que morde" com "sinal de
       r' inverte". Mas Higuchi nao e' o sinal de r': e' a eq. (15),
       que e' `-mu r^2 W'(r) >= 0`. So' o ULTIMO elo da cadeia
       (`W' <= 0 <=> r' >= 0`) usa dr/dN, e e' so' esse elo que a
       modulacao quebra. O criterio corrigido, e o que o bloco mede,
       e': (i) o limiar de dbeta_1/dN que inverte r' -- exibido; e
       (ii) se LHS(15) se move com dbeta_1/dN -- ela NAO se move.
       Logo a mordida e' no ARGUMENTO, nao no VEREDITO.]

  F2  CONTEUDO DE MATERIA (radiacao, vacuo escalar). CRITERIO: mostrar
      que o teorema E1 nao usa a forma de rho_til(N) -- so' rho_til > 0
      e 1 + w_tot > 0 --, logo r' < 0 sobrevive a QUALQUER conteudo com
      essas duas propriedades. Verificar numericamente com
      rho = rho_m a^-3 + rho_r a^-4.

  F3  A CAIXA DE m_T^2. O R-13b usa a caixa da derivations/02 como
      ENTRADA. CRITERIO: separar quais enunciados do R-13b dependem
      dela e quais nao. Se o veredito de exclusao (r' < 0 <=> Higuchi
      violado) for INDEPENDENTE da caixa, a cegueira NAO morde o
      veredito -- so' os numeros tensoriais.

  F4  ESTENCIL / REGRA 6 DENTRO DO PROPRIO R-13b. O alvo C mostrou que
      h = 1e-3 com estencil de 8a ordem PODE falhar em fundo com r
      grande. CRITERIO: verificar se algum numero DECISIVO do R-13b
      passa por estencil. Se todos forem forma fechada, a cegueira nao
      morde.

  F5  SELECAO DE RAIZ PERTO DO PONTO FIXO. CRITERIO: exibir que a
      semente pela assintota r ~ sqrt(mu rho/b4) converge para a raiz
      ERRADA quando a e' grande, e verificar se o R-13b esta' protegido
      (continuacao a partir do passado + gate M1(d)).

  F6  O QUE NENHUM GATE DESTE ARCO VE. Lista fechada, com o veredito
      de mordida para cada item.

--- CEGUEIRA DESTE PROPRIO SCRIPT (regra 7, recursiva) ---------------
  * Ele mede o LIMIAR de modulacao, nao a dinamica de phi_- da v2.
    Se a v2 nunca produzir d beta_1/dN acima do limiar, a cegueira e'
    inofensiva NA PRATICA -- e isso este script NAO decide.
  * Ele nao valida a caixa de m_T^2 nem a L2; so' rastreia dependencias.
  * Ele nao mede nada de perturbacao.

Uso:  .venv\\Scripts\\python.exe auditoria/code/r13aud_f_cegueiras.py
Saida: auditoria/code/out/r13aud_f_cegueiras.txt
"""
import os

import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
OUTD = os.path.join(HERE, 'out')
LINHAS, FALHAS = [], []


def _gradiente_proibido(*a, **k):
    raise RuntimeError("np.gradient e' PROIBIDO (regra 6, Erratum-03).")


np.gradient = _gradiente_proibido


def say(s=""):
    print(s, flush=True)
    LINHAS.append(s)


def gate(nome, ok, det=""):
    say(f"  [{nome:>7}] {'OK' if ok else '**FALHA**'}  {det}")
    if not ok:
        FALHAS.append(nome)


say("=" * 74)
say("R-13aud/F -- O QUE OS GATES DO ARCO R-13 NAO CONSEGUEM VER")
say("=" * 74)
say("")

# =====================================================================
say("-" * 74)
say("[F1] MODULACAO beta_n(phi_-): o limiar, em forma fechada e medido")
say("-" * 74)
say("")
r, mu, y, rho, w = sp.symbols('r mu y rho_til w', positive=True)
b1s, b4s = sp.symbols('beta_1 beta_4', positive=True)
db1 = sp.Symbol('dbeta_1')                      # d beta_1 / dN
W = (b4s * r**2 + b1s / r) / mu - 3 * b1s * r
Wp = sp.diff(W, r)
dWdN_r = sp.diff(W, b1s) * db1                  # so' beta_1 modulado (F1)
say(f"  W(r)      = {sp.simplify(W)}")
say(f"  W'(r)     = {sp.simplify(Wp)}")
say(f"  (dW/dN)|_r = dbeta_1 * {sp.simplify(sp.diff(W, b1s))}")
say("")
say("  dr/dN = -[3(1+w) rho_til + (dW/dN)|_r] / W'(r),  W' > 0 (teorema E1)")
say("  => r' >= 0  <=>  3(1+w) rho_til + dbeta_1 (1/(mu r) - 3 r) <= 0")
say("  => (como mu r^2 > 1 no ramo infinito, 3r - 1/(mu r) > 0)")
say("")
lim = sp.simplify(3 * (1 + w) * rho / (3 * r - 1 / (mu * r)))
say(f"      dbeta_1/dN  >=  {lim}      [LIMIAR]")
say("")
res = sp.simplify(sp.expand(
    (3 * (1 + w) * rho + lim * (1 / (mu * r) - 3 * r))))
gate("F1a", res == 0, f"consistencia do limiar: residuo = {res}")
say("")
say("  MEDIDA do limiar em celulas IBB genuinas (beta_1 = 1, poeira,")
say("  Omega_m(a=1) = 0.3). Reportado como dln(beta_1)/dN, que e' a")
say("  quantidade adimensional que a v2 tem de produzir:")
say("")


class Cel(object):
    def __init__(self, yv, muv):
        self.y, self.mu = yv, muv

    def W(self, rv):
        return (self.y * rv**2 + 1.0 / rv) / self.mu - 3.0 * rv

    def dW(self, rv):
        return (2 * self.y * rv - 1.0 / rv**2) / self.mu - 3.0

    def raizes(self, rt):
        z = np.roots([self.y / self.mu, -3.0, -rt, 1.0 / self.mu])
        return sorted(v.real for v in z
                      if abs(v.imag) < 1e-10 and v.real > 0)

    def newton(self, r0, rt):
        rv = float(r0)
        for _ in range(300):
            d = self.dW(rv)
            nr = rv - (self.W(rv) - rt) / d
            if nr <= 0:
                nr = 0.5 * rv
            if abs(nr - rv) <= 1e-15 * abs(nr):
                return nr
            rv = nr
        return rv


def r_c(c):
    return max(c.raizes(0.0))


def rt0_Om(c, Om=0.3):
    rc = r_c(c)
    lo, hi = rc * (1 + 1e-12), rc * 1e8
    for _ in range(300):
        mid = np.sqrt(lo * hi)
        Om_m = 1 - c.mu * (3 * mid) / (mid**2 * (c.y + 1.0 / mid**3))
        if Om_m < Om:
            lo = mid
        else:
            hi = mid
    return c.W(np.sqrt(lo * hi))


say(f"  {'mu':>6} {'b4/b1':>9} {'f':>6} {'a':>8} {'r':>12} "
    f"{'rho_til':>12} {'limiar dbeta_1/dN':>19} {'= dln b1/dN':>13}")
piores = []
for mu_v in (0.1, 1.0, 10.0):
    for f_v in (0.05, 0.5, 0.98):
        yv = f_v * 2.0 * mu_v**1.5
        c = Cel(yv, mu_v)
        rt0 = rt0_Om(c)
        seed = None
        for aval in (1e-3, 1e-2, 1.0, 30.0):
            rt = rt0 * aval**-3
            rr = c.raizes(rt)
            rv = c.newton(rr[-1] if seed is None else
                          min(rr, key=lambda z: abs(z - seed)), rt)
            seed = rv
            lim_v = 3.0 * rt / (3 * rv - 1.0 / (mu_v * rv))
            piores.append(lim_v)
            if mu_v == 1.0:
                say(f"  {mu_v:6.3g} {yv:9.4g} {f_v:6.2f} {aval:8.3g} "
                    f"{rv:12.5g} {rt:12.5g} {lim_v:19.6g} {lim_v:13.6g}")
say("")
say(f"  limiar MINIMO sobre todas as celulas e epocas: {min(piores):.6g}")
say(f"  limiar MAXIMO                                : {max(piores):.6g}")
say("")
say("  LEITURA. Com beta_1 = 1, dln(beta_1)/dN = dbeta_1/dN. O limiar e'")
say("  ENORME no passado profundo (acompanha rho_til ~ a^-3) e vai a ZERO")
say("  no futuro (rho_til -> 0). Logo, perto do atrator tardio, QUALQUER")
say("  modulacao com dbeta_1/dN positivo acima de um limiar que tende a")
say("  zero INVERTE o sinal de r'.")
say("")
say("  MAS -- e este e' o ponto que decide a mordida -- INVERTER O SINAL")
say("  DE r' NAO RESTAURA HIGUCHI. A cadeia do R-13a e':")
say("")
say("      Higuchi (14) <=> (15) >= 0 <=> -mu r^2 W'(r) >= 0 <=> W' <= 0")
say("")
say("  e SO' O ULTIMO ELO (W' <= 0 <=> r' >= 0) usa dr/dN. O elo")
say("  `(15) <=> W' <= 0` e' algebrico em (r, beta_n, mu) e NAO ve' a")
say("  modulacao. E o teorema E1 da' W'(r) > 0 sempre que")
say("      rho_til > 0   E   mu r^2 > 1")
say("  -- duas condicoes que NAO envolvem dbeta_n/dN.")
say("")
say("  Verificacao: sob modulacao, medir r' e' medir a coisa ERRADA.")
say("  Exemplo numerico (mu=1, y=1, a=30) com dbeta_1/dN acima do limiar:")
c_ex = Cel(1.0, 1.0)
rt0_ex = rt0_Om(c_ex)
rt_ex = rt0_ex * 30.0**-3
rr_ex = c_ex.raizes(rt_ex)
rv_ex = c_ex.newton(rr_ex[-1], rt_ex)
lim_ex = 3.0 * rt_ex / (3 * rv_ex - 1.0 / (c_ex.mu * rv_ex))
for fator in (0.0, 0.5, 1.0, 2.0, 10.0):
    dbeta = fator * lim_ex
    num = 3.0 * rt_ex + dbeta * (1.0 / (c_ex.mu * rv_ex) - 3 * rv_ex)
    rp = -num / c_ex.dW(rv_ex)
    L15 = -c_ex.mu * rv_ex**2 * c_ex.dW(rv_ex)
    say(f"    dbeta_1/dN = {dbeta:11.6g} ({fator:4.1f}x limiar) -> "
        f"r' = {rp:12.5g}  |  LHS(15) = {L15:12.6g}  -> Higuchi "
        f"{'OK' if L15 >= 0 else 'VIOLADO'}")
say("")
say("  r' troca de sinal; LHS(15) NAO se move (ela nem depende de")
say("  dbeta_1/dN). Higuchi continua VIOLADO.")
say("")
say("  >>> VEREDITO F1: a cegueira da modulacao NAO morde o veredito de")
say("      exclusao -- MAS morde o ARGUMENTO com que o corpus o defende.")
say("      Sob beta_n(phi_-):")
say("        - `r' < 0` DEIXA DE SER equivalente a violar Higuchi, e")
show = ("        - o diagnostico correto passa a ser `W'(r) > 0`, isto e'")
say(show)
say("          `mu r^2 > 1 e rho_til > 0` -- que e' o teorema E1 e vale")
say("          sem tocar em derivada temporal nenhuma.")
say("      O corpus tem de trocar o enunciado operacional. O R-13b diz")
say("      'a cadeia (14)->(16)->(18) nao sobrevive intacta' e para ai;")
say("      o que sobrevive, e e' suficiente, e' o elo (14) <=> (15).")
say("")
say("      RESSALVA HONESTA, e ela e' a fronteira real: tudo isso supoe")
say("      que a PROPRIA eq. (14) continue sendo a condicao de Higuchi")
say("      ponto a ponto sob modulacao. Essa hipotese e' declarada pelo")
say("      R-13a (sec.2.2, hipotese 2) e NAO foi verificada por ninguem")
say("      -- nem aqui. Se (14) ganhar termos em dbeta_n/dN na derivacao")
say("      hamiltoniana, nada deste bloco cobre o caso.")
say("")

# =====================================================================
say("")
say("-" * 74)
say("[F2] CONTEUDO DE MATERIA: radiacao NAO morde")
say("-" * 74)
say("")
say("  O teorema E1 usa apenas: (i) o ponto esta' no ramo infinito")
say("  (r > r_c), logo Q(r) = mu r rho_til > 0 e mu r^2 > 1; (ii)")
say("  rho_til > 0; (iii) 1 + w_tot > 0. NENHUM desses usa a FORMA de")
say("  rho_til(N). Logo r' < 0 vale para qualquer conteudo com rho > 0")
say("  e w_tot > -1 -- inclusive materia + radiacao.")
say("")
say("  Verificacao numerica com rho = rho_m a^-3 + rho_r a^-4 e")
say("  a_eq = 1/3400 (equipartição padrao):")
say("")
say(f"  {'a':>10} {'w_tot':>9} {'r':>13} {'rho_til':>13} "
    f"{'W-linha':>13} {'r-linha':>14} {'sinal':>8}")
c = Cel(1.0, 1.0)
rt0 = rt0_Om(c)
A_EQ = 1.0 / 3400
seed = None
n_neg = n_tot = 0
for aval in (1e-6, 1e-5, 1e-4, A_EQ, 1e-2, 0.1, 1.0, 30.0):
    rt = rt0 * (aval**-3 + A_EQ * aval**-4)
    rr = c.raizes(rt)
    rv = c.newton(rr[-1] if seed is None else
                  min(rr, key=lambda z: abs(z - seed)), rt)
    seed = rv
    fr = (A_EQ * aval**-4) / (aval**-3 + A_EQ * aval**-4)   # fracao radiacao
    wt = fr / 3.0
    rp = -3.0 * (1 + wt) * rt / c.dW(rv)
    n_tot += 1
    if rp < 0:
        n_neg += 1
    say(f"  {aval:10.4g} {wt:9.5f} {rv:13.6g} {rt:13.6g} "
        f"{c.dW(rv):13.6g} {rp:14.6g} "
        f"{'r-lin<0' if rp < 0 else 'r-lin>=0':>8}")
gate("F2", n_neg == n_tot, f"r' < 0 em {n_neg}/{n_tot} com radiacao ligada")
say("")
say("  >>> VEREDITO F2: a cegueira 'sem radiacao' NAO morde. O R-13b a")
say("      declara como fronteira; o teorema E1 mostra que ela era")
say("      desnecessaria para o SINAL de r'. (Ela continua necessaria")
say("      para os VALORES: a historia r(a) muda.)")

# =====================================================================
say("")
say("-" * 74)
say("[F3] A CAIXA DE m_T^2 e' ENTRADA -- o que cai com ela e o que nao")
say("-" * 74)
say("")
say("  Rastreamento de dependencia, enunciado por enunciado do R-13b:")
say("")
say(f"  {'enunciado':>44} {'usa a caixa de m_T^2?':>24} {'sobrevive?':>12}")
DEP = [
    ("(E1) r' < 0 em 108/108", "NAO -- so' o fundo", "SIM"),
    ("(E2) xi cruza zero 1x, locus fechado", "NAO -- so' o fundo", "SIM"),
    ("(E3) m_T^2 > 0 em 100%", "SIM", "cai com ela"),
    ("(E4) 1 < sup m_T^2/H^2 < 2", "SIM", "cai com ela"),
    ("(E5) Higuchi da fonte reprovado", "NAO -- e' r' >= 0", "SIM"),
    ("janela 0 < b4/b1 < 2 mu^{3/2}", "NAO -- so' o fundo", "SIM"),
    ("mu e' pura reescala", "NAO -- so' o fundo", "SIM"),
    ("o '3' vs o '12'", "SIM", "cai com ela"),
]
for a_, b_, c_ in DEP:
    say(f"  {a_:>44} {b_:>24} {c_:>12}")
say("")
say("  >>> VEREDITO F3: a cegueira 'a caixa de m_T^2 nao foi")
say("      revalidada' NAO morde o VEREDITO DE EXCLUSAO, porque a")
say("      exclusao passa por `Higuchi <=> r' >= 0`, que e' enunciado")
say("      de FUNDO puro. Ela morde os numeros TENSORIAIS (E3, E4, o")
say("      3 e o 12). Essa separacao nao esta' feita no R-13b.")

# =====================================================================
say("")
say("-" * 74)
say("[F4] REGRA 6 DENTRO DO R-13b: algum numero decisivo passa por estencil?")
say("-" * 74)
say("")
say("  Inventario do r13b_ibb_ramo_infinito.py:")
say("    dr/dN      : FORMA FECHADA  (-3 rho_til / W'(r))")
say("    xi         : FORMA FECHADA  (r + dr/dN)")
say("    m_T^2      : FORMA FECHADA  (caixa do cap.06 avaliada)")
say("    H^2        : FORMA FECHADA  (Friedmann-f)")
say("    r(a)       : raiz de polinomio + Newton (nao e' derivada)")
say("    a(xi = 0)  : bisseccao sobre a forma fechada")
say("    estencil 8a: SO' como CROSS-CHECK do gate M4, nao como fonte")
say("                 de nenhum numero reportado")
say("")
say("  >>> VEREDITO F4: NENHUM numero decisivo do R-13b passa por")
say("      estencil. O modo de falha que o alvo C encontrou (h = 1e-3")
say("      insuficiente quando r ~ 1e8) NAO atinge o R-13b. Atinge o")
say("      R-12g e qualquer reuso futuro da maquinaria de perturbacao")
say("      em fundo com r grande -- e la' ele atinge com forca.")

# =====================================================================
say("")
say("-" * 74)
say("[F5] SELECAO DE RAIZ PERTO DO PONTO FIXO -- armadilha viva")
say("-" * 74)
say("")
say("  A semente analitica do ramo infinito, r ~ sqrt(mu rho_til/b4), e'")
say("  valida SO' no passado profundo. Perto do ponto fixo ela converge")
say("  para a raiz do ramo FINITO. Demonstracao:")
say("")
say(f"  {'a':>9} {'semente':>14} {'Newton converge para':>22} "
    f"{'r_c':>12} {'ramo':>10}")
c = Cel(1.0, 1.0)
rt0 = rt0_Om(c)
rc = r_c(c)
for aval in (1e-4, 1e-2, 1.0, 10.0):
    rt = rt0 * aval**-3
    seed = np.sqrt(c.mu * rt / c.y)
    conv = c.newton(seed, rt)
    rr = c.raizes(rt)
    ramo = 'INFINITO' if abs(conv - rr[-1]) < 1e-8 * rr[-1] else '**FINITO**'
    say(f"  {aval:9.3g} {seed:14.6g} {conv:22.8g} {rc:12.6g} {ramo:>10}")
say("")
say("  >>> VEREDITO F5: o R-13b esta' PROTEGIDO -- ele semeia no passado")
say("      profundo e caminha por CONTINUACAO para o futuro, e o gate")
say("      M1(d) exige r(a_max) ~ r_c. Mas a armadilha e' viva para")
say("      quem reusar `raiz_por_continuacao` sem a semeadura correta,")
say("      e ela derrubou a 1a versao do script do alvo C desta")
say("      auditoria (rodada preservada no git).")

# =====================================================================
say("")
say("-" * 74)
say("[F6] O QUE NENHUM GATE DESTE ARCO VE -- lista fechada")
say("-" * 74)
say("")
LISTA = [
    ("beta_2 != 0 ou beta_3 != 0 no ramo infinito (a cubica vira "
     "quartica)", "LIMITA O ALCANCE, nao morde o enunciado (que e' de "
     "classe IBB genuina)"),
    ("acoplamento duplo da materia (materia so' em g nos dois lados)",
     "nao morde: e' hipotese DECLARADA tambem pela fonte"),
    ("fundo nao-FLRW (anisotropia, inomogeneidade, Vainshtein)",
     "nao morde o linear; a propria fonte (Woodard 2007) avisa que o "
     "ghost pode so' aparecer em ordem superior -- o que REFORCA a "
     "exclusao, nao a enfraquece"),
    ("a DERIVACAO do bound de Higuchi (Fasiello-Tolley 1308.1647 nao "
     "aberto)", "morde o ROTULO, nao a medida: `r' < 0` e' fato de fundo "
     "nas nossas convencoes, independente de como o bound foi derivado"),
    ("fantasma escalar (autovalores de K_2) no ramo infinito",
     "NAO MEDIDO por ninguem neste arco -- fica em aberto; nao muda o "
     "veredito (um ghost ja' basta), mas e' um canal a mais"),
    ("delta rho_m (perturbacao de materia ausente da L2)",
     "morde o c_s^2 do alvo C, nao o Higuchi. Mesma fronteira do "
     "R-11/R-12g"),
    ("validade EFT, screening, f*sigma_8",
     "fora de escopo declarado; nao morde"),
    ("beta_n(phi_-) (modulacao da v2)",
     "MORDE O ARGUMENTO, NAO O VEREDITO -- ver F1. Sob modulacao "
     "`r' < 0` deixa de ser equivalente a violar Higuchi (o limiar de "
     "dbeta_1/dN que inverte r' tende a ZERO no atrator tardio), mas "
     "LHS(15) nao depende de dbeta_n/dN e o teorema E1 mantem "
     "W' > 0. O corpus tem de trocar o diagnostico operacional de "
     "`r' < 0` para `W'(r) > 0`"),
    ("a propria eq. (14) sob modulacao (ela ganha termos em "
     "dbeta_n/dN na derivacao hamiltoniana?)",
     "NAO SABIDO POR NINGUEM. E' a fronteira epistemica real que o "
     "arco R-13 deixa aberta sobre a v2. O R-13a a declara (sec.2.2, "
     "hipotese 2) e nenhum gate deste arco -- nem desta auditoria -- "
     "a testa"),
]
for i, (a_, b_) in enumerate(LISTA, 1):
    say(f"  {i}. {a_}")
    say(f"     -> {b_}")
    say("")

say("=" * 74)
say("VEREDITO DOS GATES DESTE SCRIPT")
say("=" * 74)
say("")
say(f"  FALHAS: {FALHAS if FALHAS else 'nenhuma'}")
say("")
say("  CEGUEIRA RECURSIVA (regra 7 aplicada a este script): ele mede o")
say("  LIMIAR de modulacao, nao a dinamica de phi_- da v2 -- se a v2")
say("  nunca produzir dbeta_1/dN acima do limiar, a cegueira F1 e'")
say("  inofensiva na pratica, e isso este script NAO decide. Ele tambem")
say("  nao valida a caixa de m_T^2 nem a L2: so' rastreia dependencias.")

os.makedirs(OUTD, exist_ok=True)
with open(os.path.join(OUTD, 'r13aud_f_cegueiras.txt'), 'w',
          encoding='utf-8') as fh:
    fh.write("\n".join(LINHAS) + "\n")
print(f"\n[saida versionada] "
      f"{os.path.join(OUTD, 'r13aud_f_cegueiras.txt')}")
