# -*- coding: utf-8 -*-
"""
r7_isw_from_transfer.py
=======================

Independent low-l ISW validator.

Input
-----
An .npz transfer file on a rectangular grid with:

    k_Mpc          shape (Nk,)
    eta_Mpc        shape (Nt,)
    PhiB           shape (Nk,Nt)   # Bardeen/Newtonian spatial potential
    PsiB           shape (Nk,Nt)   # Bardeen/Newtonian lapse potential
    P_R            shape (Nk,)     # dimensionless primordial curvature spectrum
    eta0_Mpc       scalar

Optional:
    visibility      shape (Nt,)    # if present, can mask pre-recombination region

The late ISW temperature transfer is computed as

    Delta_l^ISW(k) = integral d eta [PhiB' + PsiB'] j_l[k(eta0-eta)]

up to the potential-sign convention used by the backend.  The GR gate MUST
verify the sign and normalization.

Then

    C_l^ISW = 4 pi integral d ln k P_R(k) |Delta_l^ISW(k)|^2 .

Why this exists
---------------
CLASS remains the authoritative full Boltzmann calculation.  This script is an
independent check of the specific R-5 claim that the TDCP late-time band
enhances low-l ISW.  If CLASS and this direct integral disagree badly, do not
interpret the TDCP C_l result until the convention/source mismatch is found.

It also contains the flat-g -> Bardeen reconstruction used by the future
backend.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
from scipy.integrate import simpson
from scipy.special import spherical_jn


def flat_g_to_bardeen(A, B, a, H, Bdot):
    """
    Metric convention:
      ds^2 = -(1+2A) dt^2 + 2 a d_i B dt dx^i
             + a^2[(1-2 psi)delta_ij + 2 d_i d_j E] dx^i dx^j

    Starting from flat-g gauge psi=E=0 and choosing Newtonian gauge B_N=E_N=0:

      Psi_B = A + d(aB)/dt = A + a(H B + Bdot)
      Phi_B = -a H B

    IMPORTANT: the sign convention must be fixed by a GR comparison before
    scientific use.
    """
    PsiB = A + a * (H * B + Bdot)
    PhiB = -a * H * B
    return PhiB, PsiB


def late_isw_cl(data, lmin=2, lmax=30, eta_min=None):
    k = np.asarray(data["k_Mpc"], float)
    eta = np.asarray(data["eta_Mpc"], float)
    Phi = np.asarray(data["PhiB"], float)
    Psi = np.asarray(data["PsiB"], float)
    PR = np.asarray(data["P_R"], float)
    eta0 = float(np.asarray(data["eta0_Mpc"]).reshape(()))

    if Phi.shape != (k.size, eta.size) or Psi.shape != Phi.shape:
        raise ValueError("PhiB/PsiB must have shape (Nk,Nt)")
    if PR.shape != (k.size,):
        raise ValueError("P_R must have shape (Nk,)")

    if eta_min is None:
        # Default to the latest 40% of conformal time: intentionally only late ISW.
        eta_min = eta[0] + 0.60 * (eta0 - eta[0])

    mask = eta >= eta_min
    et = eta[mask]
    if et.size < 5:
        raise ValueError("too few eta points after late-time mask")

    pot_sum = Phi[:, mask] + Psi[:, mask]
    dpot_deta = np.gradient(pot_sum, et, axis=1, edge_order=2)

    ells = np.arange(lmin, lmax + 1)
    cls = np.zeros_like(ells, dtype=float)

    ln_k = np.log(k)
    for ii, ell in enumerate(ells):
        Dl = np.zeros(k.size)
        for ik, kval in enumerate(k):
            x = kval * (eta0 - et)
            source = dpot_deta[ik] * spherical_jn(int(ell), x)
            Dl[ik] = simpson(source, x=et)
        integrand = PR * Dl**2
        cls[ii] = 4.0 * np.pi * simpson(integrand, x=ln_k)
    return ells, cls


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("transfer_npz")
    ap.add_argument("--lmin", type=int, default=2)
    ap.add_argument("--lmax", type=int, default=30)
    ap.add_argument("--eta-min", type=float, default=None)
    args = ap.parse_args()

    data = np.load(args.transfer_npz)
    ell, cl = late_isw_cl(data, args.lmin, args.lmax, args.eta_min)

    out = Path("auditoria/code/out/r7_isw_direct.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    lines = ["# ell   C_ell_ISW"] + [f"{l:4d} {c:.12e}" for l, c in zip(ell, cl)]
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    print("saved:", out)


if __name__ == "__main__":
    main()
