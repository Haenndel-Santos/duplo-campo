# -*- coding: utf-8 -*-
"""
evolucao_temporal_escalar.py (v2) — o congelamento e confiavel?

HISTORICO (faz parte do resultado). A v1 deste script tentou integrar
as perturbacoes no tempo eliminando os 4 multiplicadores por linhas
nulas de K. O auto-teste de particao abortou: "7 dinamicos, 0
auxiliares". A suposicao era FALSA — na forma Gamma-Gamma, velocidades
de lapso/shift aparecem em termos cruzados (Phidot*psidot), entao
nenhuma linha de K e nula; K e singular por COMBINACOES nao alinhadas
com campos, que giram com o fundo. A eliminacao exigiria
Faddeev-Jackiw dependente do tempo com base continua — projeto grande
e fragil. (A guarda funcionou como desenhada: abortou alto.)

ESTA VERSAO responde a mesma pergunta por dois criterios padrao,
usando SO a maquinaria ja validada (QEP 7x7 da D1):

  (1) ADIABATICIDADE: o QEP congelado e confiavel onde
          eta(N) = |d sigma/dt| / sigma^2  << 1,
      com sigma(N) = taxa de crescimento do modo mais instavel.
      Se eta << 1 ao longo da trajetoria, o taquiao congelado e
      genuino e o crescimento acumulado e integral de sigma dt.

  (2) PONTO FIXO COMO JUIZ ASSINTOTICO: em a -> infinito o fundo
      assenta em r_inf (raiz de W(r)=0, aqui ~0.332) com rdot -> 0 —
      quase-de Sitter EXATO, onde a analise congelada nao tem caveat.
      sigma(ponto fixo) > 0  =>  taquiao eterno, genuino, veredito
      fechado. sigma -> 0 antes  =>  instabilidade transiente.

Saidas: sigma(N)/H, eta(N), crescimento acumulado, e o veredito do
ponto fixo, para k = 1, 10, 100.

Requer sympy, numpy, scipy.  ~1-2 min.
Uso:  python auditoria/code/evolucao_temporal_escalar.py
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

# ------------------------- parametros (identicos ao d1_ramo_finito) --
PBnum = {b0: 1.0, b1: 1.0, b2: -0.4, b3: 0.0, b4: 0.5,
         Mg2: 1.0, Mf2: 1.0, Meff2: 0.5, m2: 1.0,
         Fb: 1.0, Fp: 0.0, Fpp: 0.0,
         chid_s: 0.0, chidd_s: 0.0, Up: 0.0, Upp: 0.3,
         rho_s: 0.0,
         Hd_s: 0.0, Hfd_s: 0.0, xid_s: 0.0}
RHO_M0 = 0.3
ESPERADO_A1_K1 = [1.3000, 3.8578, -8.4750]     # rodada 2 (via sympy-subs)

# ------------------------------ fundo (ramo finito) ------------------
# W(r) = 1.7 r^2 - 3r + 1/r - 2.2  ;  W'(r) = 3.4 r - 3 - 1/r^2
def dW_dr(r):
    return 3.4*r - 3.0 - 1.0/r**2

def raiz_finita(rho_til):
    rr = np.roots([1.7, -3.0, -(2.2 + rho_til), 1.0])
    reais = sorted(z.real for z in rr if abs(z.imag) < 1e-9 and z.real > 1e-10)
    return reais[0]

def fundo_em(N):
    a = np.exp(N)
    rho = RHO_M0 * a**-3
    rho_til = rho / 0.5
    r = raiz_finita(rho_til)
    drdN = -3.0*rho_til/dW_dr(r)
    xi = r + drdN
    Vf = 0.5 - 1.2/r**2 + 1.0/r**3
    H2 = 0.5*r*r*Vf/3.0
    H = np.sqrt(H2)
    rho_int = 0.5*(1.0 + 3.0*r - 1.2*r**2)
    Ubv = 3.0*H2 - rho_int          # ja com o truque materia->Ub embutido
    return r, xi, H, H/r, Ubv, a, r*a

# ------------------------------ matrizes ----------------------------
say("montando L2 (mesma acao/gauge da D1) ...")
L2s, fields, vels = d1.build_L2()
K7, C7, W7 = quadratic_matrices(L2s, fields, vels)
say("lambdificando (a,b,xi,H,Hf,Ub,k) ...")
livres = (a_s, b_s, xi_s, H_s, Hf_s, Ub, ksym)
K7n = sp.lambdify(livres, K7.subs(PBnum), modules='numpy')
C7n = sp.lambdify(livres, C7.subs(PBnum), modules='numpy')
W7n = sp.lambdify(livres, W7.subs(PBnum), modules='numpy')

def modos_em(N, kv):
    r, xi, H, Hf, Ubv, a, b = fundo_em(N)
    args = (a, b, xi, H, Hf, Ubv, kv)
    Kn = np.array(K7n(*args), float)
    Cn = np.array(C7n(*args), float)
    Wn = np.array(W7n(*args), float)
    return d1.agrupa_pares(d1.qep_modes(Kn, Cn, Wn)), H

def taxa_sigma(pares):
    """maior taxa de crescimento entre os modos: sigma = |Im sqrt(w2)|."""
    sig = 0.0
    for mm in pares:
        om = np.sqrt(complex(mm['omega2']))
        sig = max(sig, abs(om.imag))
    return sig

# ------------------------------ auto-teste ---------------------------
say("")
say("auto-teste: rota lambdify em a=1, k=1 deve reproduzir a rodada 2")
pares, H1 = modos_em(0.0, 1.0)
w2s = sorted(round(mm['omega2'].real, 3) for mm in pares)
say(f"    omega^2 = {w2s}   esperado ~ {sorted(ESPERADO_A1_K1)}")
ok = all(any(abs(e-v) < 2e-2*max(1, abs(e)) for v in w2s)
         for e in ESPERADO_A1_K1)
say(f"    [{'PASSA' if ok else 'FALHA'}]")
if not ok:
    say("    !! rota lambdify nao validada — abortando")
    sys.exit(1)

# ------------------------------ rastreio sigma(N) --------------------
say("")
say("=" * 68)
say("RASTREIO sigma(N) — taxa de crescimento ao longo da trajetoria")
say("    a: 0.10 -> 10.0   (o fim aproxima o ponto fixo r_inf~0.332)")
say("=" * 68)

Ns = np.linspace(np.log(0.10), np.log(10.0), 47)
resultado = {}
for kv in (1.0, 10.0, 100.0):
    sig, Hs = [], []
    for N in Ns:
        pares, H = modos_em(N, kv)
        sig.append(taxa_sigma(pares))
        Hs.append(H)
    sig = np.array(sig); Hs = np.array(Hs)
    resultado[kv] = (sig, Hs)

    # adiabaticidade: eta = |dsig/dt|/sig^2 = |dsig/dN| * H / sig^2
    dsig = np.gradient(sig, Ns)
    with np.errstate(divide='ignore', invalid='ignore'):
        eta = np.abs(dsig)*Hs/np.maximum(sig, 1e-30)**2
    mask = sig > 0.1*Hs
    eta_max = float(np.nanmax(eta[mask])) if mask.any() else float('nan')

    # crescimento acumulado ln A = int sigma dt = int (sigma/H) dN
    janela = (Ns >= np.log(0.25)) & (Ns <= np.log(2.0))
    lnA_janela = float(np.trapezoid((sig/Hs)[janela], Ns[janela]))
    lnA_total = float(np.trapezoid(sig/Hs, Ns))

    say("")
    say(f"--- k = {kv:.0f} ---")
    say(f"    {'a':>7} {'r':>7} {'sigma/H':>9}   (amostras)")
    for N in (np.log(0.1), np.log(0.25), np.log(0.5), 0.0,
              np.log(2.0), np.log(5.0), np.log(10.0)):
        i = int(np.argmin(np.abs(Ns - N)))
        r_i = fundo_em(Ns[i])[0]
        say(f"    {np.exp(Ns[i]):7.2f} {r_i:7.4f} {sig[i]/Hs[i]:9.3f}")
    say(f"    adiabaticidade max (onde sigma>0.1H): eta = {eta_max:.3f}"
        f"   [{'congelado CONFIAVEL' if eta_max < 1 else 'congelado DUVIDOSO'}]")
    say(f"    crescimento acumulado ln A: janela a=0.25->2: "
        f"{lnA_janela:6.1f}   total a=0.1->10: {lnA_total:6.1f}")

# ------------------------------ o juiz assintotico -------------------
say("")
say("=" * 68)
say("PONTO FIXO (a=10, r~r_inf, rdot~0): quase-de Sitter EXATO —")
say("aqui a analise congelada nao tem caveat de congelamento.")
say("=" * 68)
veredito_fixo = []
for kv in (1.0, 10.0, 100.0):
    sig, Hs = resultado[kv]
    s_fim = sig[-1]/Hs[-1]
    veredito_fixo.append(s_fim)
    say(f"    k={kv:6.0f}:  sigma/H no ponto fixo = {s_fim:6.3f}"
        f"   [{'TAQUIAO PERSISTE' if s_fim > 0.5 else 'DESLIGA'}]")

say("")
say("LEITURA FINAL:")
if max(veredito_fixo) > 0.5:
    say("  O taquiao SOBREVIVE no ponto fixo, onde o congelamento e")
    say("  assintoticamente exato -> instabilidade GENUINA e eterna.")
    say("  O ramo finito puro (beta_n constantes) REPROVA o setor")
    say("  escalar. A modulacao beta_n(phi_-) da v2 deixa de ser")
    say("  opcional: e o mecanismo de estabilizacao necessario.")
else:
    say("  O taquiao DESLIGA antes do ponto fixo -> instabilidade")
    say("  transiente; discutir o crescimento acumulado (ln A) e a")
    say("  tolerancia observacional.")
say("  (Complemento: se eta << 1 na historia toda, o congelado e")
say("   confiavel tambem no transiente, e ln A quantifica o dano.)")

os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
with open(os.path.join(HERE, "out", "evolucao_temporal_escalar.txt"),
          "w", encoding="utf-8") as fh:
    fh.write("\n".join(OUT))
say("")
say("concluido. saida em auditoria/code/out/evolucao_temporal_escalar.txt")
