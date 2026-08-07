# -*- coding: utf-8 -*-
"""
gate2_lapso.py — Gate 2, Parte A: linearidade nos lapsos.

Verifica que a modulacao beta_n(phi_-) NAO destroi a estrutura que
sustenta a constraint primaria de Hassan-Rosen — a linearidade do termo
de potencial nos lapsos N_g e N_f.

ESCOPO DECLARADO. Este script resolve a Parte A do Gate 2. Ele NAO
resolve a Parte B (sobrevivencia da constraint secundaria), que e o
risco real e exige o bracket {C, H} no ADM completo. Ver
docs/gate2_ghost.md Sec.3.

Requer sympy.

Uso:
    python gate2_lapso.py
"""
import sys

try:
    import sympy as sp
except ImportError:
    print("ERRO: este script precisa de sympy.  pip install sympy")
    sys.exit(2)


Ng, Nf, a, b, r = sp.symbols('N_g N_f a b r', positive=True)
phi_m = sp.Symbol('phi_-', real=True)
m2, Meff2 = sp.symbols('m^2 M_eff^2', positive=True)

# beta_n como FUNCOES ARBITRARIAS de phi_- — o ponto do teste e que a
# linearidade vale para qualquer forma funcional, nao so a escolhida.
B = [sp.Function(f'beta_{n}')(phi_m) for n in range(5)]

RESULTADOS = []


def checa(nome, cond, detalhe=""):
    ok = bool(cond)
    RESULTADOS.append((nome, ok))
    print(f"  [{'PASSA' if ok else 'FALHA'}] {nome}")
    if detalhe:
        print(f"          {detalhe}")
    return ok


