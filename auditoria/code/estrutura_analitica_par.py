# -*- coding: utf-8 -*-
"""
estrutura_analitica_par.py — O QUE controla a doenca do par relativo?

O no-go empirico (docs/no_go_beta_constante.md) mostrou: taquiao
eterno em mu>=0.3, fantasma fraco em mu=0.1, em ~1500 pontos. Padrao
coerente demais para acidente. Este script extrai a ESTRUTURA:

ETAPA A (numerica, nao pode falhar):
  A1. composicao do autovetor patologico — quais dos 7 campos dominam
      o modo doente (setor f? shifts? delta-chi?) nos tres regimes
      (taquiao mu=1, fantasma mu=0.1, taquiao mu=100);
  A2. leis de escala — kN_fantasma vs mu e m2_taquiao vs mu em celula
      fixa: expoentes empiricos que uma futura forma fechada tem que
      reproduzir;
  A3. onde a doenca mora: fracao do autovetor em cada setor.

ETAPA B (simbolica, k=0 no ponto fixo — pode explodir; guardas e
  dumps parciais):
  B1. matrizes no ponto fixo com beta_0 eliminado por W(r)=0, xi=r,
      Ub=0, H^2 = M_eff^2 r^2 V_f/(3 mu): tudo em (r, b1, b2, b4, mu);
  B2. bloco de massa W(k=0): fatorar det/tr do bloco relevante ->
      a condicao analitica de taquiao;
  B3. auto-teste: avaliar as formas fechadas na referencia numerica.

A pergunta pratica que isto decide: a doenca e de MASSA (a modulacao
beta_1(phi_-) atua exatamente ai -> v2 pode consertar) ou CINETICA
(modulacao de massa nao atua -> v2 precisa de outro desenho)?

Requer sympy, numpy, scipy.  Etapa A ~1 min; Etapa B minutos ou
explosao declarada.
Uso:  python auditoria/code/estrutura_analitica_par.py
"""
import importlib.util
import os
import sys
import time

import numpy as np
import sympy as sp

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
OUT = []
def say(*a):
    line = " ".join(str(x) for x in a)
    print(f"[{time.time()-T0:7.1f}s] {line}")
    OUT.append(line)

PBsub = {b3: 0.0, Mg2: 1.0, m2: 1.0,
         Fb: 1.0, Fp: 0.0, Fpp: 0.0,
         chid_s: 0.0, chidd_s: 0.0, Up: 0.0, Upp: 0.3,
         rho_s: 0.0, Hd_s: 0.0, Hfd_s: 0.0, xid_s: 0.0}
RHO_M0 = 0.3
INF_CUT = 1e7

# ------------------------------ fundos -------------------------------
def ponto_fixo(B1, B2, B0, B4, mu):
    """raiz de W(r)=0 (rho=0 EXATO) — usado so na Etapa B simbolica."""
    kap = 1.0/mu
    Meff2v = mu/(1.0 + mu)
    rr = np.roots([kap*B4 - 3*B2, -3*B1, 3*kap*B2 - B0, kap*B1])
    reais = sorted(z.real for z in rr if abs(z.imag) < 1e-9 and z.real > 1e-12)
    if not reais:
        return None
    r = reais[0]
    Vf = B4 + 3*B2/r**2 + B1/r**3
    H2 = Meff2v*r*r*Vf/(3.0*mu)
    if H2 <= 0:
        return None
    return r, np.sqrt(H2), Meff2v


