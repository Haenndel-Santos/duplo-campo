# -*- coding: utf-8 -*-
"""
escaneio_hierarquia.py — o taquiao sobrevive a hierarquia M_f/M_g?

Extensao v2, etapa 1-b. O escaneio anterior (escaneio_beta_ponto_fixo)
deu 0/169 na grade (beta_1, beta_2) com M_g = M_f — taquiao universal
naquela fatia, com fundo existindo em toda parte. A variavel nunca
tocada e a hierarquia mu = M_f^2/M_g^2, que e a cura padrao da
literatura bimetrica (M_f >> M_g aproxima o setor g de GR).

Generalizacao (kappa = M_g^2/M_f^2 = 1/mu; M_g^2 = 1):
  W(r)   = kappa r^2 V_f(r) - V_g(r) = rho/(m^2 M_eff^2)
  cubica (F1, b3=0):
    (kappa b4 - 3 b2) r^3 - 3 b1 r^2 + (3 kappa b2 - b0 - rho~) r
      + kappa b1 = 0        [menor raiz positiva = ramo finito]
  W'(r)  = kappa (2 b4 r - b1/r^2) - 3 b1 - 6 b2 r
  M_eff^2 = mu/(1+mu)
  H^2    = m^2 M_eff^2 r^2 V_f(r) / (3 M_f^2)   [Friedmann-f, H_f=H/r]
  Ub     = 3 M_g^2 H^2 - rho_int                 [truque materia->Ub]
  m_T^2  = m^2 M_eff^2 (1/M_g^2 + xi/(M_f^2 r^3)) r (b1 + b2(xi+r))

Resultado estrutural preservado: no primordial (r->0, xi=4r) a razao
m_T^2/H^2 -> 12 INDEPENDENTE tambem de mu (M_f^2 cancela) — Higuchi
primordial e automatico em qualquer hierarquia; o teste e no tardio.

Saidas: (i) tendencia sigma/H vs mu no ponto de referencia;
(ii) mapas (beta_1 x beta_2) no ponto fixo para varios mu;
(iii) sobreviventes -> historia + Higuchi + Omega_m.

Requer sympy, numpy, scipy.  ~4-6 min.
Uso:  python auditoria/code/escaneio_hierarquia.py
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

# fixos: M_g^2 = 1 (unidade); M_f^2, M_eff^2 e os beta ficam LIVRES
PBsub = {b3: 0.0, Mg2: 1.0, m2: 1.0,
         Fb: 1.0, Fp: 0.0, Fpp: 0.0,
         chid_s: 0.0, chidd_s: 0.0, Up: 0.0, Upp: 0.3,
         rho_s: 0.0, Hd_s: 0.0, Hfd_s: 0.0, xid_s: 0.0}
RHO_M0 = 0.3
REF = (1.0, -0.4, 1.0, 0.5)            # (b1,b2,b0,b4) de referencia
SIGMA_REF_PF = 3.651                   # mu=1, ponto fixo, k=1 (ancora exata
                                       # da rodada anterior; tolerancia 2%)

# ------------------------------ fundo generalizado -------------------
# Retorno: tupla (r, xi, H, Hf, Ub, a, b) OU uma string-motivo entre
# 'sem_raiz' / 'xi_neg' / 'H2_neg' — tres patologias fisicamente
# DISTINTAS (inexistencia genuina vs lapso f negativo vs energia
# negativa), que os mapas mostram com simbolos separados.
def fundo(N, B1, B2, B0, B4, mu):
    kap = 1.0/mu
    Meff2v = mu/(1.0 + mu)
    a = np.exp(N)
    rho = RHO_M0 * a**-3
    rho_til = rho / Meff2v                       # m^2 = 1
    rr = np.roots([kap*B4 - 3*B2, -3*B1, 3*kap*B2 - B0 - rho_til, kap*B1])
    # corte de positividade RELATIVO ao ramo finito esperado
    # (r ~ kap*B1/rho_til encolhe com mu e com a^-3; corte absoluto
    # de 1e-10 podia descartar raiz genuina em hierarquia grande)
    r_esc = max(1e-14, 1e-6*kap*B1/max(rho_til, 1.0))
    reais = sorted(z.real for z in rr
                   if abs(z.imag) < 1e-9 and z.real > r_esc)
    if not reais:
        return 'sem_raiz'
    r = reais[0]                                 # ramo finito
    dW = kap*(2*B4*r - B1/r**2) - 3*B1 - 6*B2*r
    if abs(dW) < 1e-12:
        return 'sem_raiz'
    drdN = -3.0*rho_til/dW
    xi = r + drdN
    if xi <= 0:
        return 'xi_neg'
    Vf = B4 + 3*B2/r**2 + B1/r**3
    H2 = Meff2v*r*r*Vf/(3.0*mu)                  # /M_f^2, M_f^2 = mu
    if H2 <= 0:
        return 'H2_neg'
    H = np.sqrt(H2)
    rho_int = Meff2v*(B0 + 3*B1*r + 3*B2*r**2)
    Ubv = 3.0*H2 - rho_int                       # M_g^2 = 1
    return r, xi, H, H/r, Ubv, a, r*a

def higuchi(r, xi, H, B1, B2, mu):
    """m_T^2 (D2, F=1, b3=0) generalizado; retorna (ok, mT2/H^2).

    CRITERIO PROVISORIO: o limiar 2H^2 (H do setor g) e o limite de
    Higuchi de mu=1; a forma generalizada para hierarquia nao esta
    derivada no projeto (a D2 fornece m_T^2, nao o limiar). Pontos
    reprovados SO por este criterio sao reportados a parte."""
    Meff2v = mu/(1.0 + mu)
    mT2 = Meff2v*(1.0 + xi/(mu*r**3))*r*(B1 + B2*(xi + r))
    return mT2 >= 2.0*H*H, mT2/(H*H)

# ------------------------------ maquinaria ---------------------------
say("montando L2 (mesma acao/gauge da D1) ...")
L2s, fields, vels = d1.build_L2()
K7, C7, W7 = quadratic_matrices(L2s, fields, vels)
say("lambdificando com beta e (M_f^2, M_eff^2) LIVRES ...")
livres = (a_s, b_s, xi_s, H_s, Hf_s, Ub, ksym, b1, b2, b0, b4, Mf2, Meff2)
K7n = sp.lambdify(livres, K7.subs(PBsub), modules='numpy')
C7n = sp.lambdify(livres, C7.subs(PBsub), modules='numpy')
W7n = sp.lambdify(livres, W7.subs(PBsub), modules='numpy')

def sigma_em(N, kv, B1, B2, B0, B4, mu):
    """(sigma_max/H, kN_min, fundo) ou string-motivo da patologia."""
    f = fundo(N, B1, B2, B0, B4, mu)
    if isinstance(f, str):
        return f
    r, xi, H, Hf, Ubv, a, bb = f
    Meff2v = mu/(1.0 + mu)
    args = (a, bb, xi, H, Hf, Ubv, kv, B1, B2, B0, B4, mu, Meff2v)
    Kn = np.array(K7n(*args), float)
    Cn = np.array(C7n(*args), float)
    Wn = np.array(W7n(*args), float)
    pares = d1.agrupa_pares(d1.qep_modes(Kn, Cn, Wn))
    sig, kNmin = 0.0, np.inf
    for mm in pares:
        om = np.sqrt(complex(mm['omega2']))
        sig = max(sig, abs(om.imag))
        kNmin = min(kNmin, mm['knorm'])
    return sig/H, kNmin, f

# ------------------------------ auto-teste (mu=1) --------------------
# MESMA condicao da ancora: ponto fixo, k=1 (a revisao adversarial
# pegou a versao anterior testando em k=10 contra ancora de k=1,
# passando so pela tolerancia frouxa — gate dessensibilizado).
say("")
say("auto-teste: referencia (1,-0.4,1,0.5), mu=1, k=1 (condicao da ancora)")
res = sigma_em(np.log(10.0), 1.0, *REF, 1.0)
if isinstance(res, str):
    say(f"    !! fundo de referencia inexistente ({res}) — abortando")
    sys.exit(1)
sH, kN, f = res
say(f"    sigma/H = {sH:.4f}   esperado = {SIGMA_REF_PF} (tol. 2%)")
say(f"    Ub(a=10) = {f[4]:+.2e}   (identidade Ub=rho: esperado ~3e-4)")
ok = abs(sH - SIGMA_REF_PF) < 0.02*SIGMA_REF_PF and abs(f[4] - 3e-4) < 1e-4
say(f"    [{'PASSA' if ok else 'FALHA'}]")
if not ok:
    say("    !! abortando: generalizacao nao reproduz o caso mu=1")
    sys.exit(1)

# ------------------------------ (i) tendencia em mu ------------------
say("")
say("=" * 68)
say("(i) TENDENCIA — referencia (b1,b2)=(1,-0.4), ponto fixo, k=10")
say("    a hierarquia ajuda? sigma/H e kN_min vs mu")
say("=" * 68)
say(f"    {'mu':>7} {'r_pf':>8} {'sigma/H':>9} {'kN_min':>11} {'mT2/H2':>8}")
for mu in (1.0, 2.0, 3.0, 5.0, 10.0, 20.0, 50.0, 100.0):
    r = sigma_em(np.log(10.0), 10.0, *REF, mu)
    if isinstance(r, str):
        say(f"    {mu:7.1f}  (fundo: {r})")
        continue
    sH, kN, f = r
    _, mT2H2 = higuchi(f[0], f[1], f[2], REF[0], REF[1], mu)
    say(f"    {mu:7.1f} {f[0]:8.4f} {sH:9.3f} {kN:11.3e} {mT2H2:8.2f}")

# ------------------------------ (ii) mapas por mu --------------------
say("")
say("=" * 68)
say("(ii) MAPAS (beta_1 x beta_2) no ponto fixo (a=10), k=10, por mu")
say("     # taquiao s/H>0.5 | ~ marginal | . saudavel")
say("     patologias: X sem raiz | x lapso f negativo | h H^2<=0")
say("=" * 68)

SIMB_PAT = {'sem_raiz': 'X', 'xi_neg': 'x', 'H2_neg': 'h'}
B1s = np.linspace(0.2, 2.0, 13)
B2s = np.linspace(-1.0, -0.05, 13)
NPF = np.log(10.0)
MUS = (0.1, 0.3, 3.0, 10.0, 30.0, 100.0)
candidatos = []
for mu in MUS:
    say("")
    say(f"--- mu = M_f^2/M_g^2 = {mu} ---")
    say("           beta_2 ->  " + " ".join(f"{x:5.2f}" for x in B2s))
    n_sau, n_marg = 0, 0
    for B1v in B1s:
        linha = []
        for B2v in B2s:
            r = sigma_em(NPF, 10.0, B1v, B2v, 1.0, 0.5, mu)
            if isinstance(r, str):
                linha.append(SIMB_PAT[r])
                continue
            sH, kN, f = r
            if sH < 0.05:
                linha.append('.'); n_sau += 1
                candidatos.append((mu, B1v, B2v, sH))
            elif sH <= 0.5:
                linha.append('~'); n_marg += 1
                candidatos.append((mu, B1v, B2v, sH))
            else:
                linha.append('#')
        say(f"    beta_1={B1v:4.2f}   " + "     ".join(linha))
    say(f"    saudaveis: {n_sau}   marginais: {n_marg}")

# ------------------------------ (iii) sobreviventes ------------------
say("")
say("=" * 68)
say("(iii) SOBREVIVENTES — historia (a=0.25/0.5/1) + Higuchi + Omega_m")
say("=" * 68)
# TODOS os candidatos sao verificados (a revisao adversarial pegou um
# truncamento silencioso [:24] aqui — um pleno fora do top-24 viraria
# veredito errado); so a IMPRESSAO e limitada, com aviso explicito.
# NOTA sobre o criterio de Higuchi: o limiar m_T^2 >= 2H^2 (H do setor
# g) e o criterio de mu=1; o limite generalizado para hierarquia nao
# esta derivado no projeto — o tag e PROVISORIO e nao descarta plenos
# sozinho (plenos exigem historia limpa E higuchi; reportamos os dois
# separadamente).
plenos = []
quase = []          # historia limpa mas higuchi(mu=1) falha em algum a
if not candidatos:
    say("    (nenhum candidato)")
MAX_PRINT = 30
verificados = sorted(candidatos, key=lambda t: t[3])
if len(verificados) > MAX_PRINT:
    say(f"    ({len(verificados)} candidatos — TODOS verificados; "
        f"imprimindo os {MAX_PRINT} de menor sigma no ponto fixo)")
for idx, (mu, B1v, B2v, sH_pf) in enumerate(verificados):
    hist, hig_all, ok_hist = [], True, True
    for aa in (0.25, 0.5, 1.0):
        rres = sigma_em(np.log(aa), 10.0, B1v, B2v, 1.0, 0.5, mu)
        if isinstance(rres, str):
            ok_hist = False; hist.append(SIMB_PAT[rres].center(5)); continue
        sH, kN, f = rres
        hg, _ = higuchi(f[0], f[1], f[2], B1v, B2v, mu)
        hig_all = hig_all and hg
        hist.append(f"{sH:5.2f}")
        if sH > 0.5:
            ok_hist = False
    fz = fundo(0.0, B1v, B2v, 1.0, 0.5, mu)
    Om = (RHO_M0/(3*fz[2]**2)) if not isinstance(fz, str) else float('nan')
    tag = "HISTORIA LIMPA" if (ok_hist and hig_all) else \
          ("taquiao transiente" if hig_all
           else ("limpa MAS higuchi(mu=1)" if ok_hist
                 else "viola higuchi(mu=1 prov.)"))
    if idx < MAX_PRINT:
        say(f"    mu={mu:5.1f} b1={B1v:4.2f} b2={B2v:5.2f}: pf={sH_pf:5.2f} "
            f"hist={'/'.join(hist)} Om0={Om:5.2f} [{tag}]")
    if ok_hist and hig_all:
        plenos.append((mu, B1v, B2v))
    elif ok_hist:
        quase.append((mu, B1v, B2v))
if len(verificados) > MAX_PRINT and (plenos or quase):
    say(f"    (plenos/quase fora do bloco impresso tambem contam: "
        f"plenos={len(plenos)}, limpos-sem-higuchi={len(quase)})")

# ------------------------------ veredito -----------------------------
say("")
say("=" * 68)
say("VEREDITO")
say("=" * 68)
if plenos:
    say(f"  {len(plenos)} ponto(s) com HISTORIA LIMPA + higuchi(mu=1):")
    for p in plenos[:10]:
        say(f"    mu={p[0]:.1f}, beta_1={p[1]:.2f}, beta_2={p[2]:.2f}")
    say("")
    say("  => A hierarquia M_f/M_g abre regiao viavel. Proximos passos:")
    say("     refinar a grade em torno dos plenos, checar Omega_m/H0")
    say("     razoaveis, derivar o Higuchi generalizado (o criterio")
    say("     usado e o de mu=1), e decidir se beta constante +")
    say("     hierarquia ja resolve (modulacao volta a ser opcional)")
    say("     ou se a regiao ainda pede a condensacao de phi_-.")
elif quase:
    say(f"  {len(quase)} ponto(s) com historia escalar limpa mas que")
    say("  falham o criterio de Higuchi de mu=1 — que NAO esta derivado")
    say("  para hierarquia. Derivar o limite generalizado antes de")
    say("  descartar: podem ser a regiao viavel.")
    for p in quase[:10]:
        say(f"    mu={p[0]:.1f}, beta_1={p[1]:.2f}, beta_2={p[2]:.2f}")
elif candidatos:
    say("  Ha pontos saudaveis/marginais no ponto fixo, mas nenhum com")
    say("  historia inteira limpa — a modulacao ganha alvo: levar o")
    say("  sistema ate a regiao tardia saudavel.")
else:
    say("  NADA saudavel em nenhuma hierarquia testada (mu=0.1 a 100).")
    say("  O taquiao do par relativo resiste a (beta_1, beta_2, mu).")
    say("  Proximo: extrair a estrutura analitica do m^2 do par para")
    say("  entender O QUE o controla — e documentar o no-go da classe")
    say("  com a fronteira do que foi varrido.")

os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
with open(os.path.join(HERE, "out", "escaneio_hierarquia.txt"),
          "w", encoding="utf-8") as fh:
    fh.write("\n".join(OUT))
say("")
say("concluido. saida em auditoria/code/out/escaneio_hierarquia.txt")
