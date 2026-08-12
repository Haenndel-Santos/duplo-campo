
# -*- coding: utf-8 -*-
"""
R6-F0 — derive dynamic beta1(phi_-) ADM quadratic action and diagnose the
kinetic null direction on the original rolling background.
"""
from __future__ import annotations
import importlib.util, math, time, json
from pathlib import Path
import numpy as np
import sympy as sp
from scipy.optimize import brentq
from scipy.interpolate import CubicSpline

spec=importlib.util.spec_from_file_location("r6b","/mnt/data/r6b_cubic_adm.py")
B=importlib.util.module_from_spec(spec); spec.loader.exec_module(B)
eps,z,k=B.eps,B.z,B.k
cut,cutM,inv_series,sqrt_det4,mat_sqrt,esym,adm_eh,zavg2=B.cut,B.cutM,B.inv_series,B.sqrt_det4,B.mat_sqrt,B.esym,B.adm_eh,B.zavg2

T0=time.time(); OUT=[]
def say(*a):
    s=" ".join(str(x) for x in a); print(f"[{time.time()-T0:7.2f}s] {s}"); OUT.append(s)

B0=1.; B2=-.4; B4=.5; B10=1.; VST=1.; ME2=.5; RHO0=.3
A_MIN=20.; A_MAX=80000.
XIDX=[0,1,2,4]; QIDX=[3,5,6]
FIELDS=['Phi_g','B_g','Phi_f','Psi_f','B_f','E_f','dchi']

def build_dynamic():
    say("[SYM] dynamic ADM L2: chidot,beta1',beta1'' included")
    a,b,xi,H,Hf,Ub,Up,Upp,chd,b1v,b1p,b1pp=sp.symbols(
        "a b xi H H_f Ubar Uprime Upp chidot beta1 beta1p beta1pp", real=True)
    # positive-background assumptions not needed for lambdify; numeric branch positive
    c,s=sp.cos(k*z),sp.sin(k*z)
    Pg,Bg,Pf,Ps,Bf,Ef,D=sp.symbols("Phi_g B_g Phi_f Psi_f B_f E_f dchi")
    Psd,Efd,Dd=sp.symbols("Psi_fdot E_fdot dchidot")
    fields=(Pg,Bg,Pf,Ps,Bf,Ef,D)
    vsyms=[sp.Symbol(n+"dot") for n in FIELDS]

    g=sp.zeros(4,4); g[0,0]=-(1+2*eps*Pg*c); g[0,3]=g[3,0]=-a*k*eps*Bg*s
    for i in (1,2,3): g[i,i]=a**2
    gd=sp.diag(2*a*a*H,2*a*a*H,2*a*a*H)

    f=sp.zeros(4,4); f[0,0]=-xi**2*(1+2*eps*Pf*c); f[0,3]=f[3,0]=-b*xi*k*eps*Bf*s
    f[1,1]=b*b*(1-2*eps*Ps*c); f[2,2]=f[1,1]
    f[3,3]=b*b*(1-2*eps*Ps*c-2*k*k*eps*Ef*c)
    hb=xi*Hf
    fd=sp.zeros(3,3)
    fd[0,0]=2*b*b*hb*(1-2*eps*Ps*c)-2*b*b*eps*Psd*c
    fd[1,1]=fd[0,0]
    fd[2,2]=2*b*b*hb*(1-2*eps*Ps*c-2*k*k*eps*Ef*c)-2*b*b*eps*(Psd*c+k*k*Efd*c)

    Lg=adm_eh(g,gd,1,2); Lf=adm_eh(f,fd,1,2)
    A=mat_sqrt(cutM(inv_series(g,2)*f,2),2); e0,e1,e2,e3,e4=esym(A,2)
    d=eps*D*c
    b1field=b1v+b1p*d+sp.Rational(1,2)*b1pp*d*d
    V=cut(B0*e0+b1field*e1+sp.Rational(-2,5)*e2+sp.Rational(1,2)*e4,2)
    Lint=cut(-sp.Rational(1,2)*sqrt_det4(g,2)*V,2)

    gi=inv_series(g,2)
    dm=[chd+eps*Dd*c,0,0,-eps*k*D*s]
    kin=0
    for mu in range(4):
        for nu in range(4): kin+=gi[mu,nu]*dm[mu]*dm[nu]
    kin=cut(-kin/2,2)
    U=Ub+Up*d+sp.Rational(1,2)*Upp*d*d
    Lchi=cut(sqrt_det4(g,2)*cut(kin-U,2),2)

    L2=zavg2(sp.expand(cut(Lg+Lf+Lint+Lchi,2)).coeff(eps,2))
    L2=sp.expand(L2.subs({Psd:vsyms[3],Efd:vsyms[5],Dd:vsyms[6]}))
    K=sp.zeros(7); C=sp.zeros(7); W=sp.zeros(7)
    for i in range(7):
        for j in range(7):
            K[i,j]=sp.diff(L2,vsyms[i],vsyms[j])
            C[i,j]=sp.diff(L2,vsyms[i],fields[j])
            W[i,j]=-sp.diff(L2,fields[i],fields[j])
    for i in XIDX:
        assert all(sp.simplify(K[i,j])==0 for j in range(7))
        assert all(sp.simplify(C[i,j])==0 for j in range(7))
    say("[SYM] terms",len(sp.Add.make_args(L2)),"ops",sp.count_ops(L2),"primary K=C zero PASS")
    syms=(a,b,xi,H,Hf,Ub,Up,Upp,chd,b1v,b1p,b1pp)
    funs=tuple(sp.lambdify((*syms,k),M,modules="numpy",cse=True) for M in (K,C,W))
    return syms,L2,K,C,W,funs

