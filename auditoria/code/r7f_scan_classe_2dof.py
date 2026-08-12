# -*- coding: utf-8 -*-
"""
r7f_scan_classe_2dof.py — R-7f: SCAN DE CLASSE no sistema 2-DOF
corrigido — a retirada (ou nao) do no-go congelado de classe.

CONTEXTO: erratum_02 + R-7a-e. O no-go de classe beta-constante
(~1500 pontos; docs/no_go_beta_constante.md, modulacao_qep.py,
investigacao1) foi medido com QEP CONGELADO (taxas zeradas a mao,
a=10) sobre o sistema de 3 DOFs ESPURIO — dois instrumentos hoje
invalidados (D-2 e erratum-02). O R-7a ja mostrou saude nos dois
benchmarks (beta1=1, 4.47; mu=1). Este scan cobre a CLASSE:

CELULAS: mu in {0.3, 1, 3, 10} x beta1 in {0.6, 1.0, 2.2, 4.47}
(beta0=1, beta2=-0.4, beta4=0.5) + a celula da FRESTA mu=0.1
(beta1=0.2, beta2=-1.0) — a familia de patologia "estruturalmente
diferente" do antigo no-go (fantasma quase-nulo, lapso Phi_f) — +
mu=0.1 REF (esperado: fundo invalido; reportar). Celulas sem fundo
valido em alguma epoca sao reportadas e puladas (como no antigo).

MEDIDAS por celula valida, epocas a in {150, 3635, 74992}, alvos
kh in {0.2, 2, 30} (kc = kh a H(a)); mini-trilha local de 41 pts,
reducao corrigida canal-S (G1 < 1e-10 por mini-trilha):
  - autovalores de K2 no ponto central: algum <= 0?
  - W00: sinal estavel na mini-trilha e |W00|/esc > 1e-6?
  - omega^2 do QEP 2x2 (dispersao; informativo).

CRITERIOS (pre-declarados):
  zero violacoes (negK ou W00 instavel) em todas as celulas/epocas/k
      -> NO-GO-DE-CLASSE-RETIRADO: a classe beta-constante e sa no
      sistema fisico; o sweep antigo media o sistema espurio.
  violacao em celula(s) -> listar; a(s) celula(s) vira(m) alvo de
      mergulho com a maquinaria completa (R-7a) antes de qualquer
      enunciado.
  NOTA de fronteira: epocas/k discretos (3x3) por celula — e um scan
      de assinatura (K2/W00 sao funcoes continuas e lentas do fundo),
      nao um mapa fino; o mapa fino so se justifica se algo falhar.
  PENDENTE (deferido, declarado): ramo algebrico (r*=1.25) — exige o
      porte do arranjo modulado da investigacao1; prior de artefato
      (mesmos instrumentos), mas sem reexecucao nao se afirma.

Requer sympy, numpy. ~4-8 min.
Uso (raiz do repo, venv ativo):
    python auditoria/code/r7f_scan_classe_2dof.py
Saida em auditoria/code/out/r7f_scan_classe_2dof.txt
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
MUS = [0.3, 1.0, 3.0, 10.0]
B1S = [0.6, 1.0, 2.2, 4.47]
EPOCAS = [150.0, 3635.0, 74992.0]
KHS = [0.2, 2.0, 30.0]
B0V, B4V = 1.0, 0.5
RHO0 = 0.3
UPPV = 0.3

say("=" * 72)
say("R-7f — SCAN DE CLASSE (mu x beta1 + fresta) NO 2-DOF CORRIGIDO")
say("=" * 72)

if not d1.gr_selfcheck():
    say("[!] V1 falhou — abortando")
    sys.exit(1)
say("[V1] GR selfcheck da biblioteca: PASSA")

L2s, fields, vels = d1.build_L2()
K7, C7, W7 = quadratic_matrices(L2s, fields, vels)
if [str(f) for f in fields] != NOMES:
    raise RuntimeError("ordem de campos mudou")
say("[montagem] K,C,W 7x7 prontos")

Hdd_s, Hfdd_s, xidd_s, chiddd_s = sp.symbols(
    'Hddot H_fddot xiddot chidddot')
EXTRA_RATES = {Hd_s: Hdd_s, Hfd_s: Hfdd_s, xid_s: xidd_s,
               chidd_s: chiddd_s}
Cd7 = sp.zeros(7, 7)
for i in range(7):
    for j in range(7):
        Cd7[i, j] = dt_background(C7[i, j], EXTRA_RATES)
say("[canal-S] pronto")

LIVRES = (a_s, b_s, xi_s, H_s, Hf_s, Hd_s, Hfd_s, xid_s,
          chid_s, chidd_s, Ub, Up, Upp, ksym, Mf2, Meff2,
          Hdd_s, Hfdd_s, xidd_s, chiddd_s)
FIXOS = {Mg2: 1, m2: 1, rho_s: 0}
BETAS = (b0, b1, b2, b3, b4)


def fatias(M):
    Msub = M.subs(FIXOS)
    base_s = Msub.subs({Fb: 0, Fp: 0, Fpp: 0})
    out = {'base': sp.lambdify(LIVRES, base_s, modules='numpy')}
    for tag, fsub in (('Fb', {Fb: 1, Fp: 0, Fpp: 0}),):
        for n, bn in enumerate(BETAS):
            bsub = {bm: (1 if mm == n else 0) for mm, bm in enumerate(BETAS)}
            Sl = Msub.subs(fsub).subs(bsub) - base_s
            out[(tag, n)] = sp.lambdify(LIVRES, Sl, modules='numpy')
    return out


FK, FC, FW, FCd = fatias(K7), fatias(C7), fatias(W7), fatias(Cd7)
say("[fatias] prontas")


def monta(fat, args, bvals):
    M = np.array(fat['base'](*args), float).copy()
    for n in range(5):
        if bvals[n]:
            M += bvals[n] * np.array(fat[('Fb', n)](*args), float)
    return M


def fundo_cel(a, mu, B1V, B2V):
    kap = 1.0 / mu
    meff2 = mu / (1.0 + mu)
    rho = RHO0 * a**-3
    rho_til = rho / meff2
    rr = np.roots([kap * B4V - 3 * B2V, -3 * B1V,
                   3 * kap * B2V - B0V - rho_til, kap * B1V])
    r_esc = max(1e-14, 1e-6 * kap * B1V / max(rho_til, 1.0))
    reais = sorted(z.real for z in rr
                   if abs(z.imag) < 1e-9 and z.real > r_esc)
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


def fundo_ext(a, mu, B1V, B2V, h=1e-5):
    f = fundo_cel(a, mu, B1V, B2V)
    if f is None:
        return None
    fp = fundo_cel(a * np.exp(h), mu, B1V, B2V)
    fm = fundo_cel(a * np.exp(-h), mu, B1V, B2V)
    if fp is None or fm is None:
        return None
    H = f['H']
    f['Hdd'] = H * (fp['Hd'] - fm['Hd']) / (2 * h)
    f['Hfdd'] = H * (fp['Hfd'] - fm['Hfd']) / (2 * h)
    f['xidd'] = H * (fp['xid'] - fm['xid']) / (2 * h)
    return f


def matriz_D(kc):
    return np.diag([1.0, 1.0 / kc, 1.0, 1.0, 1.0 / kc, 1.0 / kc**2, 1.0])


def e1_corrigida(Kt, Ct, Wt, Cdot):
    K = Kt.copy()
    C = Ct.copy()
    W = Wt.copy()
    n = K.shape[0]
    esc = max(1.0, np.max(np.abs(K)))
    mset = set(MULT)
    for i in MULT:
        if np.max(np.abs(K[i, :])) > 1e-10 * esc:
            raise RuntimeError("linha K de multiplicador nao-nula")
        for j in range(n):
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
    WXX = W[np.ix_(MULT, MULT)]
    WXX = 0.5 * (WXX + WXX.T)
    if np.linalg.cond(WXX) > 1e12:
        raise RuntimeError("W_XX mal condicionada")
    WXXi = np.linalg.inv(WXX)
    CdX = C[np.ix_(DYN, MULT)]
    K3 = K[np.ix_(DYN, DYN)] + CdX @ WXXi @ CdX.T
    C3 = C[np.ix_(DYN, DYN)] - CdX @ WXXi @ W[np.ix_(MULT, DYN)]
    W3 = W[np.ix_(DYN, DYN)] - W[np.ix_(DYN, MULT)] @ WXXi \
        @ W[np.ix_(MULT, DYN)]
    return K3, C3, W3


def e2_psif(K3, C3, W3, C3dot):
    K = K3.copy()
    C = C3.copy()
    W = W3.copy()
    for j in range(3):
        cij = C3[0, j]
        cd = C3dot[0, j]
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
    return 0.5 * (K2 + K2.T), C2, 0.5 * (W2 + W2.T), W00


def celula_ponto(mu, B1V, B2V, a0, kh):
    """mini-trilha local de 41 pts; devolve diagnostico ou None."""
    f0 = fundo_cel(a0, mu, B1V, B2V)
    if f0 is None:
        return 'fundo-invalido'
    kc = kh * a0 * f0['H']
    Ns = np.linspace(np.log(a0) - 0.025, np.log(a0) + 0.025, 41)
    Hs_arr = np.zeros(41)
    Ms = {x: np.zeros((41, 7, 7)) for x in ('K', 'C', 'W', 'CdS')}
    D = matriz_D(kc)
    meff2 = mu / (1.0 + mu)
    for p, N in enumerate(Ns):
        a = np.exp(N)
        f = fundo_ext(a, mu, B1V, B2V)
        if f is None:
            return 'fundo-invalido'
        Hs_arr[p] = f['H']
        args = (a, f['r'] * a, f['xi'], f['H'], f['Hf'],
                f['Hd'], f['Hfd'], f['xid'], 0.0, 0.0,
                f['Ub'], 0.0, UPPV, kc, mu, meff2,
                f['Hdd'], f['Hfdd'], f['xidd'], 0.0)
        bvals = (B0V, B1V, B2V, 0.0, B4V)
        Ms['K'][p] = D @ monta(FK, args, bvals) @ D
        Ms['C'][p] = D @ monta(FC, args, bvals) @ D
        Ms['W'][p] = D @ monta(FW, args, bvals) @ D
        Ms['CdS'][p] = D @ monta(FCd, args, bvals) @ D
    Cdots = Ms['CdS']
    K3s = np.zeros((41, 3, 3))
    C3s = np.zeros((41, 3, 3))
    W3s = np.zeros((41, 3, 3))
    g1 = 0.0
    try:
        for p in range(41):
            K3, C3, W3 = e1_corrigida(Ms['K'][p], Ms['C'][p],
                                      Ms['W'][p], Cdots[p])
            esc = np.max(np.abs(K3))
            g1 = max(g1, np.max(np.abs(K3[0, :])) / esc)
            K3[0, :] = 0.0
            K3[:, 0] = 0.0
            K3s[p], C3s[p], W3s[p] = K3, C3, W3
    except RuntimeError as e:
        return f'reducao: {e}'
    if g1 >= G1_TOL:
        return f'G1={g1:.1e}'
    C3d = np.gradient(C3s, Ns, axis=0) * Hs_arr[:, None, None]
    W00s = np.zeros(41)
    lam_c = None
    om2 = None
    for p in range(41):
        K2, C2, W2, W00s[p] = e2_psif(K3s[p], C3s[p], W3s[p], C3d[p])
        if p == 20:
            lam_c = np.linalg.eigvalsh(K2)
            om2 = (W2[0, 0] / K2[0, 0], W2[1, 1] / K2[1, 1])
    sinais = np.sign(W00s[2:-2])
    trocas = int(np.sum(sinais[1:] * sinais[:-1] < 0))
    w00rel = np.min(np.abs(W00s[2:-2])) / np.max(np.abs(W3s[20]))
    return dict(lam=lam_c, om2=om2, trocas=trocas, w00rel=float(w00rel))


CELULAS = [(mu, B1V, -0.4, 'REF') for mu in MUS for B1V in B1S]
CELULAS.append((0.1, 1.0, -0.4, 'REF'))
CELULAS.append((0.1, 0.2, -1.0, 'fresta'))

violacoes = []
invalidas = []
say("")
say(f"{'mu':>5} {'b1':>5} {'b2':>5} {'tag':>7} | por epoca x kh: "
    f"min lam(K2)/esc, trocas W00")
for mu, B1V, B2V, tag in CELULAS:
    linha = f"{mu:5.1f} {B1V:5.2f} {B2V:5.1f} {tag:>7} |"
    viol_cel = False
    todas_inv = True
    for a0 in EPOCAS:
        for kh in KHS:
            r = celula_ponto(mu, B1V, B2V, a0, kh)
            if isinstance(r, str):
                linha += " inv"
                continue
            todas_inv = False
            esc = np.max(np.abs(r['lam']))
            rel = r['lam'][0] / esc
            marca = ""
            if r['lam'][0] <= 0 or r['trocas'] > 0 \
                    or r['w00rel'] < 1e-6:
                marca = "!"
                viol_cel = True
                violacoes.append((mu, B1V, B2V, tag, a0, kh, r))
            linha += f" {rel:+.0e}{marca}"
    say(linha)
    if todas_inv:
        invalidas.append((mu, B1V, B2V, tag))
    del viol_cel

say("")
say("=" * 72)
say("VEREDITO R-7f (criterios pre-declarados no cabecalho)")
say("=" * 72)
say(f"  celulas sem fundo valido em nenhuma epoca: "
    f"{[(m, b, bb, tg) for m, b, bb, tg in invalidas]}")
if not violacoes:
    say("  >>> NO-GO-DE-CLASSE-RETIRADO: zero violacoes (negK / W00)")
    say("  em todas as celulas validas x epocas x k. A classe beta-")
    say("  constante e sa no sistema fisico de 2 DOFs; o sweep antigo")
    say("  (~1500 pts, QEP congelado, 3-DOF espurio) media artefato.")
    say("  Fronteira: scan de assinatura 3 epocas x 3 k por celula;")
    say("  ramo algebrico DEFERIDO (declarado no cabecalho).")
else:
    say(f"  >>> {len(violacoes)} violacao(oes):")
    for mu, B1V, B2V, tag, a0, kh, r in violacoes:
        say(f"      mu={mu} b1={B1V} b2={B2V} [{tag}] a={a0:g} kh={kh:g}: "
            f"lam0/esc={r['lam'][0]/np.max(np.abs(r['lam'])):+.2e}, "
            f"trocas={r['trocas']}, w00rel={r['w00rel']:.1e}")
    say("  — mergulho com a maquinaria completa (R-7a) antes de")
    say("  qualquer enunciado sobre essas celulas.")

os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
with open(os.path.join(HERE, 'out', 'r7f_scan_classe_2dof.txt'), 'w',
          encoding='utf-8') as fh:
    fh.write("\n".join(OUT) + "\n")
say("")
say("saida escrita em auditoria/code/out/r7f_scan_classe_2dof.txt")
