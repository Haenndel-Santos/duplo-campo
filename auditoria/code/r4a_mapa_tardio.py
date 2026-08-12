# -*- coding: utf-8 -*-
"""
r4a_mapa_tardio.py — R-4a: o MAPA do fenomeno tardio (bloco 1 do R-4).

CONTEXTO (docs/resultado_r3c_mecanismo.md). A cadeia R-3 -> R-3b ->
R-3c estabeleceu: existe crescimento REAL ~ +1 a +2/H do bloco metrico
na banda k_phys ~ H em fundos tardios da classe — nao-parametrico
(R-3b), nao-secular (R-3c: taxa plana sob desvio 1%->7%), e presente
no fundo BETA-CONSTANTE ESTATICO beta1=4.47 (R-3c braco G: +1.08, com
delta-chi desacoplado exato). O fundo pousado herda a instabilidade do
ponto da classe onde senta. A "estrutura IR" do R-3b relê-se como
CRUZAMENTO DE HORIZONTE: k_c=25000 cruza k_phys=H em a~22000, FORA da
janela tardia [8000,18000] — por isso +0.06 la; k_c=12500 cruza em
a~11000, DENTRO — por isso +1. Tres perguntas decidem o enunciado:

  (1) A banda e artefato de instrumento? Nenhum controle anterior
      cobriu GR com cruzamento DENTRO de uma janela tardia de fundo
      estatico tipo-dS. -> R4a-NULL (abortivo).
  (2) Onde comeca a regiao instavel em beta1? A R-1 amostrou beta1<=2
      MAS com k_phys/H <~ 0.5 nas janelas tardias (k_c<=100, a<=2000)
      — a banda nunca foi sondada la. Se ate beta1=1 crescer na banda,
      o "estavel tarde" de D2/R-1 era artefato de amostragem em k e o
      enunciado reescreve DE NOVO; se so beta1 grande crescer, e
      esquina. -> R4a-MAPA.
  (3) O crescimento da banda e TRANSIENTE de cruzamento (modo cresce
      ao redor do cruzamento e morre no super-horizonte profundo ->
      lnA finito por modo, dano mapeavel) ou SUSTENTADO (no-go
      dinamico real da regiao)? -> R4a-EXT (a ate 80000).

DESENHO (maquinaria R-3/R-3b/R-3c verbatim; grade a=[100,20000], npts
20000; janelas e normas identicas; k_phys/H impresso nas bordas de
cada janela):
  R4a-NULL: GR + Lambda (H=1.14, o H do pousado) + chi espectador
      estatico (Upp=0.3), k_c in {12500, 1250} — cruzamento em a~11000
      (dentro da tardia) e a~1100 (IR profundo). Mesmo pipeline
      (reducao + RK4). CRITERIO: nenhuma janela com taxa > +0.1H;
      FALHA -> NAO INTERPRETAR o mapa (artefato na banda).
  R4a-MAPA: fundos beta-constantes ESTATICOS (raiz cubica + taxas
      analiticas, dust rho0=0.3, mu=1, beta0=1, beta2=-0.4, beta4=0.5)
      com beta1 in {1.0, 2.0, 3.0, 4.47} x k in {banda, 3x, 0.1x},
      onde k_banda = H_fundo(11000) * 11000 (cruzamento no meio da
      tardia, por fundo). delta-chi espectador (chid=0, Up=0, Upp=0.3).
      Sintese: tabela beta1 x k -> taxa tardia met, lnA_met, negK.
      LEITURA PRE-DECLARADA: beta1*=menor beta1 com taxa_banda >= 0.5;
      se beta1=1 >= 0.5 -> CLASSE-INTEIRA (artefato de amostragem em k
      na R-1/D2 — reavaliar enunciados de novo); se so beta1 altos ->
      ESQUINA com fronteira beta1*; se nem 4.47 crescer -> contradicao
      com R-3c G1 (diagnosticar instrumento antes de qualquer coisa).
  R4a-EXT: a=[100,80000] (npts 24000; janela extra tardia2
      [30000,70000], k_phys/H ~ 0.36->0.14 p/ k_c=12500), dois fundos:
      beta-const 4.47 e POUSADO (trajetoria original da Fase A/B).
      CRITERIO por fundo: taxa met max na tardia2:
        >= 0.5 -> SUSTENTADA (persiste no super-horizonte profundo:
                  no-go dinamico real da regiao; R-4b mapeia contra
                  vinculos com essa gravidade);
        <= 0.1 -> TRANSIENTE-DE-CRUZAMENTO (o modo cresce ~lnA finito
                  ao redor do cruzamento e depois dilui — o dano e
                  lnA(k, celula), mapeavel; forma fraca no cap.07);
        senao -> intermediario (reportar; possivel cauda longa).
      Conditioning: a^3 ~ 5e14 em a=80000 — se a reducao truncar
      (guarda cond>1e12), reportar a_max e ler o que houver ate la.
  Ancoras (5000, 15000 [, 40000, 70000 na EXT]): sigma/H congelado
      reduzido (pre-escala) + negK — trilha estrutural por beta1
      (insumo Gate F: negK=1 valia em beta1<=2 a a=400; aqui esquina e
      profundidade novas).
  ANOMALIA IR DO POUSADO (k=1250 tardia: cresce so com dinamica
      residual — R-3c) fica DECLARADA FORA deste mapa (sub-estrutura
      aberta; nao bloqueia o quadro da banda).

HARDCODES/REFERENCIAS: pousado k_c=12500 tardia met +0.98 (R-3/R-3b);
beta-const 4.47 k_c=12500 tardia met +1.08 (R-3c G1) — o braco
(4.47, banda) do mapa deve reproduzi-lo (k_banda(4.47) ~ 12375 ~
12500; tolerancia frouxa 0.3 por ser k ligeiramente diferente).

Requer sympy, numpy, scipy. ~8-15 min.
Uso (raiz do repo, venv ativo):
    python auditoria/code/r4a_mapa_tardio.py
Saida em auditoria/code/out/r4a_mapa_tardio.txt
"""
import importlib.util
import os
import sys
import time

