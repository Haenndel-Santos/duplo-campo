# -*- coding: utf-8 -*-
from __future__ import annotations
import importlib.util, json, math, time, hashlib
from pathlib import Path
import numpy as np
import sympy as sp
import mpmath as mp
from scipy.linalg import eig

# reuse the already-executed cubic ADM engine
spec = importlib.util.spec_from_file_location('r6b','/mnt/data/r6b_cubic_adm.py')
r6b = importlib.util.module_from_spec(spec); spec.loader.exec_module(r6b)
eps,z,k = r6b.eps,r6b.z,r6b.k
cut,cutM,inv_series,sqrt_det4,mat_sqrt,esym,adm_eh,zavg2 = r6b.cut,r6b.cutM,r6b.inv_series,r6b.sqrt_det4,r6b.mat_sqrt,r6b.esym,r6b.adm_eh,r6b.zavg2

T0=time.time(); OUT=[]
def say(*a):
    s=' '.join(str(x) for x in a); print(f'[{time.time()-T0:7.2f}s] {s}'); OUT.append(s)

# Gate-F constants
MU=1.0; MG2=1.0; MF2=1.0; ME2=0.5; M2=1.0
B0V=1.0; B2V=-0.4; B3V=0.0; B4V=0.5; RHO0=0.3; UPP=0.3
A_MIN=100.; A_MAX=80000.
FIELDS=['Phi_g','B_g','Phi_f','Psi_f','B_f','E_f','dchi']
XIDX=[0,1,2,4]; QIDX=[3,5,6]


def build_symbolic_L2():
    say('[SYM] deriving full ADM quadratic action with Ubar included ...')
    a,b,xi,H,Hf,Ub,beta1 = sp.symbols('a b xi H H_f Ubar beta1', positive=True)
    c,s=sp.cos(k*z),sp.sin(k*z)
    Pg,Bg,Pf,Ps,Bf,Ef,D=sp.symbols('Phi_g B_g Phi_f Psi_f B_f E_f dchi')
    Psd,Efd,Dd=sp.symbols('Psi_fdot E_fdot dchidot')
    fields=(Pg,Bg,Pf,Ps,Bf,Ef,D); vels=(sp.Integer(0),sp.Integer(0),sp.Integer(0),Psd,sp.Integer(0),Efd,Dd)

    g=sp.zeros(4,4); g[0,0]=-(1+2*eps*Pg*c); g[0,3]=g[3,0]=-a*k*eps*Bg*s
    for i in (1,2,3): g[i,i]=a**2
    gd=sp.diag(2*a**2*H,2*a**2*H,2*a**2*H)

    f=sp.zeros(4,4); f[0,0]=-xi**2*(1+2*eps*Pf*c); f[0,3]=f[3,0]=-b*xi*k*eps*Bf*s
    f[1,1]=b**2*(1-2*eps*Ps*c); f[2,2]=f[1,1]; f[3,3]=b**2*(1-2*eps*Ps*c-2*k**2*eps*Ef*c)
    hbf=xi*Hf
    fd=sp.zeros(3,3)
    fd[0,0]=2*b**2*hbf*(1-2*eps*Ps*c)-2*b**2*eps*Psd*c; fd[1,1]=fd[0,0]
    fd[2,2]=2*b**2*hbf*(1-2*eps*Ps*c-2*k**2*eps*Ef*c)-2*b**2*eps*(Psd*c+k**2*Efd*c)

    Lg=adm_eh(g,gd,1,2); Lf=adm_eh(f,fd,1,2)
    A=mat_sqrt(cutM(inv_series(g,2)*f,2),2); e0,e1,e2,e3,e4=esym(A,2)
    V=cut(B0V*e0+beta1*e1+sp.Rational(-2,5)*e2+sp.Rational(1,2)*e4,2)
    Lint=cut(-sp.Rational(1,2)*sqrt_det4(g,2)*V,2)

    # chi: background chi_dot=0, U'=0, F'=F''=0 as in Gate F beta-constant run
    gi=inv_series(g,2); dm=[eps*Dd*c,0,0,-eps*k*D*s]; kin=0
    for mu in range(4):
        for nu in range(4): kin += gi[mu,nu]*dm[mu]*dm[nu]
    kin=cut(-kin/2,2)
    Upot=Ub+sp.Rational(3,20)*(eps*D*c)**2
    Lchi=cut(sqrt_det4(g,2)*cut(kin-Upot,2),2)

    L2=zavg2(sp.expand(cut(Lg+Lf+Lint+Lchi,2)).coeff(eps,2))
    vs=[sp.Symbol(n+'dot') for n in FIELDS]
    sub={Psd:vs[3],Efd:vs[5],Dd:vs[6]}
    L2=sp.expand(L2.subs(sub))
    K=sp.zeros(7); C=sp.zeros(7); W=sp.zeros(7)
    for i in range(7):
        for j in range(7):
            K[i,j]=sp.diff(L2,vs[i],vs[j])
            C[i,j]=sp.diff(L2,vs[i],fields[j])
            W[i,j]=-sp.diff(L2,fields[i],fields[j])
    # Exact ADM primary-multiplier gate
    for i in XIDX:
        assert all(sp.simplify(K[i,j])==0 for j in range(7))
        assert all(sp.simplify(C[i,j])==0 for j in range(7))
    say('[SYM] L2 terms=',len(sp.Add.make_args(L2)),'ops=',sp.count_ops(L2))
    say('[SYM] primary multiplier rows K=C=0: PASS')
    return (a,b,xi,H,Hf,Ub,beta1), fields, vs, L2,K,C,W