# Exact old R4b background machinery
a_,b_,ch_=sp.symbols('a b chi',positive=True)
pa_,pb_,pch_=sp.symbols('p_a p_b p_chi',real=True)
Hs_,Hfs_,chds_=sp.symbols('H H_f chidot',real=True)
Mg2s,Mf2s,Me2s,m2s=sp.symbols('Mg2 Mf2 Meff2 m2',positive=True)
b0s,b2s,b4s,b10s,vsts=sp.symbols('beta_0 beta_2 beta_4 b1_0 v_star',real=True)
b1c=b10s*(1+ch_**2/vsts**2); rr_=b_/a_
Vgc=b0s+3*rr_*b1c+3*rr_**2*b2s
Vfc=b1c+3*rr_*b2s+rr_**3*b4s
Hg=-pa_**2/(12*Mg2s*a_)+pch_**2/(2*a_**3)+m2s*Me2s*a_**3*Vgc
Hfham=-pb_**2/(12*Mf2s*b_)+m2s*Me2s*a_**3*Vfc
CAN=[(a_,pa_),(b_,pb_),(ch_,pch_)]
Om=sp.expand(sum(sp.diff(Hg,q)*sp.diff(Hfham,p)-sp.diff(Hg,p)*sp.diff(Hfham,q) for q,p in CAN))
Omv=sp.expand(Om.subs({pa_:-6*Mg2s*a_**2*Hs_,pb_:-6*Mf2s*b_**2*Hfs_,pch_:a_**3*chds_}))
Omfn=sp.lambdify((a_,b_,ch_,chds_,Hs_,Hfs_,Mg2s,Mf2s,Me2s,m2s,b0s,b2s,b4s,b10s,vsts),Omv,"math")

def beta1(ch): return 1+ch*ch
def dbeta1(ch): return 2*ch
def U(ch,mu2,lam,U0): return -.5*mu2*ch*ch+.25*lam*ch**4+U0
def Up(ch,mu2,lam): return -mu2*ch+lam*ch**3
def Hf2(r,ch): return ME2*(beta1(ch)+3*r*B2+r**3*B4)/(3*r**3)
def H2(r,ch,chd,a,mu2,lam,U0):
    return (.5*chd*chd+U(ch,mu2,lam,U0)+RHO0/a**3+ME2*(B0+3*r*beta1(ch)+3*r*r*B2))/3
def Omnum(r,ch,chd,a,mu2,lam,U0):
    h2=H2(r,ch,chd,a,mu2,lam,U0); hf2=Hf2(r,ch)
    if h2<=0 or hf2<=0:return float("nan")
    return Omfn(a,r*a,ch,chd,math.sqrt(h2),math.sqrt(hf2),1,1,.5,1,B0,B2,B4,1,1)
def initial_r(a,ch,chd,mu2,lam,U0):
    rt=(.5*chd*chd+U(ch,mu2,lam,U0)+RHO0/a**3)/ME2
    roots=np.roots([B4-3*B2,-3*beta1(ch),3*B2-B0-rt,beta1(ch)])
    rs=sorted(x.real for x in roots if abs(x.imag)<1e-9 and x.real>1e-12)
    return rs[0]
def find_r(prev,ch,chd,a,mu2,lam,U0):
    for fac in (.08,.25,.6):
        grid=np.linspace(prev*(1-fac),prev*(1+fac),61)
        vals=np.array([Omnum(x,ch,chd,a,mu2,lam,U0) for x in grid])
        for i in range(60):
            if np.isfinite(vals[i:i+2]).all() and vals[i]*vals[i+1]<0:
                try:return brentq(lambda x:Omnum(x,ch,chd,a,mu2,lam,U0),grid[i],grid[i+1],xtol=1e-14)
                except ValueError:pass
    return None

