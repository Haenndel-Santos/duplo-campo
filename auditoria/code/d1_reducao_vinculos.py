# -*- coding: utf-8 -*-
"""
d1_reducao_vinculos.py — Item D1 do posicionamento na literatura
(docs/posicionamento_literatura.md secao 2): o par escalar doente
SOBREVIVE a reducao explicita de vinculos?

POR QUE ISTO E CRITICO. Nosso no-go tardio (taquiao sigma/H ~ 3.65 no
ponto fixo; fantasma de norma quase nula na fresta mu=0.1) contradiz o
quadro publicado ("instavel cedo, saudavel tarde" — Comelli et al.
1202.1986/1403.5679; Konnig et al. 1407.4331). As analises publicadas
INTEGRAM lapso/shift para fora antes de diagnosticar; nosso QEP mantem
os 7 campos e filtra vinculos como autovalores infinitos. O referee
vai perguntar: os modos patologicos (com norma quase nula e suporte
nos multiplicadores) sobrevivem a reducao explicita, ou sao artefato
de nao te-la feito?

METODO. A biblioteca ja tem a maquinaria: faddeev_jackiw_reduce
(tdcp_pert_lib) — reducao iterativa (integracao por partes nas linhas
sem cinetica; eliminacao de auxiliares por complemento de Schur;
mudanca de base nas direcoes nulas de K) ate K nao-singular. Ela foi
abandonada na D1-v4 porque explodia com k SIMBOLICO; aqui rodamos com
FUNDO RACIONALIZADO (30 digitos, cubica resolvida por nroots(35)) e k
NUMERICO — algebra linear exata em racionais, sem explosao. No ponto
fixo o fundo e exatamente quase-de Sitter (congelamento exato — o juiz
estabelecido do projeto), entao coeficientes numericos constantes sao
legitimos, nao aproximacao extra.

O QUE O SCRIPT FAZ:
  V1 (ancora GR, poder de detecao): GR+chi em gauge plano pela MESMA
      rota FJ — tem de reduzir a exatamente 1 modo (dchi), K_red > 0,
      omega^2 batendo com os valores do gr_selfcheck do QEP
      (1.7119 em k=1; 100.7119 em k=10... valores da rota QEP).
  Para cada celula {REF mu=1 (taquiao), fresta mu=0.1 (fantasma
  quase-nulo)} x k in {1, 10}, no ponto fixo a=10:
  1. substitui o fundo exato nas K7/C7/W7 e roda a reducao FJ completa
     (log impresso: quem foi eliminado em qual rodada);
  2. reporta: CONTAGEM final de modos dinamicos; AUTOVALORES de K_red
     (assinatura = diagnostico de fantasma inequivoco, sem norma de
     autovetor QEP); espectro do sistema reduzido (omega^2, sigma/H);
  3. CONFRONTA com o espectro finito do QEP 7x7 no mesmo ponto
     (mesma fisica => tem de bater modo a modo).

CRITERIOS PRE-DECLARADOS:
  D1-GR: reducao GR da 1 modo, c_s^2 ~ 1 (omega^2 bate com QEP), K>0.
  D1-CONTAGEM: dim(K_red) == numero de pares finitos do QEP (3) em
      cada ponto. Se der MENOS, a contagem do QEP estava contaminada
      por modo de vinculo — reporta-se qual sobrevive e o no-go tardio
      E REESCRITO com o que sobrar (sem maquiagem).
  D1-ESPECTRO: omega^2 reduzido == omega^2 finito do QEP (rel. 1e-6).
  D1-ASSINATURA: autovalores de K_red — negativo = fantasma confirmado
      POS-reducao (o teste que a norma QEP nao dava com invariancia).
  VEREDITO "PAR SOBREVIVE" se contagem e espectro conferem E o taquiao
      (omega^2 < 0) persiste no sistema reduzido (e o fantasma da
      fresta persiste como autovalor negativo de K_red). Nesse caso o
      no-go tardio fica referee-proof: o diagnostico passa a viver no
      sistema fisico explicitamente reduzido. QUALQUER desvio e
      reportado como esta, e o enunciado do paper se ajusta ao achado.

Se a reducao abortar com "W_XX singular com acoplamento a Q"
(constraint secundaria na rodada de Schur), isso e reportado como
achado estrutural — significa que a eliminacao simples nao fecha e a
extensao (resolver a secundaria) vira o proximo passo.

Requer sympy, numpy, scipy. ~2-5 min (reducao exata em racionais).
Uso (raiz do repo, venv ativo):
    python auditoria/code/d1_reducao_vinculos.py
Saida em auditoria/code/out/d1_reducao_vinculos.txt
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
                           quadratic_matrices, faddeev_jackiw_reduce,
                           lagrangian_GG, chi_lagrangian, scalar_metric_g,
                           substitute_bg_functions, make_bg_functions,
                           z_average, eps_part, cut, symbolize)

T0 = time.time()
OUT = []


def say(*a):
    line = " ".join(str(x) for x in a)
    print(f"[{time.time()-T0:7.1f}s] {line}")
    OUT.append(line)


NOMES = ['Phi_g', 'B_g', 'Phi_f', 'Psi_f', 'B_f', 'E_f', 'dchi']
RHO0 = sp.Rational(3, 10)
CHOP = 1e-18

say("=" * 72)
say("D1 — REDUCAO EXPLICITA DE VINCULOS: o par doente sobrevive?")
say("=" * 72)


def rac(x, nd=30):
    """racionaliza um numero sympy a nd digitos (com guarda de imaginario)."""
    xN = sp.N(x, nd)
    if abs(sp.im(xN)) > sp.Float(f'1e-{nd-5}'):
        raise RuntimeError(f"valor complexo inesperado: {xN}")
    return sp.Rational(sp.re(xN))


def espectro_reduzido(Kr, Cr, Wr, H_val):
    """espectro do sistema reduzido (K invertivel) + assinatura de K."""
    n = Kr.shape[0]
    Kn = np.array([[float(sp.N(Kr[i, j], 20)) for j in range(n)]
                   for i in range(n)])
    Cn = np.array([[float(sp.N(Cr[i, j], 20)) for j in range(n)]
                   for i in range(n)])
    Wn = np.array([[float(sp.N(Wr[i, j], 20)) for j in range(n)]
                   for i in range(n)])
    Ksym = 0.5 * (Kn + Kn.T)
    eigK = np.sort(np.linalg.eigvalsh(Ksym))
    pares = d1.agrupa_pares(d1.qep_modes(Kn, Cn, Wn))
    pares.sort(key=lambda m: abs(m['omega2']))
    esp = []
    for mm in pares:
        w2 = mm['omega2']
        om = np.sqrt(complex(w2))
        esp.append(dict(w2=w2, taxa=abs(om.imag) / H_val, kN=mm['knorm']))
    return esp, eigK


# ------------------------------------------------------------------
# V1 — ancora GR pela rota FJ
# ------------------------------------------------------------------
say("")
say("V1 — ancora GR (EH_g + chi, gauge plano) pela rota de REDUCAO")
Phi_gF = sp.Function('Phi_g')(t)
B_gF = sp.Function('B_g')(t)
dchiF = sp.Function('dchi')(t)
funcs = [Phi_gF, B_gF, dchiF]
aF, bF, xiF, bg_rules = make_bg_functions()
g_gr = substitute_bg_functions(
    scalar_metric_g(Phi_gF, sp.Integer(0), B_gF, None), aF, bF, xiF)
L2_gr = z_average(eps_part(cut(lagrangian_GG(g_gr, Mg2)
                               + chi_lagrangian(g_gr, dchi=dchiF)), 2))
L2s_gr, f_gr, v_gr = symbolize(L2_gr, funcs, bg_rules)
vgr = {Mg2: 1, a_s: 1, H_s: 1, chid_s: sp.Rational(3, 10),
       Up: sp.Rational(-1, 5), Upp: sp.Rational(3, 10), rho_s: 0,
       Ub: 3 - sp.Rational(9, 200), Hd_s: -sp.Rational(9, 200)}
vgr[chidd_s] = -3 * vgr[H_s] * vgr[chid_s] - vgr[Up]
Kg, Cg, Wg = quadratic_matrices(sp.expand(L2s_gr.subs(vgr)), f_gr, v_gr)

ok_v1 = True
ALVOS_GR = {1.0: 1.7119, 10.0: 100.7119}
for kv in (1.0, 10.0):
    sub = {ksym: sp.Rational(kv)}
    try:
        Kr, Cr, Wr, nm = faddeev_jackiw_reduce(
            Kg.subs(sub), Cg.subs(sub), Wg.subs(sub),
            [str(f) for f in f_gr], kref=kv, verbose=False, log=say)
    except Exception as e:
        say(f"    k={kv:g}: reducao GR FALHOU: {e}")
        ok_v1 = False
        continue
    esp, eigK = espectro_reduzido(Kr, Cr, Wr, 1.0)
    w2s = [round(m['w2'].real, 4) for m in esp]
    say(f"    k={kv:g}: {len(nm)} modo(s) {nm}; K_red eig={eigK}; "
        f"w2={w2s} (alvo QEP {ALVOS_GR[kv]})")
    ok_v1 = (ok_v1 and len(nm) == 1 and eigK[0] > 0
             and abs(esp[0]['w2'].real - ALVOS_GR[kv]) < 0.01 * ALVOS_GR[kv])
say(f"  [D1-GR {'PASSA' if ok_v1 else 'FALHA — abortar leitura'}]")
if not ok_v1:
    sys.exit(1)

# ------------------------------------------------------------------
# montagem bimetrica completa
# ------------------------------------------------------------------
L2s, fields, vels = d1.build_L2()
K7, C7, W7 = quadratic_matrices(L2s, fields, vels)
if [str(f) for f in fields] != NOMES:
    raise RuntimeError("ordem de campos mudou")
say("[montagem] K,C,W 7x7 prontos")


def fundo_a10_exato(B1e, B2v, B0v, B4v, mu):
    """ponto fixo a=10 em aritmetica exata (30 digitos), espelhando
    fundo_a10 dos scripts anteriores (mesmo truque: materia em Ub)."""
    B1e, B2v, B0v, B4v, mu = [sp.nsimplify(x) for x in
                              (B1e, B2v, B0v, B4v, mu)]
    kap = 1 / mu
    meff2 = mu / (1 + mu)
    a = sp.Integer(10)
    rho_til = RHO0 * a**-3 / meff2
    rr = sp.Symbol('rr')
    poly = sp.Poly((kap * B4v - 3 * B2v) * rr**3 - 3 * B1e * rr**2
                   + (3 * kap * B2v - B0v - rho_til) * rr + kap * B1e, rr)
    reais = [z for z in poly.nroots(n=35)
             if abs(sp.im(z)) < 1e-30 and sp.re(z) > 1e-12]
    if not reais:
        raise RuntimeError("cubica sem raiz positiva")
    r = sp.re(min(reais, key=lambda z: sp.re(z)))
    dW = kap * (2 * B4v * r - B1e / r**2) - 3 * B1e - 6 * B2v * r
    drdN = -3 * rho_til / dW
    xi = r + drdN
    Vf = B4v + 3 * B2v / r**2 + B1e / r**3
    H2 = meff2 * r * r * Vf / (3 * mu)
    if not (H2 > 0 and xi > 0):
        raise RuntimeError("fundo invalido")
    H = sp.sqrt(H2)
    rho_int = meff2 * (B0v + 3 * B1e * r + 3 * B2v * r**2)
    Ubv = 3 * H2 - rho_int          # materia absorvida em Ub (truque padrao)
    vals = {a_s: sp.Integer(1), b_s: rac(r), xi_s: rac(xi),
            H_s: rac(H), Hf_s: rac(H / r), Ub: rac(Ubv),
            Mg2: 1, Mf2: sp.nsimplify(mu), m2: 1,
            Meff2: sp.nsimplify(meff2),
            b0: B0v, b1: B1e, b2: B2v, b3: 0, b4: B4v,
            Fb: 1, Fp: 0, Fpp: 0,
            chid_s: 0, chidd_s: 0, rho_s: 0,
            Hd_s: 0, Hfd_s: 0, xid_s: 0,
            Up: 0, Upp: sp.Rational(3, 10)}
    return vals, float(r), float(xi), float(H)


CELULAS = [
    ("REF mu=1 (taquiao)", 1.0, -0.4, 1.0, 0.5, 1.0,
     {1.0: 3.651, 10.0: 3.740}),          # sigma/H esperado (ancoras QEP)
    ("fresta mu=0.1 (fantasma quase-nulo)", 0.2, -1.0, 1.0, 0.5, 0.1,
     {1.0: 0.0, 10.0: 0.0}),
]

resultados = []
for rotulo, B1v, B2v, B0v, B4v, mu, anc in CELULAS:
    vals, rv, xv, Hv = fundo_a10_exato(B1v, B2v, B0v, B4v, mu)
    say("")
    say("=" * 72)
    say(f"CELULA: {rotulo}  (r={rv:.6f}, xi={xv:.6f}, H={Hv:.6f})")
    say("=" * 72)
    for kv in (1.0, 10.0):
        say("")
        say(f"--- k = {kv:g} ---")
        sub = dict(vals)
        sub[ksym] = sp.Rational(kv)
        say("    substituindo fundo exato nas 7x7 ...")
        Kn7 = K7.subs(sub)
        Cn7 = C7.subs(sub)
        Wn7 = W7.subs(sub)
        # referencia QEP no MESMO ponto (rota estabelecida)
        Kf = np.array([[float(sp.N(Kn7[i, j], 20)) for j in range(7)]
                       for i in range(7)])
        Cf = np.array([[float(sp.N(Cn7[i, j], 20)) for j in range(7)]
                       for i in range(7)])
        Wf = np.array([[float(sp.N(Wn7[i, j], 20)) for j in range(7)]
                       for i in range(7)])
        pares_qep = d1.agrupa_pares(d1.qep_modes(Kf, Cf, Wf))
        pares_qep.sort(key=lambda m: abs(m['omega2']))
        w2_qep = sorted([m['omega2'].real for m in pares_qep])
        say(f"    QEP 7x7 (referencia): {len(pares_qep)} pares; "
            f"w2 = {[f'{x:+.4e}' for x in w2_qep]}")
        # reducao FJ exata
        say("    reducao Faddeev-Jackiw (exata, racionais) ...")
        try:
            Kr, Cr, Wr, nomes_red = faddeev_jackiw_reduce(
                Kn7, Cn7, Wn7, list(NOMES), kref=kv,
                verbose=True, log=say, chop_tol=CHOP)
        except Exception as e:
            say(f"    !! REDUCAO ABORTOU: {type(e).__name__}: {e}")
            say("    -> achado estrutural (constraint secundaria ou")
            say("       degenerescencia nao tratada); registrar e iterar.")
            resultados.append(dict(rotulo=rotulo, k=kv, status='abort',
                                   erro=str(e)))
            continue
        esp, eigK = espectro_reduzido(Kr, Cr, Wr, Hv)
        w2_red = sorted([m['w2'].real for m in esp])
        say(f"    REDUZIDO: {len(nomes_red)} modo(s) fisicos: {nomes_red}")
        say(f"    autovalores de K_red (assinatura): "
            f"{[f'{x:+.3e}' for x in eigK]}")
        for mm in esp:
            w2 = mm['w2']
            say(f"      w2={w2.real:+.4e}"
                f"{'' if abs(w2.imag) < 1e-6*max(1.0, abs(w2.real)) else f' {w2.imag:+.2e}i'}"
                f"  sigma/H={mm['taxa']:.4f}  kN_red={mm['kN']:+.3e}")
        # confronto de espectros
        casa = (len(w2_red) == len(w2_qep)
                and all(abs(x - y) <= 1e-6 * max(1.0, abs(x), abs(y))
                        for x, y in zip(w2_red, w2_qep)))
        say(f"    espectro reduzido == QEP? {'SIM' if casa else 'NAO'}")
        sig_max = max((m['taxa'] for m in esp), default=0.0)
        n_neg = int(np.sum(eigK < -1e-15))
        resultados.append(dict(rotulo=rotulo, k=kv, status='ok',
                               n_red=len(nomes_red), n_qep=len(pares_qep),
                               casa=casa, sig=sig_max, negK=n_neg,
                               anc=anc[kv], eigK=eigK))

# ------------------------------------------------------------------
# veredito
# ------------------------------------------------------------------
say("")
say("=" * 72)
say("VEREDITO D1 (criterios pre-declarados)")
say("=" * 72)
oks = [r for r in resultados if r['status'] == 'ok']
aborts = [r for r in resultados if r['status'] == 'abort']
if aborts:
    say(f"  {len(aborts)} ponto(s) com reducao abortada — achado estrutural;")
    for r in aborts:
        say(f"    {r['rotulo']}, k={r['k']}: {r['erro'][:80]}")
cont_ok = all(r['n_red'] == r['n_qep'] for r in oks) and oks
esp_ok = all(r['casa'] for r in oks) and oks
say(f"  D1-CONTAGEM: {'PASSA' if cont_ok else 'FALHA'} — "
    + "; ".join(f"{r['rotulo'].split()[0]} k={r['k']:g}: "
                f"{r['n_red']} red vs {r['n_qep']} QEP" for r in oks))
say(f"  D1-ESPECTRO: {'PASSA' if esp_ok else 'FALHA'} — espectros "
    f"{'conferem' if esp_ok else 'DIVERGEM'} modo a modo")
taq = [r for r in oks if 'taquiao' in r['rotulo'] and r['sig'] > 0.05]
if taq:
    det = ", ".join(f"sigma/H={r['sig']:.3f} em k={r['k']:g} "
                    f"(ancora QEP {r['anc']:.3f})" for r in taq)
    say(f"  taquiao no sistema REDUZIDO: SIM — {det}")
else:
    say("  taquiao no sistema REDUZIDO: NAO")
fant = [r for r in oks if 'fantasma' in r['rotulo'] and r['negK'] > 0]
if fant:
    det = ", ".join(f"k={r['k']:g}: {r['negK']} direcao(oes) negativa(s)"
                    for r in fant)
    say(f"  fantasma (autovalor NEGATIVO de K_red) na fresta: SIM — {det}")
else:
    say("  fantasma (autovalor NEGATIVO de K_red) na fresta: NAO")
say("")
if oks and cont_ok and esp_ok and taq:
    say("  >>> O PAR SOBREVIVE A REDUCAO. O espectro do QEP e identico ao")
    say("  do sistema fisico explicitamente reduzido, o taquiao persiste")
    say("  com a mesma taxa, e a assinatura de K_red da o diagnostico de")
    say("  fantasma sem ambiguidade de norma. O no-go tardio fica")
    say("  referee-proof nesta frente (D1 do posicionamento resolvido a")
    say("  favor); a comparacao com a instabilidade de gradiente da")
    say("  literatura (D2) e o proximo item.")
elif oks:
    say("  >>> A REDUCAO MUDOU O QUADRO — reportar exatamente o que mudou")
    say("  (contagem, espectro ou desaparecimento de modo doente) e")
    say("  REESCREVER o enunciado tardio do no-go com o que sobrou.")
    say("  Este resultado teria sido apontado pelo referee; melhor agora.")
else:
    say("  >>> nenhum ponto completou — analisar os aborts antes de")
    say("  qualquer leitura.")

os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
with open(os.path.join(HERE, "out", "d1_reducao_vinculos.txt"),
          "w", encoding="utf-8") as fh:
    fh.write("\n".join(OUT))
say("")
say("concluido. saida em auditoria/code/out/d1_reducao_vinculos.txt")
