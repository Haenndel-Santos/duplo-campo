# -*- coding: utf-8 -*-
"""
r10c_saidas_ramo_e_dinamico.py — BLOCO 1: as duas saidas baratas da
instabilidade de gradiente (R-10a/R-10b).

PARTE A — A EXCLUSAO DO RAMO INFINITO ESTA CERTA?
  O repositorio descartou o ramo infinito (r ~ sqrt(rho_til) -> inf)
  porque "da xi < 0, isto e, lapso negativo no setor f"
  (docs/resultado_ramo_finito.md §2). Mas e o ramo que
  Konnig-Akrami-Amendola-Motta-Solomon (1407.4331) PROMOVEM como o
  cosmologicamente viavel. Como a nossa exclusao foi feita antes do
  Erratum-01/02 e nunca reauditada, este teste reexamina:
    A1: para cada raiz real positiva da cubica, calcular
        dr/dN = -3 rho_til / W'(r) e xi = r + dr/dN, e o sinal de xi;
    A2: onde xi > 0, calcular H^2 e verificar positividade;
    A3: se algum ramo alternativo for viavel, medir c_s^2 nele.
  Criterio: se TODAS as raizes alem da menor derem xi <= 0 ou H^2 <=
  0 em toda a historia, a exclusao esta CONFIRMADA e a discrepancia
  com a literatura e de parametrizacao (nao temos o mesmo ramo que
  eles chamam de infinito). Se alguma der xi > 0 e H^2 > 0, a
  exclusao CAI e ha um ramo nao explorado.

PARTE B — A INSTABILIDADE SOBREVIVE NO FUNDO DINAMICO?
  O R-10a/b mediram no benchmark beta-CONSTANTE. A TDCP propriamente
  dita tem beta_1(phi_-) e o fundo pousado, onde a condensacao leva
  r de 0.031 a 0.498 rapidamente. Se a condensacao atravessa a regiao
  instavel (r <~ 0.09) depressa, a era instavel pode ser curta demais
  para importar. Mede-se c_s^2(a) ao longo do fundo pousado (Heun),
  com as fatias moduladas (bp, bpp), e o crescimento acumulado.
  Criterio: lnA_total < 11.5 no fundo dinamico -> a modulacao SALVA
  a implementacao (achado positivo forte: seria a primeira vez que a
  modulacao beta_1(phi_-) faz diferenca fisica favoravel).
  lnA_total > 11.5 -> a instabilidade sobrevive a modulacao.

FRONTEIRA: uma trajetoria (celula REF), sem radiacao, kh = 30.

Requer sympy, numpy, scipy. ~4-8 min.
Uso: python auditoria/code/r10c_saidas_ramo_e_dinamico.py
Saida em auditoria/code/out/r10c_saidas_ramo_e_dinamico.txt
"""
import importlib.util
import os
import sys
import time

import numpy as np
import sympy as sp
from scipy.optimize import brentq

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
                           quadratic_matrices, dt_background)

T0 = time.time()
OUT = []


def say(*a):
    line = " ".join(str(x) for x in a)
    print(f"[{time.time()-T0:7.1f}s] {line}")
    OUT.append(line)


MULT = [0, 1, 2, 4]
DYN = [3, 5, 6]
MU = 1.0
MG2V, MF2V = 1.0, 1.0
ME2 = 0.5
M2 = 1.0
B0V, B2V, B4V = 1.0, -0.4, 0.5
B10 = 1.0
RHO0 = 0.3
VST = 1.0
KH = 30.0
LN_NL = np.log(1e5)

say("=" * 72)
say("R-10c — as duas saidas: ramo infinito e fundo dinamico")
say("=" * 72)

# ------------------------------------------------------------------
# PARTE A — todas as raizes da cubica
# ------------------------------------------------------------------
say("")
say("=" * 72)
say("PARTE A — a exclusao do ramo infinito esta certa?")
say("=" * 72)


