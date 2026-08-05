# -*- coding: utf-8 -*-
"""
Derivação 5 — verificação simbólica de que a condição de ramo dinâmico
H_g = xi * H_f (constraint de Bianchi bimétrica) é algebricamente
equivalente a rdot = 0, para a(t), b(t), N_g(t), N_f(t) genéricas
(sem fixar gauge, sem assumir forma de xi(t)).

Ver derivations/05_rdot_ramo_dinamico.md, secao 3.1-3.2.
"""
import sympy as sp


def main():
    t = sp.symbols('t', positive=True)
    a = sp.Function('a', positive=True)(t)
    b = sp.Function('b', positive=True)(t)
    Ng = sp.Function('N_g', positive=True)(t)
    Nf = sp.Function('N_f', positive=True)(t)

    Hg = sp.diff(a, t) / (Ng * a)
    Hf = sp.diff(b, t) / (Nf * b)
    xi = Nf / Ng
    r = b / a

    branch_residual = sp.simplify(Hg - xi * Hf)
    rate_diff = sp.diff(a, t) / a - sp.diff(b, t) / b

    ratio = sp.simplify(branch_residual / rate_diff)

    rdot_over_r = sp.simplify(sp.diff(r, t) / r)
    matches = sp.simplify(rdot_over_r - (sp.diff(b, t) / b - sp.diff(a, t) / a)) == 0

    print("H_g - xi*H_f  =")
    sp.pprint(branch_residual)
    print()
    print("(H_g - xi*H_f) / (adot/a - bdot/b) =", ratio,
          "   <- no N_f dependence survives")
    print()
    print("rdot/r =", rdot_over_r)
    print("rdot/r identically equals (bdot/b - adot/a)? ->", matches)
    print()
    print("CONCLUSION: H_g = xi*H_f  <=>  adot/a = bdot/b  <=>  rdot = 0,")
    print("for ANY N_g(t), N_f(t) (no gauge choice needed, no extra hypothesis).")

    assert ratio == 1 / Ng
    assert matches
    print("\nAssertions passed.")


if __name__ == '__main__':
    main()