import numpy as np
import sympy as sp
from scipy.interpolate import CubicSpline
from scipy.optimize import brentq

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
                           quadratic_matrices, lagrangian_GG,
                           chi_lagrangian, scalar_metric_g,
                           substitute_bg_functions, make_bg_functions,
                           z_average, eps_part, cut, symbolize)

T0 = time.time()
OUT = []


def say(*a):
    line = " ".join(str(x) for x in a)
    print(f"[{time.time()-T0:7.1f}s] {line}")
    OUT.append(line)


NOMES = ['Phi_g', 'B_g', 'Phi_f', 'Psi_f', 'B_f', 'E_f', 'dchi']
MULT = [0, 1, 2, 4]
DYN = [3, 5, 6]
IDX_MET_IC = [0, 1, 3, 4]
JAN_STD = [("pre", 150.0, 450.0), ("rolagem", 760.0, 2050.0),
           ("pouso", 2100.0, 6800.0), ("tardia", 8000.0, 18000.0)]
JAN_EXT = JAN_STD + [("tardia2", 30000.0, 70000.0)]
A_MIN = 100.0
A_MAX_STD, A_MAX_EXT = 20000.0, 80000.0
NPTS_STD, NPTS_EXT = 20000, 24000
ANC_STD = [5000.0, 15000.0]
ANC_EXT = [5000.0, 15000.0, 40000.0, 70000.0]

B1S = [1.0, 2.0, 3.0, 4.47]
A_REF_BANDA = 11000.0
LAM_GR = 3.9  # 3*H^2 com H=1.14 (o H do pousado)

# parametros (identicos a R-3/R-3b/R-3c)
MU = 1.0
MG2, MF2 = 1.0, MU
ME2 = MU / (1.0 + MU)
M2 = 1.0
B0V, B2V, B4V = 1.0, -0.4, 0.5
B10 = 1.0
RHO0 = 0.3
VST = 1.0

say("=" * 72)
say("R-4a — O MAPA DO FENOMENO TARDIO (bloco 1 do R-4)")
say("=" * 72)

# ------------------------------------------------------------------
# V1 + montagem + fatias (verbatim)
# ------------------------------------------------------------------
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


# ------------------------------------------------------------------
# fundos: beta-constante (R-1) e rolagem original (Fase A/B)
# ------------------------------------------------------------------
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


a_, b_, ch_ = sp.symbols('a b chi', positive=True)
pa_, pb_, pch_ = sp.symbols('p_a p_b p_chi', real=True)
Mg2s, Mf2s, Me2s, m2s = sp.symbols('Mg2 Mf2 Meff2 m2', positive=True)
b0s, b2s, b4s = sp.symbols('beta_0 beta_2 beta_4', real=True)
Hs_, Hfs_, chds_ = sp.symbols('H H_f chidot', real=True)
b10s, vsts = sp.symbols('b1_0 v_star', positive=True)
b1_conc = b10s * (1 + ch_**2 / vsts**2)
rr_ = b_ / a_
Vgc_s = b0s + 3 * rr_ * b1_conc + 3 * rr_**2 * b2s
Vfc_s = b1_conc + 3 * rr_ * b2s + rr_**3 * b4s
Hg_sym = (-pa_**2 / (12 * Mg2s * a_) + pch_**2 / (2 * a_**3)
          + m2s * Me2s * a_**3 * Vgc_s)