def raizes_todas(a, B1V):
    kap = 1.0 / MU
    meff2 = ME2
    rho_til = (RHO0 * a**-3) / meff2
    coef = [kap * B4V - 3 * B2V, -3 * B1V,
            3 * kap * B2V - B0V - rho_til, kap * B1V]
    rr = np.roots(coef)
    out = []
    for z in rr:
        if abs(z.imag) > 1e-9 or z.real <= 1e-14:
            continue
        r = float(z.real)
        dW = kap * (2 * B4V * r - B1V / r**2) - 3 * B1V - 6 * B2V * r
        if abs(dW) < 1e-300:
            continue
        drdN = -3 * rho_til / dW
        xi = r + drdN
        Vf = B4V + 3 * B2V / r**2 + B1V / r**3
        H2 = meff2 * r * r * Vf / (3.0 * MU)
        out.append(dict(r=r, drdN=drdN, xi=xi, H2=H2, Vf=Vf))
    return sorted(out, key=lambda d: d['r'])


for B1V in (1.0, 4.47):
    say("")
    say(f"  beta1 = {B1V:g}:")
    say(f"    {'a':>8} {'raiz':>3} {'r':>11} {'dr/dN':>11} {'xi':>11} "
        f"{'H^2':>11} {'viavel?':>8}")
    viaveis_alt = 0
    for a0 in (1e-3, 1e-2, 0.1, 1.0, 10.0, 1e3):
        rs = raizes_todas(a0, B1V)
        for i, d in enumerate(rs):
            ok = (d['xi'] > 0) and (d['H2'] > 0)
            if i > 0 and ok:
                viaveis_alt += 1
            say(f"    {a0:8.3g} {i:3d} {d['r']:11.4e} {d['drdN']:+11.3e} "
                f"{d['xi']:+11.3e} {d['H2']:+11.3e} "
                f"{'SIM' if ok else 'nao':>8}")
    say("")
    if viaveis_alt == 0:
        say(f"    [A-RAMO] exclusao CONFIRMADA para beta1={B1V:g}: "
            f"nenhuma raiz alem da menor tem xi > 0 e H^2 > 0.")
    else:
        say(f"    [A-RAMO] EXCLUSAO CAI: {viaveis_alt} ponto(s) com "
            f"raiz alternativa viavel — ha ramo nao explorado.")

# ------------------------------------------------------------------
# PARTE B — fundo dinamico
# ------------------------------------------------------------------
say("")
say("=" * 72)
say("PARTE B — a instabilidade sobrevive ao fundo dinamico?")
say("=" * 72)

L2s, fields, vels = d1.build_L2()
K7, C7, W7 = quadratic_matrices(L2s, fields, vels)
Hdd_s, Hfdd_s, xidd_s, chiddd_s = sp.symbols(
    'Hddot H_fddot xiddot chidddot')
Cd7 = sp.zeros(7, 7)
for i in range(7):
    for j in range(7):
        Cd7[i, j] = dt_background(
            C7[i, j], {Hd_s: Hdd_s, Hfd_s: Hfdd_s, xid_s: xidd_s,
                       chidd_s: chiddd_s})
LIVRES = (a_s, b_s, xi_s, H_s, Hf_s, Hd_s, Hfd_s, xid_s,
          chid_s, chidd_s, Ub, Up, Upp, ksym, Mf2, Meff2,
          Hdd_s, Hfdd_s, xidd_s, chiddd_s)
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


FK, FC, FW, FCd = fatias(K7), fatias(C7), fatias(W7), fatias(Cd7)
say("[fatias moduladas] prontas")


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


def beta1f(ch):
    return B10 * (1.0 + ch * ch / (VST * VST))


def dbeta1f(ch):
    return 2.0 * B10 * ch / (VST * VST)


def U_pot(ch, mu2, lam, U0):
    return -0.5 * mu2 * ch * ch + 0.25 * lam * ch**4 + U0


def dU_pot(ch, mu2, lam):
    return -mu2 * ch + lam * ch**3


def Hf2_of(r, ch):
    Vf = beta1f(ch) + 3 * r * B2V + r**3 * B4V
    return M2 * ME2 * Vf / (3 * MF2V * r**3)


def H_de(r, ch, chd, a, mu2, lam, U0):
    Vg = B0V + 3 * r * beta1f(ch) + 3 * r * r * B2V
    resto = (0.5 * chd * chd + U_pot(ch, mu2, lam, U0) + RHO0 / a**3
             + M2 * ME2 * Vg)
    return np.sqrt(resto / (3 * MG2V)) if resto > 0 else None


