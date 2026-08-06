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

REDUCAO POR COMPLEMENTO DE SCHUR (matricial): a Lagrangiana quadratica
e representada pelos blocos (K, C, W) 7x7,
    L2 = 1/2 qdot^T K qdot + qdot^T C q - 1/2 q^T W q,
e cada eliminacao (auxiliares Phi_g, Phi_f, B_f; depois as direcoes
nulas de K) e feita por algebra de blocos com cancel() — nunca por
substituicao em expressao expandida (que explode em memoria).

Uso:  python 01_setor_escalar_K_Omega.py   (saida em out/01_output.txt;
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
                           make_bg_functions, substitute_bg_functions,
                           background_onshell_rules, onshell,
                           schur_eliminate, transform_basis,
                           matrix_ipp_row, dt_background, benchmark)

OUT = []
T0 = time.time()


def say(*args):
    line = " ".join(str(x) for x in args)
    print(f"[{time.time()-T0:7.1f}s] " + line if line.strip() else line)
    OUT.append(line)


def cancelM(M):
    return M.applyfunc(lambda e: sp.cancel(sp.together(e)))


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
    names = [str(x) for x in fields]

    # ------------------------------------------------------------------
    # [2] blocos K7, C7, W7
    # ------------------------------------------------------------------
    say("[2] extraindo blocos K7, C7, W7 ...")
    K7, C7, W7 = quadratic_matrices(L2s, fields, vels)
    K7, C7, W7 = cancelM(K7), cancelM(C7), cancelM(W7)

    idx_aux = [names.index('Phi_g'), names.index('Phi_f'),
               names.index('B_f')]
    # linhas K e C dos auxiliares devem ser nulas (sem velocidades);
    # se C tiver linha nao nula, remover por partes matricialmente
    for i in idx_aux:
        row_nonzero = any(sp.cancel(C7[i, j]) != 0 for j in range(7))
        if row_nonzero:
            say(f"   removendo linha C de {names[i]} por partes ...")
            K7, C7, W7 = matrix_ipp_row(K7, C7, W7, i)
    say("   linhas K dos auxiliares nulas:",
        all(sp.cancel(K7[i, j]) == 0 for i in idx_aux for j in range(7)))

    # ------------------------------------------------------------------
    # [3] Schur: elimina Phi_g, Phi_f, B_f
    # ------------------------------------------------------------------
    say("[3] complemento de Schur (3 constraints) ...")
    K4, C4, W4, idx_dyn = schur_eliminate(K7, C7, W7, idx_aux)
    dyn_names = [names[i] for i in idx_dyn]
    say("   campos dinamicos:", dyn_names)

    # ------------------------------------------------------------------
    # [4] on-shell
    # ------------------------------------------------------------------
    say("[4] impondo fundo on-shell (rho_m = 0) ...")
    R = background_onshell_rules()

    def osz(e):
        e = sp.expand(e)
        e = e.subs({Hd_s: R['Hd'], Hfd_s: R['Hfd'], chidd_s: R['chidd']})
        e = sp.expand(e).subs(Ub, R['Ub'])
        e = sp.expand(e).subs(Hf_s**2, R['Hf2'])
        return sp.cancel(sp.together(e.subs(rho_s, 0)))

    K4 = K4.applyfunc(osz)
    C4 = C4.applyfunc(osz)
    W4 = W4.applyfunc(osz)

    # ------------------------------------------------------------------
    # [5] posto de K4 e espaco nulo
    # ------------------------------------------------------------------
    v = benchmark()
    v[Ub] = v[Ub] + v[rho_s]
    v[rho_s] = sp.Integer(0)
    say("[5] benchmark: r =", sp.nsimplify(v[b_s] / v[a_s]),
        " xi =", float(v[xi_s]))
    for kval in (sp.Rational(1, 1000000), sp.Rational(1, 10), 1, 10):
        K4n = K4.subs(v).subs(k, kval)
        say(f"   posto de K4 em k={float(kval):g}: {K4n.rank()}")

    os.makedirs("out", exist_ok=True)
    with open("out/01_matrices.txt", "w", encoding="utf-8") as fh:
        fh.write("Campos dinamicos (ordem): " + str(dyn_names) + "\n\n")
        fh.write("K4 (apos Schur das constraints, on-shell):\n")
        fh.write(sp.srepr(K4) + "\n\nlatex:\n" + sp.latex(K4) + "\n\n")
        fh.write("C4:\n" + sp.srepr(C4) + "\n\nlatex:\n" + sp.latex(C4) + "\n\n")
        fh.write("W4:\n" + sp.srepr(W4) + "\n\nlatex:\n" + sp.latex(W4) + "\n")
    say("   matrizes 4x4 salvas em out/01_matrices.txt")

    say("[6] espaco nulo simbolico de K4 ...")
    ns = K4.nullspace()
    say("   dim(null K4) =", len(ns))

    K2 = W2eff = C2 = None
    if len(ns) == 2:
        ns = [n.applyfunc(lambda e: sp.cancel(sp.together(e))) for n in ns]
        # normaliza cada vetor nulo pelo primeiro elemento nao nulo
        for n_ in ns:
            piv = next(x for x in n_ if sp.cancel(x) != 0)
            for i in range(4):
                n_[i] = sp.cancel(n_[i] / piv)
        # escolhe 2 direcoes complementares (colunas unitarias)
        chosen = []
        for i in range(4):
            e_i = sp.zeros(4, 1)
            e_i[i] = 1
            Strial = sp.Matrix.hstack(*(chosen + [e_i] + ns))
            if Strial.shape[1] == 4:
                if sp.cancel(Strial.det().subs(v).subs(k, 1)) != 0:
                    chosen.append(e_i)
            elif len(chosen) < 2:
                chosen.append(e_i)
                continue
            if len(chosen) == 2:
                break
        S = sp.Matrix.hstack(chosen[0], chosen[1], ns[0], ns[1])
        say("   base escolhida: u1 =", dyn_names[list(chosen[0]).index(1)],
            ", u2 =", dyn_names[list(chosen[1]).index(1)],
            ", u3/u4 = direcoes nulas de K4")
        detSn = sp.cancel(S.det().subs(v).subs(k, 1))
        say("   det(S) no benchmark:", detSn, " (!= 0 ok)")

        say("[6b] mudanca de base (matricial) ...")
        Ku, Cu, Wu = transform_basis(K4, C4, W4, S)
        Ku = Ku.applyfunc(osz)
        Cu = Cu.applyfunc(osz)
        Wu = Wu.applyfunc(osz)

        # linhas 3,4 de Ku devem ser nulas por construcao
        zero_ok = all(sp.cancel(Ku[i, j]) == 0
                      for i in (2, 3) for j in range(4))
        say("   linhas 3,4 de K_u nulas:", zero_ok)

        for i in (2, 3):
            if any(sp.cancel(Cu[i, j]) != 0 for j in range(4)):
                say(f"   removendo linha C de u{i+1} por partes ...")
                Ku, Cu, Wu = matrix_ipp_row(Ku, Cu, Wu, i)
                Cu = Cu.applyfunc(osz)
                Wu = Wu.applyfunc(osz)

        say("[6c] Schur final (elimina u3, u4) ...")
        K2, C2, W2, _ = schur_eliminate(Ku, Cu, Wu, [2, 3])
        K2 = K2.applyfunc(osz)
        C2 = C2.applyfunc(osz)
        W2 = W2.applyfunc(osz)

        # absorve a parte simetrica de C2 na massa: W_eff = W + d/dt C_sym
        Csym = (C2 + C2.T) / 2
        W2eff = cancelM(W2 + Csym.applyfunc(
            lambda e: dt_background(e)).applyfunc(osz))
        C2a = cancelM((C2 - C2.T) / 2)

        with open("out/01_matrices.txt", "a", encoding="utf-8") as fh:
            fh.write("\n\nBase: q = S u; S:\n" + sp.srepr(S) + "\n\nlatex:\n"
                     + sp.latex(S) + "\n")
            fh.write("\nK2:\n" + sp.srepr(K2) + "\n\nlatex:\n"
                     + sp.latex(K2) + "\n")
            fh.write("\nW2eff:\n" + sp.srepr(W2eff) + "\n\nlatex:\n"
                     + sp.latex(W2eff) + "\n")
            fh.write("\nC2 antissim:\n" + sp.srepr(C2a) + "\n")
        say("   K2/W2eff salvas em out/01_matrices.txt")
    else:
        say("   [!] dim(null) != 2 — analise segue com as matrizes 4x4")

    # ------------------------------------------------------------------
    # [7] analise numerica: no-ghost, c_s^2, massas, claims
    # ------------------------------------------------------------------
    say("")
    say("=" * 70)
    say("ANALISE NUMERICA (vacuo+chi, F1: beta3=0)")
    say("=" * 70)

    def numeric_report(delta, label):
        vb = benchmark(sp.Rational(delta[0], delta[1]))
        vb[Ub] = vb[Ub] + vb[rho_s]
        vb[rho_s] = sp.Integer(0)
        rv = float(vb[b_s] / vb[a_s])
        fac = float((b1 + 2 * b2 * (b_s / a_s)).subs(vb))
        say(f"\n--- {label}: r = {rv:.4f}, beta1+2*beta2*r = {fac:+.4f} ---")
        Ksrc = K2 if K2 is not None else K4
        Wsrc = W2eff if K2 is not None else W4
        say("  k        autovals K            omega^2 (K^-1 W)")
        for kv in (sp.Rational(1, 10), 1, 10, 100):
            try:
                Kn = Ksrc.subs(vb).subs(k, kv)
                Wn = Wsrc.subs(vb).subs(k, kv)
                Kn = sp.Matrix(Kn.shape[0], Kn.shape[1],
                               lambda i, j: sp.nsimplify(sp.N(Kn[i, j], 30)))
                Wn = sp.Matrix(Wn.shape[0], Wn.shape[1],
                               lambda i, j: sp.nsimplify(sp.N(Wn[i, j], 30)))
                evK = sorted(complex(sp.N(e)).real for e in Kn.eigenvals())
                evD = sorted(complex(sp.N(e)).real
                             for e in (Kn.inv() * Wn).eigenvals())
                say(f"  {float(kv):7.2f}  [{evK[0]:+.4e}, {evK[-1]:+.4e}]"
                    f"  [{evD[0]:+.4e}, {evD[-1]:+.4e}]")
            except Exception as ex:
                say(f"  {float(kv):7.2f}  [!] {repr(ex)[:80]}")

    numeric_report((1, 25), "benchmark A (r < r_star)")
    numeric_report((-1, 25), "benchmark B (r > r_star)")

    say("")
    say("Leitura (P1.9–P1.12):")
    say("- no-ghost: sinais dos autovalores de K nos benchmarks A/B vs")
    say("  o sinal de beta1+2*beta2*r (claim Cap.15 §15.4);")
    say("- gradiente: omega^2 ~ c_s^2 k^2/a^2 em k grande;")
    say("- massas: omega^2 em k pequeno; comparar o modo relativo com")
    say("  m^2 F (beta1+2*beta2*r) (claim Cap.15 §15.5);")
    say("- contagem: posto de K4 (Cap.6.2 §6.4 diz 3 modos; Anexo C, 2).")

    with open("out/01_output.txt", "w", encoding="utf-8") as fh:
        fh.write("\n".join(OUT))
    say("\nconcluido. saida em out/01_output.txt")


if __name__ == '__main__':
    main()
