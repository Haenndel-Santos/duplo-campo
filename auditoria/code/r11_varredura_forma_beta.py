# -*- coding: utf-8 -*-
"""
r11_varredura_forma_beta.py — o item n.1 da fila: existe FORMA-beta
com c_s^2 > 0 no regime r -> 0?

CONTEXTO: R-10 consolidado (docs/resultado_r10_consolidado.md). A
instabilidade de gradiente em r -> 0 nao e curada por: ramo infinito
(nao conecta), modulacao beta_1(phi_-) (chega tarde), nem screening
(delta_screen ~ 20-60; o lambda cancela). Resta varrer a FORMA do
potencial — o R-8b mostrou rigidez sob RESCALA uniforme (fold em
s ~ 5.7), mas a forma (as razoes entre beta_n) nunca foi varrida.

PISTA FORTE: no R-10a, c_s^2(r->0) deu -1.0103 (kh=30) e -1.2609
(kh=100) IDENTICOS para beta_1 = 1 e beta_1 = 4.47. Identidade a 5
casas entre dois fundos diferentes sugere CONSTANTE ESTRUTURAL, nao
dependencia de parametro. Se confirmado na varredura, o resultado
muda de natureza: deixa de ser "esta celula e instavel" e passa a ser
"a classe F1 (beta_3 = 0, materia so em g) e instavel em r -> 0",
que e um enunciado de classe — e o candidato a resultado central do
paper, com sinal negativo.

VARREDURA (F1: beta_3 = 0 por definicao da acao, cap. 03):
  beta_2 in {-2, -1, -0.4, -0.1}   (o benchmark tem -0.4)
  beta_4 in {0.1, 0.5, 2.0}        (benchmark 0.5)
  beta_0 in {0.5, 1.0, 2.0}        (benchmark 1.0)
  mu = M_f^2/M_g^2 in {0.3, 1.0, 3.0}  (benchmark 1.0)
  beta_1 = 1 fixo (o R-8b mostrou que a rescala uniforme e um dial
  degenerado; e a FORMA que interessa)
  => 108 celulas, cada uma avaliada em a = 0.01 (r ~ 1e-6, bem dentro
  do regime da instabilidade) com kh = 30.

MEDIDAS (pre-declaradas):
  F1-CS: c_s^2 do escalar metrico em r -> 0 por celula.
  F1-CAL: c_s^2 do espectador (tem que dar 1; celula com desvio >1%
    e descartada como nao-interpretavel).
  F1-VIAB: fundo valido (H^2 > 0, xi > 0) — celulas invalidas
    reportadas e puladas.

CRITERIOS (pre-declarados):
  Existe celula com c_s^2 > 0 e fundo viavel -> SAIDA ENCONTRADA:
    refazer a cascata nessa celula (a implementacao pode ser salva
    dentro do programa atual).
  Todas as celulas viaveis dao c_s^2 < 0, com dispersao pequena ->
    NO-GO DE CLASSE POR GRADIENTE: enunciado estrutural, o resultado
    central (negativo) da implementacao F1.
  Dispersao grande com todos negativos -> negativo, mas nao
    estrutural; reportar a dependencia.

Requer sympy, numpy. ~5-10 min.
Uso: python auditoria/code/r11_varredura_forma_beta.py
Saida em auditoria/code/out/r11_varredura_forma_beta.txt
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
                           quadratic_matrices, dt_background)

T0 = time.time()
OUT = []


def say(*a):
    line = " ".join(str(x) for x in a)
    print(f"[{time.time()-T0:7.1f}s] {line}")
    OUT.append(line)


MULT = [0, 1, 2, 4]
DYN = [3, 5, 6]
A_TESTE = 0.01
KH = 30.0
RHO0 = 0.3
B1V = 1.0
B2S = [-2.0, -1.0, -0.4, -0.1]
B4S = [0.1, 0.5, 2.0]
B0S = [0.5, 1.0, 2.0]
MUS = [0.3, 1.0, 3.0]

say("=" * 72)
say("R-11 — varredura de FORMA-beta: existe c_s^2 > 0 em r -> 0?")
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
    for n, bn in enumerate(BETAS):
        bsub = {bm: (1 if mm == n else 0) for mm, bm in enumerate(BETAS)}
        Sl = Msub.subs({Fb: 1, Fp: 0, Fpp: 0}).subs(bsub) - base_s
        out[('Fb', n)] = sp.lambdify(LIVRES, Sl, modules='numpy')
    return out


FK, FC, FW, FCd = fatias(K7), fatias(C7), fatias(W7), fatias(Cd7)
say("[fatias] prontas")


def monta(fat, args, bvals):
    M = np.array(fat['base'](*args), float).copy()
    for n in range(5):
        if bvals[n]:
            M += bvals[n] * np.array(fat[('Fb', n)](*args), float)
    return M


def fundo(a, B0V, B2V, B4V, mu):
    kap = 1.0 / mu
    meff2 = mu / (1.0 + mu)
    rho_til = (RHO0 * a**-3) / meff2
    rr = np.roots([kap * B4V - 3 * B2V, -3 * B1V,
                   3 * kap * B2V - B0V - rho_til, kap * B1V])
    reais = sorted(z.real for z in rr
                   if abs(z.imag) < 1e-9 and z.real > 1e-16)
    if not reais:
        return None
    r = reais[0]
    dW = kap * (2 * B4V * r - B1V / r**2) - 3 * B1V - 6 * B2V * r
    if abs(dW) < 1e-300:
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
    Hd = H2 * (0.5 * (2 / r + dVf / Vf) * drdN)
    xid = H * (drdN + d2rdN2)
    Hfd = (Hd - H2 * drdN / r) / r
    rho_int = meff2 * (B0V + 3 * B1V * r + 3 * B2V * r**2)
    return dict(r=r, xi=xi, H=H, Hf=H / r, Hd=Hd, Hfd=Hfd, xid=xid,
                Ub=3 * H2 - rho_int, meff2=meff2)


def fundo_ext(a, B0V, B2V, B4V, mu, h=1e-5):
    f = fundo(a, B0V, B2V, B4V, mu)
    if f is None:
        return None
    fp = fundo(a * np.exp(h), B0V, B2V, B4V, mu)
    fm = fundo(a * np.exp(-h), B0V, B2V, B4V, mu)
    if fp is None or fm is None:
        return None
    H = f['H']
    f['Hdd'] = H * (fp['Hd'] - fm['Hd']) / (2 * h)
    f['Hfdd'] = H * (fp['Hfd'] - fm['Hfd']) / (2 * h)
    f['xidd'] = H * (fp['xid'] - fm['xid']) / (2 * h)
    return f


def matriz_D(kc):
    return np.diag([1.0, 1.0 / kc, 1.0, 1.0, 1.0 / kc, 1.0 / kc**2, 1.0])


def cs2_celula(B0V, B2V, B4V, mu):
    f0 = fundo(A_TESTE, B0V, B2V, B4V, mu)
    if f0 is None:
        return None
    kc = KH * A_TESTE * f0['H']
    Ns = np.linspace(np.log(A_TESTE) - 0.02, np.log(A_TESTE) + 0.02, 41)
    Hs = np.zeros(41)
    Ms = {x: np.zeros((41, 7, 7)) for x in ('K', 'C', 'W', 'CdS')}
    D = matriz_D(kc)
    for p, N in enumerate(Ns):
        a = np.exp(N)
        f = fundo_ext(a, B0V, B2V, B4V, mu)
        if f is None:
            return None
        Hs[p] = f['H']
        args = (a, f['r'] * a, f['xi'], f['H'], f['Hf'], f['Hd'],
                f['Hfd'], f['xid'], 0.0, 0.0, f['Ub'], 0.0, 0.3,
                kc, mu, f['meff2'], f['Hdd'], f['Hfdd'], f['xidd'], 0.0)
        bvals = (B0V, B1V, B2V, 0.0, B4V)
        Ms['K'][p] = D @ monta(FK, args, bvals) @ D
        Ms['C'][p] = D @ monta(FC, args, bvals) @ D
        Ms['W'][p] = D @ monta(FW, args, bvals) @ D
        Ms['CdS'][p] = D @ monta(FCd, args, bvals) @ D
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
    K2 = np.zeros((41, 2, 2))
    C2 = np.zeros((41, 2, 2))
    W2 = np.zeros((41, 2, 2))
    for p in range(41):
        K, C, W = K3s[p].copy(), C3s[p].copy(), W3s[p].copy()
        for j in range(3):
            cij, cd = C3s[p][0, j], C3d[p][0, j]
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
        K2[p] = K[np.ix_(keep, keep)] + cx @ cx.T / W00
        C2[p] = C[np.ix_(keep, keep)] - cx @ W[np.ix_([0], keep)] / W00
        W2[p] = W[np.ix_(keep, keep)] - wx @ W[np.ix_([0], keep)] / W00
    C2d = np.gradient(C2, Ns, axis=0) * Hs[:, None, None]
    kf2 = (KH * Hs[20])**2
    return dict(
        cs2=(C2d[20, 0, 0] + W2[20, 0, 0]) / K2[20, 0, 0] / kf2,
        cal=(C2d[20, 1, 1] + W2[20, 1, 1]) / K2[20, 1, 1] / kf2,
        r=f0['r'], K2=K2[20, 0, 0])


say("")
say(f"    varrendo {len(B2S)*len(B4S)*len(B0S)*len(MUS)} celulas em "
    f"a = {A_TESTE} (kh = {KH:g}) ...")
say("")
say(f"    {'b0':>5} {'b2':>6} {'b4':>5} {'mu':>5} {'r':>10} "
    f"{'c_s^2':>10} {'calib':>8} {'K2>0':>5}")
positivas = []
negativas = []
invalidas = 0
nao_interp = 0
for B0V in B0S:
    for B2V in B2S:
        for B4V in B4S:
            for mu in MUS:
                r = cs2_celula(B0V, B2V, B4V, mu)
                if r is None:
                    invalidas += 1
                    continue
                if abs(r['cal'] - 1.0) > 0.01:
                    nao_interp += 1
                    continue
                mostrar = (mu == 1.0 and B0V == 1.0) or r['cs2'] > 0
                if mostrar:
                    say(f"    {B0V:5.1f} {B2V:6.1f} {B4V:5.1f} {mu:5.1f} "
                        f"{r['r']:10.2e} {r['cs2']:+10.5f} "
                        f"{r['cal']:8.5f} "
                        f"{'sim' if r['K2'] > 0 else 'NAO':>5}")
                if r['cs2'] > 0:
                    positivas.append((B0V, B2V, B4V, mu, r['cs2']))
                else:
                    negativas.append((B0V, B2V, B4V, mu, r['cs2']))

say("")
say("=" * 72)
say("VEREDITO R-11 (criterios pre-declarados no cabecalho)")
say("=" * 72)
tot = len(positivas) + len(negativas)
say(f"  celulas: {tot} interpretaveis; {invalidas} com fundo "
    f"invalido; {nao_interp} descartadas por calibracao.")
if positivas:
    say(f"  >>> SAIDA ENCONTRADA: {len(positivas)} celula(s) com "
        f"c_s^2 > 0 em r -> 0:")
    for c in positivas[:10]:
        say(f"      b0={c[0]}, b2={c[1]}, b4={c[2]}, mu={c[3]}: "
            f"c_s^2 = {c[4]:+.5f}")
    say("      -> refazer a cascata nessa(s) celula(s).")
else:
    vals = np.array([c[4] for c in negativas])
    say(f"  >>> NENHUMA SAIDA: {tot}/{tot} celulas interpretaveis dao")
    say(f"  c_s^2 < 0 em r -> 0.")
    say(f"      c_s^2: min = {vals.min():+.5f}, max = {vals.max():+.5f},")
    say(f"      mediana = {np.median(vals):+.5f}, "
        f"desvio-padrao = {vals.std():.2e}")
    if vals.std() < 1e-3:
        say("      DISPERSAO NULA (< 1e-3) sobre 4 parametros de forma")
        say("      => c_s^2(r->0) e CONSTANTE ESTRUTURAL da classe F1,")
        say("      nao funcao dos beta_n. Isto e um NO-GO DE CLASSE")
        say("      POR GRADIENTE: nenhuma escolha de forma-beta (com")
        say("      beta_3 = 0 e materia so em g) evita a instabilidade")
        say("      no regime r -> 0. Candidato a resultado central")
        say("      (negativo) da implementacao F1 — e enunciavel como")
        say("      teorema a ser provado analiticamente.")
    else:
        say("      dispersao nao-nula: negativo em toda a varredura,")
        say("      mas dependente de forma — reportar a dependencia.")

os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
with open(os.path.join(HERE, 'out', 'r11_varredura_forma_beta.txt'),
          'w', encoding='utf-8') as fh:
    fh.write("\n".join(OUT) + "\n")
say("")
say("saida escrita em auditoria/code/out/r11_varredura_forma_beta.txt")