def fundo_a10(B1, B2, B0, B4, mu):
    """MESMO fundo dos scripts de escaneio (a=10, rho=3e-4): e nele
    que as ancoras numericas (3.651, -1.6e-5) foram medidas."""
    kap = 1.0/mu
    Meff2v = mu/(1.0 + mu)
    a = 10.0
    rho = RHO_M0 * a**-3
    rho_til = rho / Meff2v
    rr = np.roots([kap*B4 - 3*B2, -3*B1, 3*kap*B2 - B0 - rho_til, kap*B1])
    r_esc = max(1e-14, 1e-6*kap*B1/max(rho_til, 1.0))
    reais = sorted(z.real for z in rr
                   if abs(z.imag) < 1e-9 and z.real > r_esc)
    if not reais:
        return None
    r = reais[0]
    dW = kap*(2*B4*r - B1/r**2) - 3*B1 - 6*B2*r
    drdN = -3.0*rho_til/dW
    xi = r + drdN
    if xi <= 0:
        return None
    Vf = B4 + 3*B2/r**2 + B1/r**3
    H2 = Meff2v*r*r*Vf/(3.0*mu)
    if H2 <= 0:
        return None
    H = np.sqrt(H2)
    rho_int = Meff2v*(B0 + 3*B1*r + 3*B2*r**2)
    return r, xi, H, H/r, 3.0*H2 - rho_int, a, r*a

# ------------------------------ maquinaria ---------------------------
say("montando L2 ...")
L2s, fields, vels = d1.build_L2()
K7, C7, W7 = quadratic_matrices(L2s, fields, vels)
NOMES = [str(f) for f in fields]
say(f"campos (ordem): {NOMES}")
livres = (a_s, b_s, xi_s, H_s, Hf_s, Ub, ksym, b1, b2, b0, b4, Mf2, Meff2)
K7n = sp.lambdify(livres, K7.subs(PBsub), modules='numpy')
C7n = sp.lambdify(livres, C7.subs(PBsub), modules='numpy')
W7n = sp.lambdify(livres, W7.subs(PBsub), modules='numpy')

def modos_a10(kv, B1, B2, B0, B4, mu):
    """modos da BIBLIOTECA (d1.qep_modes — mesma rota das ancoras),
    no fundo a=10; devolve (pares, r, H) ou None."""
    f = fundo_a10(B1, B2, B0, B4, mu)
    if f is None:
        return None
    r, xi, H, Hf, Ubv, a, bb = f
    Meff2v = mu/(1.0 + mu)
    args = (a, bb, xi, H, Hf, Ubv, kv, B1, B2, B0, B4, mu, Meff2v)
    Kn = np.array(K7n(*args), float)
    Cn = np.array(C7n(*args), float)
    Wn = np.array(W7n(*args), float)
    return d1.agrupa_pares(d1.qep_modes(Kn, Cn, Wn)), r, H

def pior_modo(modos, H):
    """o modo patologico: maior sigma; empate -> knorm mais negativo."""
    def chave(mm):
        om = np.sqrt(complex(mm['omega2']))
        return (abs(om.imag)/H, -mm['knorm'])
    return max(modos, key=chave)

def composicao(v):
    p = np.abs(v)**2
    p = p/p.sum()
    return " ".join(f"{NOMES[i]}:{p[i]:.2f}" for i in np.argsort(-p)[:4])

# ------------------------------ auto-teste ---------------------------
# rota IDENTICA a das ancoras: d1.qep_modes + fundo a=10
say("")
say("auto-teste: rota da biblioteca vs ancoras conhecidas (fundo a=10)")
pares, r, H = modos_a10(1.0, 1.0, -0.4, 1.0, 0.5, 1.0)
mm = pior_modo(pares, H)
sig = abs(np.sqrt(complex(mm['omega2'])).imag)/H
say(f"    mu=1  REF k=1: sigma/H = {sig:.4f} (esperado 3.651)")
ok1 = abs(sig - 3.651) < 0.02*3.651
pares, r, H = modos_a10(1.0, 0.20, -1.00, 1.0, 0.5, 0.1)
kNmin = min(m['knorm'] for m in pares)
say(f"    mu=0.1 (0.20,-1.00) k=1: kN_min = {kNmin:+.3e} "
    f"(esperado ~ -1.6e-05)")
