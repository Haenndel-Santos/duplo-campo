# -*- coding: utf-8 -*-
"""
r2_fantasma_estrutural.py — R-2 da fila pos-D2: caracterizacao da
direcao cinetica negativa (o que restou do no-go apos D2+R-1).

CONTEXTO. D2: o taquiao tardio congelado nao e dinamico. R-1: em
14/14 celulas o tardio dilui — MAS todas tem negK=1 (uma direcao
negativa em K_red). A evolucao linear nao testa fantasma (energia
negativa nao gera crescimento linear sem acoplamento). Este script
caracteriza a direcao com DIAGNOSTICOS INVARIANTES:

  - A ASSINATURA de K_red e invariante de congruencia (Sylvester);
    magnitudes de autovalor NAO sao (dependem de base) — declarado.
  - O invariante fisico e a ENERGIA CONSERVADA POR MODO do sistema
    congelado: para q = Re(v e^{i w t}),
        E = (1/4) (w^2 v'Kv + v'Wv)
    (o termo giroscopico C nao contribui a H). Modo propagante
    (w real) com E < 0 = FANTASMA LINEAR INVARIANTE.

MEDIDAS (criterios pre-declarados):
  R2-K: robustez da assinatura em k — min eig(K_red) em
      k_c in {1,3,10,30,100,300} (REF mu=1, a=400). Se o sinal
      flipar com k, a "direcao negativa" e dependente de
      representacao (eco da velha ressalva do kN); se uniforme, e
      robusta.
  R2-E: energias por modo (REF, a=400, todos os k): existe modo
      propagante com E<0? qual w^2, qual composicao (Psi_f, E_f,
      dchi)?
  R2-A: persistencia em a (REF, k_c=10, a in {30,100,400,1900}).
  R2-MU: escala de E_fantasma com mu na celula da lei de escala
      (0.5,-0.84), mu in {0.1,0.2,0.3,0.5,1} — a lei antiga
      |kN| ~ mu^3 revisitada como lei de ENERGIA (invariante).
  VEREDITO:
      FANTASMA-ROBUSTO: modo E<0 presente em todos os k/a testados
        com E nao-evanescente => o no-go sobrevive em forma de
        fantasma (letalidade = nivel de interacao; discutir contra a
        leitura strong-coupling da literatura).
      FANTASMA-MARGINAL: E<0 evanescente (E -> 0 em algum limite
        varrido) ou assinatura k-dependente => a patologia restante
        vive na fronteira de confiabilidade da ordem quadratica —
        convergindo com a leitura moderna da literatura (2507.11526);
        a F1 nao fica excluida neste nivel.

Reducao pontual com Cdot local (mini-trajetoria em torno da ancora),
mesma maquinaria validada (D2/R-1; controle GR la).

Requer sympy, numpy, scipy. ~2-4 min.
Uso: python auditoria/code/r2_fantasma_estrutural.py
Saida em auditoria/code/out/r2_fantasma_estrutural.txt
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


NOMES = ['Phi_g', 'B_g', 'Phi_f', 'Psi_f', 'B_f', 'E_f', 'dchi']
NOMES_RED = ['Psi_f', 'E_f', 'dchi']
MULT = [0, 1, 2, 4]
DYN = [3, 5, 6]
RHO0 = 0.3

say("=" * 72)
say("R-2 — O FANTASMA ESTRUTURAL: diagnosticos invariantes")
say("=" * 72)


def fundo_em(a, B0V, B1V, B2V, B4V, mu):
    kap = 1.0 / mu
    meff2 = mu / (1.0 + mu)
    rho = RHO0 * a**-3
    rho_til = rho / meff2
    rr = np.roots([kap * B4V - 3 * B2V, -3 * B1V,
                   3 * kap * B2V - B0V - rho_til, kap * B1V])
    reais = sorted(z.real for z in rr if abs(z.imag) < 1e-9 and z.real > 1e-10)
    if not reais:
        return None
    r = reais[0]
    dW = kap * (2 * B4V * r - B1V / r**2) - 3 * B1V - 6 * B2V * r
    if abs(dW) < 1e-14:
        return None
    drdN = -3 * rho_til / dW
    d2W = kap * (2 * B4V + 2 * B1V / r**3) - 6 * B2V
    d2rdN2 = 9 * rho_til / dW + 3 * rho_til * d2W * drdN / dW**2
    xi = r + drdN
    Vf = B4V + 3 * B2V / r**2 + B1V / r**3
    dVf = -6 * B2V / r**3 - 3 * B1V / r**4
    H2 = meff2 * r * r * Vf / (3.0 * mu)
    if H2 <= 0 or xi <= 0:
        return None
    H = np.sqrt(H2)
    dlnH_dN = 0.5 * (2 / r + dVf / Vf) * drdN
    Hd = H2 * dlnH_dN
    xid = H * (drdN + d2rdN2)
    Hfd = (Hd - H2 * drdN / r) / r
    rho_int = meff2 * (B0V + 3 * B1V * r + 3 * B2V * r**2)
    return dict(r=r, xi=xi, H=H, Hf=H / r, Hd=Hd, Hfd=Hfd, xid=xid,
                Ub=3 * H2 - rho_int)


def reduz_ponto(Kt, Ct, Wt, Cdot):
    K = Kt.copy()
    C = Ct.copy()
    W = Wt.copy()
    for i in MULT:
        for j in range(7):
            cij = C[i, j]
            cd = Cdot[i, j]
            if i == j:
                W[i, i] += cd
            else:
                W[i, j] += cd
                W[j, i] += cd
                C[j, i] -= cij
        C[i, :] = 0.0
    WXX = W[np.ix_(MULT, MULT)]
    if np.linalg.cond(WXX) > 1e12:
        raise RuntimeError("W_XX mal condicionada")
    WXXi = np.linalg.inv(WXX)
    return (K[np.ix_(DYN, DYN)] + C[np.ix_(DYN, MULT)] @ WXXi
            @ C[np.ix_(DYN, MULT)].T,
            C[np.ix_(DYN, DYN)] - C[np.ix_(DYN, MULT)] @ WXXi
            @ W[np.ix_(MULT, DYN)],
            W[np.ix_(DYN, DYN)] - W[np.ix_(DYN, MULT)] @ WXXi
            @ W[np.ix_(MULT, DYN)])


# ------------------------------------------------------------------
say("[montagem] L2 e lambdify (betas e mu livres) ...")
L2s, fields, vels = d1.build_L2()
K7, C7, W7 = quadratic_matrices(L2s, fields, vels)
if [str(f) for f in fields] != NOMES:
    raise RuntimeError("ordem de campos mudou")
FIXOS = {Mg2: 1, m2: 1, b3: 0, Fb: 1, Fp: 0, Fpp: 0,
         chid_s: 0, chidd_s: 0, rho_s: 0, Up: 0, Upp: sp.Rational(3, 10)}
LIVRES = (a_s, b_s, xi_s, H_s, Hf_s, Hd_s, Hfd_s, xid_s, Ub, ksym,
          b0, b1, b2, b4, Mf2, Meff2)
K7F = sp.lambdify(LIVRES, K7.subs(FIXOS), 'numpy')
C7F = sp.lambdify(LIVRES, C7.subs(FIXOS), 'numpy')
W7F = sp.lambdify(LIVRES, W7.subs(FIXOS), 'numpy')
say("[montagem] pronto")


def reduzido_em(a_anc, B0V, B1V, B2V, B4V, mu, kc, npts=401):
    """K_r, C_r, W_r no ponto a_anc, com Cdot de mini-trajetoria local."""
    Ns = np.linspace(np.log(a_anc / 1.3), np.log(a_anc * 1.3), npts)
    Cs = np.zeros((npts, 7, 7))
    Ks = Ws = None
    Hs_arr = np.zeros(npts)
    meff2 = mu / (1.0 + mu)
    pc = npts // 2
    for p, N in enumerate(Ns):
        f = fundo_em(np.exp(N), B0V, B1V, B2V, B4V, mu)
        if f is None:
            return None
        Hs_arr[p] = f['H']
        args = (np.exp(N), f['r'] * np.exp(N), f['xi'], f['H'], f['Hf'],
                f['Hd'], f['Hfd'], f['xid'], f['Ub'], kc,
                B0V, B1V, B2V, B4V, mu, meff2)
        Cs[p] = np.array(C7F(*args), float)
        if p == pc:
            Ks = np.array(K7F(*args), float)
            Ws = np.array(W7F(*args), float)
    Cd = np.gradient(Cs, Ns, axis=0) * Hs_arr[:, None, None]
    Kr, Cr, Wr = reduz_ponto(Ks, Cs[pc], Ws, Cd[pc])
    return Kr, Cr, Wr, Hs_arr[pc]


def analisa(Kr, Cr, Wr, H):
    """eig(K), e por modo do QEP: w2, kN, E=(w2*kN+wN)/4, composicao.
    Devolve (eigK, lista de modos, modo_fantasma ou None)."""
    eigK = np.sort(np.linalg.eigvalsh(0.5 * (Kr + Kr.T)))
    pares = d1.agrupa_pares(d1.qep_modes(Kr, Cr, Wr))
    modos = []
    fantasma = None
    for mm in pares:
        w2 = mm['omega2']
        v = mm['v']
        kN = float(np.real(np.conjugate(v) @ Kr @ v))
        wN = float(np.real(np.conjugate(v) @ Wr @ v))
        real_w = (w2.real > 0 and abs(w2.imag) < 1e-3 * abs(w2.real))
        E = 0.25 * (w2.real * kN + wN) if real_w else float('nan')
        comp = np.abs(v)**2
        comp = comp / comp.sum()
        modos.append(dict(w2=w2, kN=kN, E=E, comp=comp, real=real_w,
                          sig=abs(np.sqrt(complex(w2)).imag) / H))
        if real_w and E < 0:
            if fantasma is None or E < fantasma['E']:
                fantasma = modos[-1]
    return eigK, modos, fantasma


def linha_modo(mm):
    c = mm['comp']
    return (f"w2={mm['w2'].real:+.3e}"
            f"{'' if abs(mm['w2'].imag) < 1e-6*max(1, abs(mm['w2'].real)) else ' (cplx)'}"
            f" kN={mm['kN']:+.2e} E={mm['E']:+.3e} "
            f"[{NOMES_RED[0]}:{c[0]:.2f} {NOMES_RED[1]}:{c[1]:.2f} "
            f"{NOMES_RED[2]}:{c[2]:.2f}]")


B0V, B4V = 1.0, 0.5

# ------------------------------------------------------------------
say("")
say("R2-K / R2-E — REF mu=1, a=400: varredura em k")
say(f"    {'k_c':>5} {'min eig(K_r)':>13} {'E_fantasma':>11} "
    f"{'w2_fant':>10}  composicao do modo E<0")
kvar = [1.0, 3.0, 10.0, 30.0, 100.0, 300.0]
res_k = []
for kc in kvar:
    out = reduzido_em(400.0, B0V, 1.0, -0.4, B4V, 1.0, kc)
    if out is None:
        say(f"    {kc:5.0f}  sem fundo")
        continue
    Kr, Cr, Wr, H = out
    eigK, modos, fant = analisa(Kr, Cr, Wr, H)
    if fant:
        c = fant['comp']
        say(f"    {kc:5.0f} {eigK[0]:+13.3e} {fant['E']:+11.3e} "
            f"{fant['w2'].real:+10.3e}  Psi_f:{c[0]:.2f} E_f:{c[1]:.2f} "
            f"dchi:{c[2]:.2f}")
    else:
        say(f"    {kc:5.0f} {eigK[0]:+13.3e}  (nenhum modo real com E<0)")
    res_k.append(dict(kc=kc, eig0=eigK[0], fant=fant))

sinais = set(np.sign(r['eig0']) for r in res_k)
k_uniforme = (len(sinais) == 1)
fant_todos_k = all(r['fant'] is not None for r in res_k)

# ------------------------------------------------------------------
say("")
say("R2-A — REF mu=1, k_c=10: persistencia em a")
res_a = []
for a_anc in (30.0, 100.0, 400.0, 1900.0):
    out = reduzido_em(a_anc, B0V, 1.0, -0.4, B4V, 1.0, 10.0)
    if out is None:
        continue
    Kr, Cr, Wr, H = out
    eigK, modos, fant = analisa(Kr, Cr, Wr, H)
    say(f"    a={a_anc:6.0f}: min eig(K_r)={eigK[0]:+.3e}  "
        + (f"E_fant={fant['E']:+.3e}" if fant else "sem modo E<0"))
    res_a.append(dict(a=a_anc, eig0=eigK[0], fant=fant))
a_persistente = all(r['fant'] is not None for r in res_a)

# ------------------------------------------------------------------
say("")
say("R2-MU — celula da lei de escala (0.5,-0.84), k_c=10, a=400:")
say("    escala de E_fantasma com mu (lei antiga: |kN| ~ mu^3)")
mus = [0.1, 0.2, 0.3, 0.5, 1.0]
Es = []
say(f"    {'mu':>6} {'min eig(K_r)':>13} {'E_fantasma':>12} {'w2_fant':>10}")
for mu in mus:
    out = reduzido_em(400.0, B0V, 0.5, -0.84, B4V, mu, 10.0)
    if out is None:
        say(f"    {mu:6.2f}  sem fundo")
        Es.append(np.nan)
        continue
    Kr, Cr, Wr, H = out
    eigK, modos, fant = analisa(Kr, Cr, Wr, H)
    Ef = fant['E'] if fant else np.nan
    say(f"    {mu:6.2f} {eigK[0]:+13.3e} {Ef:+12.3e} "
        + (f"{fant['w2'].real:+10.3e}" if fant else ""))
    Es.append(Ef)
Es = np.array(Es)
fin = np.isfinite(Es) & (Es < 0)
p_exp = float('nan')
if np.sum(fin) >= 3:
    lm = np.log(np.array(mus)[fin])
    lE = np.log(-Es[fin])
    p_exp = np.polyfit(lm, lE, 1)[0]
say(f"    expoente ajustado: E_fantasma ~ mu^{p_exp:.2f}"
    if np.isfinite(p_exp) else "    (ajuste indisponivel)")

# ------------------------------------------------------------------
say("")
say("DETALHE — espectro completo na REF mu=1, a=400, k_c=10:")
out = reduzido_em(400.0, B0V, 1.0, -0.4, B4V, 1.0, 10.0)
Kr, Cr, Wr, H = out
eigK, modos, fant = analisa(Kr, Cr, Wr, H)
for mm in sorted(modos, key=lambda m: abs(m['w2'])):
    say("    " + linha_modo(mm))
say(f"    eig(K_r) = {[f'{x:+.3e}' for x in eigK]}")

# ------------------------------------------------------------------
say("")
say("=" * 72)
say("VEREDITO R-2 (criterios pre-declarados)")
say("=" * 72)
say(f"  R2-K: assinatura de K_r uniforme em k? "
    f"{'SIM' if k_uniforme else 'NAO — flipa com k'}")
say(f"  R2-E: modo propagante com E<0 em todos os k testados? "
    f"{'SIM' if fant_todos_k else 'NAO'}")
say(f"  R2-A: fantasma persistente em a (30..1900)? "
    f"{'SIM' if a_persistente else 'NAO'}")
say(f"  R2-MU: E_fantasma ~ mu^{p_exp:.2f} (evanescente se expoente >~ 2 "
    "e E->0 quando mu->0)" if np.isfinite(p_exp) else "  R2-MU: sem ajuste")
say("")
evanescente = np.isfinite(p_exp) and p_exp >= 2.0
if k_uniforme and fant_todos_k and a_persistente and not evanescente:
    say("  >>> FANTASMA-ROBUSTO: modo de energia negativa invariante,")
    say("  presente em todos os k e a testados, sem evanescencia na")
    say("  amostra. O no-go da F1 sobrevive EM FORMA DE FANTASMA — com a")
    say("  ressalva declarada: a letalidade e de nivel de interacao (a")
    say("  dinamica linear nao a realiza), e a leitura alternativa da")
    say("  literatura (setor fortemente acoplado; quebra da ordem")
    say("  quadratica) permanece em pe como interpretacao concorrente.")
    say("  A distincao entre as duas exige analise alem da quadratica —")
    say("  fora do alcance da maquinaria atual; fronteira do programa.")
elif k_uniforme and fant_todos_k and a_persistente and evanescente:
    say("  >>> FANTASMA-EVANESCENTE: presente em toda a amostra mas com")
    say("  energia -> 0 quando mu -> 0 (lei de potencia acima). A")
    say("  patologia enfraquece de acoplamento na direcao do limite GR —")
    say("  quantitativamente marginal la; robusta em mu ~ 1. Reportar o")
    say("  mapa e discutir contra strong coupling.")
else:
    say("  >>> FANTASMA-MARGINAL/REPRESENTACIONAL: assinatura ou")
    say("  existencia dependente de k/a na amostra — a patologia restante")
    say("  vive na fronteira de confiabilidade da ordem quadratica,")
    say("  convergindo com a leitura moderna da literatura. A F1 NAO fica")
    say("  excluida neste nivel; o setor escalar fica 'sem veredito de")
    say("  exclusao' no quadratico.")

os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
with open(os.path.join(HERE, "out", "r2_fantasma_estrutural.txt"),
          "w", encoding="utf-8") as fh:
    fh.write("\n".join(OUT))
say("")
say("concluido. saida em auditoria/code/out/r2_fantasma_estrutural.txt")
