# -*- coding: utf-8 -*-
"""
evolucao_temporal_escalar.py — O TESTE ALEM DO CONGELAMENTO.

Integra as perturbacoes escalares NO TEMPO, sobre o fundo do ramo
finito evoluindo de verdade (r(N), xi(N), H(N) da cubica), e compara o
crescimento medido com a previsao do QEP congelado.

Por que isto e necessario. A v3 do d1_ramo_finito tentou testar o
congelamento alimentando Hdot/Hfdot/xidot verdadeiros — e deu saida
BIT A BIT identica ao caso congelado. Motivo estrutural: a acao usa a
forma Gamma-Gamma (so primeiras derivadas do fundo), entao as matrizes
K, C, W nao contem esses simbolos. O congelamento da D1 nao esta nos
valores das taxas: esta no ansatz q ~ e^{i w t} com matrizes
constantes. O teste genuino e resolver

    K(t) qdd + [Kdot + C - C^T](t) qd + [Cdot + W](t) q = 0

ao longo da trajetoria de fundo, com os vinculos (4 multiplicadores)
eliminados algebricamente a cada instante, e medir ln|q|(N).

Leitura:
  - crescimento ~ integral do Im(omega) congelado -> taquiao GENUINO;
    o ramo finito puro (beta_n constantes) reprova o setor escalar.
  - crescimento muito menor / oscilacao -> o congelamento era o
    artefato; o fundo em movimento doma o par.

Auto-testes embutidos:
  (i)  QEP do sistema REDUZIDO (3x3) em a=1, k=1 deve reproduzir os
       omega^2 do QEP 7x7 da rodada 2: {+1.3000, +3.8578, -8.4750};
  (ii) modo espectador delta-chi integrado no tempo deve OSCILAR sem
       crescimento secular (controle).

Requer sympy, numpy, scipy.  Demora ~2-4 min (montagem simbolica +
lambdify + integracao).  Uso:
    python auditoria/code/evolucao_temporal_escalar.py
"""
import importlib.util
import os
import sys
import time

import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

HERE = os.path.dirname(os.path.abspath(__file__))
DCODE = os.path.normpath(os.path.join(HERE, '..', '..', 'derivations', 'code'))
sys.path.insert(0, DCODE)

spec = importlib.util.spec_from_file_location(
    "d1mod", os.path.join(DCODE, "01_setor_escalar_K_Omega.py"))
d1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(d1)

from tdcp_pert_lib import (a_s, b_s, xi_s, H_s, Hf_s, Hd_s, Hfd_s, xid_s,
                           chid_s, chidd_s, Mg2, Mf2, m2, Meff2,
                           b0, b1, b2, b3, b4, Fb, Fp, Fpp,
                           Ub, Up, Upp, rho_s, k as ksym,
                           quadratic_matrices)

T0 = time.time()
def say(*a):
    print(f"[{time.time()-T0:7.1f}s]", *a)

# ------------------------- parametros (identicos ao d1_ramo_finito) --
PBnum = {b0: 1.0, b1: 1.0, b2: -0.4, b3: 0.0, b4: 0.5,
         Mg2: 1.0, Mf2: 1.0, Meff2: 0.5, m2: 1.0,
         Fb: 1.0, Fp: 0.0, Fpp: 0.0,
         chid_s: 0.0, chidd_s: 0.0, Up: 0.0, Upp: 0.3,
         rho_s: 0.0,                        # materia -> Ub (mesmo truque)
         Hd_s: 0.0, Hfd_s: 0.0, xid_s: 0.0}
RHO_M0 = 0.3
ESPERADO_A1_K1 = np.array([1.3000, 3.8578, -8.4750])   # rodada 2, 7x7

# ------------------------------ fundo (ramo finito, cubica) ----------
def W_de_r(r):
    Vf = 0.5 - 1.2/r**2 + 1.0/r**3
    Vg = 1.0 + 3.0*r - 1.2*r**2
    return r*r*Vf - Vg

