# -*- coding: utf-8 -*-
from __future__ import annotations
import hashlib, json, math, time
from pathlib import Path
import numpy as np
import sympy as sp

T0=time.time(); OUT=[]
def say(*a):
    s=' '.join(str(x) for x in a); print(f'[{time.time()-T0:7.2f}s] {s}'); OUT.append(s)

eps=sp.Symbol('epsilon'); z=sp.Symbol('z', real=True); k=sp.Symbol('k', positive=True)

def cut(e,n=3):
    e=sp.expand(e); return sp.Add(*[e.coeff(eps,i)*eps**i for i in range(n+1)])
def cutM(M,n=3): return M.applyfunc(lambda x: cut(x,n))
def coeffM(M,n): return M.applyfunc(lambda x: sp.expand(x).coeff(eps,n))
def inv_series(M,n=3):
    Ms=[coeffM(M,i) for i in range(n+1)]; I=[None]*(n+1); I[0]=Ms[0].inv()
    for m in range(1,n+1):
        S=sp.zeros(*M.shape)
        for j in range(1,m+1): S += Ms[j]*I[m-j]
        I[m]=-I[0]*S
    return cutM(sum((eps**i*I[i] for i in range(n+1)),sp.zeros(*M.shape)),n)
def inv_scalar(x,n=3):
    xs=[sp.expand(x).coeff(eps,i) for i in range(n+1)]; ys=[1/xs[0]]
    for m in range(1,n+1): ys.append(-sum(xs[j]*ys[m-j] for j in range(1,m+1))/xs[0])
    return cut(sum(eps**i*ys[i] for i in range(n+1)),n)
def sqrt_series(x,n=3):
    xs=[sp.expand(x).coeff(eps,i) for i in range(n+1)]; x0=xs[0]
    u=sum((xs[i]/x0)*eps**i for i in range(1,n+1)); a=1+sp.Rational(1,2)*u
    if n>=2: a-=sp.Rational(1,8)*cut(u*u,n)
    if n>=3: a+=sp.Rational(1,16)*cut(u*u*u,n)
    return cut(sp.sqrt(x0)*a,n)
def sqrt_det4(g,n=3): return sqrt_series(cut(-g.det(),n),n)
def mat_sqrt(M,n=3):
    Ms=[coeffM(M,i) for i in range(n+1)]; M0=Ms[0]
    if not M0.is_diagonal(): raise RuntimeError('M0 not diagonal')
    lam=[sp.sqrt(M0[i,i]) for i in range(4)]; A=[sp.diag(*lam)]
    for m in range(1,n+1):
        R=Ms[m].copy()
        for j in range(1,m): R-=A[j]*A[m-j]
        Am=sp.zeros(4,4)
        for i in range(4):
            for j in range(4): Am[i,j]=sp.cancel(R[i,j]/(lam[i]+lam[j]))
        A.append(Am)
    return cutM(sum((eps**i*A[i] for i in range(n+1)),sp.zeros(4,4)),n)
def esym(A,n=3):
    P=A; pp=[]
    for j in range(1,5):
        if j>1: P=cutM(P*A,n)
        pp.append(cut(P.trace(),n))
    p1,p2,p3,p4=pp; e1=p1
    e2=cut((e1*p1-p2)/2,n); e3=cut((e2*p1-e1*p2+p3)/3,n)
    e4=cut((e3*p1-e2*p2+e1*p3-p4)/4,n)
    return sp.Integer(1),e1,e2,e3,e4

def spatial_ricci(gamma,n=3):
    inv=inv_series(gamma,n); G=[[[0]*3 for _ in range(3)] for __ in range(3)]
    def d(e,c): return sp.diff(e,z) if c==2 else 0
    for l in range(3):
        for i in range(3):
            for j in range(i,3):
                v=0
                for m in range(3): v += inv[l,m]*(d(gamma[m,j],i)+d(gamma[m,i],j)-d(gamma[i,j],m))
                v=cut(v/2,n); G[l][i][j]=v; G[l][j][i]=v
    Rij=sp.zeros(3,3)
    for i in range(3):
        for j in range(3):
            v=0
            for m in range(3):
                if m==2: v+=sp.diff(G[m][i][j],z)
                if j==2: v-=sp.diff(G[m][i][m],z)
                v+=G[m][i][j]*sum(G[l][m][l] for l in range(3))
                for l in range(3): v-=G[l][i][m]*G[m][j][l]
            Rij[i,j]=cut(v,n)
    R=0
    for i in range(3):
        for j in range(3): R+=inv[i,j]*Rij[i,j]
    return cut(R,n),G,inv