Hf_sym = -pb_**2 / (12 * Mf2s * b_) + m2s * Me2s * a_**3 * Vfc_s
CANON = [(a_, pa_), (b_, pb_), (ch_, pch_)]
Om_sym = sp.expand(sum(sp.diff(Hg_sym, q) * sp.diff(Hf_sym, p)
                       - sp.diff(Hg_sym, p) * sp.diff(Hf_sym, q)
                       for q, p in CANON))
Om_v = sp.expand(Om_sym.subs({pa_: -6 * Mg2s * a_**2 * Hs_,
                              pb_: -6 * Mf2s * b_**2 * Hfs_,
                              pch_: a_**3 * chds_}))
Om_fn = sp.lambdify((a_, b_, ch_, chds_, Hs_, Hfs_,
                     Mg2s, Mf2s, Me2s, m2s, b0s, b2s, b4s, b10s, vsts),
                    Om_v, modules='math')


def beta1(ch, vst):
    return B10 * (1.0 + ch * ch / (vst * vst))


def dbeta1(ch, vst):
    return 2.0 * B10 * ch / (vst * vst)


def U_pot(ch, mu2, lam, U0):
    return -0.5 * mu2 * ch * ch + 0.25 * lam * ch**4 + U0


def dU_pot(ch, mu2, lam):
    return -mu2 * ch + lam * ch**3


def Hf2_of(r, ch, vst):
    b1v = beta1(ch, vst)
    Vf = b1v + 3 * r * B2V + r**3 * B4V
    return M2 * ME2 * Vf / (3 * MF2 * r**3)


def H2_of(r, ch, chd, a, vst, mu2, lam, U0):
    b1v = beta1(ch, vst)
    Vg = B0V + 3 * r * b1v + 3 * r * r * B2V
    return (0.5 * chd * chd + U_pot(ch, mu2, lam, U0) + RHO0 / a**3
            + M2 * ME2 * Vg) / (3 * MG2)


def Om_num(r, ch, chd, a, vst, mu2, lam, U0):
    H2 = H2_of(r, ch, chd, a, vst, mu2, lam, U0)
    Hf2 = Hf2_of(r, ch, vst)
    if H2 <= 0 or Hf2 <= 0:
        return float('nan')
    return Om_fn(a, r * a, ch, chd, np.sqrt(H2), np.sqrt(Hf2),
                 MG2, MF2, ME2, M2, B0V, B2V, B4V, B10, vst)


def acha_raiz(r_prev, ch, chd, a, vst, mu2, lam, U0):
    for fator in (0.08, 0.25, 0.6):
        lo, hi = r_prev * (1 - fator), r_prev * (1 + fator)
        grade = np.linspace(lo, hi, 61)
        vals = np.array([Om_num(x, ch, chd, a, vst, mu2, lam, U0)
                         for x in grade])
        fin = np.isfinite(vals)
        for i in range(len(grade) - 1):
            if fin[i] and fin[i + 1] and vals[i] * vals[i + 1] < 0:
                try:
                    return brentq(
                        lambda x: Om_num(x, ch, chd, a, vst, mu2, lam, U0),
                        grade[i], grade[i + 1], xtol=1e-14)
                except ValueError:
                    continue
    return None


def raiz_cubica(a, ch, chd, vst, mu2, lam, U0):
    b1v = beta1(ch, vst)
    rho_tot = 0.5 * chd * chd + U_pot(ch, mu2, lam, U0) + RHO0 / a**3
    rt = rho_tot / (M2 * ME2)
    kap = MG2 / MF2
    rr = np.roots([kap * B4V - 3 * B2V, -3 * b1v,
                   3 * kap * B2V - B0V - rt, kap * b1v])
    reais = sorted(x.real for x in rr if abs(x.imag) < 1e-9 and x.real > 1e-12)
    return reais[0] if reais else None