def raiz_cub(a, ch, chd, mu2, lam, U0, seed=None):
    b1v = beta1f(ch)
    rho_tot = 0.5 * chd * chd + U_pot(ch, mu2, lam, U0) + RHO0 / a**3
    rt = rho_tot / (M2 * ME2)
    kap = MG2V / MF2V
    rr = np.roots([kap * B4V - 3 * B2V, -3 * b1v,
                   3 * kap * B2V - B0V - rt, kap * b1v])
    reais = sorted(x.real for x in rr
                   if abs(x.imag) < 1e-9 and x.real > 1e-12)
    if not reais:
        return None
    if seed is None:
        return reais[0]
    return min(reais, key=lambda x: abs(x - seed))


def integra_fundo(g_end=2.0, mchi2=30.0, a0=0.01, a1=1e5, dN=1e-3):
    v = g_end * VST
    mu2 = 0.5 * mchi2
    lam = mu2 / (v * v)
    U0 = 0.25 * mu2 * v * v
    N0, N1 = np.log(a0), np.log(a1)
    n = int((N1 - N0) / dN) + 1
    ch, chd = 1e-3 * v, 0.0
    r = raiz_cub(a0, ch, chd, mu2, lam, U0)
    rp = 0.0
    rec = {kk: [] for kk in ('N', 'a', 'r', 'xi', 'H', 'Hf', 'ch',
                             'chd', 'chidd')}

    def rhs(N, ch, chd, rseed, rp):
        a = np.exp(N)
        r_ = raiz_cub(a, ch, chd, mu2, lam, U0, rseed)
        H = H_de(r_, ch, chd, a, mu2, lam, U0)
        Hf = np.sqrt(Hf2_of(r_, ch))
        xi = H * (1.0 + rp / r_) / Hf
        chidd = (-3 * H * chd - dU_pot(ch, mu2, lam)
                 - M2 * ME2 * dbeta1f(ch) * (xi + 3 * r_))
        return chd / H, chidd / H, r_, H, Hf, xi, chidd

    for i in range(n):
        N = N0 + i * dN
        d1c, d1d, r1, H1, Hf1, xi1, cdd = rhs(N, ch, chd, r, rp)
        chp, chdp = ch + dN * d1c, chd + dN * d1d
        d2c, d2d, r2, _, _, _, _ = rhs(N + dN, chp, chdp, r1,
                                       (r1 - r) / dN if i else rp)
        for kk, vv in (('N', N), ('a', np.exp(N)), ('r', r1),
                       ('xi', xi1), ('H', H1), ('Hf', Hf1), ('ch', ch),
                       ('chd', chd), ('chidd', cdd)):
            rec[kk].append(vv)
        ch += 0.5 * dN * (d1c + d2c)
        chd += 0.5 * dN * (d1d + d2d)
        rp = (r2 - r1) / dN
        r = r1
    return {kk: np.array(vv) for kk, vv in rec.items()}, v, mu2, lam, U0


say("[fundo dinamico] integrando ...")
BG, vv, mu2, lam, U0 = integra_fundo()
say(f"    r: {BG['r'][0]:.4f} -> {BG['r'][-1]:.4f}; "
    f"chi/v final = {BG['ch'][-1]/vv:.4f}")

from scipy.interpolate import CubicSpline
SPL = {kk: CubicSpline(BG['N'], BG[kk])
       for kk in ('r', 'xi', 'H', 'Hf', 'ch', 'chd', 'chidd')}
DSPL = {kk: SPL[kk].derivative() for kk in SPL}


def bg_pt(N):
    H = float(SPL['H'](N))
    ch = float(SPL['ch'](N))
    r = float(SPL['r'](N))
    Hf = float(SPL['Hf'](N))
    a = np.exp(N)
    xi_c = H * (1.0 + float(DSPL['r'](N)) / r) / Hf
    return dict(a=a, r=r, xi=xi_c, H=H, Hf=Hf, ch=ch,
                chd=float(SPL['chd'](N)),
                chidd=H * float(DSPL['chd'](N)),
                Hd=H * float(DSPL['H'](N)),
                Hfd=H * float(DSPL['Hf'](N)),
                chiddd=H * float(DSPL['chidd'](N)),
                Ubv=U_pot(ch, mu2, lam, U0) + RHO0 / a**3,
                Upv=dU_pot(ch, mu2, lam),
                Uppv=-mu2 + 3 * lam * ch * ch)


