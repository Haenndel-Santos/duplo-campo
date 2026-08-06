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

MODOS DE EXECUCAO:
  SEMI_NUMERIC = True  (padrao): o fundo do benchmark (consistente com
     as Friedmann g/f e a eq. de chi; Hdot=Hfdot=xidot=0, quase-de
     Sitter) e substituido logo apos a montagem de L2; k fica simbolico.
     A reducao (Schur) roda em segundos e decide todas as claims de
     sinal/posto/massa nos DOIS benchmarks (r < r_star e r > r_star).
  SEMI_NUMERIC = False: via totalmente simbolica (rodada longa; use so
     depois de validar o modo padrao — pode levar horas/muita RAM).

Reducao por complemento de Schur em blocos (K, C, W):
    L2 = 1/2 qdot^T K qdot + qdot^T C q - 1/2 q^T W q.

Uso:  python 01_setor_escalar_K_Omega.py   (saida em out/01_output.txt;
      matrizes em out/01_matrices.txt)
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
                           background_onshell_rules,
                           schur_eliminate, transform_basis,
                           matrix_ipp_row, dt_background, benchmark)

SEMI_NUMERIC = True

OUT = []
T0 = time.time()


def say(*args):
    line = " ".join(str(x) for x in args)
    print(f"[{time.time()-T0:7.1f}s] " + line if line.strip() else line)
    OUT.append(line)


def cancelM(M):
    return M.applyfunc(lambda e: sp.cancel(sp.together(e)))


def build_L2():
    """Monta a L2 simbolica completa (unica parte pesada)."""
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
    say("[1c] potencial HR (sqrt de Sylvester + e_n) ...")
    Lint = interaction_lagrangian(g, f, dchi=dchi)
    say("[1d] setor chi ...")
    Lchi = chi_lagrangian(g, dchi=dchi)

    Ltot = cut(Lg + Lf + Lint + Lchi)
    say("[1e] extraindo ordem eps^2 e mediando em z ...")
    L2 = z_average(eps_part(Ltot, 2))
    L2s, fields, vels = symbolize(L2, funcs, bg_rules)
    say(f"     L2 simbolizada: {len(L2s.args)} termos")
    return L2s, fields, vels


def onshell_numeric_values(delta):
    """Benchmark consistente, sem materia, com aceleracoes nulas."""
    v = benchmark(sp.Rational(delta[0], delta[1]))
    v[Ub] = v[Ub] + v[rho_s]
    v[rho_s] = sp.Integer(0)
    # chiddot consistente com a eq. derivada da acao (sinal -F'V)
    return v


