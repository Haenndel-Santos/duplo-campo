# -*- coding: utf-8 -*-
"""
06_mu_alpha_QS.py — Derivacao 6 (plano P6.1–P6.6).

Deriva mu(k,a), eta_slip(k,a) e Sigma(k,a) EXATOS no limite
quase-estatico (QS), a partir do mesmo setor escalar do script 01,
acrescentando a fonte de materia fria delta-rho no vinculo de Phi_g
(acoplamento minimo ao setor g: L_src = -a^3 drho Phi_g, do termo
(1/2) sqrt(-g) dT^{00} dg_{00} com dT^{00} = drho, dg_00 = -2 Phi_g).

Limite QS implementado por contagem de ordens: todas as velocidades das
perturbacoes -> 0 e grandezas de fundo tipo-H (H, H_f, chidot, xidot)
marcadas como pequenas frente a k/a e as massas de interacao m^2 F
(que sao mantidas — e exatamente isso que gera a estrutura Yukawa).

Confrontos (P6.6): forma exata vs ansatz de 1 polo do Cap.18 §18.3;
numero de polos (Cap.7 §7.6 antecipa 2); alpha(a) derivado vs
alpha_0 r^2/(1+r^2) (Cap.18 §18.4); eta_slip vs Cap.18 §18.7.

Uso:  python 06_mu_alpha_QS.py    (saida em out/06_output.txt)
"""
import os
import time
import sympy as sp
from tdcp_pert_lib import (eps, t, k, a_s, b_s, xi_s, H_s, Hf_s,
                           Hd_s, Hfd_s, xid_s, chid_s, chidd_s,
                           Mg2, Mf2, m2, Meff2, b0, b1, b2, b3, b4,
                           Fb, Fp, Fpp, Ub, Up, Upp, rho_s,
                           cut, eps_part, lagrangian_GG,
                           interaction_lagrangian, chi_lagrangian,
                           scalar_metric_g, scalar_metric_f,
                           z_average, symbolize,
                           make_bg_functions, substitute_bg_functions,
                           background_onshell_rules, onshell, benchmark)

OUT = []
T0 = time.time()
drho = sp.Symbol('drho')          # perturbacao de densidade de materia
small = sp.Symbol('s_QS')         # contador de ordem QS


def say(*args):
    line = " ".join(str(x) for x in args)
    print(f"[{time.time()-T0:7.1f}s] " + line if line.strip() else line)
    OUT.append(line)