def bg(a,B1V):
    kap=1.; meff2=.5; rho=RHO0*a**-3; rhot=rho/meff2
    roots=np.roots([kap*B4V-3*B2V,-3*B1V,3*kap*B2V-B0V-rhot,kap*B1V])
    rs=sorted(x.real for x in roots if abs(x.imag)<1e-9 and x.real>1e-10)
    if not rs: raise RuntimeError('no bg root')
    r=rs[0]; dW=kap*(2*B4V*r-B1V/r**2)-3*B1V-6*B2V*r
    dr=-3*rhot/dW
    d2W=kap*(2*B4V+2*B1V/r**3)-6*B2V
    d2r=9*rhot/dW+3*rhot*d2W*dr/dW**2
    xi=r+dr
    Vf=B4V+3*B2V/r**2+B1V/r**3; dVf=-6*B2V/r**3-3*B1V/r**4
    H2=meff2*r*r*Vf/3
    H=math.sqrt(H2); dlnH=.5*(2/r+dVf/Vf)*dr
    Hd=H2*dlnH; xid=H*(dr+d2r); Hfd=(Hd-H2*dr/r)/r
    rho_int=meff2*(B0V+3*B1V*r+3*B2V*r*r)
    Ub=3*H2-rho_int
    return dict(r=r,xi=xi,H=H,Hf=H/r,Hd=Hd,Hfd=Hfd,xid=xid,Ub=Ub,rho=rho,dr=dr)


def lambdas(symbols,K,C,W):
    args=(*symbols,k)
    say('[SYM] lambdifying matrices ...')
    return tuple(sp.lambdify(args,M,modules='numpy',cse=True) for M in (K,C,W))


def eval_mats(funs,symbols,a0,B1V,kc):
    f=bg(a0,B1V); vals=(a0,f['r']*a0,f['xi'],f['H'],f['Hf'],f['Ub'],B1V,kc)
    return tuple(np.array(fn(*vals),float) for fn in funs),f


def schur_adm(K,C,W, rcond=1e-13):
    # K/C rows X are exactly zero in symbolic ADM action.
    Wxx=W[np.ix_(XIDX,XIDX)]; Cqx=C[np.ix_(QIDX,XIDX)]
    Wqx=W[np.ix_(QIDX,XIDX)]; Wxq=W[np.ix_(XIDX,QIDX)]
    Kqq=K[np.ix_(QIDX,QIDX)]; Cqq=C[np.ix_(QIDX,QIDX)]; Wqq=W[np.ix_(QIDX,QIDX)]
    cond=np.linalg.cond(Wxx)
    if cond>1/rcond: raise RuntimeError(f'Wxx condition {cond:.3e}')
    solC=np.linalg.solve(Wxx,Cqx.T)
    solW=np.linalg.solve(Wxx,Wxq)
    Kr=Kqq+Cqx@solC
    Cr=Cqq-Cqx@solW
    Wr=Wqq-Wqx@solW
    return 0.5*(Kr+Kr.T),Cr,0.5*(Wr+Wr.T),cond


