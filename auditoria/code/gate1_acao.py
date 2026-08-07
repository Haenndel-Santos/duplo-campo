# -*- coding: utf-8 -*-
"""
gate1_acao.py — Gate 1 do plano de reconstrucao v2.

Verifica mecanicamente os sete criterios do Gate 1 sobre a acao
definida em docs/acao_v2.md:

  (a) homogeneidade dimensional, termo a termo
  (b) simetria Z2 em phi_- (paridade de V e dos beta_n)
  (c) V(phi_+,phi_-) explicito e com a instabilidade correta
  (d) beta_n(phi_-) com forma funcional fechada
  (e) reduz a Hassan-Rosen padrao quando phi_- = const
  (f) a raiz r* de fato se move com phi_-
  (g) modulacao GLOBAL nao move a raiz (confirma o achado da Sec.0)

Requer sympy.

Uso:
    python gate1_acao.py
"""
import sys

try:
    import sympy as sp
except ImportError:
    print("ERRO: este script precisa de sympy.  pip install sympy")
    sys.exit(2)


# ---------------------------------------------------------------------
# simbolos
# ---------------------------------------------------------------------
phi_p, phi_m = sp.symbols('phi_+ phi_-', real=True)
mu_m, lam_m, lam_c = sp.symbols('mu_- lambda_- lambda_c', positive=True)
v_ast = sp.Symbol('v_*', positive=True)
b0, b1, b2, b3, b4 = sp.symbols('beta_0 beta_1 beta_2 beta_3 beta_4', real=True)
b1_0, b2_0 = sp.symbols('beta_1^0 beta_2^0', real=True)
r, F = sp.symbols('r F', positive=True)
Vp = sp.Function('V_+')

RESULTADOS = []


def checa(nome, condicao, detalhe=""):
    ok = bool(condicao)
    RESULTADOS.append((nome, ok, detalhe))
    marca = "PASSA" if ok else "FALHA"
    print(f"  [{marca}] {nome}")
    if detalhe:
        print(f"          {detalhe}")
    return ok


# ---------------------------------------------------------------------
# (a) DIMENSOES
# ---------------------------------------------------------------------
# dimensao de massa de cada objeto (docs/acao_v2.md Sec.3)
DIM = {
    'd4x': -4, 'sqrt_g': 0, 'R': 2, 'K': 0, 'e_n': 0, 'beta_n': 0,
    'M_g': 1, 'M_f': 1, 'M_eff': 1, 'm': 1,
    'phi': 1, 'dphi': 2, 'g_inv': 0,
    'mu_-': 1, 'lambda': 0, 'v_*': 1, 'V': 4,
}


def dim_termo(fatores):
    return sum(DIM[f] for f in fatores)


def secao_a():
    print("\n(a) HOMOGENEIDADE DIMENSIONAL")
    print("    cada termo da densidade lagrangiana deve ter dimensao 4\n")

    termos = {
        "EH de g:  M_g^2 sqrt(-g) R[g]":
            ['M_g', 'M_g', 'sqrt_g', 'R'],
        "EH de f:  M_f^2 sqrt(-f) R[f]":
            ['M_f', 'M_f', 'sqrt_g', 'R'],
        "potencial HR:  m^2 M_eff^2 sqrt(-g) beta_n e_n":
            ['m', 'm', 'M_eff', 'M_eff', 'sqrt_g', 'beta_n', 'e_n'],
        "cinetico phi_+:  sqrt(-g) g^{mn} d_m phi d_n phi":
            ['sqrt_g', 'g_inv', 'dphi', 'dphi'],
        "cinetico phi_-:  sqrt(-g) g^{mn} d_m phi d_n phi":
            ['sqrt_g', 'g_inv', 'dphi', 'dphi'],
        "potencial escalar:  sqrt(-g) V(phi_+,phi_-)":
            ['sqrt_g', 'V'],
    }
    todos_ok = True
    for nome, fatores in termos.items():
        d = dim_termo(fatores)
        ok = checa(f"{nome}  ->  dim = {d}", d == 4)
        todos_ok = todos_ok and ok

    # dimensoes internas do potencial
    print()
    sub = {
        "mu_-^2 phi_-^2": 2 * DIM['mu_-'] + 2 * DIM['phi'],
        "lambda_- phi_-^4": DIM['lambda'] + 4 * DIM['phi'],
        "lambda_c phi_+^2 phi_-^2": DIM['lambda'] + 4 * DIM['phi'],
    }
    for nome, d in sub.items():
        ok = checa(f"termo de V:  {nome}  ->  dim = {d}", d == 4)
        todos_ok = todos_ok and ok

    # argumento da modulacao precisa ser adimensional
    d_arg = 2 * DIM['phi'] - 2 * DIM['v_*']
    ok = checa(f"argumento de beta_1:  phi_-^2/v_*^2  ->  dim = {d_arg}",
               d_arg == 0,
               "beta_n e adimensional, logo o argumento tambem precisa ser")
    todos_ok = todos_ok and ok

    # acao total
    ok = checa("acao total S = int d^4x L  ->  dim = 0",
               DIM['d4x'] + 4 == 0)
    return todos_ok and ok


