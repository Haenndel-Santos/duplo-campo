# -*- coding: utf-8 -*-
"""
02_setor_tensorial_mT2.py — Derivacao 2 (plano P2.1–P2.6).

Deriva do zero a acao quadratica tensorial (TT) da TDCP bimetrica:
setores Einstein-Hilbert g e f (forma Gamma-Gamma, so 1as derivadas)
+ potencial HR F(chi) V(sqrt(g^-1 f)) expandido a O(h^2) via Sylvester.

Decide as tres discrepancias mapeadas no plano (E2.b/E2.c):
  (i)  cinetico de ell: M_f^2 r^2 (Cap.16 §16.2) vs M_f^2 r^3/xi (Anexo D §D.3);
  (ii) estrutura do termo de massa: exatamente (h-ell)^2 ou nao;
  (iii) coeficiente m_mix^2: depende de xi? reproduz beta1 r + 2 beta2 r^2?
Extrai m_T^2 (autovalor nao nulo de K^-1 M) e as velocidades c_g^2, c_f^2.

Uso:  python 02_setor_tensorial_mT2.py   (saida tambem em out/02_output.txt)
"""
import os
import sympy as sp
from tdcp_pert_lib import (eps, t, k, a_s, b_s, xi_s, H_s, Hf_s,
                           Hd_s, Hfd_s, xid_s, chid_s, chidd_s,
                           Mg2, Mf2, m2, Meff2, b0, b1, b2, b3, b4,
                           Fb, Fp, Ub, Up, rho_s, cut, eps_part, cutM,
                           lagrangian_GG, interaction_lagrangian,
                           tensor_metric_g, tensor_metric_f,
                           z_average, symbolize, quadratic_matrices,
                           effective_mass_matrix, make_bg_functions,
                           substitute_bg_functions, benchmark,
                           chi_lagrangian, background_onshell_rules, onshell)

OUT = []


def say(*args):
    line = " ".join(str(x) for x in args)
    print(line)
    OUT.append(line)


