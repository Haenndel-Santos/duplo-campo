# -*- coding: utf-8 -*-
"""
r6b_degenerescencia_K.py — det K_red = 0 OU NAO: o teste de precisao
estendida.

MOTIVO: o R-6 (out/r6_posto_K_reduzida.txt) mediu o espectro de K_red
e caiu em ZONA CINZA porque a metrica usada (rho_K = |lam0|/max|lam|)
tem denominador contaminado: lam2 e a direcao E_f, que carrega k^4 e
chega a 1e26, enquanto lam0 ~ -1e12 e lam1 ~ +1e14. Contra lam1 o
autovalor negativo NAO e pequeno. Achados que ficam de pe do R-6:
  - K7 bruto tem K[Psi_f,Psi_f] ~ 0 e K[E_f,E_f] ~ 0; so existe o
    cruzado K[Psi_f,E_f] — o sinal negativo nasce do termo cruzado;
  - a direcao negativa de K_red e |v0.Psi_f|^2 = 1.0000 em 40/40
    marcos nos dois fundos (Psi_f puro).

Pela lei da inercia de Sylvester a ASSINATURA de K_red e invariante
por qualquer mudanca de variavel invertivel. Logo a pergunta e
binaria: det K_red = 0 (assinatura 0,+,+ e a direcao Psi_f e vinculo)
ou det K_red < 0 (assinatura -,+,+ e ha um fantasma). Escolha de
variavel nao muda a resposta; so muda a facilidade de medir.

O QUE DECIDE: como lam0 depende da precisao aritmetica.
  - zero estrutural mascarado por cancelamento catastrofico:
    |lam0|/|lam1| CAI ao aumentar os digitos (com dps -> inf, -> 0);
  - modo genuino: |lam0|/|lam1| CONVERGE para um valor nao-nulo,
    estavel entre dps=15, 30 e 60.

FONTES DE ERRO CONTROLADAS (as duas que o Gate F-b nao separava):
  (E1) roundoff float64 -> tratado com mpmath em dps = 15/30/60;
  (E2) Cdot por np.gradient na grade (erro O(dN^2) ~ 1e-6 a 1e-7, que
       entra em K_red via W_XX^-1) -> aqui Cdot vem de diferenca
       central em N com passo h proprio, independente da grade, com
       h varrido (teste de halving) dentro da precisao corrente.

MEDIDAS (pre-declaradas):
  A1 — K_red 3x3 impressa (entradas), em 3 epocas por fundo.
  A2 — espectro EQUILIBRADO (D K D com D=diag(1/sqrt(max_j|K_ij|))):
       teste de posto livre de escala de variavel.
  A3 — lam0/lam1 vs dps in {15,30,60} nas mesmas epocas.
  A4 — halving em h (Cdot) dentro de cada dps.
  A5 — controle GR: mesma maquina em GR+escalar deve dar assinatura
       (+) sem direcao negativa (o gr_selfcheck da lib ja roda, mas
       aqui olhamos o espectro).

CRITERIOS (pre-declarados; leitura so depois de rodar):
  |lam0|/|lam1| cai >= 3 ordens de dps=15 -> 60, com h estavel
      -> DEGENERADA: Psi_f e vinculo; a canonizacao do Gate F-b
         dividiu por zero; omega_0/H ~ 7-12 nao e frequencia fisica.
  |lam0|/|lam1| estavel dentro de 1 ordem entre dps=15,30,60
      -> NAO-DEGENERADA: assinatura (-,+,+) e real; a critica externa
         nao se aplica a esta acao; o fantasma do Gate F sobrevive.
  Caso intermediario -> declarar inconclusivo e nao interpretar.

Requer sympy, numpy, mpmath. ~poucos minutos.
Uso (raiz do repo, venv ativo):
    python auditoria/code/r6b_degenerescencia_K.py
Saida em auditoria/code/out/r6b_degenerescencia_K.txt
"""
import importlib.util
import os
import sys
import time

import mpmath as mp
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
MULT = [0, 1, 2, 4]
DYN = [3, 5, 6]
A_MIN = 100.0
EPOCAS = [150.0, 3635.0, 74992.0]
DPS_LISTA = [15, 30, 60]
H_LISTA = ['1e-4', '1e-5', '1e-6']

MU = 1
ME2 = sp.Rational(1, 2)      # MU/(1+MU) com MU=1
MF2 = 1
B0V, B2V, B4V = 1, sp.Rational(-2, 5), sp.Rational(1, 2)
RHO0 = sp.Rational(3, 10)
UPP = sp.Rational(3, 10)

say("=" * 72)
say("R-6b — det K_red = 0 OU NAO: teste de precisao estendida")
say("=" * 72)

if not d1.gr_selfcheck():
    say("[!] V1 (GR selfcheck da biblioteca) falhou — abortando")
    sys.exit(1)
say("[V1] GR selfcheck da biblioteca: PASSA")

L2s, fields, vels = d1.build_L2()
K7, C7, W7 = quadratic_matrices(L2s, fields, vels)
if [str(f) for f in fields] != NOMES:
    raise RuntimeError("ordem de campos mudou")
