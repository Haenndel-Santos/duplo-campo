
# -*- coding: utf-8 -*-
"""
R6-E — identify the remaining canonical growth and reconstruct g-sector multipliers
after exact ADM/FJ constraint reduction.
"""
from __future__ import annotations
import importlib.util, json, math, time
from pathlib import Path
import numpy as np

spec=importlib.util.spec_from_file_location("r6c","/mnt/data/r6c_gatef_adm_reaudit.py")
R=importlib.util.module_from_spec(spec); spec.loader.exec_module(R)
spec2=importlib.util.spec_from_file_location("r6d","/mnt/data/r6d_r4b_adm_passage.py")
D=importlib.util.module_from_spec(spec2); spec2.loader.exec_module(D)

T0=time.time(); OUT=[]
def say(*a):
    s=" ".join(str(x) for x in a); print(f"[{time.time()-T0:7.2f}s] {s}"); OUT.append(s)

def original_reconstruction_mats(funs,symbols,a,b1,kc):
    (K,C,W),f=R.eval_mats(funs,symbols,a,b1,kc)
    Wxx=W[np.ix_(R.XIDX,R.XIDX)]
    Cqx=C[np.ix_(R.QIDX,R.XIDX)]
    Wxq=W[np.ix_(R.XIDX,R.QIDX)]
    # X = A_v qdot + A_q q
    Av=np.linalg.solve(Wxx,Cqx.T)
    Aq=-np.linalg.solve(Wxx,Wxq)
    return Av,Aq,f

def integrate_capture(Ns,Hs,K,C,W,Kd,Cd,y0,v0,capture):
    y=y0.copy(); v=v0.copy(); out={}
    cap=set(capture)
    if 0 in cap: out[0]=(y.copy(),v.copy())
    for p in range(len(Ns)-1):
        dt=(Ns[p+1]-Ns[p])/Hs[p]
        Ki=np.linalg.inv(K[p]); A=Kd[p]+C[p]-C[p].T; B=Cd[p]+W[p]
        def rhs(yy,vv): return -Ki@(A@vv+B@yy)
        k1y,k1v=v,rhs(y,v)
        k2y,k2v=v+.5*dt*k1v,rhs(y+.5*dt*k1y,v+.5*dt*k1v)
        k3y,k3v=v+.5*dt*k2v,rhs(y+.5*dt*k2y,v+.5*dt*k2v)
        k4y,k4v=v+dt*k3v,rhs(y+dt*k3y,v+dt*k3v)
        y=y+dt*(k1y+2*k2y+2*k3y+k4y)/6
        v=v+dt*(k1v+2*k2v+2*k3v+k4v)/6
        if p+1 in cap: out[p+1]=(y.copy(),v.copy())
    return out

def q3_state(p,y,v,K2,C2,W2,Kd,Cd,av,aq,avd,aqd):
    a2=D.accel(p,y,v,K2,C2,W2,Kd,Cd)
    psi=float(av[p]@v+aq[p]@y)
    psid=float(avd[p]@v+av[p]@a2+aqd[p]@y+aq[p]@v)
    q=np.array([psi,y[0],y[1]])
    qd=np.array([psid,v[0],v[1]])
    return q,qd