def reduce_pipeline(L2in, fields, vels, label, numeric_subs=None):
    """
    Reducao completa: blocos 7x7 -> Schur(constraints) -> espaco nulo
    -> Schur final -> (K2, C2a, W2eff). numeric_subs != None ativa o
    modo semi-numerico (fundo substituido, k simbolico).
    """
    names = [str(x) for x in fields]
    L2w = L2in
    if numeric_subs is not None:
        L2w = sp.expand(L2w.subs(numeric_subs))

    say(f"[{label}] blocos K7, C7, W7 ...")
    K7, C7, W7 = quadratic_matrices(L2w, fields, vels)
    K7, C7, W7 = cancelM(K7), cancelM(C7), cancelM(W7)

    idx_aux = [names.index('Phi_g'), names.index('Phi_f'), names.index('B_f')]
    for i in idx_aux:
        if any(sp.cancel(C7[i, j]) != 0 for j in range(7)):
            say(f"   removendo linha C de {names[i]} por partes ...")
            K7, C7, W7 = matrix_ipp_row(K7, C7, W7, i)

    say(f"[{label}] Schur (3 constraints) ...")
    K4, C4, W4, idx_dyn = schur_eliminate(K7, C7, W7, idx_aux, verbose=False)
    dyn_names = [names[i] for i in idx_dyn]
    say("   campos dinamicos:", dyn_names)

    say(f"[{label}] posto de K4 (k=1e-6, 0.1, 1, 10):")
    postos = []
    for kval in (sp.Rational(1, 1000000), sp.Rational(1, 10), 1, 10):
        postos.append(K4.subs(k, kval).rank() if numeric_subs is not None
                      else None)
    say("   ", postos)

    say(f"[{label}] espaco nulo de K4 ...")
    ns = K4.nullspace()
    say("   dim(null K4) =", len(ns))
    if len(ns) != 2:
        say("   [!] dim != 2 — retorno com 4x4")
        return dict(K=K4, C=C4, W=W4, dyn=dyn_names, reduced=False)

    ns = [n.applyfunc(lambda e: sp.cancel(sp.together(e))) for n in ns]
    for n_ in ns:
        piv = next(x for x in n_ if sp.cancel(x) != 0)
        for i in range(4):
            n_[i] = sp.cancel(n_[i] / piv)

    chosen, chosen_idx = [], []
    for i in range(4):
        e_i = sp.zeros(4, 1)
        e_i[i] = 1
        Strial = sp.Matrix.hstack(*(chosen + [e_i] + ns))
        if Strial.shape[1] == 4:
            d = Strial.det()
            d = d.subs(k, 1) if numeric_subs is not None else d.subs(k, 1)
            if sp.cancel(d) != 0:
                chosen.append(e_i)
                chosen_idx.append(i)
        else:
            chosen.append(e_i)
            chosen_idx.append(i)
        if len(chosen) == 2:
            break
    S = sp.Matrix.hstack(chosen[0], chosen[1], ns[0], ns[1])
    say("   base: u1 =", dyn_names[chosen_idx[0]],
        ", u2 =", dyn_names[chosen_idx[1]], ", u3/u4 = direcoes nulas")

    Ku, Cu, Wu = transform_basis(K4, C4, W4, S)
    for i in (2, 3):
        if any(sp.cancel(Cu[i, j]) != 0 for j in range(4)):
            Ku, Cu, Wu = matrix_ipp_row(Ku, Cu, Wu, i)

    say(f"[{label}] Schur final (u3, u4) ...")
    K2, C2, W2, _ = schur_eliminate(Ku, Cu, Wu, [2, 3], verbose=False)
    Csym = (C2 + C2.T) / 2
    W2eff = cancelM(W2 + Csym.applyfunc(lambda e: dt_background(e)))
    C2a = cancelM((C2 - C2.T) / 2)
    return dict(K=cancelM(K2), C=C2a, W=W2eff, dyn=dyn_names,
                base=(dyn_names[chosen_idx[0]], dyn_names[chosen_idx[1]]),
                S=S, reduced=True)


def analyze(res, vb, label):
    """Autovalores de K e de K^-1 W sobre a grade de k + claims."""
    K2, W2 = res['K'], res['W']
    rv = float(vb[b_s] / vb[a_s])
    fac = float((b1 + 2 * b2 * (b_s / a_s)).subs(vb))
    claim_mS2 = float((m2 * Fb).subs(vb)) * fac
    say(f"\n--- {label}: r = {rv:.4f}, beta1+2*beta2*r = {fac:+.4f} ---")
    say(f"    claim Cap.15 §15.5: m_S^2 ~ m2*F*(beta1+2b2r) = {claim_mS2:+.4f}")
    say("  k        autovals K              omega^2 = eig(K^-1 W)")
    grades = {}
    for kv in (sp.Rational(1, 10), 1, 10, 100):
        Kn = K2.subs(k, kv)
        Wn = W2.subs(k, kv)
        evK = sorted(complex(sp.N(e)).real for e in Kn.eigenvals())
        evD = sorted(complex(sp.N(e)).real for e in (Kn.inv() * Wn).eigenvals())
        grades[float(kv)] = (evK, evD)
        say(f"  {float(kv):7.2f}  [{evK[0]:+.4e}, {evK[-1]:+.4e}]"
            f"  [{evD[0]:+.4e}, {evD[-1]:+.4e}]")
    # c_s^2 e massas via fit omega^2 = c^2 k^2/a^2 + m^2 nos 2 maiores k
    a2 = float(vb[a_s]**2)
    try:
        k1, k2v = 10.0, 100.0
        for idx, nome in ((0, "modo 1 (menor omega^2)"),
                          (1, "modo 2 (maior omega^2)")):
            w1 = grades[k1][1][idx]
            w2 = grades[k2v][1][idx]
            c2 = (w2 - w1) / ((k2v**2 - k1**2) / a2)
            mm2 = w1 - c2 * k1**2 / a2
            say(f"    {nome}: c_s^2 = {c2:+.5f},  m^2 = {mm2:+.5f}"
                f"   [claim m_S^2 = {claim_mS2:+.5f}]")
    except Exception as ex:
        say("    [!] fit c_s^2/m^2 falhou:", repr(ex)[:70])
    return grades


