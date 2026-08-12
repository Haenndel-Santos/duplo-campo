
# -*- coding: utf-8 -*-
"""R6-G — boundary-safe full rolling R4b passage re-audit."""
from __future__ import annotations
import importlib.util, json, math, time, os
from pathlib import Path
import numpy as np

spec=importlib.util.spec_from_file_location("F","/mnt/data/r6f_dynamic_r4b_reaudit.py")
F=importlib.util.module_from_spec(spec);spec.loader.exec_module(F)
spec0=importlib.util.spec_from_file_location("F0","/mnt/data/r6f0_dynamic_adm_null_gate.py")
F0=importlib.util.module_from_spec(spec0);spec0.loader.exec_module(F0)
spec2=importlib.util.spec_from_file_location("F2","/mnt/data/r6f2_boundary_safe_kinetic_map.py")
F2=importlib.util.module_from_spec(spec2);spec2.loader.exec_module(F2)

NPTS=int(os.environ.get("R6G_NPTS","7000"))
OUT=[];T0=time.time()
def say(*a):
    s=" ".join(str(x) for x in a);print(f"[{time.time()-T0:7.2f}s] {s}");OUT.append(s)

def fj_recon(Ns,Hs,K3,C3,W3):
    n=len(Ns);Kz=K3.copy();Kz[:,0,:]=0;Kz[:,:,0]=0
    Cdot=np.gradient(C3,Ns,axis=0,edge_order=2)*Hs[:,None,None]
    K2=np.zeros((n,2,2));C2=np.zeros_like(K2);W2=np.zeros_like(K2)
    av=np.zeros((n,2));aq=np.zeros((n,2));aux=np.zeros(n)
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
        K2[p]=.5*(K2[p]+K2[p].T);W2[p]=.5*(W2[p]+W2[p].T)
        av[p]=Cp[keep,0]/w;aq[p]=-Wp[0,keep]/w
    avd=np.gradient(av,Ns,axis=0,edge_order=2)*Hs[:,None]
    aqd=np.gradient(aq,Ns,axis=0,edge_order=2)*Hs[:,None]
    return K2,C2,W2,av,aq,avd,aqd,aux

def deriv(Ns,Hs,K,C):
    return (np.gradient(K,Ns,axis=0,edge_order=2)*Hs[:,None,None],
            np.gradient(C,Ns,axis=0,edge_order=2)*Hs[:,None,None])

def accel(p,y,v,K,C,W,Kd,Cd):
    return -np.linalg.solve(K[p],(Kd[p]+C[p]-C[p].T)@v+(Cd[p]+W[p])@y)

def psistate(p,y,v,K,C,W,Kd,Cd,av,aq,avd,aqd):
    ac=accel(p,y,v,K,C,W,Kd,Cd)
    ps=float(av[p]@v+aq[p]@y)
    psd=float(avd[p]@v+av[p]@ac+aqd[p]@y+aq[p]@v)
    return ps,psd

def integ(p0,p1,Ns,Hs,K,C,W,Kd,Cd,y,v):
    y=y.copy();v=v.copy()
    for p in range(p0,p1):
        dt=(Ns[p+1]-Ns[p])/Hs[p]
        Ki=np.linalg.inv(K[p]);A=Kd[p]+C[p]-C[p].T;B=Cd[p]+W[p]
        def rhs(yy,vv):return -Ki@(A@vv+B@yy)
        k1y,k1v=v,rhs(y,v)
        k2y,k2v=v+.5*dt*k1v,rhs(y+.5*dt*k1y,v+.5*dt*k1v)
        k3y,k3v=v+.5*dt*k2v,rhs(y+.5*dt*k2y,v+.5*dt*k2v)
        k4y,k4v=v+dt*k3v,rhs(y+dt*k3y,v+dt*k3v)
        y=y+dt*(k1y+2*k2y+2*k3y+k4y)/6
        v=v+dt*(k1v+2*k2v+2*k3v+k4v)/6
        if not np.all(np.isfinite(y)) or not np.all(np.isfinite(v)):raise RuntimeError("nonfinite")
    return y,v

def metric(p,y,v,K,C,W,Kd,Cd,av,aq,avd,aqd):
    ps,psd=psistate(p,y,v,K,C,W,Kd,Cd,av,aq,avd,aqd)
    return math.sqrt(ps*ps+psd*psd+y[0]**2+v[0]**2),ps,psd

def Xorig(funs,spl,N,kc,q,qd):
    (K,C,W),vv=F.mats_at(funs,spl,N,kc)
    Wxx=W[np.ix_(F0.XIDX,F0.XIDX)];Cqx=C[np.ix_(F0.QIDX,F0.XIDX)];Wxq=W[np.ix_(F0.XIDX,F0.QIDX)]
    return np.linalg.solve(Wxx,Cqx.T@qd-Wxq@q)

