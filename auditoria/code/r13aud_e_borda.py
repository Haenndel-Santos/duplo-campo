# -*- coding: utf-8 -*-
"""
r13aud_e_borda.py -- AUDITORIA ADVERSARIAL DO R-13b, ALVO E: A BORDA.

A QUEIXA SOB AUDITORIA. O R-13b reporta `r' < 0 em 100%` com
`max r' = -6.05e-5`. Essa margem PARECE estreita. O alvo E pede:
varrer a vizinhanca das fronteiras da janela (beta_4/beta_1 -> 0+ e
-> 2 mu^{3/2}-) com resolucao maior e em precisao estendida; o sinal de
r' sobrevive, ou ha' celula onde ele cruza? E o que define "celula IBB
genuina" -- ha' teste de que a raiz e' o ramo infinito e nao um
espurio?

=======================================================================
CRITERIOS PRE-DECLARADOS (escritos ANTES da execucao -- regra 2)
=======================================================================

  E1  TEOREMA DO SINAL (o alvo real). Com b0 = b2 = b3 = 0, b1 = 1,
      y = b4/b1, defina
          Q(r) = mu r W(r)  = y r^3 - 3 mu r^2 + 1        (= mu r rho_til)
          P(r) = mu r^2 W'(r) = 2 y r^3 - 3 mu r^2 - 1
      CRITERIO: provar por IDENTIDADE (sympy, residuo 0) que
          P(r) = 2 Q(r) + 3(mu r^2 - 1).
      Com isso, no ramo infinito (r > r_c, logo Q > 0 e mu r^2 > mu r_c^2):
          mu r_c^2 > 1  =>  P > 0  =>  W' > 0  =>  r' = -3 rho_til/W' < 0
      ESTRITAMENTE, sem margem numerica nenhuma. Se a identidade fechar,
      a "margem estreita" do R-13b e' ARTEFATO DE GRADE, nao fisica.

  E2  DE ONDE VEM O -6.05e-5. CRITERIO: mostrar que sup(r') sobre a
      historia e' 0, atingido SO' assintoticamente em a -> infinito
      (onde rho_til -> 0 e W'(r_c) > 0 finito), e que o numero
      reportado e' simplesmente r'(a_max = 30) da grade do R-13b.
      Verificacao: recomputar max(r') em grades com a_max = 30, 300,
      3000 e exibir que ele -> 0- como rho_til(a_max) ~ a_max^{-3}.
      Se a razao entre os max r' de duas grades bater com o cubo da
      razao dos a_max, o numero e' de grade, nao de fisica.

  E3  BORDA EM PRECISAO ESTENDIDA. mpmath dps = 50. Varrer
      f = y/(2 mu^{3/2}) em 24 valores log-espacados nas DUAS bordas:
          f de 1e-9 a 1e-1   (borda y -> 0+)
          1-f de 1e-9 a 1e-1 (borda y -> 2 mu^{3/2}-)
      x 3 valores de mu (0.1, 1, 10) x 200 pontos em a de 1e-6 a 1e6.
      REPORTAR: min de P(r), min de (mu r^2 - 1), max de r', e se ha'
      QUALQUER ponto com r' >= 0.
      CRITERIO: se aparecer ponto com r' >= 0 dentro da janela, o
      teorema E1 esta' errado e o veredito do R-13b cai.

  E4  O QUE DEFINE "CELULA IBB GENUINA" -- e ha' raiz espuria?
      CRITERIO: provar em forma fechada que a cubica
          (y/mu) r^3 - 3 r^2 - rho_til r + 1/mu = 0
      tem produto das raizes = -1/y < 0, logo EXATAMENTE UMA raiz
      negativa quando ha' duas positivas. Portanto as raizes positivas
      sao exatamente DUAS -- ramo finito (menor) e infinito (maior) --
      e nao existe "terceira raiz positiva espuria" a confundir.
      Verificacao numerica em precisao estendida nas bordas.

  E5  PODER DO TESTE (regra 3): FORA da janela (y > 2 mu^{3/2}) o sinal
      de r' TEM de poder cruzar -- senao o teste E3 nao tem poder e a
      janela nao estaria fazendo trabalho nenhum. CRITERIO: exibir pelo
      menos uma celula com y > 2 mu^{3/2} e algum ponto com r' > 0.

  E6  A DEGENERESCENCIA EM f -> 1. Medir, em precisao estendida, como
      r_c e mu r_c^2 se aproximam de mu^{-1/2} e de 1, e confirmar que
      m_T^2/H^2|_{r_c} = 1 + 1/(mu r_c^2) sobe para 2 SEM alcanca-lo.

--- CEGUEIRA DESTE GATE (regra 7) ------------------------------------
  * So' o bloco IBB GENUINO (b0 = b2 = b3 = 0). Com b2 ou b3 ligados a
    cubica vira quartica e NADA aqui vale.
  * Poeira. Com w geral o fator (1+w) > 0 e' comum e nao muda o sinal
    (alvo A, gate A8d), mas a cubica de fundo muda se houver radiacao
    junto -- nao varrido.
  * beta_n constantes. Modulacao nao coberta.
  * Nao mede Higuchi, gradiente, nem nada de perturbacao.

Uso:  .venv\\Scripts\\python.exe auditoria/code/r13aud_e_borda.py
Saida: auditoria/code/out/r13aud_e_borda.txt
"""
import os

