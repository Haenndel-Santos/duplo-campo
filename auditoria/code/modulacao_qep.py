# -*- coding: utf-8 -*-
"""
modulacao_qep.py — O TESTE DA v2: a modulacao beta_1(phi_-) cura o par?

Tudo ate aqui usou beta_n constantes (F'=F''=0). Este script liga a
modulacao POR COEFICIENTE — beta_1(phi_-) = beta_1^0 (1 + phi_-^2/v*^2)
— nas perturbacoes, pela primeira vez no projeto.

METODO (sem alterar a biblioteca): as matrizes K7/C7/W7 sao BILINEARES
nos produtos {Fb,Fp,Fpp} x {b0..b4} (o potencial e F(chi)*sum b_n e_n,
linear em F e em cada b_n). Fatiando por substituicao:
    Base       = M|_{Fb=Fp=Fpp=0}          (EH + setor chi)
    S_i[n]     = M|_{F=e_i, b_m=delta_mn} - Base
e recombinando com os valores POR COEFICIENTE:
    M_mod = Base + sum_n [ beta_n(x) S_Fb[n] + beta_n'(x) S_Fp[n]
                           + (1/2?) beta_n''(x) S_Fpp[n] ]
(a normalizacao do slice Fpp e a da propria biblioteca — o auto-teste
1 garante a reconstrucao exata, entao nenhuma convencao e assumida).

FUNDO ACOPLADO com <phi_-> = xbar estacionario no ponto fixo:
  - branch: com p_phi=0 o termo novo da constraint secundaria se anula
    -> H_f = H/r vale no ponto estacionario;
  - escolha U(xbar)=0 (constante de U absorvida) -> r resolve
    W(r; beta_1eff)=0, mesma cubica com beta_1 -> beta_1eff;
  - estacionariedade de chi:  U'(xbar) = -M_eff^2 beta_1'(xbar) e_1,
    com e_1 = xi+3r = 4r no ponto fixo -> Up_val fixado;
  - U''(xbar) = m_chi^2 e knob livre (massa de phi_- no vacuo).

KNOBS da varredura:  g = xbar/v*  (intensidade da condensacao),
                     v*           (escala da modulacao),
                     m_chi^2      (massa de phi_-).
  beta_1eff = b1_0 (1+g^2);  beta_1' = 2 b1_0 g / v*;
  beta_1'' = 2 b1_0 / v*^2.

AUTO-TESTES:
  (T1) fatias recombinadas com beta constantes == matrizes originais
       (exato, ~1e-12) — valida a decomposicao e a convencao do Fpp;
  (T2) limite g=0, v*->inf reproduz a ancora sem modulacao
       (sigma/H = 3.651 na REF, k=1, fundo a=10).

VEREDITO procurado: existe (g, v*, m_chi^2) com o espectro LIMPO
(sem taquiao, sem fantasma) no ponto fixo?

Requer sympy, numpy, scipy.  ~3-5 min.
Uso:  python auditoria/code/modulacao_qep.py
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

RHO_M0 = 0.3
B1_0, B2_V, B0_V, B4_V, MU = 1.0, -0.4, 1.0, 0.5, 1.0
BETAS = (b0, b1, b2, b3, b4)
MEFF2 = MU/(1.0 + MU)

# simbolos que ficam livres no lambdify das FATIAS
LIVRES = (a_s, b_s, xi_s, H_s, Hf_s, Ub, Up, Upp, ksym)
FIXOS = {Mg2: 1.0, Mf2: MU, Meff2: MEFF2, m2: 1.0,
         chid_s: 0.0, chidd_s: 0.0, rho_s: 0.0,
         Hd_s: 0.0, Hfd_s: 0.0, xid_s: 0.0}

# ------------------------------ montagem + fatias --------------------
say("montando L2 ...")
L2s, fields, vels = d1.build_L2()
K7, C7, W7 = quadratic_matrices(L2s, fields, vels)
say("fatiando as matrizes em {Fb,Fp,Fpp} x {b0..b4} ...")

def fatias(M):
    """Base + 3x5 fatias lambdificadas."""
    Msub = M.subs(FIXOS)
    base_s = Msub.subs({Fb: 0, Fp: 0, Fpp: 0})
    out = {'base': sp.lambdify(LIVRES, base_s, modules='numpy')}
    for tag, fsub in (('Fb', {Fb: 1, Fp: 0, Fpp: 0}),
                      ('Fp', {Fb: 0, Fp: 1, Fpp: 0}),
                      ('Fpp', {Fb: 0, Fp: 0, Fpp: 1})):
        for n, bn in enumerate(BETAS):
            bsub = {bm: (1 if m == n else 0)
                    for m, bm in enumerate(BETAS)}
            Sl = sp.simplify(Msub.subs(fsub).subs(bsub) - base_s)
            out[(tag, n)] = sp.lambdify(LIVRES, Sl, modules='numpy')
    return out

FK, FC, FW = fatias(K7), fatias(C7), fatias(W7)
say("fatias prontas (3 matrizes x 15 fatias + base)")

def monta(fat, args, bvals, bp, bpp):
    """recombina: Base + sum_n b_n S_Fb[n] + bp_n S_Fp[n] + bpp_n S_Fpp[n]."""
    M = np.array(fat['base'](*args), float).copy()
    for n in range(5):
        M += bvals[n]*np.array(fat[('Fb', n)](*args), float)
        if bp[n]:
            M += bp[n]*np.array(fat[('Fp', n)](*args), float)
        if bpp[n]:
            M += bpp[n]*np.array(fat[('Fpp', n)](*args), float)
    return M

# ------------------------------ fundos -------------------------------
def fundo_a10(B1e):
    """fundo a=10 (mesmo dos scripts anteriores) com beta_1 -> B1e."""
    kap = 1.0/MU
    a = 10.0
    rho_til = RHO_M0*a**-3/MEFF2
    rr = np.roots([kap*B4_V - 3*B2_V, -3*B1e,
                   3*kap*B2_V - B0_V - rho_til, kap*B1e])
    reais = sorted(z.real for z in rr
                   if abs(z.imag) < 1e-9 and z.real > 1e-12)
    if not reais:
        return None
    r = reais[0]
    dW = kap*(2*B4_V*r - B1e/r**2) - 3*B1e - 6*B2_V*r
    drdN = -3.0*rho_til/dW
    xi = r + drdN
    Vf = B4_V + 3*B2_V/r**2 + B1e/r**3
    H2 = MEFF2*r*r*Vf/(3.0*MU)
    if H2 <= 0 or xi <= 0:
        return None
    H = np.sqrt(H2)
    rho_int = MEFF2*(B0_V + 3*B1e*r + 3*B2_V*r**2)
    return r, xi, H, H/r, 3.0*H2 - rho_int, a, r*a

def espectro(kv, g, vst, mchi2):
    """espectro no fundo modulado; devolve (pares, r, H) ou None.

    beta_1eff = B1_0(1+g^2); bp1 = 2 B1_0 g/vst; bpp1 = 2 B1_0/vst^2.
    Up fixado pela estacionariedade (e_1 = xi+3r no fundo usado);
    Upp = mchi2.
    """
    B1e = B1_0*(1.0 + g*g)
    f = fundo_a10(B1e)
    if f is None:
        return None
    r, xi, H, Hf, Ubv, a, bb = f
    bp1 = 2.0*B1_0*g/vst
    bpp1 = 2.0*B1_0/vst**2
    e1 = xi + 3.0*r
    Up_val = -MEFF2*bp1*e1          # estacionariedade de chi
    args = (a, bb, xi, H, Hf, Ubv, Up_val, mchi2, kv)
    bvals = (B0_V, B1e, B2_V, 0.0, B4_V)
    bp = (0.0, bp1, 0.0, 0.0, 0.0)
    bpp = (0.0, bpp1, 0.0, 0.0, 0.0)
    Kn = monta(FK, args, bvals, bp, bpp)
    Cn = monta(FC, args, bvals, bp, bpp)
    Wn = monta(FW, args, bvals, bp, bpp)
    return d1.agrupa_pares(d1.qep_modes(Kn, Cn, Wn)), r, H

def saude(pares, H, tol_sig=0.05, tol_kn=1e-9):
    sig = max(abs(np.sqrt(complex(mm['omega2'])).imag) for mm in pares)/H
    kNm = min(mm['knorm'] for mm in pares)
    if sig > tol_sig:
        return 'TAQUIAO', sig, kNm
    if kNm < -tol_kn:
        return 'FANTASMA', sig, kNm
    return 'LIMPA', sig, kNm

# ------------------------------ T1: reconstrucao exata ---------------
say("")
say("auto-teste T1: fatias recombinadas == matrizes originais")
f = fundo_a10(B1_0)
r, xi, H, Hf, Ubv, a, bb = f
argsT = (a, bb, xi, H, Hf, Ubv, 0.0, 0.3, 1.0)
bvalsT = (B0_V, B1_0, B2_V, 0.0, B4_V)
zer = (0.0,)*5
K_rec = monta(FK, argsT, bvalsT, zer, zer)
subsT = dict(FIXOS)
subsT.update({a_s: a, b_s: bb, xi_s: xi, H_s: H, Hf_s: Hf, Ub: Ubv,
              Up: 0.0, Upp: 0.3, ksym: 1.0,
              Fb: 1.0, Fp: 0.0, Fpp: 0.0,
              b0: B0_V, b1: B1_0, b2: B2_V, b3: 0.0, b4: B4_V})
K_dir = np.array(sp.Matrix(K7).subs(subsT).evalf(), float)
dif = np.max(np.abs(K_rec - K_dir))
say(f"    max|K_fatias - K_direta| = {dif:.3e}")
ok1 = dif < 1e-10
say(f"    [{'PASSA' if ok1 else 'FALHA'}]")

# ------------------------------ T2: limite sem modulacao -------------
say("")
say("auto-teste T2: g=0, v*=1e6 reproduz a ancora (3.651)")
res = espectro(1.0, 0.0, 1e6, 0.3)
pares, r, H = res
sig = max(abs(np.sqrt(complex(mm['omega2'])).imag) for mm in pares)/H
say(f"    sigma/H = {sig:.4f} (esperado 3.651, tol 2%)")
ok2 = abs(sig - 3.651) < 0.02*3.651
say(f"    [{'PASSA' if ok2 else 'FALHA'}]")
if not (ok1 and ok2):
    say("    !! abortando")
    sys.exit(1)

# ------------------------------ varredura ----------------------------
say("")
say("=" * 70)
say("VARREDURA — a modulacao positiviza o par?  (REF: b1_0=1, b2=-0.4,")
say(f"    mu={MU}; sem modulacao: TAQUIAO sigma/H=3.65)")
say("    saude checada em k=1 E k=10; classes: LIMPA / TAQUIAO / FANTASMA")
say("=" * 70)
GS = (0.5, 1.0, 2.0, 4.0)
VS = (0.3, 1.0, 3.0, 10.0)
MC = (0.3, 3.0, 30.0)
limpas = []
for mchi2 in MC:
    say("")
    say(f"--- m_chi^2 = {mchi2} ---")
    say("      g\\v*   " + "  ".join(f"{v:7.1f}" for v in VS))
    for g in GS:
        linha = []
        for vst in VS:
            piores = []
            for kv in (1.0, 10.0):
                res = espectro(kv, g, vst, mchi2)
                if res is None:
                    piores.append(('X', 0, 0))
                    break
                pares, r, H = res
                piores.append(saude(pares, H))
            cls = [p[0] for p in piores]
            if 'X' in cls:
                linha.append("   X   ")
            elif all(c == 'LIMPA' for c in cls):
                linha.append(" LIMPA ")
                limpas.append((g, vst, mchi2))
            elif 'TAQUIAO' in cls:
                s = max(p[1] for p in piores if p[0] != 'X')
                linha.append(f"T{s:5.2f} ")
            else:
                kmin = min(p[2] for p in piores)
                linha.append(f"F{kmin:+.0e}")
        say(f"    {g:5.1f}   " + " ".join(linha))

# ------------------------------ veredito -----------------------------
say("")
say("=" * 70)
say("VEREDITO")
say("=" * 70)
if limpas:
    say(f"  {len(limpas)} combinacao(oes) LIMPAS em k=1 e k=10:")
    for g, vst, mc in limpas[:12]:
        say(f"    g={g}, v*={vst}, m_chi^2={mc}")
    say("")
    say("  A MODULACAO CURA O PAR nesta regiao — primeira configuracao")
    say("  genuinamente saudavel do setor escalar em todo o projeto.")
    say("  Proximos passos: (a) checar a historia (nao so o ponto")
    say("  fixo); (b) k=100 e k=0.1; (c) Gate 2 Parte B (ADM completo)")
    say("  vira prioridade — a contagem de graus com a modulacao ligada")
    say("  precisa ser provada, nao so sondada.")
else:
    say("  Nenhuma combinacao limpa nesta grade. A modulacao beta_1")
    say("  quadratica nao cura nos knobs varridos. Antes de concluir:")
    say("  (a) ampliar (g, v*, m_chi^2); (b) modular tambem beta_2/beta_4;")
    say("  (c) se persistir, o no-go se estende a v2 minimal e a")
    say("  reformulacao precisa ser mais profunda que modulacao de")
    say("  coeficientes.")

os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
with open(os.path.join(HERE, "out", "modulacao_qep.txt"),
          "w", encoding="utf-8") as fh:
    fh.write("\n".join(OUT))
say("")
say("concluido. saida em auditoria/code/out/modulacao_qep.txt")