# W(r) = 0.5 r^2 - 1.2 + 1/r - 1 - 3r + 1.2 r^2 = 1.7 r^2 - 3r + 1/r - 2.2
#   ->  W'(r) = 3.4 r - 3 - 1/r^2
def dW_dr(r):
    return 3.4*r - 3.0 - 1.0/r**2

def raiz_finita(rho_til):
    # cubica: 1.7 r^3 - 3 r^2 - (2.2+rho_til) r + 1 = 0 ; menor raiz > 0
    rr = np.roots([1.7, -3.0, -(2.2 + rho_til), 1.0])
    reais = sorted(z.real for z in rr if abs(z.imag) < 1e-9 and z.real > 1e-10)
    return reais[0]

def fundo_em(N):
    """r, xi, H, Hf, Ub, a, b no instante N=ln a."""
    a = np.exp(N)
    rho = RHO_M0 * a**-3
    rho_til = rho / 0.5                          # m^2 M_eff^2 = 0.5
    r = raiz_finita(rho_til)
    drdN = -3.0*rho_til/dW_dr(r)
    xi = r + drdN
    Vf = 0.5 - 1.2/r**2 + 1.0/r**3
    H2 = 0.5*r*r*Vf/3.0
    H = np.sqrt(H2)
    rho_int = 0.5*(1.0 + 3.0*r - 1.2*r**2)
    Ubv = 3.0*H2 - rho - rho_int + rho           # + rho: truque materia->Ub
    return r, xi, H, H/r, Ubv, a, r*a

# ------------------------------ matrizes numericas -------------------
say("montando L2 (mesma acao/gauge da D1) ...")
L2s, fields, vels = d1.build_L2()
K7, C7, W7 = quadratic_matrices(L2s, fields, vels)
say(f"lambdificando 3 matrizes 7x7 em (a,b,xi,H,Hf,Ub,k) ...")
livres = (a_s, b_s, xi_s, H_s, Hf_s, Ub, ksym)
K7n = sp.lambdify(livres, K7.subs(PBnum), modules='numpy')
C7n = sp.lambdify(livres, C7.subs(PBnum), modules='numpy')
W7n = sp.lambdify(livres, W7.subs(PBnum), modules='numpy')

def matrizes7(N, kv):
    r, xi, H, Hf, Ubv, a, b = fundo_em(N)
    args = (a, b, xi, H, Hf, Ubv, kv)
    return (np.array(K7n(*args), float),
            np.array(C7n(*args), float),
            np.array(W7n(*args), float))

# ------------------------------ reducao (elimina multiplicadores) ----
def particao(K, C, tol=1e-12):
    """dinamicos = linhas de K ou C nao-nulas em VELOCIDADE."""
    din, aux = [], []
    for i in range(K.shape[0]):
        if np.abs(K[i]).max() > tol or np.abs(K[:, i]).max() > tol \
                or np.abs(C[i]).max() > tol:
            din.append(i)
        else:
            aux.append(i)
    return din, aux

def reduz(K, C, W, din, aux):
    """Elimina os auxiliares (sem velocidade): dL/dy = 0 ->
       y = Wyy^-1 (C_xy^T xdot - W_yx x); extrai K,C,W reduzidas por
       polarizacao (exata para formas quadraticas)."""
    x, y = din, aux
    Kxx = K[np.ix_(x, x)]
    Cxx = C[np.ix_(x, x)]
    Cxy = C[np.ix_(x, y)]
    Wxx = W[np.ix_(x, x)]
    Wxy = W[np.ix_(x, y)]
    Wyy = W[np.ix_(y, y)]
    Wyx = W[np.ix_(y, x)]
    Wyy_inv = np.linalg.inv(Wyy)
    P = Wyy_inv @ Cxy.T          # y = P xdot + Q x
    Q = -Wyy_inv @ Wyx

    def L(xv, xd):
        yv = P @ xd + Q @ xv
        return (0.5*xd @ Kxx @ xd + xd @ (Cxx @ xv + Cxy @ yv)
                - 0.5*(xv @ Wxx @ xv + 2*xv @ (Wxy @ yv) + yv @ Wyy @ yv))

    n = len(x)
    e = np.eye(n)
    z = np.zeros(n)
    Kr = np.array([[L(z, e[i]+e[j]) - L(z, e[i]) - L(z, e[j])
                    for j in range(n)] for i in range(n)])
    Wr = -np.array([[L(e[i]+e[j], z) - L(e[i], z) - L(e[j], z)
                     for j in range(n)] for i in range(n)])
    Cr = np.array([[L(e[j], e[i]) - L(e[j], z) - L(z, e[i])
                    for j in range(n)] for i in range(n)])
    return Kr, Cr, Wr

