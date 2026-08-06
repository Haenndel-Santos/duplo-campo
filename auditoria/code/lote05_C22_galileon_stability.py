# -*- coding: utf-8 -*-
"""
lote05_C22_galileon_stability.py — verificacao simbolica das formulas
Z_t, Z_r, Z_Omega do Cap.22 Sec.22.5 (C22.10-C22.12/C22.16) do corpus
TDCP-F1, geradas a partir da matriz cinetica K^{mu nu} do galileon
cubico (C22.07) para flutuacoes em torno de um background estatico
esfericamente simetrico pi_bar(r).

Contexto (auditoria/lotes/lote_05_C22-C26.md): a conta a mao nesta
auditoria NAO reproduziu os coeficientes em caixa do Cap.22 Sec.22.5 a
partir de C22.07 + a decomposicao da Hessiana radial/angular de
C22.09 (essa ultima foi verificada e confere). O proprio texto
ressalva "ate fatores convencionais de sinal" -- entao a discrepancia
pode ser so uma convencao de projecao/normalizacao nao declarada, nao
necessariamente um erro. Este script refaz a conta com rigor (indices
cartesianos completos, assinatura (-,+,+,+), projecao radial/angular
explicita) para decidir.

Rode:  python lote05_C22_galileon_stability.py
"""
import sympy as sp

x, y, z, r = sp.symbols('x y z r', real=True)
c3, Lam3, Z = sp.symbols('c_3 Lambda_3 Z', positive=True)

# pi_bar(r) generico (funcao radial arbitraria) -- trabalhamos em
# coordenadas cartesianas com r = sqrt(x^2+y^2+z^2) para poder tomar
# derivadas parciais cartesianas genuinas (∂_i∂_j), depois projetamos
# no ponto (0,0,z0) por simetria esferica (qualquer ponto serve).
pib = sp.Function('pibar')
Rexpr = sp.sqrt(x**2 + y**2 + z**2)
pi_of_xyz = pib(Rexpr)

coords = [x, y, z]

# eta^{mu nu} = diag(-1,1,1,1) (mostly-plus, consistente com C18.01)
eta = sp.diag(-1, 1, 1, 1)

# derivadas espaciais cartesianas de pi_bar (indices para baixo = para
# cima no espaco plano euclidiano)
d2 = sp.Matrix(3, 3, lambda i, j: sp.diff(pi_of_xyz, coords[i], coords[j]))

# Box pi_bar = eta^{mu nu} d_mu d_nu pi_bar. pi_bar estatico (sem
# dependencia temporal) => so a parte espacial contribui, com o sinal
# espacial (+1,+1,+1) de eta:
box_pi = sp.trigsimp(sp.simplify(d2[0, 0] + d2[1, 1] + d2[2, 2]))

# ponto de avaliacao: eixo z, (0,0,z0) com z0>0 -- por simetria
# esferica, qualquer direcao serve; usamos o eixo z para simplificar
z0 = sp.Symbol('z0', positive=True)
subs_point = {x: 0, y: 0, z: z0}


def d_r(n):
    """n-esima derivada de pibar em r, como funcao de r."""
    f = pib(r)
    for _ in range(n):
        f = sp.diff(f, r)
    return f


pibar_p = d_r(1)   # pibar'(r)
pibar_pp = d_r(2)  # pibar''(r)

# --- Verificacao independente de C22.08 e C22.09 (ja conferidas a
#     mao nesta auditoria; usadas aqui so como checagem cruzada) ---
box_pi_at_point = box_pi.subs(subs_point)
box_pi_radial_form = (pibar_pp + 2 * pibar_p / r).subs(r, z0)
check_C22_08 = sp.simplify(
    box_pi_at_point.rewrite(sp.Derivative)
    - box_pi_radial_form.rewrite(sp.Derivative)
)

print("=== Checagem cruzada C22.08 (Box pibar = pibar'' + 2 pibar'/r) ===")
print("diferenca (deve ser 0):", check_C22_08)

# --- Matriz cinetica completa K^{mu nu} = Z eta^{mu nu}
#     + (2 c3/Lambda3^3) [ 2 d^mu d^nu pibar - eta^{mu nu} Box pibar ] ---
# indices 0..3 = (t, x, y, z); pibar estatico => d^0(...) = 0 sempre.
d2_4 = sp.zeros(4, 4)
for i in range(3):
    for j in range(3):
        d2_4[i + 1, j + 1] = d2[i, j]
