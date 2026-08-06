# -*- coding: utf-8 -*-
"""
01_setor_escalar_K_Omega.py — Derivacao 1 (plano P1.1–P1.12), v4.

Setor escalar completo da TDCP bimetrica em k finito, do zero.

HISTORICO DE METODO (os becos sem saida fazem parte do resultado):
  v2 (gauge Newtoniano fixado na acao): posto(K)=3 — mas fixar B_g=E_g=0
     NA ACAO descarta as constraints desses campos (risco de modo
     espurio).
  v3 (sem fixar gauge, 9 campos): o auto-teste GR reprovou (3 modos em
     vez de 1) — em fundo congelado os modos de gauge nao aparecem como
     direcoes nulas de K, entao ficam no espectro.
  v4 (padrao): GAUGE PLANO NO SETOR g (Psi_g = E_g = 0) — fixa o gauge
     em campos DINAMICOS e mantem TODOS os multiplicadores (Phi_g, B_g,
     Phi_f, B_f), entao nenhuma constraint se perde. E a pratica segura
     (gauge plano/unitario) da literatura de acoes quadraticas.

Reducao iterativa de Faddeev–Jackiw (ipp -> auxiliares/Schur ->
direcoes nulas, repetindo ate a cinetica ficar nao-singular). O numero
de modos que sobrar responde a contagem (Cap.6.2 §6.4 diz 3; Anexo C
§C.3 diz 2).

Auto-teste GR embutido: o mesmo pipeline so com EH_g + chi em gauge
plano tem que dar EXATAMENTE 1 modo com c_s^2 = 1 antes do caso
bimetrico rodar.

Modos: SEMI_NUMERIC=True (padrao) substitui o fundo do benchmark logo
apos montar L2 (k fica simbolico) e roda em minutos; False = via
totalmente simbolica (horas/RAM — so depois de validar o padrao).

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
                           faddeev_jackiw_reduce, matrix_ipp_row,
                           dt_background, benchmark)

SEMI_NUMERIC = True
# 'flat-g'  (padrao): Psi_g = E_g = 0 — fixa o gauge em campos
#           DINAMICOS e mantem todos os multiplicadores (Phi_g, B_g,
#           Phi_f, B_f); nenhuma constraint se perde (pratica segura,
#           tipo gauge plano/unitario da literatura).
# 'none'   : 9 campos sem fixar gauge — deixa modos de gauge no
#           espectro em fundo congelado (o auto-teste GR reprova; util
#           so como diagnostico).
# 'newtonian': B_g = E_g = 0 fixado na acao — perde as constraints de
#           B_g/E_g (modo espurio; tambem so diagnostico).
GAUGE = 'flat-g'
RUN_GR_CHECK = True      # auto-teste GR+chi (1 modo, c_s^2=1) antes

OUT = []
T0 = time.time()


def say(*args):
    line = " ".join(str(x) for x in args)
    print(f"[{time.time()-T0:7.1f}s] " + line if line.strip() else line)
    OUT.append(line)


def cancelM(M):
    return M.applyfunc(lambda e: sp.cancel(sp.together(e)))


# ----------------------------------------------------------------------
# montagem de L2
# ----------------------------------------------------------------------
def build_fields(gauge):
    Phi_g = sp.Function('Phi_g')(t)
    Phi_f = sp.Function('Phi_f')(t)
    Psi_f = sp.Function('Psi_f')(t)
    B_f = sp.Function('B_f')(t)
    E_f = sp.Function('E_f')(t)
    dchi = sp.Function('dchi')(t)
    if gauge == 'flat-g':
        B_g = sp.Function('B_g')(t)
        return ([Phi_g, B_g, Phi_f, Psi_f, B_f, E_f, dchi],
                dict(Phi_g=Phi_g, Psi_g=sp.Integer(0), B_g=B_g,
                     E_g=None, Phi_f=Phi_f, Psi_f=Psi_f, B_f=B_f,
                     E_f=E_f, dchi=dchi))
    if gauge == 'newtonian':
        Psi_g = sp.Function('Psi_g')(t)
        return ([Phi_g, Psi_g, Phi_f, Psi_f, B_f, E_f, dchi],
                dict(Phi_g=Phi_g, Psi_g=Psi_g, B_g=None, E_g=None,
                     Phi_f=Phi_f, Psi_f=Psi_f, B_f=B_f, E_f=E_f,
                     dchi=dchi))
    Psi_g = sp.Function('Psi_g')(t)
    B_g = sp.Function('B_g')(t)
    E_g = sp.Function('E_g')(t)
    return ([Phi_g, B_g, Psi_g, E_g, Phi_f, B_f, Psi_f, E_f, dchi],
            dict(Phi_g=Phi_g, Psi_g=Psi_g, B_g=B_g, E_g=E_g,
                 Phi_f=Phi_f, Psi_f=Psi_f, B_f=B_f, E_f=E_f,
                 dchi=dchi))


def build_L2(gauge):
    funcs, F = build_fields(gauge)
    aF, bF, xiF, bg_rules = make_bg_functions()
    g = substitute_bg_functions(
        scalar_metric_g(F['Phi_g'], F['Psi_g'], F['B_g'], F['E_g']),
        aF, bF, xiF)
    f = substitute_bg_functions(
        scalar_metric_f(F['Phi_f'], F['Psi_f'], F['B_f'], F['E_f']),
        aF, bF, xiF)

    say("[1a] EH setor g (Gamma-Gamma) ...")
    Lg = lagrangian_GG(g, Mg2)
    say("[1b] EH setor f (Gamma-Gamma) ...")
    Lf = lagrangian_GG(f, Mf2)
    say("[1c] potencial HR (sqrt de Sylvester + e_n) ...")
    Lint = interaction_lagrangian(g, f, dchi=F['dchi'])
    say("[1d] setor chi ...")
    Lchi = chi_lagrangian(g, dchi=F['dchi'])

    Ltot = cut(Lg + Lf + Lint + Lchi)
    say("[1e] extraindo ordem eps^2 e mediando em z ...")
    L2 = z_average(eps_part(Ltot, 2))
    L2s, fields, vels = symbolize(L2, funcs, bg_rules)
    say(f"     L2 simbolizada: {len(L2s.args)} termos, "
        f"{len(fields)} campos")
    return L2s, fields, vels


# ----------------------------------------------------------------------
# auto-teste GR: EH_g + chi, sem setor f e sem interacao
# ----------------------------------------------------------------------
def gr_selfcheck():
    say("")
    say("[GR] auto-teste: GR + chi (sem f, sem interacao), gauge plano"
        " (Psi=E=0) — meta: 1 modo, c_s^2 = 1")
    Phi_g = sp.Function('Phi_g')(t)
    B_g = sp.Function('B_g')(t)
    dchi = sp.Function('dchi')(t)
    funcs = [Phi_g, B_g, dchi]
    aF, bF, xiF, bg_rules = make_bg_functions()
    g = substitute_bg_functions(
        scalar_metric_g(Phi_g, sp.Integer(0), B_g, None), aF, bF, xiF)
    Lg = lagrangian_GG(g, Mg2)
    Lchi = chi_lagrangian(g, dchi=dchi)
    L2 = z_average(eps_part(cut(Lg + Lchi), 2))
    L2s, fields, vels = symbolize(L2, funcs, bg_rules)

    # fundo GR consistente: 3 Mg^2 H^2 = chid^2/2 + U ; Hd = -chid^2/2
    vgr = {Mg2: 1, a_s: 1, H_s: 1, chid_s: sp.Rational(3, 10),
           Up: sp.Rational(-1, 5), Upp: sp.Rational(3, 10), rho_s: 0}
    vgr[Ub] = 3 - sp.Rational(9, 200)
    vgr[Hd_s] = -sp.Rational(9, 200)
    vgr[chidd_s] = -3 * vgr[H_s] * vgr[chid_s] - vgr[Up]
    L2n = sp.expand(L2s.subs(vgr))

    K, C, W = quadratic_matrices(L2n, fields, vels)
    K, C, W = cancelM(K), cancelM(C), cancelM(W)
    names = [str(x) for x in fields]
    K, C, W, names = faddeev_jackiw_reduce(K, C, W, names, log=say)
    say("[GR] modos finais:", len(names), names)
    if len(names) == 1:
        ks = [sp.Rational(1, 10), 1, 10, 100]
        w2 = [float(sp.N((W[0, 0] / K[0, 0]).subs(k, kv))) for kv in ks]
        c2 = (w2[-1] - w2[-2]) / (float(ks[-1]**2 - ks[-2]**2))
        say(f"[GR] omega^2(k) = {w2}")
        say(f"[GR] c_s^2 (fit k grande) = {c2:+.6f}  [meta: +1.0]")
        ok = abs(c2 - 1.0) < 0.05
        say("[GR] APROVADO" if ok else "[GR] REPROVADO — investigar antes"
            " de confiar no caso bimetrico")
        return ok
    say("[GR] REPROVADO (contagem != 1) — investigar")
    return False


# ----------------------------------------------------------------------
# benchmark e analise
# ----------------------------------------------------------------------
def onshell_numeric_values(delta):
    v = benchmark(sp.Rational(delta[0], delta[1]))
    v[Ub] = v[Ub] + v[rho_s]
    v[rho_s] = sp.Integer(0)
    return v


def gen_eigs(K, W, kv):
    """Autovalores generalizados det(W - lam K) = 0 (robusto a K singular)."""
    lam = sp.Symbol('lam')
    Kn = K.subs(k, kv)
    Wn = W.subs(k, kv)
    p = sp.Poly(sp.cancel(sp.together((Wn - lam * Kn).det())), lam)
    return sorted(complex(r).real for r in sp.nroots(p))


def analyze(K, C, W, names, vb, label):
    rv = float(vb[b_s] / vb[a_s])
    fac = float((b1 + 2 * b2 * (b_s / a_s)).subs(vb))
    claim = float((m2 * Fb).subs(vb)) * fac
    say(f"\n--- {label}: r = {rv:.4f}, beta1+2*beta2*r = {fac:+.4f} ---")
    say(f"    modos dinamicos ({len(names)}): {names}")
    say(f"    claim Cap.15 §15.5: m_S^2 ~ m2*F*(beta1+2b2r) = {claim:+.4f}")
    # acoplamento giroscopico (parte antissimetrica de C): se ~0, o
    # espectro generalizado det(W - lam K)=0 abaixo e exato; senao, e
    # aproximacao (caveat a reportar)
    Ca = (C - C.T) / 2
    try:
        camax = max(abs(float(sp.N(Ca[i, j].subs(k, 1))))
                    for i in range(Ca.shape[0]) for j in range(Ca.shape[1]))
    except Exception:
        camax = float('nan')
    say(f"    |C_antissim|_max (k=1) = {camax:.3e}"
        " (0 => dispersao abaixo exata)")
    say("  k        autovals K                     omega^2 (gen.)")
    dados = {}
    for kv in (sp.Rational(1, 10), 1, 10, 100):
        Kn = K.subs(k, kv)
        evK = sorted(complex(sp.N(e)).real for e in Kn.eigenvals())
        evD = gen_eigs(K, W, kv)
        dados[float(kv)] = (evK, evD)
        say(f"  {float(kv):7.2f}  {['%+.3e' % x for x in evK]}"
            f"  {['%+.3e' % x for x in evD]}")
    a2 = float(vb[a_s]**2)
    try:
        k1, k2v = 10.0, 100.0
        nmodos = len(dados[k1][1])
        for idx in range(nmodos):
            w1, w2 = dados[k1][1][idx], dados[k2v][1][idx]
            c2 = (w2 - w1) / ((k2v**2 - k1**2) / a2)
            mm2 = w1 - c2 * k1**2 / a2
            say(f"    modo {idx+1}: c_s^2 = {c2:+.5f},  m^2 = {mm2:+.5f}"
                f"   [claim m_S^2 = {claim:+.5f}]")
    except Exception as ex:
        say("    [!] fit c_s^2/m^2 falhou:", repr(ex)[:70])


def main():
    say("=" * 70)
    say("DERIVACAO 1 — setor escalar: K_ij e Omega_ij em k finito (v4)")
    say(f"    gauge: {GAUGE}"
        + (" (Psi_g=E_g=0; multiplicadores mantidos)"
           if GAUGE == 'flat-g' else ""))
    say("    modo:", "SEMI-NUMERICO" if SEMI_NUMERIC else "SIMBOLICO")
    say("=" * 70)

    os.makedirs("out", exist_ok=True)

    if RUN_GR_CHECK:
        gr_ok = gr_selfcheck()
        say("")
        if not gr_ok:
            say("[!] auto-teste GR falhou — resultados bimetricos abaixo"
                " devem ser lidos com desconfianca")

    L2s, fields, vels = build_L2(GAUGE)

    if not SEMI_NUMERIC:
        say("[modo simbolico] extraindo blocos e reduzindo (pode levar"
            " horas) ...")
        K, C, W = quadratic_matrices(L2s, fields, vels)
        K, C, W = cancelM(K), cancelM(C), cancelM(W)
        names = [str(x) for x in fields]
        K, C, W, names = faddeev_jackiw_reduce(K, C, W, names, log=say)
        with open("out/01_matrices.txt", "w", encoding="utf-8") as fh:
            fh.write("modos: " + str(names) + "\n\nK:\n" + sp.srepr(K)
                     + "\n\nlatex:\n" + sp.latex(K) + "\n\nW:\n"
                     + sp.srepr(W) + "\n\nlatex:\n" + sp.latex(W) + "\n")
        say("matrizes simbolicas salvas em out/01_matrices.txt")
    else:
        primeira = True
        for delta, label in (((1, 25), "benchmark A (r < r_star)"),
                             ((-1, 25), "benchmark B (r > r_star)")):
            vb = onshell_numeric_values(delta)
            say("")
            say(f"[{label}] substituindo fundo e extraindo blocos ...")
            L2n = sp.expand(L2s.subs(vb))
            K, C, W = quadratic_matrices(L2n, fields, vels)
            K, C, W = cancelM(K), cancelM(C), cancelM(W)
            names = [str(x) for x in fields]
            say(f"[{label}] reducao Faddeev-Jackiw ...")
            K, C, W, names = faddeev_jackiw_reduce(K, C, W, names, log=say,
                                                   chop_tol=1e-18)
            analyze(K, C, W, names, vb, label)
            with open("out/01_matrices.txt",
                      "w" if primeira else "a", encoding="utf-8") as fh:
                fh.write(f"\n\n===== {label} =====\n")
                fh.write("modos: " + str(names) + "\n")
                fh.write("K:\n" + sp.latex(K.applyfunc(
                    lambda e: sp.nsimplify(e, rational=True))) + "\n")
                fh.write("W_eff:\n" + sp.latex(W.applyfunc(
                    lambda e: sp.nsimplify(e, rational=True))) + "\n")
            primeira = False

        say("")
        say("Leitura (P1.9–P1.12):")
        say("- CONTAGEM: n. de modos finais decide Cap.6.2 §6.4 (3) vs")
        say("  Anexo C §C.3 (2); o auto-teste GR valida a maquina;")
        say("- no-ghost: sinais de eig(K) em A (fator>0) vs B (fator<0)")
        say("  testam Cap.15 §15.4;")
        say("- m^2 dos modos vs claim m2*F*(beta1+2b2r) testa §15.5;")
        say("- caveat: Hdot=Hfdot=xidot=0 no benchmark (quase-de Sitter).")

    with open("out/01_output.txt", "w", encoding="utf-8") as fh:
        fh.write("\n".join(OUT))
    say("\nconcluido. saida em out/01_output.txt")


if __name__ == '__main__':
    main()