def integra_alvo(g_end=2.0, mchi2=30.0, vst=1.0, a0=0.01, a1=1e5, dN=5e-4):
    v = g_end * vst
    mu2 = 0.5 * mchi2
    lam = mu2 / (v * v)
    U0 = 0.25 * mu2 * v * v
    N0, N1 = np.log(a0), np.log(a1)
    n = int((N1 - N0) / dN) + 1
    ch, y = 1e-3 * v, 0.0
    r = raiz_cubica(a0, ch, 0.0, vst, mu2, lam, U0)
    rp = 3.0 * r
    Hprev = None
    rec = {kk: [] for kk in ('N', 'a', 'r', 'xi', 'H', 'Hfv', 'ch', 'chd',
                             'chidd', 'desl')}
    for i in range(n):
        N = N0 + i * dN
        a = np.exp(N)
        b1v = beta1(ch, vst)
        Vg = B0V + 3 * r * b1v + 3 * r * r * B2V
        resto = U_pot(ch, mu2, lam, U0) + RHO0 / a**3 + M2 * ME2 * Vg
        den = 3 * MG2 - 0.5 * y * y
        if den <= 0 or resto <= 0:
            raise RuntimeError(f"fundo abortou (H^2) em a={a:.3f}")
        H = np.sqrt(resto / den)
        chd = H * y
        Hf2 = Hf2_of(r, ch, vst)
        if Hf2 <= 0:
            raise RuntimeError(f"fundo abortou (H_f^2) em a={a:.3f}")
        Hfv = np.sqrt(Hf2)
        xi = H * (1.0 + rp / r) / Hfv
        chidd = (-3 * H * chd - dU_pot(ch, mu2, lam)
                 - M2 * ME2 * dbeta1(ch, vst) * (xi + 3 * r))
        Hp = 0.0 if Hprev is None else (H - Hprev) / dN
        yp = chidd / (H * H) - (Hp / H) * y
        if i % max(1, n // 20000) == 0:
            for kk, vv in (('N', N), ('a', a), ('r', r), ('xi', xi),
                           ('H', H), ('Hfv', Hfv), ('ch', ch), ('chd', chd),
                           ('chidd', chidd), ('desl', (H - r * Hfv) / H)):
                rec[kk].append(vv)
        ch += dN * y
        y += dN * yp
        r_new = acha_raiz(r, ch, H * y, np.exp(N + dN), vst, mu2, lam, U0)
        if r_new is None:
            raise RuntimeError(f"fundo perdeu a raiz em a={np.exp(N+dN):.3f}")
        rp = (r_new - r) / dN
        r = r_new
        Hprev = H
    rec = {kk: np.array(vv) for kk, vv in rec.items()}
    rec['v'] = v
    rec['vst'] = vst
    rec['mu2'] = mu2
    rec['lam'] = lam
    rec['U0'] = U0
    return rec


def make_ctx(rec, rotulo):
    spl = {kk: CubicSpline(rec['N'], rec[kk])
           for kk in ('r', 'xi', 'H', 'Hfv', 'ch', 'chd', 'chidd')}
    return dict(rec=rec, spl=spl, dH=spl['H'].derivative(),
                dHf=spl['Hfv'].derivative(), dxi=spl['xi'].derivative(),
                rotulo=rotulo)


def bg_ponto(ctx, N):
    spl = ctx['spl']
    rec = ctx['rec']
    H = float(spl['H'](N))
    ch = float(spl['ch'](N))
    mu2, lam, U0 = rec['mu2'], rec['lam'], rec['U0']
    a = np.exp(N)
    return dict(
        a=a, r=float(spl['r'](N)), xi=float(spl['xi'](N)), H=H,
        Hf=float(spl['Hfv'](N)), ch=ch, chd=float(spl['chd'](N)),
        chidd=float(spl['chidd'](N)),
        Hd=H * float(ctx['dH'](N)), Hfd=H * float(ctx['dHf'](N)),
        xid=H * float(ctx['dxi'](N)),
        Ubv=U_pot(ch, mu2, lam, U0) + RHO0 / a**3,
        Upv=dU_pot(ch, mu2, lam), Uppv=-mu2 + 3 * lam * ch * ch)


def builder_rolagem(ctx, a_max):
    def build(kc, npts):
        Ns = np.linspace(np.log(A_MIN), np.log(a_max), npts)
        Hs_arr = np.zeros(npts)
        Ms = {x: np.zeros((npts, 7, 7)) for x in 'KCW'}
        for p, N in enumerate(Ns):
            f = bg_ponto(ctx, N)
            Hs_arr[p] = f['H']
            args = (f['a'], f['r'] * f['a'], f['xi'], f['H'], f['Hf'],
                    f['Hd'], f['Hfd'], f['xid'], f['chd'], f['chidd'],
                    f['Ubv'], f['Upv'], f['Uppv'], kc, MF2, ME2)
            bvals = (B0V, beta1(f['ch'], VST), B2V, 0.0, B4V)
            bp = (0.0, dbeta1(f['ch'], VST), 0.0, 0.0, 0.0)
            bpp = (0.0, 2.0 * B10 / VST**2, 0.0, 0.0, 0.0)
            Ms['K'][p] = monta(FK, args, bvals, bp, bpp)
            Ms['C'][p] = monta(FC, args, bvals, bp, bpp)
            Ms['W'][p] = monta(FW, args, bvals, bp, bpp)
        return Ns, Hs_arr, Ms
    return build


def builder_bconst(B1V, a_max):
    def build(kc, npts):
        Ns = np.linspace(np.log(A_MIN), np.log(a_max), npts)
        Hs_arr = np.zeros(npts)
        Ms = {x: np.zeros((npts, 7, 7)) for x in 'KCW'}
        for p, N in enumerate(Ns):
            a = np.exp(N)
            f = fundo_bconst(a, B1V)
            if f is None:
                raise RuntimeError(f"fundo beta-constante invalido em "
                                   f"a={a:.1f}")
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


# ------------------------------------------------------------------
# reducao + evolucao (verbatim)
# ------------------------------------------------------------------
def reduz_ponto(Kt, Ct, Wt, Cdot, mult, dyn):
    K = Kt.copy()
    C = Ct.copy()
    W = Wt.copy()
    n = K.shape[0]
    for i in mult:
        if np.max(np.abs(K[i, :])) > 1e-10 * max(1.0, np.max(np.abs(K))):
            raise RuntimeError(
                f"linha K do multiplicador {i} nao-nula "
                f"(max {np.max(np.abs(K[i, :])):.2e} vs escala "
                f"{np.max(np.abs(K)):.2e})")
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


def reduz_trilha(Ms, Ns, Hs_arr, mult, dyn):
    npts = len(Ns)
    Cdots = np.gradient(Ms['C'], Ns, axis=0) * Hs_arr[:, None, None]
    nd = len(dyn)
    Kr = np.zeros((npts, nd, nd))
    Cr = np.zeros((npts, nd, nd))
    Wr = np.zeros((npts, nd, nd))
    p_fim = npts
    for p in range(npts):
        try:
            Kr[p], Cr[p], Wr[p] = reduz_ponto(
                Ms['K'][p], Ms['C'][p], Ms['W'][p], Cdots[p], mult, dyn)
        except RuntimeError as e:
            say(f"    [ESTRUTURA] reducao falhou em a={np.exp(Ns[p]):.1f}: "
                f"{e} — trilha truncada")
            p_fim = p
            break
    Ns_t, Hs_t = Ns[:p_fim], Hs_arr[:p_fim]
    Kr, Cr, Wr = Kr[:p_fim], Cr[:p_fim], Wr[:p_fim]
    Krd = np.gradient(Kr, Ns_t, axis=0) * Hs_t[:, None, None]
    Crd = np.gradient(Cr, Ns_t, axis=0) * Hs_t[:, None, None]
    return Kr, Cr, Wr, Krd, Crd, Ns_t, Hs_t


def evolui(Kr, Cr, Wr, Krd, Crd, Ns, Hs_arr, janelas, met_idx=(0, 1)):
    npts = len(Ns)
    nd = Kr.shape[1]
    aas = np.exp(Ns)
    Hmid = {}
    for nome, lo, hi in janelas:
        pm = int(np.argmin(np.abs(aas - np.sqrt(lo * hi))))
        Hmid[nome] = Hs_arr[pm]
    taxas_f, taxas_m, amps_m = [], [], []
    for ic in range(2 * nd):
        q = np.zeros(nd)
        qd = np.zeros(nd)
        if ic < nd:
            q[ic] = 1.0
        else:
            qd[ic - nd] = 1.0
        tcum = 0.0
        amp_m = 0.0
        reg = {nome: [None] * 6 for nome, _, _ in janelas}
        for p in range(npts - 1):
            dN = Ns[p + 1] - Ns[p]
            dt = dN / Hs_arr[p]
            Ki = np.linalg.inv(Kr[p])
            A = Krd[p] + Cr[p] - Cr[p].T
            B = Crd[p] + Wr[p]

            def rhs(qq, vv):
                return -Ki @ (A @ vv + B @ qq)

            k1q, k1v = qd, rhs(q, qd)
            k2q, k2v = qd + .5 * dt * k1v, rhs(q + .5 * dt * k1q,
                                               qd + .5 * dt * k1v)
            k3q, k3v = qd + .5 * dt * k2v, rhs(q + .5 * dt * k2q,
                                               qd + .5 * dt * k2v)
            k4q, k4v = qd + dt * k3v, rhs(q + dt * k3q, qd + dt * k3v)
            q = q + dt * (k1q + 2 * k2q + 2 * k3q + k4q) / 6
            qd = qd + dt * (k1v + 2 * k2v + 2 * k3v + k4v) / 6
            tcum += dt
            aa = aas[p + 1]
            n2_f = q @ q + qd @ qd
            if met_idx is None:
                n2_m = n2_f
            else:
                n2_m = sum(q[j]**2 + qd[j]**2 for j in met_idx)
            ln_f = np.log(max(np.sqrt(n2_f), 1e-300))
            ln_m = np.log(max(np.sqrt(n2_m), 1e-300))
            if ic in IDX_MET_IC:
                amp_m = max(amp_m, ln_m)
            for nome, lo, hi in janelas:
                r = reg[nome]
                if r[0] is None and aa >= lo:
                    r[0], r[1], r[4] = ln_f, tcum, ln_m
                if r[2] is None and aa >= hi:
                    r[2], r[3], r[5] = ln_f, tcum, ln_m
        tx_f, tx_m = {}, {}
        for nome, lo, hi in janelas:
            r = reg[nome]
            if r[0] is not None and r[2] is not None and r[3] > r[1]:
                tx_f[nome] = (r[2] - r[0]) / (r[3] - r[1]) / Hmid[nome]
                tx_m[nome] = (r[5] - r[4]) / (r[3] - r[1]) / Hmid[nome]
            else:
                tx_f[nome] = float('nan')
                tx_m[nome] = float('nan')
        taxas_f.append(tx_f)
        taxas_m.append(tx_m)
        amps_m.append(amp_m if ic in IDX_MET_IC else float('nan'))
    return taxas_f, taxas_m, amps_m


def roda(rotulo, build, kc, npts, janelas, ancoras):
    say("")
    say(f"--- {rotulo}: k_c={kc:g}, npts={npts} ---")
    Ns, Hs_arr, Ms = build(kc, npts)
    Kr, Cr, Wr, Krd, Crd, Ns_t, Hs_t = reduz_trilha(Ms, Ns, Hs_arr,
                                                    MULT, DYN)
    a_max_val = float(np.exp(Ns_t[-1]))
    if a_max_val < 0.99 * np.exp(Ns[-1]):
        say(f"    [reducao] TRUNCADA em a={a_max_val:.0f}")
    aas_t = np.exp(Ns_t)
    negK15 = -1
    for a_anc in ancoras:
        if a_anc > a_max_val:
            continue
        p_anc = int(np.argmin(np.abs(aas_t - a_anc)))
        sK = max(np.max(np.abs(Kr[p_anc])), 1e-30)
        pares = d1.agrupa_pares(d1.qep_modes(Kr[p_anc] / sK,
                                             Cr[p_anc] / sK,
                                             Wr[p_anc] / sK))
        eigK = np.linalg.eigvalsh(0.5 * (Kr[p_anc] + Kr[p_anc].T))
        negK = int(np.sum(eigK < -1e-12))
        if abs(a_anc - 15000.0) < 1:
            negK15 = negK
        if pares:
            sig_r = max(abs(np.sqrt(complex(mm['omega2'])).imag)
                        for mm in pares) / Hs_t[p_anc]
            say(f"    ancora a={a_anc:6.0f}: sigma/H cong (red) = "
                f"{sig_r:5.2f}  negK={negK}")
        else:
            say(f"    ancora a={a_anc:6.0f}: QEP sem modos finitos "
                f"(pre-escalado)  negK={negK}")
    tf, tm, am_ = evolui(Kr, Cr, Wr, Krd, Crd, Ns_t, Hs_t, janelas)
    say("    taxas reais/H (norma total | norma METRICA), 6 ICs; "
        "k_phys/H nas bordas:")
    for nome, lo, hi in janelas:
        vf = [tx[nome] for tx in tf]
        vm = [tx[nome] for tx in tm]
        p_lo = int(np.argmin(np.abs(aas_t - lo)))
        p_hi = int(np.argmin(np.abs(aas_t - min(hi, a_max_val))))
        kh_lo = kc / (aas_t[p_lo] * Hs_t[p_lo])
        kh_hi = kc / (aas_t[p_hi] * Hs_t[p_hi])
        say(f"    {nome:<8}" + "".join(f"{v:+7.2f}" for v in vf)
            + "  |" + "".join(f"{v:+7.2f}" for v in vm)
            + f"   [{kh_lo:5.2f}->{kh_hi:5.2f}]")
    lnA = max(am_[i] for i in IDX_MET_IC)
    say(f"    lnA_met max = {lnA:.2f}")
    return dict(tf=tf, tm=tm, lnA=lnA, negK15=negK15, a_max=a_max_val)


def met_max(res, nome):
    fin = [res['tm'][i][nome] for i in IDX_MET_IC
           if np.isfinite(res['tm'][i][nome])]
    return max(fin) if fin else float('nan')


# ------------------------------------------------------------------
# R4a-NULL — GR + Lambda + chi espectador, cruzamento NA tardia
# ------------------------------------------------------------------
say("")
say("=" * 72)
say("R4a-NULL — controle GR na banda (portao de credibilidade)")
say("=" * 72)
Phi_gF = sp.Function('Phi_g')(t)
B_gF = sp.Function('B_g')(t)
dchiF = sp.Function('dchi')(t)
aF, bF, xiF, bg_rules = make_bg_functions()
g_gr = substitute_bg_functions(
    scalar_metric_g(Phi_gF, sp.Integer(0), B_gF, None), aF, bF, xiF)
L2_gr = z_average(eps_part(cut(lagrangian_GG(g_gr, Mg2)
                               + chi_lagrangian(g_gr, dchi=dchiF)), 2))
L2s_gr, f_gr, v_gr = symbolize(L2_gr, [Phi_gF, B_gF, dchiF], bg_rules)
Kg, Cg, Wg = quadratic_matrices(L2s_gr, f_gr, v_gr)
FIX_GR = {Mg2: 1, rho_s: 0}
LIV_GR = (a_s, H_s, Hd_s, chid_s, chidd_s, Ub, Up, Upp, ksym)
KgF = sp.lambdify(LIV_GR, Kg.subs(FIX_GR), 'numpy')
CgF = sp.lambdify(LIV_GR, Cg.subs(FIX_GR), 'numpy')
WgF = sp.lambdify(LIV_GR, Wg.subs(FIX_GR), 'numpy')


def builder_gr(kc_dummy_unused=None):
    def build(kc, npts):
        Ns = np.linspace(np.log(A_MIN), np.log(A_MAX_STD), npts)
        Hs_arr = np.zeros(npts)
        Ms = {x: np.zeros((npts, 3, 3)) for x in 'KCW'}
        for p, N in enumerate(Ns):
            a = np.exp(N)
            rho_d = RHO0 / a**3
            H = np.sqrt((LAM_GR + rho_d) / 3.0)
            Hs_arr[p] = H
            args = (a, H, -0.5 * rho_d, 0.0, 0.0,
                    LAM_GR + rho_d, 0.0, 0.3, kc)
            Ms['K'][p] = np.array(KgF(*args), float)
            Ms['C'][p] = np.array(CgF(*args), float)
            Ms['W'][p] = np.array(WgF(*args), float)
        return Ns, Hs_arr, Ms
    return build


ok_null = True
for kc in (12500.0, 1250.0):
    say("")
    say(f"--- GR-NULL: k_c={kc:g} (H=1.14; cruzamento em "
        f"a~{kc/1.14:.0f}) ---")
    Ns, Hs_arr, Ms = builder_gr()(kc, NPTS_STD)
    Kr, Cr, Wr, Krd, Crd, Ns_t, Hs_t = reduz_trilha(Ms, Ns, Hs_arr,
                                                    [0, 1], [2])
    tf, tm, _ = evolui(Kr, Cr, Wr, Krd, Crd, Ns_t, Hs_t, JAN_STD,
                       met_idx=None)
    aas_t = np.exp(Ns_t)
    for nome, lo, hi in JAN_STD:
        fin = [tx[nome] for tx in tf if np.isfinite(tx[nome])]
        vmax = max(fin) if fin else float('nan')
        p_lo = int(np.argmin(np.abs(aas_t - lo)))
        p_hi = int(np.argmin(np.abs(aas_t - hi)))
        kh_lo = kc / (aas_t[p_lo] * Hs_t[p_lo])
        kh_hi = kc / (aas_t[p_hi] * Hs_t[p_hi])
        say(f"    {nome:<8} taxa max = {vmax:+.2f}   "
            f"[k_phys/H {kh_lo:5.2f}->{kh_hi:5.2f}]")
        if np.isfinite(vmax) and vmax > 0.1:
            ok_null = False
say("")
say(f"  [R4a-NULL {'PASSA — banda nao e artefato do pipeline em GR'
    if ok_null else 'FALHA — NAO INTERPRETAR o mapa (artefato na banda)'}]")

