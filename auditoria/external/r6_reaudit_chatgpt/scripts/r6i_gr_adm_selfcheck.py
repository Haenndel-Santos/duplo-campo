
# -*- coding: utf-8 -*-
"""R6-I — symbolic GR + canonical scalar ADM null test."""
import importlib.util
from pathlib import Path
import sympy as sp

spec=importlib.util.spec_from_file_location("B","/mnt/data/r6b_cubic_adm.py")
B=importlib.util.module_from_spec(spec);spec.loader.exec_module(B)
eps,z,k=B.eps,B.z,B.k
a,H,Ub,Upp=sp.symbols("a H Ubar Upp",positive=True)
Pg,Bg,D=sp.symbols("Phi_g B_g dchi")
Dd=sp.symbols("dchidot")
c,s=sp.cos(k*z),sp.sin(k*z)

g=sp.zeros(4,4);g[0,0]=-(1+2*eps*Pg*c);g[0,3]=g[3,0]=-a*k*eps*Bg*s
for i in (1,2,3):g[i,i]=a*a
gd=sp.diag(2*a*a*H,2*a*a*H,2*a*a*H)
Lg=B.adm_eh(g,gd,1,2)
gi=B.inv_series(g,2)
dm=[eps*Dd*c,0,0,-eps*k*D*s]
kin=0
for mu in range(4):
    for nu in range(4):kin+=gi[mu,nu]*dm[mu]*dm[nu]
kin=B.cut(-kin/2,2)
U=Ub+sp.Rational(1,2)*Upp*(eps*D*c)**2
Lc=B.cut(B.sqrt_det4(g,2)*B.cut(kin-U,2),2)
L2=B.zavg2(sp.expand(B.cut(Lg+Lc,2)).coeff(eps,2))
fields=[Pg,Bg,D];vels=[sp.Symbol("Phi_dot"),sp.Symbol("B_dot"),Dd]
K=sp.zeros(3);C=sp.zeros(3);W=sp.zeros(3)
for i in range(3):
    for j in range(3):
        K[i,j]=sp.diff(L2,vels[i],vels[j])
        C[i,j]=sp.diff(L2,vels[i],fields[j])
        W[i,j]=-sp.diff(L2,fields[i],fields[j])
# multipliers Phi,B algebraic; D already decouples because background scalar velocity=0
print("K =",K)
print("C =",C)
print("K_DD =",sp.factor(K[2,2]))
print("W_DD =",sp.factor(W[2,2]))
targetK=a**3/sp.Integer(2)
targetW=(a*k**2+a**3*Upp)/2
print("K target residual =",sp.simplify(K[2,2]-targetK))
print("W target residual =",sp.simplify(W[2,2]-targetW))
print("offdiag D with metric K,C,W =",
      [sp.simplify(M[2,j]) for M in (K,C,W) for j in (0,1)])
assert sp.simplify(K[2,2]-targetK)==0
assert sp.simplify(W[2,2]-targetW)==0
assert all(sp.simplify(M[2,j])==0 for M in (K,C,W) for j in (0,1))
print("[GR-ADM PASS] one canonical scalar, c_s^2=1; no scalar metric DOF.")
out=Path("/mnt/data/r6i_out");out.mkdir(exist_ok=True)
(out/"r6i_output.txt").write_text(
    "K_DD="+str(sp.factor(K[2,2]))+"\nW_DD="+str(sp.factor(W[2,2]))+
    "\nPASS: c_s^2=1; metric-scalar offdiagonal=0\n",encoding="utf-8")