def main():
    print("=" * 68)
    print("GATE 2 / PARTE A — linearidade nos lapsos com beta_n(phi_-)")
    print("=" * 68)

    xi = Nf / Ng
    e = [sp.Integer(1),
         xi + 3 * r,
         3 * xi * r + 3 * r**2,
         3 * xi * r**2 + r**3,
         xi * r**3]

    print("\n(1) POLINOMIOS e_n NO FUNDO FLRW  (Anexo A Sec.A.7)\n")
    for n, en in enumerate(e):
        print(f"      e_{n} = {sp.simplify(en)}")

    # termo de potencial em minisuperespaco (Anexo B Sec.B.4.2)
    L_int = -m2 * Meff2 * Ng * a**3 * sum(B[n] * e[n] for n in range(5))
    L_int = sp.expand(sp.simplify(L_int))

    print("\n(2) TERMO DE POTENCIAL EXPANDIDO\n")
    print("    sqrt(-g) V = -m^2 M_eff^2 N_g a^3 sum_n beta_n(phi_-) e_n\n")
    poly_g = sp.Poly(L_int, Ng)
    poly_f = sp.Poly(L_int, Nf)
    print(f"      grau em N_g: {poly_g.degree()}")
    print(f"      grau em N_f: {poly_f.degree()}")

    print("\n(3) LINEARIDADE — o teste do gate\n")
    d2_g = sp.simplify(sp.diff(L_int, Ng, 2))
    d2_f = sp.simplify(sp.diff(L_int, Nf, 2))
    ok1 = checa("d^2/dN_g^2 (sqrt(-g)V) = 0", d2_g == 0,
                f"segunda derivada = {d2_g}")
    ok2 = checa("d^2/dN_f^2 (sqrt(-g)V) = 0", d2_f == 0,
                f"segunda derivada = {d2_f}")
    ok3 = checa("d^2/(dN_g dN_f) = 0  (sem termo cruzado)",
                sp.simplify(sp.diff(L_int, Ng, Nf)) == 0)
    ok4 = checa("grau 1 em N_g", poly_g.degree() == 1)
    ok5 = checa("grau 1 em N_f", poly_f.degree() == 1)

    print("\n(4) FORMA LINEAR EXPLICITA\n")
    cg = sp.simplify(sp.diff(L_int, Ng))
    cf = sp.simplify(sp.diff(L_int, Nf))
    resto = sp.simplify(L_int - cg * Ng - cf * Nf)
    print(f"      coeficiente de N_g:\n        {sp.factor(cg)}\n")
    print(f"      coeficiente de N_f:\n        {sp.factor(cf)}\n")
    ok6 = checa("sqrt(-g)V = C_g*N_g + C_f*N_f  (sem termo independente)",
                sp.simplify(resto) == 0,
                f"resto = {resto}")
    ok7 = checa("C_g nao depende de N_g nem N_f",
                sp.diff(cg, Ng) == 0 and sp.diff(cg, Nf) == 0)
    ok8 = checa("C_f nao depende de N_g nem N_f",
                sp.diff(cf, Ng) == 0 and sp.diff(cf, Nf) == 0)

    print("\n(5) OS beta_n(phi_-) NAO INTRODUZEM LAPSO\n")
    ok9 = checa("d(beta_n)/dN_g = 0 para todo n",
                all(sp.diff(B[n], Ng) == 0 for n in range(5)),
                "phi_- e escalar; seu valor num ponto independe do lapso")
    ok10 = checa("a linearidade vale para beta_n ARBITRARIOS",
                 d2_g == 0 and d2_f == 0,
                 "beta_n entraram como sp.Function, sem forma assumida")

    print("\n(6) CONTRASTE: o setor escalar NAO e linear (e tudo bem)\n")
    dphi = sp.Symbol('phidot', real=True)
    V_phi = sp.Function('V')(phi_m)
    L_phi = a**3 * (dphi**2 / (2 * Ng) - Ng * V_phi)
    d2_phi = sp.simplify(sp.diff(L_phi, Ng, 2))
    ok11 = checa("L_phi tem d^2/dN_g^2 != 0  (esperado)",
                 d2_phi != 0,
                 f"= {sp.simplify(d2_phi)}  — estrutura de materia "
                 f"minimamente acoplada, que comprovadamente nao "
                 f"reintroduz o fantasma BD")

    print("\n(7) CONTRAPROVA: modulacao COM lapso quebraria a linearidade\n")
    beta_ruim = sp.Function('beta_ruim')(Ng)
    L_ruim = -m2 * Meff2 * Ng * a**3 * beta_ruim * e[1]
    d2_ruim = sp.simplify(sp.diff(L_ruim, Ng, 2))
    ok12 = checa("se beta dependesse do lapso, d^2/dN_g^2 != 0",
                 d2_ruim != 0,
                 "confirma que o teste tem poder de deteccao")

    print("\n" + "=" * 68)
    falhas = [n for n, ok in RESULTADOS if not ok]
    print(f"RESUMO: {len(RESULTADOS) - len(falhas)}/{len(RESULTADOS)} "
          f"checagens passaram")

    if falhas:
        print("\nGATE 2 / PARTE A: NAO PASSA. Falhas:")
        for n in falhas:
            print(f"  - {n}")
    else:
        print("\nGATE 2 / PARTE A: PASSA.")
        print("  A linearidade nos lapsos sobrevive a beta_n(phi_-) para")
        print("  QUALQUER forma funcional. Logo a constraint primaria de")
        print("  Hassan-Rosen sobrevive.  [Nivel 2a]")
        print()
        print("  >>> ISTO NAO FECHA O GATE 2. <<<")
        print()
        print("  Falta a PARTE B: a constraint secundaria.")
        print("  Como C agora depende de phi_- via beta_1, o bracket")
        print("  {C,H} ganha o termo novo  (dC/dphi_-)(pi_phi/a^3),")
        print("  e e preciso mostrar que dC/dt=0 continua sendo uma")
        print("  constraint — e nao uma equacao que determina o lapso.")
        print()
        print("  Ver docs/gate2_ghost.md Sec.3.  O Passo 3 NAO comeca")
        print("  antes disso.")
    print("=" * 68)
    return 1 if falhas else 0


if __name__ == '__main__':
    sys.exit(main())
