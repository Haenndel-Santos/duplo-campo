# -*- coding: utf-8 -*-
"""
Derivação 3 — verificação simbólica da regra da cadeia completa em
d/dN_g de V(xi,r), com xi = N_f/N_g, e reconciliação das duas formas de
rho_int^(g) usadas no projeto (Anexo A Sec.A.8 vs. Anexo B Sec.B.5).

Ver derivations/03_dV_dNg_regra_cadeia.md, secao 3.
"""
import sympy as sp


def main():
    xi, r = sp.symbols('xi r', positive=True)
    b0, b1, b2, b3, b4 = sp.symbols('beta_0 beta_1 beta_2 beta_3 beta_4')

    # V(xi,r) para a família F1 completa (beta_3 incluído aqui por
    # generalidade da identidade algébrica; no corpo principal beta_3=0).
    V = (b0
         + b1 * (xi + 3 * r)
         + b2 * (3 * xi * r + 3 * r ** 2)
         + b3 * (3 * xi * r ** 2 + r ** 3)
         + b4 * (xi * r ** 3))

    dV_dxi = sp.diff(V, xi)

    # Regra da cadeia completa: d/dN_g [N_g * V(xi(N_g), r)]
    #   = V(xi,r) + N_g * dV/dxi * dxi/dN_g,   dxi/dN_g = -xi/N_g
    #   = V(xi,r) - xi * dV/dxi
    rho_int_g_correct = sp.expand(V - xi * dV_dxi)

    # Forma incompleta tal como escrita no Anexo B Sec.B.5 (trata V como
    # se não dependesse de N_g através de xi):
    rho_int_g_incomplete = V

    # Forma citada no Anexo A Sec.A.8 (sem beta_4, sem xi):
    rho_int_g_anexo_A = b0 + 3 * b1 * r + 3 * b2 * r ** 2 + b3 * r ** 3

    # Forma do setor f, Anexo B Sec.B.6 (já correta na fonte):
    rho_f_sector_stated = b4 + 3 * b3 / r + 3 * b2 / r ** 2 + b1 / r ** 3

    print("V(xi,r) =")
    sp.pprint(V)
    print()

    print("dV/dxi =")
    sp.pprint(dV_dxi)
    print()

    print("Regra da cadeia completa: V(xi,r) - xi*dV/dxi =")
    sp.pprint(rho_int_g_correct)
    print()

    match_A = sp.simplify(rho_int_g_correct - rho_int_g_anexo_A) == 0
    print("Igual à forma do Anexo A Sec.A.8 (beta0+3beta1 r+3beta2 r^2+beta3 r^3)? ->", match_A)
    print()

    depends_on_xi = xi in rho_int_g_incomplete.free_symbols
    print("Forma incompleta (Anexo B Sec.B.5 como escrita) ainda depende de xi? ->", depends_on_xi)
    has_beta4_incomplete = rho_int_g_incomplete.coeff(b4) != 0
    has_beta4_correct = rho_int_g_correct.coeff(b4) != 0
    print("Forma incompleta contém beta_4? ->", has_beta4_incomplete)
    print("Forma corrigida (regra da cadeia completa) contém beta_4? ->", has_beta4_correct)
    print()

    # Verificação cruzada independente: a mesma dV/dxi, dividida por r^3
    # (fator de normalização de volume do setor f, b^3=r^3 a^3), deve
    # reproduzir o resultado já correto do Anexo B Sec.B.6 para o setor f.
    cross_check = sp.simplify(dV_dxi / r ** 3 - rho_f_sector_stated) == 0
    print("Checagem cruzada com o setor f (Anexo B Sec.B.6, já correto):")
    print("  (dV/dxi)/r^3 == beta_4+3beta_3/r+3beta_2/r^2+beta_1/r^3 ? ->", cross_check)
    print()

    print("Resultado final em LaTeX (rho_int^(g), regra da cadeia completa):")
    print(sp.latex(rho_int_g_correct))

    assert match_A
    assert depends_on_xi
    assert has_beta4_incomplete
    assert not has_beta4_correct
    assert cross_check
    print("\nAssertions passed.")


if __name__ == '__main__':
    main()