ok2 = -1e-3 < kNmin < -1e-6
say(f"    [{'PASSA' if ok1 and ok2 else 'FALHA'}]")
if not (ok1 and ok2):
    say("    !! abortando: rota nao reproduz as ancoras")
    sys.exit(1)

# ------------------------------ ETAPA A ------------------------------
say("")
say("=" * 70)
say("ETAPA A1 — composicao do autovetor patologico (ponto fixo, k=1)")
say("=" * 70)
CASOS = [
    ("taquiao mu=1 (REF)",       1.0, -0.4, 1.0, 0.5, 1.0),
    ("taquiao mu=100 (REF)",     1.0, -0.4, 1.0, 0.5, 100.0),
    ("fantasma mu=0.1 fraco",    0.20, -1.00, 1.0, 0.5, 0.1),
    ("fantasma mu=0.1 forte",    1.25, -1.00, 1.0, 0.5, 0.1),
]
for nome, B1v, B2v, B0v, B4v, mu in CASOS:
    Mx = modos_a10(1.0, B1v, B2v, B0v, B4v, mu)
    if Mx is None:
        say(f"  {nome}: fundo inexistente")
        continue
    pares, r, H = Mx
    mm = pior_modo(pares, H)
    w2 = complex(mm['omega2'])
    om = np.sqrt(w2)
    say(f"  {nome}  (r_pf={r:.4f}):")
    say(f"      w2={w2.real:+.4e}{w2.imag:+.2e}i  "
        f"sigma/H={abs(om.imag)/H:.3f}  kN={mm['knorm']:+.3e}")
    say(f"      composicao: {composicao(mm['v'])}")
    # e tambem o modo de kN mais negativo (nem sempre e o mesmo)
    mg = min(pares, key=lambda m: m['knorm'])
    if mg is not mm and mg['knorm'] < 0:
        w2g = complex(mg['omega2'])
        say(f"      modo de kN minimo: w2={w2g.real:+.4e}  "
            f"kN={mg['knorm']:+.3e}")
        say(f"      composicao: {composicao(mg['v'])}")

say("")
say("=" * 70)
say("ETAPA A2 — leis de escala em mu (celula fixa b1=0.5, b2=-0.84)")
say("=" * 70)
say(f"    {'mu':>7} {'r_pf':>9} {'sigma/H':>9} {'kN_min':>12}")
esc = []
for mu in (0.02, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 5.0):
    Mx = modos_a10(1.0, 0.5, -0.84, 1.0, 0.5, mu)
    if Mx is None:
        say(f"    {mu:7.2f}  (fundo inexistente)")
        continue
    pares, r, H = Mx
    mm = pior_modo(pares, H)
    sig = abs(np.sqrt(complex(mm['omega2'])).imag)/H
    kNmin = min(m['knorm'] for m in pares)
    say(f"    {mu:7.2f} {r:9.5f} {sig:9.3f} {kNmin:+12.3e}")
    esc.append((mu, sig, kNmin))
# expoente empirico do kN na regiao de fantasma (sig~0)
fant = [(mu, kN) for mu, sig, kN in esc if sig < 0.05 and kN < 0]
if len(fant) >= 2:
    mus = np.log([f[0] for f in fant])
    kns = np.log([-f[1] for f in fant])
    p = np.polyfit(mus, kns, 1)[0]
    say(f"    expoente empirico: |kN_fantasma| ~ mu^{p:.2f}")

