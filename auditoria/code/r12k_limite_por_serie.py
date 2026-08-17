# -*- coding: utf-8 -*-
"""
r12k_limite_por_serie.py — R-12(k): c_s^2(r -> 0) por SERIE TRUNCADA.

ESTADO: NAO FECHA. Preservado pelo diagnostico, nao pelo resultado.
Ver docs/resultado_r12j_generaliza_teorema.md 3. Resumo:
  * a serie e ~8x mais rapida por celula que a forma fechada, mas o
    gargalo migra da inversao 4x4 (resolvida em 2 s aqui) para as
    etapas seguintes (Cdot3, E2, Cdot2), e o calculo nao termina;
  * ACHADO QUE VALE: expandir em rho a k FIXO e o limite
    SUPER-horizonte (kh = k/(aH) -> 0 quando H ~ 1/rho -> oo) e da
    -2 na celula C1, ESTAVEL em NORD 10 e 12 — numero perfeitamente
    estavel e perfeitamente errado, pego pelo gate V-C1. O
    sub-horizonte da -1. A ordem dos limites e parte da definicao de
    c_s^2.
  * a escala CORRIGIDA (k = q/rho, com dN(q) = q g/(2 rho^2)) ja esta
    implementada abaixo.
Rotas para retomar: representacao propria de Laurent truncado
(dicionario de potencias) no lugar de expressoes sympy, e/ou eliminar
a variavel `a` explorando a homogeneidade em (a, k).

POR QUE ESTE SCRIPT EXISTE. O R-12j calcula a forma fechada exata de
c_s^2(r) e fecha em ~2 min nas celulas com beta_2 = beta_4 = 0 (C1, C2).
Nas celulas com beta_2 ou beta_4 nao nulos ele NAO fecha: a entrada
cresce 2x (ops(W): 711 -> 1245/1533) e o custo pos-inversao explode
mais de 600x (15 s -> >9500 s sem terminar). E inchaco de expressao em
aritmetica de funcoes racionais: cada complemento de Schur multiplica
os graus e o `cancel` em 4 variaveis degrada de forma superexponencial.

A CORRECAO DE METODO. Nao precisamos da funcao inteira — precisamos do
LIMITE r -> 0. Entao:

  1. TRUNCAR. Substituicao r = rho^2, H = w/rho (com w^2 = H^2 r finito
     no limite fisico), o que torna beta_1 = 3(1+mu) w^2 - beta_4 rho^6
     - 3 beta_2 rho^2 POLINOMIAL e mantem tudo racional em
     (a, k, rho, w) — sem raiz e sem extensao algebrica. Toda expressao
     e truncada como polinomio de Laurent em rho ate ordem NORD
     ABSOLUTA. O tamanho fica limitado por construcao.
  2. NAO INVERTER. A inversa 4x4 por adjugate multiplica graus (foi o
     passo de 596 s / 887 s no R-12j). Aqui resolvemos os dois sistemas
     de que a reducao precisa por ELIMINACAO DE GAUSS com truncamento a
     cada atualizacao — custo limitado, sem adjugate.
  3. PIVOTAR POR ORDEM. O pivo e a entrada de MENOR ordem em rho (a
     dominante perto de rho = 0), nao a primeira nao nula.
  4. IMPRIMIR PROGRESSO. O R-12j ficou 2h40 sem imprimir nada entre a
     inversao e o fim; aqui cada etapa reporta.

GATES (pre-declarados):
  V-C1/V-C2 : nas celulas C1 e C2 — as DUAS que ja tem forma fechada
            (R-12b/R-12j) — a serie tem de reproduzir o limite -1, e os
            coeficientes de r quando estiverem na faixa confiavel
            (C1: 2; C2: 12). Duas celulas independentes de resposta
            conhecida sao o gate. Falha => o truncamento corrompe;
            nada abaixo vale.
  LIMITES NAO COMUTAM (medido, nao suposto): expandir em rho a k FIXO e
            o limite SUPER-horizonte, pois kh = k/(aH) -> 0 quando
            H ~ 1/rho -> oo. Por isso os coeficientes de rho^2 em diante
            divergem em k -> oo, e a contaminacao NAO sobe com NORD
            (medida em rho^2 tanto para NORD=10 quanto 12). O
            coeficiente rho^0 — que e c_s^2(r -> 0), o unico que este
            script afirma — converge.
  MARGEM  : as 4 ordens mais altas de cada serie sao a camada-limite do
            truncamento e sao DESCARTADAS; so se le ate rho^(NORD-4).
            Com NORD = 8 isso entrega rho^0, rho^2 e rho^4 — exatamente
            os tres coeficientes que o V-C1 confere.
  V-ORDEM : cada celula e calculada com NORD e NORD+2. O limite (e o
            coeficiente de r) tem de coincidir. Falha => ordem
            insuficiente; reportar e nao concluir a celula.
  V-SPEC  : o espectador tem de dar om2 = (k/a)^2 + U'' na serie.

CELULAS: C1 e C2 (controles, ja tem forma fechada), C3 (beta_2 != 0),
C4 (beta_4 != 0) e CB (o BENCHMARK do R-10a/R-11, com beta_2 E beta_4
nao nulos — a celula que nunca fechou em forma fechada).

FRONTEIRA: identica ao R-12b/R-12j (classe F1, beta_3 = 0, ramo finito,
materia so como rho de fundo, sem radiacao, F' = F'' = 0).

Uso: python -u auditoria/code/r12k_limite_por_serie.py
Saida em auditoria/code/out/r12k_limite_por_serie.txt
"""
import importlib.util
import os
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
    with open(os.path.join(OUTD, 'r12k_limite_por_serie.txt'), 'w',
              encoding='utf-8') as fh:
        fh.write("\n".join(OUT) + "\n")