def bg_ext(N, h=1e-4):
    f = bg_pt(N)
    fp, fm = bg_pt(N + h), bg_pt(N - h)
    H = f['H']
    xl = (fp['xi'] - fm['xi']) / (2 * h)
    xll = (fp['xi'] - 2 * f['xi'] + fm['xi']) / h**2
    f['xid'] = H * xl
    f['xidd'] = f['Hd'] * xl + H * H * xll
    f['Hdd'] = H * (fp['Hd'] - fm['Hd']) / (2 * h)
    f['Hfdd'] = H * (fp['Hfd'] - fm['Hfd']) / (2 * h)
    return f


def matriz_D(kc):
    return np.diag([1.0, 1.0 / kc, 1.0, 1.0, 1.0 / kc, 1.0 / kc**2, 1.0])


def reduz_pt(N0, kh):
    f0 = bg_pt(N0)
    kc = kh * f0['a'] * f0['H']
    Ns = np.linspace(N0 - 0.02, N0 + 0.02, 41)
    Hs = np.zeros(41)
    Ms = {x: np.zeros((41, 7, 7)) for x in ('K', 'C', 'W', 'CdS')}
    D = matriz_D(kc)
    for p, N in enumerate(Ns):
        f = bg_ext(N)
        Hs[p] = f['H']
        args = (f['a'], f['r'] * f['a'], f['xi'], f['H'], f['Hf'],
                f['Hd'], f['Hfd'], f['xid'], f['chd'], f['chidd'],
                f['Ubv'], f['Upv'], f['Uppv'], kc, MF2V, ME2,
                f['Hdd'], f['Hfdd'], f['xidd'], f['chiddd'])
        bvals = (B0V, beta1f(f['ch']), B2V, 0.0, B4V)
        bp = (0.0, dbeta1f(f['ch']), 0.0, 0.0, 0.0)
        bpp = (0.0, 2.0 * B10 / VST**2, 0.0, 0.0, 0.0)
        Ms['K'][p] = D @ monta(FK, args, bvals, bp, bpp) @ D
        Ms['C'][p] = D @ monta(FC, args, bvals, bp, bpp) @ D
        Ms['W'][p] = D @ monta(FW, args, bvals, bp, bpp) @ D
        Ms['CdS'][p] = D @ monta(FCd, args, bvals, bp, bpp) @ D
    K3s = np.zeros((41, 3, 3))
    C3s = np.zeros((41, 3, 3))
    W3s = np.zeros((41, 3, 3))
    mset = set(MULT)
    try:
        for p in range(41):
            K, C, W = (Ms['K'][p].copy(), Ms['C'][p].copy(),
                       Ms['W'][p].copy())
            Cd = Ms['CdS'][p]
            for i in MULT:
                for j in range(7):
                    cd, cij = Cd[i, j], Ms['C'][p][i, j]
                    if i == j:
                        W[i, i] += cd
                    elif j in mset:
                        W[i, j] += cd
                    else:
                        W[i, j] += cd
                        W[j, i] += cd
                        C[j, i] -= cij
                C[i, :] = 0.0
            WXX = 0.5 * (W[np.ix_(MULT, MULT)] + W[np.ix_(MULT, MULT)].T)
            WXXi = np.linalg.inv(WXX)
            CdX = C[np.ix_(DYN, MULT)]
            K3 = K[np.ix_(DYN, DYN)] + CdX @ WXXi @ CdX.T
            C3 = C[np.ix_(DYN, DYN)] - CdX @ WXXi @ W[np.ix_(MULT, DYN)]
            W3 = W[np.ix_(DYN, DYN)] - W[np.ix_(DYN, MULT)] @ WXXi \
                @ W[np.ix_(MULT, DYN)]
            K3[0, :] = 0.0
            K3[:, 0] = 0.0
            K3s[p], C3s[p], W3s[p] = K3, C3, W3
    except np.linalg.LinAlgError:
        return None
    C3d = np.gradient(C3s, Ns, axis=0) * Hs[:, None, None]
    K2s = np.zeros((41, 2, 2))
    C2s = np.zeros((41, 2, 2))
    W2s = np.zeros((41, 2, 2))
    for p in range(41):
        K3, C3, W3, C3dp = K3s[p], C3s[p], W3s[p], C3d[p]
        K, C, W = K3.copy(), C3.copy(), W3.copy()
        for j in range(3):
            cij, cd = C3[0, j], C3dp[0, j]
            if j == 0:
                W[0, 0] += cd
            else:
                W[0, j] += cd
                W[j, 0] += cd
                C[j, 0] -= cij
        C[0, :] = 0.0
        W00 = W[0, 0]
        keep = [1, 2]
        cx = C[np.ix_(keep, [0])]
        wx = W[np.ix_(keep, [0])]
        K2s[p] = K[np.ix_(keep, keep)] + cx @ cx.T / W00
        C2s[p] = C[np.ix_(keep, keep)] - cx @ W[np.ix_([0], keep)] / W00
        W2s[p] = W[np.ix_(keep, keep)] - wx @ W[np.ix_([0], keep)] / W00
    C2d = np.gradient(C2s, Ns, axis=0) * Hs[:, None, None]
    kf2 = (kh * Hs[20])**2
    return dict(cs2=(C2d[20, 0, 0] + W2s[20, 0, 0]) / K2s[20, 0, 0] / kf2,
                cal=(C2d[20, 1, 1] + W2s[20, 1, 1]) / K2s[20, 1, 1] / kf2,
                K2=K2s[20, 0, 0], H=Hs[20])


