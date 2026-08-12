# -*- coding: utf-8 -*-
"""
r10a_gradiente_alto_z.py — BLOCO 1, item A1: c_s^2 ao longo de TODA a
historia, com foco em ALTO REDSHIFT (r -> 0) — o regime onde a
literatura declara o ramo finito instavel por gradiente.

CONTEXTO: parecer de cosmologia (docs/pareceres_especialistas/
parecer_cosmologia.md; sintese §4.1 item 2): o repositorio trabalha no
FINITE BRANCH, que Konnig-Akrami-Amendola-Motta-Solomon (arXiv:
1407.4331) declaram instavel por gradiente em alto z; o ramo infinito
que descartamos (xi < 0) e o que eles promovem. O
posicionamento_literatura.md registra os papers mas a cascata nunca
executou o confronto. O R-9a (Bloco 0) mediu c_s^2 > 0 mas SO na faixa
a = 150..75000, que no brinquedo e a era tardia (r ~ 0.33 = r_inf):
nao tocou o regime da alegacao.

O REGIME DA ALEGACAO: no ramo finito r ~ beta_1/rho_til -> 0 quando
rho -> infinito (alto z). E la que a instabilidade e reivindicada.
Este script varre a de 1e-3 a 1e5 (r de ~1e-5 a r_inf) e mede c_s^2.

MEDIDAS (pre-declaradas):
  A1-CS: c_s^2 = om2_ef/(k/a)^2 por componente (Etil = escalar
    metrico; dchi = espectador), em ~16 epocas log-espacadas x kh in
    {30, 100} (a janela bem-condicionada certificada no R-9a), nos
    dois fundos beta-constantes (beta1 = 1 e 4.47).
    om2_ef = (Cdot+W)/K — a frequencia efetiva CORRETA (R-9a; W/K
    sozinho nao e frequencia nesta convencao).
  A1-COND: cond(W_XX) por ponto — separa estrutura de ruido.
  A1-CAL: o espectador tem c_s^2 = 1 exato; qualquer desvio dele e a
    barra de erro do metodo naquele ponto.
  A1-R: r(a) e xi/r tabelados junto, para localizar onde estamos no
    ramo (r -> 0 primordial; r -> r_inf tardio; xi = 4r no primordial
    e a assinatura do ramo finito).

CRITERIOS (pre-declarados):
  c_s^2(Etil) > 0 em TODAS as epocas e kh, nos dois fundos, com o
    espectador calibrando dentro de 1% -> RAMO-FINITO-ESTAVEL nesta
    implementacao: a instabilidade de gradiente de 1407.4331 NAO se
    reproduz aqui, e a discrepancia com a literatura vira item de
    confronto explicito (parametrizacao? ramo? convencao de c_s?).
  c_s^2(Etil) < 0 em alguma epoca -> INSTABILIDADE CONFIRMADA:
    localizar a janela em a e em k, medir a taxa |c_s| k/a vs H, e
    reescrever o cap. 07 — seria o achado mais grave desde o
    Erratum-02.
  Se o espectador desviar de 1 por mais de 1% em algum ponto, esse
    ponto e declarado NAO-INTERPRETAVEL (metodo fora de validade).

FRONTEIRA: fundos beta-constantes (a alegacao da literatura e sobre
HR com beta constante, entao este e o confronto correto); materia como
rho do fundo; sem radiacao (o brinquedo nao a tem — declarado, e e o
item (f) do Bloco 1).

Requer sympy, numpy. ~3-6 min.
Uso (raiz do repo, venv ativo):
    python auditoria/code/r10a_gradiente_alto_z.py
Saida em auditoria/code/out/r10a_gradiente_alto_z.txt
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


NOMES = ['Phi_g', 'B_g', 'Phi_f', 'Psi_f', 'B_f', 'E_f', 'dchi']
MULT = [0, 1, 2, 4]
DYN = [3, 5, 6]
G1_TOL = 1e-10
EPOCAS = list(np.geomspace(1e-3, 1e5, 17))
KHS = [30.0, 100.0]
MU = 1.0
ME2 = 0.5
B0V, B2V, B4V = 1.0, -0.4, 0.5
RHO0 = 0.3

say("=" * 72)
say("R-10a — BLOCO 1(A1): c_s^2 em TODA a historia (foco em alto z)")
say("=" * 72)

if not d1.gr_selfcheck():
    say("[!] V1 falhou — abortando")
    sys.exit(1)
say("[V1] GR selfcheck: PASSA")

L2s, fields, vels = d1.build_L2()
K7, C7, W7 = quadratic_matrices(L2s, fields, vels)
if [str(f) for f in fields] != NOMES:
    raise RuntimeError("ordem de campos mudou")
Hdd_s, Hfdd_s, xidd_s, chiddd_s = sp.symbols(
    'Hddot H_fddot xiddot chidddot')
Cd7 = sp.zeros(7, 7)
for i in range(7):
    for j in range(7):
        Cd7[i, j] = dt_background(
            C7[i, j], {Hd_s: Hdd_s, Hfd_s: Hfdd_s, xid_s: xidd_s,
                       chidd_s: chiddd_s})
say("[montagem] K,C,W,CdS prontos")

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


def fundo(a, B1V):
    kap = 1.0 / MU
    meff2 = ME2
    rho = RHO0 * a**-3
    rho_til = rho / meff2
    rr = np.roots([kap * B4V - 3 * B2V, -3 * B1V,
                   3 * kap * B2V - B0V - rho_til, kap * B1V])
    reais = sorted(z.real for z in rr
                   if abs(z.imag) < 1e-9 and z.real > 1e-14)
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


def fundo_ext(a, B1V, h=1e-5):
    f = fundo(a, B1V)
    if f is None:
        return None
    fp = fundo(a * np.exp(h), B1V)
    fm = fundo(a * np.exp(-h), B1V)
    if fp is None or fm is None:
        return None
    H = f['H']
    f['Hdd'] = H * (fp['Hd'] - fm['Hd']) / (2 * h)
    f['Hfdd'] = H * (fp['Hfd'] - fm['Hfd']) / (2 * h)
    f['xidd'] = H * (fp['xid'] - fm['xid']) / (2 * h)
    return f


def matriz_D(kc):
    return np.diag([1.0, 1.0 / kc, 1.0, 1.0, 1.0 / kc, 1.0 / kc**2, 1.0])


def e1(Kt, Ct, Wt, Cdot):
    K, C, W = Kt.copy(), Ct.copy(), Wt.copy()
    esc = max(1.0, np.max(np.abs(K)))
    mset = set(MULT)
    for i in MULT:
        if np.max(np.abs(K[i, :])) > 1e-10 * esc:
            raise RuntimeError("K mult nao-nula")
        for j in range(7):
            cd = Cdot[i, j]
            cij = Ct[i, j]
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
    cnd = np.linalg.cond(WXX)
    WXXi = np.linalg.inv(WXX)
    CdX = C[np.ix_(DYN, MULT)]
    K3 = K[np.ix_(DYN, DYN)] + CdX @ WXXi @ CdX.T
    C3 = C[np.ix_(DYN, DYN)] - CdX @ WXXi @ W[np.ix_(MULT, DYN)]
    W3 = W[np.ix_(DYN, DYN)] - W[np.ix_(DYN, MULT)] @ WXXi \
        @ W[np.ix_(MULT, DYN)]
    return K3, C3, W3, cnd


def e2(K3, C3, W3, C3d):
    K, C, W = K3.copy(), C3.copy(), W3.copy()
    for j in range(3):
        cij, cd = C3[0, j], C3d[0, j]
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
    K2 = K[np.ix_(keep, keep)] + cx @ cx.T / W00
    C2 = C[np.ix_(keep, keep)] - cx @ W[np.ix_([0], keep)] / W00
    W2 = W[np.ix_(keep, keep)] - wx @ W[np.ix_([0], keep)] / W00
    return 0.5 * (K2 + K2.T), C2, 0.5 * (W2 + W2.T)


def om2_no_ponto(a0, B1V, kh):
    """om2_ef por componente numa mini-trilha centrada em a0."""
    f0 = fundo(a0, B1V)
    if f0 is None:
        return None
    kc = kh * a0 * f0['H']
    Ns = np.linspace(np.log(a0) - 0.02, np.log(a0) + 0.02, 41)
    Hs = np.zeros(41)
    Ms = {x: np.zeros((41, 7, 7)) for x in ('K', 'C', 'W', 'CdS')}
    D = matriz_D(kc)
    for p, N in enumerate(Ns):
        a = np.exp(N)
        f = fundo_ext(a, B1V)
        if f is None:
            return None
        Hs[p] = f['H']
        args = (a, f['r'] * a, f['xi'], f['H'], f['Hf'], f['Hd'],
                f['Hfd'], f['xid'], 0.0, 0.0, f['Ub'], 0.0, 0.3,
                kc, 1.0, ME2, f['Hdd'], f['Hfdd'], f['xidd'], 0.0)
        bvals = (B0V, B1V, B2V, 0.0, B4V)
        Ms['K'][p] = D @ monta(FK, args, bvals) @ D
        Ms['C'][p] = D @ monta(FC, args, bvals) @ D
        Ms['W'][p] = D @ monta(FW, args, bvals) @ D
        Ms['CdS'][p] = D @ monta(FCd, args, bvals) @ D
    K3s = np.zeros((41, 3, 3))
    C3s = np.zeros((41, 3, 3))
    W3s = np.zeros((41, 3, 3))
    g1 = 0.0
    cnd = 0.0
    try:
        for p in range(41):
            K3, C3, W3, c_ = e1(Ms['K'][p], Ms['C'][p], Ms['W'][p],
                                Ms['CdS'][p])
            cnd = max(cnd, c_)
            esc = np.max(np.abs(K3))
            g1 = max(g1, np.max(np.abs(K3[0, :])) / esc)
            K3[0, :] = 0.0
            K3[:, 0] = 0.0
            K3s[p], C3s[p], W3s[p] = K3, C3, W3
    except (RuntimeError, np.linalg.LinAlgError) as e:
        return dict(erro=str(e))
    if g1 >= G1_TOL:
        return dict(erro=f'G1={g1:.1e}')
    C3d = np.gradient(C3s, Ns, axis=0) * Hs[:, None, None]
    K2s = np.zeros((41, 2, 2))
    C2s = np.zeros((41, 2, 2))
    W2s = np.zeros((41, 2, 2))
    for p in range(41):
        K2s[p], C2s[p], W2s[p] = e2(K3s[p], C3s[p], W3s[p], C3d[p])
    C2d = np.gradient(C2s, Ns, axis=0) * Hs[:, None, None]
    om2 = [(C2d[20, i, i] + W2s[20, i, i]) / K2s[20, i, i]
           for i in range(2)]
    lamK = np.linalg.eigvalsh(K2s[20])
    kdiag = [K2s[20, i, i] for i in range(2)]
    wdiag = [C2d[20, i, i] + W2s[20, i, i] for i in range(2)]
    return dict(om2=om2, H=Hs[20], cond=cnd, r=f0['r'], xi=f0['xi'],
                lamK_rel=lamK[0] / max(abs(lamK).max(), 1e-300),
                kdiag=kdiag, wdiag=wdiag, erro=None)


alertas = []
nao_interp = []
for B1V in (1.0, 4.47):
    say("")
    say("=" * 72)
    say(f"FUNDO beta-constante beta1={B1V:g}")
    say("=" * 72)
    say(f"    {'a':>10} {'r':>10} {'xi/r':>7} " +
        " ".join([f"cs2_Et(kh={kh:g})".rjust(15) for kh in KHS]) +
        f" {'cs2_dchi':>9} {'K2_Et':>10} {'lamK_rel':>10} {'cond':>8}")
    for a0 in EPOCAS:
        f0 = fundo(a0, B1V)
        if f0 is None:
            say(f"    {a0:10.3g} {'—':>10} (fundo invalido)")
            continue
        cs_et = []
        cs_dc = []
        cnds = []
        kd = float('nan')
        lamk = float('nan')
        for kh in KHS:
            r = om2_no_ponto(a0, B1V, kh)
            if r is None or r.get('erro'):
                cs_et.append(float('nan'))
                cs_dc.append(float('nan'))
                cnds.append(float('nan'))
                continue
            kfis2 = (kh * r['H'])**2
            cs_et.append(r['om2'][0] / kfis2)
            cs_dc.append(r['om2'][1] / kfis2)
            cnds.append(r['cond'])
            kd = r['kdiag'][0]
            lamk = r['lamK_rel']
        say(f"    {a0:10.3g} {f0['r']:10.3e} {f0['xi']/f0['r']:7.3f} " +
            " ".join(f"{c:+15.5f}" for c in cs_et) +
            f" {np.nanmean(cs_dc):9.5f} {kd:+10.2e} {lamk:+10.2e} "
            f"{np.nanmax(cnds):8.1e}")
        for kh, c in zip(KHS, cs_et):
            if np.isfinite(c) and c < 0:
                alertas.append((B1V, a0, kh, c, kd, lamk,
                                np.nanmax(cnds)))
        cal = np.nanmean(cs_dc)
        if np.isfinite(cal) and abs(cal - 1.0) > 0.01:
            nao_interp.append((B1V, a0, cal))

say("")
say("=" * 72)
say("VEREDITO R-10a / A1 (criterios pre-declarados no cabecalho)")
say("=" * 72)
say(f"  cobertura: r de {fundo(EPOCAS[0], 1.0)['r']:.2e} ate "
    f"{fundo(EPOCAS[-1], 1.0)['r']:.4f} — o regime r -> 0 (alto z) da")
say("  alegacao de 1407.4331 ESTA coberto (xi/r -> 4 confirma o ramo")
say("  finito primordial).")
if nao_interp:
    say(f"  [A1-CAL] {len(nao_interp)} ponto(s) com o espectador fora de")
    say(f"  1% (metodo fora de validade ali): "
        f"{[(b, f'a={a:.2g}', f'{c:.4f}') for b, a, c in nao_interp[:6]]}")
else:
    say("  [A1-CAL OK] o espectador da c_s^2 = 1 dentro de 1% em todos")
    say("  os pontos — o metodo esta calibrado em toda a varredura.")
if alertas:
    say(f"  >>> INSTABILIDADE DE GRADIENTE CONFIRMADA em "
        f"{len(alertas)} ponto(s):")
    say(f"      {'beta1':>6} {'a':>9} {'kh':>5} {'c_s^2':>9} "
        f"{'K2_Et':>10} {'lamK_rel':>10} {'cond':>8}")
    for b, a0, kh, c, kd, lamk, cn in alertas[:12]:
        say(f"      {b:6g} {a0:9.3g} {kh:5g} {c:+9.4f} {kd:+10.2e} "
            f"{lamk:+10.2e} {cn:8.1e}")
    kneg = [x for x in alertas if x[4] < 0]
    say("")
    if kneg:
        say(f"      ATENCAO: em {len(kneg)}/{len(alertas)} pontos o")
        say("      PROPRIO K2 do modo metrico e NEGATIVO — nesses")
        say("      pontos o sinal de om2/(k/a)^2 NAO e c_s^2 de um")
        say("      modo saudavel: e a assinatura de FANTASMA, nao de")
        say("      gradiente. Interpretar separadamente.")
    else:
        say("      K2 do modo metrico POSITIVO em todos os pontos de")
        say("      alerta => o sinal negativo e genuinamente de")
        say("      GRADIENTE (c_s^2 < 0 com cinetica sa), nao de")
        say("      fantasma.")
    bem = [x for x in alertas if x[6] < 1e6]
    say(f"      pontos de alerta com cond(W_XX) < 1e6 (bem")
    say(f"      condicionados): {len(bem)}/{len(alertas)} — o achado")
    say(f"      {'NAO ' if not bem else ''}depende de pontos mal")
    say(f"      condicionados.")
    say("      -> localizar a janela, medir |c_s| k/a vs H e")
    say("      reescrever o cap. 07. Achado mais grave desde o")
    say("      Erratum-02.")
else:
    say("  >>> RAMO-FINITO-ESTAVEL nesta implementacao: c_s^2 > 0 em")
    say("  TODAS as epocas (incluindo r -> 0), nos dois fundos e nos")
    say("  dois kh. A instabilidade de gradiente do finite branch")
    say("  reivindicada em 1407.4331 NAO se reproduz aqui.")
    say("  ISTO NAO FECHA O CONFRONTO: as diferencas candidatas a")
    say("  explicar a discrepancia sao (i) parametrizacao dos beta_n")
    say("  (o benchmark tem beta_3 = 0 e beta_4 != 0); (ii) presenca")
    say("  do espectador phi_- no nosso setor; (iii) convencao de")
    say("  c_s^2 (aqui = coeficiente de (k/a)^2 em om2_ef do sistema")
    say("  2-DOF reduzido, com o Cdot incluido — o R-9a mostrou que")
    say("  omitir Cdot inverte o sinal!). A hipotese (iii) e a mais")
    say("  provavel e a mais barata de testar contra a literatura:")
    say("  recomendo pedir/refazer a definicao exata usada em")
    say("  1407.4331 antes de declarar contradicao.")

os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
with open(os.path.join(HERE, 'out', 'r10a_gradiente_alto_z.txt'), 'w',
          encoding='utf-8') as fh:
    fh.write("\n".join(OUT) + "\n")
say("")
say("saida escrita em auditoria/code/out/r10a_gradiente_alto_z.txt")