def adm_eh(g4,gdot,M2=1,n=3):
    gam=g4[1:4,1:4]; R3,G,ginv=spatial_ricci(gam,n)
    Nc=sp.Matrix([g4[0,i+1] for i in range(3)]); Nu=cutM(ginv*Nc,n)
    N=sqrt_series(cut(-g4[0,0]+(Nc.T*Nu)[0],n),n); iN=inv_scalar(N,n)
    sg=sqrt_series(cut(gam.det(),n),n)
    DN=[[0]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3): DN[i][j]=cut((sp.diff(Nc[j],z) if i==2 else 0)-sum(G[m][i][j]*Nc[m] for m in range(3)),n)
    Kij=sp.zeros(3,3)
    for i in range(3):
        for j in range(3): Kij[i,j]=cut(iN*(gdot[i,j]-DN[i][j]-DN[j][i])/2,n)
    Kt=0; Ks=0
    for i in range(3):
        for j in range(3): Kt+=ginv[i,j]*Kij[i,j]
    Kt=cut(Kt,n)
    for i in range(3):
        for j in range(3):
            for m in range(3):
                for q in range(3): Ks+=ginv[i,m]*ginv[j,q]*Kij[i,j]*Kij[m,q]
    return cut(sp.Rational(1,2)*M2*N*sg*cut(R3+cut(Ks,n)-Kt**2,n),n)

def zavg2(e):
    e=sp.expand(e).subs(sp.sin(k*z)*sp.cos(k*z),0)
    e=e.subs({sp.cos(k*z)**2:sp.Rational(1,2),sp.sin(k*z)**2:sp.Rational(1,2)})
    return sp.expand(e.subs({sp.cos(k*z):0,sp.sin(k*z):0}))

def relations():
    r,h=sp.symbols('r h',positive=True)
    b1=sp.factor(r*(22-17*r**2)/(10*(1-3*r**2)))
    h2=sp.factor((15*r**4-24*r**2-10)/(60*(3*r**2-1)))
    return r,h,b1,h2

def anchor(b1):
    roots=np.roots([1.7,-3*b1,-2.2,b1]); r=sorted(x.real for x in roots if abs(x.imag)<1e-10 and x.real>0)[0]
    H2=0.5*r*r*(0.5-1.2/r**2+b1/r**3)/3
    return float(r),math.sqrt(H2)

