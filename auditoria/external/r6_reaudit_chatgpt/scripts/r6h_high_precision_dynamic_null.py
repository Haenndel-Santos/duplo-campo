
# -*- coding: utf-8 -*-
"""R6-H — arbitrary precision Schur-null check on dynamic beta1(phi) action."""
from __future__ import annotations
import importlib.util, math, json
from pathlib import Path
import sympy as sp
import numpy as np
from scipy.interpolate import CubicSpline
import mpmath as mp

spec=importlib.util.spec_from_file_location("F0","/mnt/data/r6f0_dynamic_adm_null_gate.py")
F0=importlib.util.module_from_spec(spec);spec.loader.exec_module(F0)

def main():
    syms,L2,K,C,W,funs=F0.build_dynamic()
    d=np.load("/mnt/data/r6f0_out/rolling_background.npz")
    rec={q:d[q] for q in d.files}
    spl={q:CubicSpline(rec["N"],rec[q]) for q in rec if q not in ("N","a")}
    across=4000.;kc=across*float(spl["H"](math.log(across)))
    rows=[]
    for a0 in (100.,4000.,15000.):
        N=math.log(a0)
        vals={q:float(spl[q](N)) for q in ("r","xi","H","Hf","ch","chd","Ub","Up","Upp")}
        b1=F0.beta1(vals["ch"]); bp=F0.dbeta1(vals["ch"]); bpp=2.
        nums=(a0,vals["r"]*a0,vals["xi"],vals["H"],vals["Hf"],vals["Ub"],vals["Up"],
              vals["Upp"],vals["chd"],b1,bp,bpp)
        subs={s:sp.Float(v,85) for s,v in zip(syms,nums)}
        subs[F0.k]=sp.Float(kc,85)
        Kn=K.subs(subs).evalf(75);Cn=C.subs(subs).evalf(75);Wn=W.subs(subs).evalf(75)
        X=F0.XIDX;Q=F0.QIDX
        Wxx=Wn.extract(X,X); Cqx=Cn.extract(Q,X)
        Kq=(Kn.extract(Q,Q)+Cqx*Wxx.inv()*Cqx.T).evalf(70)
        mp.mp.dps=70
        Km=mp.matrix([[mp.mpf(str(sp.N(Kq[i,j],68))) for j in range(3)] for i in range(3)])
        ev,E=mp.eigsy(Km)
        eigs=[mp.nstr(ev[i],35) for i in range(3)]
        sc=max(abs(ev[i]) for i in range(3))
        j=min(range(3),key=lambda i:abs(ev[i]))
        rel=abs(ev[j])/sc
        row0=[sp.N(Kq[0,jj],55) for jj in range(3)]
        r=dict(a=a0,kh=kc/(a0*vals["H"]),chi=vals["ch"],beta1=b1,
               Krow0=[str(x) for x in row0],eigs=eigs,relative_null=mp.nstr(rel,30))
        rows.append(r)
        print("\nA=",a0,"kh=",r["kh"],"chi=",r["chi"],"beta1=",b1)
        print("K row Psi:",row0)
        print("eigenvalues:",eigs)
        print("relative null:",mp.nstr(rel,30))
    out=Path("/mnt/data/r6h_out");out.mkdir(exist_ok=True)
    (out/"r6h_result.json").write_text(json.dumps(rows,indent=2),encoding="utf-8")
if __name__=="__main__":main()
