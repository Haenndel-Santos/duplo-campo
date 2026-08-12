
# -*- coding: utf-8 -*-
"""
R6-D — reexecucao R4b no sistema ADM/FJ fisico de 2 DOF.

Compara a passagem kh=20 -> 0.2 em:
  (a) norma metrica historica do R4b, agora somente com ICs fisicas;
  (b) ganho maximo (SVD) no estado canonico positivo [x, xdot/H].

Q fisico apos constraints: y=(E_f, dchi).
Psi_f e reconstruida algebricamente da constraint secundaria.

Nao usa o antigo terceiro modo nem qualquer cutoff.
"""
from __future__ import annotations
import importlib.util, json, math, time
from pathlib import Path
import numpy as np
from scipy.linalg import eig

spec=importlib.util.spec_from_file_location("r6c","/mnt/data/r6c_gatef_adm_reaudit.py")
R=importlib.util.module_from_spec(spec); spec.loader.exec_module(R)

OUT=[]; T0=time.time()
def say(*a):
    s=" ".join(str(x) for x in a)
    print(f"[{time.time()-T0:7.2f}s] {s}")
    OUT.append(s)

KH_EDGES=[40.,20.,10.,6.,4.,2.5,1.6,1.,.7,.45,.3,.2,.1]
KH_PASS=(20.,.2)

def fj_with_reconstruction(Ns,Hs,Kr,Cr,Wr):
    n=len(Ns)
    Kz=Kr.copy(); Kz[:,0,:]=0.; Kz[:,:,0]=0.
    Cdot=np.gradient(Cr,Ns,axis=0)*Hs[:,None,None]
    K2=np.zeros((n,2,2)); C2=np.zeros_like(K2); W2=np.zeros_like(K2)
    av=np.zeros((n,2)); aq=np.zeros((n,2)); auxW=np.zeros(n)
    for p in range(n):
        Kp=Kz[p].copy(); Cp=Cr[p].copy(); Wp=Wr[p].copy()
        # IPP na linha estruturalmente nula Psi_f (0).
        for j in range(3):
            cij=Cp[0,j]; cd=Cdot[p,0,j]
            if j==0:
                Wp[0,0]+=cd
            else:
                Wp[0,j]+=cd; Wp[j,0]+=cd; Cp[j,0]-=cij
            Cp[0,j]=0.
        w00=Wp[0,0]; auxW[p]=w00
        if abs(w00) < 1e-18: raise RuntimeError(f"W00=0 at p={p}")
        keep=[1,2]
        cx=Cp[np.ix_(keep,[0])]                 # 2x1 = C_{y,Psi}
        wx=Wp[np.ix_(keep,[0])]
        K2[p]=Kp[np.ix_(keep,keep)]+cx@cx.T/w00
        C2[p]=Cp[np.ix_(keep,keep)]-cx@Wp[np.ix_([0],keep)]/w00
        W2[p]=Wp[np.ix_(keep,keep)]-wx@Wp[np.ix_([0],keep)]/w00
        K2[p]=.5*(K2[p]+K2[p].T); W2[p]=.5*(W2[p]+W2[p].T)
        # Psi = av.y_dot + aq.y
        av[p]=Cp[keep,0]/w00
        aq[p]=-Wp[0,keep]/w00
    avd=np.gradient(av,Ns,axis=0)*Hs[:,None]
    aqd=np.gradient(aq,Ns,axis=0)*Hs[:,None]
    return K2,C2,W2,av,aq,avd,aqd,auxW

def derivatives(Ns,Hs,K,C,W):
    return (np.gradient(K,Ns,axis=0)*Hs[:,None,None],
            np.gradient(C,Ns,axis=0)*Hs[:,None,None])

def accel(p,y,v,K,C,W,Kd,Cd):
    return -np.linalg.solve(K[p], (Kd[p]+C[p]-C[p].T)@v+(Cd[p]+W[p])@y)

