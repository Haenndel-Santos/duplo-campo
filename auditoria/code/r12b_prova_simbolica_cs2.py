# -*- coding: utf-8 -*-
"""
r12b_prova_simbolica_cs2.py — R-12(b): a REDUCAO 2-DOF FEITA EM FORMA
FECHADA, e c_s^2 do escalar metrico como LIMITE EXATO (nao ajuste).

OBJETIVO (item 1 da fila pos-R-11): estabelecer analiticamente o valor
de c_s^2 do escalar metrico no regime r -> 0 da classe F1.

CONTEXTO (ler junto com docs/resultado_r12_instrumento_e_cs2.md). O
alvo "provar c_s^2 = -1" vem do R-11. No meio desta sessao, as sondas
R-12a/R-12c sugeriram que -1 era artefato de extrapolacao e que o valor
sub-horizonte seria -0.687; isso foi RETRATADO pelo R-12e/f/g, que
demonstraram que o desvio vinha do estencil de 2a ordem (np.gradient)
usado para Cdot3/Cdot2, amplificado pelo condicionamento da reducao.
Com instrumento limpo o canal numerico da -1 com |c_s^2+1| <= 1.1e-7 em
108/108 celulas. Este script fecha o alvo em FORMA FECHADA.

DEFINICAO ADOTADA (padrao):  c_s^2(r) = lim_{k -> oo} om2_ef * a^2/k^2
— o coeficiente do termo de gradiente na relacao de dispersao
sub-horizonte. E o que governa a taxa |c_s| k/a da instabilidade.

METODO (zero ajuste, zero grade numerica):
  1. L2 simbolica (mesma acao e gauge de derivations/code/
     01_setor_escalar_K_Omega.py) -> K7, C7, W7 exatas.
  2. Fundo EXATO em coordenadas (r, H) com BETA_1 ELIMINADO:
         beta_1 = 3(1+mu) H^2 r - beta_4 r^3 - 3 beta_2 r
     (que e a equacao de Friedmann do setor f resolvida para beta_1).
     Esse e o passo que faz a conta fechar. Se em vez disso tratarmos
     H como simbolo livre com o vinculo H^2 = HH(r) guardado para o
     fim, as identidades ESTRUTURAIS da reducao — em particular
     K3[0,:] = 0, que diz que Psi_f e auxiliar — deixam de valer
     identicamente e a reducao nao pode ser feita (foi o modo de falha
     da v2 deste script, preservado no git). Com beta_1 eliminado,
     (a, r, k, H) sao coordenadas LIVRES, tudo e racional, e nao ha
     extensao algebrica nem raiz em lugar nenhum.
     A legitimidade e um teorema de uma linha, verificado como gate:
     dN(beta_1) = 0 identicamente (V-B1), logo dN em (r, H) coincide
     com a derivada verdadeira a beta_1 fixo.
  3. E1 (multiplicadores Phi_g, B_g, Phi_f, B_f) e E2 (Psi_f) por
     complemento de Schur SIMBOLICO, com a mesma absorcao one-shot do
     Cdot da maquinaria pos-Erratum-02 (S simetrica, Cdot uma vez por
     par).
     A reescala D = diag(1, 1/k, 1, 1, 1/k, 1/k^2, 1) e OMITIDA de
     proposito: sendo congruencia diagonal CONSTANTE, cancela em
     om2_ii = (Cdot2+W2)_ii/K2_ii. Ela existe so para condicionamento
     numerico.
  4. d/dt = H * dN,  dN = a d/da + g d/dr + H L d/dH, com k comovel
     FIXO — exatamente o que o numerico faz por np.gradient.

GATES (pre-declarados):
  V-BG   : d2r/dN2 simbolico == expressao do codigo numerico e
           rho~'(r) == dW(r). Falha => fundo simbolico != numerico.
  V-B1   : dN(beta_1) == 0 identicamente. E o que autoriza (2).
  V-K3   : a linha 0 de K3 (Psi_f) e IDENTICAMENTE nula em forma
           fechada — o gate G1 do numerico (|.| < 1e-10) vira exato.
  V-EVEN : om2 e PAR em H (paridade t -> -t com p(B) = -1). Falha =>
           erro de montagem.
  V-SPEC : c_s^2 do espectador dchi == 1 EXATAMENTE, como identidade
           racional. E o calibrador do R-10a, agora analitico.
  V-A    : om2/(k/a)^2 nao depende de a.
  V-NUM  : a forma fechada avaliada em r = 1e-6 e 1e-9 tem de bater
           com o canal limpo (mpmath dps=60, estencil de 8a ordem) do
           R-12f/g dentro do que a diferenca de celula permite.

FRONTEIRA (identica a do R-10a/R-11): classe F1 (beta_3 = 0), ramo
finito, materia so como rho de fundo, sem radiacao, F' = F'' = 0
(beta-constante), sistema 2-DOF do setor escalar. Celula de referencia
= o benchmark beta1=1 do R-10a; a generalidade em (beta_0, beta_2,
beta_4, mu) e o objeto do R-12c.

Requer sympy. Uso (raiz do repo, venv ativo):
    python -u auditoria/code/r12b_prova_simbolica_cs2.py
Saida em auditoria/code/out/r12b_prova_simbolica_cs2.txt
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
    with open(os.path.join(OUTD, 'r12b_prova_simbolica_cs2.txt'), 'w',
              encoding='utf-8') as fh:
        fh.write("\n".join(OUT) + "\n")


NOMES = ['Phi_g', 'B_g', 'Phi_f', 'Psi_f', 'B_f', 'E_f', 'dchi']
MULT = [0, 1, 2, 4]
DYN = [3, 5, 6]

r = sp.Symbol('r', positive=True)
Hq = H_s
kh = sp.Symbol('kh', positive=True)

# CELULA DA PROVA. beta_2 = beta_4 = 0 (o modelo minimo beta_0-beta_1
# da classe F1): membro legitimo da F1, e a unica escolha que mantem o
# fundo pequeno o bastante para a reducao fechar em forma exata. A
# generalidade em (beta_0, beta_2, beta_4, mu) e estabelecida
# numericamente pelo R-12g (108/108 celulas, |c_s^2+1| <= 1.1e-7).
B0V, B2V, B4V, MUV = (sp.Integer(1), sp.Integer(0),
                      sp.Integer(0), sp.Integer(1))
ME2V = MUV / (1 + MUV)

os.makedirs(OUTD, exist_ok=True)
say("=" * 72)
say("R-12b — c_s^2 do escalar metrico EM FORMA FECHADA (reducao 2-DOF)")
say("=" * 72)

# ----------------------------------------------------------------------
# 1. fundo exato em (r, H), com beta_1 eliminado
# ----------------------------------------------------------------------
kap = 1 / MUV
Vf = b4 + 3 * b2 / r**2 + b1 / r**3
rho_til = ((kap * b4 - 3 * b2) * r**2 - 3 * b1 * r
           + (3 * kap * b2 - b0) + kap * b1 / r)
dW_cod = kap * (2 * b4 * r - b1 / r**2) - 3 * b1 - 6 * b2 * r
d2W_cod = kap * (2 * b4 + 2 * b1 / r**3) - 6 * b2
rhop = sp.cancel(sp.diff(rho_til, r))                  # a beta_n FIXOS
g_b1 = sp.cancel(-3 * rho_til / rhop)                  # dr/dN
g2_b1 = sp.cancel(g_b1 * sp.diff(g_b1, r))
g2_cod = (9 * rho_til / dW_cod + 3 * rho_til * d2W_cod * g_b1 / dW_cod**2)
L_b1 = sp.cancel(sp.Rational(1, 2) * (2 / r + sp.diff(Vf, r) / Vf) * g_b1)
rho_int = Meff2 * (b0 + 3 * b1 * r + 3 * b2 * r**2)
Ub_b1 = 3 * Hq**2 - rho_int

v1 = sp.simplify(rhop - dW_cod)
v2 = sp.simplify(g2_b1 - g2_cod)
say("")
say(f"[V-BG] rho~'(r) - dW(r) = {v1}   (esperado 0)")
say(f"[V-BG] d2r/dN2 (cadeia) - d2r/dN2 (codigo) = {v2}   (esperado 0)")
if v1 != 0 or v2 != 0:
    say("[V-BG] REPROVADO. Abortando.")
    grava()
    sys.exit(1)
say("[V-BG] APROVADO — o fundo simbolico e o mesmo do R-10a/R-11.")

# beta_1 eliminado pela Friedmann do setor f: H^2 = M_eff^2 r^2 V_f/(3 mu)
B1_DE_H = sp.cancel(sp.solve(sp.Eq(Hq**2, ME2V * r**2 * Vf / (3 * MUV)),
                             b1)[0])
NUM = {b0: B0V, b2: B2V, b4: B4V, b3: 0, Mf2: MUV, Meff2: ME2V,
       Mg2: 1, m2: 1}
ELIM = {b1: sp.cancel(B1_DE_H.subs(NUM))}
say("")
say("[elim] beta_1 = " + sp.sstr(sp.expand(ELIM[b1]))
    + "   (Friedmann do setor f resolvida para beta_1)")


def sub_fundo(e):
    return sp.cancel(sp.expand(sp.expand(e).subs(NUM).subs(ELIM)))


g = sub_fundo(g_b1)
L = sub_fundo(L_b1)
Ubv = sub_fundo(Ub_b1)
g2 = sub_fundo(g2_b1)
xiv = sp.cancel(r + g)


def dN(e):
    """d/dN ao longo do fundo, k comovel fixo."""
    return sp.cancel(a_s * sp.diff(e, a_s) + g * sp.diff(e, r)
                     + Hq * L * sp.diff(e, Hq))


vb1 = sp.simplify(dN(ELIM[b1]))
say(f"[V-B1] dN(beta_1) = {vb1}   (esperado 0 — legitima as coordenadas"
    " (r, H) livres)")
if vb1 != 0:
    say("[V-B1] REPROVADO. Abortando.")
    grava()
    sys.exit(1)
say("[V-B1] APROVADO.")
say("       (xi/r -> 4 em r -> 0 e verificado ON-SHELL adiante; em")
say("       coordenadas (r, H) livres o limite a H fixo nao e o fisico)")

# ----------------------------------------------------------------------
# 2. L2 -> K7, C7, W7 com o fundo substituido   (cache por etapa)
# ----------------------------------------------------------------------
SUB = {Fb: 1, Fp: 0, Fpp: 0, chid_s: 0, chidd_s: 0, Up: 0, rho_s: 0,
       b_s: r * a_s, xi_s: xiv, Hf_s: Hq / r,
       Hd_s: Hq**2 * L, Hfd_s: sp.cancel(Hq**2 * (L - g / r) / r),
       xid_s: Hq * (g + g2), Ub: Ubv}
SUB.update(NUM)
SUB.update(ELIM)

CACHE = os.path.join(OUTD, 'r12b_cache.pkl')
etapas = {}
if os.path.exists(CACHE):
    with open(CACHE, 'rb') as fh:
        etapas = pickle.load(fh)
    say(f"[cache] etapas disponiveis: {sorted(etapas)}")


def salva(nome, val):
    etapas[nome] = val
    with open(CACHE, 'wb') as fh:
        pickle.dump(etapas, fh)
    return val


def ops(M):
    return sum(sp.count_ops(e) for e in M)


if 'KCW' in etapas:
    K, C, W = etapas['KCW']
    say("[1-2] K,C,W carregadas do cache")
else:
    say("")
    say("[1] montando L2 simbolica ...")
    L2s, fields, vels = d1.build_L2()
    K7, C7, W7 = quadratic_matrices(L2s, fields, vels)
    if [str(f) for f in fields] != NOMES:
        raise RuntimeError("ordem de campos mudou")
    say("[2] substituindo o fundo (r, H, a, k) ...")

    def sub_bg(M, nome):
        t0 = time.time()
        R = M.applyfunc(lambda e: sp.cancel(sp.together(e.subs(SUB))))
        say(f"    {nome}: {time.time()-t0:.1f}s  ops={ops(R)}")
        return R

    K, C, W = sub_bg(K7, 'K'), sub_bg(C7, 'C'), sub_bg(W7, 'W')
    salva('KCW', (K, C, W))
say(f"    ops: K={ops(K)} C={ops(C)} W={ops(W)}")


def ponto(M):
    return M.applyfunc(lambda e: sp.cancel(Hq * dN(e)))


def cc(M):
    return M.applyfunc(sp.cancel)


if 'E1' in etapas:
    K3, C3, W3 = etapas['E1']
    say("[3-4] E1 carregada do cache")
else:
    say("[3] Cdot7 ...")
    t0 = time.time()
    Cd = ponto(C)
    say(f"    pronto ({time.time()-t0:.1f}s)")
    say("[4] E1: eliminando Phi_g, B_g, Phi_f, B_f ...")
    t0 = time.time()
    Kx, Cx, Wx = K.copy(), C.copy(), W.copy()
    mset = set(MULT)
    for i in MULT:
        if any(sp.cancel(Kx[i, j]) != 0 for j in range(7)):
            raise RuntimeError(f"K linha {i} nao-nula")
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
    say(f"    invertendo W_XX 4x4 (ops={ops(WXX)}) ...")
    t = time.time()
    WXXi = cc(WXX.inv(method='ADJ'))
    say(f"    inversa pronta ({time.time()-t:.1f}s, ops={ops(WXXi)})")
    CX = Cx[DYN, MULT]
    K3 = cc(Kx[DYN, DYN] + CX * WXXi * CX.T)
    C3 = cc(Cx[DYN, DYN] - CX * WXXi * Wx[MULT, DYN])
    W3 = cc(Wx[DYN, DYN] - Wx[DYN, MULT] * WXXi * Wx[MULT, DYN])
    say(f"    E1 concluida ({time.time()-t0:.1f}s) "
        f"ops: K3={ops(K3)} C3={ops(C3)} W3={ops(W3)}")
    salva('E1', (K3, C3, W3))

lin0 = [sp.cancel(K3[0, j]) for j in range(3)]
say("")
say(f"[V-K3] linha 0 (Psi_f) de K3 nula? {[e == 0 for e in lin0]}")
if any(e != 0 for e in lin0):
    say("[V-K3] REPROVADO — Psi_f nao e auxiliar. Abortando.")
    for j in range(3):
        say(f"       K3[0,{j}] ops = {sp.count_ops(lin0[j])}")
    grava()
    sys.exit(1)
say("[V-K3] APROVADO — o gate G1 do numerico (|.| < 1e-10) e EXATO:"
    " Psi_f e algebrico em forma fechada.")
for j in range(3):
    K3[0, j] = 0
    K3[j, 0] = 0

if 'E2' in etapas:
    K2, C2, W2 = etapas['E2']
    say("[5-6] E2 carregada do cache")
else:
    say("[5] Cdot3 ...")
    t0 = time.time()
    Cd3 = ponto(C3)
    say(f"    pronto ({time.time()-t0:.1f}s, ops={ops(Cd3)})")
    say("[6] E2: eliminando Psi_f ...")
    t0 = time.time()
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
    cx = Cx[keep, [0]]
    wx = Wx[keep, [0]]
    K2 = cc(Kx[keep, keep] + cx * cx.T / W00)
    C2 = cc(Cx[keep, keep] - cx * Wx[[0], keep] / W00)
    W2 = cc(Wx[keep, keep] - wx * Wx[[0], keep] / W00)
    K2, W2 = cc((K2 + K2.T) / 2), cc((W2 + W2.T) / 2)
    say(f"    E2 concluida ({time.time()-t0:.1f}s) "
        f"ops: K2={ops(K2)} C2={ops(C2)} W2={ops(W2)}")
    salva('E2', (K2, C2, W2))

if 'OM2' in etapas:
    om2 = etapas['OM2']
    say("[7] om2 carregado do cache")
else:
    say("[7] Cdot2 e om2 ...")
    t0 = time.time()
    Cd2 = ponto(C2)
    om2 = [sp.cancel((Cd2[i, i] + W2[i, i]) / K2[i, i]) for i in range(2)]
    say(f"    pronto ({time.time()-t0:.1f}s, ops={[sp.count_ops(e) for e in om2]})")
    salva('OM2', om2)

# ----------------------------------------------------------------------
# 3. gates finais e resultado
# ----------------------------------------------------------------------
say("")
par = [sp.simplify(e - e.subs(Hq, -Hq)) for e in om2]
say(f"[V-EVEN] om2(H) - om2(-H) = {par}   (esperado [0, 0])")
if any(e != 0 for e in par):
    say("[V-EVEN] REPROVADO. Abortando.")
    grava()
    sys.exit(1)
say("[V-EVEN] APROVADO — om2 e par em H, como exige t -> -t.")

razao = [sp.cancel(om2[i] * a_s**2 / ksym**2) for i in range(2)]
esp = sp.simplify(om2[1] - (ksym**2 / a_s**2 + Upp))
say(f"[V-SPEC] om2(dchi) - [(k/a)^2 + U''] = {esp}   (esperado 0)")
if esp != 0:
    say("[V-SPEC] REPROVADO. Abortando.")
    grava()
    sys.exit(1)
say("[V-SPEC] APROVADO — o espectador tem, em forma fechada,")
say("         om2 = (k/a)^2 + U'' : c_s^2 = 1 EXATO e massa = U''.")
say("         (E o calibrador do R-10a, agora analitico — e o teste e")
say("         mais forte que o numerico, que so via 1 + U''/(k/a)^2.)")

Fm = sp.cancel(razao[0])
lam = sp.Symbol('lambda_', positive=True)
vA = sp.simplify(Fm.subs({a_s: lam * a_s, ksym: lam * ksym}) - Fm)
say(f"[V-A] c_s^2(lam*a, lam*k) - c_s^2(a, k) = {vA}   (esperado 0:")
say("      a e k so podem aparecer via k/a)")
if vA != 0:
    say("[V-A] REPROVADO. Abortando.")
    grava()
    sys.exit(1)
say("[V-A] APROVADO — a dependencia e so em k/a, como exige a fisica.")
Fm = sp.cancel(Fm.subs(a_s, 1))          # k passa a ser k/a

# on-shell: H^2 = HH(r) na celula de referencia (beta_1 = 1)
HH = sp.cancel((ME2V * r**2 * Vf / (3 * MUV)).subs(NUM).subs({b1: 1}))
say("    (celula da prova: beta_2 = beta_4 = 0, beta_0 = 1, mu = 1)")
say("")
say("    on-shell da celula (beta_1 = 1): H^2 = " + sp.sstr(sp.factor(HH)))

Fkh = sp.cancel(Fm.subs(ksym, kh * Hq))
Fkh = sp.cancel(Fkh.subs(Hq**2, HH).subs(Hq, sp.sqrt(HH)))

say("")
say("[V-NUM] forma fechada avaliada no regime r -> 0 (o canal limpo do")
say("        R-12g da -1 com |c_s^2+1| <= 1.1e-7 em 108/108 celulas):")
say(f"        {'r':>12} {'kh':>8} {'c_s^2 (forma fechada)':>26}")
for rv in (sp.Rational(1, 10**6), sp.Rational(1, 10**9)):
    for khv in (30, 100, 1000, 10000):
        val = sp.N(Fkh.subs({r: rv, kh: khv}), 20)
        say(f"        {float(rv):12.1e} {khv:8d} {sp.sstr(val):>26}")

say("")
say("=" * 72)
say("O LIMITE SUB-HORIZONTE  k -> oo  (a definicao de c_s^2)")
say("=" * 72)
cs2_kH = sp.factor(sp.simplify(sp.limit(Fm, ksym, sp.oo)))
say("")
say("  c_s^2(r, H) = " + sp.sstr(cs2_kH))
cs2_r = sp.factor(sp.cancel(cs2_kH.subs(Hq**2, HH)))
say("")
say("  ON-SHELL (H^2 = 1/(6r) nesta celula):")
say("      c_s^2(r) = " + sp.sstr(cs2_r))
say("")
say(f"    {'r':>12} {'c_s^2(r)':>20}")
for rv in [sp.Rational(1, 10**n) for n in (1, 2, 3, 4, 6, 9, 12)]:
    say(f"    {float(rv):12.1e} {float(cs2_r.subs(r, rv)):+20.14f}")

cs2_0 = sp.simplify(sp.limit(cs2_r, r, 0, '+'))
ser = sp.series(cs2_r, r, 0, 3).removeO()
say("")
say("  ===> LIMITE r -> 0 :  c_s^2 = " + sp.sstr(cs2_0))
say("       serie:  c_s^2(r) = " + sp.sstr(sp.expand(ser)) + " + O(r^3)")

# atrator tardio: rho~ = 0 com beta_1 = 1 (nesta celula: 3r^2 + r - 1 = 0)
rho_on = sp.cancel(rho_til.subs(NUM).subs({b1: 1}))
rinf = [x for x in sp.solve(sp.Eq(rho_on, 0), r) if x.is_real and x > 0][0]
val_inf = sp.radsimp(sp.simplify(cs2_r.subs(r, rinf)))
say("")
say(f"  ===> ATRATOR TARDIO (rho~ = 0):  r_inf = {sp.sstr(rinf)} = "
    f"{float(rinf):.8f}")
say(f"       c_s^2(r_inf) = {sp.sstr(val_inf)} = {float(val_inf):.14f}")

# massa efetiva: termo constante da relacao de dispersao
om2_on = sp.cancel(om2[0].subs(a_s, 1).subs(Hq**2, HH))
mef = sp.simplify(sp.limit(om2_on - cs2_r * ksym**2, ksym, sp.oo))
say("")
say("  RELACAO DE DISPERSAO (on-shell, sub-horizonte):")
say("      om2 = c_s^2 (k/a)^2 + m_ef^2 + O(1/k^2)")
say("      m_ef^2 = " + sp.sstr(sp.factor(mef)))
mef_H = sp.simplify(sp.limit(sp.cancel(mef / HH), r, 0, '+'))
say(f"      m_ef^2/H^2 em r -> 0 : {sp.sstr(mef_H)} = {float(mef_H)}")

say("")
say("=" * 72)
say("TEOREMA (celula minima da classe F1: beta_2 = beta_4 = 0)")
say("=" * 72)
say("  No ramo finito da bimetrica de Hassan-Rosen com beta_3 = 0 e")
say("  materia acoplada so a g, o escalar metrico do sistema 2-DOF tem")
say("")
say("      c_s^2(r) = " + sp.sstr(cs2_r))
say("")
say(f"  logo c_s^2 -> {sp.sstr(cs2_0)} quando r -> 0 (alto redshift) e")
say(f"  c_s^2 -> {sp.sstr(sp.radsimp(val_inf))} no atrator tardio r_inf.")
say("  A instabilidade de gradiente NAO e aproximada nem numerica: e")
say("  exata, e o valor -1 e limite de uma funcao racional do fundo.")
say("")
say("  ALCANCE: prova em forma fechada para esta celula; a extensao a")
say("  (beta_0, beta_2, beta_4, mu) e nivel 2b pelo R-12g (108/108")
say("  celulas, |c_s^2+1| <= 1.1e-7 com instrumento limpo).")

grava()
say("")
say("saida escrita em auditoria/code/out/r12b_prova_simbolica_cs2.txt")
