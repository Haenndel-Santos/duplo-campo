# -*- coding: utf-8 -*-
"""
gate2_bianchi_confronto.py — resolve a discrepancia entre duas formas
do segundo fator da constraint de Bianchi.

CANONICA (do bracket {H_g,H_f} em minisuperespaco):
    fator ~ (adot/N_g - bdot/N_f)          [livre de lapso em var. canonicas]

CORPUS (Anexo B Sec.B.8, e a base da ancora D5):
    fator ~ (H_g - xi H_f) = (1/N_g)(adot/a - bdot/b) = -rdot/(r N_g)

Estas nao sao a mesma expressao. Como e de (H_g - xi H_f) que sai o
resultado rdot=0 no ramo dinamico (D5, classificado Nivel 1), a
discrepancia precisa ser resolvida ANTES do Passo 3.

Hipotese a testar: as duas sao equivalentes NA SUPERFICIE DE
CONSTRAINTS, isto e, sua diferenca e combinacao linear de H_g e H_f.

Requer sympy.  Uso:  python gate2_bianchi_confronto.py
"""
import sys

try:
    import sympy as sp
except ImportError:
    print("ERRO: precisa de sympy.  pip install sympy")
    sys.exit(2)

a, b = sp.symbols('a b', positive=True)
pa, pb, pph = sp.symbols('p_a p_b p_phi', real=True)
Ng, Nf = sp.symbols('N_g N_f', positive=True)
Mg2, Mf2, Meff2, m2 = sp.symbols('M_g^2 M_f^2 M_eff^2 m^2', positive=True)
rho_m = sp.Symbol('rho_m', nonnegative=True)
b0, b1, b2, b4 = sp.symbols('beta_0 beta_1 beta_2 beta_4', real=True)
Vv = sp.Symbol('V', real=True)