say("")
say(f"    c_s^2 ao longo do fundo dinamico (kh = {KH:g}):")
say(f"    {'a':>9} {'r':>8} {'chi/v':>7} {'c_s^2':>9} {'calib':>8} "
    f"{'K2>0':>6}")
Ns_amostra = np.linspace(BG['N'][3], BG['N'][-4], 22)
perfil = []
for N0 in Ns_amostra:
    rr = reduz_pt(N0, KH)
    if rr is None:
        continue
    f = bg_pt(N0)
    perfil.append((N0, rr['cs2'], f['H']))
    say(f"    {np.exp(N0):9.3g} {f['r']:8.4f} {f['ch']/vv:7.4f} "
        f"{rr['cs2']:+9.4f} {rr['cal']:8.5f} "
        f"{'sim' if rr['K2'] > 0 else 'NAO':>6}")

Nsp = np.array([p[0] for p in perfil])
csp = np.array([p[1] for p in perfil])
neg = csp < 0
say("")
if not neg.any():
    say("    [B-DIN] c_s^2 > 0 em TODA a trajetoria dinamica —")
    say("    a modulacao beta_1(phi_-) SALVA a implementacao:")
    say("    a condensacao tira o fundo da regiao instavel antes")
    say("    que ela importe. ACHADO POSITIVO FORTE.")
else:
    N_ini, N_fim = Nsp[neg][0], Nsp[neg][-1]
    lnA = float(np.trapezoid(
        np.sqrt(np.abs(np.minimum(csp[neg], 0.0))) * KH, Nsp[neg]))
    say(f"    [B-DIN] c_s^2 < 0 em {neg.sum()}/{len(csp)} amostras, de")
    say(f"    a = {np.exp(N_ini):.3g} a a = {np.exp(N_fim):.3g} "
        f"({N_fim - N_ini:.2f} e-folds).")
    say(f"    crescimento acumulado do modo kh={KH:g}: lnA = {lnA:.1f} "
        f"({'SAI do linear' if lnA > LN_NL else 'fica linear'}; "
        f"criterio {LN_NL:.1f})")
    if lnA > LN_NL:
        say("    >>> a instabilidade SOBREVIVE a modulacao: o fundo")
        say("    dinamico da TDCP tambem atravessa a regiao instavel")
        say("    por tempo suficiente.")
    else:
        say("    >>> a modulacao ATENUA: a era instavel existe mas e")
        say("    curta demais para tirar o modo do regime linear.")

os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
with open(os.path.join(HERE, 'out', 'r10c_saidas_ramo_e_dinamico.txt'),
          'w', encoding='utf-8') as fh:
    fh.write("\n".join(OUT) + "\n")
say("")
say("saida escrita em auditoria/code/out/r10c_saidas_ramo_e_dinamico.txt")