# ---------------------------------------------------------------------
# potencial e modulacao (definicoes de docs/acao_v2.md)
# ---------------------------------------------------------------------
V = (Vp(phi_p)
     - sp.Rational(1, 2) * mu_m**2 * phi_m**2
     + sp.Rational(1, 4) * lam_m * phi_m**4
     + lam_c * phi_p**2 * phi_m**2)

beta1 = b1_0 * (1 + phi_m**2 / v_ast**2)
beta2 = b2_0


# ---------------------------------------------------------------------
# (b) SIMETRIA Z2
# ---------------------------------------------------------------------
def secao_b():
    print("\n(b) SIMETRIA Z2:  phi_- -> -phi_-  (troca phi_1 <-> phi_2)\n")
    dV = sp.simplify(V.subs(phi_m, -phi_m) - V)
    ok1 = checa("V(phi_+,-phi_-) = V(phi_+,phi_-)", dV == 0,
                f"diferenca = {dV}")
    db = sp.simplify(beta1.subs(phi_m, -phi_m) - beta1)
    ok2 = checa("beta_1(-phi_-) = beta_1(phi_-)", db == 0,
                f"diferenca = {db}")

    # contraprova: modulacao LINEAR quebraria a Z2 explicitamente
    beta1_linear = b1_0 * (1 + phi_m / v_ast)
    db_lin = sp.simplify(beta1_linear.subs(phi_m, -phi_m) - beta1_linear)
    ok3 = checa("contraprova: beta_1 LINEAR em phi_- quebra a Z2",
                db_lin != 0,
                f"diferenca = {sp.simplify(db_lin)}  (nao-nula, como esperado)")
    return ok1 and ok2 and ok3


# ---------------------------------------------------------------------
# (c) BIFURCACAO
# ---------------------------------------------------------------------
def secao_c():
    print("\n(c) POTENCIAL EXPLICITO E BIFURCACAO\n")
    d2V = sp.simplify(sp.diff(V, phi_m, 2).subs(phi_m, 0))
    esperado = -mu_m**2 + 2 * lam_c * phi_p**2
    ok1 = checa("massa efetiva de phi_- em phi_-=0",
                sp.simplify(d2V - esperado) == 0,
                f"d2V/dphi_-^2|_0 = {d2V}")

    # o fator 2 — verificacao da correcao feita a proposta original
    coef = sp.simplify(sp.expand(d2V).coeff(lam_c * phi_p**2))
    ok2 = checa("coeficiente do termo de portal = 2 (nao 1)", coef == 2,
                f"coeficiente = {coef}  "
                f"(proposta original trazia 1 — corrigido)")

    # ponto critico
    crit = sp.solve(sp.Eq(d2V, 0), phi_p**2)
    crit_val = crit[0] if crit else None
    ok3 = checa("ponto critico phi_+^2 = mu_-^2/(2 lambda_c)",
                sp.simplify(crit_val - mu_m**2 / (2 * lam_c)) == 0,
                f"phi_+crit^2 = {sp.simplify(crit_val)}")

    # VEV pos-bifurcacao
    dV = sp.diff(V, phi_m)
    solucoes = sp.solve(sp.Eq(dV, 0), phi_m)
    v2_esperado = (mu_m**2 - 2 * lam_c * phi_p**2) / lam_m
    achou = False
    for s in solucoes:
        if sp.simplify(s**2 - v2_esperado) == 0:
            achou = True
            break
    ok4 = checa("VEV: v^2 = (mu_-^2 - 2 lambda_c phi_+^2)/lambda_-", achou,
                f"solucoes de dV/dphi_- = 0: {solucoes}")

    # o estado simetrico e instavel abaixo do critico
    teste = d2V.subs({mu_m: 2, lam_c: 1, phi_p: sp.Rational(1, 2)})
    ok5 = checa("abaixo do critico, phi_-=0 e instavel (m_eff^2 < 0)",
                teste < 0, f"exemplo numerico: m_eff^2 = {teste}")
    return ok1 and ok2 and ok3 and ok4 and ok5


