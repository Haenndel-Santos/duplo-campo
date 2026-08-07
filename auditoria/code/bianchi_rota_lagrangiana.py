# -*- coding: utf-8 -*-
"""
bianchi_rota_lagrangiana.py — TESTE DECISIVO.

Deriva a constraint de Bianchi do minisuperespaco bimetrico por rota
puramente LAGRANGIANA, independente do bracket hamiltoniano de
gate2_bracket.py / gate2_bianchi_confronto.py.

Motivo: as duas rotas devem dar a MESMA constraint. Se concordarem,
fica resolvido qual e o segundo fator correto:

    forma do CORPUS   (Cap.5 Sec.5.5, Anexo B Sec.B.8, base da D5):
        B(r) * (H_g - xi H_f) = 0     <=>  B(r) * (adot/a - bdot/b) = 0
        -> ramo dinamico da rdot = 0

    forma CANONICA    (bracket {H_g,H_f}):
        B(r) * (adot/N_g - bdot/N_f) = 0   <=>  xi = bdot/adot
        -> ramo dinamico NAO da rdot = 0

METODO. Para a lagrangiana de minisuperespaco L(a,adot,N_g;b,bdot,N_f;
phi,phidot), a variacao em N_g e N_f produz vinculos (as duas
Friedmann). A consistencia temporal do vinculo de N_g, usando as
equacoes dinamicas de a, b, phi e o vinculo de N_f, deixa um residuo:
esse residuo E a constraint de Bianchi.

Requer sympy.  Uso:  python bianchi_rota_lagrangiana.py
"""
import sys

try:
    import sympy as sp
except ImportError:
    print("ERRO: precisa de sympy.  pip install sympy")
    sys.exit(2)

t = sp.Symbol('t')
Mg2, Mf2, Meff2, m2 = sp.symbols('M_g^2 M_f^2 M_eff^2 m^2', positive=True)
b0, b1, b2, b3, b4 = sp.symbols('beta_0 beta_1 beta_2 beta_3 beta_4', real=True)

a = sp.Function('a', positive=True)(t)
b = sp.Function('b', positive=True)(t)
Ng = sp.Function('N_g', positive=True)(t)
Nf = sp.Function('N_f', positive=True)(t)
ph = sp.Function('phi')(t)
Vf = sp.Function('V')

D = lambda X: sp.diff(X, t)


def main():
    print("=" * 70)
    print("TESTE DECISIVO — constraint de Bianchi por rota lagrangiana")
    print("=" * 70)

    xi = Nf / Ng
    r = b / a

    e = [sp.Integer(1),
         xi + 3*r,
         3*xi*r + 3*r**2,
         3*xi*r**2 + r**3,
         xi*r**3]
    betas = [b0, b1, b2, b3, b4]

    # lagrangiana de minisuperespaco (Anexo B Sec.B.4.5)
    L = (-3*Mg2*a*D(a)**2/Ng
         - 3*Mf2*b*D(b)**2/Nf
         - m2*Meff2*Ng*a**3*sum(betas[n]*e[n] for n in range(5))
         + a**3*(D(ph)**2/(2*Ng) - Ng*Vf(ph)))

    print("\n(1) EQUACOES DE MOVIMENTO\n")

    E_Ng = sp.simplify(sp.diff(L, Ng))            # vinculo (Friedmann g)
    E_Nf = sp.simplify(sp.diff(L, Nf))            # vinculo (Friedmann f)
    E_a = sp.simplify(D(sp.diff(L, D(a))) - sp.diff(L, a))
    E_b = sp.simplify(D(sp.diff(L, D(b))) - sp.diff(L, b))
    E_ph = sp.simplify(D(sp.diff(L, D(ph))) - sp.diff(L, ph))

    print("    E_Ng = dL/dN_g = 0      (Friedmann do setor g)")
    print("    E_Nf = dL/dN_f = 0      (Friedmann do setor f)")
    print("    E_a, E_b, E_phi = 0     (equacoes dinamicas)\n")

    print("(2) CONSISTENCIA: derivada temporal do vinculo E_Ng\n")
    dE = sp.simplify(D(E_Ng))

    # eliminar as segundas derivadas usando as equacoes dinamicas
    add, bdd, phdd = D(D(a)), D(D(b)), D(D(ph))
    sol = sp.solve([sp.Eq(E_a, 0), sp.Eq(E_b, 0), sp.Eq(E_ph, 0)],
                   [add, bdd, phdd], dict=True)
    if not sol:
        print("    [!] sympy nao resolveu as equacoes dinamicas.")
        return 1
    sol = sol[0]
    dE_red = sp.simplify(dE.subs(sol))

    # usar tambem o vinculo do setor f para eliminar o que sobrar
    solNf = sp.solve(sp.Eq(E_Nf, 0), D(b)**2, dict=True)
    if solNf:
        dE_red = sp.simplify(dE_red.subs(solNf[0]))

    dE_red = sp.simplify(sp.factor(sp.simplify(dE_red)))

    print("    residuo apos usar E_a, E_b, E_phi e E_Nf:\n")
    print(f"      {dE_red}\n")

    print("(3) IDENTIFICACAO DOS FATORES\n")

    Bfac = b1 + 2*b2*r + b3*r**2
    print(f"    fator de Bianchi esperado:  B(r) = {sp.simplify(Bfac)}")

    fator_corpus = sp.simplify(D(a)/a - D(b)/b)
    fator_canon = sp.simplify(D(a)/Ng - D(b)/Nf)
    print(f"    candidato CORPUS:   adot/a - bdot/b")
    print(f"    candidato CANONICO: adot/N_g - bdot/N_f\n")

    for nome, cand in (("CORPUS", fator_corpus), ("CANONICO", fator_canon)):
        prod = sp.simplify(Bfac * cand)
        q = sp.simplify(sp.cancel(dE_red / prod)) if prod != 0 else None
        # teste honesto: o residuo se anula quando o candidato se anula?
        solc = sp.solve(sp.Eq(cand, 0), D(b))
        if solc:
            resto = sp.simplify(dE_red.subs(D(b), solc[0]))
            anula = (sp.simplify(resto) == 0)
            print(f"  [{'CONFIRMA' if anula else 'REJEITA '}] "
                  f"candidato {nome}: residuo com {nome.lower()}=0 -> "
                  f"{sp.simplify(resto)}")

    print("\n(4) VEREDITO\n")
    print("    O candidato cujo anulamento zera o residuo e o segundo")
    print("    fator correto da constraint de Bianchi.\n")
    print("    Se for o CORPUS   -> D5 (rdot=0) intacta; o bracket")
    print("                         hamiltoniano tem erro meu.")
    print("    Se for o CANONICO -> a constraint do corpus esta errada")
    print("                         em Cap.5, Anexo B, Cap.14, Anexo E e")
    print("                         Anexo H; D5 vira consequencia correta")
    print("                         de premissa errada; e os benchmarks")
    print("                         de ramo dinamico de D1/D2 (montados")
    print("                         com xi = H/H_f) nao sao o ramo")
    print("                         dinamico. O parecer precisa de revisao.")
    print("=" * 70)
    return 0


if __name__ == '__main__':
    sys.exit(main())
