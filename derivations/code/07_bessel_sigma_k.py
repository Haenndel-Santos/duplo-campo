# -*- coding: utf-8 -*-
"""
07_bessel_sigma_k.py — Derivacao 7 (plano P7.1–P7.6).

Resolve exatamente a equacao de modo do Cap.10 §10.3,

    sigma_k'' + 2(a'/a) sigma_k' + (k^2 - a^2 |m_sigma^2|) sigma_k = 0,

em fundo de Sitter a = -1/(H tau), via funcoes de Hankel, e verifica a
claim "para k << aH: sigma_k ~ k^{-3/2}".

Parte A (sympy): confirma que u = a sigma, com
    u'' + (k^2 - (nu^2 - 1/4)/tau^2) u = 0,  nu^2 = 9/4 + |m^2|/H^2,
tem solucao u = sqrt(-tau) H_nu^{(1)}(-k tau); extrai o expoente
super-horizonte |sigma_k| ~ k^{-nu} e o indice espectral
n_sigma - 1 = 3 - 2 nu.

Parte B (scipy): integra numericamente o modo de sub- a super-horizonte
com condicao inicial de Bunch-Davies e mede o expoente d ln|sigma|/d ln k,
comparando com -nu para |m^2|/H^2 = 0, 1, 3.

Uso:  python 07_bessel_sigma_k.py    (saida em out/07_output.txt)
"""
import os
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

OUT = []


def say(*args):
    line = " ".join(str(x) for x in args)
    print(line)
    OUT.append(line)


# ----------------------------------------------------------------------
# Parte A — verificacao simbolica
# ----------------------------------------------------------------------
def parte_A():
    say("=" * 70)
    say("PARTE A — solucao exata (sympy)")
    say("=" * 70)

    tau, kk, nu = sp.symbols('tau k nu', positive=True)
    m2H2 = sp.Symbol('mu2', positive=True)   # |m_sigma^2| / H^2

    # (P7.1/P7.2) reducao a forma de Bessel: u = a sigma, a = -1/(H tau)
    # sigma'' + 2(a'/a) sigma' + (k^2 - a^2|m^2|) sigma = 0
    # => u'' + (k^2 - (a''/a) - a^2 |m^2|) u = 0, a''/a = 2/tau^2,
    #    a^2|m^2| = |m^2|/(H^2 tau^2)
    # => u'' + (k^2 - (2 + mu2)/tau^2) u = 0 ; 2 + mu2 = nu^2 - 1/4
    nu2 = sp.Rational(9, 4) + m2H2
    say("nu^2 = 9/4 + |m_sigma^2|/H^2  (massa taquionica AUMENTA nu)")

    # verificacao: u = sqrt(-tau)*Hankel1(nu, -k*tau) resolve a EDO
    # (usamos x = -k tau > 0)
    x = sp.Symbol('x', positive=True)
    u = sp.sqrt(x) * sp.hankel1(nu, x)
    ode = sp.diff(u, x, 2) + (1 - (nu**2 - sp.Rational(1, 4)) / x**2) * u
    resid = sp.simplify(sp.expand_func(ode))
    # sympy nao aplica a recorrencia de Bessel sozinho:
    # H_{nu-2}(x) = 2(nu-1)/x H_{nu-1}(x) - H_nu(x)
    resid = resid.subs(sp.hankel1(nu - 2, x),
                       2 * (nu - 1) / x * sp.hankel1(nu - 1, x)
                       - sp.hankel1(nu, x))
    resid = sp.simplify(sp.expand(resid))
    say("residuo da EDO com u = sqrt(-tau) H1_nu(-k tau):", resid)
    assert resid == 0

    # (P7.4) limite super-horizonte x -> 0: H1_nu(x) ~ -(i/pi)Gamma(nu)(x/2)^-nu
    # => u ~ x^{1/2 - nu}; sigma = u/a = -H tau u => |sigma| ~ k^{-nu} * f(tau)
    say("")
    say("limite super-horizonte (-k tau -> 0):")
    say("  |u| ~ (k)^(-nu) * (-tau)^(1/2-nu) * Gamma(nu) 2^nu / pi")
    say("  |sigma_k| = |u|/a ~ k^(-nu)   [dependencia em k]")
    say("")
    say("=> claim do Cap.10 §10.3 ('sigma_k ~ k^{-3/2}') vale SOMENTE se")
    say("   nu = 3/2, i.e. |m_sigma^2| << H^2. Com massa taquionica nao")
    say("   desprezivel, nu = sqrt(9/4 + |m^2|/H^2) > 3/2 e o espectro e")
    say("   red-tilted:")
    say("   n_sigma - 1 = 3 - 2 nu ~= -(2/3)|m_sigma^2|/H^2  (expansao)")
    ns_minus_1 = sp.series(3 - 2 * sp.sqrt(nu2), m2H2, 0, 2)
    say("   expansao exata: n_sigma - 1 =", ns_minus_1)
    say("")
    tabela = []
    for mu2v in (0, sp.Rational(1, 2), 1, 2, 3):
        nuv = sp.sqrt(sp.Rational(9, 4) + mu2v)
        tabela.append((float(mu2v), float(nuv), float(3 - 2 * nuv)))
    say("  |m^2|/H^2    nu       n_sigma-1")
    for r_ in tabela:
        say(f"   {r_[0]:6.2f}   {r_[1]:6.4f}   {r_[2]:+8.4f}")
    return tabela