def build_track(funs,symbols,B1V,npts):
    Ns=np.linspace(np.log(A_MIN),np.log(A_MAX),npts); aa=np.exp(Ns)
    f0=bg(A_MIN,B1V); kc=45*f0['H']*A_MIN
    Kr=np.zeros((npts,3,3)); Cr=np.zeros_like(Kr); Wr=np.zeros_like(Kr)
    Hs=np.zeros(npts); conds=np.zeros(npts); bgarr=[]
    for p,a0 in enumerate(aa):
        (K,C,W),f=eval_mats(funs,symbols,a0,B1V,kc)
        Kr[p],Cr[p],Wr[p],conds[p]=schur_adm(K,C,W)
        Hs[p]=f['H']; bgarr.append(f)
    return Ns,aa,kc,Hs,Kr,Cr,Wr,conds,bgarr


def eig_signature(K):
    vals=np.linalg.eigvalsh(0.5*(K+K.T)); scale=max(np.max(np.abs(vals)),1e-300)
    return vals, vals/scale


def high_precision_rank(symbols,K,C,W,B1V,a_samples,kh_target=None):
    a,b,xi,H,Hf,Ub,beta1=symbols
    rows=[]
    f0=bg(A_MIN,B1V); kc=45*f0['H']*A_MIN
    for a0 in a_samples:
        f=bg(a0,B1V)
        subs={a:sp.Float(a0,80),b:sp.Float(f['r']*a0,80),xi:sp.Float(f['xi'],80),H:sp.Float(f['H'],80),Hf:sp.Float(f['Hf'],80),Ub:sp.Float(f['Ub'],80),beta1:sp.Float(B1V,80),k:sp.Float(kc,80)}
        Kn=K.subs(subs).evalf(70); Cn=C.subs(subs).evalf(70); Wn=W.subs(subs).evalf(70)
        Wxx=Wn.extract(XIDX,XIDX); Cqx=Cn.extract(QIDX,XIDX); Wqx=Wn.extract(QIDX,XIDX); Wxq=Wn.extract(XIDX,QIDX)
        Kqq=Kn.extract(QIDX,QIDX); Cqq=Cn.extract(QIDX,QIDX); Wqq=Wn.extract(QIDX,QIDX)
        Kr=Kqq+Cqx*Wxx.inv()*Cqx.T
        det=sp.N(Kr.det(),50)
        mp.mp.dps=80
        Km=mp.matrix([[mp.mpf(str(sp.N(Kr[i,j],70))) for j in range(3)] for i in range(3)])
        evmp,_=mp.eigsy(Km)
        evs=sorted([mp.mpf(evmp[i]) for i in range(3)], key=lambda x:abs(x))
        rows.append(dict(a=a0,kh=kc/(a0*f['H']),det=str(det),eigs=[mp.nstr(x,35) for x in evs]))
    return rows