MULT = [0, 1, 2, 4]
DYN = [3, 5, 6]
R1 = sp.Rational
rho = sp.Symbol('rho', positive=True)      # r = rho^2
w = sp.Symbol('w', positive=True)          # H = w/rho
q = sp.Symbol('q', positive=True)          # k = q/rho  (=> kh = q/(a w))
r_de_rho = rho**2
H_de_rho = w / rho

CELULAS = [
    ('C1  b2=0     b4=0    b0=1 mu=1', R1(1), R1(0), R1(0), R1(1)),
    ('C2  b2=0     b4=0    b0=2 mu=3', R1(2), R1(0), R1(0), R1(3)),
    ('C3  b2=-2/5  b4=0    b0=1 mu=1', R1(1), R1(-2, 5), R1(0), R1(1)),
    ('C4  b2=0     b4=1/2  b0=1 mu=1', R1(1), R1(0), R1(1, 2), R1(1)),
    ('CB  b2=-2/5  b4=1/2  b0=1 mu=1 (benchmark R-10a/R-11)',
     R1(1), R1(-2, 5), R1(1, 2), R1(1)),
]
NORD_BASE = 4


# ----------------------------------------------------------------------
# aritmetica de Laurent truncada em rho
# ----------------------------------------------------------------------
def tr(e, N):
    """Trunca e como polinomio de Laurent em rho, mantendo rho^n, n <= N."""
    e = sp.cancel(sp.together(e))
    if e == 0:
        return sp.Integer(0)
    s = sp.series(e, rho, 0, N + 1)
    return sp.expand(s.removeO())


def lim_k_inf(e, var=None):
    """Limite k -> oo EXATO, por comparacao de graus em k.

    sp.limit sobre a expressao inteira devolvia 0 (ela e grande e
    multivariada); aqui o limite e tomado coeficiente a coeficiente da
    serie em rho, comparando os graus de numerador e denominador em k.
    """
    var = var if var is not None else ksym
    e = sp.cancel(sp.together(e))
    num, den = sp.fraction(e)
    if not num.has(var) and not den.has(var):
        return sp.cancel(e)
    pn = sp.Poly(sp.expand(num), var)
    pd = sp.Poly(sp.expand(den), var)
    dn, dd = pn.degree(), pd.degree()
    if dn > dd:
        return sp.nan
    if dn < dd:
        return sp.Integer(0)
    return sp.cancel(pn.LC() / pd.LC())


def coefs_rho(e, lo=-40, hi=40):
    """Dicionario {potencia de rho: coeficiente} de um Laurent."""
    e = sp.expand(e)
    if e == 0:
        return {}
    pp = sp.Poly(sp.expand(e * rho**(-lo)), rho)
    return {m[0] + lo: pp.coeff_monomial(rho**m[0]) for m in pp.monoms()}