say("[montagem] K,C,W 7x7 prontos")

LIVRES = (a_s, b_s, xi_s, H_s, Hf_s, Hd_s, Hfd_s, xid_s,
          chid_s, chidd_s, Ub, Up, Upp, ksym, Mf2, Meff2)


def compila(B1V):
    """K,C,W com betas/F numericos exatos; lambdify em mpmath."""
    sub = {Mg2: 1, m2: 1, rho_s: 0, Fb: 0, Fp: 0, Fpp: 0,
           b0: B0V, b1: B1V, b2: B2V, b3: 0, b4: B4V}
    fs = []
    for M in (K7, C7, W7):
        Ms = sp.nsimplify(M.subs(sub))
        fs.append(sp.lambdify(LIVRES, Ms, modules='mpmath'))
    return fs


def fundo_mp(a, B1V):
    """fundo beta-constante em precisao corrente (mp.mp.dps)."""
    a = mp.mpf(a)
    kap = mp.mpf(1) / MU
    meff2 = mp.mpf(1) / 2
    rho = mp.mpf(RHO0) * a ** -3
    rho_til = rho / meff2
    B1 = mp.mpf(sp.Float(B1V, 50).__str__())
    B0, B2, B4 = mp.mpf(B0V), mp.mpf(-0.4), mp.mpf(0.5)
    coef = [kap * B4 - 3 * B2, -3 * B1, 3 * kap * B2 - B0 - rho_til, kap * B1]
    rr = mp.polyroots(coef, maxsteps=200, extraprec=200)
    reais = sorted(z.real for z in rr
                   if abs(mp.im(z)) < mp.mpf('1e-20') and mp.re(z) > 0)
    if not reais:
        raise RuntimeError("sem raiz real positiva")
    r = reais[0]
    dW = kap * (2 * B4 * r - B1 / r ** 2) - 3 * B1 - 6 * B2 * r
    drdN = -3 * rho_til / dW
    d2W = kap * (2 * B4 + 2 * B1 / r ** 3) - 6 * B2
    d2rdN2 = 9 * rho_til / dW + 3 * rho_til * d2W * drdN / dW ** 2
    xi = r + drdN
    Vf = B4 + 3 * B2 / r ** 2 + B1 / r ** 3
    dVf = -6 * B2 / r ** 3 - 3 * B1 / r ** 4
    H2 = meff2 * r * r * Vf / (3 * mp.mpf(MU))
    H = mp.sqrt(H2)
    dlnH_dN = mp.mpf(1) / 2 * (2 / r + dVf / Vf) * drdN
    Hd = H2 * dlnH_dN
    xid = H * (drdN + d2rdN2)
    Hfd = (Hd - H2 * drdN / r) / r
    rho_int = meff2 * (B0 + 3 * B1 * r + 3 * B2 * r ** 2)
    return dict(r=r, xi=xi, H=H, Hf=H / r, Hd=Hd, Hfd=Hfd, xid=xid,
                Ub=3 * H2 - rho_int)


def args_em(N, B1V, kc):
    a = mp.exp(N)
    f = fundo_mp(a, B1V)
    return (a, f['r'] * a, f['xi'], f['H'], f['Hf'], f['Hd'], f['Hfd'],
            f['xid'], mp.mpf(0), mp.mpf(0), f['Ub'], mp.mpf(0),
            mp.mpf(sp.Float(UPP, 50).__str__()), kc,
            mp.mpf(MF2), mp.mpf(1) / 2), f['H']


def mat(fn, args):
    return mp.matrix(fn(*args))


def kred_mp(N, B1V, kc, fK, fC, fW, h):
    """K_red 3x3 em precisao corrente; Cdot por diferenca central em N."""
    ar, H = args_em(N, B1V, kc)
    K = mat(fK, ar)
    C = mat(fC, ar)
    W = mat(fW, ar)
    hh = mp.mpf(h)
    ap, _ = args_em(N + hh, B1V, kc)
    am, _ = args_em(N - hh, B1V, kc)
    Cp, Cm = mat(fC, ap), mat(fC, am)
    Cdot = (Cp - Cm) / (2 * hh) * H

    n = 7
    for i in MULT:
        linha = max(abs(K[i, j]) for j in range(n))
        esc = max(max(abs(K[p, q]) for q in range(n)) for p in range(n))
        if linha > mp.mpf('1e-10') * max(mp.mpf(1), esc):
            raise RuntimeError(f"linha K do multiplicador {NOMES[i]} nao-nula")
        for j in range(n):
            cij = C[i, j]
            cd = Cdot[i, j]
            if i == j:
                W[i, i] += cd
            else:
                W[i, j] += cd
                W[j, i] += cd
                C[j, i] -= cij
        for j in range(n):
            C[i, j] = mp.mpf(0)
    WXX = mp.matrix(4, 4)
    for ii, i in enumerate(MULT):
        for jj, j in enumerate(MULT):
            WXX[ii, jj] = W[i, j]
    WXXi = WXX ** -1
    CdX = mp.matrix(3, 4)
    WdX = mp.matrix(3, 4)
    WXd = mp.matrix(4, 3)
    for ii, i in enumerate(DYN):
        for jj, j in enumerate(MULT):
            CdX[ii, jj] = C[i, j]
            WdX[ii, jj] = W[i, j]
            WXd[jj, ii] = W[j, i]
    Kdd = mp.matrix(3, 3)
    for ii, i in enumerate(DYN):
        for jj, j in enumerate(DYN):
            Kdd[ii, jj] = K[i, j]
    Kr = Kdd + CdX * WXXi * CdX.T
    return Kr


