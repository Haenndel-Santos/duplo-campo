# -*- coding: utf-8 -*-
"""
01_setor_escalar_K_Omega.py — Derivacao 1 (plano P1.1–P1.12), v5.

Setor escalar completo da TDCP bimetrica em k finito, do zero.

HISTORICO DE METODO (faz parte do resultado):
  v2 gauge Newtoniano fixado na acao -> perde constraints (modo espurio);
  v3 sem fixar gauge -> auto-teste GR reprovou (modos de gauge ficam no
     espectro em fundo congelado);
  v4 gauge plano no setor g (Psi_g=E_g=0, multiplicadores mantidos) —
     correto — mas a reducao simbolica de Faddeev-Jackiw em k simbolico
     explode nas rodadas 2+ (funcoes racionais com coeficientes
     gigantes; sondagem instrumentada em 2026-08-06);
  v5 (atual): mesma acao e gauge da v4; o espectro fisico e obtido por
     PROBLEMA DE AUTOVALOR QUADRATICO (QEP) numerico por k:
         (lam^2 K + lam C_a + W) v = 0,   lam = i*omega,
     linearizado para autovalor generalizado 2n x 2n. Vinculos e
     multiplicadores aparecem como autovalores infinitos (filtrados);
     modos fisicos como pares finitos +-; ghost detectado pelo sinal de
     Re(v^dagger K v) por automodo. Sem reducao simbolica; trata
     exatamente o acoplamento giroscopico C_a.

Saidas: contagem de modos fisicos (decide Cap.6.2 §6.4 = 3 vs Anexo C
§C.3 = 2), omega^2(k), c_s^2 e m^2 por modo, sinais cineticos
(no-ghost) nos dois benchmarks (r < r_star e r > r_star), e as
matrizes 7x7 SIMBOLICAS K, C, W (pre-reducao) em out/01_matrices.txt
— os K_ij/Omega_ij explicitos do plano.

Auto-teste GR embutido (EH_g + chi, gauge plano): 1 modo, c_s^2 = 1.

Uso:  python 01_setor_escalar_K_Omega.py
      (saida em out/01_output.txt; matrizes em out/01_matrices.txt)
"""
import os
import time
import numpy as np
import scipy.linalg as sla
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
                           benchmark)

KGRID = [0.1, 1.0, 10.0, 100.0]
INF_CUT = 1e7          # |lam| acima disso = modo de vinculo (infinito)

OUT = []
T0 = time.time()


def say(*args):
    line = " ".join(str(x) for x in args)
    print(f"[{time.time()-T0:7.1f}s] " + line if line.strip() else line)
    OUT.append(line)


# ----------------------------------------------------------------------
# montagem simbolica (gauge plano no setor g)
# ----------------------------------------------------------------------
def build_L2():
    Phi_g = sp.Function('Phi_g')(t)
    B_g = sp.Function('B_g')(t)
    Phi_f = sp.Function('Phi_f')(t)
    Psi_f = sp.Function('Psi_f')(t)
    B_f = sp.Function('B_f')(t)
    E_f = sp.Function('E_f')(t)
    dchi = sp.Function('dchi')(t)
    funcs = [Phi_g, B_g, Phi_f, Psi_f, B_f, E_f, dchi]

    aF, bF, xiF, bg_rules = make_bg_functions()
    g = substitute_bg_functions(
        scalar_metric_g(Phi_g, sp.Integer(0), B_g, None), aF, bF, xiF)
    f = substitute_bg_functions(
        scalar_metric_f(Phi_f, Psi_f, B_f, E_f), aF, bF, xiF)

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
    say(f"     L2 simbolizada: {len(L2s.args)} termos, {len(fields)} campos")
    return L2s, fields, vels