def ordem(e):
    """Menor potencia de rho presente (ou +oo se e == 0)."""
    if e == 0:
        return sp.oo
    p = sp.Poly(sp.expand(e * rho**40), rho)
    return min(m[0] for m in p.monoms()) - 40


def solve_ser(A, B, N):
    """Resolve A X = B por Gauss-Jordan com truncamento a cada passo.

    A: n x n, B: n x m (entradas = Laurent truncados em rho).
    Pivo = entrada de MENOR ordem em rho na coluna (a dominante em
    rho -> 0), nao a primeira nao nula.
    """
    n = A.rows
    M = sp.Matrix.hstack(A.copy(), B.copy())
    for c in range(n):
        melhor, ordbest = None, sp.oo
        for lin in range(c, n):
            o = ordem(sp.cancel(M[lin, c]))
            if o < ordbest:
                melhor, ordbest = lin, o
        if melhor is None or ordbest is sp.oo:
            raise RuntimeError(f"coluna {c} singular na serie")
        if melhor != c:
            M.row_swap(c, melhor)
        piv = tr(M[c, c], N)
        pinv = tr(1 / piv, N)
        for j in range(c, M.cols):
            M[c, j] = tr(M[c, j] * pinv, N)
        for lin in range(n):
            if lin == c:
                continue
            f = M[lin, c]
            if f == 0:
                continue
            for j in range(c, M.cols):
                M[lin, j] = tr(M[lin, j] - f * M[c, j], N)
    return M[:, n:]


say("=" * 72)
say("R-12k — c_s^2(r -> 0) por serie truncada")
say("=" * 72)
say("[1] montando L2 simbolica (uma vez) ...")
L2s, fields, vels = d1.build_L2()
K7, C7, W7 = quadratic_matrices(L2s, fields, vels)
say("    pronta")