def fj_reduce_track(Ns,Hs,Kr,Cr,Wr):
    """Exact-structure FJ: the null coordinate is Psi_f (index 0) in Q=(Psi_f,E_f,dchi)."""
    n=len(Ns)
    # Structural null: numerical Schur leaves O(1e-25..1e-29 relative) roundoff.
    Kz=Kr.copy(); Kz[:,0,:]=0.0; Kz[:,:,0]=0.0
    Cdot=np.gradient(Cr,Ns,axis=0)*Hs[:,None,None]
    K2=np.zeros((n,2,2)); C2=np.zeros_like(K2); W2=np.zeros_like(K2)
    auxW=np.zeros(n); aux_rel=np.zeros(n)
    for p in range(n):
        Kp=Kz[p].copy(); Cp=Cr[p].copy(); Wp=Wr[p].copy(); i=0
        # IPP row Psi_f: C[i,j] udot_i u_j -> -C[i,j] u_i udot_j - Cdot[i,j] u_i u_j
        for j in range(3):
            cij=Cp[i,j]; cd=Cdot[p,i,j]
            if i==j:
                Wp[i,i]+=cd
            else:
                Wp[i,j]+=cd; Wp[j,i]+=cd; Cp[j,i]-=cij
            Cp[i,j]=0.0
        auxW[p]=Wp[i,i]
        aux_rel[p]=abs(Wp[i,i])/max(np.max(np.abs(Wp)),1e-300)
        # W00 is nonzero on the entire Gate-F tracks; solve Psi_f algebraically.
        if abs(Wp[i,i]) < 1e-18:
            raise RuntimeError(f'Psi_f auxiliary coefficient vanishes at p={p}')
        keep=[1,2]
        cx=Cp[np.ix_(keep,[i])]
        wx=Wp[np.ix_(keep,[i])]
        K2[p]=Kp[np.ix_(keep,keep)]+cx@cx.T/Wp[i,i]
        C2[p]=Cp[np.ix_(keep,keep)]-cx@Wp[np.ix_([i],keep)]/Wp[i,i]
        W2[p]=Wp[np.ix_(keep,keep)]-wx@Wp[np.ix_([i],keep)]/Wp[i,i]
        K2[p]=0.5*(K2[p]+K2[p].T); W2[p]=0.5*(W2[p]+W2[p].T)
    return K2,C2,W2,None,auxW,None,None,aux_rel

def canonical_track(Ns,Hs,K,C,W):
    n=len(Ns); T=np.zeros((n,2,2)); prev=None; signs=[]
    evals=np.zeros((n,2))
    for p in range(n):
        vals,E=np.linalg.eigh(0.5*(K[p]+K[p].T)); evals[p]=vals
        if prev is not None:
            if abs(prev[:,0]@E[:,1])+abs(prev[:,1]@E[:,0]) > abs(prev[:,0]@E[:,0])+abs(prev[:,1]@E[:,1]):
                E[:,[0,1]]=E[:,[1,0]]; vals[[0,1]]=vals[[1,0]]
            for j in range(2):
                if prev[:,j]@E[:,j]<0:E[:,j]*=-1
        prev=E.copy(); signs.append(np.sign(vals))
        if np.min(np.abs(vals))<1e-14*np.max(np.abs(vals)): raise RuntimeError('K2 singular')
        T[p]=E*(1/np.sqrt(np.abs(vals)))[None,:]
    Td=np.gradient(T,Ns,axis=0)*Hs[:,None,None]
    Cc=np.zeros_like(C); Wc=np.zeros_like(W)
    eta_arr=np.zeros_like(K)
    for p in range(n):
        eta_arr[p]=T[p].T@K[p]@T[p]
        Cc[p]=T[p].T@K[p]@Td[p]+T[p].T@C[p]@T[p]
        X=Td[p].T@C[p]@T[p]
        Wc[p]=T[p].T@W[p]@T[p]-Td[p].T@K[p]@Td[p]-(X+X.T)
        Wc[p]=0.5*(Wc[p]+Wc[p].T)
    Ccd=np.gradient(Cc,Ns,axis=0)*Hs[:,None,None]
    return T,Td,Cc,Wc,Ccd,eta_arr,evals


def qep(K,C,W):
    n=K.shape[0]; Ca=C-C.T
    A=np.block([[-Ca,-W],[np.eye(n),np.zeros((n,n))]])
    B=np.block([[K,np.zeros((n,n))],[np.zeros((n,n)),np.eye(n)]])
    lam,vec=eig(A,B); out=[]
    for i,l in enumerate(lam):
        if np.isfinite(l) and abs(l)<1e8:
            v=vec[n:,i]; nv=np.linalg.norm(v)
            if nv>1e-12: out.append((complex(l),v/nv))
    return out


def growth_spectrum(Ns,aa,kc,Hs,K,C,W,marks):
    Kd=np.gradient(K,Ns,axis=0)*Hs[:,None,None]
    Cd=np.gradient(C,Ns,axis=0)*Hs[:,None,None]
    rows=[]
    for a_target in marks:
        p=int(np.argmin(np.abs(aa-a_target)))
        modes=qep(K[p],C[p],W[p]); lams=[x[0] for x in modes]
        maxgrowth=max((l.real/Hs[p] for l in lams),default=float('nan'))
        freqs=sorted(abs(l.imag)/Hs[p] for l in lams if abs(l.imag)>1e-8)
        rows.append(dict(a=float(aa[p]),kh=float(kc/(aa[p]*Hs[p])),max_Re_lambda_over_H=float(maxgrowth),imag_freqs_over_H=freqs))
    return rows,Kd,Cd