def main():
    say("=" * 70)
    say("DERIVACAO 1 — setor escalar: K_ij e Omega_ij em k finito")
    say("    modo:", "SEMI-NUMERICO (fundo benchmark, k simbolico)"
        if SEMI_NUMERIC else "SIMBOLICO COMPLETO")
    say("=" * 70)

    L2s, fields, vels = build_L2()

    os.makedirs("out", exist_ok=True)
    if SEMI_NUMERIC:
        resultados = {}
        for delta, label in (((1, 25), "A (r < r_star)"),
                             ((-1, 25), "B (r > r_star)")):
            vb = onshell_numeric_values(delta)
            say("")
            res = reduce_pipeline(L2s, fields, vels, f"bench {label}",
                                  numeric_subs=vb)
            resultados[label] = (res, vb)
            with open("out/01_matrices.txt",
                      "a" if resultados else "w", encoding="utf-8") as fh:
                fh.write(f"\n\n===== benchmark {label} =====\n")
                fh.write("K (dim %dx%d):\n" % res['K'].shape)
                fh.write(sp.latex(res['K'].applyfunc(
                    lambda e: sp.nsimplify(e, rational=True))) + "\n")
                fh.write("W_eff:\n" + sp.latex(res['W'].applyfunc(
                    lambda e: sp.nsimplify(e, rational=True))) + "\n")

        say("")
        say("=" * 70)
        say("ANALISE (vacuo+chi, F1: beta3=0; fundo quase-de Sitter)")
        say("=" * 70)
        for label, (res, vb) in resultados.items():
            if res['reduced']:
                say(f"\nbase fisica reduzida de {label}: u1 = {res['base'][0]}, "
                    f"u2 = {res['base'][1]}")
            analyze(res, vb, "benchmark " + label)

        say("")
        say("Leitura (P1.9–P1.12):")
        say("- no-ghost: sinais de eig(K) em A (fator>0) vs B (fator<0)")
        say("  testam a claim do Cap.15 §15.4;")
        say("- m^2 do modo relativo vs claim m2*F*(beta1+2b2r) testa §15.5;")
        say("- posto de K4 = numero de modos dinamicos (Cap.6.2 §6.4 diz 3;")
        say("  Anexo C §C.3 diz 2);")
        say("- caveat: Hdot=Hfdot=xidot=0 no benchmark (quase-de Sitter).")
    else:
        res = reduce_pipeline(L2s, fields, vels, "simbolico",
                              numeric_subs=None)
        with open("out/01_matrices.txt", "w", encoding="utf-8") as fh:
            for nome in ('K', 'W', 'C'):
                fh.write(f"{nome}:\n" + sp.srepr(res[nome])
                         + "\n\nlatex:\n" + sp.latex(res[nome]) + "\n\n")
        say("matrizes simbolicas salvas em out/01_matrices.txt")

    with open("out/01_output.txt", "w", encoding="utf-8") as fh:
        fh.write("\n".join(OUT))
    say("\nconcluido. saida em out/01_output.txt")


if __name__ == '__main__':
    main()
