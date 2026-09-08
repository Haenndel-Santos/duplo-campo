# -*- coding: utf-8 -*-
"""
litrev_check_ft_konnig.py — revisão de literatura 2026-09-07 (docs/revisao_literatura_higuchi_modulacao_2026-09-07.md)

CRITÉRIOS PRÉ-DECLARADOS (passa/reprova):
 G1  Fasiello–Tolley 1308.1647 eq.(1.3) [= (3.18) = (7.1)], com H/H_f = r (vínculo de Bianchi,
     ramo dinâmico — os próprios F–T usam b/a = H/H_f na eq.(3.20)) e β^FT_n = 2 M_ef² β_n
     (normalização da eq.(3.1): −(m²/2)Σβ^FT U_n contra HR −m²M_ef²Σβ e_n), é IDÊNTICA à
     "forma massa" do R-13a §2.2: (m²M_ef²/M_f²)·ℬ(r)·(1+μr²)/r ≥ 2H².  Critério: resíduo simbólico 0.
 G2  A forma simétrica (1.4) difere de (1.3) por fator positivo.  Critério: razão > 0 para H,H_f > 0.
 G3  Könnig 1503.07436 eq.(14), via o mapa do R-13a §2.1 (verificado em auditoria_r13 §1), difere da
     forma massa por fator positivo.  Critério: razão > 0.
 G4  Limite primordial do ramo finito da F1 (H² → m²M_ef²β₁/(3M_f²r)): massa dinâmica de F–T / H² → 3.
 G5  De Felice–Mukohyama–Oliosi 1711.04655 eq.(43) (autovalor cinético κ₁ do gráviton escalar, UV,
     β_i(φ) GERAIS), no limite β constante (φ̇ = 0, U_{,ξφ} = J_{,φ} = 0) e no ramo dinâmico
     (H_f = H/ξ), reduz-se a  3HJ·[m²(1+κξ²)J − 2κξH²]·(a⁴m²M_g²/(8Hκ)); e, no mapa
     β^DMO_i = −(M_ef²/M_g²)β_i (eq.(2) deles: +M_g²m²Σβ_iU_i contra HR −m²M_ef²Σβ_n e_n; ξ_DMO = r,
     κ = μ), o colchete é proporcional à forma massa de G1.  Critério: resíduo 0.
 G6  Os termos de modulação de κ₁ são exibidos; o termo em U²_{,ξφ} é negativo-definido
     (aperta a condição para qualquer sinal de φ̇β′).  Critério: sinal do coeficiente.
Cegueira declarada: nada aqui mede física; é álgebra de tradução entre convenções publicadas.
"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
import sympy as sp

m,H,Hf,Mp,Mf,r,mu,b1,b2,b3,b4 = sp.symbols('m H H_f M_p M_f r mu beta1 beta2 beta3 beta4', positive=True)
Meff2 = Mp**2*Mf**2/(Mp**2+Mf**2)
B = b1 + 2*b2*r + b3*r**2                        # ℬ(r) do cap. 03
massform = m**2*Meff2/Mf**2*B*(1+mu*r**2)/r - 2*H**2   # ≥ 0  (R-13a §2.2)
bFT = {n: 2*Meff2*b for n,b in ((1,b1),(2,b2),(3,b3))}

# --- G1
x = H/Hf
mt2 = m**2/(2*Mp**2)*x*(bFT[1] + 2*bFT[2]*x + bFT[3]*x**2)      # (1.2)
LHS13 = mt2*(H**2 + Hf**2*Mp**2/Mf**2) - 2*H**4                 # (1.3) ≥ 0
res1 = sp.simplify((LHS13.subs(Hf, H/r) - massform*H**2).subs(mu, Mf**2/Mp**2))
print('G1 resíduo [FT(1.3)|_{H_f=H/r} − H²·forma-massa] =', res1, '->', 'PASSA' if res1==0 else 'REPROVA')

# --- G2
LHS14 = m**2/2*(bFT[1]*Hf**2 + 2*bFT[2]*H*Hf + bFT[3]*H**2)*(H**2/Mp**2 + Hf**2/Mf**2) - 2*Hf**3*H**3
ratio = sp.simplify(LHS14/LHS13)
print('G2 (1.4)/(1.3) =', ratio, '->', 'PASSA' if ratio.is_positive else 'REPROVA')

# --- G3
A = m**2*Meff2/Mp**2
rK = sp.sqrt(mu)*r
bK = {n: A*mu**(-sp.Rational(n,2))*b for n,b in ((1,b1),(2,b2),(3,b3),(4,b4))}
K14 = sp.Rational(3,2)*(bK[1]+2*bK[2]*rK+bK[3]*rK**2)*(1+rK**2) - 3*rK*H**2   # (14) com RHS = 3 r_K H²
prop = sp.simplify((K14/massform).subs(mu, Mf**2/Mp**2))
print('G3 Könnig(14)|mapa / forma-massa =', prop, '->', 'PASSA' if prop.is_positive else 'REPROVA')

# --- G4
H2prim = m**2*Meff2*b1/(3*Mf**2*r)
lim = sp.limit((m**2*Meff2/Mf**2*B*(1+mu*r**2)/r)/H2prim, r, 0)
print('G4 massa dinâmica de F–T / H² em r→0 (ramo finito F1) =', lim, '->', 'PASSA' if lim==3 else 'REPROVA')

# --- G5 / G6 : eq.(43) de 1711.04655
a,kap,xi,Mg = sp.symbols('a kappa xi M_g', positive=True)
J,Jxi,Jphi,Uxiphi,phid = sp.symbols('J J_xi J_phi U_xiphi phidot', real=True)
kappa1 = a**4*m**2*Mg**2/(8*H*kap)*( 3*m**2*(H - H*kap*xi**2 + 2*Hf*kap*xi**3)*J**2
        + 2*kap*xi**2*J*(3*Hf*H*(2*Hf*xi - 3*H) - sp.Rational(1,4)*m**2*phid*Uxiphi)
        + 2*H*kap*xi**2*(3*Hf*xi*(H - Hf*xi)*Jxi - 3*Hf*phid*Jphi - sp.Rational(1,16)*m**2*Mg**2*Uxiphi**2) )
k1_const = sp.simplify(kappa1.subs({phid:0, Uxiphi:0, Jphi:0, Hf:H/xi}))
target = sp.simplify(a**4*m**2*Mg**2/(8*H*kap) * 3*H*J*(m**2*(1+kap*xi**2)*J - 2*kap*xi*H**2))
print('G5a κ₁|β-const, ramo dinâmico − 3HJ[m²(1+κξ²)J − 2κξH²]·pref =', sp.simplify(k1_const - target))
# mapa para HR: J = R_{,ξ}/3 com U = −(β₄ξ⁴+4β₃ξ³+6β₂ξ²+4β₁ξ+β₀) em β^DMO; β^DMO = −(M_ef²/M_g²)β^HR
bD = {n: -(Meff2/Mp**2)*b for n,b in ((1,b1),(2,b2),(3,b3),(4,b4))}
b0 = sp.symbols('beta0', positive=True); bD[0] = -(Meff2/Mp**2)*b0
U = -(bD[4]*xi**4 + 4*bD[3]*xi**3 + 6*bD[2]*xi**2 + 4*bD[1]*xi + bD[0])
Rf = U - xi*sp.diff(U,xi)/4
Jexpr = sp.diff(Rf,xi)/3
bracket = (m**2*(1+kap*xi**2)*Jexpr - 2*kap*xi*H**2)/(kap*xi)   # ≥ 0 ⇔ κ₁ ≥ 0 (J>0, H>0)
res5 = sp.simplify((bracket - massform.subs(mu,kap)).subs({xi:r, Mp:Mg}).subs(kap, Mf**2/Mg**2))
print('G5b colchete de κ₁ (mapa HR) − forma-massa =', res5, '->', 'PASSA' if res5==0 else 'REPROVA')
mod = sp.expand(kappa1 - kappa1.subs({phid:0, Uxiphi:0, Jphi:0}))
print('G6 termos de modulação de κ₁ =', sp.factor_terms(mod))
coef_U2 = mod.coeff(Uxiphi,2)
print('   coeficiente de U_{,ξφ}² =', sp.factor(coef_U2), '-> negativo-definido:', sp.simplify(coef_U2).is_negative)