# ----------------------------------------------------------------------
# QEP numerico
# ----------------------------------------------------------------------
def qep_modes(Kn, Cn, Wn):
    """
    Resolve (lam^2 K + lam C_a + W) v = 0 por linearizacao:
        lam * [[K,0],[0,I]] z = [[-C_a,-W],[I,0]] z,  z = (lam v, v).
    Retorna lista de dicts dos automodos FINITOS:
        {lam, omega2 (= -lam^2), v, knorm (= Re v^H K v)}.
    """
    n = Kn.shape[0]
    Ca = Cn - Cn.T
    A = np.block([[-Ca, -Wn], [np.eye(n), np.zeros((n, n))]])
    B = np.block([[Kn, np.zeros((n, n))], [np.zeros((n, n)), np.eye(n)]])
    lam, vec = sla.eig(A, B)
    modos = []
    for i in range(len(lam)):
        li = lam[i]
        if not np.isfinite(li) or abs(li) > INF_CUT:
            continue
        v = vec[n:, i]
        nv = np.linalg.norm(v)
        if nv < 1e-12:
            continue
        v = v / nv
        knorm = float(np.real(np.conjugate(v) @ Kn @ v))
        modos.append(dict(lam=complex(li), omega2=complex(-li**2),
                          v=v, knorm=knorm))
    return modos


def agrupa_pares(modos, tol=1e-6):
    """Agrupa automodos em pares +-lam; retorna um representante por par."""
    usados = [False] * len(modos)
    pares = []
    for i, mi in enumerate(modos):
        if usados[i]:
            continue
        usados[i] = True
        for j in range(i + 1, len(modos)):
            if usados[j]:
                continue
            if abs(mi['lam'] + modos[j]['lam']) <= tol * (1 + abs(mi['lam'])):
                usados[j] = True
                break
        pares.append(mi)
    return pares


def to_numpy(M, subs):
    Mn = M.subs(subs)
    return np.array([[float(sp.N(Mn[i, j], 20))
                      for j in range(M.shape[1])]
                     for i in range(M.shape[0])], dtype=float)


def espectro_por_k(K, C, W, vb, label, claim=None):
    say(f"\n--- {label} ---")
    resultados = {}
    for kv in KGRID:
        subs = dict(vb)
        subs[k] = sp.Rational(kv)
        Kn = to_numpy(K, subs)
        Cn = to_numpy(C, subs)
        Wn = to_numpy(W, subs)
        pares = agrupa_pares(qep_modes(Kn, Cn, Wn))
        pares.sort(key=lambda m: abs(m['omega2']))
        resultados[kv] = pares
        desc = ", ".join(
            f"w2={m['omega2'].real:+.4e}{'' if abs(m['omega2'].imag) < 1e-8 else ' (imag!)'}"
            f" kN={m['knorm']:+.2e}" for m in pares)
        say(f"  k={kv:7.2f}: {len(pares)} modo(s) | {desc}")
    # fit c^2 e m^2 por modo com os dois maiores k
    k1, k2v = KGRID[-2], KGRID[-1]
    p1, p2 = resultados[k1], resultados[k2v]
    a2 = float(vb[a_s]**2)
    if len(p1) == len(p2) and p1:
        for idx in range(len(p1)):
            w1 = p1[idx]['omega2'].real
            w2 = p2[idx]['omega2'].real
            c2 = (w2 - w1) / ((k2v**2 - k1**2) / a2)
            mm2 = w1 - c2 * k1**2 / a2
            extra = f"   [claim m_S^2 = {claim:+.5f}]" if claim is not None else ""
            say(f"    modo {idx+1}: c_s^2 = {c2:+.6f}, m^2 = {mm2:+.5f}, "
                f"kinetic-sign = {'+' if p1[idx]['knorm'] > 0 else '-'}{extra}")
    return resultados