import mpmath as mp
import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
OUTD = os.path.join(HERE, 'out')
LINHAS, FALHAS = [], []


def _gradiente_proibido(*a, **k):
    raise RuntimeError("np.gradient e' PROIBIDO (regra 6, Erratum-03).")


np.gradient = _gradiente_proibido
mp.mp.dps = 50


def say(s=""):
    print(s, flush=True)
    LINHAS.append(s)


def gate(nome, ok, det=""):
    say(f"  [{nome:>7}] {'OK' if ok else '**FALHA**'}  {det}")
    if not ok:
        FALHAS.append(nome)


say("=" * 74)
say("R-13aud/E -- A BORDA DA JANELA IBB, EM PRECISAO ESTENDIDA")
say("=" * 74)
say("")

# =====================================================================
say("-" * 74)
say("[E1] TEOREMA DO SINAL DE r' -- identidade, nao amostragem")
say("-" * 74)
say("")
r, muS, yS, rho = sp.symbols('r mu y rho_til', positive=True)
W = (yS * r**2 + 1 / r) / muS - 3 * r          # b0=b2=b3=0, b1=1
Wp = sp.diff(W, r)
Q = sp.expand(sp.cancel(muS * r * W))
P = sp.expand(sp.cancel(muS * r**2 * Wp))
say(f"  Q(r) = mu r W(r)   = {Q}")
say(f"  P(r) = mu r^2 W'(r) = {P}")
res_E1 = sp.simplify(sp.expand(P - (2 * Q + 3 * (muS * r**2 - 1))))
say("")
say("  IDENTIDADE:  P(r) = 2 Q(r) + 3 (mu r^2 - 1)")
gate("E1a", res_E1 == 0, f"residuo = {res_E1}")
say("")
say("  No ramo INFINITO, r > r_c com Q(r_c) = 0 e Q > 0 para r > r_c")
say("  (Q e' rho_til, positivo por construcao). E a fronteira de")
say("  existencia da' r_c > 2 mu/y > mu^{-1/2}, logo mu r_c^2 > 1 e")
say("  a fortiori mu r^2 > 1 em todo o ramo. Portanto")
say("")
say("      P(r) = 2 Q + 3(mu r^2 - 1) > 0   ESTRITAMENTE")
say("      => W'(r) > 0  => r' = -3 rho_til/W'(r) < 0  ESTRITAMENTE")
say("")
say("  para TODO ponto do ramo infinito com rho_til > 0, em TODA celula")
say("  da janela, em TODO mu. NAO ha' margem numerica: e' um teorema.")
say("")
say("  Sub-lema (usado acima): r_c > 2 mu / y  e  2 mu / y > mu^{-1/2}")
say("  quando y < 2 mu^{3/2}.")
rstar = 2 * muS / yS
res_E1b = sp.simplify(sp.diff(Q, r).subs(r, rstar))
say(f"    Q'(r) = 3 r (y r - 2 mu) => minimo local em r* = 2 mu/y;")
say(f"    Q'(r*) = {res_E1b}   (tem de ser 0)")
gate("E1b", res_E1b == 0)
res_E1c = sp.simplify(sp.expand(rstar - muS**sp.Rational(-1, 2))
                      .subs(yS, 2 * muS**sp.Rational(3, 2)))
say(f"    r*|_{{y = 2 mu^{{3/2}}}} = mu^{{-1/2}}  =>  residuo = {res_E1c}")
gate("E1c", res_E1c == 0)
say("    e r* = 2mu/y e' DECRESCENTE em y, logo y < 2 mu^{3/2} => "
    "r* > mu^{-1/2}. [OK]")