def roda(nome, B0V, B2V, B4V, MUV, N):
    ME2V = MUV / (1 + MUV)
    kap = 1 / MUV
    Vf = b4 + 3 * b2 / sp.Symbol('r_', positive=True)**2  # placeholder
    # --- fundo com beta_1 eliminado, em (rho, w) ---
    rr = sp.Symbol('r_', positive=True)
    Vf = b4 + 3 * b2 / rr**2 + b1 / rr**3
    rho_til = ((kap * b4 - 3 * b2) * rr**2 - 3 * b1 * rr
               + (3 * kap * b2 - b0) + kap * b1 / rr)
    rhop = sp.diff(rho_til, rr)                     # a beta_n FIXOS
    g_b1 = -3 * rho_til / rhop
    L_b1 = R1(1, 2) * (2 / rr + sp.diff(Vf, rr) / Vf) * g_b1
    Ub_b1 = 3 * H_s**2 - Meff2 * (b0 + 3 * b1 * rr + 3 * b2 * rr**2)
    B1_EL = sp.solve(sp.Eq(H_s**2, ME2V * rr**2 * Vf / (3 * MUV)), b1)[0]
    NUM = {b0: B0V, b2: B2V, b4: B4V, b3: 0, Mf2: MUV, Meff2: ME2V,
           Mg2: 1, m2: 1}
    PARA_RHO = {rr: r_de_rho, H_s: H_de_rho}

    def ao_rho(e):
        e = e.subs(NUM)
        e = e.subs(b1, B1_EL.subs(NUM))
        return sp.cancel(sp.together(e.subs(PARA_RHO)))

    g = ao_rho(g_b1)                 # dr/dN
    Lb = ao_rho(L_b1)                # dlnH/dN
    Ubv = ao_rho(Ub_b1)
    xiv = ao_rho(rr + g_b1)
    b1v = ao_rho(b1)

    # Variaveis (a, rho, w, q) com r = rho^2, H = w/rho, k = q/rho.
    # A escala de k com rho e ESSENCIAL: a rho fixo, kh = k/(aH) =
    # q/(a w), entao expandir em rho a q fixo e expandir a kh FIXO — o
    # regime sub-horizonte, onde c_s^2 e definido. Expandir a k fixo
    # (versao anterior deste script) e o limite SUPER-horizonte e dava
    # -2 em vez de -1 na celula C1, de forma estavel em NORD: os dois
    # limites nao comutam, e o gate V-C1 pegou.
    #   dN(rho) = g/(2 rho)
    #   dN(w)   = w L + g w/(2 rho^2)
    #   dN(q)   = q g/(2 rho^2)        [k comovel constante]
    cop_rho = sp.cancel(g / (2 * rho))
    cop_w = sp.cancel(g * w / (2 * rho**2) + w * Lb)
    cop_q = sp.cancel(q * g / (2 * rho**2))

    def dN(e, N):
        return tr(a_s * sp.diff(e, a_s) + cop_rho * sp.diff(e, rho)
                  + cop_w * sp.diff(e, w) + cop_q * sp.diff(e, q), N)

    v_b1 = tr(dN(b1v, N + 4), N + 2)
    if sp.simplify(v_b1) != 0:
        return dict(erro=f'V-B1 falhou: dN(beta_1) = {v_b1}')

    g2 = tr(sp.cancel(cop_rho * sp.diff(g, rho) + cop_w * sp.diff(g, w)),
            N + 4)
    SUB = {Fb: 1, Fp: 0, Fpp: 0, chid_s: 0, chidd_s: 0, Up: 0, rho_s: 0,
           b_s: r_de_rho * a_s, xi_s: xiv, H_s: H_de_rho,
           Hf_s: sp.cancel(H_de_rho / r_de_rho),
           Hd_s: sp.cancel(H_de_rho**2 * Lb),
           Hfd_s: sp.cancel(H_de_rho**2 * (Lb - g / r_de_rho) / r_de_rho),
           xid_s: sp.cancel(H_de_rho * (g + g2)), Ub: Ubv,
           ksym: q / rho}
    SUB.update(NUM)
    SUB[b1] = b1v

    t0 = time.time()
    K = K7.subs(SUB).applyfunc(lambda e: tr(e, N))
    C = C7.subs(SUB).applyfunc(lambda e: tr(e, N))
    W = W7.subs(SUB).applyfunc(lambda e: tr(e, N))
    say(f"      fundo substituido e truncado ({time.time()-t0:.0f}s)")
    Cd = C.applyfunc(lambda e: tr(H_de_rho * dN(e, N + 2), N))

    Kx, Cx, Wx = K.copy(), C.copy(), W.copy()
    mset = set(MULT)
    for i in MULT:
        for j in range(7):
            cd, cij = Cd[i, j], C[i, j]
            if i == j:
                Wx[i, i] = tr(Wx[i, i] + cd, N)
            elif j in mset:
                Wx[i, j] = tr(Wx[i, j] + cd, N)
            else:
                Wx[i, j] = tr(Wx[i, j] + cd, N)
                Wx[j, i] = tr(Wx[j, i] + cd, N)
                Cx[j, i] = tr(Cx[j, i] - cij, N)
        for j in range(7):
            Cx[i, j] = 0
    WXX = sp.Matrix(4, 4, lambda i, j:
                    tr((Wx[MULT[i], MULT[j]] + Wx[MULT[j], MULT[i]]) / 2, N))
    t0 = time.time()
    RHS = sp.Matrix.hstack(sp.Matrix(4, 3, lambda i, j: Cx[DYN[j], MULT[i]]),
                           sp.Matrix(4, 3, lambda i, j: Wx[MULT[i], DYN[j]]))
    Y = solve_ser(WXX, RHS, N)
    say(f"      sistema 4x4 resolvido por Gauss truncado "
        f"({time.time()-t0:.0f}s)")
    Y1, Y2 = Y[:, 0:3], Y[:, 3:6]
    CXm = sp.Matrix(3, 4, lambda i, j: Cx[DYN[i], MULT[j]])
    WDX = sp.Matrix(3, 4, lambda i, j: Wx[DYN[i], MULT[j]])
    K3 = sp.Matrix(3, 3, lambda i, j: tr(
        Kx[DYN[i], DYN[j]] + (CXm * Y1)[i, j], N))
    C3 = sp.Matrix(3, 3, lambda i, j: tr(
        Cx[DYN[i], DYN[j]] - (CXm * Y2)[i, j], N))
    W3 = sp.Matrix(3, 3, lambda i, j: tr(
        Wx[DYN[i], DYN[j]] - (WDX * Y2)[i, j], N))
    ordK3 = [ordem(K3[0, j]) for j in range(3)]
    say(f"      [V-K3] ordem em rho da linha 0 de K3: {ordK3}"
        f"  (nula em forma fechada; na serie truncada aparece so o"
        f" residuo do corte)")
    for j in range(3):
        K3[0, j] = 0
        K3[j, 0] = 0
    Cd3 = C3.applyfunc(lambda e: tr(H_de_rho * dN(e, N + 2), N))

    Kx, Cx, Wx = K3.copy(), C3.copy(), W3.copy()
    for j in range(3):
        cij, cd = C3[0, j], Cd3[0, j]
        if j == 0:
            Wx[0, 0] = tr(Wx[0, 0] + cd, N)
        else:
            Wx[0, j] = tr(Wx[0, j] + cd, N)
            Wx[j, 0] = tr(Wx[j, 0] + cd, N)
            Cx[j, 0] = tr(Cx[j, 0] - cij, N)
    for j in range(3):
        Cx[0, j] = 0
    W00 = tr(Wx[0, 0], N)
    W00i = tr(1 / W00, N)
    keep = [1, 2]
    K2 = sp.Matrix(2, 2, lambda i, j: tr(
        Kx[keep[i], keep[j]] + Cx[keep[i], 0] * Cx[keep[j], 0] * W00i, N))
    C2 = sp.Matrix(2, 2, lambda i, j: tr(
        Cx[keep[i], keep[j]] - Cx[keep[i], 0] * Wx[0, keep[j]] * W00i, N))
    W2 = sp.Matrix(2, 2, lambda i, j: tr(
        Wx[keep[i], keep[j]] - Wx[keep[i], 0] * Wx[0, keep[j]] * W00i, N))
    Cd2 = C2.applyfunc(lambda e: tr(H_de_rho * dN(e, N + 2), N))
    om2 = [tr(sp.cancel((Cd2[i, i] + W2[i, i]) / K2[i, i]), N)
           for i in range(2)]

    esp_c = coefs_rho(sp.cancel(om2[1].subs(a_s, 1)
                                - (q**2 / rho**2 + Upp)))
    esp = {n: c for n, c in esp_c.items() if sp.simplify(c) != 0}
    if esp:
        return dict(erro=f'V-SPEC falhou (residuo em rho^{sorted(esp)})')

    Fm = sp.cancel(om2[0].subs(a_s, 1) * rho**2 / q**2)   # om2/(k/a)^2
    # limite k -> oo COEFICIENTE A COEFICIENTE da serie em rho.
    # As MARGEM ordens mais altas sao a camada-limite do truncamento (os
    # termos que as cancelariam foram cortados); descartadas por
    # construcao. So se exige convergencia ate rho^(N - MARGEM).
    # A camada-limite do truncamento nao tem largura fixa (medida:
    # desce ate rho^(N-4)). Em vez de adivinhar a margem, DETECTA-SE:
    # coeficiente que diverge em k -> oo esta contaminado e e
    # descartado; quem decide o que e confiavel e o gate V-ORDEM, que
    # compara NORD com NORD+2.
    coef, descartados = {}, []
    for n, c in sorted(coefs_rho(Fm).items()):
        lc = lim_k_inf(c, q)
        if lc is sp.nan:
            descartados.append(n)
            continue
        if sp.simplify(lc) != 0:
            coef[n] = sp.cancel(lc)
    n_ok = min(descartados) - 1 if descartados else N
    if n_ok < 0:
        return dict(erro=f'nem o coeficiente rho^0 converge em k -> oo'
                         f' (contaminacao desde rho^{min(descartados)})')
    coef = {n: c for n, c in coef.items() if n <= n_ok}
    cs2 = sum(c * rho**n for n, c in coef.items())
    neg = {n: c for n, c in coef.items() if n < 0}
    return dict(erro=None, cs2=cs2, c0=sp.simplify(coef.get(0, 0)),
                c2=(sp.simplify(coef.get(2, 0)) if n_ok >= 2 else None),
                c4=(sp.simplify(coef.get(4, 0)) if n_ok >= 4 else None),
                n_ok=n_ok, neg=neg)