# ------------------------------------------------------------------
# R4a-MAPA — beta1 x k nos fundos estaticos
# ------------------------------------------------------------------
say("")
say("=" * 72)
say("R4a-MAPA — beta1 x k (fundos beta-constantes estaticos)")
say("=" * 72)
MAPA = {}
for B1V in B1S:
    fchk = fundo_bconst(A_REF_BANDA, B1V)
    f100 = fundo_bconst(A_MIN, B1V)
    f20k = fundo_bconst(A_MAX_STD, B1V)
    if fchk is None or f100 is None or f20k is None:
        say(f"  beta1={B1V:g}: SEM ramo finito valido no range — pulado "
            "(achado por si: registrar)")
        continue
    k_banda = fchk['H'] * A_REF_BANDA
    say(f"  beta1={B1V:g}: r={fchk['r']:.4f} H={fchk['H']:.4f} "
        f"xi={fchk['xi']:.4f} -> k_banda={k_banda:.0f}")
    for tag, kc in (("banda", k_banda), ("3x", 3 * k_banda),
                    ("0.1x", 0.1 * k_banda)):
        res = roda(f"beta1={B1V:g}, k={tag}", builder_bconst(B1V, A_MAX_STD),
                   kc, NPTS_STD, JAN_STD, ANC_STD)
        MAPA[(B1V, tag)] = res