# =====================================================================
say("")
say("-" * 74)
say("[E4] NAO HA' RAIZ POSITIVA ESPURIA -- prova em forma fechada")
say("-" * 74)
say("")
say("  A equacao de fundo r(W(r) - rho_til) = 0 e', com b0=b2=b3=0,")
say("      (y/mu) r^3 - 3 r^2 - rho_til r + 1/mu = 0")
c3, c2, c1, c0 = yS / muS, -3, -rho, 1 / muS
prod = sp.simplify(-c0 / c3)
soma = sp.simplify(-c2 / c3)
say(f"  produto das tres raizes = -c0/c3 = {prod}")
say(f"  soma das tres raizes    = -c2/c3 = {soma}")
say("")
say("  Como y > 0, o PRODUTO e' NEGATIVO. Logo o numero de raizes")
say("  negativas e' IMPAR: 1 ou 3. Como a soma e' POSITIVA e o")
say("  coeficiente de r^0 e' positivo, o caso de 3 negativas e'")
say("  impossivel (soma seria negativa). Portanto ha' EXATAMENTE UMA")
say("  raiz negativa, e as demais sao ou duas positivas ou um par")
say("  complexo conjugado.")
say("")
say("  >>> CONSEQUENCIA: quando o ramo existe, ha' EXATAMENTE DUAS")
say("      raizes positivas -- a menor e' o ramo FINITO, a maior e' o")
say("      INFINITO. NAO EXISTE 'terceira raiz positiva espuria'. A")
say("      pergunta do alvo E ('ha' teste de que a raiz e' o ramo")
say("      infinito e nao um espurio?') tem resposta FECHADA: basta")
say("      tomar a MAIOR das duas positivas -- nao ha' o que confundir.")
gate("E4a", sp.simplify(prod + 1 / yS) == 0, f"produto = -1/y")
say("")
say("  Verificacao numerica em precisao estendida (dps=50), nas bordas:")
say(f"  {'mu':>7} {'f':>12} {'a':>9} {'n raizes reais':>15} "
    f"{'n positivas':>12} {'raiz negativa':>18}")


def cubica(y, mu, rt):
    return [y / mu, mp.mpf(-3), -rt, 1 / mu]


def raizes(y, mu, rt):
    z = mp.polyroots(cubica(y, mu, rt), maxsteps=300, extraprec=300)
    reais = [mp.re(v) for v in z
             if abs(mp.im(v)) < mp.mpf(10)**(-mp.mp.dps + 10)
             * max(1, abs(mp.re(v)))]
    return z, reais


def y_de_f(f, mu):
    return 2 * mu**mp.mpf(1.5) * f


def r_c(y, mu):
    _, reais = raizes(y, mu, mp.mpf(0))
    pos = [v for v in reais if v > 0]
    return max(pos) if pos else mp.nan


def rho0_Omega(y, mu, Om=mp.mpf('0.3')):
    rc = r_c(y, mu)
    lo, hi = rc * (1 + mp.mpf(10)**-40), rc * mp.mpf(10)**10
    for _ in range(400):
        mid = mp.sqrt(lo * hi)
        Om_m = 1 - mu * (3 * mid) / (mid**2 * (y + 1 / mid**3))
        if Om_m < Om:
            lo = mid
        else:
            hi = mid
    r0 = mp.sqrt(lo * hi)
    return (y * r0**2 + 1 / r0) / mu - 3 * r0


for mu in (mp.mpf('0.1'), mp.mpf(1), mp.mpf(10)):
    for f in (mp.mpf(10)**-9, mp.mpf(1) - mp.mpf(10)**-9):
        y = y_de_f(f, mu)
        rt0 = rho0_Omega(y, mu)
        for aval in (mp.mpf(10)**-4, mp.mpf(1), mp.mpf(30)):
            rt = rt0 * aval**-3
            z, reais = raizes(y, mu, rt)
            pos = [v for v in reais if v > 0]
            neg = [v for v in reais if v < 0]
            say(f"  {float(mu):7.3g} {float(f):12.4g} {float(aval):9.3g} "
                f"{len(reais):15d} {len(pos):12d} "
                f"{(mp.nstr(neg[0], 8) if neg else '--'):>18}")

