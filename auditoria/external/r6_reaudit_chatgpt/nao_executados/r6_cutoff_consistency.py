# -*- coding: utf-8 -*-
"""
r6_cutoff_consistency.py
========================

R6-A: audit of the strong-coupling/cutoff claim in TDCP-F1.

Purpose
-------
The current Gate F-b compares the canonical negative-norm branch
frequency omega_0 with a proxy Lambda_3 constructed from m_T^2.
This script separates quantities that must NOT be conflated:

  (A) the fundamental interaction scale appearing in the action,
      m^2 M_eff^2 sum beta_n e_n(sqrt(g^-1 f));

  (B) candidate Lambda_3 scales built from the bare spin-2 interaction
      mass parameter and the independent Planck scales;

  (C) the cosmological tensor eigenmass m_T^2 derived exactly from the
      quadratic tensor action;

  (D) the canonical scalar-branch frequency omega_0 from Gate F-b.

A quadratic calculation cannot by itself prove its own nonlinear cutoff.
Therefore this script has a hard epistemic gate:

    R6-RIGOROUS = PASS

is impossible unless an independently derived nonlinear/cubic or
Stueckelberg/decoupling-limit scale is provided with --lambda-nonlinear.

This is deliberate.  It prevents "m_T -> Lambda_3" from being elevated
from proxy to derivation without an extra calculation.

Usage (from repository root)
----------------------------
    python auditoria/code/r6_cutoff_consistency.py
    python auditoria/code/r6_cutoff_consistency.py --beta1 1
    python auditoria/code/r6_cutoff_consistency.py \
        --lambda-nonlinear 1.23 --lambda-nonlinear-label "cubic canonical"

Outputs
-------
    auditoria/code/out/r6_cutoff_consistency.txt
    auditoria/code/out/r6_cutoff_consistency.json

The default numbers reproduce the two Gate-F backgrounds beta1={1,4.47},
with the same F1 choices used there.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass, asdict
from pathlib import Path

import numpy as np


@dataclass
class Params:
    beta0: float = 1.0
    beta1: float = 1.0
    beta2: float = -0.4
    beta3: float = 0.0
    beta4: float = 0.5
    mu: float = 1.0              # M_f^2 / M_g^2
    Mg2: float = 1.0
    m2: float = 1.0
    Fbar: float = 1.0
    rho0: float = 0.3


@dataclass
class Point:
    a: float
    r: float
    xi: float
    H: float
    Hf: float
    mT2: float
    omega0_over_H: float
    omega0: float
    Lambda3_g: float
    Lambda3_f: float
    Lambda3_eff: float
    Lambda3_mT_g: float
    omega_over_L3g: float
    omega_over_L3f: float
    omega_over_L3eff: float
    omega_over_L3mTg: float


def cube_root_pos(x: float) -> float:
    if x <= 0:
        raise ValueError(f"positive scale expected, got {x}")
    return x ** (1.0 / 3.0)


def meff2(p: Params) -> float:
    """
    Convention already used by the TDCP scripts:
        M_eff^2 = M_g^2 M_f^2 / (M_g^2 + M_f^2)
    for M_f^2 = mu M_g^2.
    """
    Mf2 = p.mu * p.Mg2
    return p.Mg2 * Mf2 / (p.Mg2 + Mf2)


def finite_branch_background(a: float, p: Params) -> tuple[float, float, float, float]:
    """
    Same corrected finite-branch background used by Gate F:
    r is the smallest positive real root of the cubic.
    xi = r + dr/dN, H_f = H/r.
    """
    Mf2 = p.mu * p.Mg2
    Me2 = meff2(p)
    kap = p.Mg2 / Mf2

    rho = p.rho0 * a ** -3
    rho_tilde = rho / (p.m2 * Me2 * p.Fbar)

    coeff = [
        kap * p.beta4 - 3.0 * p.beta2,
        -3.0 * p.beta1,
        3.0 * kap * p.beta2 - p.beta0 - rho_tilde,
        kap * p.beta1,
    ]
    roots = np.roots(coeff)
    real_pos = sorted(
        z.real for z in roots
        if abs(z.imag) < 1e-9 and z.real > 1e-12
    )
    if not real_pos:
        raise RuntimeError(f"no positive finite-branch root at a={a}")

    r = real_pos[0]

    dW = (
        kap * (2.0 * p.beta4 * r - p.beta1 / r**2)
        - 3.0 * p.beta1
        - 6.0 * p.beta2 * r
    )
    if abs(dW) < 1e-14:
        raise RuntimeError("background derivative singular")

    drdN = -3.0 * rho_tilde / dW
    xi = r + drdN

    Vf = (
        p.beta4
        + 3.0 * p.beta3 / r
        + 3.0 * p.beta2 / r**2
        + p.beta1 / r**3
    )
    H2 = p.m2 * Me2 * p.Fbar * r**2 * Vf / (3.0 * Mf2)
    if H2 <= 0 or xi <= 0:
        raise RuntimeError(f"invalid background at a={a}: H2={H2}, xi={xi}")

    H = math.sqrt(H2)
    Hf = H / r
    return r, xi, H, Hf


def tensor_mass_exact(a: float, r: float, xi: float, p: Params) -> float:
    """
    Exact m_T^2 from derivations/code/02_setor_tensorial_mT2.py:

      m_T^2 =
      F M_eff^2 m^2 (M_f^2 b^3 + M_g^2 a^3 xi)
      (a beta1 + a beta2 xi + b beta2 + b beta3 xi)
      / (M_f^2 M_g^2 a^2 b^2)

    with b = r a.
    """
    b = r * a
    Mf2 = p.mu * p.Mg2
    Me2 = meff2(p)

    num = (
        p.Fbar * Me2 * p.m2
        * (Mf2 * b**3 + p.Mg2 * a**3 * xi)
        * (a * p.beta1 + a * p.beta2 * xi + b * p.beta2 + b * p.beta3 * xi)
    )
    den = Mf2 * p.Mg2 * a**2 * b**2
    return num / den


def fundamental_lambda3_scales(p: Params) -> tuple[float, float, float]:
    """
    Candidate Lambda_3 normalizations built from *bare action parameters*.

    We intentionally print three Planck-mass conventions instead of silently
    choosing one:
        L3_g   = (m^2 M_g)^(1/3)
        L3_f   = (m^2 M_f)^(1/3)
        L3_eff = (m^2 M_eff)^(1/3)

    Here M_g = sqrt(M_g^2), etc.
    Which one is the physically relevant decoupling-limit normalization must
    follow from the explicit bimetric helicity/Stueckelberg derivation.
    """
    Mf2 = p.mu * p.Mg2
    Me2 = meff2(p)
    Mg = math.sqrt(p.Mg2)
    Mf = math.sqrt(Mf2)
    Me = math.sqrt(Me2)
    return (
        cube_root_pos(p.m2 * Mg),
        cube_root_pos(p.m2 * Mf),
        cube_root_pos(p.m2 * Me),
    )


def gate_f_omega_over_H(beta1: float) -> float:
    """
    Official Gate F-b late settled values.
    Keep this mapping explicit and fail on other beta1 values.
    """
    known = {1.0: 12.0, 4.47: 7.4}
    for key, value in known.items():
        if abs(beta1 - key) < 1e-9:
            return value
    raise ValueError(
        f"No official omega0/H stored for beta1={beta1}. "
        "Pass only beta1=1 or 4.47, or extend this function from a validated run."
    )


def evaluate(beta1: float, a: float, base: Params) -> Point:
    p = Params(**{**asdict(base), "beta1": beta1})
    r, xi, H, Hf = finite_branch_background(a, p)
    mt2 = tensor_mass_exact(a, r, xi, p)

    omh = gate_f_omega_over_H(beta1)
    omega = omh * H

    Lg, Lf, Leff = fundamental_lambda3_scales(p)
    # This is the old proxy, kept only for direct comparison:
    LmTg = cube_root_pos(abs(mt2) * math.sqrt(p.Mg2))

    return Point(
        a=a, r=r, xi=xi, H=H, Hf=Hf, mT2=mt2,
        omega0_over_H=omh, omega0=omega,
        Lambda3_g=Lg, Lambda3_f=Lf, Lambda3_eff=Leff,
        Lambda3_mT_g=LmTg,
        omega_over_L3g=omega / Lg,
        omega_over_L3f=omega / Lf,
        omega_over_L3eff=omega / Leff,
        omega_over_L3mTg=omega / LmTg,
    )


def verdict(points: list[Point], nonlinear: float | None) -> list[str]:
    lines = []
    lines.append("R6-ACTION: PASS — fundamental action scales evaluated without m_T substitution.")
    lines.append("R6-TENSOR: PASS — exact cosmological m_T^2 formula evaluated independently.")
    lines.append("R6-SCALAR: PASS — omega_0/H imported only from validated Gate F-b anchors.")

    if nonlinear is None:
        lines.append(
            "R6-NONLINEAR: NOT RUN — no cubic/Stueckelberg scale supplied."
        )
        lines.append(
            "R6-RIGOROUS: OPEN — quadratic data alone cannot establish the nonlinear cutoff."
        )
    else:
        ratios = [p.omega0 / nonlinear for p in points]
        lines.append(
            f"R6-NONLINEAR: SUPPLIED — Lambda_nl={nonlinear:.8g}; "
            f"omega/Lambda_nl={', '.join(f'{x:.3g}' for x in ratios)}"
        )
        if all(x > 1.0 for x in ratios):
            lines.append(
                "R6-RIGOROUS: CONDITIONAL PASS — the canonical branch lies above "
                "the independently supplied nonlinear scale at both anchors."
            )
        else:
            lines.append(
                "R6-RIGOROUS: FAIL/OPEN — at least one anchor is not above the "
                "independently supplied nonlinear scale."
            )
    return lines


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--a", type=float, default=75000.0,
                    help="late-time anchor scale factor used for the background")
    ap.add_argument("--beta1", type=float, action="append",
                    help="Gate-F beta1 anchor; default: 1 and 4.47")
    ap.add_argument("--lambda-nonlinear", type=float, default=None,
                    help="independently derived nonlinear strong-coupling scale")
    ap.add_argument("--lambda-nonlinear-label", default="external nonlinear derivation")
    args = ap.parse_args()

    betas = args.beta1 or [1.0, 4.47]
    base = Params()

    pts = [evaluate(b, args.a, base) for b in betas]

    out = []
    out.append("=" * 92)
    out.append("R6 — STRONG-COUPLING / CUTOFF CONSISTENCY AUDIT")
    out.append("=" * 92)
    out.append("")
    out.append(
        "IMPORTANT: Lambda3_g/f/eff use the bare mass parameter m^2 from the action. "
        "Lambda3_mT_g is printed only as the OLD cosmological tensor-mass proxy."
    )
    out.append("")

    hdr = (
        f"{'b1':>6} {'r':>9} {'xi':>9} {'H':>10} {'mT2':>11} "
        f"{'om/H':>7} {'om':>10} {'L3g':>9} {'L3f':>9} {'L3eff':>9} {'L3(mT)':>9}"
    )
    out.append(hdr)
    for p in pts:
        out.append(
            f"{next(b for b in betas if abs(gate_f_omega_over_H(b)-p.omega0_over_H)<1e-12):6.2f} "
            f"{p.r:9.5f} {p.xi:9.5f} {p.H:10.5g} {p.mT2:11.5g} "
            f"{p.omega0_over_H:7.2f} {p.omega0:10.5g} "
            f"{p.Lambda3_g:9.5g} {p.Lambda3_f:9.5g} "
            f"{p.Lambda3_eff:9.5g} {p.Lambda3_mT_g:9.5g}"
        )
    out.append("")
    out.append("omega / cutoff candidates:")
    for b, p in zip(betas, pts):
        out.append(
            f"  beta1={b:g}: "
            f"omega/L3_g={p.omega_over_L3g:.4g}, "
            f"omega/L3_f={p.omega_over_L3f:.4g}, "
            f"omega/L3_eff={p.omega_over_L3eff:.4g}, "
            f"omega/L3(mT proxy)={p.omega_over_L3mTg:.4g}"
        )
    out.append("")
    if args.lambda_nonlinear is not None:
        out.append(
            f"independent nonlinear scale: {args.lambda_nonlinear_label} = "
            f"{args.lambda_nonlinear:.8g}"
        )
    out.extend(verdict(pts, args.lambda_nonlinear))

    print("\n".join(out))

    outdir = Path("auditoria/code/out")
    outdir.mkdir(parents=True, exist_ok=True)
    (outdir / "r6_cutoff_consistency.txt").write_text("\n".join(out) + "\n", encoding="utf-8")
    payload = {
        "points": [asdict(p) for p in pts],
        "lambda_nonlinear": args.lambda_nonlinear,
        "lambda_nonlinear_label": args.lambda_nonlinear_label,
        "verdict": verdict(pts, args.lambda_nonlinear),
    }
    (outdir / "r6_cutoff_consistency.json").write_text(
        json.dumps(payload, indent=2), encoding="utf-8"
    )


if __name__ == "__main__":
    main()