def exact_gate():
    say('='*72); say('R6-B/Q2 exact ADM fixed-point gate'); say('='*72)
    r,h,b1,h2=relations(); c,s=sp.cos(k*z),sp.sin(k*z)
    Pg,Bg,Pf,Ps,Bf,Ef=sp.symbols('Phi_g B_g Phi_f Psi_f B_f E_f')
    Pgd,Bgd,Pfd,Psd,Bfd,Efd=sp.symbols('Phi_gdot B_gdot Phi_fdot Psi_fdot B_fdot E_fdot')
    flds=(Pg,Bg,Pf,Ps,Bf,Ef); vels=(Pgd,Bgd,Pfd,Psd,Bfd,Efd)
    g=sp.zeros(4,4); g[0,0]=-(1+2*eps*Pg*c); g[0,3]=g[3,0]=-k*eps*Bg*s
    for i in (1,2,3): g[i,i]=1
    gd=sp.diag(2*h,2*h,2*h)
    f=sp.zeros(4,4); f[0,0]=-r**2*(1+2*eps*Pf*c); f[0,3]=f[3,0]=-r**2*k*eps*Bf*s
    f[1,1]=r**2*(1-2*eps*Ps*c); f[2,2]=f[1,1]; f[3,3]=r**2*(1-2*eps*Ps*c-2*k**2*eps*Ef*c)
    fd=sp.zeros(3,3); fd[0,0]=2*r**2*h*(1-2*eps*Ps*c)-2*r**2*eps*Psd*c; fd[1,1]=fd[0,0]
    fd[2,2]=2*r**2*h*(1-2*eps*Ps*c-2*k**2*eps*Ef*c)-2*r**2*eps*(Psd*c+k**2*Efd*c)
    Lg=adm_eh(g,gd,1,2); Lf=adm_eh(f,fd,1,2)
    A=mat_sqrt(cutM(inv_series(g,2)*f,2),2); e0,e1,e2,e3,e4=esym(A,2)
    V=cut(e0+b1*e1-sp.Rational(2,5)*e2+sp.Rational(1,2)*e4,2)
    Li=cut(-sp.Rational(1,2)*sqrt_series(cut(-g.det(),2),2)*V,2)
    L2=zavg2(sp.expand(cut(Lg+Lf+Li,2)).coeff(eps,2))
    K=sp.zeros(6); C=sp.zeros(6); W=sp.zeros(6)
    for i in range(6):
        for j in range(6):
            K[i,j]=sp.diff(L2,vels[i],vels[j]); C[i,j]=sp.diff(L2,vels[i],flds[j]); W[i,j]=-sp.diff(L2,flds[i],flds[j])
    X=[0,1,2,4]; Q=[3,5]
    for i in X:
        assert all(sp.simplify(K[i,j])==0 for j in range(6)); assert all(sp.simplify(C[i,j])==0 for j in range(6))
    Kq=K.extract(Q,Q); Cqx=C.extract(Q,X); Wxx=W.extract(X,X)
    Ke=sp.simplify(Kq+Cqx*Wxx.inv()*Cqx.T)
    Kon=Ke.applyfunc(lambda e:sp.factor(e.subs(h,sp.sqrt(h2))))
    KE=sp.factor(7*k**4*r**2*(r**2+2)/(-240*k**2*r**2+80*k**2+21*r**4+63*r**2+42))
    assert sp.simplify(Kon[0,0])==0 and sp.simplify(Kon[0,1])==0 and sp.simplify(Kon[1,0])==0 and sp.simplify(Kon[1,1]-KE)==0 and sp.simplify(Kon.det())==0
    KY=sp.factor(KE/k**4)
    say('[Q2 PASS] K_metric =',Kon); say('[Q2 PASS] det(K_metric)=0 exact'); say('[Q2 PASS] K_Y for Y=k^2 E_f =',KY)
    say('[Q2 COUNT] 1 metric scalar + dchi = 2 scalar DOF at fixed point')
    return {'K_metric':str(Kon),'K_E':str(KE),'K_Y':str(KY),'beta1_of_r':str(b1),'H2_of_r':str(h2)}