ALVO_C1 = {0: sp.Integer(-1), 2: sp.Integer(2), 4: R1(39, 2)}
res = {}
for nome, B0V, B2V, B4V, MUV in CELULAS:
    say("")
    say("=" * 72)
    say(f"CELULA {nome}")
    say("=" * 72)
    saidas = {}
    for N in (NORD_BASE, NORD_BASE + 2):
        t0 = time.time()
        say(f"    -- NORD = {N}")
        try:
            o = roda(nome, B0V, B2V, B4V, MUV, N)
        except Exception as e:                             # noqa: BLE001
            say(f"       EXCECAO: {type(e).__name__}: {str(e)[:110]}")
            grava()
            o = dict(erro='excecao')
        if o.get('erro'):
            say(f"       {o['erro']}")
            continue
        ext = ""
        if o['c2'] is not None:
            ext = f" + ({sp.sstr(o['c2'])}) r"
        if o['c4'] is not None:
            ext += f" + ({sp.sstr(o['c4'])}) r^2"
        say(f"       c_s^2(r -> 0) = {sp.sstr(o['c0'])}{ext}"
            f"   [confiavel ate rho^{o['n_ok']}; {time.time()-t0:.0f}s]")
        if o['neg']:
            say(f"       ATENCAO: potencias negativas de rho sobraram:"
                f" {sorted(o['neg'])} — o limite nao e finito nesta ordem")
        saidas[N] = o
        grava()
    if len(saidas) == 2:
        a1, a2 = saidas[NORD_BASE], saidas[NORD_BASE + 2]
        est = sp.simplify(a1['c0'] - a2['c0']) == 0
        if a1['c2'] is not None and a2['c2'] is not None:
            est = est and sp.simplify(a1['c2'] - a2['c2']) == 0
        say(f"    [V-ORDEM] limite e coef. de r estaveis entre NORD"
            f" {NORD_BASE} e {NORD_BASE+2}: {'SIM' if est else 'NAO'}")
        if est:
            res[nome] = a2
        else:
            say("       -> ordem insuficiente; celula NAO concluida")
    else:
        say("    [V-ORDEM] nao ha as duas ordens; celula NAO concluida")
    if nome.startswith('C2') and nome in res:
        o = res[nome]
        ok2 = sp.simplify(o['c0'] + 1) == 0
        say(f"    [V-C2] limite -1 da forma fechada do R-12j: "
            f"{'SIM' if ok2 else 'NAO'}")
        if not ok2:
            say("    [V-C2] REPROVADO. Abortando.")
            grava()
            sys.exit(1)
    if nome.startswith('C1') and nome in res:
        o = res[nome]
        pares = [('c0', 0)]
        if o['c2'] is not None:
            pares.append(('c2', 2))
        if o['c4'] is not None:
            pares.append(('c4', 4))
        ok = all(sp.simplify(o[kk] - ALVO_C1[nn]) == 0 for kk, nn in pares)
        say(f"    [V-C1] reproduz {len(pares)} coeficiente(s) de"
            f" -1 + 2r + (39/2) r^2 do R-12b: {'SIM' if ok else 'NAO'}")
        if not ok:
            say("    [V-C1] REPROVADO — o truncamento corrompe o")
            say("           resultado; nada abaixo vale. Abortando.")
            grava()
            sys.exit(1)
    grava()

say("")
say("=" * 72)
say("VEREDITO R-12k")
say("=" * 72)
say(f"  celulas concluidas: {len(res)}/{len(CELULAS)}")
if res:
    say("")
    say(f"  {'celula':<52} {'c_s^2(r->0)':>12} {'coef. de r':>14}")
    for nome, o in res.items():
        say(f"  {nome:<52} {sp.sstr(o['c0']):>12} {sp.sstr(o['c2']):>14}")
    todos = all(sp.simplify(o['c0'] + 1) == 0 for o in res.values())
    say("")
    if todos:
        say("  ===> c_s^2(r -> 0) = -1 em TODAS as celulas concluidas.")
        say("       O coeficiente de r DIFERE entre celulas (como tem de")
        say("       ser: a trajetoria r(a) depende dos beta_n); o que e")
        say("       universal e o LIMITE.")
    else:
        say("  ===> ATENCAO: nem todas dao -1 — reportar a dependencia.")
grava()
say("")
say("saida escrita em auditoria/code/out/r12k_limite_por_serie.txt")
