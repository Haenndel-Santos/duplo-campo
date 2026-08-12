
# -*- coding: utf-8 -*-
"""R6-F2 — boundary-safe kinetic signature map, grid extended around analysis domain."""
from __future__ import annotations
import importlib.util, json, math, time
from pathlib import Path
import numpy as np
from scipy.interpolate import CubicSpline

spec=importlib.util.spec_from_file_location("F0","/mnt/data/r6f0_dynamic_adm_null_gate.py")
F0=importlib.util.module_from_spec(spec);spec.loader.exec_module(F0)
specF=importlib.util.spec_from_file_location("F","/mnt/data/r6f_dynamic_r4b_reaudit.py")
F=importlib.util.module_from_spec(specF);specF.loader.exec_module(F)

OUT=[];T0=time.time()
def say(*a):
    s=" ".join(str(x) for x in a);print(f"[{time.time()-T0:7.2f}s] {s}");OUT.append(s)

def load_bg():
    d=np.load("/mnt/data/r6f0_out/rolling_background.npz")
    rec={q:d[q] for q in d.files}
    spl={q:CubicSpline(rec["N"],rec[q]) for q in rec if q not in ("N","a")}
    return rec,spl

def build_ext(funs,spl,kc,npts=7000):
    Ns=np.linspace(np.log(10.),np.log(1e5),npts);aa=np.exp(Ns)
    Hs=np.array([float(spl["H"](N)) for N in Ns])
    K3=np.zeros((npts,3,3));C3=np.zeros_like(K3);W3=np.zeros_like(K3)
    row=np.zeros(npts);er=np.zeros(npts)
    for p,N in enumerate(Ns):
        (K,C,W),v=F.mats_at(funs,spl,N,kc)
        Wxx=W[np.ix_(F0.XIDX,F0.XIDX)];Cqx=C[np.ix_(F0.QIDX,F0.XIDX)]
        Wqx=W[np.ix_(F0.QIDX,F0.XIDX)];Wxq=W[np.ix_(F0.XIDX,F0.QIDX)]
        Kqq=K[np.ix_(F0.QIDX,F0.QIDX)];Cqq=C[np.ix_(F0.QIDX,F0.QIDX)];Wqq=W[np.ix_(F0.QIDX,F0.QIDX)]
        sc=np.linalg.solve(Wxx,Cqx.T);sw=np.linalg.solve(Wxx,Wxq)
        K3[p]=.5*((Kqq+Cqx@sc)+(Kqq+Cqx@sc).T)
        C3[p]=Cqq-Cqx@sw
        W3[p]=.5*((Wqq-Wqx@sw)+(Wqq-Wqx@sw).T)
        es=np.linalg.eigvalsh(K3[p]);er[p]=np.min(abs(es))/max(np.max(abs(es)),1e-300)
        row[p]=np.linalg.norm(K3[p][0,:])/max(np.linalg.norm(K3[p]),1e-300)
    return Ns,aa,Hs,K3,C3,W3,row,er

def fj_all(Ns,Hs,K3,C3,W3):
    n=len(Ns);Kz=K3.copy();Kz[:,0,:]=0;Kz[:,:,0]=0
    Cdot=np.gradient(C3,Ns,axis=0,edge_order=2)*Hs[:,None,None]
    K2=np.zeros((n,2,2));C2=np.zeros_like(K2);W2=np.zeros_like(K2);aux=np.zeros(n)
    for p in range(n):
        Kp=Kz[p].copy();Cp=C3[p].copy();Wp=W3[p].copy()
        for j in range(3):
            cij=Cp[0,j];cd=Cdot[p,0,j]
            if j==0:Wp[0,0]+=cd
            else:Wp[0,j]+=cd;Wp[j,0]+=cd;Cp[j,0]-=cij
            Cp[0,j]=0
        w=Wp[0,0];aux[p]=w;keep=[1,2];cx=Cp[np.ix_(keep,[0])];wx=Wp[np.ix_(keep,[0])]
        K2[p]=Kp[np.ix_(keep,keep)]+cx@cx.T/w
        C2[p]=Cp[np.ix_(keep,keep)]-cx@Wp[np.ix_([0],keep)]/w
        W2[p]=Wp[np.ix_(keep,keep)]-wx@Wp[np.ix_([0],keep)]/w
        K2[p]=.5*(K2[p]+K2[p].T)
    return K2,aux

def main():
    out=Path("/mnt/data/r6f2_out");out.mkdir(exist_ok=True)
    syms,L2,K,C,W,funs=F0.build_dynamic();rec,spl=load_bg()
    results=[]
    for ac in F.A_CROSS:
        kc=ac*float(spl["H"](math.log(ac)))
        Ns,aa,Hs,K3,C3,W3,row,er=build_ext(funs,spl,kc)
        K2,aux=fj_all(Ns,Hs,K3,C3,W3)
        ev,vec=np.linalg.eigh(K2)
        mask=(aa>=20)&(aa<=80000)
        neg=(ev[:,0]<0)&mask
        idx=np.where(neg)[0]
        rel=ev[:,0]/np.maximum(np.max(abs(ev),axis=1),1e-300)
        r=dict(across=ac,negative_points=int(neg.sum()),analysis_points=int(mask.sum()),
               min_rel=float(rel[mask].min()),min_eig=float(ev[mask,0].min()),
               nullrow_max=float(row[mask].max()),nulleig_max=float(er[mask].max()),
               auxmin=float(np.min(abs(aux[mask]))))
        if len(idx):
            p=idx[np.argmin(rel[idx])]
            r["worst"]=dict(a=float(aa[p]),kh=float(kc/(aa[p]*Hs[p])),
                            rel=float(rel[p]),eigs=ev[p].tolist(),vec=np.abs(vec[p,:,0]).tolist())
        results.append(r)
        say(f"[cross={ac:6.0f}] negatives={r['negative_points']}/{r['analysis_points']}; "
            f"minrel={r['min_rel']:+.3e}; nullrow={r['nullrow_max']:.1e}; auxmin={r['auxmin']:.3e}"
            + (f"; worst={r['worst']}" if 'worst' in r else ""))
    (out/"r6f2_result.json").write_text(json.dumps(results,indent=2),encoding="utf-8")
    (out/"r6f2_output.txt").write_text("\n".join(OUT)+"\n",encoding="utf-8")
if __name__=="__main__":main()