def qep_reduzida(Kr, Cr, Wr):
    """autovalores lam de (lam^2 K + lam Ca + W) v = 0, Ca = C - C^T."""
    n = Kr.shape[0]
    Ca = Cr - Cr.T
    A = np.block([[np.zeros((n, n)), np.eye(n)],
                  [-np.linalg.solve(Kr, Wr), -np.linalg.solve(Kr, Ca)]])
    return np.linalg.eigvals(A), A

# ------------------------------ auto-teste (i): QEP reduzida ---------
say("auto-teste (i): QEP reduzida em a=1, k=1 vs rodada 2 do 7x7 ...")
K, C, W = matrizes7(0.0, 1.0)
din, aux = particao(K, C)
say(f"    particao: {len(din)} dinamicos {din}, {len(aux)} auxiliares {aux}")
Kr, Cr, Wr = reduz(K, C, W, din, aux)
lam, _ = qep_reduzida(Kr, Cr, Wr)
w2 = np.sort_complex(-lam**2)          # lam = i w  ->  w^2 = -lam^2
w2_reais = sorted(set(np.round(
    [z.real for z in w2 if abs(z.imag) < 1e-4*max(1, abs(z))], 3)))
say(f"    omega^2 (reduzida) = {w2_reais}")
say(f"    esperado (7x7)     = {sorted(ESPERADO_A1_K1)}")
casa = all(any(abs(e - v) < 2e-2*max(1, abs(e)) for v in w2_reais)
           for e in ESPERADO_A1_K1)
say(f"    [{'PASSA' if casa else 'FALHA'}] reducao reproduz o espectro 7x7")
if not casa:
    say("    !! abortando: a reducao nao esta validada")
    sys.exit(1)