def run(b1,npts,symbols,Ks,Cs,Ws,funs):
    say(""); say("="*78); say(f"R6-E beta1={b1:g}, npts={npts}"); say("="*78)
    Ns,aa,kc,Hs,Kr,Cr,Wr,conds,bgs=R.build_track(funs,symbols,b1,npts)
    K2,C2,W2,av,aq,avd,aqd,aux=D.fj_with_reconstruction(Ns,Hs,Kr,Cr,Wr)
    Kd,Cd=D.derivatives(Ns,Hs,K2,C2,W2)
    kh=kc/(aa*Hs)

    # Exact numerical decoupling check of dchi from Ef in final physical system.
    def rel_off(M):
        diag=np.maximum(np.max(np.abs(M),axis=(1,2)),1e-300)
        off=np.maximum(np.abs(M[:,0,1]),np.abs(M[:,1,0]))
        return off/diag
    offK=rel_off(K2); offC=rel_off(C2); offW=rel_off(W2)
    say(f"[DECOUPLE] max relative offdiag K={offK.max():.3e}, C={offC.max():.3e}, W={offW.max():.3e}")

    # Compare dchi EOM coefficients to healthy spectator:
    # dchi_ddot + 3H dchi_dot + [(k/a)^2+U''] dchi = 0.
    sample_targets=[20,4,1,.45,.2,.06]
    chi_checks=[]
    for target in sample_targets:
        p=int(np.argmin(abs(kh-target)))
        friction=(Kd[p,1,1]+C2[p,1,1]-C2[p,1,1])/K2[p,1,1]
        mass=(Cd[p,1,1]+W2[p,1,1])/K2[p,1,1]
        expected_m=(kc/aa[p])**2+R.UPP
        fr_rel=(friction-3*Hs[p])/max(abs(3*Hs[p]),1e-300)
        m_rel=(mass-expected_m)/max(abs(expected_m),1e-300)
        sig_pred=math.sqrt(max(0.,2.25-R.UPP/Hs[p]**2-kh[p]**2))
        phys_slow=-1.5+sig_pred
        chi_checks.append(dict(kh=float(kh[p]),friction_over_H=float(friction/Hs[p]),
                               mass_over_H2=float(mass/Hs[p]**2),
                               rel_friction=float(fr_rel),rel_mass=float(m_rel),
                               sigma_can_pred_over_H=float(sig_pred),
                               physical_slow_exp_over_H=float(phys_slow)))
    say("[CHI healthy-spectator EOM check]")
    for x in chi_checks:
        say(f"  kh={x['kh']:.3f}: friction/H={x['friction_over_H']:.8f}, "
            f"mass/H2={x['mass_over_H2']:.8f}, rel errs=({x['rel_friction']:.2e},{x['rel_mass']:.2e}), "
            f"sigma_can_pred/H={x['sigma_can_pred_over_H']:.4f}, phys slow/H={x['physical_slow_exp_over_H']:+.4f}")

    # Capture band marks plus passage boundaries for physical Ef ICs.
    targets=[20,10,6,4,2.5,1.6,1,.7,.5,.45,.3,.2]
    idx={t:int(np.argmin(abs(kh-t))) for t in targets}
    capture=sorted(set(idx.values()))
    trajectories={}
    for name,y0,v0 in [
        ("Ef_pos",np.array([1.,0.]),np.zeros(2)),
        ("Ef_vel",np.zeros(2),np.array([1.,0.])),
        ("dchi_pos",np.array([0.,1.]),np.zeros(2)),
        ("dchi_vel",np.zeros(2),np.array([0.,1.])),
    ]:
        trajectories[name]=integrate_capture(Ns,Hs,K2,C2,W2,Kd,Cd,y0,v0,capture)

    rows=[]
    for name,tr in trajectories.items():
        vals=[]
        for t in targets:
            p=idx[t]; y,v=tr[p]
            q,qd=q3_state(p,y,v,K2,C2,W2,Kd,Cd,av,aq,avd,aqd)
            Av,Aq,f=original_reconstruction_mats(funs,symbols,aa[p],b1,kc)
            X=Av@qd+Aq@q
            qm=math.sqrt(q[0]**2+q[1]**2+qd[0]**2+qd[1]**2)
            vals.append(dict(target=t,kh=float(kh[p]),a=float(aa[p]),Phi_g=float(X[0]),B_g=float(X[1]),
                             Phi_f=float(X[2]),B_f=float(X[3]),qmet=float(qm),
                             Ef=float(y[0]),dchi=float(y[1])))
        rows.append(dict(ic=name,values=vals))
        p20,p02=idx[20],idx[.2]
        v20=next(x for x in vals if x["target"]==20)
        v02=next(x for x in vals if x["target"]==.2)
        def dln(key):
            return math.log(max(abs(v02[key]),1e-300))-math.log(max(abs(v20[key]),1e-300))
        say(f"[RECON {name:9s}] ln |Phi_g| 20->.2={dln('Phi_g'):+.5f}; "
            f"ln qmet={dln('qmet'):+.5f}; Phi_g/qmet end={abs(v02['Phi_g'])/max(v02['qmet'],1e-300):.3e}")

    # Rate differences Phi_g vs qmet across adjacent marks for Ef ICs.
    rate_rows=[]
    for rr in rows:
        if not rr["ic"].startswith("Ef_"): continue
        vals=rr["values"]
        for x0,x1 in zip(vals[:-1],vals[1:]):
            if not (.5 <= x1["kh"] <= 6): continue
            dN=math.log(x1["a"]/x0["a"])
            txp=math.log(max(abs(x1["Phi_g"]),1e-300)/max(abs(x0["Phi_g"]),1e-300))/dN
            txq=math.log(max(x1["qmet"],1e-300)/max(x0["qmet"],1e-300))/dN
            rate_rows.append(dict(ic=rr["ic"],kh=x1["kh"],txPhi=txp,txq=txq,diff=txp-txq,
                                  ratio=abs(x1["Phi_g"])/max(x1["qmet"],1e-300)))
    if rate_rows:
        dif=np.median([x["diff"] for x in rate_rows])
        ratio=np.median([x["ratio"] for x in rate_rows])
        say(f"[R5-A REAUDIT] median(txPhi-txq)={dif:+.5f}; median |Phi_g|/qmet={ratio:.6e}; N={len(rate_rows)}")
    else:
        dif=ratio=float("nan")

    return dict(beta1=b1,npts=npts,max_offdiag_rel={"K":float(offK.max()),"C":float(offC.max()),"W":float(offW.max())},
                chi_checks=chi_checks,reconstruction=rows,r5a_rate_diff_median=float(dif),
                r5a_ratio_median=float(ratio))

def main():
    out=Path("/mnt/data/r6e_out"); out.mkdir(exist_ok=True)
    symbols,fields,vels,L2,K,C,W=R.build_symbolic_L2(); funs=R.lambdas(symbols,K,C,W)
    res=[]
    for n in (12000,24000):
        for b1 in (1.,4.47):
            res.append(run(b1,n,symbols,K,C,W,funs))
    conv=[]
    for b1 in (1.,4.47):
        a=next(x for x in res if x["beta1"]==b1 and x["npts"]==12000)
        b=next(x for x in res if x["beta1"]==b1 and x["npts"]==24000)
        conv.append(dict(beta1=b1,d_rate=b["r5a_rate_diff_median"]-a["r5a_rate_diff_median"],
                         d_ratio=b["r5a_ratio_median"]-a["r5a_ratio_median"]))
    say(""); say("[CONVERGENCE]"); [say(x) for x in conv]
    (out/"r6e_result.json").write_text(json.dumps({"runs":res,"convergence":conv},indent=2),encoding="utf-8")
    (out/"r6e_output.txt").write_text("\n".join(OUT)+"\n",encoding="utf-8")

if __name__=="__main__": main()
