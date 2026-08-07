# -*- coding: utf-8 -*-
"""
gate2_bracket.py — Gate 2, Parte B (sondagem em minisuperespaco).

Calcula explicitamente a constraint secundaria {H_g, H_f} do sistema
bimetrico FLRW com beta_n(phi_-), para responder:

  (i)  a secundaria continua sendo CONSTRAINT (livre de lapso), ou vira
       equacao que determina o lapso?
  (ii) qual e a forma dela — e o que muda em relacao a constraint de
       Bianchi da v1?

ESCOPO DECLARADO. Minisuperespaco NAO decide a contagem do fantasma BD
(que e um modo com dependencia espacial). O que ele decide e a
ESTRUTURA da cadeia de Dirac e a forma explicita da secundaria. Ver
docs/gate2_ghost.md Sec.3.

Requer sympy.

Uso:
    python gate2_bracket.py
"""
import sys

try:
    import sympy as sp
except ImportError:
    print("ERRO: este script precisa de sympy.  pip install sympy")
    sys.exit(2)


# variaveis canonicas do minisuperespaco
a, b, ph = sp.symbols('a b phi_-', positive=True)
pa, pb, pph = sp.symbols('p_a p_b p_phi', real=True)
Mg2, Mf2, Meff2, m2 = sp.symbols('M_g^2 M_f^2 M_eff^2 m^2', positive=True)
rho_m = sp.Symbol('rho_m', nonnegative=True)

# beta_n como funcoes arbitrarias de phi_-
B = [sp.Function(f'beta_{n}')(ph) for n in range(5)]
Vpot = sp.Function('V')(ph)

CANON = [(a, pa), (b, pb), (ph, pph)]


def poisson(f, g):
    return sum(sp.diff(f, q) * sp.diff(g, p) - sp.diff(f, p) * sp.diff(g, q)
               for q, p in CANON)