def cubic(b1v,outdir):
    rv,hv=anchor(b1v); r=sp.Float(rv,30); h=sp.Float(hv,30); c,s=sp.cos(k*z),sp.sin(k*z)
    Pg,Bg,Pf,Ps,Bf,Ef,D=sp.symbols('Phi_g B_g Phi_f Psi_f B_f E_f dchi'); Psd,Efd,Dd=sp.symbols('Psi_fdot E_fdot dchidot'); F3,U3=sp.symbols('F3 U3')
    g=sp.zeros(4,4); g[0,0]=-(1+2*eps*Pg*c); g[0,3]=g[3,0]=-k*eps*Bg*s
    for i in (1,2,3): g[i,i]=1
    gd=sp.diag(2*h,2*h,2*h)
    f=sp.zeros(4,4); f[0,0]=-r**2*(1+2*eps*Pf*c); f[0,3]=f[3,0]=-r**2*k*eps*Bf*s
    f[1,1]=r**2*(1-2*eps*Ps*c); f[2,2]=f[1,1]; f[3,3]=r**2*(1-2*eps*Ps*c-2*k**2*eps*Ef*c)
    fd=sp.zeros(3,3); fd[0,0]=2*r**2*h*(1-2*eps*Ps*c)-2*r**2*eps*Psd*c; fd[1,1]=fd[0,0]
    fd[2,2]=2*r**2*h*(1-2*eps*Ps*c-2*k**2*eps*Ef*c)-2*r**2*eps*(Psd*c+k**2*Efd*c)
    Lg=adm_eh(g,gd,1,3); Lf=adm_eh(f,fd,1,3)
    M=cutM(inv_series(g,3)*f,3); A=mat_sqrt(M,3); resid=cutM(A*A-M,3); e0,e1,e2,e3,e4=esym(A,3)
    V=cut(e0+sp.Float(b1v,30)*e1-sp.Rational(2,5)*e2+sp.Rational(1,2)*e4,3)
    F=1+sp.Rational(1,6)*F3*(eps*D*c)**3; Li=cut(-sp.Rational(1,2)*sqrt_det4(g,3)*cut(F*V,3),3)
    gi=inv_series(g,3); dm=[eps*Dd*c,0,0,-eps*k*D*s]; kin=0
    for mu in range(4):
        for nu in range(4): kin+=gi[mu,nu]*dm[mu]*dm[nu]
    kin=cut(-kin/2,3); U=sp.Rational(3,20)*(eps*D*c)**2+sp.Rational(1,6)*U3*(eps*D*c)**3
    Lchi=cut(sqrt_det4(g,3)*cut(kin-U,3),3); L=cut(Lg+Lf+Li+Lchi,3); L3=sp.expand(L).coeff(eps,3)
    test={Pg:.07,Bg:-.03,Pf:.02,Ps:.04,Bf:-.01,Ef:.03,D:.05,Psd:.02,Efd:-.01,Dd:.03,k:.2,z:.37,eps:.1,F3:0,U3:0}
    mr=0.0
    for i in range(4):
        for j in range(4): mr=max(mr,abs(complex(sp.N(resid[i,j].subs(test),20))))
    assert mr<1e-12 and sp.expand(L3)!=0
    txt=str(L3); assert not any(x in txt for x in ('Phi_gdot','B_gdot','Phi_fdot','B_fdot'))
    tag=str(b1v).replace('.','p'); p=outdir/f'r6b_L3_beta1_{tag}.txt'; p.write_text(f'# beta1={b1v}; r={rv:.16g}; H={hv:.16g}\n# local single-mode L3; F3,U3 symbolic\n# physical cubic vertex requires a Fourier triad\n\n'+sp.sstr(L3)+'\n',encoding='utf-8')
    sha=hashlib.sha256(p.read_bytes()).hexdigest(); terms=len(sp.Add.make_args(sp.expand(L3))); ops=int(sp.count_ops(L3))
    say(f'[C3 beta1={b1v:g}] r={rv:.12g} H={hv:.12g} terms={terms} ops={ops} residual={mr:.2e}'); say('[C3 PASS] ADM primary multipliers have no velocities'); say('[C3] U3 coeff =',sp.factor(sp.diff(L3,U3))); say('[C3] F3 coeff =',sp.factor(sp.diff(L3,F3))); say('[C3] file',p,'sha256='+sha)
    return {'beta1':b1v,'r':rv,'H':hv,'terms':terms,'ops':ops,'residual':mr,'file':str(p),'sha256':sha,'U3_coeff':str(sp.factor(sp.diff(L3,U3))),'F3_coeff':str(sp.factor(sp.diff(L3,F3)))}

def main():
    out=Path('/mnt/data/r6b_out'); out.mkdir(exist_ok=True)
    say('='*72); say('R6-B cubic ADM F1'); say('scope: late proportional beta-constant Gate-F backgrounds'); say('='*72)
    exact=exact_gate(); aa=[cubic(1.0,out),cubic(4.47,out)]
    say(''); say('='*72); say('R6-B VERDICT'); say('='*72); say('[EXPANSION] PASS O(epsilon^3)'); say('[ADM] PASS primary lapse/shift constraints algebraic'); say('[Q2] PASS det K_metric=0 exactly on-shell'); say('[COUNT] 2 scalar DOF total at fixed point, not 3'); say('[GHOST PREMISE] FAIL in this exact gate: second metric direction is null constraint'); say('[STRONG COUPLING] ABORTED for that direction; re-audit Gate F before defining Lambda_SC')
    payload={'exact':exact,'anchors':aa,'verdict':{'expansion':'PASS','detK_metric':'ZERO_EXACT','scalar_dof':2,'gateF_negative_mode':'NULL_CONSTRAINT_IN_EXACT_ADM_GATE','strong_coupling':'ABORT_PENDING_GATEF_REAUDIT'}}
    (out/'r6b_result.json').write_text(json.dumps(payload,indent=2),encoding='utf-8'); (out/'r6b_output.txt').write_text('\n'.join(OUT)+'\n',encoding='utf-8')
if __name__=='__main__': main()