def run(ac,funs,spl):
    kc=ac*float(spl["H"](math.log(ac)))
    Ns,aa,Hs,K3,C3,W3,row,er=F2.build_ext(funs,spl,kc,NPTS)
    K2,C2,W2,av,aq,avd,aqd,aux=fj_recon(Ns,Hs,K3,C3,W3)
    ev=np.linalg.eigvalsh(K2);mask=(aa>=20)&(aa<=80000)
    if np.any(ev[mask]<=0):raise RuntimeError("nonpositive K2 in analysis domain")
    Kd,Cd=deriv(Ns,Hs,K2,C2)
    kh=kc/(aa*Hs);pstart=int(np.where(aa>=20)[0][0])
    i20=np.where((np.arange(len(aa))>=pstart)&(kh<=20))[0]
    i02=np.where((np.arange(len(aa))>=pstart)&(kh<=.2))[0]
    if not len(i20) or not len(i02) or i02[0]>np.where(aa<=80000)[0][-1]:
        return dict(across=ac,npts=NPTS,complete=False)
    p20,p02=int(i20[0]),int(i02[0])
    ics=[("Ef_pos",np.array([1.,0.]),np.zeros(2),True),
         ("Ef_vel",np.zeros(2),np.array([1.,0.]),True),
         ("chi_pos",np.array([0.,1.]),np.zeros(2),False),
         ("chi_vel",np.zeros(2),np.array([0.,1.]),False)]
    vals=[]
    for name,y,v,mi in ics:
        y,v=integ(pstart,p20,Ns,Hs,K2,C2,W2,Kd,Cd,y,v)
        n0,ps0,psd0=metric(p20,y,v,K2,C2,W2,Kd,Cd,av,aq,avd,aqd)
        q0=np.array([ps0,y[0],y[1]]);qd0=np.array([psd0,v[0],v[1]])
        X0=Xorig(funs,spl,Ns[p20],kc,q0,qd0)
        y,v=integ(p20,p02,Ns,Hs,K2,C2,W2,Kd,Cd,y,v)
        n1,ps1,psd1=metric(p02,y,v,K2,C2,W2,Kd,Cd,av,aq,avd,aqd)
        q1=np.array([ps1,y[0],y[1]]);qd1=np.array([psd1,v[0],v[1]])
        X1=Xorig(funs,spl,Ns[p02],kc,q1,qd1)
        ln=math.log(max(n1,1e-300))-math.log(max(n0,1e-300))
        lp=math.log(max(abs(X1[0]),1e-300))-math.log(max(abs(X0[0]),1e-300))
        vals.append(dict(ic=name,is_metric=mi,ln_metric=ln,ln_Phi_g=lp,
                         n0=n0,n1=n1,Phi0=float(X0[0]),Phi1=float(X1[0])))
    return dict(across=ac,npts=NPTS,complete=True,
                metricmax=max(x["ln_metric"] for x in vals if x["is_metric"]),
                allmax=max(x["ln_metric"] for x in vals),
                phimax=max(x["ln_Phi_g"] for x in vals),
                values=vals,old=F.OLD[ac],Kmin=float(ev[mask].min()),
                nullrow=float(row[mask].max()),nulleig=float(er[mask].max()),
                auxmin=float(np.min(abs(aux[mask]))),
                a20=float(aa[p20]),a02=float(aa[p02]))

def main():
    out=Path(f"/mnt/data/r6g_out_{NPTS}");out.mkdir(exist_ok=True)
    syms,L2,K,C,W,funs=F0.build_dynamic();rec,spl=F.load_bg()
    res=[]
    for ac in F.A_CROSS:
        r=run(ac,funs,spl);res.append(r)
        if r["complete"]:
            say(f"[cross {ac:6.0f}] Kmin={r['Kmin']:.3e}; lnA metric(Ef)={r['metricmax']:+.5f}; "
                f"all physical={r['allmax']:+.5f}; Phi_g max={r['phimax']:+.5f}; old={r['old']:+.2f}")
            for v in r["values"]:
                say(f"   {v['ic']:8s}: ln metric={v['ln_metric']:+.5f}, ln Phi_g={v['ln_Phi_g']:+.5f}")
        else:say(f"[cross {ac:6.0f}] passage incomplete")
    (out/"r6g_result.json").write_text(json.dumps(res,indent=2),encoding="utf-8")
    (out/"r6g_output.txt").write_text("\n".join(OUT)+"\n",encoding="utf-8")
if __name__=="__main__":main()
