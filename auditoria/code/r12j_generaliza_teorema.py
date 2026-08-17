# -*- coding: utf-8 -*-
"""
r12j_generaliza_teorema.py — R-12(j): o teorema de c_s^2 em OUTRAS
celulas da classe F1.

NOTA DE ROTULO: este estudo nasceu como "R-12i", mas o rotulo R-12i ja
esta ocupado no branch revisao-corpus-pos-r12 pelo CONFRONTO com
Konnig et al. 1407.4331 (docs/resultado_r12i_confronto_konnig.md), que
e outra coisa. Renomeado para R-12j.

CONTEXTO. O R-12b provou em forma fechada, na celula minima
(beta_2 = beta_4 = 0, beta_0 = 1, mu = 1):

    c_s^2(r) = -(3r+1)(9r^5 - 6r^3 + 3r^2 - 10r + 2) / (2(3r^2+1)^2)
    -> -1 em r -> 0 ; +1 no atrator tardio.

A generalidade em (beta_0, beta_2, beta_4, mu) esta so em nivel 2b
(R-12g: 108/108 celulas numericas). Este script tenta subir o nivel
rodando a MESMA reducao simbolica em outras celulas.

PORQUE ISTO PODE FECHAR AGORA. A tentativa anterior (celula de
benchmark, beta_2 e beta_4 AMBOS nao-nulos) nao terminou: a
substituicao do fundo em W sozinha passou de 2000 s de CPU. As celulas
aqui ligam beta_2 e beta_4 UM DE CADA VEZ, o que mantem V_f com dois
termos em vez de tres.

CELULAS (todas F1, beta_3 = 0, beta_1 fixado a 1 on-shell):
  C1  b2=0,    b4=0,    b0=1, mu=1   (a do R-12b — controle)
  C2  b2=0,    b4=0,    b0=2, mu=3   (varia beta_0 e mu)
  C3  b2=-2/5, b4=0,    b0=1, mu=1   (liga beta_2)
  C4  b2=0,    b4=1/2,  b0=1, mu=1   (liga beta_4)

MEDIDAS: por celula, a forma fechada de c_s^2(r, H), a versao on-shell
c_s^2(r), o limite r -> 0, o limite no atrator tardio, e m_ef^2/H^2.

GATES (pre-declarados, por celula):
  V-K3  : linha 0 de K3 identicamente nula (Psi_f auxiliar).
  V-SPEC: espectador com om2 = (k/a)^2 + U'' EXATO.
  V-A   : c_s^2 invariante sob (a, k) -> (lam a, lam k).
  Celula que reprove qualquer um e reportada e PULADA (nao entra no
  enunciado).

CRITERIO: se todas as celulas que fecham derem c_s^2(r -> 0) = -1,
o enunciado "c_s^2 = -1 e constante de classe" sobe de nivel 2b para
nivel 1 nas celulas cobertas — e a formula em si passa a ser
comparavel entre celulas (ela NAO precisa ser a mesma; so o limite).

Uso: python -u auditoria/code/r12j_generaliza_teorema.py
Saida em auditoria/code/out/r12j_generaliza_teorema.txt
"""
import importlib.util
import os
import pickle
import sys
import time

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
DCODE = os.path.normpath(os.path.join(HERE, '..', '..', 'derivations', 'code'))
OUTD = os.path.join(HERE, 'out')
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
    print(f"[{time.time()-T0:7.1f}s] {line}", flush=True)
    OUT.append(line)


def grava():
    os.makedirs(OUTD, exist_ok=True)
    nome_saida = f'r12j_generaliza_teorema{("_" + _TAG) if _TAG else ""}.txt'
    with open(os.path.join(OUTD, nome_saida), 'w',
              encoding='utf-8') as fh:
        fh.write("\n".join(OUT) + "\n")


MULT = [0, 1, 2, 4]
DYN = [3, 5, 6]
r = sp.Symbol('r', positive=True)
Hq = H_s
R1 = sp.Rational
# permite rodar um subconjunto de celulas em processo separado, com
# cache proprio (evita corrida de escrita entre processos paralelos):
#   R12J_CELULAS=3  R12J_TAG=c4  python -u ...r12j...
_TAG = os.environ.get('R12J_TAG', '')
CACHE = os.path.join(OUTD, f'r12j_cache{("_" + _TAG) if _TAG else ""}.pkl')
# resposta conhecida da celula C1 (R-12b, commit 548bf3e) — gate V-C1
C1_ALVO = ("-(3*r + 1)*(9*r**5 - 6*r**3 + 3*r**2 - 10*r + 2)"
           "/(2*(3*r**2 + 1)**2)")