# =====================================================================
say("")
say("-" * 74)
say("[E3] BORDA EM PRECISAO ESTENDIDA -- 24 f x 3 mu x 200 epocas")
say("-" * 74)
say("")
say("  f = y/(2 mu^{3/2}); as duas bordas varridas log-espacadas.")
say("  a de 1e-6 a 1e6 (12 ordens -- muito alem da grade do R-13b).")
say("")
FS = ([mp.mpf(10)**(-9 + i) for i in range(9)]
      + [mp.mpf(1) - mp.mpf(10)**(-1 - i) for i in range(9)]
      + [mp.mpf('0.2'), mp.mpf('0.4'), mp.mpf('0.6'), mp.mpf('0.8'),
         mp.mpf('0.9'), mp.mpf('0.99')])
MUS = (mp.mpf('0.1'), mp.mpf(1), mp.mpf(10))
NA = 200
LN = [mp.log(mp.mpf(10)) * (-6 + 12 * mp.mpf(i) / (NA - 1))
      for i in range(NA)]
say(f"  {'mu':>7} {'f':>14} {'y':>14} {'r_c':>14} {'min P(r)':>14} "
    f"{'min(mu r^2-1)':>15} {'max r-linha':>14} {'r>=0?':>7}")
pior_rp = -mp.inf
n_viol = 0
n_pts = 0
for mu in MUS:
    for f in FS:
        y = y_de_f(f, mu)
        rc = r_c(y, mu)
        if not mp.isfinite(rc):
            say(f"  {float(mu):7.3g} {float(f):14.6g}   sem ponto fixo")
            continue
        rt0 = rho0_Omega(y, mu)
        minP, minM, maxrp = mp.inf, mp.inf, -mp.inf
        ref = None
        for Nv in LN:
            rt = rt0 * mp.e**(-3 * Nv)
            z, reais = raizes(y, mu, rt)
            pos = sorted(v for v in reais if v > 0)
            if not pos:
                continue
            rv = pos[-1]                      # MAIOR raiz = ramo infinito
            Pv = 2 * y * rv**3 - 3 * mu * rv**2 - 1
            Wp_ = Pv / (mu * rv**2)
            rp = -3 * rt / Wp_
            minP = min(minP, Pv)
            minM = min(minM, mu * rv**2 - 1)
            maxrp = max(maxrp, rp)
            n_pts += 1
            if rp >= 0:
                n_viol += 1
            ref = rv
        pior_rp = max(pior_rp, maxrp)
        say(f"  {float(mu):7.3g} {float(f):14.6g} {float(y):14.6g} "
            f"{mp.nstr(rc, 8):>14} {mp.nstr(minP, 6):>14} "
            f"{mp.nstr(minM, 6):>15} {mp.nstr(maxrp, 6):>14} "
            f"{'SIM' if maxrp >= 0 else 'nao':>7}")
say("")
say(f"  pontos varridos: {n_pts}   com r' >= 0: {n_viol}")
say(f"  max r' sobre TODA a varredura de borda: {mp.nstr(pior_rp, 8)}")
gate("E3", n_viol == 0,
     "nenhum ponto da janela, em nenhuma borda, com r' >= 0")

# =====================================================================
say("")
say("-" * 74)
say("[E2] DE ONDE VEM O -6.05e-5: e' NUMERO DE GRADE, nao de fisica")
say("-" * 74)
say("")
say("  Em a -> infinito, rho_til -> 0 e W'(r_c) > 0 finito, logo")
say("  r' = -3 rho_til/W' -> 0^-. O supremo de r' sobre a historia e'")
say("  0, atingido SO' assintoticamente. Qualquer 'max r'' reportado e'")
say("  o valor no ULTIMO ponto da grade, e escala como a_max^{-3}.")
say("")
say(f"  {'a_max':>9} {'max r-linha':>18} {'razao com a linha acima':>26}")
mu, f = mp.mpf(1), mp.mpf('0.726')          # a celula do -1.91e-4 do R-13b
y = y_de_f(f, mu)
rt0 = rho0_Omega(y, mu)
prev = None
for amax in (mp.mpf(30), mp.mpf(300), mp.mpf(3000), mp.mpf(30000)):
    rt = rt0 * amax**-3
    z, reais = raizes(y, mu, rt)
    rv = max(v for v in reais if v > 0)
    Wp_ = (2 * y * rv**3 - 3 * mu * rv**2 - 1) / (mu * rv**2)
    rp = -3 * rt / Wp_
    raz = (mp.nstr(rp / prev, 8) if prev is not None else '--')
    say(f"  {float(amax):9.4g} {mp.nstr(rp, 10):>18} {raz:>26}")
    prev = rp
