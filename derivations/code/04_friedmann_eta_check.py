# -*- coding: utf-8 -*-
"""
Derivação 4 — tentativa de obter H^2 = (8 pi G/3) rho_tot/(1-eta) a
partir de uma ação.

Estratégia: como o corpo do projeto (Anexo E Sec.E.3, eq.1) já deriva a
equação de Friedmann do setor g diretamente da ação bimétrica + campo
escalar minimamente acoplado, e essa equação NÃO contém eta, a única
forma de gerar um fator (1-eta) multiplicando H^2 é via um acoplamento
não-mínimo entre eta e o escalar de Ricci do setor g (tipo Brans-Dicke /
"massa de Planck rodante"): Omega(t) = M_g^2 (1 - eta(t)) multiplicando
R_g na ação.

Este script calcula, do zero, os símbolos de Christoffel, o tensor de
Ricci, o escalar de Ricci e o tensor de Einstein para o FLRW plano, e a
derivada covariante segunda de uma função escalar Omega(t), para obter a
equação de campo "00" exata de uma teoria escalar-tensorial com
acoplamento não-mínimo Omega(t) R. Não assume nenhuma fórmula de
"livro-texto" pronta — toda curvatura é computada explicitamente.

Ver derivations/04_friedmann_eta_acao.md, seção 3.
"""
import sympy as sp


def christoffel_symbols(g, ginv, coords):
    n = len(coords)
    Gamma = [[[sp.Integer(0)] * n for _ in range(n)] for _ in range(n)]
    for lam in range(n):
        for mu in range(n):
            for nu in range(n):
                s = sp.Integer(0)
                for sig in range(n):
                    s += ginv[lam, sig] * (sp.diff(g[sig, nu], coords[mu])
                                           + sp.diff(g[sig, mu], coords[nu])
                                           - sp.diff(g[mu, nu], coords[sig]))
                Gamma[lam][mu][nu] = sp.simplify(s / 2)
    return Gamma


def riemann_tensor(Gamma, coords):
    n = len(coords)
    R = [[[[sp.Integer(0)] * n for _ in range(n)] for _ in range(n)] for _ in range(n)]
    for rho in range(n):
        for sig in range(n):
            for mu in range(n):
                for nu in range(n):
                    term = sp.diff(Gamma[rho][nu][sig], coords[mu]) - sp.diff(Gamma[rho][mu][sig], coords[nu])
                    for lam in range(n):
                        term += Gamma[rho][mu][lam] * Gamma[lam][nu][sig] - Gamma[rho][nu][lam] * Gamma[lam][mu][sig]
                    R[rho][sig][mu][nu] = sp.simplify(term)
    return R


def ricci_tensor(Riem, n):
    Ric = sp.zeros(n, n)
    for mu in range(n):
        for nu in range(n):
            s = sp.Integer(0)
            for rho in range(n):
                s += Riem[rho][mu][rho][nu]
            Ric[mu, nu] = sp.simplify(s)
    return Ric


def covariant_hessian_scalar(Omega, Gamma, coords):
    n = len(coords)
    H = sp.zeros(n, n)
    for mu in range(n):
        for nu in range(n):
            term = sp.diff(Omega, coords[mu], coords[nu])
            for lam in range(n):
                term -= Gamma[lam][mu][nu] * sp.diff(Omega, coords[lam])
            H[mu, nu] = sp.simplify(term)
    return H