CELULAS = [
    ('C1  b2=0 b4=0 b0=1 mu=1', R1(1), R1(0), R1(0), R1(1)),
    ('C2  b2=0 b4=0 b0=2 mu=3', R1(2), R1(0), R1(0), R1(3)),
    ('C3  b2=-2/5 b4=0 b0=1 mu=1', R1(1), R1(-2, 5), R1(0), R1(1)),
    ('C4  b2=0 b4=1/2 b0=1 mu=1', R1(1), R1(0), R1(1, 2), R1(1)),
]

_SEL = os.environ.get('R12J_CELULAS', '')
if _SEL:
    _idx = [int(x) for x in _SEL.split(',')]
    CELULAS = [CELULAS[i] for i in _idx]

say("=" * 72)
say("R-12j — o teorema de c_s^2 em outras celulas da classe F1")
say("=" * 72)
say("[1] montando L2 simbolica (uma vez) ...")
L2s, fields, vels = d1.build_L2()
K7, C7, W7 = quadratic_matrices(L2s, fields, vels)
say("    pronta")


def cc(M):
    return M.applyfunc(sp.cancel)


def roda(nome, B0V, B2V, B4V, MUV):
    ME2V = MUV / (1 + MUV)
    kap = 1 / MUV
    Vf = b4 + 3 * b2 / r**2 + b1 / r**3
    rho_til = ((kap * b4 - 3 * b2) * r**2 - 3 * b1 * r
               + (3 * kap * b2 - b0) + kap * b1 / r)
    rhop = sp.cancel(sp.diff(rho_til, r))
    g_b1 = sp.cancel(-3 * rho_til / rhop)
    g2_b1 = sp.cancel(g_b1 * sp.diff(g_b1, r))
    L_b1 = sp.cancel(R1(1, 2) * (2 / r + sp.diff(Vf, r) / Vf) * g_b1)
    Ub_b1 = 3 * Hq**2 - Meff2 * (b0 + 3 * b1 * r + 3 * b2 * r**2)
    B1_DE_H = sp.cancel(sp.solve(sp.Eq(Hq**2, ME2V * r**2 * Vf / (3 * MUV)),
                                 b1)[0])
    NUM = {b0: B0V, b2: B2V, b4: B4V, b3: 0, Mf2: MUV, Meff2: ME2V,
           Mg2: 1, m2: 1}
    ELIM = {b1: sp.cancel(B1_DE_H.subs(NUM))}

    def sub_fundo(e):
        return sp.cancel(sp.expand(sp.expand(e).subs(NUM).subs(ELIM)))

    g, L = sub_fundo(g_b1), sub_fundo(L_b1)
    g2, Ubv = sub_fundo(g2_b1), sub_fundo(Ub_b1)
    xiv = sp.cancel(r + g)

    def dN(e):
        return sp.cancel(a_s * sp.diff(e, a_s) + g * sp.diff(e, r)
                         + Hq * L * sp.diff(e, Hq))

    if sp.simplify(dN(ELIM[b1])) != 0:
        return dict(erro='V-B1 reprovado')

    SUB = {Fb: 1, Fp: 0, Fpp: 0, chid_s: 0, chidd_s: 0, Up: 0, rho_s: 0,
           b_s: r * a_s, xi_s: xiv, Hf_s: Hq / r,
           Hd_s: Hq**2 * L, Hfd_s: sp.cancel(Hq**2 * (L - g / r) / r),
           xid_s: Hq * (g + g2), Ub: Ubv}
    SUB.update(NUM)
    SUB.update(ELIM)

    def sub_bg(M):
        return M.applyfunc(lambda e: sp.cancel(sp.together(e.subs(SUB))))

    t0 = time.time()
    K, C, W = sub_bg(K7), sub_bg(C7), sub_bg(W7)
    say(f"    fundo substituido ({time.time()-t0:.0f}s) ops W="
        f"{sum(sp.count_ops(e) for e in W)}")

    ponto = lambda M: M.applyfunc(lambda e: sp.cancel(Hq * dN(e)))
    Cd = ponto(C)

    Kx, Cx, Wx = K.copy(), C.copy(), W.copy()
    mset = set(MULT)
    for i in MULT:
        for j in range(7):
            cd, cij = Cd[i, j], C[i, j]
            if i == j:
                Wx[i, i] += cd
            elif j in mset:
                Wx[i, j] += cd
            else:
                Wx[i, j] += cd
                Wx[j, i] += cd
                Cx[j, i] -= cij
        for j in range(7):
            Cx[i, j] = 0
    WXX = cc((Wx[MULT, MULT] + Wx[MULT, MULT].T) / 2)
    t0 = time.time()
    WXXi = cc(WXX.inv(method='ADJ'))
    say(f"    W_XX invertida ({time.time()-t0:.0f}s)")
    CX = Cx[DYN, MULT]
    K3 = cc(Kx[DYN, DYN] + CX * WXXi * CX.T)
    C3 = cc(Cx[DYN, DYN] - CX * WXXi * Wx[MULT, DYN])
    W3 = cc(Wx[DYN, DYN] - Wx[DYN, MULT] * WXXi * Wx[MULT, DYN])
    if any(sp.cancel(K3[0, j]) != 0 for j in range(3)):
        return dict(erro='V-K3 reprovado')
    for j in range(3):
        K3[0, j] = 0
        K3[j, 0] = 0
    Cd3 = ponto(C3)

    Kx, Cx, Wx = K3.copy(), C3.copy(), W3.copy()
    for j in range(3):
        cij, cd = C3[0, j], Cd3[0, j]
        if j == 0:
            Wx[0, 0] += cd
        else:
            Wx[0, j] += cd
            Wx[j, 0] += cd
            Cx[j, 0] -= cij
    for j in range(3):
        Cx[0, j] = 0
    W00 = sp.cancel(Wx[0, 0])
    keep = [1, 2]
    cx, wx = Cx[keep, [0]], Wx[keep, [0]]
    K2 = cc(Kx[keep, keep] + cx * cx.T / W00)
    C2 = cc(Cx[keep, keep] - cx * Wx[[0], keep] / W00)
    W2 = cc(Wx[keep, keep] - wx * Wx[[0], keep] / W00)
    K2, W2 = cc((K2 + K2.T) / 2), cc((W2 + W2.T) / 2)
    Cd2 = ponto(C2)
    om2 = [sp.cancel((Cd2[i, i] + W2[i, i]) / K2[i, i]) for i in range(2)]

    if sp.simplify(om2[1] - (ksym**2 / a_s**2 + Upp)) != 0:
        return dict(erro='V-SPEC reprovado')
    Fm = sp.cancel(om2[0] * a_s**2 / ksym**2)
    lam = sp.Symbol('lambda_', positive=True)
    if sp.simplify(Fm.subs({a_s: lam * a_s, ksym: lam * ksym}) - Fm) != 0:
        return dict(erro='V-A reprovado')
    Fm = sp.cancel(Fm.subs(a_s, 1))

    HH = sp.cancel((ME2V * r**2 * Vf / (3 * MUV)).subs(NUM).subs({b1: 1}))
    cs2_kH = sp.factor(sp.simplify(sp.limit(Fm, ksym, sp.oo)))
    cs2_r = sp.factor(sp.cancel(cs2_kH.subs(Hq**2, HH)))
    cs2_0 = sp.simplify(sp.limit(cs2_r, r, 0, '+'))
    ser = sp.expand(sp.series(cs2_r, r, 0, 2).removeO())
    rho_on = sp.cancel(rho_til.subs(NUM).subs({b1: 1}))
    raizes = [x for x in sp.solve(sp.Eq(rho_on, 0), r)
              if x.is_real and x > 0]
    rinf = min(raizes) if raizes else None
    val_inf = (sp.radsimp(sp.simplify(cs2_r.subs(r, rinf)))
               if rinf is not None else None)
    om2_on = sp.cancel(om2[0].subs(a_s, 1).subs(Hq**2, HH))
    mef = sp.simplify(sp.limit(om2_on - cs2_r * ksym**2, ksym, sp.oo))
    mef_H = sp.simplify(sp.limit(sp.cancel(mef / HH), r, 0, '+'))
    return dict(erro=None, cs2_kH=cs2_kH, cs2_r=cs2_r, cs2_0=cs2_0,
                ser=ser, rinf=rinf, val_inf=val_inf, mef_H=mef_H, HH=HH)


