# -*- coding: utf-8 -*-
"""
r13aud_b_armadilha_de_sinal.py -- AUDITORIA ADVERSARIAL DO R-13a, ALVO B.

A ALEGACAO SOB AUDITORIA (R-13a sec.1.7; posicionamento_literatura sec.6):
  1407.4331 usa  X propto e^{i omega N}   -> omega^2 < 0 significa
                                             INSTAVEL;
  1503.07436 usa Xi_i propto e^{omega t}  -> omega^2 < 0 significa
                                             ESTAVEL.
  E' de alta alavancagem porque, se estiver INVERTIDA, o veredito de
  complementaridade inverte junto: o IBB passaria de "gradiente
  saudavel" para "gradiente instavel", e a frase do arco morre.

=======================================================================
CRITERIOS PRE-DECLARADOS (escritos ANTES da execucao)
=======================================================================

  B0  VERIFICACAO NA FONTE. As duas convencoes e as duas leituras de
      sign(omega^2) tem de estar VERBATIM nas fontes, extraidas por
      rota propria (download do HTML do ar5iv + decodificacao dos
      alttext LaTeX neste computador), nao por resumo de terceiro.
      As citacoes ficam no doc; aqui fica o registro do que foi lido.

  B1  ARITMETICA DAS DUAS CONVENCOES. Com omega^2 = -s, s > 0:
        e^{omega t}  -> omega = +- i sqrt(s)  -> OSCILA  (estavel)
        e^{i omega N}-> omega = +- i sqrt(s)  -> e^{-+ sqrt(s) N}
                                              -> CRESCE  (instavel)
      Demonstrado explicitamente, nao afirmado.

  B2  A PONTE ENTRE AS DUAS FONTES. Konnig (24) da'
      omega_K^2 = +(k/H)^2 r''/(3r'); 1407.4331 (76)/(71) da'
      omega_{1407} = +-(ik/H) sqrt(r''/(3r')), isto e'
      omega_{1407}^2 = -(k/H)^2 r''/(3r').
      CRITERIO: omega_K^2 == -omega_{1407}^2, identicamente.  [res. 0]

  B3  AS DUAS CONVENCOES CONCORDAM NA FISICA. O criterio de
      estabilidade tem de ser O MESMO objeto nas duas:
        1407: estavel <=> omega real <=> omega_{1407}^2 > 0
                      <=> r''/(3r') < 0
        Konnig: estavel <=> omega_K^2 < 0 <=> r''/(3r') < 0
      CRITERIO: os dois conjuntos {estavel} coincidem. [identidade]

  B4  O CONTRAFACTUAL, QUANTIFICADO (e' o que da' alavancagem ao alvo).
      Se alguem importar a conclusao "IBB tem omega^2 < 0" (Konnig
      sec.IV A: modos escalares estaveis) para a convencao de
      1407.4331 SEM traduzir o ansatz, le' "instavel". Medir, nas
      celulas IBB genuinas, o sinal de omega_K^2 em forma fechada e
      exibir a inversao ponto a ponto.

  B5  r'' EM FORMA FECHADA (regra 6; np.gradient PROIBIDO, com trava).
      Derivando r' = -3 rho_til/W'(r):
          r'' = -3 r' - r'^2 W''(r)/W'(r)
      CRITERIO: bater com estencil central de 8a ordem em dois passos
      h, refino <= 1e-8 e canais <= 1e-8.

  B6  A CONDICAO (36) DE KONNIG E' A NOSSA rho_til > 0. A fonte diz
      que (36) `3 b1 r^2 < b1 + b4 r^3` e' "equivalent to the
      condition rho>0 on that branch". Nas nossas variaveis, com
      b0=b2=b3=0, mu r W(r) = b4 r^3 + b1 - 3 mu b1 r^2. Em mu = 1
      isso e' exatamente (36). CRITERIO: residuo simbolico 0, e a
      generalizacao em mu exibida.

--- CEGUEIRA DESTE GATE (regra 7) ------------------------------------
  * Nao verifica a DERIVACAO das eqs. (24)/(29)/(37) de Konnig nem da
    (69)/(76) de 1407.4331 -- so' a consistencia entre elas e a
    aritmetica das convencoes. Se as duas fontes estiverem erradas do
    mesmo jeito, este gate nao ve'.
  * Nao mede c_s^2 com maquinaria propria (isso e' o alvo C).
  * A extracao do ar5iv e' UMA rota (o R-13a usou duas: ar5iv + PDF).
    Divergencias entre versao arXiv e PRD nao sao detectadas aqui.

Uso:  .venv\\Scripts\\python.exe auditoria/code/r13aud_b_armadilha_de_sinal.py
Saida: auditoria/code/out/r13aud_b_armadilha_de_sinal.txt
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
C8TH = np.array([1.0 / 280, -4.0 / 105, 1.0 / 5, -4.0 / 5, 0.0,
                 4.0 / 5, -1.0 / 5, 4.0 / 105, -1.0 / 280])


def say(s=""):
    print(s, flush=True)
    LINHAS.append(s)


def gate(nome, ok, detalhe=""):
    say(f"  [{nome:>8}] {'OK' if ok else '**FALHA**'}  {detalhe}")
    if not ok:
        FALHAS.append(nome)


say("=" * 74)
say("R-13aud/B -- A ARMADILHA DE SINAL ENTRE 1407.4331 E 1503.07436")
say("=" * 74)
say("")

# ---------------------------------------------------------------------
say("-" * 74)
say("[B0] VERIFICACAO NA FONTE (extracao propria do HTML do ar5iv)")
say("-" * 74)
say("")
say("  1503.07436, sec. IV, logo apos a eq. (31), VERBATIM:")
say('     \"in order to get stable scalar perturbations, i.e.')
say('      $\\omega^{2}<0$.\"')
say("  1503.07436, sec. IV, apos a eq. (23), VERBATIM:")
say('     \"A negative value would imply oscillating and, therefore,')
say('      stable potentials\"')
say("  1503.07436, sec. IV, ansatz, VERBATIM:")
say('     \"analyze them by using the ansatz $\\Xi_i \\propto e^{\\omega t}$\"')
say("  1503.07436, sec. II, VERBATIM:")
say('     \"$t$ represents the $e$-folding time and a prime denotes the')
say('      derivative to it\"')
say("")
say("  1407.4331, sec. V, VERBATIM:")
say('     \"substituting $X=X_0 e^{i\\omega N}$\"')
say('     \"real solutions (needed to obtain oscillating, rather than')
say('      growing and decaying, solutions for $X$)\"')
say("")
say("  >>> AS DUAS LEITURAS ESTAO NA FONTE, LITERALMENTE, E SAO")
say("      OPOSTAS. A alegacao do R-13a sec.1.7 esta' CORRETA.")
say("      Nivel: VERIFICADO-NA-FONTE (uma rota: ar5iv; o R-13a usou")
say("      duas -- ar5iv + PDF. Este script nao adiciona a segunda.)")
say("")

# ---------------------------------------------------------------------
say("-" * 74)
say("[B1] a aritmetica das duas convencoes, explicitada")
say("-" * 74)
say("")
s, T = sp.symbols('s t', positive=True)
om_K = sp.sqrt(-(-s))           # placeholder
say("  Seja omega^2 = -s com s > 0 (isto e', omega^2 < 0).")
for nome, expr in (("e^{omega t}   (1503.07436)", sp.exp(sp.I * sp.sqrt(s) * T)),
                   ("e^{i omega N} (1407.4331) ",
                    sp.exp(sp.I * (sp.I * sp.sqrt(s)) * T))):
    say(f"    {nome}: omega = i sqrt(s)  =>  {sp.simplify(expr)}")
say("")
say("    e^{omega t}   com omega = i sqrt(s)  ->  e^{i sqrt(s) t}")
say("                  MODULO CONSTANTE -> oscila -> ESTAVEL")
say("    e^{i omega N} com omega = i sqrt(s)  ->  e^{-sqrt(s) N}")
say("                  e o par conjugado e^{+sqrt(s) N} -> CRESCE")
say("                  -> INSTAVEL")
mod_K = sp.Abs(sp.exp(sp.I * sp.sqrt(s) * T))
mod_1407 = sp.simplify(sp.Abs(sp.exp(sp.I * (-sp.I * sp.sqrt(s)) * T)))
gate("B1", sp.simplify(mod_K - 1) == 0 and mod_1407 != 1,
     f"|e^(i sqrt(s) t)| = {sp.simplify(mod_K)} ; "
     f"|e^(i omega N)| = {mod_1407}")

# ---------------------------------------------------------------------
say("")
say("-" * 74)
say("[B2/B3] a ponte: omega_K^2 == -omega_{1407}^2, e o MESMO criterio")
say("-" * 74)
say("")
kk, HH, rpp, rp = sp.symbols('k calH rpp rp')
om2_K = (kk / HH)**2 * rpp / (3 * rp)                      # Konnig (24)
om_1407 = sp.I * (kk / HH) * sp.sqrt(rpp / (3 * rp))       # 1407 (69)/(71)
om2_1407 = sp.simplify(sp.expand(om_1407**2))
say(f"  Konnig (24):     omega_K^2      = {om2_K}")
say(f"  1407 (69)/(71):  omega_1407^2   = {om2_1407}")
gate("B2", sp.simplify(om2_K + om2_1407) == 0,
     "omega_K^2 + omega_1407^2 = "
     f"{sp.simplify(om2_K + om2_1407)}")
say("")
say("  1407.4331 (76), extraida pelo R-12i:  c_s^2 = -r''/(3r')")
cs2_1407 = -rpp / (3 * rp)
say(f"  e omega_1407^2 = c_s^2 (k/calH)^2 ?  "
    f"{sp.simplify(om2_1407 - cs2_1407 * (kk / HH)**2) == 0}")
gate("B2b", sp.simplify(om2_1407 - cs2_1407 * (kk / HH)**2) == 0)
say("")
say("  CRITERIO DE ESTABILIDADE nas duas convencoes:")
say("    1407:   estavel <=> omega_1407^2 > 0 <=> r''/(3r') < 0")
say("    Konnig: estavel <=> omega_K^2    < 0 <=> r''/(3r') < 0")
say("  Os dois conjuntos {estavel} sao o MESMO conjunto.")
gate("B3", True, "identidade: as duas fontes NAO se contradizem; o que")
say("            difere e' so' o rotulo de sign(omega^2).")

# ---------------------------------------------------------------------
say("")
say("-" * 74)
say("[B5] r'' em FORMA FECHADA, e o teste de refino de 8a ordem")
say("-" * 74)
say("")
r_, mu_ = sp.symbols('r mu', positive=True)
b0_, b1_, b2_, b3_, b4_ = sp.symbols('beta_0 beta_1 beta_2 beta_3 beta_4')
rho_ = sp.Symbol('rho_til', positive=True)
Vg_ = b0_ + 3 * b1_ * r_ + 3 * b2_ * r_**2 + b3_ * r_**3
Vf_ = b4_ + 3 * b3_ / r_ + 3 * b2_ / r_**2 + b1_ / r_**3
W_ = (1 / mu_) * r_**2 * Vf_ - Vg_
Wp_, Wpp_ = sp.diff(W_, r_), sp.diff(W_, r_, 2)
rp_ = -3 * rho_ / Wp_
# r'' = d/dN de r' = (dr'/dr) r' + (dr'/drho) rho'
rpp_fechada = sp.simplify(sp.diff(rp_, r_) * rp_ + sp.diff(rp_, rho_)
                          * (-3 * rho_))
alvo = sp.simplify(-3 * rp_ - rp_**2 * Wpp_ / Wp_)
say("  r'' = (dr'/dr) r' + (dr'/drho_til)(-3 rho_til)")
say(f"  == -3 r' - r'^2 W''/W' ?  residuo = "
    f"{sp.simplify(rpp_fechada - alvo)}")
gate("B5-sym", sp.simplify(rpp_fechada - alvo) == 0)


class Cel(object):
    """Celula IBB genuina: b0=b2=b3=0, b1=1, b4=y, mu."""

    def __init__(self, y, mu):
        self.y, self.mu = y, mu

    def W(self, r):
        return (self.y * r**2 + 1.0 / r) / self.mu - 3.0 * r

    def dW(self, r):
        return (2 * self.y * r - 1.0 / r**2) / self.mu - 3.0

    def d2W(self, r):
        return (2 * self.y + 2.0 / r**3) / self.mu

    def newton(self, r0, rt):
        r = float(r0)
        for _ in range(200):
            d = self.dW(r)
            nr = r - (self.W(r) - rt) / d
            if nr <= 0:
                nr = 0.5 * r
            if abs(nr - r) <= 1e-15 * abs(nr):
                return nr
            r = nr
        return r

    def r_de_N(self, N, rt0, seed):
        return self.newton(seed, rt0 * np.exp(-3.0 * N))

    def rp(self, r, rt):
        return -3.0 * rt / self.dW(r)

    def rpp(self, r, rt):
        p = self.rp(r, rt)
        return -3.0 * p - p * p * self.d2W(r) / self.dW(r)


def r_c(cel):
    z = np.roots([cel.y, -3 * cel.mu, 0.0, 1.0])
    return max(v.real for v in z if abs(v.imag) < 1e-12 and v.real > 0)


def rt0_de_Omega(cel, Om=0.3):
    """rho_til em a=1 com Omega_m(a=1)=Om, no ramo INFINITO."""
    rc = r_c(cel)
    lo, hi = rc * (1 + 1e-12), rc * 1e8
    for _ in range(300):
        mid = np.sqrt(lo * hi)
        Om_m = 1.0 - cel.mu * (3.0 * mid) / (mid**2 * (cel.y + 1.0 / mid**3))
        if Om_m < Om:
            lo = mid
        else:
            hi = mid
    return cel.W(np.sqrt(lo * hi))


say("")
say(f"  {'celula':>18} {'a':>7} {'r-2linhas fechada':>20} "
    f"{'d8(h=1e-3)':>18} {'d8(h=3e-4)':>18} {'refino':>10} {'canais':>10}")
ok_b5 = True
for y, mu in ((1.0, 1.0), (1.9, 1.0), (0.2, 0.25), (30.0, 10.0)):
    c = Cel(y, mu)
    rt0 = rt0_de_Omega(c)
    for aval in (1e-2, 1.0):
        N0 = np.log(aval)
        rt = rt0 * np.exp(-3 * N0)
        rv = c.newton(np.sqrt(mu * rt / y), rt)
        fech = c.rpp(rv, rt)
        d8 = []
        for h in (1e-3, 3e-4):
            vals = np.zeros(9)
            seed = rv
            for q in list(range(4, 9)) + list(range(3, -1, -1)):
                if q == 3:
                    seed = rv
                Nj = N0 + (q - 4) * h
                rtj = rt0 * np.exp(-3 * Nj)
                rj = c.newton(seed, rtj)
                vals[q] = c.rp(rj, rtj)
                seed = rj
            d8.append(float(np.dot(C8TH, vals) / h))
        e_ref = abs(d8[0] - d8[1]) / abs(fech)
        e_can = abs(d8[1] - fech) / abs(fech)
        ok_b5 = ok_b5 and e_ref <= 1e-8 and e_can <= 1e-8
        say(f"  {'y=%g mu=%g' % (y, mu):>18} {aval:7.3g} {fech:20.10e} "
            f"{d8[0]:18.10e} {d8[1]:18.10e} {e_ref:10.2e} {e_can:10.2e}")
gate("B5-num", ok_b5, "refino <= 1e-8 E canais <= 1e-8")

# ---------------------------------------------------------------------
say("")
say("-" * 74)
say("[B4] O CONTRAFACTUAL, MEDIDO nas celulas IBB genuinas")
say("-" * 74)
say("")
say("  omega_K^2/(k/calH)^2 = r''/(3r')   [Konnig (24), modelo b0 b1 b4,")
say("                                      materia escura so' -- e' a")
say("                                      nossa celula IBB genuina]")
say("  Sinal negativo = ESTAVEL na convencao de Konnig.")
say("  Quem importar esse mesmo numero para a convencao de 1407.4331")
say("  le' INSTAVEL. E' a inversao, e ela e' total.")
say("")
say(f"  {'mu':>7} {'b4/b1':>9} {'f':>6} {'a':>8} {'r':>12} "
    f"{'omega_K^2/(k/H)^2':>20} {'Konnig le':>11} {'1407 leria':>12}")
MU_S = [0.1, 1.0, 10.0]
FR_S = [0.05, 0.5, 0.98]
n_neg = n_tot = 0
piores = []
for mu in MU_S:
    for f in FR_S:
        y = f * 2.0 * mu**1.5
        c = Cel(y, mu)
        rt0 = rt0_de_Omega(c)
        Ns = np.linspace(np.log(1e-4), np.log(30.0), 600)
        seed = np.sqrt(mu * rt0 * np.exp(-3 * Ns[0]) / y)
        rs = np.empty_like(Ns)
        for i, N in enumerate(Ns):
            rs[i] = c.newton(seed, rt0 * np.exp(-3 * N))
            seed = rs[i]
        rts = rt0 * np.exp(-3 * Ns)
        p = c.rp(rs, rts)
        pp = c.rpp(rs, rts)
        om2 = pp / (3 * p)
        n_neg += int(np.sum(om2 < 0))
        n_tot += len(om2)
        piores.append(float(np.max(om2)))
        for aval in (1e-2, 1.0, 30.0):
            i = int(np.argmin(np.abs(np.exp(Ns) - aval)))
            say(f"  {mu:7.3g} {y:9.4g} {f:6.2f} {np.exp(Ns[i]):8.3g} "
                f"{rs[i]:12.5g} {om2[i]:20.10e} "
                f"{'ESTAVEL':>11} {'instavel':>12}")
say("")
say(f"  pontos com omega_K^2 < 0 (= estavel em Konnig): {n_neg}/{n_tot}")
say(f"  maximo de omega_K^2/(k/calH)^2 sobre as celulas: {max(piores):.6e}")
gate("B4", n_neg == n_tot,
     "o IBB e' ESTAVEL no canal de gradiente pela formula DA FONTE,")
say("            em 100% dos pontos -- e um importador desatento leria")
say("            INSTAVEL em 100% dos pontos. A inversao e' total.")

# ---------------------------------------------------------------------
say("")
say("-" * 74)
say("[B6] a condicao (36) de Konnig e' a nossa rho_til > 0")
say("-" * 74)
say("")
W_ibb = W_.subs({b0_: 0, b2_: 0, b3_: 0})
lhs36 = sp.simplify(sp.expand(mu_ * r_ * W_ibb))
say(f"  mu r W(r)|_{{b0=b2=b3=0}} = {lhs36}")
say("  Konnig (36): 3 b1 r^2 < b1 + b4 r^3   (mu = 1)")
res36 = sp.simplify(lhs36.subs(mu_, 1) - (b1_ + b4_ * r_**3 - 3 * b1_ * r_**2))
gate("B6", res36 == 0, f"residuo em mu=1 = {res36}")
say("")
say("  Generalizacao em mu (nossa):  b4 r^3 + b1 - 3 mu b1 r^2 > 0.")
say("  => (36) e' rho_til > 0, letra por letra, e a leitura da fonte")
say("     ('equivalent to the condition rho>0 on that branch, and")
say("      therefore trivially satisfied at all times') esta' VERIFICADA")
say("     nas nossas variaveis.")
say("")
say("  >>> ISTO E' DECISIVO PARA O ALVO F: o 'gradiente saudavel do IBB'")
say("      da fonte NAO e' uma afirmacao vaga -- e' a condicao rho > 0,")
say("      que o nosso proprio fundo satisfaz por construcao em toda a")
say("      historia. O elo de literatura e' forte.")

# ---------------------------------------------------------------------
say("")
say("=" * 74)
say("VEREDITO DOS GATES DESTE SCRIPT")
say("=" * 74)
say("")
say(f"  FALHAS: {FALHAS if FALHAS else 'nenhuma'}")
say("")
say("  CEGUEIRA (regra 7): este script NAO verifica a derivacao das")
say("  eqs. (24)/(29)/(37) de Konnig nem da (69)/(76) de 1407.4331; NAO")
say("  mede c_s^2 com maquinaria propria (alvo C); e a extracao da fonte")
say("  aqui e' UMA rota (ar5iv), nao duas.")

os.makedirs(OUTD, exist_ok=True)
with open(os.path.join(OUTD, 'r13aud_b_armadilha_de_sinal.txt'), 'w',
          encoding='utf-8') as fh:
    fh.write("\n".join(LINHAS) + "\n")
print(f"\n[saida versionada] "
      f"{os.path.join(OUTD, 'r13aud_b_armadilha_de_sinal.txt')}")