def evolve_fundamental(Ns,Hs,K,C,W):
    """Integrate 2-dof linear EOM for 4 basis ICs; return amplification of canonical q norm."""
    n=len(Ns); Kd=np.gradient(K,Ns,axis=0)*Hs[:,None,None]; Cd=np.gradient(C,Ns,axis=0)*Hs[:,None,None]
    # state matrix 4x4, columns fundamental ICs [q; qdot]
    Y=np.eye(4); logs=[]; kh_dummy=[]
    # rescale periodically to avoid overflow; track log singular values incrementally
    logscale=0.0; snaps=[]
    for p in range(n-1):
        dt=(Ns[p+1]-Ns[p])/Hs[p]
        Ki=np.linalg.inv(K[p]); A=Kd[p]+C[p]-C[p].T; B=Cd[p]+W[p]
        def F(M):
            q=M[:2,:]; v=M[2:,:]
            return np.vstack([v,-Ki@(A@v+B@q)])
        k1=F(Y); k2=F(Y+.5*dt*k1); k3=F(Y+.5*dt*k2); k4=F(Y+dt*k3)
        Y=Y+dt*(k1+2*k2+2*k3+k4)/6
        if p%200==199:
            norm=np.linalg.norm(Y)
            if norm>1e50 or norm<1e-50:
                Y/=norm; logscale+=math.log(norm)
        if p in (int(.1*n),int(.25*n),int(.5*n),int(.75*n),n-2):
            svals=np.linalg.svd(Y,compute_uv=False); snaps.append((p,logscale+math.log(max(svals))))
    return snaps


def run_case(symbols,Ks,Cs,Ws,funs,B1V,npts):
    say(''); say('='*72); say(f'CASE beta1={B1V:g}, npts={npts}'); say('='*72)
    Ns,aa,kc,Hs,Kr,Cr,Wr,conds,bgs=build_track(funs,symbols,B1V,npts)
    # raw Schur eigen diagnostics
    evals=np.linalg.eigvalsh(Kr); scale=np.max(np.abs(evals),axis=1); rel=np.abs(evals[:,0])/np.maximum(scale,1e-300)
    say(f'[SCHUR] Wxx cond max={conds.max():.3e}, median={np.median(conds):.3e}')
    say(f'[SCHUR] smallest |lambda_K|/max: max={rel.max():.3e}, median={np.median(rel):.3e}, final={rel[-1]:.3e}')
    say(f'[SCHUR] K signatures sample start/mid/end: {np.linalg.eigvalsh(Kr[0])} | {np.linalg.eigvalsh(Kr[npts//2])} | {np.linalg.eigvalsh(Kr[-1])}')

    K2,C2,W2,eig3,auxW,S,Sd,auxrel=fj_reduce_track(Ns,Hs,Kr,Cr,Wr)
    ev2=np.linalg.eigvalsh(K2)
    say(f'[FJ] reduced K2 min eigenvalue={ev2.min():.6e}; max={ev2.max():.6e}; negatives={(ev2<0).sum()} / {ev2.size}')
    say(f'[FJ] Psi_f auxiliary W range=[{auxW.min():.3e},{auxW.max():.3e}], min relative={auxrel.min():.3e}')
    if np.any(ev2<=0): say('[FJ-GHOST] NEGATIVE kinetic survives exact-null reduction')
    else: say('[FJ-GHOST] NO negative kinetic direction after null-constraint reduction')

    T,Td,Cc,Wc,Ccd,eta,cevals=canonical_track(Ns,Hs,K2,C2,W2)
    etaerr=np.max(np.abs(eta-np.eye(2)))
    say(f'[CAN] max|T^T K T-I|={etaerr:.3e}')

    marks=np.geomspace(120,75000,24)
    spec,Kd,Cd=growth_spectrum(Ns,aa,kc,Hs,np.tile(np.eye(2),(npts,1,1)),Cc,Wc,marks)
    # counts by kh regimes
    band=[x for x in spec if .5<=x['kh']<=30]
    ir=[x for x in spec if x['kh']<.5]
    say('[SPEC] selected points (a,kh,maxRe/H):')
    for x in spec[::4]+([spec[-1]] if spec else []): say(f"       a={x['a']:.0f} kh={x['kh']:.3f} maxRe/H={x['max_Re_lambda_over_H']:+.3f}")
    if band: say(f"[SPEC-BAND] max growth in 0.5<=kh<=30: {max(x['max_Re_lambda_over_H'] for x in band):+.3f} H")
    if ir: say(f"[SPEC-IR] max growth kh<0.5: {max(x['max_Re_lambda_over_H'] for x in ir):+.3f} H")

    snaps=evolve_fundamental(Ns,Hs,K2,C2,W2)
    say('[EVOLVE] log max singular amplification snapshots:',snaps)

    return dict(beta1=B1V,npts=npts,kc=kc,Wxx_cond_max=float(conds.max()),null_rel_max=float(rel.max()),null_rel_median=float(np.median(rel)),K2_min=float(ev2.min()),K2_max=float(ev2.max()),K2_negative_count=int((ev2<0).sum()),eta_error=float(etaerr),spectrum=spec,evolution_snaps=[(int(p),float(v)) for p,v in snaps])