def carrega():
    if not os.path.exists(CACHE):
        return {}
    with open(CACHE, 'rb') as fh:
        cru = pickle.load(fh)
    return {k: {kk: (sp.sympify(vv) if isinstance(vv, str) else vv)
                for kk, vv in v.items()} for k, v in cru.items()}


def guarda(d):
    os.makedirs(OUTD, exist_ok=True)
    cru = {k: {kk: (sp.srepr(vv) if isinstance(vv, sp.Basic) else vv)
               for kk, vv in v.items()} for k, v in d.items()}
    with open(CACHE, 'wb') as fh:
        pickle.dump(cru, fh)


def gate_c1(nome, o):
    """V-C1: a celula ja provada no R-12b tem de sair identica."""
    if not nome.startswith('C1'):
        return True
    alvo = sp.sympify(C1_ALVO, locals={'r': r})
    bate = sp.simplify(sp.cancel(o['cs2_r'] - alvo)) == 0
    say(f"    [V-C1] reproduz a forma fechada do R-12b (548bf3e): "
        f"{'SIM' if bate else 'NAO'}")
    if not bate:
        say("    [V-C1] REPROVADO — o pipeline mudou de resposta numa")
        say("           celula ja provada. Abortando.")
    return bate


res = carrega()
if res:
    say(f"[cache] celulas ja concluidas: {sorted(res)}")
