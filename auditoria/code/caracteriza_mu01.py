# -*- coding: utf-8 -*-
"""
caracteriza_mu01.py — a regiao saudavel de mu=0.1 e GENUINA?

O escaneio de hierarquia encontrou 35+1 celulas com sigma/H = 0 no
ponto fixo em mu = M_f^2/M_g^2 = 0.1 (hierarquia INVERTIDA — setor f
mais leve), todas com historia transiente taquionica (sigma/H ~ 8 em
a=0.25 caindo a ~3 em a=1 e a 0 no ponto fixo).

LACUNA A FECHAR (deste proprio projeto): a classificacao 'saudavel'
usou SO sigma — nao checou o sinal das normas cineticas. Uma celula
sem taquiao pode ainda ter FANTASMA (kN<0 com omega^2 real positivo).
Se a regiao trocou taquiao por fantasma, o achado evapora.

Este script:
  (1) inventario COMPLETO de modos (todos os omega^2 e kN) nas
      celulas candidatas de mu=0.1, no ponto fixo, k=1 e k=10;
      classifica: LIMPA (sem taquiao E sem fantasma) / FANTASMA /
      taquiao residual;
  (2) para as melhores celulas LIMPAS: rastreio denso sigma(N) e
      kN_min(N) de a=0.1 a a=10 + ln A acumulado na janela
      observacional (a=0.25 -> 2) — a pergunta quantitativa que volta
      a decidir, ja que o taquiao transiente nao e no-go automatico;
  (3) veredito: existe celula com ponto fixo LIMPO de verdade?

Requer sympy, numpy, scipy.  ~2-3 min.
Uso:  python auditoria/code/caracteriza_mu01.py
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
MU = 0.1
NPF = np.log(10.0)

# tolerancias de classificacao no ponto fixo
TOL_TAQ = 0.05      # |Im omega|/H acima disso = taquiao/instavel
TOL_KN = 1e-9       # kN abaixo de -TOL_KN = fantasma
KN_ESPEC = 0.5      # norma do espectador delta-chi (referencia)

# ------------------------------ fundo (identico ao escaneio) ---------
def fundo(N, B1, B2, B0, B4, mu):
    kap = 1.0/mu
    Meff2v = mu/(1.0 + mu)
    a = np.exp(N)
    rho = RHO_M0 * a**-3
    rho_til = rho / Meff2v
    rr = np.roots([kap*B4 - 3*B2, -3*B1, 3*kap*B2 - B0 - rho_til, kap*B1])
    r_esc = max(1e-14, 1e-6*kap*B1/max(rho_til, 1.0))
    reais = sorted(z.real for z in rr
                   if abs(z.imag) < 1e-9 and z.real > r_esc)
    if not reais:
        return 'sem_raiz'
    r = reais[0]
    dW = kap*(2*B4*r - B1/r**2) - 3*B1 - 6*B2*r
    if abs(dW) < 1e-12:
        return 'sem_raiz'
    drdN = -3.0*rho_til/dW
    xi = r + drdN
    if xi <= 0:
        return 'xi_neg'
    Vf = B4 + 3*B2/r**2 + B1/r**3
    H2 = Meff2v*r*r*Vf/(3.0*mu)
    if H2 <= 0:
        return 'H2_neg'
    H = np.sqrt(H2)
    rho_int = Meff2v*(B0 + 3*B1*r + 3*B2*r**2)
    return r, xi, H, H/r, 3.0*H2 - rho_int, a, r*a

# ------------------------------ maquinaria ---------------------------
say("montando L2 (mesma acao/gauge da D1) ...")
L2s, fields, vels = d1.build_L2()
K7, C7, W7 = quadratic_matrices(L2s, fields, vels)
say("lambdificando ...")
livres = (a_s, b_s, xi_s, H_s, Hf_s, Ub, ksym, b1, b2, b0, b4, Mf2, Meff2)
K7n = sp.lambdify(livres, K7.subs(PBsub), modules='numpy')
C7n = sp.lambdify(livres, C7.subs(PBsub), modules='numpy')
W7n = sp.lambdify(livres, W7.subs(PBsub), modules='numpy')

def modos(N, kv, B1, B2, B0, B4, mu):
    f = fundo(N, B1, B2, B0, B4, mu)
    if isinstance(f, str):
        return f, None
    r, xi, H, Hf, Ubv, a, bb = f
    Meff2v = mu/(1.0 + mu)
    args = (a, bb, xi, H, Hf, Ubv, kv, B1, B2, B0, B4, mu, Meff2v)
    Kn = np.array(K7n(*args), float)
    Cn = np.array(C7n(*args), float)
    Wn = np.array(W7n(*args), float)
    return d1.agrupa_pares(d1.qep_modes(Kn, Cn, Wn)), f

def classifica_pf(pares, H):
    """(classe, detalhe) da celula no ponto fixo, olhando TODOS os
    modos: taquiao (sigma), fantasma (kN<0 com modo propagante) ou
    LIMPA. O espectador (kN~+0.5) e identificado e nao conta contra."""
    sig_max = 0.0
    kn_ruins = []
    for mm in pares:
        w2 = complex(mm['omega2'])
        om = np.sqrt(w2)
        sig_max = max(sig_max, abs(om.imag))
        kn = mm['knorm']
        if kn < -TOL_KN:
            kn_ruins.append((kn, w2.real))
    if sig_max/H > TOL_TAQ:
        return 'TAQUIAO', f"sigma/H={sig_max/H:.2f}"
    if kn_ruins:
        pior = min(kn_ruins)[0]
        return 'FANTASMA', f"kN_min={pior:+.3e} ({len(kn_ruins)} modo(s))"
    return 'LIMPA', ""

# ------------------------------ auto-teste ---------------------------
say("")
say("auto-teste: referencia (1,-0.4,1,0.5) mu=1 k=1 no ponto fixo")
pares, f = modos(NPF, 1.0, 1.0, -0.4, 1.0, 0.5, 1.0)
sig = max(abs(np.sqrt(complex(mm['omega2'])).imag) for mm in pares)
say(f"    sigma/H = {sig/f[2]:.4f}  (esperado 3.651, tol 2%)")
if abs(sig/f[2] - 3.651) > 0.02*3.651:
    say("    [FALHA] — abortando")
    sys.exit(1)
say("    [PASSA]")

# ------------------------------ (1) inventario nas candidatas --------
say("")
say("=" * 70)
say("(1) INVENTARIO DE MODOS — celulas candidatas de mu=0.1, ponto fixo")
say(f"    criterio LIMPA: sem taquiao (sigma/H<{TOL_TAQ}) E sem fantasma")
say(f"    (kN<-{TOL_KN:g} em qualquer modo). Checado em k=1 E k=10.")
say("=" * 70)

# as 36 celulas candidatas do escaneio (regiao saudavel/marginal)
B1s = np.linspace(0.2, 2.0, 13)
B2s = np.linspace(-1.0, -0.05, 13)
candidatas = []
for B1v in B1s:
    for B2v in B2s:
        r = modos(NPF, 10.0, B1v, B2v, 1.0, 0.5, MU)
        if isinstance(r[0], str):
            continue
        pares, f = r
        sig = max(abs(np.sqrt(complex(mm['omega2'])).imag) for mm in pares)
        if sig/f[2] <= 0.5:
            candidatas.append((B1v, B2v))

say(f"    candidatas re-detectadas: {len(candidatas)} (esperado ~36)")
say("")
limpas = []
for B1v, B2v in candidatas:
    classes = []
    for kv in (1.0, 10.0):
        pares, f = modos(NPF, kv, B1v, B2v, 1.0, 0.5, MU)
        cl, det = classifica_pf(pares, f[2])
        classes.append((kv, cl, det))
    pior = ('LIMPA' if all(c[1] == 'LIMPA' for c in classes)
            else next(c[1] for c in classes if c[1] != 'LIMPA'))
    det = "; ".join(f"k={c[0]:g}:{c[1]}{(' '+c[2]) if c[2] else ''}"
                    for c in classes)
    say(f"    b1={B1v:4.2f} b2={B2v:5.2f}: [{pior:8s}] {det}")
    if pior == 'LIMPA':
        limpas.append((B1v, B2v))

say("")
say(f"    LIMPAS de verdade (sem taquiao E sem fantasma, k=1 e 10): "
    f"{len(limpas)}/{len(candidatas)}")

# ------------------------------ (2) rastreio das melhores ------------
if limpas:
    say("")
    say("=" * 70)
    say("(2) RASTREIO sigma(N), kN_min(N) e ln A — melhores celulas LIMPAS")
    say("=" * 70)
    Ns = np.linspace(np.log(0.10), np.log(10.0), 37)
    for B1v, B2v in limpas[:3]:
        say("")
        say(f"--- b1={B1v:.2f}, b2={B2v:.2f}, mu={MU} ---")
        say(f"    {'a':>7} {'r':>9} {'sigma/H':>9} {'kN_min':>11}")
        sig_tr, H_tr = [], []
        for N in Ns:
            r = modos(N, 10.0, B1v, B2v, 1.0, 0.5, MU)
            if isinstance(r[0], str):
                sig_tr.append(np.nan); H_tr.append(np.nan)
                continue
            pares, f = r
            sig = max(abs(np.sqrt(complex(mm['omega2'])).imag)
                      for mm in pares)
            knm = min(mm['knorm'] for mm in pares)
            sig_tr.append(sig); H_tr.append(f[2])
            if any(abs(N - x) < 0.06 for x in
                   (np.log(0.1), np.log(0.25), np.log(0.5), 0.0,
                    np.log(2.0), np.log(10.0))):
                say(f"    {np.exp(N):7.2f} {f[0]:9.5f} {sig/f[2]:9.3f} "
                    f"{knm:11.3e}")
        sig_tr = np.array(sig_tr); H_tr = np.array(H_tr)
        jan = (Ns >= np.log(0.25)) & (Ns <= np.log(2.0)) & \
              np.isfinite(sig_tr)
        lnA = float(np.trapezoid((sig_tr/H_tr)[jan], Ns[jan]))
        say(f"    ln A acumulado na janela a=0.25->2:  {lnA:6.1f}   "
            f"(amplificacao ~ e^{lnA:.0f})")

# ------------------------------ veredito -----------------------------
say("")
say("=" * 70)
say("VEREDITO")
say("=" * 70)
if limpas:
    say(f"  {len(limpas)} celula(s) de mu=0.1 com ponto fixo GENUINAMENTE")
    say("  limpo (sem taquiao e sem fantasma). O taquiao e TRANSIENTE")
    say("  nessas celulas — o no-go do taquiao eterno nao se aplica.")
    say("")
    say("  A pergunta que decide passa a ser QUANTITATIVA: o ln A do")
    say("  transiente (acima) e tolerabel? Caminhos:")
    say("  - se ln A ~ poucos: regiao viavel SEM modulacao — a TDCP-F1")
    say("    corrigida com hierarquia invertida e candidata direta;")
    say("  - se ln A ~ 10+: o transiente e catastrofico em teoria")
    say("    linear — mas e exatamente a era que a condensacao de")
    say("    phi_- da v2 deveria absorver (o taquiao E a bifurcacao);")
    say("    o alvo da modulacao fica definido por este mapa.")
else:
    say("  NENHUMA celula sobrevive a checagem de fantasma: a regiao")
    say("  'saudavel' de mu=0.1 trocou taquiao por fantasma. O no-go")
    say("  do setor escalar se estende a hierarquia invertida — segue")
    say("  para a extracao analitica da estrutura do m^2 do par.")

os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
with open(os.path.join(HERE, "out", "caracteriza_mu01.txt"),
          "w", encoding="utf-8") as fh:
    fh.write("\n".join(OUT))
say("")
say("concluido. saida em auditoria/code/out/caracteriza_mu01.txt")