def main():
    print("=" * 70)
    print("CONFRONTO — segundo fator da constraint de Bianchi")
    print("=" * 70)

    r = b / a

    # ---- constraints primarias (beta_3 = 0, F1) ----
    C_g = sp.expand(-Meff2*m2*a**3*(b0 + 3*r*b1 + 3*r**2*b2))
    C_f = sp.expand(-Meff2*m2*a**3*(b1 + 3*r*b2 + r**3*b4))
    H_g = -pa**2/(12*Mg2*a) + pph**2/(2*a**3) + a**3*Vv + a**3*rho_m - C_g
    H_f = -pb**2/(12*Mf2*b) - C_f

    # ---- relacoes momento <-> velocidade ----
    adot = -Ng*pa/(6*Mg2*a)
    bdot = -Nf*pb/(6*Mf2*b)

    print("\n(1) AS DUAS FORMAS EM VARIAVEIS CANONICAS\n")

    fator_canon = sp.simplify(adot/Ng - bdot/Nf)
    print(f"    canonica:  adot/N_g - bdot/N_f")
    print(f"               = {sp.simplify(fator_canon)}")
    print(f"               (lapsos cancelaram: {'SIM' if not fator_canon.has(Ng) and not fator_canon.has(Nf) else 'NAO'})\n")

    fator_corpus = sp.simplify((sp.Rational(1, 1)/Ng)*(adot/a - bdot/b))
    print(f"    corpus:    (1/N_g)(adot/a - bdot/b)")
    print(f"               = {sp.simplify(fator_corpus)}")
    tem_lapso = fator_corpus.has(Ng) or fator_corpus.has(Nf)
    print(f"               (contem lapso: {'SIM' if tem_lapso else 'NAO'})\n")

    print("  >>> a forma do corpus CONTEM o lapso; a canonica nao.")
    print("      Uma constraint genuina tem de ser livre de lapso.\n")

    # ---- razao entre elas ----
    print("(2) RAZAO ENTRE AS DUAS\n")
    razao = sp.simplify(fator_canon / fator_corpus)
    print(f"    canonica / corpus = {sp.simplify(razao)}\n")

    # ---- teste da hipotese: diferenca ~ combinacao de H_g, H_f ? ----
    print("(3) HIPOTESE: sao equivalentes NA SUPERFICIE DE CONSTRAINTS?\n")
    print("    Testando se  fator_canon - lambda*fator_corpus  se anula")
    print("    quando H_g = 0 e H_f = 0, para algum lambda.\n")

    # resolve H_g=0 e H_f=0 para pa, pb (escolhendo um ramo de sinal)
    sol_pa = sp.solve(sp.Eq(H_g, 0), pa)
    sol_pb = sp.solve(sp.Eq(H_f, 0), pb)
    print(f"    H_g=0  ->  p_a = {sol_pa[0] if sol_pa else '(sem solucao)'}")
    print(f"    H_f=0  ->  p_b = {sol_pb[0] if sol_pb else '(sem solucao)'}\n")

    if sol_pa and sol_pb:
        sub = {pa: sol_pa[0], pb: sol_pb[0]}
        fc_on = sp.simplify(fator_canon.subs(sub))
        fk_on = sp.simplify(fator_corpus.subs(sub))
        print("    Na superficie de constraints:")
        print(f"      canonica = {sp.simplify(fc_on)}")
        print(f"      corpus   = {sp.simplify(fk_on)}\n")
        lam = sp.simplify(fc_on / fk_on)
        print(f"      razao (on-shell) = {sp.simplify(lam)}\n")
        indep = not (lam.has(pa) or lam.has(pb) or lam.has(pph))
        print(f"  [{'COMPATIVEL' if indep else 'INCOMPATIVEL'}] "
              f"a razao on-shell {'nao depende' if indep else 'DEPENDE'} "
              f"dos momentos")
        if indep:
            print("      -> as duas formas se anulam nos MESMOS pontos da")
            print("         superficie de constraints. Sao a mesma condicao,")
            print("         expressa de formas diferentes. D5 fica INTACTA.")
        else:
            print("      -> ALARME: as duas formas NAO definem a mesma")
            print("         condicao. O ramo 'dinamico' do corpus e o ramo")
            print("         canonico sao conjuntos diferentes, e o")
            print("         resultado rdot=0 (D5) precisa ser reexaminado.")

    # ---- o que cada uma diz sobre rdot ----
    print("\n(4) O QUE CADA RAMO IMPLICA PARA rdot\n")
    rdot = sp.simplify(bdot/a - b*adot/a**2)
    print(f"    rdot = {sp.simplify(rdot)}\n")

    print("    ramo do corpus  (adot/a - bdot/b = 0):")
    sol_corpus = sp.solve(sp.Eq(adot/a - bdot/b, 0), pb)
    if sol_corpus:
        rdot_corpus = sp.simplify(rdot.subs(pb, sol_corpus[0]))
        print(f"      rdot = {rdot_corpus}   "
              f"{'-> rdot = 0 (confirma D5)' if sp.simplify(rdot_corpus) == 0 else '-> rdot NAO nulo'}")

    print("\n    ramo canonico  (adot/N_g - bdot/N_f = 0):")
    sol_canon = sp.solve(sp.Eq(adot/Ng - bdot/Nf, 0), pb)
    if sol_canon:
        rdot_canon = sp.simplify(rdot.subs(pb, sol_canon[0]))
        print(f"      rdot = {sp.factor(rdot_canon)}   "
              f"{'-> rdot = 0' if sp.simplify(rdot_canon) == 0 else '-> rdot NAO e nulo!'}")

    print("\n" + "=" * 70)
    print("O QUE ESTA EM JOGO")
    print()
    print("  Se as duas formas coincidem on-shell: D5 (rdot=0) fica")
    print("  intacta, a constraint canonica so a reescreve, e o Passo 3")
    print("  segue com a formula limpa do deslocamento.")
    print()
    print("  Se NAO coincidem: o 'ramo dinamico' do corpus nao e o ramo")
    print("  que a analise canonica produz, e rdot=0 — classificado")
    print("  Nivel 1 na estratificacao — precisa ser reclassificado e")
    print("  reexaminado. Isso afetaria o parecer, nao so o plano v2.")
    print("=" * 70)
    return 0


if __name__ == '__main__':
    sys.exit(main())