say("")
say("  SINTESE DO MAPA (taxa met max na tardia | lnA_met | negK@15000):")
say(f"    {'beta1':>6} {'banda':>16} {'3x':>16} {'0.1x':>16}")
for B1V in B1S:
    cols = []
    for tag in ("banda", "3x", "0.1x"):
        r = MAPA.get((B1V, tag))
        if r is None:
            cols.append(f"{'—':>16}")
        else:
            cols.append(f"{met_max(r, 'tardia'):+6.2f} {r['lnA']:5.1f} "
                        f"n{r['negK15']:d}")
    say(f"    {B1V:6.2f} " + " ".join(f"{c:>16}" for c in cols))

# ------------------------------------------------------------------
# R4a-EXT — transiente de cruzamento ou sustentada?
# ------------------------------------------------------------------
say("")
say("=" * 72)
say("R4a-EXT — a ate 80000: transiente de cruzamento ou sustentada?")
say("=" * 72)
say("[fundo POUSADO] reintegrando a trajetoria original ...")
BG_ORG = integra_alvo()
ok_org = (abs(BG_ORG['r'][-1] - 0.4979) < 0.005
          and abs(BG_ORG['ch'][-1] / BG_ORG['v'] - 0.932) < 0.005)
say(f"    r_fim={BG_ORG['r'][-1]:.4f}, "
    f"chi/v_fim={BG_ORG['ch'][-1]/BG_ORG['v']:.3f}  "
    f"[{'CONFERE' if ok_org else 'DIVERGE — nao interpretar EXT-pousado'}]")