# ------------------------------ integracao temporal ------------------
def integra(kv, N0=np.log(0.25), N1=np.log(2.0), n_grid=241,
            modo='instavel'):
    """Integra K x'' + (Kdot + Ca) x' + (Cdot + W) x = 0 em t, com
    matrizes reduzidas interpoladas na trajetoria de fundo."""
    Ns = np.linspace(N0, N1, n_grid)
    Kr_s, Cr_s, Wr_s, Hs, ts = [], [], [], [], [0.0]
    for i, N in enumerate(Ns):
        K, C, W = matrizes7(N, kv)
        d_, a_ = particao(K, C)
        if (d_, a_) != (din, aux):
            raise RuntimeError(f"particao mudou em N={N:.3f}")
        Kr, Cr, Wr = reduz(K, C, W, d_, a_)
        Kr_s.append(Kr); Cr_s.append(Cr); Wr_s.append(Wr)
        H = fundo_em(N)[2]
        Hs.append(H)
        if i:
            dN = Ns[i]-Ns[i-1]
            ts.append(ts[-1] + dN*2.0/(Hs[-1]+Hs[-2]))   # dt = dN/H
    Kr_s = np.array(Kr_s); Cr_s = np.array(Cr_s); Wr_s = np.array(Wr_s)
    ts = np.array(ts); Hs = np.array(Hs)
    Kdot = np.gradient(Kr_s, ts, axis=0)
    Cdot = np.gradient(Cr_s, ts, axis=0)

    def interp(arr, t):
        j = np.clip(np.searchsorted(ts, t)-1, 0, len(ts)-2)
        w = (t-ts[j])/(ts[j+1]-ts[j])
        return (1-w)*arr[j] + w*arr[j+1]

    n = Kr_s.shape[1]

    def rhs(t, z):
        x, v = z[:n], z[n:]
        K = interp(Kr_s, t); Kd = interp(Kdot, t)
        C = interp(Cr_s, t); Cd = interp(Cdot, t)
        W = interp(Wr_s, t)
        G = Kd + C - C.T
        F = Cd + W
        return np.concatenate([v, -np.linalg.solve(K, G @ v + F @ x)])

    # condicao inicial: automodo do pencil congelado em N0
    lam0, A0 = qep_reduzida(Kr_s[0], Cr_s[0] , Wr_s[0])
    vals, vecs = np.linalg.eig(A0)
    if modo == 'instavel':
        i0 = int(np.argmax(vals.real))
    else:                                   # espectador: w2 ~ k^2+0.31
        alvo = np.sqrt(kv**2/np.exp(2*N0) + 0.31)
        i0 = int(np.argmin(np.abs(np.abs(vals.imag) - alvo)
                           + 1e3*np.abs(vals.real)))
    z0 = np.real(vecs[:, i0])
    if np.linalg.norm(z0) < 1e-12:
        z0 = np.imag(vecs[:, i0])
    z0 = z0/np.linalg.norm(z0)

    sol = solve_ivp(rhs, (ts[0], ts[-1]), z0, method='RK45',
                    rtol=1e-8, atol=1e-10, dense_output=True,
                    max_step=(ts[-1]-ts[0])/2000)
    # medida: ln|z| no fim vs inicio + previsao WKB congelada
    lnA = np.log(np.linalg.norm(sol.y[:, -1])/np.linalg.norm(sol.y[:, 0]))
    wkb = 0.0
    for i in range(len(Ns)-1):
        lam_i, _ = qep_reduzida(Kr_s[i], Cr_s[i], Wr_s[i])
        taxa = max(lam_i.real.max(), 0.0)
        wkb += taxa*(ts[i+1]-ts[i])
    return lnA, wkb, sol, ts

say("")
say("auto-teste (ii): espectador delta-chi deve oscilar sem crescer ...")
lnA, wkb, sol, ts = integra(1.0, modo='espectador')
say(f"    ln(amplificacao) do espectador = {lnA:+.3f}  "
    f"[{'PASSA (limitado)' if abs(lnA) < 1.5 else 'FALHA'}]")

say("")
say("=" * 66)
say("INTEGRACAO TEMPORAL — par relativo, fundo em movimento")
say("    trajetoria: a = 0.25 -> 2.0  (z = 3 -> -0.5)")
say("=" * 66)
for kv in (1.0, 10.0, 100.0):
    lnA, wkb, sol, ts = integra(kv, modo='instavel')
    razao = lnA/wkb if wkb > 0 else float('nan')
    say(f"  k={kv:6.1f}:  ln(ampl.) MEDIDO = {lnA:+8.3f}   "
        f"previsto (WKB congelado) = {wkb:+8.3f}   razao = {razao:5.2f}")

say("")
say("LEITURA:")
say("  razao ~ 1  -> o taquiao e GENUINO: o fundo em movimento nao doma")
say("               a instabilidade; o QEP congelado estava certo e o")
say("               ramo finito puro (beta const) reprova o setor escalar.")
say("  razao << 1 -> o congelamento ERA o artefato: a evolucao do fundo")
say("               (constraint dependente do tempo) remove/doma o modo.")
say("  ln(ampl.) medido ~ poucas unidades -> crescimento total modesto,")
say("               discutir se e observacionalmente toleravel.")