for nome, B0V, B2V, B4V, MUV in CELULAS:
    if nome in res:
        o = res[nome]
        say("")
        say(f"CELULA {nome} — do cache: c_s^2(r->0) = "
            f"{sp.sstr(o['cs2_0'])}, c_s^2(r_inf) = "
            f"{sp.sstr(o['val_inf'])}, m_ef^2/H^2 = {sp.sstr(o['mef_H'])}")
        if not gate_c1(nome, o):
            grava()
            sys.exit(1)
        continue
    say("")
    say("=" * 72)
    say(f"CELULA {nome}")
    say("=" * 72)
    t0 = time.time()
    try:
        out = roda(nome, B0V, B2V, B4V, MUV)
    except Exception as e:                               # noqa: BLE001
        say(f"    EXCECAO: {type(e).__name__}: {str(e)[:120]}")
        grava()
        continue
    if out.get('erro'):
        say(f"    {out['erro']} — celula PULADA")
        grava()
        continue
    say(f"    concluida em {time.time()-t0:.0f}s")
    say(f"    on-shell H^2 = {sp.sstr(sp.factor(out['HH']))}")
    say(f"    c_s^2(r) = {sp.sstr(out['cs2_r'])}")
    say(f"    serie    : {sp.sstr(out['ser'])} + O(r^2)")
    say(f"    ===> r -> 0        : c_s^2 = {sp.sstr(out['cs2_0'])}")
    if out['rinf'] is not None:
        say(f"    ===> atrator r_inf = {sp.sstr(out['rinf'])} "
            f"({float(out['rinf']):.6f}) : c_s^2 = "
            f"{sp.sstr(out['val_inf'])} ({float(out['val_inf']):.10f})")
    say(f"    m_ef^2/H^2 em r -> 0 : {sp.sstr(out['mef_H'])}")
    if not gate_c1(nome, out):
        grava()
        sys.exit(1)
    res[nome] = out
    guarda(res)
    grava()

say("")
say("=" * 72)
say("VEREDITO R-12j")
say("=" * 72)
say(f"  celulas que fecharam em forma fechada: {len(res)}/{len(CELULAS)}")
if res:
    say("")
    say(f"  {'celula':<28} {'c_s^2(r->0)':>12} {'c_s^2(r_inf)':>14} "
        f"{'m_ef^2/H^2':>12}")
    for nome, o in res.items():
        say(f"  {nome:<28} {sp.sstr(o['cs2_0']):>12} "
            f"{sp.sstr(o['val_inf']) if o['val_inf'] is not None else '—':>14} "
            f"{sp.sstr(o['mef_H']):>12}")
    todos_m1 = all(o['cs2_0'] == -1 for o in res.values())
    todos_p1 = all(o['val_inf'] == 1 for o in res.values()
                   if o['val_inf'] is not None)
    say("")
    if todos_m1:
        say("  ===> c_s^2(r -> 0) = -1 em TODAS as celulas que fecharam:")
        say("       o valor -1 e constante de classe em NIVEL 1 nelas")
        say("       (e nivel 2b nas 108 do R-12g).")
    else:
        say("  ===> ATENCAO: nem todas dao -1 — reportar a dependencia.")
    if todos_p1:
        say("  ===> c_s^2(r_inf) = +1 em todas: o atrator tardio tambem e")
        say("       constante de classe.")
    say("")
    say("  NOTA: as FORMULAS diferem entre celulas (como tem de ser — a")
    say("  trajetoria r(a) depende dos beta_n); o que e universal sao os")
    say("  dois LIMITES.")

grava()
say("")
say("saida escrita em auditoria/code/out/r12j_generaliza_teorema.txt")
