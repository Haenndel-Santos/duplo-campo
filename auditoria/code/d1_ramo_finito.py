# -*- coding: utf-8 -*-
"""
d1_ramo_finito.py — O TESTE QUE DECIDE: setor escalar no ramo finito.

Refaz a analise da Derivacao 1 (QEP numerico por k, gauge plano no
setor g) no fundo CORRETO pos-Erratum 01 — o ramo finito, com beta_n
CONSTANTES e sem modulacao (F=1, F'=0).

Por que isto decide. O antigo "ramo dinamico duplamente morto" tinha
duas pernas: rdot=0 (caiu com o Erratum 01 — no ramo correto r evolui)
e o par escalar fantasma/taquiônico da D1. Mas a D1 montou seus
benchmarks impondo xi = H/H_f, que NAO satisfaz a constraint correta
(no ramo certo, H/H_f = r). Este script roda a MESMA maquinaria da D1
(mesma acao, mesmo gauge, mesmo QEP, mesmo auto-teste GR) no fundo
consistente com a constraint corrigida:

    r     : raiz FINITA da cubica  m^2 M_eff^2 W(r) = rho
    xi    : r + dr/dN,  com dr/dN = -3 rho_til / W'(r)  (implicita)
    H_f   : H / r
    chi   : espectador congelado (chid=0, U'=0, F'=0) — beta constantes

Resultados possiveis:
  - par relativo SAUDAVEL  -> o ramo finito e viavel; a TDCP-F1
    corrigida (sem modulacao) passa Higuchi E no-ghost; a arquitetura
    beta_n(phi_-) vira extensao opcional.
  - par relativo FANTASMA  -> a patologia escalar e intrinseca ao
    setor bimetrico (nao artefato do fundo errado); volta a modulacao
    ou o veredito de inviabilidade.

CAVEATS (mesmos da D1, declarados): fundo quase-de Sitter congelado
(Hdot=Hfdot=xidot=0 — aqui |Hdot/H^2| ~ 0.3 no ponto de a=1, entao a
aproximacao e mais tensa que na D1; modos com |w2| ~ H^2 devem ser
lidos com cautela; a hierarquia k >> H e a regiao confiavel).
Materia de fundo movida para Ub (mesmo truque do main() da D1 — nao ha
perturbacao de materia na analise).

Requer sympy, numpy, scipy.  Rodar DESTA pasta ou da raiz do repo:
    python auditoria/code/d1_ramo_finito.py
Demora varios minutos (montagem simbolica 7x7 + QEP por k).
"""
import importlib.util
import os
import sys
import time

import sympy as sp

# ---------------------------------------------------------------------
# carrega o script 01 como modulo (nome comeca com digito)
# ---------------------------------------------------------------------
HERE = os.path.dirname(os.path.abspath(__file__))
DCODE = os.path.normpath(os.path.join(HERE, '..', '..', 'derivations', 'code'))
sys.path.insert(0, DCODE)

spec = importlib.util.spec_from_file_location(
    "d1mod", os.path.join(DCODE, "01_setor_escalar_K_Omega.py"))
d1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(d1)

from tdcp_pert_lib import (a_s, b_s, xi_s, H_s, Hf_s, Hd_s, Hfd_s, xid_s,
                           chid_s, chidd_s, Mg2, Mf2, m2, Meff2,
                           b0, b1, b2, b3, b4, Fb, Fp, Fpp,
                           Ub, Up, Upp, rho_s, quadratic_matrices)

# ---------------------------------------------------------------------
# parametros do ramo finito (os MESMOS de ramo_dinamico_correto.py)
# ---------------------------------------------------------------------
PB = {b0: sp.Integer(1), b1: sp.Integer(1), b2: sp.Rational(-2, 5),
      b3: sp.Integer(0), b4: sp.Rational(1, 2),
      Mg2: sp.Integer(1), Mf2: sp.Integer(1),
      Meff2: sp.Rational(1, 2), m2: sp.Integer(1)}
RHO_M0 = sp.Rational(3, 10)


def _W(r):
    """W(r) = (Mg2/Mf2) r^2 V_f(r) - V_g(r), simbolico em r."""
    Vf = PB[b4] + 3*PB[b3]/r + 3*PB[b2]/r**2 + PB[b1]/r**3
    Vg = PB[b0] + 3*PB[b1]*r + 3*PB[b2]*r**2 + PB[b3]*r**3
    return (PB[Mg2]/PB[Mf2])*r**2*Vf - Vg