# ------------------------------ ETAPA B ------------------------------
say("")
say("=" * 70)
say("ETAPA B — forma fechada em k=0 no ponto fixo (pode explodir)")
say("=" * 70)
try:
    rS = sp.Symbol('r', positive=True)
    muS = sp.Symbol('mu', positive=True)
    kapS = 1/muS
    Meff2S = muS/(1 + muS)
    VfS = b4 + 3*b2/rS**2 + b1/rS**3
    b0_elim = sp.expand(kapS*rS**2*VfS - 3*b1*rS - 3*b2*rS**2)
    H2S = Meff2S*rS**2*VfS/(3*muS)
    HS = sp.sqrt(H2S)
    subsB = dict(PBsub)
    subsB.update({ksym: 0, a_s: 1, b_s: rS, xi_s: rS,
                  H_s: HS, Hf_s: HS/rS, Ub: 0,
                  b0: b0_elim, Mf2: muS, Meff2: Meff2S})
    say("  substituindo (k=0, xi=r, Ub=0, beta_0 eliminado por W=0) ...")
    W0 = sp.Matrix(W7).subs(subsB)
    K0 = sp.Matrix(K7).subs(subsB)
    say(f"  simplificando W(k=0) ({sum(sp.count_ops(x) for x in W0)} ops) ...")
    W0 = W0.applyfunc(lambda e: sp.cancel(sp.together(e)))
    K0 = K0.applyfunc(lambda e: sp.cancel(sp.together(e)))
    nops = sum(sp.count_ops(x) for x in W0)
    say(f"  W(k=0) simplificada: {nops} ops")

    # estrutura de blocos: quais campos tem massa/mistura em k=0?
    say("")
    say("  linhas nao-nulas de W(k=0) (estrutura de acoplamento):")
    for i in range(7):
        nz = [NOMES[j] for j in range(7) if W0[i, j] != 0]
        if nz:
            say(f"    {NOMES[i]:8s} <-> {nz}")

    # bloco de massa do par: subespaco dos campos com W nao-nulo
    idx = [i for i in range(7)
           if any(W0[i, j] != 0 for j in range(7))]
    Wb = W0[idx, idx]
    say("")
    say(f"  bloco de massa ({len(idx)}x{len(idx)}): campos "
        f"{[NOMES[i] for i in idx]}")
    detW = sp.factor(sp.cancel(Wb.det()))
    trW = sp.factor(sp.cancel(sp.trace(Wb)))
    say("")
    say("  det(bloco de massa) fatorado:")
    say(f"    {detW}")
    say("")
    say("  tr(bloco de massa) fatorado:")
    say(f"    {trW}")

    # auto-teste da forma fechada contra a rota numerica no MESMO
    # ponto (ponto fixo exato: a=1, b=r, xi=r, Ub=0, k~0)
    say("")
    say("  auto-teste: forma fechada vs lambdify na REF (mu=1) ...")
    pf = ponto_fixo(1.0, -0.4, 1.0, 0.5, 1.0)
    r_n, H_n, Meff2_n = pf
    subsN = {rS: r_n, muS: 1.0, b1: 1.0, b2: -0.4, b4: 0.5}
    W0num = np.array(W0.subs(subsN).evalf(), float)
    argsN = (1.0, r_n, r_n, H_n, H_n/r_n, 0.0, 1e-8,
             1.0, -0.4, 1.0, 0.5, 1.0, Meff2_n)
    Wdir = np.array(W7n(*argsN), float)
    dif = np.max(np.abs(W0num - Wdir))
    say(f"    max|W_simbolica - W_lambdify(k=1e-8)| = {dif:.3e}")
    say(f"    [{'PASSA' if dif < 1e-6 else 'FALHA'}]")
    if dif >= 1e-6:
        say("    !! divergencia: a eliminacao simbolica de beta_0 nao")
        say("       bate com a avaliacao direta — investigar antes de")
        say("       usar o det/tr acima")
except Exception as e:
    say(f"  !! ETAPA B abortou: {type(e).__name__}: {e}")
    say("  (a Etapa A acima permanece valida; a forma fechada fica")
    say("   para uma rodada com mais simplificacao dirigida)")

os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
with open(os.path.join(HERE, "out", "estrutura_analitica_par.txt"),
          "w", encoding="utf-8") as fh:
    fh.write("\n".join(OUT))
say("")
say("concluido. saida em auditoria/code/out/estrutura_analitica_par.txt")