def main():
    outdir=Path('/mnt/data/r6c_out'); outdir.mkdir(exist_ok=True)
    symbols,fields,vels,L2,K,C,W=build_symbolic_L2()
    # save symbolic L2/matrices digest
    (outdir/'r6c_L2_symbolic.txt').write_text('L2=\n'+sp.sstr(L2)+'\n\nK=\n'+sp.sstr(K)+'\n\nC=\n'+sp.sstr(C)+'\n\nW=\n'+sp.sstr(W)+'\n',encoding='utf-8')
    funs=lambdas(symbols,K,C,W)

    hp={}
    for b1 in (1.0,4.47):
        # sample near kh ~30,10,3,1,.3,.06 by choosing closest a on dense background map
        aa=np.geomspace(A_MIN,A_MAX,4000); f0=bg(A_MIN,b1); kc=45*f0['H']*A_MIN
        kh=np.array([kc/(x*bg(x,b1)['H']) for x in aa])
        targets=[30,10,3,1,.5,.2,.06]
        samp=[]
        for t in targets: samp.append(float(aa[np.argmin(abs(kh-t))]))
        # direct high-precision is expensive: use only 4 representative points
        pick=[samp[0],samp[2],samp[3],samp[-1]]
        say(f'[HP beta1={b1:g}] points={pick}')
        hp[str(b1)]=high_precision_rank(symbols,K,C,W,b1,pick)
        for row in hp[str(b1)]: say('[HP]',row)

    results=[]
    for npts in (3000,6000):
        for b1 in (1.0,4.47): results.append(run_case(symbols,K,C,W,funs,b1,npts))

    # convergence summary
    conv=[]
    for b1 in (1.0,4.47):
        r3=next(x for x in results if x['beta1']==b1 and x['npts']==3000)
        r6=next(x for x in results if x['beta1']==b1 and x['npts']==6000)
        conv.append(dict(beta1=b1,dK2min=abs(r6['K2_min']-r3['K2_min'])/max(abs(r6['K2_min']),1e-300),dnull=abs(r6['null_rel_max']-r3['null_rel_max'])))
    payload={'high_precision':hp,'runs':results,'convergence':conv}
    (outdir/'r6c_result.json').write_text(json.dumps(payload,indent=2),encoding='utf-8')
    say(''); say('='*72); say('R6-C REAUDIT SUMMARY'); say('='*72)
    for c in conv: say('[CONV]',c)
    for b1 in (1.,4.47):
        rr=next(x for x in results if x['beta1']==b1 and x['npts']==6000)
        say(f"beta1={b1:g}: null_rel_max={rr['null_rel_max']:.3e}; K2_min={rr['K2_min']:.3e}; negatives={rr['K2_negative_count']}; etaerr={rr['eta_error']:.3e}")
    (outdir/'r6c_output.txt').write_text('\n'.join(OUT)+'\n',encoding='utf-8')

if __name__=='__main__': main()
