# -*- coding: utf-8 -*-
"""
06_mu_alpha_QS.py — Derivacao 6 (plano P6.1–P6.6), v3.

v4: a truncagem QS por marcacao de simbolos (v3) era inconsistente —
descartava chidot/H mas mantinha U', U'' e rho_int (que a Friedmann
amarra a H^2), gerando estrutura espuria em k pequeno ate no limite
m2->0. Agora a resposta e ESTATICA EXATA (qdot=0, sem hierarquia
assumida): mu(k) = resposta(m2)/resposta(m2->0), em que as correcoes
de fundo cancelam na razao e o regime quase-estatico emerge sozinho em
k >> H. Calibracao GR verificada em k grande (Poisson -> -1/2,
Phi/Psi -> 1).

v3 (historico): a calibracao GR da v2 reprovou (Phi != Psi e Poisson errado no
limite m2->0) — mesma causa-raiz do episodio v2 da Derivacao 1: fixar
o gauge Newtoniano NA ACAO perde as equacoes de vinculo de B_g e E_g,
e a equacao de E_g (ij sem traco) e exatamente a que impoe Phi=Psi em
GR. Agora a acao e construida com os 9 campos SEM fixar gauge, as 9
equacoes QS sao derivadas, e so entao B_g = E_g = 0 e imposto NAS
EQUACOES; o sistema resolvido usa as equacoes de vinculo
{Phi_g, B_g, E_g, Phi_f, B_f, E_f, dchi} (00, 0i e ij-sem-traco dos
dois setores + campo), descartando as duas equacoes dinamicas
redundantes (Psi_g, Psi_f) como e padrao no regime quase-estatico.

Deriva mu(k,a), eta_slip(k,a) e Sigma(k,a) EXATOS no limite
quase-estatico (QS), a partir do mesmo setor escalar do script 01,
acrescentando a fonte de materia fria delta-rho no vinculo de Phi_g
(acoplamento minimo ao setor g: L_src = -a^3 drho Phi_g /2, do termo
(1/2) sqrt(-g) dT^{00} dg_{00} com dT^{00} = drho, dg_00 = -2 Phi_g).

Limite QS: velocidades das perturbacoes -> 0; grandezas de fundo
tipo-H (H, H_f, chidot, xidot) marcadas pequenas frente a k/a e as
massas de interacao m^2 F (mantidas — sao elas que geram a estrutura
tipo-Yukawa).

MODO SEMI-NUMERICO (padrao): o fundo do benchmark e substituido nas
equacoes QS ANTES do solve, mantendo k E m^2 simbolicos — m^2 fica
simbolico para que a calibracao GR (mu == 1 quando m^2 -> 0, com fundo
congelado) seja exata. Roda nos dois benchmarks (r < r_star e
r > r_star) para sondar a dependencia em r de alpha(a).

Confrontos (P6.6): forma exata vs ansatz de 1 polo (Cap.18 §18.3);
numero de polos (Cap.7 §7.6 antecipa 2); alpha(a) derivado vs
alpha_0 r^2/(1+r^2) (Cap.18 §18.4); eta_slip vs Cap.18 §18.7.

Uso:  python 06_mu_alpha_QS.py    (saida em out/06_output.txt;
      formas exatas em out/06_matrices.txt)
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

SEMI_NUMERIC = True

OUT = []
T0 = time.time()
drho = sp.Symbol('drho')
small = sp.Symbol('s_QS')


def say(*args):
    line = " ".join(str(x) for x in args)
    print(f"[{time.time()-T0:7.1f}s] " + line if line.strip() else line)
    OUT.append(line)


def build_qs_equations():
    """L2 + fonte de materia -> equacoes QS simbolicas (uma vez)."""
    Phi_g = sp.Function('Phi_g')(t)
    B_g = sp.Function('B_g')(t)
    Psi_g = sp.Function('Psi_g')(t)
    E_g = sp.Function('E_g')(t)
    Phi_f = sp.Function('Phi_f')(t)
    Psi_f = sp.Function('Psi_f')(t)
    B_f = sp.Function('B_f')(t)
    E_f = sp.Function('E_f')(t)
    dchi = sp.Function('dchi')(t)
    funcs = [Phi_g, B_g, Psi_g, E_g, Phi_f, Psi_f, B_f, E_f, dchi]

    aF, bF, xiF, bg_rules = make_bg_functions()
    g = substitute_bg_functions(scalar_metric_g(Phi_g, Psi_g, B_g, E_g),
                                aF, bF, xiF)
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

    PhiG = fields[0]
    L2s = L2s - a_s**3 * drho * PhiG / 2
    say("[1] L2 com fonte:", len(L2s.args), "termos")

    say("[2] montando equacoes quase-estaticas ...")
    zero_vel = {v: 0 for v in vels}
    eqs = [sp.expand(sp.diff(L2s, X).subs(zero_vel)) for X in fields]

    say("[3] impondo fundo on-shell e contagem QS ...")
    R = background_onshell_rules()
    eqs_qs = []
    for X, e in zip(fields, eqs):
        e = onshell(e, R)
        e = sp.expand(e.subs(rho_s, 0))
        eqs_qs.append(e)
        say(f"   eq {X}: {len(e.args) if e != 0 else 0} termos (estatica exata)")
    return eqs_qs, fields


def solve_qs(eqs, fallback, unknowns, label):
    """
    Resolve o sistema QS linear com linsolve (aceita sobredeterminado
    consistente). Se vier subdeterminado ou inconsistente, adiciona as
    equacoes dinamicas de reserva uma a uma, reportando.
    """
    pool = [e for e in eqs if e != 0]
    extra = [e for e in fallback if e != 0]
    say(f"[{label}] equacoes de vinculo nao triviais: {len(pool)}"
        f" (+{len(extra)} reservas dinamicas)")
    while True:
        A, rhs = sp.linear_eq_to_matrix(pool, unknowns)
        A = A.applyfunc(lambda e: sp.cancel(sp.together(e)))
        rhs = rhs.applyfunc(lambda e: sp.cancel(sp.together(e)))
        sol = sp.linsolve((A, rhs), *unknowns)
        if sol is sp.EmptySet or len(sol) == 0:
            say(f"[{label}] [!] sistema inconsistente com {len(pool)} eqs")
            if not extra:
                raise RuntimeError("sistema QS inconsistente sem reservas")
            pool.append(extra.pop(0))
            continue
        tup = list(list(sol)[0])
        livres = set()
        for x in tup:
            livres |= (x.free_symbols & set(unknowns))
        if livres and extra:
            say(f"[{label}] subdeterminado (livres: {livres}); "
                "adicionando eq. dinamica de reserva")
            pool.append(extra.pop(0))
            continue
        if livres:
            say(f"[{label}] [!] permanece subdeterminado; zerando {livres}")
            tup = [x.subs({s: 0 for s in livres}) for x in tup]
        say(f"[{label}] sistema resolvido ({len(pool)} eqs x "
            f"{len(unknowns)} inc.)")
        return dict(zip(unknowns,
                        [sp.cancel(sp.together(x)) for x in tup]))


def analyze_benchmark(eqs_qs, fields, delta, label, fh_forms):
    """Substitui o fundo (exceto m2), resolve e extrai mu/slip/Sigma."""
    vb = benchmark(sp.Rational(delta[0], delta[1]))
    vb[Ub] = vb[Ub] + vb[rho_s]
    vb[rho_s] = sp.Integer(0)
    # racionais PEQUENOS (denominador 10^12): os racionais exatos de 30
    # digitos tem numeradores ~2^100 e fazem o LUsolve simbolico em
    # (k, m2) rastejar; a 1e-12 os residuos ficam abaixo de qualquer
    # grandeza fisica do problema
    vnum = {s: sp.Rational(int(round(float(val) * 10**12)), 10**12)
            for s, val in vb.items() if s is not m2}
    rv = sp.nsimplify(vb[b_s] / vb[a_s])
    say("")
    say(f"===== {label}: r = {rv} = {float(rv):.4f}, "
        f"xi = {float(vb[xi_s]):.4f} =====")

    # gauge Newtoniano imposto NAS EQUACOES (nao na acao): B_g=E_g=0
    Bg, Eg = fields[1], fields[3]
    eqs_n = [sp.expand(e.subs(vnum).subs({Bg: 0, Eg: 0})) for e in eqs_qs]
    # potenciais resolvidos com {00-g, ij-sem-traco-g} + setor f completo
    # {00-f, trace-f, 0i-f, ij-sem-traco-f} + campo (dchi). A equacao de
    # momento do setor g (B_g) NAO entra: ela e fonteada pela velocidade
    # da materia (descartada no limite estatico) e serve para determinar
    # v, nao os potenciais — inclui-la impunha Phi=3Psi espurio no GR.
    # Reservas: Psi_g (trace-g), B_g (momento-g).
    prim = [eqs_n[i] for i in (0, 3, 4, 5, 6, 7, 8)]
    resv = [eqs_n[i] for i in (2, 1)]
    unknowns = [fields[i] for i in (0, 2, 4, 5, 6, 7, 8)]
    S = solve_qs(prim, resv, unknowns, label)
    S[Bg] = sp.Integer(0)
    S[Eg] = sp.Integer(0)

    PhiG, PsiG = fields[0], fields[2]
    respPhi = sp.cancel(sp.together(S[PhiG] / drho))
    respPsi = sp.cancel(sp.together(S[PsiG] / drho))

    # calibracao GR: m2 -> 0 com fundo congelado
    respPhi_GR = sp.cancel(sp.limit(respPhi, m2, 0))
    respPsi_GR = sp.cancel(sp.limit(respPsi, m2, 0))
    say(f"[{label}] resposta GR (m2->0): k^2 Phi/drho =",
        sp.nsimplify(sp.cancel(respPhi_GR * k**2), rational=True))
    say(f"[{label}]                      k^2 Psi/drho =",
        sp.nsimplify(sp.cancel(respPsi_GR * k**2), rational=True))
    Mg2n = vb[Mg2]
    a2n = vb[a_s]**2
    # em resposta estatica exata, correcoes O(H^2/k^2) sao fisicas:
    # calibra-se em k grande (regime quase-estatico emergente)
    kbig = 1000
    pois_num = float(sp.N(respPsi_GR.subs(k, kbig) * kbig**2))
    pois_alvo = float(-a2n / (2 * Mg2n))
    slip_num = float(sp.N((respPhi_GR / respPsi_GR).subs(k, kbig)))
    poisson_ok = abs(pois_num - pois_alvo) < 1e-3 * abs(pois_alvo)
    slip_gr_ok = abs(slip_num - 1) < 1e-3
    say(f"[{label}] Poisson GR em k={kbig}: {pois_num:+.6f} "
        f"(alvo {pois_alvo:+.6f}) -> {poisson_ok}")
    say(f"[{label}] Phi/Psi GR em k={kbig}: {slip_num:+.6f} -> {slip_gr_ok}")

    mu_m = sp.cancel(sp.together(respPhi / respPhi_GR))
    slip_m = sp.cancel(sp.together(S[PsiG] / S[PhiG]))
    Sig_m = sp.cancel(sp.together((respPhi + respPsi)
                                  / (respPhi_GR + respPsi_GR)))

    fh_forms.write(f"\n\n===== {label} =====\n")
    fh_forms.write("mu(k, m2) [fundo benchmark]:\n"
                   + sp.latex(mu_m) + "\n")
    fh_forms.write("eta_slip(k, m2):\n" + sp.latex(slip_m) + "\n")
    fh_forms.write("Sigma(k, m2):\n" + sp.latex(Sig_m) + "\n")

    # com m2 do benchmark: estrutura de polos em k^2
    mu_k = sp.cancel(mu_m.subs(m2, vb[m2]))
    slip_k = sp.cancel(slip_m.subs(m2, vb[m2]))
    Sig_k = sp.cancel(Sig_m.subs(m2, vb[m2]))

    K2 = sp.Symbol('K2')
    mu_K = sp.cancel(mu_k.subs(k**2, K2))
    num, den = sp.fraction(sp.together(mu_K))
    try:
        dn = sp.degree(sp.Poly(num, K2))
        dd = sp.degree(sp.Poly(den, K2))
        say(f"[{label}] mu racional em k^2: grau num = {dn}, den = {dd}")
        polos = sp.nroots(sp.Poly(den, K2)) if dd > 0 else []
        say(f"[{label}] polos em k^2: "
            + str([complex(p) for p in polos]))
        say(f"[{label}] (1 polo = ansatz Yukawa Cap.18 §18.3; "
            "2 polos = dois mediadores Cap.7 §7.6)")
        say(f"[{label}] massas: m_i^2 a^2 = -polo => "
            + str([complex(-p) for p in polos]))
        apart_mu = sp.apart(mu_K, K2)
        say(f"[{label}] fracoes parciais: {apart_mu}")
    except Exception as ex:
        say(f"[{label}] [!] analise de polos: {repr(ex)[:80]}")

    mu_inf = sp.limit(mu_k, k, sp.oo)
    alpha_der = float(sp.N(mu_inf - 1))
    e2 = float(vb[Mf2] * rv**2 / vb[Mg2])
    alpha_c18 = e2 / (1 + e2)
    say(f"[{label}] alpha derivado = mu(oo)-1 = {alpha_der:+.6f}")
    say(f"[{label}] alpha Cap.18 §18.4 (eps^2/(1+eps^2), eps=Mf r/Mg) "
        f"= {alpha_c18:+.6f}")

    say(f"[{label}]   k       mu          eta_slip     Sigma")
    for kv in (0.01, 0.1, 1, 10, 100, 1000):
        try:
            muv = float(sp.N(mu_k.subs(k, kv)))
            slv = float(sp.N(slip_k.subs(k, kv)))
            sgv = float(sp.N(Sig_k.subs(k, kv)))
            say(f"[{label}]  {kv:7.2f}  {muv:+10.6f}  {slv:+10.6f}"
                f"  {sgv:+10.6f}")
        except Exception as ex:
            say(f"[{label}]  {kv:7.2f}  [!] {repr(ex)[:60]}")
    return dict(mu=mu_m, slip=slip_m, Sigma=Sig_m, alpha=alpha_der,
                alpha_c18=alpha_c18, r=float(rv))


def main():
    say("=" * 70)
    say("DERIVACAO 6 — mu(k,a), eta_slip, Sigma (v4, resposta estatica exata)")
    say("    modo:", "SEMI-NUMERICO (fundo benchmark; k e m2 simbolicos)"
        if SEMI_NUMERIC else "SIMBOLICO COMPLETO")
    say("=" * 70)

    eqs_qs, fields = build_qs_equations()

    os.makedirs("out", exist_ok=True)
    fh_forms = open("out/06_matrices.txt", "w", encoding="utf-8")

    if SEMI_NUMERIC:
        resA = analyze_benchmark(eqs_qs, fields, (1, 25),
                                 "bench A (r<r_star)", fh_forms)
        resB = analyze_benchmark(eqs_qs, fields, (-1, 25),
                                 "bench B (r>r_star)", fh_forms)
        say("")
        say("Sondagem da dependencia em r de alpha(a) (P6.6):")
        say(f"  r = {resA['r']:.4f}: alpha_der = {resA['alpha']:+.6f}  "
            f"vs Cap.18: {resA['alpha_c18']:+.6f}")
        say(f"  r = {resB['r']:.4f}: alpha_der = {resB['alpha']:+.6f}  "
            f"vs Cap.18: {resB['alpha_c18']:+.6f}")
        say("")
        say("Leitura: numero de polos decide Yukawa-1-polo vs 2 polos;")
        say("alpha derivado vs alpha_0 r^2/(1+r^2) decide §18.4; a coluna")
        say("eta_slip decide §18.7. Formas exatas (m2 simbolico) em")
        say("out/06_matrices.txt.")
    else:
        vb = None
        S = solve_qs(eqs_qs, list(fields), "simbolico")
        PhiG, PsiG = fields[0], fields[1]
        respPhi = sp.cancel(sp.together(S[PhiG] / drho))
        respPhi_GR = sp.cancel(sp.limit(respPhi, m2, 0))
        mu_m = sp.cancel(sp.together(respPhi / respPhi_GR))
        fh_forms.write("mu(k,a) simbolico:\n" + sp.latex(mu_m) + "\n")
        say("mu simbolico salvo em out/06_matrices.txt")

    fh_forms.close()
    with open("out/06_output.txt", "w", encoding="utf-8") as fh:
        fh.write("\n".join(OUT))
    say("\nconcluido. saida em out/06_output.txt")


if __name__ == '__main__':
    main()