def metric_state(p,y,v,K,C,W,Kd,Cd,av,aq,avd,aqd,kc,H):
    a=accel(p,y,v,K,C,W,Kd,Cd)
    psi=float(av[p]@v+aq[p]@y)
    psid=float(avd[p]@v+av[p]@a+aqd[p]@y+aq[p]@v)
    Ef=float(y[0]); Efd=float(v[0])
    # historical R4b coordinate norm
    mh=np.array([psi,psid,Ef,Efd])
    # regularized metric norm (Y=k^2 E)
    mr=np.array([psi,psid/H,kc*kc*Ef,kc*kc*Efd/H])
    return mh,mr

def canonical_arrays(Ns,Hs,K,C,W):
    T,Td,Cc,Wc,Ccd,eta,evals=R.canonical_track(Ns,Hs,K,C,W)
    Ti=np.array([np.linalg.inv(x) for x in T])
    return T,Td,Ti,Cc,Wc,eta

def to_canonical_state(p,y,v,T,Td,Ti,H):
    x=Ti[p]@y
    xd=Ti[p]@(v-Td[p]@x)
    return np.concatenate([x,xd/H])

def from_canonical_state(p,u,T,Td,H):
    x=u[:2]; xd=H*u[2:]
    y=T[p]@x
    v=Td[p]@x+T[p]@xd
    return y,v

def integrate_segment(p0,p1,Ns,Hs,K,C,W,Kd,Cd,y0,v0,
                      av=None,aq=None,avd=None,aqd=None,kc=None,
                      metric_capture=False):
    y=y0.copy(); v=v0.copy()
    m0=mr0=None
    if metric_capture:
        m0,mr0=metric_state(p0,y,v,K,C,W,Kd,Cd,av,aq,avd,aqd,kc,Hs[p0])
    for p in range(p0,p1):
        dN=Ns[p+1]-Ns[p]; dt=dN/Hs[p]
        # local coefficients as in original R4b RK4
        Ki=np.linalg.inv(K[p]); A=Kd[p]+C[p]-C[p].T; B=Cd[p]+W[p]
        def rhs(yy,vv): return -Ki@(A@vv+B@yy)
        k1y,k1v=v,rhs(y,v)
        k2y,k2v=v+.5*dt*k1v,rhs(y+.5*dt*k1y,v+.5*dt*k1v)
        k3y,k3v=v+.5*dt*k2v,rhs(y+.5*dt*k2y,v+.5*dt*k2v)
        k4y,k4v=v+dt*k3v,rhs(y+dt*k3y,v+dt*k3v)
        y=y+dt*(k1y+2*k2y+2*k3y+k4y)/6
        v=v+dt*(k1v+2*k2v+2*k3v+k4v)/6
    if metric_capture:
        m1,mr1=metric_state(p1,y,v,K,C,W,Kd,Cd,av,aq,avd,aqd,kc,Hs[p1])
        return y,v,m0,m1,mr0,mr1
    return y,v

def kh_indices(Ns,Hs,kc):
    aa=np.exp(Ns); kh=kc/(aa*Hs)
    out={}
    for x in set(KH_EDGES)|set(KH_PASS):
        idx=np.where(kh<=x)[0]
        out[x]=int(idx[0]) if len(idx) and kh[0]>x and kh[-1]<x else None
    return kh,out

def frozen_identity(p,H,K,C,W,T,Cc,Wc):
    # canonical QEP with K=I, using actual connection-retaining Cc,Wc.
    modes=R.qep(np.eye(2),Cc[p],Wc[p])
    if not modes: return {}
    lams=np.array([m[0] for m in modes],complex)
    j=int(np.argmax(lams.real))
    lam,v=modes[j]
    vy=T[p]@v
    # Raw physical component indicators; report, don't interpret as invariant probabilities.
    ef=abs(vy[0]); dc=abs(vy[1])
    return dict(lambda_over_H=[float(lam.real/H),float(lam.imag/H)],
                raw_Ef_over_dchi=float(ef/max(dc,1e-300)),
                canonical_position=[float(np.real(v[0])),float(np.real(v[1]))],
                y_position_abs=[float(ef),float(dc)])