def espectro(Kr):
    Ks = (Kr + Kr.T) / 2
    lam = mp.eigsy(Ks, eigvals_only=True)
    return sorted([lam[i] for i in range(3)])


def equilibra(Kr):
    """D K D com D = diag(1/sqrt(max_j |K_ij|)) — livre de escala."""
    D = mp.matrix(3, 3)
    for i in range(3):
        s = max(abs(Kr[i, j]) for j in range(3))
        D[i, i] = 1 / mp.sqrt(s) if s > 0 else mp.mpf(1)
    return D * ((Kr + Kr.T) / 2) * D


def analisa(B1V):
    say("")
    say("=" * 72)
    say(f"FUNDO beta-constante beta1={B1V}")
    say("=" * 72)
    mp.mp.dps = 30
    f0 = fundo_mp(A_MIN, B1V)
    kc = 45 * f0['H'] * A_MIN
    say(f"    H(100) = {mp.nstr(f0['H'], 12)}; k_c = {mp.nstr(kc, 12)}")
    fK, fC, fW = compila(B1V)
    say("    [compilacao mpmath] ok")

    tab = {}
    for aval in EPOCAS:
        N = mp.log(mp.mpf(aval))
        say("")
        say(f"    --- epoca a = {aval:g} ---")
        for dps in DPS_LISTA:
            mp.mp.dps = dps
            Nd = mp.log(mp.mpf(aval))
            kcd = 45 * fundo_mp(A_MIN, B1V)['H'] * A_MIN
            for h in H_LISTA:
                try:
                    Kr = kred_mp(Nd, B1V, kcd, fK, fC, fW, h)
                except RuntimeError as e:
                    say(f"      dps={dps:3d} h={h}: ABORTOU ({e})")
                    continue
                lam = espectro(Kr)
                leq = espectro(equilibra(Kr))
                r01 = abs(lam[0]) / abs(lam[1])
                req = abs(leq[0]) / max(abs(x) for x in leq)
                tab[(aval, dps, h)] = (lam, leq, r01, req)
                say(f"      dps={dps:3d} h={h}: lam = "
                    f"{mp.nstr(lam[0], 8)} {mp.nstr(lam[1], 8)} "
                    f"{mp.nstr(lam[2], 8)}")
                say(f"                       |lam0|/|lam1| = "
                    f"{mp.nstr(r01, 6)}   equilibrada: min/max = "
                    f"{mp.nstr(req, 6)}")
        # A1 — entradas de K_red na maior precisao
        mp.mp.dps = DPS_LISTA[-1]
        kcd = 45 * fundo_mp(A_MIN, B1V)['H'] * A_MIN
        Kr = kred_mp(mp.log(mp.mpf(aval)), B1V, kcd, fK, fC, fW, H_LISTA[-1])
        say(f"      K_red (base Psi_f,E_f,dchi; dps={DPS_LISTA[-1]}):")
        for i in range(3):
            say("        " + "  ".join(mp.nstr(Kr[i, j], 8) for j in range(3)))
    return tab


tabs = {}
for B1V in (1, sp.Rational(447, 100)):
    tabs[str(B1V)] = analisa(B1V)

say("")
say("=" * 72)
say("VEREDITO R-6b (criterios pre-declarados no cabecalho)")
say("=" * 72)
for chave, tab in tabs.items():
    say(f"  beta1={chave}:")
    for aval in EPOCAS:
        linha = []
        for dps in DPS_LISTA:
            ks = [k for k in tab if k[0] == aval and k[1] == dps]
            if ks:
                r01 = tab[sorted(ks)[-1]][2]
                linha.append(f"dps{dps}={mp.nstr(r01, 5)}")
        say(f"    a={aval:8g}  |lam0|/|lam1|: " + "  ".join(linha))
        ks = [k for k in tab if k[0] == aval]
        if ks:
            vals = [tab[k][2] for k in ks]
            queda = (max(vals) / min(vals)) if min(vals) > 0 else mp.inf
            say(f"                 variacao total (todos dps,h): fator "
                f"{mp.nstr(queda, 5)}")

os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
with open(os.path.join(HERE, 'out', 'r6b_degenerescencia_K.txt'), 'w',
          encoding='utf-8') as fh:
    fh.write("\n".join(OUT) + "\n")
say("")
say("saida escrita em auditoria/code/out/r6b_degenerescencia_K.txt")
