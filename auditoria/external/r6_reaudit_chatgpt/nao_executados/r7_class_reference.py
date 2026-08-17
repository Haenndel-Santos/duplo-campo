# -*- coding: utf-8 -*-
"""
r7_class_reference.py
=====================

Runs an unmodified CLASS reference cosmology and stores the quantities that a
future TDCP-CLASS backend MUST reproduce in the GR limit.

Requirements
------------
Clone/build CLASS and install its Python wrapper (`classy`) in the same venv.

Example:
    git clone https://github.com/lesgourg/class_public external/class_public
    cd external/class_public
    make -j
    cd ../..
    python auditoria/code/r7_class_reference.py

Outputs
-------
    auditoria/code/out/r7_class_reference.npz
    auditoria/code/out/r7_class_reference.json

This script does NOT implement TDCP.  It is the regression/validation anchor.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

try:
    from classy import Class
except Exception as exc:
    raise SystemExit(
        "Could not import classy. Build/install the official CLASS Python wrapper first.\n"
        f"Original error: {exc}"
    )


DEFAULT = {
    "h": 0.674,
    "omega_b": 0.02237,
    "omega_cdm": 0.1200,
    "A_s": 2.10e-9,
    "n_s": 0.965,
    "tau_reio": 0.054,
    "N_ur": 3.046,
    "T_cmb": 2.7255,
    "output": "tCl,pCl,lCl,mPk,dTk",
    "lensing": "yes",
    "l_max_scalars": 2500,
    "P_k_max_h/Mpc": 20.0,
    "z_max_pk": 20.0,
    "gauge": "newtonian",
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lmax", type=int, default=2500)
    args = ap.parse_args()

    pars = dict(DEFAULT)
    pars["l_max_scalars"] = args.lmax

    cosmo = Class()
    cosmo.set(pars)
    cosmo.compute()

    cl_raw = cosmo.raw_cl(args.lmax)
    cl_lensed = cosmo.lensed_cl(args.lmax)
    bg = cosmo.get_background()
    th = cosmo.get_thermodynamics()

    outdir = Path("auditoria/code/out")
    outdir.mkdir(parents=True, exist_ok=True)

    np.savez_compressed(
        outdir / "r7_class_reference.npz",
        ell=np.asarray(cl_raw["ell"]),
        tt_raw=np.asarray(cl_raw["tt"]),
        ee_raw=np.asarray(cl_raw["ee"]),
        te_raw=np.asarray(cl_raw["te"]),
        pp_raw=np.asarray(cl_raw.get("pp", np.zeros_like(cl_raw["ell"], dtype=float))),
        tt_lensed=np.asarray(cl_lensed["tt"]),
        ee_lensed=np.asarray(cl_lensed["ee"]),
        te_lensed=np.asarray(cl_lensed["te"]),
        bg_z=np.asarray(bg["z"]),
        bg_H=np.asarray(bg["H [1/Mpc]"]),
        th_z=np.asarray(th["z"]),
        th_xe=np.asarray(th["x_e"]),
    )

    meta = {
        "parameters": pars,
        "gr_gate": {
            "description": (
                "This file is the numerical anchor for the TDCP CLASS fork. "
                "With TDCP interaction disabled, TT/TE/EE and background must "
                "agree with this run to the chosen tolerance."
            ),
            "recommended_tolerance_fraction": 1e-4,
        },
    }
    (outdir / "r7_class_reference.json").write_text(
        json.dumps(meta, indent=2), encoding="utf-8"
    )

    print("saved:")
    print(" ", outdir / "r7_class_reference.npz")
    print(" ", outdir / "r7_class_reference.json")

    cosmo.struct_cleanup()
    cosmo.empty()


if __name__ == "__main__":
    main()