CTX_ORG = make_ctx(BG_ORG, "ORG")

EXT = {}
EXT['bconst'] = roda("EXT beta-const 4.47", builder_bconst(4.47, A_MAX_EXT),
                     12500.0, NPTS_EXT, JAN_EXT, ANC_EXT)
EXT['pousado'] = roda("EXT pousado (ORG)", builder_rolagem(CTX_ORG,
                                                           A_MAX_EXT),
                      12500.0, NPTS_EXT, JAN_EXT, ANC_EXT)

# ------------------------------------------------------------------
# veredito
# ------------------------------------------------------------------
say("")
say("=" * 72)
say("VEREDITO R-4a (criterios pre-declarados no cabecalho)")
say("=" * 72)
say(f"  R4a-NULL: {'PASSA' if ok_null else 'FALHA — NAO INTERPRETAR'}")
if ok_null:
    say("")
    banda_t = {B1V: met_max(MAPA[(B1V, 'banda')], 'tardia')
               for B1V in B1S if (B1V, 'banda') in MAPA}
    inst = [B1V for B1V, v in banda_t.items()
            if np.isfinite(v) and v >= 0.5]
    say("  R4a-MAPA (banda): " + "  ".join(
        f"beta1={B1V:g}: {v:+.2f}" for B1V, v in banda_t.items()))
    if 1.0 in inst:
        say("    >>> beta1=1 CRESCE na banda: o fenomeno e da CLASSE")
        say("    INTEIRA beta-constante em k_phys~H tardio — o 'estavel")
        say("    tarde' de D2/R-1 era artefato de amostragem em k (nunca")
        say("    testaram a banda). Reavaliar enunciados: o setor escalar")
        say("    tardio tem instabilidade dinamica real em toda a classe;")
        say("    a gravidade depende do R4a-EXT abaixo.")
    elif inst:
        b1_star = min(inst)
        say(f"    >>> fronteira da regiao instavel: beta1* ~ {b1_star:g}")
        say("    (abaixo disso a banda dilui) — ESQUINA confirmada com")
        say("    limiar; o retangulo da R-1 (beta1<=2) fica "
            + ("parcialmente dentro" if b1_star <= 2.0 else "fora")
            + " da regiao.")
    else:
        say("    >>> NENHUM beta1 cresce na banda — contradicao com o")
        say("    R-3c G1 (+1.08 em 4.47): diagnosticar instrumento antes")
        say("    de qualquer enunciado (diferenca: k_banda vs k=12500?).")
    say("")
    for rot, res in EXT.items():
        t2 = met_max(res, 'tardia2')
        t1 = met_max(res, 'tardia')
        lab = ("SUSTENTADA" if (np.isfinite(t2) and t2 >= 0.5) else
               "TRANSIENTE-DE-CRUZAMENTO" if (np.isfinite(t2)
                                              and t2 <= 0.1) else
               "intermediario/indefinido")
        say(f"  R4a-EXT [{rot}]: tardia {t1:+.2f} -> tardia2 {t2:+.2f} "
            f"(a_max={res['a_max']:.0f})  => {lab}")
    say("")
    say("  (lnA_met por braco na sintese do mapa; anomalia IR do pousado")
    say("  segue declarada fora — sub-estrutura aberta.)")

os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
with open(os.path.join(HERE, "out", "r4a_mapa_tardio.txt"),
          "w", encoding="utf-8") as fh:
    fh.write("\n".join(OUT))
say("")
say("concluido. saida em auditoria/code/out/r4a_mapa_tardio.txt")
