# -*- coding: utf-8 -*-
"""
gate2_fatoracao.py — correcao do teste (5) de gate2_bracket.py.

O teste original era VACUO:
    q = br / B ; verificar q*B - br == 0
sempre da 0 por identidade algebrica, divida ou nao exatamente.

Teste correto: a constraint fatora como B(r) x (cinematica) se e
somente se ela SE ANULA quando B(r)=0. Entao substitui-se a raiz
r = r* e verifica-se o que sobra.

O que sobrar e a obstrucao — e diz onde a solucao realmente vive.

Requer sympy.  Uso:  python gate2_fatoracao.py
"""
import sys

try:
    import sympy as sp
except ImportError:
    print("ERRO: precisa de sympy.  pip install sympy")
    sys.exit(2)

a, b, ph = sp.symbols('a b phi_-', positive=True)
pa, pb, pph = sp.symbols('p_a p_b p_phi', real=True)
Mg2, Mf2, Meff2, m2 = sp.symbols('M_g^2 M_f^2 M_eff^2 m^2', positive=True)
rho_m = sp.Symbol('rho_m', nonnegative=True)

CANON = [(a, pa), (b, pb), (ph, pph)]


def poisson(f, g):
    return sum(sp.diff(f, q)*sp.diff(g, p) - sp.diff(f, p)*sp.diff(g, q)
               for q, p in CANON)


def bracket(B):
    r = b/a
    C_g = sp.expand(-Meff2*m2*a**3*(B[0] + 3*r*B[1] + 3*r**2*B[2] + r**3*B[3]))
    C_f = sp.expand(-Meff2*m2*a**3*(B[1] + 3*r*B[2] + 3*r**2*B[3] + r**3*B[4]))
    H_g = (-pa**2/(12*Mg2*a) + pph**2/(2*a**3)
           + a**3*sp.Function('V')(ph) + a**3*rho_m - C_g)
    H_f = -pb**2/(12*Mf2*b) - C_f
    return sp.simplify(poisson(H_g, H_f))


def main():
    print("=" * 70)
    print("GATE 2 — a constraint secundaria FATORA em dois ramos?")
    print("=" * 70)

    # ---------- caso F1 minimo da v2: so beta_1 depende de phi_- ----------
    b1f = sp.Function('beta_1')(ph)
    b0c, b2c, b4c = sp.symbols('beta_0 beta_2 beta_4', real=True)
    B_v2 = [b0c, b1f, b2c, sp.Integer(0), b4c]        # beta_3 = 0 (F1)
    br_v2 = bracket(B_v2)

    # ---------- controle: todos os beta constantes (v1) ----------
    b1c = sp.Symbol('beta_1', real=True)
    B_v1 = [b0c, b1c, b2c, sp.Integer(0), b4c]
    br_v1 = bracket(B_v1)

    # ---------- a raiz algebrica: B(r) = beta_1 + 2 beta_2 r = 0 ----------
    # => b = -a*beta_1/(2*beta_2)
    raiz_v1 = {b: -a*b1c/(2*b2c)}
    raiz_v2 = {b: -a*b1f/(2*b2c)}

    print("\n(1) CONTROLE — v1, beta_n TODOS constantes\n")
    res_v1 = sp.simplify(br_v1.subs(raiz_v1))
    print(f"    {{H_g,H_f}} avaliada em r = r* = -beta_1/(2 beta_2):")
    print(f"      {res_v1}\n")
    ok1 = (sp.simplify(res_v1) == 0)
    print(f"  [{'PASSA' if ok1 else 'FALHA'}] anula-se na raiz "
          f"-> FATORA em dois ramos")
    print("          confirma a estrutura da v1: ramo algebrico B(r)=0")
    print("          satisfaz a constraint sozinho, sem condicao cinematica\n")

    print("(2) v2 — beta_1 = beta_1(phi_-), demais constantes\n")
    res_v2 = sp.simplify(br_v2.subs(raiz_v2))
    res_v2 = sp.simplify(sp.expand(res_v2))
    print(f"    {{H_g,H_f}} avaliada em r = r*(phi_-):")
    print(f"      {sp.factor(res_v2)}\n")
    ok2 = (sp.simplify(res_v2) == 0)
    print(f"  [{'FATORA' if ok2 else 'NAO FATORA'}] "
          f"{'anula-se' if ok2 else 'NAO se anula'} na raiz")

    if not ok2:
        print()
        print("      *** RESULTADO ESTRUTURAL ***")
        print()
        print("      A dicotomia 'ramo algebrico OU ramo dinamico' e um")
        print("      ARTEFATO de beta_n constantes. Com beta_1(phi_-), a")
        print("      constraint nao fatora: estar sobre a raiz NAO basta.")
        print()
        print("      A obstrucao acima e a condicao que sobra. Ela se")
        print("      anula so se p_phi = 0 (phi_- congelado) ou")
        print("      beta_1' = 0 (sem modulacao) — ou seja, exatamente")
        print("      nos casos em que a v2 degenera na v1.")

    # ---------- o deslocamento da raiz ----------
    print("\n(3) ONDE A SOLUCAO VIVE — deslocamento da raiz\n")
    delta = sp.Symbol('delta', real=True)   # b = a(r* + delta/(2 beta_2))
    # parametriza:  beta_1 + 2 beta_2 (b/a) = delta   <=>  b = a(delta-beta_1)/(2beta_2)
    desloc = {b: a*(delta - b1f)/(2*b2c)}
    eq = sp.simplify(br_v2.subs(desloc))
    sol = sp.solve(sp.Eq(eq, 0), delta)
    print("    Parametrizando  B(r) = beta_1 + 2 beta_2 r = delta,")
    print("    a constraint {H_g,H_f}=0 da:\n")
    if sol:
        for s in sol:
            print(f"      delta = {sp.simplify(sp.factor(s))}")
        print()
        print("    -> a solucao NAO fica sobre a raiz: fica DESLOCADA por")
        print("       delta, e o deslocamento e proporcional a p_phi*beta_1'")
        print("       — ou seja, a quao rapido phi_- evolui.")
        print()
        print("    CONVERGENCIA COM A ANCORA D1: a D1 encontrou que NA")
        print("    RAIZ EXATA o par escalar degenera (kN ~ 1e-16,")
        print("    fortemente acoplado). O Gate 4 ia ter que perguntar se")
        print("    existe um 'corredor seguro' fora da raiz. A constraint")
        print("    responde sozinha: ela PROIBE ficar na raiz enquanto")
        print("    phi_- evolui. O deslocamento nao e ajuste — e imposto.")
    else:
        print("      (sympy nao resolveu em forma fechada — inspecionar)")
        print(f"      equacao: {sp.factor(eq)}")

    print("\n" + "=" * 70)
    print("RESUMO")
    print(f"  v1 (beta const):  fatora em dois ramos      -> {ok1}")
    print(f"  v2 (beta_1(phi)): fatora em dois ramos      -> {ok2}")
    print()
    if ok1 and not ok2:
        print("  A v2 escapa da dicotomia que matou a v1. Nao esta presa")
        print("  nem ao ramo algebrico (rdot=0 + degenerescencia) nem ao")
        print("  ramo dinamico (fantasma + rdot=0). E uma terceira")
        print("  estrutura de solucao, com r deslocado da raiz por um")
        print("  termo que a propria constraint fixa.")
    print("=" * 70)
    return 0


if __name__ == '__main__':
    sys.exit(main())