def integrate_bg(dN=5e-4):
    v=2.; mu2=15.; lam=3.75; U0=15.
    N0,N1=np.log(.01),np.log(1e5); n=int((N1-N0)/dN)+1
    ch=.002; y=0.; r=initial_r(.01,ch,0.,mu2,lam,U0); rp=3*r; Hprev=None
    rec={q:[] for q in ("N","a","r","xi","H","Hf","ch","chd","Ub","Up","Upp")}
    stride=max(1,n//24000)
    for i in range(n):
        N=N0+i*dN; a=np.exp(N)
        Vg=B0+3*r*beta1(ch)+3*r*r*B2
        rest=U(ch,mu2,lam,U0)+RHO0/a**3+ME2*Vg
        den=3-.5*y*y
        if den<=0 or rest<=0: raise RuntimeError("bad H")
        H=math.sqrt(rest/den); chd=H*y
        hf2=Hf2(r,ch)
        if hf2<=0: raise RuntimeError("bad Hf")
        Hf=math.sqrt(hf2); xi=H*(1+rp/r)/Hf
        chidd=-3*H*chd-Up(ch,mu2,lam)-ME2*dbeta1(ch)*(xi+3*r)
        Hp=0 if Hprev is None else (H-Hprev)/dN
        yp=chidd/(H*H)-(Hp/H)*y
        if i%stride==0:
            for q,val in [
                ("N",N),("a",a),("r",r),("xi",xi),("H",H),("Hf",Hf),("ch",ch),("chd",chd),
                ("Ub",U(ch,mu2,lam,U0)+RHO0/a**3),("Up",Up(ch,mu2,lam)),
                ("Upp",-mu2+3*lam*ch*ch)]:rec[q].append(val)
        ch+=dN*y; y+=dN*yp
        rnew=find_r(r,ch,H*y,np.exp(N+dN),mu2,lam,U0)
        if rnew is None: raise RuntimeError(f"lost root a={np.exp(N+dN)}")
        rp=(rnew-r)/dN; r=rnew; Hprev=H
    rec={q:np.array(v) for q,v in rec.items()}
    say(f"[BG] points={len(rec['N'])}; r_end={rec['r'][-1]:.6f}; chi/v={rec['ch'][-1]/2:.6f}")
    return rec

def make_spl(rec):
    return {q:CubicSpline(rec["N"],rec[q]) for q in rec if q!="N" and q!="a"}

def eval_mats(funs,syms,spl,N,kc):
    a=math.exp(N)
    vals={q:float(spl[q](N)) for q in ("r","xi","H","Hf","ch","chd","Ub","Up","Upp")}
    b1=beta1(vals["ch"]); b1p=dbeta1(vals["ch"]); b1pp=2.
    args=(a,vals["r"]*a,vals["xi"],vals["H"],vals["Hf"],vals["Ub"],vals["Up"],vals["Upp"],
          vals["chd"],b1,b1p,b1pp,kc)
    mats=tuple(np.array(f(*args),float) for f in funs)
    return mats,vals

def diagnose(funs,syms,rec):
    spl=make_spl(rec)
    # sample full dynamic history a=20..80000, one representative mode crossing at 4000
    Ngrid=np.linspace(np.log(20.),np.log(80000.),3000)
    Hcross=float(spl["H"](np.log(4000.))); kc=4000*Hcross
    rowrel=[]; eigrel=[]; nullvec=[]; cond=[]
    for N in Ngrid:
        (K,C,W),v=eval_mats(funs,syms,spl,N,kc)
        Wxx=W[np.ix_(XIDX,XIDX)]; Cqx=C[np.ix_(QIDX,XIDX)]
        Kq=K[np.ix_(QIDX,QIDX)]+Cqx@np.linalg.solve(Wxx,Cqx.T)
        es,ev=np.linalg.eigh(.5*(Kq+Kq.T)); sc=max(abs(es).max(),1e-300)
        j=np.argmin(abs(es))
        eigrel.append(abs(es[j])/sc)
        rowrel.append(np.linalg.norm(Kq[0,:])/max(np.linalg.norm(Kq),1e-300))
        nullvec.append(abs(ev[:,j]))
        cond.append(np.linalg.cond(Wxx))
    nullvec=np.array(nullvec)
    say(f"[NULL] max row(Psi_f)/||K||={max(rowrel):.3e}; max |lambda_min|/scale={max(eigrel):.3e}")
    say(f"[NULL] median abs null eigenvector components (Psi,Ef,dchi)={np.median(nullvec,axis=0)}")
    say(f"[WXX] cond max={max(cond):.3e}")
    return dict(max_rowrel=float(max(rowrel)),max_eigrel=float(max(eigrel)),
                med_null=np.median(nullvec,axis=0).tolist(),condmax=float(max(cond)))

def main():
    out=Path("/mnt/data/r6f0_out");out.mkdir(exist_ok=True)
    syms,L2,K,C,W,funs=build_dynamic()
    (out/"dynamic_L2.txt").write_text("L2=\n"+sp.sstr(L2)+"\n\nK=\n"+sp.sstr(K)+"\n\nC=\n"+sp.sstr(C)+"\n\nW=\n"+sp.sstr(W),encoding="utf-8")
    rec=integrate_bg()
    diag=diagnose(funs,syms,rec)
    np.savez_compressed(out/"rolling_background.npz",**rec)
    (out/"r6f0_result.json").write_text(json.dumps(diag,indent=2),encoding="utf-8")
    (out/"r6f0_output.txt").write_text("\n".join(OUT)+"\n",encoding="utf-8")
if __name__=="__main__":main()