def main():
    say("=" * 70)
    say("DERIVACAO 2 — setor tensorial TT: acao quadratica e m_T^2")
    say("=" * 70)

    hx = sp.Function('h')(t)      # polarizacao cruzada do setor g
    lx = sp.Function('l')(t)      # idem setor f

    aF, bF, xiF, bg_rules = make_bg_functions()

    # ---- metricas TT perturbadas (com fundo como Function(t)) ----
    g = substitute_bg_functions(tensor_metric_g(hx), aF, bF, xiF)
    f = substitute_bg_functions(tensor_metric_f(lx), aF, bF, xiF)

    # ---- P2.3: Einstein-Hilbert dos dois setores (Gamma-Gamma) ----
    say("\n[1/5] expandindo EH do setor g ...")
    Lg = lagrangian_GG(g, Mg2)
    say("[2/5] expandindo EH do setor f ...")
    Lf = lagrangian_GG(f, Mf2)

    # ---- P2.1/P2.2: interacao HR a O(h^2) ----
    say("[3/5] expandindo potencial HR (sqrt matricial + e_n) ...")
    Lint = interaction_lagrangian(g, f)

    # setor chi (fundo): sqrt(-g) TT-perturbado multiplica chidot^2/2 - U,
    # entao contribui a O(h^2). Materia fria (p=0) NAO contribui: a
    # densidade de poeira escala com o volume proprio, sqrt(-g) rho_m =
    # N * rho_m0 = const, sem dependencia nas perturbacoes TT.
    Lchi = chi_lagrangian(g, dchi=None)

    Ltot = cut(Lg + Lf + Lint + Lchi)
    L2 = eps_part(Ltot, 2)
    L2 = z_average(L2)

    L2s, fields, vels = symbolize(L2, [hx, lx], bg_rules)
    L2s = sp.expand(L2s.subs({sp.Symbol('h'): sp.Symbol('h'),
                              sp.Symbol('l'): sp.Symbol('l')}))

    say("[4/5] extraindo matrizes K, C, W ...")
    K, C, W = quadratic_matrices(L2s, fields, vels)
    Weff, Casym = effective_mass_matrix(W, C)

    K = K.applyfunc(sp.simplify)
    Casym = Casym.applyfunc(sp.simplify)

    h, l = fields
    say("\n--- RESULTADO (por polarizacao; media em z inclui fator 1/2) ---")
    say("K (cinetica; L2 = 1/2 qdot K qdot + ... , q=(h,l)):")
    say(sp.pretty(K))
    say("\nC antissimetrica (giroscopica; deve ser 0):")
    say(sp.pretty(Casym))

    # ---------------------------------------------------------------
    # imposicao das equacoes de fundo (on-shell)
    # ---------------------------------------------------------------
    say("\n[4b/5] derivando eqs. de aceleracao do fundo e impondo on-shell ...")
    R = background_onshell_rules()
    say("   Hdot  (eq. aceleracao g) =", R['Hd'])
    say("   Hfdot (eq. aceleracao f) =", R['Hfd'])
    Weff = Weff.applyfunc(lambda e: onshell(e, R))

    say("\nW_eff on-shell (massa+gradiente; L2 contem -1/2 q W_eff q):")
    say(sp.pretty(Weff))

    # ---------------------------------------------------------------
    # separacao gradiente (k^2) vs massa (k-independente)
    # ---------------------------------------------------------------
    G = Weff.applyfunc(lambda e: sp.expand(e).coeff(k, 2))
    M = Weff.applyfunc(lambda e: sp.expand(e).subs(k, 0))
    resid = sp.simplify(Weff - k**2 * G - M)
    say("\nW_eff e polinomial em k^2 (residuo 0)?", resid == sp.zeros(2, 2))

    say("\nG (coef. de k^2):")
    say(sp.pretty(G.applyfunc(sp.simplify)))
    say("\nM (parte de massa, on-shell):")
    say(sp.pretty(M.applyfunc(sp.simplify)))

    # ---------------------------------------------------------------
    # (i) confronto do cinetico de ell: r^2 (Cap.16) vs r^3/xi (Anexo D)
    # ---------------------------------------------------------------
    say("\n--- (i) CINETICO DO SETOR f ---")
    ratio = sp.simplify(K[1, 1] / K[0, 0])
    say("K_ll / K_hh =", sp.simplify(ratio), "  [com r=b/a]")
    r_expr = b_s / a_s
    cap16 = sp.simplify(ratio - (Mf2 / Mg2) * r_expr**2)
    anexoD = sp.simplify(ratio - (Mf2 / Mg2) * r_expr**3 / xi_s)
    say("igual a (Mf2/Mg2) r^2      (Cap.16 §16.2)?", cap16 == 0)
    say("igual a (Mf2/Mg2) r^3/xi   (Anexo D §D.3)?", anexoD == 0)

    # velocidades de propagacao (normalizadas a k^2/a^2)
    cg2 = sp.simplify(a_s**2 * G[0, 0] / K[0, 0])
    cf2 = sp.simplify(a_s**2 * G[1, 1] / K[1, 1])
    say("\nc_g^2 =", cg2, "   c_f^2 =", cf2, "  [normalizados a k^2/a^2]")
    say("(Anexo D preve c_f^2 = xi^2 a^2/b^2 = xi^2/r^2:",
        sp.simplify(cf2 - xi_s**2 * a_s**2 / b_s**2) == 0, ")")

    # ---------------------------------------------------------------
    # (ii) estrutura do termo de massa: proporcional a (h-l)^2 ?
    # ---------------------------------------------------------------
    say("\n--- (ii) ESTRUTURA DO TERMO DE MASSA ---")
    c_hh, c_hl, c_ll = M[0, 0], M[0, 1], M[1, 1]
    say("M_hh =", sp.simplify(c_hh))
    say("M_hl =", sp.simplify(c_hl))
    say("M_ll =", sp.simplify(c_ll))
    is_diff2 = (sp.simplify(c_hh + c_hl) == 0) and (sp.simplify(c_ll + c_hl) == 0)
    say("proporcional exatamente a (h-l)^2 ?", is_diff2)

    # ---------------------------------------------------------------
    # (iii) coeficiente de mistura vs claim do Cap.16 §16.2
    # ---------------------------------------------------------------
    say("\n--- (iii) COEFICIENTE DE MISTURA ---")
    # convencao do Cap.16: L contem -(1/2) m_mix^2 (h-l)^2 * a^3 * (1/2 da media z)
    # portanto m_mix^2 = M_hh / (a^3/2)  se a estrutura for (h-l)^2
    mmix2 = sp.simplify(c_hh / (a_s**3 / 2))
    say("m_mix^2 (derivado) =", mmix2)
    claim = m2 * Meff2 * Fb * (b1 * r_expr + 2 * b2 * r_expr**2)
    say("claim Cap.16 §16.2:  m2 Meff2 F (beta1 r + 2 beta2 r^2)")
    say("m_mix^2derivado - claim =", sp.simplify(mmix2 - claim))
    say("depende de xi?", xi_s in mmix2.free_symbols)
    say("depende de beta3/beta4?", (b3 in mmix2.free_symbols) or
        (b4 in mmix2.free_symbols))
    # limites uteis
    say("no limite xi -> r:  m_mix^2 - claim =",
        sp.simplify(mmix2.subs(xi_s, r_expr * 1) - claim).subs(b_s, r_expr * a_s))
    say("no limite xi -> 1:  m_mix^2 - claim =",
        sp.simplify(mmix2.subs(xi_s, 1) - claim))

    # ---------------------------------------------------------------
    # P2.4/P2.5: massas fisicas = autovalores de K^-1 M
    # ---------------------------------------------------------------
    say("\n--- MASSAS FISICAS (autovalores de K^-1 M) ---")
    KiM = sp.simplify(K.inv() * M)
    evs = KiM.eigenvals()
    say("autovalores (multiplicidade):")
    mT2 = None
    for ev, mult in evs.items():
        ev_s = sp.simplify(ev)
        say("  ", ev_s, " x", mult)
        if ev_s != 0:
            mT2 = ev_s
    if mT2 is None:
        say("  [!] nenhum autovalor nao nulo — massa tensorial identicamente 0?")
    else:
        say("\nm_T^2 (exato) =", mT2)
        say("\nm_T^2 em LaTeX:")
        say(sp.latex(mT2))
        claim164 = m2 * Fb * (Meff2 / Mg2) * (b1 * r_expr + 2 * b2 * r_expr**2)
        say("\nclaim Cap.16 §16.4: m2 F (Meff2/Mg2)(beta1 r + 2 beta2 r^2)")
        say("m_T^2 - claim =", sp.simplify(mT2 - claim164))
        # o fator de escala de Planck correto:
        say("\nfator de escala: m_T^2 / [m2 Meff2 F * (coef. beta)] =")
        coef_beta = sp.simplify(mmix2 / (m2 * Meff2 * Fb))
        say(sp.simplify(mT2 / (m2 * Meff2 * Fb * coef_beta)))

    # tem modo massless?
    say("\ndet(M) =", sp.simplify(M.det()), " (0 => existe modo massless)")

    # ---------------------------------------------------------------
    # avaliacao numerica no benchmark
    # ---------------------------------------------------------------
    say("\n--- BENCHMARK NUMERICO (fundo consistente, r ligeiramente fora da raiz) ---")
    v = benchmark()
    say("r =", sp.nsimplify(v[b_s] / v[a_s]), " xi =", float(v[xi_s]),
        " H =", float(v[H_s]), " H_f =", float(v[Hf_s]))
    Kn = K.subs(v)
    Mn = M.subs(v)
    say("K numerica =", [float(sp.N(Kn[i, i])) for i in range(2)],
        " (off-diag:", float(sp.N(Kn[0, 1])), ")")
    KiMn = (Kn.inv() * Mn)
    evn = [complex(sp.N(ev)) for ev in KiMn.eigenvals()]
    say("autovalores de K^-1 M no benchmark:", evn)
    if mT2 is not None:
        say("m_T^2 benchmark =", float(sp.N(mT2.subs(v))))
        say("2H^2 =", float(sp.N(2 * v[H_s]**2)),
            "  -> Higuchi satisfeito?", bool(sp.N(mT2.subs(v)) >= sp.N(2 * v[H_s]**2)))

    say("\n[5/5] concluido.")
    os.makedirs("out", exist_ok=True)
    with open("out/02_output.txt", "w", encoding="utf-8") as fh:
        fh.write("\n".join(OUT))
    say("saida salva em out/02_output.txt")


if __name__ == '__main__':
    main()