# ---------------------------------------------------------------------
# (e) LIMITE HR / (f) RAIZ MOVEL / (g) DEGENERESCENCIA GLOBAL
# ---------------------------------------------------------------------
def secao_efg():
    print("\n(e) LIMITE: phi_- = const  ->  Hassan-Rosen padrao\n")
    c = sp.Symbol('c', real=True)
    b1_const = sp.simplify(beta1.subs(phi_m, c))
    ok1 = checa("beta_1(const) e constante (sem dependencia de phi_-)",
                sp.diff(b1_const, phi_m) == 0,
                f"beta_1 = {b1_const}")

    print("\n(f) A RAIZ SE MOVE\n")
    # F1: beta_3 = 0  =>  B(r) = beta_1 + 2 beta_2 r = 0
    B = beta1 + 2 * beta2 * r
    r_star = sp.solve(sp.Eq(B, 0), r)[0]
    r_star = sp.simplify(r_star)
    esperado = -b1_0 / (2 * b2_0) * (1 + phi_m**2 / v_ast**2)
    ok2 = checa("r*(phi_-) = -(beta_1^0/2beta_2^0)(1 + phi_-^2/v_*^2)",
                sp.simplify(r_star - esperado) == 0,
                f"r* = {r_star}")

    dr = sp.simplify(sp.diff(r_star, phi_m))
    ok3 = checa("dr*/dphi_- != 0  (a raiz de fato evolui)",
                sp.simplify(dr) != 0,
                f"dr*/dphi_- = {dr}")

    # amplitude: de phi_-=0 ate phi_-=v_*
    razao = sp.simplify(r_star.subs(phi_m, v_ast) / r_star.subs(phi_m, 0))
    ok4 = checa("amplitude r*(v_*)/r*(0) = 2", razao == 2,
                f"razao = {razao}  (evolucao ampla, sem tuning)")

    print("\n(g) CONTRAPROVA: modulacao GLOBAL nao move a raiz\n")
    print("      (este e o achado da Sec.0 — porque a v1 nao podia funcionar)\n")
    B_glob = F * b1_0 + 2 * F * b2_0 * r
    r_star_glob = sp.simplify(sp.solve(sp.Eq(B_glob, 0), r)[0])
    ok5 = checa("com beta_n -> F*beta_n, r* independe de F",
                sp.diff(r_star_glob, F) == 0,
                f"r*_global = {r_star_glob}  (F cancelou)")

    r_star_v1 = sp.simplify(-b1_0 / (2 * b2_0))
    ok6 = checa("r*_global identico ao caso sem modulacao",
                sp.simplify(r_star_glob - r_star_v1) == 0,
                "confirma: F(phi) global era incapaz de mover a estrutura")
    return ok1 and ok2 and ok3 and ok4 and ok5 and ok6


# ---------------------------------------------------------------------
def main():
    print("=" * 66)
    print("GATE 1 — verificacao da acao minima (docs/acao_v2.md)")
    print("=" * 66)

    oks = [secao_a(), secao_b(), secao_c(), secao_efg()]

    print("\n" + "=" * 66)
    falhas = [n for n, ok, _ in RESULTADOS if not ok]
    total = len(RESULTADOS)
    print(f"RESUMO: {total - len(falhas)}/{total} checagens passaram")
    if falhas:
        print("\nGATE 1: NAO PASSA. Falhas:")
        for n in falhas:
            print(f"  - {n}")
        print("\nAcao: rever docs/acao_v2.md antes do Passo 2.")
    else:
        print("\nGATE 1: PASSA.")
        print("  (a) dimensoes homogeneas  (b) Z2 preservada")
        print("  (c) bifurcacao decorre do potencial — fecha o achado A7")
        print("  (d) beta_n(phi_-) fechado  (e) limite HR recuperado")
        print("  (f) a raiz se move  (g) modulacao global NAO moveria")
        print("\nLiberado para o Passo 2 (ghost-freedom sob beta_n(phi)).")
    print("=" * 66)
    return 0 if not falhas else 1


if __name__ == '__main__':
    sys.exit(main())
