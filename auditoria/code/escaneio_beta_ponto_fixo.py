# -*- coding: utf-8 -*-
"""
escaneio_beta_ponto_fixo.py — o taquiao existe para TODO beta?

Primeira etapa da extensao v2. Antes de construir a maquinaria de
modulacao por coeficiente, responde a pergunta que define o ALVO dela:
existe regiao de beta CONSTANTE onde o par escalar e saudavel?

Todos os testes escalares ate aqui usaram (beta_1, beta_2)=(1, -0.4),
herdados do benchmark da D1. O scan do Higuchi (ramo_dinamico_correto)
variou so (beta_0, beta_4). beta_1 e beta_2 — que entram no fator
estrutural e na cubica do fundo — nunca foram varridos.

Consequencias possiveis:
  - existe regiao saudavel cobrindo a historia toda -> beta constante
    resolve; modulacao volta a ser OPCIONAL;
  - existe regiao saudavel so no tardio -> a modulacao ganha um alvo
    preciso: beta_1(phi_-) deve levar o beta efetivo da regiao
    primordial ate la (condensacao de phi_- faz exatamente isso);
  - nao existe regiao saudavel -> a estabilizacao por mixing e a unica
    esperanca, e o prognostico e ruim (repulsao de niveis empurra o
    taquiao para BAIXO); reportar honestamente.

Estrutura: ponto fixo como filtro (la xi=r exato, quase-de Sitter
exato, sem caveat de congelamento) + checagem de historia nos
sobreviventes + Higuchi (forma fechada da D2) + Omega_m hoje.

Requer sympy, numpy, scipy.  ~2-4 min.
Uso:  python auditoria/code/escaneio_beta_ponto_fixo.py
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

# fixos (menos os beta a varrer); b3=0 (F1)
PBsub = {b3: 0.0,
         Mg2: 1.0, Mf2: 1.0, Meff2: 0.5, m2: 1.0,
         Fb: 1.0, Fp: 0.0, Fpp: 0.0,
         chid_s: 0.0, chidd_s: 0.0, Up: 0.0, Upp: 0.3,
         rho_s: 0.0, Hd_s: 0.0, Hfd_s: 0.0, xid_s: 0.0}
RHO_M0 = 0.3
REF = (1.0, -0.4, 1.0, 0.5)            # (b1,b2,b0,b4) do benchmark
SIGMA_REF_PF = 3.65                    # sigma/H no ponto fixo, k=1 (rodada ant.)

# ------------------------------ fundo generalizado -------------------
def fundo(N, B1, B2, B0, B4):
    """r, xi, H, Hf, Ub no instante N, para betas dados. None se o
    fundo nao existe (sem raiz positiva ou H^2<=0)."""
    a = np.exp(N)
    rho_til = RHO_M0 * a**-3 / 0.5
    rr = np.roots([B4 - 3*B2, -3*B1, 3*B2 - B0 - rho_til, B1])
    reais = sorted(z.real for z in rr if abs(z.imag) < 1e-9 and z.real > 1e-10)
    if not reais:
        return None
    r = reais[0]                                   # ramo finito
    dW = 2*B4*r - B1/r**2 - 3*B1 - 6*B2*r
    if abs(dW) < 1e-12:
        return None
    drdN = -3.0*rho_til/dW
    xi = r + drdN
    if xi <= 0:
        return None
    Vf = B4 + 3*B2/r**2 + B1/r**3
    H2 = 0.5*r*r*Vf/3.0
    if H2 <= 0:
        return None
    H = np.sqrt(H2)
    rho_int = 0.5*(B0 + 3*B1*r + 3*B2*r**2)
    Ubv = 3.0*H2 - rho_int
    return r, xi, H, H/r, Ubv, a, r*a

def higuchi_ok(r, xi, H, B1, B2):
    """m_T^2 >= 2H^2 com a forma fechada da D2 (F=1, b3=0)."""
    mT2 = 0.5*(1.0 + xi/r**3)*r*(B1 + B2*(xi + r))
    return mT2 >= 2.0*H*H, mT2

# ------------------------------ maquinaria ---------------------------
say("montando L2 (mesma acao/gauge da D1) ...")
L2s, fields, vels = d1.build_L2()
K7, C7, W7 = quadratic_matrices(L2s, fields, vels)
say("lambdificando com os beta LIVRES ...")
livres = (a_s, b_s, xi_s, H_s, Hf_s, Ub, ksym, b1, b2, b0, b4)
K7n = sp.lambdify(livres, K7.subs(PBsub), modules='numpy')
C7n = sp.lambdify(livres, C7.subs(PBsub), modules='numpy')
W7n = sp.lambdify(livres, W7.subs(PBsub), modules='numpy')

def sigma_em(N, kv, B1, B2, B0, B4):
    """sigma_max/H e kN minimo dos modos finitos; None se fundo nao existe."""
    f = fundo(N, B1, B2, B0, B4)
    if f is None:
        return None
    r, xi, H, Hf, Ubv, a, bb = f
    args = (a, bb, xi, H, Hf, Ubv, kv, B1, B2, B0, B4)
    Kn = np.array(K7n(*args), float)
    Cn = np.array(C7n(*args), float)
    Wn = np.array(W7n(*args), float)
    pares = d1.agrupa_pares(d1.qep_modes(Kn, Cn, Wn))
    sig = 0.0
    kNmin = np.inf
    for mm in pares:
        om = np.sqrt(complex(mm['omega2']))
        sig = max(sig, abs(om.imag))
        kNmin = min(kNmin, mm['knorm'])
    return sig/H, kNmin, f

# ------------------------------ auto-teste ---------------------------
say("")
say("auto-teste: ponto de referencia (1,-0.4,1,0.5) no ponto fixo")
res = sigma_em(np.log(10.0), 1.0, *REF)
sH, kN, f = res
say(f"    sigma/H = {sH:.3f}   esperado ~ {SIGMA_REF_PF}")
say(f"    Ub no ponto fixo = {f[4]:+.2e}   (identidade: deve ser ~0)")
ok = abs(sH - SIGMA_REF_PF) < 0.15*SIGMA_REF_PF and abs(f[4]) < 1e-3
say(f"    [{'PASSA' if ok else 'FALHA'}]")
if not ok:
    say("    !! abortando")
    sys.exit(1)

# ------------------------------ ESTAGIO 1: mapa no ponto fixo --------
say("")
say("=" * 68)
say("ESTAGIO 1 — saude do par no PONTO FIXO (a=10), k=10")
say("    grade beta_1 x beta_2, com beta_0=1, beta_4=0.5")
say("    simbolos:  X fundo inexistente | # taquiao (s/H>0.5)")
say("               ~ marginal (0.05<s/H<0.5) | . saudavel (s/H<0.05)")
say("=" * 68)

B1s = np.linspace(0.2, 2.0, 13)
B2s = np.linspace(-1.0, -0.05, 13)
NPF = np.log(10.0)
mapa = {}
say("")
say("           beta_2 ->  " + " ".join(f"{x:5.2f}" for x in B2s))
for B1v in B1s:
    linha = []
    for B2v in B2s:
        r = sigma_em(NPF, 10.0, B1v, B2v, 1.0, 0.5)
        if r is None:
            linha.append('X'); mapa[(B1v, B2v)] = None
            continue
        sH, kN, f = r
        mapa[(B1v, B2v)] = (sH, kN)
        linha.append('#' if sH > 0.5 else ('~' if sH > 0.05 else '.'))
    say(f"    beta_1={B1v:4.2f}   " + "     ".join(linha))

saudaveis = [(p, v) for p, v in mapa.items() if v and v[0] < 0.05]
marginais = [(p, v) for p, v in mapa.items() if v and 0.05 <= v[0] <= 0.5]
say("")
say(f"    saudaveis no ponto fixo: {len(saudaveis)} / {len(mapa)}")
say(f"    marginais:               {len(marginais)}")

# ------------------------------ ESTAGIO 2: historia dos sobreviventes
say("")
say("=" * 68)
say("ESTAGIO 2 — sobreviventes: historia (a=0.25, 0.5, 1) + Higuchi")
say("=" * 68)
candidatos = saudaveis + marginais
plenos = []
if not candidatos:
    say("    (nenhum candidato — pular)")
for (B1v, B2v), (sH_pf, _) in sorted(candidatos, key=lambda t: t[1][0]):
    hist = []
    hig_all = True
    ok_hist = True
    for aa in (0.25, 0.5, 1.0):
        rres = sigma_em(np.log(aa), 10.0, B1v, B2v, 1.0, 0.5)
        if rres is None:
            ok_hist = False
            hist.append('X')
            continue
        sH, kN, f = rres
        hig, mT2 = higuchi_ok(f[0], f[1], f[2], B1v, B2v)
        hig_all = hig_all and hig
        hist.append(f"{sH:5.2f}")
        if sH > 0.5:
            ok_hist = False
    fzero = fundo(0.0, B1v, B2v, 1.0, 0.5)
    Om = (RHO_M0/(3*fzero[2]**2)) if fzero else float('nan')
    tag = "HISTORIA LIMPA" if (ok_hist and hig_all) else \
          ("taquiao transiente" if hig_all else "viola Higuchi")
    say(f"    b1={B1v:4.2f} b2={B2v:5.2f}: pf={sH_pf:5.2f}  "
        f"hist(0.25/0.5/1)={'/'.join(hist)}  Om0={Om:4.2f}  [{tag}]")
    if ok_hist and hig_all:
        plenos.append((B1v, B2v))

# ------------------------------ veredito -----------------------------
say("")
say("=" * 68)
say("VEREDITO DO ESCANEIO")
say("=" * 68)
if plenos:
    say(f"  {len(plenos)} ponto(s) com HISTORIA LIMPA (escalar + Higuchi):")
    for p in plenos[:8]:
        say(f"    beta_1={p[0]:.2f}, beta_2={p[1]:.2f}")
    say("")
    say("  => beta CONSTANTE resolve: a TDCP-F1 corrigida e viavel sem")
    say("     modulacao. beta_n(phi_-) volta a ser extensao opcional")
    say("     (mecanismo da bifurcacao), nao reparo obrigatorio.")
elif saudaveis or marginais:
    say("  Existe regiao saudavel NO PONTO FIXO, mas nenhuma com a")
    say("  historia inteira limpa.")
    say("")
    say("  => A MODULACAO GANHA UM ALVO PRECISO: beta_1(phi_-) deve")
    say("     levar o beta efetivo da regiao primordial ate a regiao")
    say("     saudavel conforme phi_- condensa. Proximo passo: a")
    say("     maquinaria por-coeficiente, com a trajetoria-alvo")
    say("     lida deste mapa.")
else:
    say("  NENHUMA regiao saudavel encontrada nesta grade.")
    say("")
    say("  => Estabilizacao so por mixing (prognostico ruim: repulsao")
    say("     de niveis empurra o taquiao para baixo) ou o no-go do")
    say("     setor escalar bimetrico neste ramo. Ampliar a grade")
    say("     (beta_0, beta_4, hierarquia M_f/M_g) antes de concluir.")

os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
with open(os.path.join(HERE, "out", "escaneio_beta_ponto_fixo.txt"),
          "w", encoding="utf-8") as fh:
    fh.write("\n".join(OUT))
say("")
say("concluido. saida em auditoria/code/out/escaneio_beta_ponto_fixo.txt")