def main():
    say("=" * 70)
    say("DERIVACAO 6 — mu(k,a), eta_slip, Sigma exatos no limite QS")
    say("=" * 70)

    # ------------------------------------------------------------------
    # [1] mesma L2 do script 01 + fonte de materia
    # ------------------------------------------------------------------
    Phi_g = sp.Function('Phi_g')(t)
    Psi_g = sp.Function('Psi_g')(t)
    Phi_f = sp.Function('Phi_f')(t)
    Psi_f = sp.Function('Psi_f')(t)
    B_f = sp.Function('B_f')(t)
    E_f = sp.Function('E_f')(t)
    dchi = sp.Function('dchi')(t)
    funcs = [Phi_g, Psi_g, Phi_f, Psi_f, B_f, E_f, dchi]

    aF, bF, xiF, bg_rules = make_bg_functions()
    g = substitute_bg_functions(scalar_metric_g(Phi_g, Psi_g), aF, bF, xiF)
    f = substitute_bg_functions(scalar_metric_f(Phi_f, Psi_f, B_f, E_f),
                                aF, bF, xiF)

    say("[1] montando L2 (EH g, EH f, interacao HR, setor chi) ...")
    Lg = lagrangian_GG(g, Mg2)
    Lf = lagrangian_GG(f, Mf2)
    Lint = interaction_lagrangian(g, f, dchi=dchi)
    Lchi = chi_lagrangian(g, dchi=dchi)
    Ltot = cut(Lg + Lf + Lint + Lchi)
    L2 = z_average(eps_part(Ltot, 2))
    L2s, fields, vels = symbolize(L2, funcs, bg_rules)

    PhiG, PsiG, PhiF, PsiF, Bf_, Ef_, Dchi = fields

    # fonte de materia (mesmo fator 1/2 da media em z dos quadraticos)
    L2s = L2s - a_s**3 * drho * PhiG / 2
    say("[1] L2 com fonte:", len(L2s.args), "termos")

    # ------------------------------------------------------------------
    # [2] equacoes QS: dL/dX com todas as velocidades -> 0
    # ------------------------------------------------------------------
    say("[2] montando equacoes quase-estaticas ...")
    zero_vel = {v: 0 for v in vels}
    eqs = []
    for X in fields:
        E_X = sp.expand(sp.diff(L2s, X).subs(zero_vel))
        eqs.append(E_X)

    # ------------------------------------------------------------------
    # [3] on-shell + contagem de ordens QS
    # ------------------------------------------------------------------
    say("[3] impondo fundo on-shell e contagem QS ...")
    R = background_onshell_rules()

    def qs_reduce(e):
        e = onshell(e, R)
        e = e.subs(rho_s, 0)
        e = sp.expand(e.subs({H_s: small * H_s, Hf_s: small * Hf_s,
                              chid_s: small * chid_s, xid_s: small * xid_s}))
        # ordem dominante: s_QS^0
        return sp.expand(e.coeff(small, 0))

    eqs_qs = []
    for i, e in enumerate(eqs):
        eq = qs_reduce(e)
        eqs_qs.append(eq)
        say(f"   eq {fields[i]}: {len(sp.expand(eq).args) if eq != 0 else 0} termos QS")

    # ------------------------------------------------------------------
    # [4] resolver o sistema linear algebraico (LUsolve explicito)
    # ------------------------------------------------------------------
    say("[4] resolvendo sistema QS (algebra linear explicita) ...")
    unknowns = [PhiG, PsiG, PhiF, PsiF, Bf_, Ef_, Dchi]
    nontrivial = [e for e in eqs_qs if e != 0]
    say("   equacoes nao triviais:", len(nontrivial))
    A, rhs = sp.linear_eq_to_matrix(nontrivial, unknowns)
    A = A.applyfunc(lambda e: sp.cancel(sp.together(e)))
    rhs = rhs.applyfunc(lambda e: sp.cancel(sp.together(e)))

    # colunas identicamente nulas = variaveis que decaem do sistema QS
    # (tipicamente B_f, que so entra com derivadas temporais)
    keep_cols = []
    dropped = []
    for j, X in enumerate(unknowns):
        if all(sp.cancel(A[i, j]) == 0 for i in range(A.shape[0])):
            dropped.append(X)
        else:
            keep_cols.append(j)
    if dropped:
        say("   variaveis que decaem do sistema QS (postas a 0):", dropped)
    Ak = A[:, keep_cols]
    kept = [unknowns[j] for j in keep_cols]

    # remove equacoes identicamente nulas apos o corte
    keep_rows = [i for i in range(Ak.shape[0])
                 if any(sp.cancel(Ak[i, j]) != 0 for j in range(Ak.shape[1]))
                 or sp.cancel(rhs[i]) != 0]
    Ak = Ak[keep_rows, :]
    rk = rhs[keep_rows, :]
    say(f"   sistema final: {Ak.shape[0]} eqs x {Ak.shape[1]} incognitas")
    assert Ak.shape[0] == Ak.shape[1], "sistema QS nao quadrado apos corte"

    xsol = Ak.LUsolve(rk)
    xsol = xsol.applyfunc(lambda e: sp.cancel(sp.together(e)))
    S = dict(zip(kept, xsol))
    for X in dropped:
        S[X] = sp.Integer(0)
    say("   resolvido para:", [str(x) for x in kept])

    PhiG_sol = sp.cancel(sp.together(S[PhiG]))
    PsiG_sol = sp.cancel(sp.together(S[PsiG]))

    # ------------------------------------------------------------------
    # [5] mu, eta_slip, Sigma — calibrados pelo limite GR (m2 -> 0)
    # ------------------------------------------------------------------
    say("[5] montando mu(k,a), eta_slip(k,a), Sigma(k,a) ...")
    respPhi = sp.cancel(PhiG_sol / drho)
    respPsi = sp.cancel(PsiG_sol / drho)

    respPhi_GR = sp.limit(respPhi, m2, 0)
    respPsi_GR = sp.limit(respPsi, m2, 0)
    say("   resposta GR (m2->0):  k^2 Phi_g/drho =",
        sp.simplify(respPhi_GR * k**2))
    say("                          k^2 Psi_g/drho =",
        sp.simplify(respPsi_GR * k**2))
    gr_ok = sp.simplify(respPhi_GR - respPsi_GR) == 0
    say("   Phi = Psi no limite GR?", gr_ok)
    say("   Poisson GR: k^2 Psi = -a^2 drho/(2 Mg^2)?",
        sp.simplify(respPsi_GR * k**2 + a_s**2 / (2 * Mg2)) == 0)

    mu_exact = sp.cancel(sp.together(respPhi / respPhi_GR))
    eta_slip = sp.cancel(sp.together(PsiG_sol / PhiG_sol))
    Sigma = sp.cancel(sp.together((respPhi + respPsi) / (respPhi_GR + respPsi_GR)))

    say("")
    say("mu(k,a) exato [pot. temporal Phi_g, que governa o crescimento]:")
    say("  ", sp.simplify(mu_exact))
    say("")
    say("eta_slip(k,a) = Psi_g/Phi_g exato:")
    say("  ", sp.simplify(eta_slip))
    say("")
    say("Sigma(k,a) exato [lensing, (Phi+Psi)/2 normalizado]:")
    say("  ", sp.simplify(Sigma))

    # ------------------------------------------------------------------
    # [6] estrutura de polos em k^2 e confronto com o ansatz Yukawa
    # ------------------------------------------------------------------
    say("")
    say("[6] estrutura de polos em k^2 ...")
    K2sym = sp.Symbol('K2', positive=True)
    mu_k = sp.cancel(mu_exact.subs(k**2, K2sym))
    num, den = sp.fraction(sp.cancel(sp.together(mu_k)))
    deg_num = sp.degree(sp.Poly(num, K2sym))
    deg_den = sp.degree(sp.Poly(den, K2sym))
    say(f"   mu como funcao racional de k^2: grau num = {deg_num}, "
        f"grau den = {deg_den}")
    polos = sp.solve(sp.Eq(den, 0), K2sym)
    say("   numero de polos em k^2:", len(polos))
    say("   (1 polo => forma Yukawa do Cap.18 §18.3;")
    say("    2 polos => forma de dois mediadores do Cap.7 §7.6)")
    apart_mu = sp.apart(mu_k, K2sym, full=False)
    say("   fracoes parciais:")
    say("   ", apart_mu)

    # limite k -> infinito: mu_inf = 1 + alpha(a)
    mu_inf = sp.limit(mu_k, K2sym, sp.oo)
    alpha_derived = sp.simplify(mu_inf - 1)
    say("")
    say("   mu(k->oo) = 1 + alpha(a) com alpha(a) derivado =")
    say("   ", alpha_derived)
    rr = b_s / a_s
    alpha_cap18 = (Mf2 * rr**2 / Mg2) / (1 + Mf2 * rr**2 / Mg2)
    say("   comparacao Cap.18 §18.4 (alpha ~ eps^2/(1+eps^2), eps=Mf r/Mg):")
    say("   alpha_derivado - alpha_Cap18 =",
        sp.simplify(alpha_derived - alpha_cap18))

    # massas dos polos: m_i^2 = -a^2 * polo (Yukawa: k^2/a^2 + m^2)
    say("")
    for i, p in enumerate(polos):
        mp2 = sp.simplify(-p / a_s**2 * a_s**2)  # polo em k^2; massa^2 = -polo/a^2*a^2
        say(f"   polo {i+1}: k^2 = {sp.simplify(p)}")
        say(f"            => m^2(a) a^2 = {sp.simplify(-p)}")

    with open("out/06_matrices.txt", "w", encoding="utf-8") as fh:
        fh.write("mu(k,a) exato:\n" + sp.srepr(mu_exact) + "\n\nlatex:\n"
                 + sp.latex(sp.simplify(mu_exact)) + "\n\n")
        fh.write("eta_slip:\n" + sp.srepr(eta_slip) + "\n\nlatex:\n"
                 + sp.latex(sp.simplify(eta_slip)) + "\n\n")
        fh.write("Sigma:\n" + sp.srepr(Sigma) + "\n\nlatex:\n"
                 + sp.latex(sp.simplify(Sigma)) + "\n")

    # ------------------------------------------------------------------
    # [7] avaliacao numerica no benchmark
    # ------------------------------------------------------------------
    say("")
    say("[7] benchmark numerico (F1, r fora da raiz por -4%):")
    v = benchmark()
    v[Ub] = v[Ub] + v[rho_s]
    v[rho_s] = sp.Integer(0)
    say("   r =", sp.nsimplify(v[b_s] / v[a_s]), " xi =", float(v[xi_s]))
    say("   k/aH        mu          eta_slip     Sigma")
    for kv in (0.01, 0.1, 1, 10, 100, 1000):
        try:
            muv = complex(sp.N(mu_exact.subs(v).subs(k, kv))).real
            slv = complex(sp.N(eta_slip.subs(v).subs(k, kv))).real
            sgv = complex(sp.N(Sigma.subs(v).subs(k, kv))).real
            say(f"   {kv:8.2f}  {muv:+10.6f}  {slv:+10.6f}  {sgv:+10.6f}")
        except Exception as ex:
            say(f"   {kv:8.2f}  [!] {repr(ex)}")

    os.makedirs("out", exist_ok=True)
    with open("out/06_output.txt", "w", encoding="utf-8") as fh:
        fh.write("\n".join(OUT))
    say("\nconcluido. saida em out/06_output.txt; formas exatas em "
        "out/06_matrices.txt")


if __name__ == '__main__':
    main()