def benchmark_ramo_finito(a_val):
    """Fundo consistente com a constraint CORRIGIDA no ramo finito.

    r resolve  m^2 M_eff^2 W(r) = rho  (raiz finita, por nsolve com
    chute r ~ beta_1/rho_til, o balanco do ramo finito);
    xi = r + dr/dN via diferenciacao implicita;
    H_f = H/r;  chi congelado (beta_n constantes, sem modulacao).
    """
    rho = RHO_M0 * a_val**-3
    rho_til = rho / (PB[m2]*PB[Meff2])

    rr = sp.Symbol('rr', positive=True)
    eq = _W(rr) - rho_til
    chute = min(sp.Rational(1, 3),
                PB[b1]/rho_til)          # r ~ b1/rho_til quando rho grande
    r_val = sp.nsolve(eq, rr, chute, prec=30)

    dW = sp.diff(_W(rr), rr).subs(rr, r_val)
    drdN = -3*rho_til/dW                  # d/dN de W(r)=rho_til
    xi_val = r_val + drdN

    H2 = (PB[m2]*PB[Meff2]*r_val**2 *
          (PB[b4] + 3*PB[b3]/r_val + 3*PB[b2]/r_val**2 + PB[b1]/r_val**3)
          ) / (3*PB[Mf2])
    H_val = sp.sqrt(H2)

    rho_int = (PB[m2]*PB[Meff2] *
               (PB[b0] + 3*PB[b1]*r_val + 3*PB[b2]*r_val**2
                + PB[b3]*r_val**3))
    Ub_val = 3*PB[Mg2]*H2 - rho - rho_int   # deve ser ~0 (identidade)

    vals = dict(PB)
    vals.update({
        a_s: sp.Integer(1),               # a reescalado p/ 1 no ponto
        b_s: r_val,                       # (so a razao r importa)
        xi_s: xi_val,
        H_s: H_val,
        Hf_s: H_val / r_val,              # ramo correto: H_f = H/r
        Fb: sp.Integer(1), Fp: sp.Integer(0), Fpp: sp.Integer(0),
        chid_s: sp.Integer(0), chidd_s: sp.Integer(0),
        Up: sp.Integer(0), Upp: sp.Rational(3, 10),
        rho_s: rho,
        Ub: Ub_val,
        Hd_s: 0, Hfd_s: 0, xid_s: 0,      # fundo congelado (caveat D1)
    })
    # mesmo truque do main() da D1: materia -> Ub (sem perturbacao de materia)
    vals[Ub] = vals[Ub] + vals[rho_s]
    vals[rho_s] = sp.Integer(0)
    # racionaliza (30 digitos), como o benchmark original
    out = {}
    for kk, vv in vals.items():
        out[kk] = sp.Rational(sp.N(vv, 30)) if vv != 0 else sp.Integer(0)
    return out, float(r_val), float(xi_val), float(H_val), float(drdN)


def main():
    d1.say("=" * 70)
    d1.say("D1 NO RAMO FINITO — setor escalar com a constraint CORRIGIDA")
    d1.say("    beta_n CONSTANTES, sem modulacao (F=1, F'=0)")
    d1.say("    fundo: r da cubica, xi = r + dr/dN, H_f = H/r")
    d1.say("=" * 70)

    gr_ok = d1.gr_selfcheck()
    if not gr_ok:
        d1.say("[!] auto-teste GR falhou — abortar leitura dos resultados")
        return 1

    L2s, fields, vels = d1.build_L2()
    d1.say("[2] blocos simbolicos (K, C, W) ...")
    K7, C7, W7 = quadratic_matrices(L2s, fields, vels)

    for a_val, tag in ((sp.Integer(1), "hoje (a=1)"),
                       (sp.Rational(1, 2), "passado (a=0.5)"),
                       (sp.Integer(2), "futuro (a=2, perto do ponto fixo)")):
        vb, rv, xv, Hv, dr = benchmark_ramo_finito(a_val)
        fac = float(sp.N(PB[b1] + PB[b2]*(sp.Float(xv) + sp.Float(rv))))
        d1.say(f"\n    ponto: {tag}  r={rv:.4f}  xi={xv:.4f}  "
               f"H={Hv:.4f}  dr/dN={dr:+.4f}")
        d1.say(f"    fator estrutural beta1+beta2(xi+r) = {fac:+.4f}  "
               f"(era -0.88 no fundo errado da D1)")
        d1.espectro_por_k(
            K7, C7, W7, vb,
            f"RAMO FINITO {tag}: r={rv:.4f}, xi={xv:.4f}")

    d1.say("")
    d1.say("LEITURA:")
    d1.say("- contagem esperada: 3 modos (delta-chi espectador + par")
    d1.say("  relativo); o espectador deve dar c_s^2=1, m^2=+0.3;")
    d1.say("- kinetic-sign NEGATIVO em modo do par relativo = fantasma")
    d1.say("  persiste mesmo no fundo correto -> patologia intrinseca;")
    d1.say("- todos kN>0 e w2 reais -> o ramo finito passa no-ghost, e a")
    d1.say("  TDCP-F1 corrigida (sem modulacao) fica viavel neste nivel;")
    d1.say("- caveat: fundo congelado com |Hdot/H^2|~0.3 — modos com")
    d1.say("  |w2| ~ H^2 sao indicativos; k >> H e a regiao confiavel.")

    os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
    with open(os.path.join(HERE, "out", "d1_ramo_finito.txt"),
              "w", encoding="utf-8") as fh:
        fh.write("\n".join(d1.OUT))
    d1.say("\nconcluido. saida em auditoria/code/out/d1_ramo_finito.txt")
    return 0


if __name__ == '__main__':
    sys.exit(main())