def main():
    t, x, y, z = sp.symbols('t x y z')
    coords = [t, x, y, z]
    n = 4

    a = sp.Function('a', positive=True)(t)
    eta = sp.Function('eta')(t)
    Mg2, rho_tot = sp.symbols('M_g^2 rho_tot', positive=True)

    g = sp.diag(-1, a ** 2, a ** 2, a ** 2)
    ginv = sp.diag(-1, 1 / a ** 2, 1 / a ** 2, 1 / a ** 2)

    Gamma = christoffel_symbols(g, ginv, coords)
    Riem = riemann_tensor(Gamma, coords)
    Ric = ricci_tensor(Riem, n)

    Rscalar = sp.simplify(sum(ginv[i, i] * Ric[i, i] for i in range(n)))

    G = sp.zeros(n, n)
    for mu in range(n):
        for nu in range(n):
            G[mu, nu] = sp.simplify(Ric[mu, nu] - sp.Rational(1, 2) * g[mu, nu] * Rscalar)

    H = sp.Function('H')(t)  # placeholder to display in terms of Hubble rate
    adot = sp.diff(a, t)
    Hval = adot / a

    G00 = sp.simplify(G[0, 0])
    G00_in_H = sp.simplify(G00.subs(sp.diff(a, t, 2), sp.diff(Hval * a, t).subs(sp.diff(a, t), Hval * a)))

    print("=== Verificação da geometria FLRW (checagem de sanidade) ===")
    print("G_00 (bruto, em termos de a, adot) =", G00)
    G00_standard = 3 * Hval ** 2
    diff_G00 = sp.simplify(G00 - G00_standard)
    print("G_00 - 3H^2  (deve ser 0) ->", diff_G00)
    assert diff_G00 == 0
    print()

    # Omega(t) = Mg^2 (1 - eta(t)): acoplamento nao-minimo proposto.
    Omega = Mg2 * (1 - eta)

    Hess = covariant_hessian_scalar(Omega, Gamma, coords)
    Hess00 = sp.simplify(Hess[0, 0])

    BoxOmega = sp.simplify(sum(ginv[i, i] * Hess[i, i] for i in range(n)))

    print("=== Termos do acoplamento não-mínimo Omega(t) R, Omega=M_g^2(1-eta) ===")
    print("nabla_0 nabla_0 Omega =", Hess00)
    print("Box(Omega) =", BoxOmega)
    print()

    # Equacao de campo escalar-tensorial padrao:
    #   Omega * G_munu = T_munu + nabla_mu nabla_nu Omega - g_munu Box(Omega)
    # Componente 00, com T_00 = rho_tot (fluido perfeito, comoving):
    field_eq_00 = sp.expand(Omega * G00 - rho_tot - Hess00 + g[0, 0] * BoxOmega)
    field_eq_00 = sp.simplify(field_eq_00)

    print("Equação de campo '00' completa (deve ser igualada a zero):")
    sp.pprint(field_eq_00)
    print()

    # Reescrever em termos de H e eta_dot para leitura direta.
    Hs, etadot, etaddot = sp.symbols('H etadot etaddot')
    field_eq_00_H = field_eq_00.subs({
        sp.diff(a, t): Hs * a,
        sp.diff(eta, t): etadot,
        sp.diff(eta, t, 2): etaddot,
    })
    field_eq_00_H = sp.simplify(sp.expand(field_eq_00_H))
    print("Mesma equação, substituindo adot=H*a, eta_dot, eta_ddot:")
    sp.pprint(field_eq_00_H)
    print()

    # Isolar H^2:
    Hsq = sp.symbols('H^2', positive=True)
    solved = sp.solve(sp.Eq(field_eq_00_H.subs(Hs**2, Hsq), 0), Hsq)
    print("H^2 isolado (forma exata da teoria proposta, com termo de eta_dot):")
    for s in solved:
        sp.pprint(sp.simplify(s))
    print()

    target = rho_tot / (3 * Mg2 * (1 - eta))
    print("Meta do Cap.1/Anexo E Sec.E.7 (com 8 pi G = 1/M_g^2):")
    sp.pprint(sp.Eq(sp.Symbol('H^2'), target))
    print()

    if solved:
        residual = sp.simplify(solved[0] - target)
        print("H^2_exato - H^2_meta =", residual, "  (0 esperado SOMENTE se etadot->0)")
        residual_no_etadot = residual.subs(etadot, 0)
        print("Mesmo resíduo, forçando etadot=0 ->", sp.simplify(residual_no_etadot))


if __name__ == '__main__':
    main()