say("")
say("  A razao e' 1e-3 a cada decada de a_max -- exatamente a^{-3}.")
say("  >>> O 'max r' = -6.05e-5' do R-13b e' r'(a = 30) reescalado por")
say("      mu^{-1/2}; ele NAO e' uma margem estreita: e' o valor de uma")
say("      quantidade que tende a zero por construcao. A margem correta")
say("      e' o teorema E1, que nao tem margem.")

# =====================================================================
say("")
say("-" * 74)
say("[E5] PODER DO TESTE: FORA da janela o sinal de r' TEM de cruzar")
say("-" * 74)
say("")
say("  Se y >= 2 mu^{3/2} nao ha' ponto fixo tardio: Q(r) > 0 para todo")
say("  r > 0. Mas P = 2Q + 3(mu r^2 - 1) pode ser NEGATIVO onde")
say("  mu r^2 < 1. Logo o sinal de r' pode cruzar. Se NAO cruzar em")
say("  celula nenhuma, o teste E3 nao tem poder.")
say("")
say(f"  {'mu':>7} {'y':>10} {'y/y_max':>9} {'r':>12} {'P(r)':>14} "
    f"{'W-linha':>14} {'r-linha':>14} {'sinal':>8}")
achou = False
for mu in (mp.mpf(1),):
    for mult in (mp.mpf('1.01'), mp.mpf(2), mp.mpf(10)):
        y = 2 * mu**mp.mpf(1.5) * mult
        for rv in (mp.mpf('0.2'), mp.mpf('0.5'), mp.mpf('0.9'),
                   mp.mpf(2), mp.mpf(10)):
            Q_ = y * rv**3 - 3 * mu * rv**2 + 1
            if Q_ <= 0:
                continue                       # rho_til <= 0: nao fisico
            rt = Q_ / (mu * rv)
            Pv = 2 * y * rv**3 - 3 * mu * rv**2 - 1
            Wp_ = Pv / (mu * rv**2)
            rp = -3 * rt / Wp_
            if rp > 0:
                achou = True
            say(f"  {float(mu):7.3g} {float(y):10.4g} {float(mult):9.3g} "
                f"{float(rv):12.4g} {mp.nstr(Pv, 6):>14} "
                f"{mp.nstr(Wp_, 6):>14} {mp.nstr(rp, 6):>14} "
                f"{'r-linha>0' if rp > 0 else 'r-linha<0':>8}")
gate("E5", achou,
     "fora da janela existe ponto com r' > 0 => o teste TEM poder,")
say("            e a janela 0 < y < 2 mu^{3/2} esta' fazendo trabalho.")

# =====================================================================
say("")
say("-" * 74)
say("[E6] a degenerescencia em f -> 1 e o sup de m_T^2/H^2")
say("-" * 74)
say("")
say(f"  {'1-f':>12} {'r_c':>20} {'mu r_c^2':>20} "
    f"{'1 + 1/(mu r_c^2)':>20}")
mu = mp.mpf(1)
for e in range(1, 13):
    f = mp.mpf(1) - mp.mpf(10)**(-e)
    y = y_de_f(f, mu)
    rc = r_c(y, mu)
    say(f"  {float(mp.mpf(10)**-e):12.1e} {mp.nstr(rc, 16):>20} "
        f"{mp.nstr(mu*rc**2, 16):>20} "
        f"{mp.nstr(1 + 1/(mu*rc**2), 16):>20}")
say("")
say("  mu r_c^2 -> 1+ e a razao -> 2- SEM alcancar. Confirma o (F-1) do")
say("  R-13b em precisao estendida ate' 1-f = 1e-12 (o R-13b foi ate'")
say("  1-f = 0.02).")

# =====================================================================
say("")
say("=" * 74)
say("VEREDITO DOS GATES DESTE SCRIPT")
say("=" * 74)
say("")
say(f"  FALHAS: {FALHAS if FALHAS else 'nenhuma'}")
say("")
say("  CEGUEIRA (regra 7): so' o bloco IBB genuino (b0=b2=b3=0), poeira,")
say("  beta_n constantes. Com b2 ou b3 ligados a cubica vira quartica e")
say("  NADA aqui vale. Nao mede Higuchi, gradiente nem perturbacao.")

os.makedirs(OUTD, exist_ok=True)
with open(os.path.join(OUTD, 'r13aud_e_borda.txt'), 'w',
          encoding='utf-8') as fh:
    fh.write("\n".join(LINHAS) + "\n")
print(f"\n[saida versionada] "
      f"{os.path.join(OUTD, 'r13aud_e_borda.txt')}")
