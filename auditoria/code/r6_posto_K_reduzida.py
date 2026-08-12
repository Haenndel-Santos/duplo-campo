# -*- coding: utf-8 -*-
"""
r6_posto_K_reduzida.py — O POSTO DE K_red: a direcao K<0 do Gate F-b e
um modo ou uma degenerescencia?

MOTIVO (2026-08-12): uma reauditoria externa (ADM/Faddeev-Jackiw
simbolica no ponto fixo tardio) alega que det K_metric = 0
EXATAMENTE, com direcao nula ~ Psi_f puro, e que portanto a direcao
canonizada como fantasma pelo Gate F-b nao e um DOF. Duas coisas ja
foram confirmadas por leitura do codigo:
  (i)  gatef_b_canonica.py:128 postula DYN=[Psi_f,E_f,dchi] (3 DOFs);
  (ii) constroi_canonica() so testa a ASSINATURA de lam (linha 310) e
       depois normaliza com s=1/sqrt(|lam|) (linha 320) — V-ETA passa
       POR CONSTRUCAO mesmo com lam[0] ~ ruido em torno de zero.
Falta o fato empirico. Este script mede.

MAQUINA: identica ao Gate F-b (mesma L2, mesmas fatias, mesmo fundo
beta-constante, mesmo reduz_ponto/reduz_trilha, mesmos MULT/DYN) —
copiada verbatim para garantir que estamos medindo a MESMA K_red que o
Gate F-b canonizou, e nao uma reimplementacao.

MEDIDAS (pre-declaradas):
  M1 — espectro de K_red 3x3 nos marcos: lam[0],lam[1],lam[2] e a
       razao adimensional  rho_K = |lam_0| / max|lam| .
  M2 — a direcao nula: autovetor de lam[0] na base (Psi_f,E_f,dchi);
       componente |v[Psi_f]|^2.
  M3 — K7 sem reducao: |K7[Psi_f,:]|/max|K7| (Psi_f ja e linha de
       multiplicador na acao original?) e espectro de K7.
  M4 — controle de escala: rho_K em GR+escalar seria ~1 (1 dof, sem
       degenerescencia). Aqui o controle e a comparacao lam1 vs lam2.
  M5 — reducao alternativa com Psi_f tratado como multiplicador
       (MULT=[0,1,2,4,3], DYN=[5,6]): a K 2x2 resultante e positiva
       definida?

CRITERIOS (pre-declarados; leitura so depois de rodar):
  rho_K <= 1e-12 nos marcos  -> DEGENERESCENCIA ESTRUTURAL: a direcao
      K<0 e nula; a normalizacao canonica do F-b divide por zero e o
      omega_0/H ~ 7-12 nao e uma frequencia fisica. Gate F cai.
  rho_K >= 1e-3              -> a direcao K<0 e um modo genuino; a
      critica externa nao se aplica ao nosso gate.
  1e-12 < rho_K < 1e-3       -> ZONA CINZA: float64 nao decide (o
      roundoff catastrofico vive em ~1e-16 relativo); exige rodada em
      precisao estendida antes de qualquer leitura.

Requer sympy, numpy. Grade reduzida (NPTS menor que o F-b) porque o
espectro e uma medida LOCAL — nao ha integracao aqui.

Uso (raiz do repo, venv ativo):
    python auditoria/code/r6_posto_K_reduzida.py
Saida em auditoria/code/out/r6_posto_K_reduzida.txt
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

from tdcp_pert_lib import (t, a_s, b_s, xi_s, H_s, Hf_s, Hd_s, Hfd_s, xid_s,
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


# ---- constantes verbatim do gatef_b_canonica.py -------------------
NOMES = ['Phi_g', 'B_g', 'Phi_f', 'Psi_f', 'B_f', 'E_f', 'dchi']
MULT = [0, 1, 2, 4]
DYN = [3, 5, 6]
A_MIN, A_MAX = 100.0, 80000.0
NPTS = 3000
MARCAS = list(np.geomspace(150.0, 75000.0, 40))

MU = 1.0
MG2, MF2 = 1.0, MU
ME2 = MU / (1.0 + MU)
M2 = 1.0
B0V, B2V, B4V = 1.0, -0.4, 0.5
RHO0 = 0.3

say("=" * 72)
say("R-6 — O POSTO DE K_red: a direcao K<0 do Gate F-b e modo ou")
say("degenerescencia?")
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

say("[fatias] {Fb,Fp,Fpp} x {b0..b4}, taxas livres ...")
LIVRES = (a_s, b_s, xi_s, H_s, Hf_s, Hd_s, Hfd_s, xid_s,
          chid_s, chidd_s, Ub, Up, Upp, ksym, Mf2, Meff2)
FIXOS = {Mg2: 1, m2: 1, rho_s: 0}
BETAS = (b0, b1, b2, b3, b4)


def fatias(M):
    Msub = M.subs(FIXOS)
    base_s = Msub.subs({Fb: 0, Fp: 0, Fpp: 0})
    out = {'base': sp.lambdify(LIVRES, base_s, modules='numpy')}
    for tag, fsub in (('Fb', {Fb: 1, Fp: 0, Fpp: 0}),
                      ('Fp', {Fb: 0, Fp: 1, Fpp: 0}),
                      ('Fpp', {Fb: 0, Fp: 0, Fpp: 1})):
        for n, bn in enumerate(BETAS):
            bsub = {bm: (1 if mm == n else 0) for mm, bm in enumerate(BETAS)}
            Sl = Msub.subs(fsub).subs(bsub) - base_s
            out[(tag, n)] = sp.lambdify(LIVRES, Sl, modules='numpy')
    return out


FK, FC, FW = fatias(K7), fatias(C7), fatias(W7)
say("[fatias] prontas")


def monta(fat, args, bvals, bp, bpp):
    M = np.array(fat['base'](*args), float).copy()
    for n in range(5):
        if bvals[n]:
            M += bvals[n] * np.array(fat[('Fb', n)](*args), float)
        if bp[n]:
            M += bp[n] * np.array(fat[('Fp', n)](*args), float)
        if bpp[n]:
            M += bpp[n] * np.array(fat[('Fpp', n)](*args), float)
    return M


def fundo_bconst(a, B1V):
    kap = 1.0 / MU
    meff2 = ME2
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
    H2 = meff2 * r * r * Vf / (3.0 * MU)
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


def builder_bconst(B1V):
    def build(kc, npts):
        Ns = np.linspace(np.log(A_MIN), np.log(A_MAX), npts)
        Hs_arr = np.zeros(npts)
        Ms = {x: np.zeros((npts, 7, 7)) for x in 'KCW'}
        for p, N in enumerate(Ns):
            a = np.exp(N)
            f = fundo_bconst(a, B1V)
            if f is None:
                raise RuntimeError(f"fundo invalido em a={a:.1f}")
            Hs_arr[p] = f['H']
            args = (a, f['r'] * a, f['xi'], f['H'], f['Hf'],
                    f['Hd'], f['Hfd'], f['xid'], 0.0, 0.0,
                    f['Ub'], 0.0, 0.3, kc, MF2, ME2)
            bvals = (B0V, B1V, B2V, 0.0, B4V)
            Ms['K'][p] = monta(FK, args, bvals, (0,) * 5, (0,) * 5)
            Ms['C'][p] = monta(FC, args, bvals, (0,) * 5, (0,) * 5)
            Ms['W'][p] = monta(FW, args, bvals, (0,) * 5, (0,) * 5)
        return Ns, Hs_arr, Ms
    return build


def reduz_ponto(Kt, Ct, Wt, Cdot, mult, dyn):
    K = Kt.copy()
    C = Ct.copy()
    W = Wt.copy()
    n = K.shape[0]
    for i in mult:
        if np.max(np.abs(K[i, :])) > 1e-10 * max(1.0, np.max(np.abs(K))):
            raise RuntimeError("linha K do multiplicador nao-nula")
        for j in range(n):
            cij = C[i, j]
            cd = Cdot[i, j]
            if i == j:
                W[i, i] += cd
            else:
                W[i, j] += cd
                W[j, i] += cd
                C[j, i] -= cij
        C[i, :] = 0.0
    WXX = W[np.ix_(mult, mult)]
    if np.linalg.cond(WXX) > 1e12:
        raise RuntimeError("W_XX mal condicionada")
    WXXi = np.linalg.inv(WXX)
    return (K[np.ix_(dyn, dyn)] + C[np.ix_(dyn, mult)] @ WXXi
            @ C[np.ix_(dyn, mult)].T,
            C[np.ix_(dyn, dyn)] - C[np.ix_(dyn, mult)] @ WXXi
            @ W[np.ix_(mult, dyn)],
            W[np.ix_(dyn, dyn)] - W[np.ix_(dyn, mult)] @ WXXi
            @ W[np.ix_(mult, dyn)])


def reduz_trilha(Ms, Ns, Hs_arr, mult=None, dyn=None):
    mult = MULT if mult is None else mult
    dyn = DYN if dyn is None else dyn
    nd = len(dyn)
    npts = len(Ns)
    Cdots = np.gradient(Ms['C'], Ns, axis=0) * Hs_arr[:, None, None]
    Kr = np.zeros((npts, nd, nd))
    Cr = np.zeros((npts, nd, nd))
    Wr = np.zeros((npts, nd, nd))
    for p in range(npts):
        Kr[p], Cr[p], Wr[p] = reduz_ponto(
            Ms['K'][p], Ms['C'][p], Ms['W'][p], Cdots[p], mult, dyn)
    return Kr, Cr, Wr


# ------------------------------------------------------------------
def analisa(B1V):
    say("")
    say("=" * 72)
    say(f"FUNDO beta-constante beta1={B1V:g}")
    say("=" * 72)
    f0 = fundo_bconst(A_MIN, B1V)
    kc = 45.0 * f0['H'] * A_MIN
    Ns = np.linspace(np.log(A_MIN), np.log(A_MAX), NPTS)
    build = builder_bconst(B1V)
    _, Hs_arr, Ms = build(kc, NPTS)
    Kr, Cr, Wr = reduz_trilha(Ms, Ns, Hs_arr)
    aas = np.exp(Ns)
    mark_idx = sorted(set(int(np.argmin(np.abs(aas - am))) for am in MARCAS))
    mark_idx = [m for m in mark_idx if 2 <= m <= NPTS - 3]

    # ---- M3: K7 sem reducao ---------------------------------------
    p_mid = mark_idx[len(mark_idx) // 2]
    K7n = Ms['K'][p_mid]
    esc7 = np.max(np.abs(K7n))
    say("")
    say(f"    M3 — K7 (sem reducao) em a={aas[p_mid]:.0f}, escala "
        f"max|K7|={esc7:.3e}")
    for i, nm in enumerate(NOMES):
        say(f"       |K7[{nm:>6},:]|/max = "
            f"{np.max(np.abs(K7n[i, :]))/esc7:.3e}")
    lam7 = np.linalg.eigvalsh(0.5 * (K7n + K7n.T))
    say(f"       espectro K7 = " +
        " ".join(f"{x:+.3e}" for x in lam7))

    # ---- M1 + M2: espectro de K_red -------------------------------
    say("")
    say("    M1/M2 — espectro de K_red 3x3 (base Psi_f,E_f,dchi):")
    say(f"    {'a':>8} {'kh':>7} {'lam0':>12} {'lam1':>12} {'lam2':>12}"
        f" {'rho_K':>10} {'|v0.Psi_f|^2':>12}")
    rhos = []
    psif_fr = []
    for mi in mark_idx:
        Ks = 0.5 * (Kr[mi] + Kr[mi].T)
        lam, E = np.linalg.eigh(Ks)
        rho = abs(lam[0]) / max(abs(lam).max(), 1e-300)
        v0 = E[:, 0]
        fr = float(v0[0] ** 2 / (v0 @ v0))
        rhos.append(rho)
        psif_fr.append(fr)
        kh = kc / (aas[mi] * Hs_arr[mi])
        say(f"    {aas[mi]:8.0f} {kh:7.2f} {lam[0]:+12.3e} {lam[1]:+12.3e}"
            f" {lam[2]:+12.3e} {rho:10.2e} {fr:12.4f}")
    rhos = np.array(rhos)
    say("")
    say(f"    rho_K: mediana = {np.median(rhos):.3e}; max = {rhos.max():.3e};"
        f" min = {rhos.min():.3e}")
    say(f"    |v0.Psi_f|^2: mediana = {np.median(psif_fr):.4f}; "
        f"min = {min(psif_fr):.4f}")

    if rhos.max() <= 1e-12:
        vd = "DEGENERESCENCIA ESTRUTURAL (rho_K <= 1e-12 em todos os marcos)"
    elif np.median(rhos) >= 1e-3:
        vd = "MODO GENUINO (rho_K >= 1e-3)"
    else:
        vd = "ZONA CINZA — float64 nao decide; exige precisao estendida"
    say(f"    >>> M1 veredito: {vd}")

    # ---- M5: Psi_f como multiplicador ------------------------------
    say("")
    say("    M5 — reducao alternativa com Psi_f tratado como multiplicador")
    say("         (MULT=[Phi_g,B_g,Phi_f,B_f,Psi_f], DYN=[E_f,dchi]):")
    try:
        Kr2, Cr2, Wr2 = reduz_trilha(Ms, Ns, Hs_arr,
                                     mult=[0, 1, 2, 4, 3], dyn=[5, 6])
        neg = 0
        say(f"    {'a':>8} {'lam0(2x2)':>12} {'lam1(2x2)':>12}")
        for mi in mark_idx:
            l2 = np.linalg.eigvalsh(0.5 * (Kr2[mi] + Kr2[mi].T))
            if l2[0] < 0:
                neg += 1
            if mi in mark_idx[::4]:
                say(f"    {aas[mi]:8.0f} {l2[0]:+12.3e} {l2[1]:+12.3e}")
        say(f"    autovalores negativos da K 2x2: {neg}/{len(mark_idx)} "
            f"marcos")
    except RuntimeError as e:
        say(f"    [M5 ABORTOU] {e}")
        say("       (isto e informativo: Psi_f NAO e multiplicador na acao")
        say("        original — a linha K7[Psi_f,:] nao e nula.)")

    return dict(rho_med=float(np.median(rhos)), rho_max=float(rhos.max()),
                psif=float(np.median(psif_fr)), veredito=vd)


res = {}
for B1V in (1.0, 4.47):
    res[B1V] = analisa(B1V)

say("")
say("=" * 72)
say("VEREDITO R-6 (criterios pre-declarados no cabecalho)")
say("=" * 72)
for B1V in (1.0, 4.47):
    r = res[B1V]
    say(f"  beta1={B1V:g}: rho_K mediana = {r['rho_med']:.2e} "
        f"(max {r['rho_max']:.2e}); |v0.Psi_f|^2 = {r['psif']:.3f}")
    say(f"           -> {r['veredito']}")

os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
with open(os.path.join(HERE, 'out', 'r6_posto_K_reduzida.txt'), 'w',
          encoding='utf-8') as fh:
    fh.write("\n".join(OUT) + "\n")
say("")
say("saida escrita em auditoria/code/out/r6_posto_K_reduzida.txt")