# ----------------------------------------------------------------------
# auto-teste GR
# ----------------------------------------------------------------------
def gr_selfcheck():
    say("")
    say("[GR] auto-teste: GR + chi, gauge plano — meta: 1 modo, c_s^2 = 1")
    Phi_g = sp.Function('Phi_g')(t)
    B_g = sp.Function('B_g')(t)
    dchi = sp.Function('dchi')(t)
    funcs = [Phi_g, B_g, dchi]
    aF, bF, xiF, bg_rules = make_bg_functions()
    g = substitute_bg_functions(
        scalar_metric_g(Phi_g, sp.Integer(0), B_g, None), aF, bF, xiF)
    L2 = z_average(eps_part(cut(lagrangian_GG(g, Mg2)
                                + chi_lagrangian(g, dchi=dchi)), 2))
    L2s, fields, vels = symbolize(L2, funcs, bg_rules)
    vgr = {Mg2: 1, a_s: 1, H_s: 1, chid_s: sp.Rational(3, 10),
           Up: sp.Rational(-1, 5), Upp: sp.Rational(3, 10), rho_s: 0,
           Ub: 3 - sp.Rational(9, 200), Hd_s: -sp.Rational(9, 200)}
    vgr[chidd_s] = -3 * vgr[H_s] * vgr[chid_s] - vgr[Up]
    K, C, W = quadratic_matrices(sp.expand(L2s.subs(vgr)), fields, vels)

    ok_count = True
    w2s = {}
    for kv in KGRID:
        subs = {k: sp.Rational(kv)}
        pares = agrupa_pares(qep_modes(to_numpy(K, subs), to_numpy(C, subs),
                                       to_numpy(W, subs)))
        if len(pares) != 1:
            ok_count = False
        if pares:
            w2s[kv] = pares[0]['omega2'].real
    say(f"[GR] modos por k: "
        + str({kv: len(agrupa_pares(qep_modes(
            to_numpy(K, {k: sp.Rational(kv)}), to_numpy(C, {k: sp.Rational(kv)}),
            to_numpy(W, {k: sp.Rational(kv)})))) for kv in KGRID}))
    c2 = (w2s[KGRID[-1]] - w2s[KGRID[-2]]) / (KGRID[-1]**2 - KGRID[-2]**2)
    say(f"[GR] omega^2(k) = {[round(w2s[kv], 4) for kv in KGRID]}")
    say(f"[GR] c_s^2 (fit) = {c2:+.6f}  [meta +1.0]")
    ok = ok_count and abs(c2 - 1) < 0.02
    say("[GR] APROVADO" if ok else "[GR] REPROVADO — investigar")
    return ok


# ----------------------------------------------------------------------
def main():
    say("=" * 70)
    say("DERIVACAO 1 — setor escalar (v5, QEP numerico por k)")
    say("    gauge: flat-g (Psi_g=E_g=0; multiplicadores mantidos)")
    say("=" * 70)

    os.makedirs("out", exist_ok=True)
    gr_ok = gr_selfcheck()
    if not gr_ok:
        say("[!] auto-teste GR falhou — abortar leitura dos resultados")

    L2s, fields, vels = build_L2()

    say("[2] blocos simbolicos 7x7 (K, C, W) ...")
    K7, C7, W7 = quadratic_matrices(L2s, fields, vels)
    with open("out/01_matrices.txt", "w", encoding="utf-8") as fh:
        fh.write("Campos (ordem): " + str([str(f) for f in fields]) + "\n")
        fh.write("Gauge: plano no setor g (Psi_g=E_g=0)\n")
        fh.write("L2 = 1/2 qdot K qdot + qdot C q - 1/2 q W q\n\n")
        for nome, M in (("K7", K7), ("C7", C7), ("W7", W7)):
            fh.write(f"===== {nome} =====\n")
            fh.write("srepr:\n" + sp.srepr(M) + "\n\nlatex:\n"
                     + sp.latex(M) + "\n\n")
    say("    matrizes simbolicas salvas em out/01_matrices.txt")

    for delta, label in ((sp.Rational(1, 25), "benchmark A (r < r_star)"),
                         (sp.Rational(-1, 25), "benchmark B (r > r_star)")):
        vb = benchmark(delta)
        vb[Ub] = vb[Ub] + vb[rho_s]
        vb[rho_s] = sp.Integer(0)
        rv = float(vb[b_s] / vb[a_s])
        fac = float((b1 + 2 * b2 * (b_s / a_s)).subs(vb))
        claim = float((m2 * Fb).subs(vb)) * fac
        espectro_por_k(K7, C7, W7, vb,
                       f"{label}: r = {rv:.4f}, "
                       f"beta1+2*beta2*r = {fac:+.4f}", claim)

    say("")
    say("Leitura (P1.9–P1.12):")
    say("- CONTAGEM de modos finitos decide Cap.6.2 §6.4 (3) vs Anexo C (2);")
    say("- kinetic-sign negativo em algum modo = ghost; comparar A (fator>0)")
    say("  vs B (fator<0) testa a claim do Cap.15 §15.4;")
    say("- m^2 do modo relativo vs claim m2*F*(beta1+2b2r) testa §15.5;")
    say("- caveat: fundo quase-de Sitter congelado (Hdot=Hfdot=xidot=0);")
    say("- w2 com parte imaginaria = instabilidade (reportada).")

    with open("out/01_output.txt", "w", encoding="utf-8") as fh:
        fh.write("\n".join(OUT))
    say("\nconcluido. saida em out/01_output.txt")


if __name__ == '__main__':
    main()