def run_case(symbols,Ks,Cs,Ws,funs,b1,npts):
    say(""); say("="*76); say(f"R6-D beta1={b1:g}, npts={npts}"); say("="*76)
    Ns,aa,kc,Hs,Kr,Cr,Wr,conds,bgs=R.build_track(funs,symbols,b1,npts)
    K2,C2,W2,av,aq,avd,aqd,auxW=fj_with_reconstruction(Ns,Hs,Kr,Cr,Wr)
    ev=np.linalg.eigvalsh(K2)
    say(f"[K] negatives={(ev<0).sum()}/{ev.size}; min={ev.min():.6e}; aux W no-zero={np.min(np.abs(auxW)):.3e}")

    Kd,Cd=derivatives(Ns,Hs,K2,C2,W2)
    T,Td,Ti,Cc,Wc,eta=canonical_arrays(Ns,Hs,K2,C2,W2)
    etaerr=float(np.max(np.abs(eta-np.eye(2))))
    kh,idx=kh_indices(Ns,Hs,kc)
    p20,p02=idx[20.],idx[.2]
    if p20 is None or p02 is None: raise RuntimeError("passage not covered")
    say(f"[PASS] a20={aa[p20]:.3f}, a0.2={aa[p02]:.3f}; kh actual={kh[p20]:.5f}->{kh[p02]:.5f}")

    # Historical-like physical metric ICs: only E_f position and E_f velocity
    # are independent metric ICs after Psi_f constraint removal.
    hist=[]
    ic_defs=[
        ("Ef_pos",np.array([1.,0.]),np.zeros(2)),
        ("Ef_vel",np.zeros(2),np.array([1.,0.])),
        ("dchi_pos",np.array([0.,1.]),np.zeros(2)),
        ("dchi_vel",np.zeros(2),np.array([0.,1.])),
    ]
    for name,y0,v0 in ic_defs:
        # As R4b, initialize at a=100 then compare the same trajectory at passage boundaries.
        # integrate to p20 first
        y,v=integrate_segment(0,p20,Ns,Hs,K2,C2,W2,Kd,Cd,y0,v0)
        y,v,m0,m1,mr0,mr1=integrate_segment(
            p20,p02,Ns,Hs,K2,C2,W2,Kd,Cd,y,v,av,aq,avd,aqd,kc,True)
        ln_hist=float(np.log(max(np.linalg.norm(m1),1e-300))-np.log(max(np.linalg.norm(m0),1e-300)))
        ln_reg=float(np.log(max(np.linalg.norm(mr1),1e-300))-np.log(max(np.linalg.norm(mr0),1e-300)))
        hist.append(dict(ic=name,lnA_metric_historical=ln_hist,lnA_metric_regularized=ln_reg,
                         norm0=float(np.linalg.norm(m0)),norm1=float(np.linalg.norm(m1))))
        say(f"[IC {name:9s}] lnA historical={ln_hist:+.5f}; regularized={ln_reg:+.5f}")
    metric_physical_max=max(x["lnA_metric_historical"] for x in hist if x["ic"].startswith("Ef_"))
    metric_all_max=max(x["lnA_metric_historical"] for x in hist)
    say(f"[R4b-like] max physical metric ICs (Ef only) = {metric_physical_max:+.5f}")
    say(f"[ALL physical basis ICs] max metric response = {metric_all_max:+.5f}")

    # Canonical finite-time transfer SVD: initialize at kh=20 with unit
    # u=[x,xdot/H], evolve to kh=.2, and read u_end.
    M=np.zeros((4,4))
    for j in range(4):
        u0=np.zeros(4); u0[j]=1.
        y0,v0=from_canonical_state(p20,u0,T,Td,Hs[p20])
        y1,v1=integrate_segment(p20,p02,Ns,Hs,K2,C2,W2,Kd,Cd,y0,v0)
        M[:,j]=to_canonical_state(p02,y1,v1,T,Td,Ti,Hs[p02])
    sv=np.linalg.svd(M,compute_uv=False)
    lnsv=np.log(sv)
    say(f"[CAN-SVD] singular values={sv}")
    say(f"[CAN-SVD] ln sigma_max={lnsv[0]:+.6f}; ln sigma_min={lnsv[-1]:+.6f}")

    # Window-by-window canonical SVD to localize the band.
    windows=[]
    for hi,lo in zip(KH_EDGES[:-1],KH_EDGES[1:]):
        pi,pf=idx[hi],idx[lo]
        if pi is None or pf is None: continue
        MM=np.zeros((4,4))
        for j in range(4):
            u=np.zeros(4); u[j]=1.
            y0,v0=from_canonical_state(pi,u,T,Td,Hs[pi])
            y1,v1=integrate_segment(pi,pf,Ns,Hs,K2,C2,W2,Kd,Cd,y0,v0)
            MM[:,j]=to_canonical_state(pf,y1,v1,T,Td,Ti,Hs[pf])
        ss=np.linalg.svd(MM,compute_uv=False)
        dtime=np.trapz(1/Hs[pi:pf+1],x=Ns[pi:pf+1])
        Hmid=Hs[(pi+pf)//2]
        rate=float(np.log(ss[0])/max(dtime*Hmid,1e-300))
        windows.append(dict(hi=hi,lo=lo,ln_smax=float(np.log(ss[0])),rate_over_Hmid=rate))
    say("[WINDOW canonical SVD]")
    for w in windows:
        say(f"  kh {w['hi']:>4g}->{w['lo']:<4g}: ln smax={w['ln_smax']:+.4f}, rate/H={w['rate_over_Hmid']:+.3f}")

    # Frozen growing-mode diagnostics around physical band and IR.
    ids=[]
    for target in [20,10,6,4,2.5,1.6,1,.7,.45,.3,.2,.1,.06]:
        ids0=np.where(kh<=target)[0]
        if not len(ids0): continue
        p=int(ids0[0])
        d=frozen_identity(p,Hs[p],K2,C2,W2,T,Cc,Wc)
        d.update(kh=float(kh[p]),a=float(aa[p]),target=target)
        ids.append(d)
    say("[FROZEN identity]")
    for d in ids:
        say(f"  kh={d['kh']:.3f}: Re/H={d.get('lambda_over_H',[float('nan')])[0]:+.3f}, "
            f"|Ef|/|dchi| raw={d.get('raw_Ef_over_dchi',float('nan')):.3e}")

    return dict(beta1=b1,npts=npts,kc=kc,eta_error=etaerr,K_negative=int((ev<0).sum()),
                passage_indices=[p20,p02],hist=hist,
                r4b_like_metric_physical_max=metric_physical_max,
                all_physical_metric_max=metric_all_max,
                canonical_singular_values=sv.tolist(),
                canonical_ln_smax=float(lnsv[0]),windows=windows,frozen_identity=ids)

def main():
    out=Path("/mnt/data/r6d_out"); out.mkdir(exist_ok=True)
    symbols,fields,vels,L2,K,C,W=R.build_symbolic_L2()
    funs=R.lambdas(symbols,K,C,W)
    results=[]
    for npts in (6000,12000):
        for b1 in (1.0,4.47):
            results.append(run_case(symbols,K,C,W,funs,b1,npts))
    # convergence
    conv=[]
    for b1 in (1.,4.47):
        lo=next(x for x in results if x["beta1"]==b1 and x["npts"]==6000)
        hi=next(x for x in results if x["beta1"]==b1 and x["npts"]==12000)
        conv.append(dict(beta1=b1,
                         d_lnS=hi["canonical_ln_smax"]-lo["canonical_ln_smax"],
                         d_metric=hi["r4b_like_metric_physical_max"]-lo["r4b_like_metric_physical_max"]))
    say(""); say("="*76); say("R6-D CONVERGENCE"); say("="*76)
    for c in conv: say(c)
    payload={"runs":results,"convergence":conv}
    (out/"r6d_result.json").write_text(json.dumps(payload,indent=2),encoding="utf-8")
    (out/"r6d_output.txt").write_text("\n".join(OUT)+"\n",encoding="utf-8")

if __name__=="__main__":
    main()