# ----------------------------------------------------------------------
# Parte B — integracao numerica e medida do expoente
# ----------------------------------------------------------------------
def parte_B():
    say("")
    say("=" * 70)
    say("PARTE B — integracao numerica (scipy) e expoente medido")
    say("=" * 70)

    H = 1.0

    def evolve(kv, mu2, tau_end=-1e-3):
        """
        Integra u'' + (k^2 - (2+mu2)/tau^2) u = 0 de tau_i (sub-horizonte)
        a tau_end, com condicao de Bunch-Davies u = e^{-i k tau}/sqrt(2k).
        Retorna |sigma| = |u| * H * |tau| em tau_end.
        """
        tau_i = -60.0 / kv

        def rhs(tau, y):
            ur, ui, vr, vi = y
            w2 = kv**2 - (2.0 + mu2) / tau**2
            return [vr, vi, -w2 * ur, -w2 * ui]

        u0 = np.exp(-1j * kv * tau_i) / np.sqrt(2 * kv)
        v0 = -1j * kv * u0
        y0 = [u0.real, u0.imag, v0.real, v0.imag]
        sol = solve_ivp(rhs, (tau_i, tau_end), y0, rtol=1e-10, atol=1e-12,
                        dense_output=False, max_step=abs(tau_i) / 200)
        ur, ui = sol.y[0, -1], sol.y[1, -1]
        u_abs = np.hypot(ur, ui)
        return u_abs * H * abs(tau_end)

    say("expoente medido p = d ln|sigma_k| / d ln k (em tau_end = -1e-3):")
    say("  |m^2|/H^2   p_medido    -nu_teorico   diferenca")
    ok = True
    for mu2 in (0.0, 1.0, 3.0):
        ks = np.array([0.25, 0.5, 1.0, 2.0, 4.0])
        amps = np.array([evolve(kv, mu2) for kv in ks])
        p = np.polyfit(np.log(ks), np.log(amps), 1)[0]
        nu = np.sqrt(2.25 + mu2)
        diff = p - (-nu)
        say(f"   {mu2:6.2f}    {p:+8.4f}    {-nu:+8.4f}    {diff:+.2e}")
        if abs(diff) > 0.01:
            ok = False
    say("")
    say("expoente numerico coincide com -nu (tol 1%):", ok)
    if not ok:
        say("[!] divergencia acima da tolerancia — investigar")
    return ok


def main():
    parte_A()
    ok = parte_B()
    say("")
    say("=" * 70)
    say("CONCLUSAO (P7.5)")
    say("=" * 70)
    say("A solucao exata e sigma_k = (H/ k^{3/2}) (sqrt(pi)/2) (-k tau)^{3/2}")
    say("H^{(1)}_nu(-k tau) (normalizacao Bunch-Davies), com")
    say("nu = sqrt(9/4 + |m_sigma^2|/H^2).")
    say("O comportamento super-horizonte e |sigma_k| ~ k^{-nu}, NAO k^{-3/2}")
    say("em geral. A claim do Cap.10 §10.3 e o caso limite nu -> 3/2")
    say("(|m_sigma^2| << H^2), condicao que precisa ser declarada no texto")
    say("e que conecta com §10.7 ('massa efetiva pequena').")
    say("Previsao quantitativa: n_sigma - 1 = 3 - 2 nu ~= -(2/3)|m^2|/H^2.")

    os.makedirs("out", exist_ok=True)
    with open("out/07_output.txt", "w", encoding="utf-8") as fh:
        fh.write("\n".join(OUT))
    say("\nsaida salva em out/07_output.txt")


if __name__ == '__main__':
    main()