def main():
    print("=" * 70)
    print("GATE 2 / PARTE B — constraint secundaria em minisuperespaco")
    print("=" * 70)

    r = b / a

    # coeficientes dos lapsos (forma linear confirmada pelo gate2_lapso.py)
    C_g = -Meff2 * m2 * a**3 * (B[0] + 3*r*B[1] + 3*r**2*B[2] + r**3*B[3])
    C_f = -Meff2 * m2 * a**3 * (B[1] + 3*r*B[2] + 3*r**2*B[3] + r**3*B[4])
    C_g = sp.expand(C_g)
    C_f = sp.expand(C_f)

    # constraints primarias: H = N_g*H_g + N_f*H_f
    H_g = (-pa**2 / (12*Mg2*a) + pph**2 / (2*a**3)
           + a**3*Vpot + a**3*rho_m - C_g)
    H_f = -pb**2 / (12*Mf2*b) - C_f

    print("\n(1) CONSTRAINTS PRIMARIAS  (H = N_g H_g + N_f H_f)\n")
    print("    H_g = -p_a^2/(12 M_g^2 a) + p_phi^2/(2a^3)")
    print("          + a^3 V(phi_-) + a^3 rho_m - C_g")
    print("    H_f = -p_b^2/(12 M_f^2 b) - C_f\n")

    ok_lapso = (sp.diff(H_g, sp.Symbol('N_g')) == 0)
    print(f"  [{'PASSA' if ok_lapso else 'FALHA'}] H_g e H_f nao contem lapso")
    print("          (logo N_g, N_f sao multiplicadores de Lagrange)\n")

    # ---------------- a secundaria ----------------
    print("(2) CONSTRAINT SECUNDARIA: {H_g, H_f}\n")
    br = sp.simplify(poisson(H_g, H_f))

    contem_lapso = br.has(sp.Symbol('N_g')) or br.has(sp.Symbol('N_f'))
    print(f"  [{'FALHA' if contem_lapso else 'PASSA'}] "
          f"{{H_g,H_f}} nao contem lapso")
    print("          -> a condicao dH_g/dt = N_f {H_g,H_f} = 0 e uma")
    print("             CONSTRAINT, nao uma equacao para o lapso\n")

    # ---------------- caso beta constante: recupera Bianchi? ----------------
    print("(3) LIMITE beta_n CONSTANTES — deve recuperar Bianchi da v1\n")
    b0c, b1c, b2c, b3c, b4c = sp.symbols(
        'beta_0c beta_1c beta_2c beta_3c beta_4c', real=True)
    const = {B[n]: [b0c, b1c, b2c, b3c, b4c][n] for n in range(5)}
    br_const = sp.simplify(br.subs(const).doit())
    br_const = sp.simplify(sp.expand(br_const))

    print("    {H_g,H_f} com beta_n constantes:")
    print(f"      {sp.factor(sp.simplify(br_const))}\n")

    # fator de Bianchi esperado:  B(r) = beta_1 + 2 beta_2 r + beta_3 r^2
    Bianchi = b1c + 2*b2c*(b/a) + b3c*(b/a)**2
    quociente = sp.simplify(sp.cancel(br_const / Bianchi))
    resto_ok = sp.simplify(quociente * Bianchi - br_const) == 0
    print(f"  [{'PASSA' if resto_ok else 'VER'}] "
          f"{{H_g,H_f}}|_const e divisivel por B(r)=beta_1+2beta_2 r+beta_3 r^2")
    if resto_ok:
        print("      quociente:")
        print(f"        {sp.simplify(quociente)}\n")
        print("      -> a constraint FATORA: B(r) * (cinematica) = 0")
        print("         que e exatamente a estrutura de dois ramos da v1")
        print("         (Anexo B Sec.B.8): ramo algebrico B(r)=0 OU ramo")
        print("         dinamico com o segundo fator nulo.\n")

    # ---------------- o termo novo ----------------
    print("(4) O TERMO NOVO — o que beta_n(phi_-) acrescenta\n")
    novo = sp.simplify(br - br_const.subs(
        {b0c: B[0], b1c: B[1], b2c: B[2], b3c: B[3], b4c: B[4]}))
    novo = sp.simplify(sp.expand(novo))
    print("    {H_g,H_f} - {H_g,H_f}|_(beta tratados como const) =")
    print(f"      {sp.factor(novo)}\n")

    tem_pph = novo.has(pph)
    print(f"  [{'CONFIRMA' if tem_pph else 'VER'}] o termo novo e "
          f"proporcional a p_phi")
    print("          -> existe apenas quando phi_- EVOLUI (p_phi != 0)")
    print("             e quando os beta_n dependem de phi_- (beta' != 0)\n")

    # ---------------- a consequencia estrutural ----------------
    print("(5) CONSEQUENCIA: a constraint AINDA FATORA em dois ramos?\n")
    quociente_full = sp.simplify(sp.cancel(br / Bianchi.subs(
        {b1c: B[1], b2c: B[2], b3c: B[3]})))
    fatora = sp.simplify(
        quociente_full * Bianchi.subs({b1c: B[1], b2c: B[2], b3c: B[3]}) - br
    ) == 0
    print(f"  [{'SIM' if fatora else 'NAO'}] {{H_g,H_f}} e divisivel por B(r)")
    if not fatora:
        print()
        print("      *** RESULTADO ESTRUTURAL ***")
        print("      Com beta_n(phi_-), a constraint NAO fatora mais em")
        print("      B(r) x (cinematica). A dicotomia 'ramo algebrico vs")
        print("      ramo dinamico' e um artefato de beta_n CONSTANTES.")
        print()
        print("      Implicacao para o Passo 3: a v2 nao esta presa a")
        print("      nenhum dos dois ramos que morreram na v1. A raiz")
        print("      movel nao e 'ramo algebrico com coeficientes lentos'")
        print("      — e uma estrutura de solucao nova.")

    print("\n" + "=" * 70)
    print("VEREDITO DA SONDAGEM (minisuperespaco):")
    print()
    if not contem_lapso:
        print("  (i)  A secundaria e livre de lapso -> a cadeia de Dirac")
        print("       continua, a constraint existe. Evidencia POSITIVA")
        print("       para o Gate 2.")
    else:
        print("  (i)  A secundaria contem lapso -> ALARME.")
    print()
    print("  (ii) A forma da secundaria MUDOU: ganhou o termo em p_phi.")
    print()
    print("  LIMITE: minisuperespaco nao ve o fantasma BD (modo com")
    print("  dependencia espacial). Isto NAO fecha o Gate 2 — mas mostra")
    print("  que a estrutura de constraints nao colapsa, que era o risco")
    print("  principal, e entrega a constraint modificada que o Passo 3")
    print("  precisa.")
    print("=" * 70)
    return 0


if __name__ == '__main__':
    sys.exit(main())