# d^mu d^nu com indices levantados: no espaco plano euclidiano
# (assinatura espacial +1,+1,+1) d^i = d_i; d^0 = -d_0 = 0 (estatico).
box_pi_4 = box_pi  # eta^{munu} d_mu d_nu pibar (ja calculado acima)

Kmunu = Z * eta + (2 * c3 / Lam3**3) * (2 * d2_4 - eta * box_pi_4)

K00 = sp.simplify(Kmunu[0, 0].subs(subs_point))
Kxx = sp.simplify(Kmunu[1, 1].subs(subs_point))
Kyy = sp.simplify(Kmunu[2, 2].subs(subs_point))
Kzz = sp.simplify(Kmunu[3, 3].subs(subs_point))

# no ponto (0,0,z0), a direcao radial e o eixo z (n=(0,0,1)); as
# direcoes angulares/transversas sao x,y.
K_radial = Kzz    # K^{zz} = componente ao longo de n^i n^j
K_ang = Kxx        # K^{xx} = K^{yy} = componente transversa (angular)

print("\n=== K^00 (deveria dar -Z_t, com Z_t = Z - (2c3/Lam3^3) Box_pibar"
      " pela algebra desta auditoria) ===")
print("K^00 bruto:", K00)

print("\n=== K^zz = componente radial (deveria dar Z_r) ===")
print("K^zz bruto:", Kzz)

print("\n=== K^xx = componente angular/transversa (deveria dar Z_Omega) ===")
print("K^xx bruto:", Kxx)

# --- Comparacao numerica direta com uma pibar(r) de teste concreta,
#     para evitar a fragilidade de sp.Function em simplificacao
#     simbolica com mudanca de variavel r->sqrt(x^2+y^2+z^2) ---
print("\n=== Checagem numerica com pibar(r) = r**p (potencia de teste) ===")
p_test = sp.Rational(-1, 2)  # regime Vainshtein: y=pibar'/r ~ r^{-3/2}
Zn, c3n, Lam3n = 1, 1, 1
z0n = sp.Rational(3, 2)

pibar_num = Rexpr**p_test
d2_num = sp.Matrix(3, 3, lambda i, j: sp.diff(pibar_num, coords[i], coords[j]))
box_num = sp.simplify((d2_num[0, 0] + d2_num[1, 1] + d2_num[2, 2])
                       .subs(subs_point))

K00_num = sp.simplify(
    (Zn * (-1) + (2 * c3n / Lam3n**3) * (0 - (-1) * box_num))
)
Kzz_num = sp.simplify(
    Zn + (2 * c3n / Lam3n**3) * (2 * d2_num[2, 2].subs(subs_point) - box_num)
)
Kxx_num = sp.simplify(
    Zn + (2 * c3n / Lam3n**3) * (2 * d2_num[0, 0].subs(subs_point) - box_num)
)
K00_num = K00_num.subs(z0, z0n)
Kzz_num = Kzz_num.subs(z0, z0n)
Kxx_num = Kxx_num.subs(z0, z0n)

pibar_p_num = sp.diff(r**p_test, r).subs(r, z0n)
pibar_pp_num = sp.diff(r**p_test, r, 2).subs(r, z0n)

Zt_boxed = Zn + 4 * c3n / Lam3n**3 * (pibar_pp_num + 2 * pibar_p_num / z0n)
Zr_boxed = Zn + 8 * c3n / Lam3n**3 * (pibar_p_num / z0n)
ZOmega_boxed = Zn + 4 * c3n / Lam3n**3 * (pibar_pp_num + pibar_p_num / z0n)

print(f"pibar'(z0)={pibar_p_num}, pibar''(z0)={pibar_pp_num}")
print(f"K^00 numerico = {sp.nsimplify(K00_num)}  vs  -Z_t(caixa) = {-sp.nsimplify(Zt_boxed)}")
print(f"K^zz numerico = {sp.nsimplify(Kzz_num)}  vs  Z_r(caixa)  = {sp.nsimplify(Zr_boxed)}")
print(f"K^xx numerico = {sp.nsimplify(Kxx_num)}  vs  Z_Omega(caixa) = {sp.nsimplify(ZOmega_boxed)}")

print("\nSe as linhas acima NAO baterem, o Cap.22 Sec.22.5 (C22.10-12,"
      " C22.16) precisa de ERRO DE CALCULO com a forma corrigida; se"
      " baterem, o veredito desta auditoria (CONFERE SOB HIPOTESE,"
      " pendente de verificacao) deve virar CONFERE simples.")
