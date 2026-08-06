# -*- coding: utf-8 -*-
"""
01_setor_escalar_K_Omega.py — Derivacao 1 (plano P1.1–P1.12).

Setor escalar completo da TDCP bimetrica em k finito, do zero:
  campos: Phi_g, Psi_g (gauge Newtoniano no setor g: B_g=E_g=0),
          Phi_f, Psi_f, B_f, E_f (setor f completo), dchi.
  acoes:  EH g + EH f (forma Gamma-Gamma, so 1as derivadas)
          + potencial HR F(chi) V(sqrt(g^-1 f)) via Sylvester
          + setor chi (cinetico + U + acoplamentos F', F'').
Escopo: vacuo + chi (sem perturbacoes de materia — plano A2; materia
entra na Derivacao 6). Materia de fundo posta a zero (rho_m = 0).

Pipeline:
  [1] L2 total, media em z, simbolizacao;
  [2] remocao por partes de velocidades lineares dos auxiliares;
  [3] eliminacao algebrica de Phi_g, Phi_f, B_f (3 constraints);
  [4] on-shell (aceleracoes g/f, Friedmann g/f, eq. de chi);
  [5] K4/C4/W4 -> posto de K4 (esperado 2, achado A1: so em k finito);
  [6] reducao a 2 modos via espaco nulo de K4;
  [7] K2, W2_eff finais + condicoes no-ghost/no-gradient/massa
      + confronto com as claims do Cap.15 §15.4/§15.5 e Cap.6.2.

Uso:  python 01_setor_escalar_K_Omega.py    (saida em out/01_output.txt;
      matrizes completas em out/01_matrices.txt)
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
                           z_average, symbolize, quadratic_matrices,
                           effective_mass_matrix, dt_background,
                           make_bg_functions, substitute_bg_functions,
                           background_onshell_rules, onshell,
                           eliminate_auxiliaries, benchmark)

OUT = []
T0 = time.time()


def say(*args):
    line = " ".join(str(x) for x in args)
    print(f"[{time.time()-T0:7.1f}s] " + line if line.strip() else line)
    OUT.append(line)


def dt_total(expr, fields, vels):
    """d/dt de uma expressao simbolizada: fundo + campos + velocidades."""
    out = dt_background(expr)
    for f, v in zip(fields, vels):
        d = sp.diff(expr, f)
        if d != 0:
            out += d * v
    # velocidades -> aceleracoes nao devem aparecer (checado pelo caller)
    return sp.expand(out)


def ipp_remove_velocity(L, X, fields, vels):
    """
    Remove Xdot de L por integracao por partes (L quadratica):
      A*Xdot com A = alpha_j q_j + beta*X  ->  -alphadot_j q_j X
                                               - alpha_j qdot_j X
                                               - (betadot/2) X^2
    Exige que A nao contenha nenhuma velocidade (senao X e dinamico).
    """
    Xdot = sp.Symbol(str(X) + 'dot')
    A = sp.expand(sp.diff(L, Xdot))
    if A == 0:
        return L
    for v in vels:
        if sp.expand(sp.diff(A, v)) != 0:
            raise RuntimeError(f"{X}: coeficiente de {Xdot} contem {v} — "
                               "variavel nao e auxiliar")
    beta = sp.expand(sp.diff(A, X))
    if sp.expand(sp.diff(beta, X)) != 0:
        raise RuntimeError("estrutura nao-quadratica inesperada")
    Aother = sp.expand(A - beta * X)
    repl = -(dt_background(beta) / 2) * X**2
    for f, v in zip(fields, vels):
        cf = sp.expand(sp.diff(Aother, f))
        if cf != 0:
            repl += -(dt_background(cf) * f + cf * v) * X
    # termo independente de campos em A (nao deve existir em L quadratica)
    A0 = Aother
    for f in fields:
        A0 = A0.subs(f, 0)
    if sp.expand(A0) != 0:
        raise RuntimeError(f"{X}: termo A0 de fundo em coeficiente de {Xdot}")
    return sp.expand(L - A * Xdot + repl)


def main():
    say("=" * 70)
    say("DERIVACAO 1 — setor escalar: K_ij e Omega_ij em k finito")
    say("=" * 70)

    # ------------------------------------------------------------------
    # [1] montagem de L2
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

    say("[1a] EH setor g (Gamma-Gamma) ...")
    Lg = lagrangian_GG(g, Mg2)
    say("[1b] EH setor f (Gamma-Gamma) ...")
    Lf = lagrangian_GG(f, Mf2)
    say("[1c] potencial HR (sqrt matricial de Sylvester + e_n) ...")
    Lint = interaction_lagrangian(g, f, dchi=dchi)
    say("[1d] setor chi ...")
    Lchi = chi_lagrangian(g, dchi=dchi)

    Ltot = cut(Lg + Lf + Lint + Lchi)
    L2 = z_average(eps_part(Ltot, 2))
    L2s, fields, vels = symbolize(L2, funcs, bg_rules)
    say(f"[1e] L2 simbolizada: {len(L2s.args)} termos")

    PhiG, PsiG, PhiF, PsiF, Bf_, Ef_, Dchi = fields

    # ------------------------------------------------------------------
    # [2] velocidades dos auxiliares (se lineares, remover por partes)
    # ------------------------------------------------------------------
    aux = [PhiG, PhiF, Bf_]
    for X in aux:
        Xdot = sp.Symbol(str(X) + 'dot')
        if L2s.has(Xdot):
            say(f"[2] removendo {Xdot} por integracao por partes ...")
            L2s = ipp_remove_velocity(L2s, X, fields, vels)
    say("[2] velocidades de Phi_g, Phi_f, B_f ausentes:",
        all(not L2s.has(sp.Symbol(str(X) + 'dot')) for X in aux))

    # ------------------------------------------------------------------
    # [3] eliminacao das 3 constraints
    # ------------------------------------------------------------------
    say("[3] resolvendo constraints de Phi_g, Phi_f, B_f ...")
    L2r, fields4, vels4, sol = eliminate_auxiliaries(L2s, fields, vels, aux)
    say("    campos dinamicos restantes:", fields4)

    # ------------------------------------------------------------------
    # [4] matrizes K4, C4, W4 e imposicao on-shell
    # ------------------------------------------------------------------
    say("[4] extraindo K4, C4, W4 ...")
    K4, C4, W4 = quadratic_matrices(L2r, fields4, vels4)
    W4eff, C4asym = effective_mass_matrix(W4, C4)

    say("[4b] impondo equacoes de fundo (on-shell, rho_m=0) ...")
    R = background_onshell_rules()

    def osz(e):
        return onshell(e, R).subs(rho_s, 0)

    K4 = K4.applyfunc(osz)
    W4eff = W4eff.applyfunc(osz)
    C4asym = C4asym.applyfunc(osz)

    # ------------------------------------------------------------------
    # [5] posto de K4 (numerico no benchmark, k generico)
    # ------------------------------------------------------------------
    v = benchmark()
    v[Ub] = v[Ub] + v[rho_s]     # remove materia do benchmark
    v[rho_s] = sp.Integer(0)
    # recomputa chiddot com a regra derivada da acao (sem materia nao muda)
    say("[5] benchmark: r =", sp.nsimplify(v[b_s] / v[a_s]),
        " xi =", float(v[xi_s]))

    ranks = {}
    for kval in (sp.Rational(1, 10), 1, 10):
        K4n = K4.subs(v).subs(k, kval)
        ranks[kval] = K4n.rank()
    say("    posto de K4 em k=0.1,1,10 (benchmark):", list(ranks.values()))
    K4n0 = K4.subs(v).subs(k, sp.Rational(1, 1000000))
    say("    posto de K4 em k=1e-6 (limite homogeneo, achado A1):",
        K4n0.rank())

    os.makedirs("out", exist_ok=True)
    with open("out/01_matrices.txt", "w", encoding="utf-8") as fh:
        fh.write("K4 (apos constraints, on-shell):\n")
        fh.write(sp.srepr(K4) + "\n\nlatex:\n" + sp.latex(K4) + "\n\n")
        fh.write("W4eff:\n" + sp.srepr(W4eff) + "\n\nlatex:\n"
                 + sp.latex(W4eff) + "\n\n")
        fh.write("C4 antissimetrica:\n" + sp.srepr(C4asym) + "\n")
    say("    matrizes 4x4 completas salvas em out/01_matrices.txt")

    # ------------------------------------------------------------------
    # [6] reducao ao subespaco dinamico (espaco nulo de K4)
    # ------------------------------------------------------------------
    say("[6] espaco nulo simbolico de K4 ...")
    try:
        K4s = K4.applyfunc(lambda e: sp.cancel(sp.together(e)))
        ns = K4s.nullspace()
        say("    dim(null K4) =", len(ns))
    except Exception as ex:
        ns = []
        say("    [!] nullspace simbolico falhou:", repr(ex))

    K2 = W2 = None
    if len(ns) == 2:
        # base: dois vetores unitarios com K-diagonal nao nula + nulos
        diag_ok = [i for i in range(4)
                   if sp.simplify(K4[i, i].subs(v).subs(k, 1)) != 0]
        cols = []
        for i in diag_ok:
            e_i = sp.zeros(4, 1)
            e_i[i] = 1
            cols.append(e_i)
            if len(cols) == 2:
                break
        S = sp.Matrix.hstack(cols[0], cols[1],
                             ns[0].applyfunc(sp.cancel),
                             ns[1].applyfunc(sp.cancel))
        detS = sp.simplify(S.det())
        say("    det(S) =", detS, " (deve ser != 0)")
        u = sp.symbols('u1 u2 u3 u4')
        udot = sp.symbols('u1dot u2dot u3dot u4dot')
        subs_q = {}
        for i, q in enumerate(fields4):
            expr_q = sum(S[i, j] * u[j] for j in range(4))
            expr_qd = sum(S[i, j] * udot[j]
                          + dt_background(S[i, j]) * u[j] for j in range(4))
            subs_q[q] = expr_q
            subs_q[sp.Symbol(str(q) + 'dot')] = expr_qd
        L2u = sp.expand(L2r.subs(subs_q))
        L2u = sp.expand(L2u.subs({Hd_s: R['Hd'], Hfd_s: R['Hfd'],
                                  chidd_s: R['chidd']}).subs(Ub, R['Ub'])
                        .subs(Hf_s**2, R['Hf2']).subs(rho_s, 0))

        ulist, udlist = list(u), list(udot)
        for X in (u[2], u[3]):
            Xd = sp.Symbol(str(X) + 'dot')
            if L2u.has(Xd):
                say(f"    removendo {Xd} por partes ...")
                L2u = ipp_remove_velocity(L2u, X, ulist, udlist)
        say("[6b] eliminando u3, u4 (agora algebricos) ...")
        L2f, fields2, vels2, _ = eliminate_auxiliaries(
            L2u, ulist, udlist, [u[2], u[3]])

        say("[7] matrizes finais 2x2 ...")
        K2, C2, W2 = quadratic_matrices(L2f, fields2, vels2)
        W2eff, C2a = effective_mass_matrix(W2, C2)
        K2 = K2.applyfunc(osz)
        W2eff = W2eff.applyfunc(osz)
        C2a = C2a.applyfunc(osz)
        W2 = W2eff

        with open("out/01_matrices.txt", "a", encoding="utf-8") as fh:
            fh.write("\n\nBase da reducao: q = S u, colunas de S:\n")
            fh.write(sp.srepr(S) + "\n\nlatex:\n" + sp.latex(S) + "\n")
            fh.write("\nK2:\n" + sp.srepr(K2) + "\n\nlatex:\n"
                     + sp.latex(K2) + "\n")
            fh.write("\nW2eff:\n" + sp.srepr(W2) + "\n\nlatex:\n"
                     + sp.latex(W2) + "\n")
            fh.write("\nC2 antissim:\n" + sp.srepr(C2a) + "\n")
        say("    K2/W2eff salvas em out/01_matrices.txt")
        say("    base fisica: u1 =", fields4[diag_ok[0]],
            ", u2 =", fields4[diag_ok[1]],
            " (com u3,u4 = direcoes nulas eliminadas)")
    else:
        say("    [!] reducao simbolica nao concluida; segue analise 4x4")

    # ------------------------------------------------------------------
    # [8] analise numerica: no-ghost, c_s^2, massas, claims
    # ------------------------------------------------------------------
    say("")
    say("=" * 70)
    say("ANALISE NUMERICA NO BENCHMARK (vacuo+chi, F1: beta3=0)")
    say("=" * 70)

    def numeric_report(delta, label):
        vb = benchmark(sp.Rational(delta[0], delta[1]))
        vb[Ub] = vb[Ub] + vb[rho_s]
        vb[rho_s] = sp.Integer(0)
        rv = float(vb[b_s] / vb[a_s])
        fac = float((b1 + 2 * b2 * (b_s / a_s)).subs(vb))
        say(f"\n--- {label}: r = {rv:.4f}, beta1+2*beta2*r = {fac:+.4f} ---")
        Ksrc = K2 if K2 is not None else K4
        Wsrc = W2 if K2 is not None else W4eff
        for kv in (sp.Rational(1, 10), 1, 10, 100):
            Kn = sp.N(Ksrc.subs(vb).subs(k, kv), 12)
            Wn = sp.N(Wsrc.subs(vb).subs(k, kv), 12)
            Kn = Kn.applyfunc(lambda x: complex(x).real)
            Wn = Wn.applyfunc(lambda x: complex(x).real)
            try:
                evK = sorted(complex(sp.N(e)).real for e in Kn.eigenvals())
                disp = (Kn.inv() * Wn)
                evD = sorted(complex(sp.N(e)).real
                             for e in disp.eigenvals())
                say(f"  k={float(kv):8.2f}: autovals K = "
                    f"[{evK[0]:+.3e}, {evK[-1]:+.3e}]  "
                    f"omega^2 = [{evD[0]:+.3e}, {evD[-1]:+.3e}]")
            except Exception as ex:
                say(f"  k={float(kv):8.2f}: [!] {repr(ex)}")

    # dois lados da raiz r_star = 5/4 (claim: sinal de beta1+2 beta2 r
    # decide ghost — P1.9/P1.12)
    numeric_report((1, 25), "benchmark A (r < r_star)")
    numeric_report((-1, 25), "benchmark B (r > r_star)")

    say("")
    say("Interpretacao (P1.9–P1.12): comparar o sinal dos autovalores de K")
    say("nos benchmarks A/B com o sinal de beta1+2*beta2*r; omega^2 em")
    say("k grande da c_s^2*k^2/a^2 (gradiente) e em k pequeno as massas.")
    say("Claims sob teste: Cap.15 §15.4 (no-ghost <-> beta1+2beta2 r>0),")
    say("Cap.15 §15.5 (m_S^2 ~ m^2 F (beta1+2beta2 r)), Cap.6.2 §6.4.")

    with open("out/01_output.txt", "w", encoding="utf-8") as fh:
        fh.write("\n".join(OUT))
    say("\nconcluido. saida em out/01_output.txt")


if __name__ == '__main__':
    main()
