# -*- coding: utf-8 -*-
"""
stuckelberg_goldstone.py — C1 da fila: derivacao de Stueckelberg in-repo
(docs/gate1c_nota_trilema.md secao 7).

OBJETIVO. A nota do trilema (G1-c) apoia a "circularidade HR-Goldstone"
em duas premissas: (1) o helicity-0 e o setor de Goldstone das difeos
RELATIVAS quebradas pelo termo de interacao [nivel 3 — estrutura padrao
da EFT de gravidade massiva, NAO derivada in-repo]; (2) os autovetores
patologicos medidos vivem no setor de vinculos [nivel 2b —
estrutura_par_relativo.md]. Este script deriva (1) DENTRO do repo e
adiciona um teste novo (origem da massa), com o objetivo declarado de
subir a premissa estrutural a nivel 2a — ou enfraquece-la
(gate1c secao 8(i)).

O QUE O SCRIPT FAZ:

PARTE A (simbolica; alvo nivel 2a):
  A1. Deriva os vetores de orbita das difeos relativas no setor escalar:
      com o gauge plano fixado no setor g (a escolha da biblioteca), as
      transformacoes relativas podem ser representadas agindo so em f
      (modulo o subgrupo diagonal, ja fixado). Para
      eps^0 = T(t) cos kz, eps^z = Z(t) sin kz, a derivada de Lie do
      fundo f da o deslocamento em espaco de campos:
          dPhi_f = -Tdot - (xidot/xi) T
          dPsi_f = xi H_f T
          dB_f   = (xi/b) T + b Zdot/(xi k)
          dE_f   = Z/k
      DUAS ROTAS: derivada de Lie automatizada (rota 1) casada contra a
      parametrizacao da PROPRIA biblioteca (scalar_metric_f), vs as
      formulas fechadas acima (rota 2). Mais CONTROLE NEGATIVO (formula
      deliberadamente errada tem de FALHAR o casamento) — poder de
      detecao, regra do projeto.
  A2. Asserts estruturais: K7 e C7 NAO contem Fb/Fp/Fpp (o termo de
      quebra e NAO-DERIVATIVO => entra puramente como potencial W).
      Consequencia 2a imediata: doenca CINETICA (fantasma) nao pode vir
      diretamente do termo de quebra; doenca de MASSA (taquiao) pode.
  A3. Os 4 vetores de orbita geram todo o bloco-f {Phi_f,Psi_f,B_f,E_f}
      (det != 0 nos fundos avaliados) — no gauge plano-g, o setor de
      Goldstone das difeos relativas E o bloco-f inteiro; o espaco de
      campos fatora em {multiplicadores-g} + {orbitas de Goldstone} +
      {dchi}. Combinado com o G1-b (projecao dchi = 0), segue de
      DERIVACAO que os modos patologicos vivem no setor
      {Goldstone + multiplicadores}.

PARTE B (numerica; nivel 2b) — nos MESMOS fundos do G1-b
(ponto fixo a=10; celulas REF mu={0.3,1,3,10} e fresta mu=0.1; k=1 e 10):
  B1. Para cada modo do QEP: pesos por bloco (orbita-f / multiplicadores
      / dchi) e DECOMPOSICAO DE GOLDSTONE exata — coordenadas do
      autovetor na base (nao-ortogonal, unit-normalizada) dos 4 vetores
      de orbita: (T, Tdot) = pi0 (Goldstone temporal), (Z, Zdot) = piL
      (Goldstone longitudinal — o helicity-0 "classico" do gravitao
      massivo). Identifica QUAL Goldstone e o modo doente.
  B2. ORIGEM DA MASSA (teste novo): decompoe v†Wv = v†W_EH v + v†W_int v
      (fatia Fb, mesma tecnica validada pelo T1 de modulacao_qep.py) e
      reporta rI = |v†W_int v| / (|v†W_int v| + |v†W_EH v|) por modo.
      Taquiao com rI alto = pseudo-Goldstone que ganha massa (de sinal
      errado) do termo de quebra — o padrao textbook.

CRITERIOS PRE-DECLARADOS:
  C1 (2a): rota1 == rota2, controle negativo falha como esperado,
      K_int = C_int = 0 simbolico, det(orbita) != 0 em todos os fundos.
  C2 (2b): todo modo patologico com peso >= 0.95 em
      {orbita-f + multiplicadores} (equivalente a dchi <= 0.05 — o G1-b
      reafirmado nesta rota).
  C3 (2b): todo modo TAQUIONICO com rI >= 0.5 (o potencial que o modo
      sente e dominado pelo termo de quebra).
  VEREDITO: C1 e C2 e C3 => CONFIRMA — a premissa estrutural da
      circularidade sobe a 2a, com composicao e origem em 2b; os modos
      doentes sao pseudo-Goldstones das difeos relativas, identificados.
      C3 falhar => ENFRAQUECE (gate1c secao 8(i)) — reportar os numeros.
      Fantasmas: rI reportado como diagnostico; leitura adiada (K_int=0
      ja diz que a doenca cinetica nao vem diretamente da quebra).

CONTINUIDADE (ancoras): sigma/H = 3.651 na REF mu=1 k=1;
kN = -1.6e-5 na fresta mu=0.1 k=1. Reproduzir ambas ou abortar.

Requer sympy, numpy, scipy. ~3-5 min (montagem simbolica + asserts).
Uso (raiz do repo, venv ativo):
    python auditoria/code/stuckelberg_goldstone.py
Saida em auditoria/code/out/stuckelberg_goldstone.txt
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

from tdcp_pert_lib import (t, z, a_s, b_s, xi_s, H_s, Hf_s, Hd_s, Hfd_s,
                           xid_s, chid_s, chidd_s, Mg2, Mf2, m2, Meff2,
                           b0, b1, b2, b3, b4, Fb, Fp, Fpp,
                           Ub, Up, Upp, rho_s, k as ksym, eps,
                           eps_part, scalar_metric_f, quadratic_matrices)

T0 = time.time()
OUT = []


def say(*a):
    line = " ".join(str(x) for x in a)
    print(f"[{time.time()-T0:7.1f}s] {line}")
    OUT.append(line)


NOMES = ['Phi_g', 'B_g', 'Phi_f', 'Psi_f', 'B_f', 'E_f', 'dchi']
IDX_F = [2, 3, 4, 5]          # bloco-f (Phi_f, Psi_f, B_f, E_f)
IDX_MULT = [0, 1]             # multiplicadores do setor g
IDX_DCHI = 6
TOL_SIG = 0.05
TOL_KN = 1e-9

say("=" * 72)
say("STUCKELBERG / GOLDSTONE — C1 da fila (gate1c secao 7)")
say("=" * 72)

# ------------------------------------------------------------------
# montagem (mesma maquinaria de todas as ancoras)
# ------------------------------------------------------------------
gr_ok = d1.gr_selfcheck()
if not gr_ok:
    say("[!] auto-teste GR falhou — abortando")
    sys.exit(1)

L2s, fields, vels = d1.build_L2()
K7, C7, W7 = quadratic_matrices(L2s, fields, vels)
nomes_reais = [str(f) for f in fields]
if nomes_reais != NOMES:
    raise RuntimeError(f"ordem de campos mudou: {nomes_reais}")
say(f"[montagem] K,C,W 7x7 prontos; campos: {NOMES}")

# ==================================================================
# PARTE A — simbolica
# ==================================================================
say("")
say("-" * 72)
say("PARTE A — derivacao simbolica do setor de Goldstone (alvo: 2a)")
say("-" * 72)

# ---------- A1: vetores de orbita por derivada de Lie ----------
say("")
say("A1. vetores de orbita das difeos relativas (duas rotas + controle)")

Tsym, Tdsym, Zsym, Zdsym = sp.symbols('T Tdot Zpar Zdot')

# rota 1: derivada de Lie do fundo f, automatizada
xF = sp.Function('xiBG', positive=True)(t)
bF = sp.Function('bBG', positive=True)(t)
TF = sp.Function('TF')(t)
ZF = sp.Function('ZF')(t)
xcoord, ycoord = sp.symbols('x y')
COORDS4 = (t, xcoord, ycoord, z)
cz, sz = sp.cos(ksym * z), sp.sin(ksym * z)

fbar = sp.diag(-xF**2, bF**2, bF**2, bF**2)
epsvec = [TF * cz, sp.Integer(0), sp.Integer(0), ZF * sz]

Lie = sp.zeros(4, 4)
for mu in range(4):
    for nu in range(4):
        e = sum(epsvec[al] * sp.diff(fbar[mu, nu], COORDS4[al])
                for al in range(4))
        e += sum(fbar[al, nu] * sp.diff(epsvec[al], COORDS4[mu])
                 + fbar[mu, al] * sp.diff(epsvec[al], COORDS4[nu])
                 for al in range(4))
        Lie[mu, nu] = sp.expand(e)
delta_f = -Lie   # convencao: x -> x + eps  =>  delta(pert) = -Lie_eps(fundo)

SUB_BG = {sp.Derivative(bF, t): b_s * xi_s * Hf_s,
          sp.Derivative(xF, t): xid_s,
          bF: b_s, xF: xi_s,
          sp.Derivative(TF, t): Tdsym, TF: Tsym,
          sp.Derivative(ZF, t): Zdsym, ZF: Zsym}


def coef_trig(expr, trig):
    """expr deve ser coeff*trig; devolve coeff e verifica que e puro."""
    c = sp.simplify(sp.cancel(sp.expand(expr) / trig))
    if c.has(sp.cos(ksym * z)) or c.has(sp.sin(ksym * z)):
        raise RuntimeError(f"coeficiente nao-puro: {c}")
    return c


# casa contra a parametrizacao da PROPRIA biblioteca
dPhi, dPsi, dB, dE = sp.symbols('dPhiF dPsiF dBF dEF')
fp = scalar_metric_f(dPhi, dPsi, dB, dE)
lin = {ij: eps_part(fp[ij], 1) for ij in ((0, 0), (0, 3), (1, 1), (3, 3))}

eqs = []
for ij in ((0, 0), (0, 3), (1, 1), (3, 3)):
    trig = sz if ij == (0, 3) else cz
    lhs = coef_trig(lin[ij], trig)
    rhs = coef_trig(delta_f[ij].subs(SUB_BG), trig)
    eqs.append(sp.Eq(lhs, rhs))
sol = sp.solve(eqs, (dPhi, dPsi, dB, dE), dict=True)
if len(sol) != 1:
    raise RuntimeError(f"casamento nao-unico: {sol}")
sol = sol[0]
rota1 = {n: sp.simplify(sol[s]) for n, s in
         (('Phi_f', dPhi), ('Psi_f', dPsi), ('B_f', dB), ('E_f', dE))}

# rota 2: formulas fechadas (derivadas a mao no design da C1)
rota2 = {'Phi_f': -Tdsym - (xid_s / xi_s) * Tsym,
         'Psi_f': xi_s * Hf_s * Tsym,
         'B_f': xi_s * Tsym / b_s + b_s * Zdsym / (xi_s * ksym),
         'E_f': Zsym / ksym}

ok_a1 = True
for n in rota1:
    d = sp.simplify(rota1[n] - rota2[n])
    ok = (d == 0)
    ok_a1 = ok_a1 and ok
    say(f"    delta {n:6s} = {rota2[n]}   [rotas {'BATEM' if ok else 'DIVERGEM: ' + str(d)}]")

# controle negativo: sinal errado em Psi_f TEM de divergir
d_neg = sp.simplify(rota1['Psi_f'] - (-rota2['Psi_f']))
ok_neg = (d_neg != 0)
say(f"    controle negativo (sinal de Psi_f trocado): "
    f"{'DETECTADO (diverge, como esperado)' if ok_neg else 'FALHOU — teste sem poder'}")
say(f"  [A1 {'PASSA' if (ok_a1 and ok_neg) else 'FALHA'}]")

# ---------- A2: a quebra e puramente potencial ----------
say("")
say("A2. K e C nao contem Fb/Fp/Fpp (quebra = potencial puro)")
ok_a2 = True
for nomeM, M in (('K7', K7), ('C7', C7)):
    for Fsym in (Fb, Fp, Fpp):
        dep = any(sp.diff(M[i, j], Fsym) != 0
                  for i in range(7) for j in range(7))
        if dep:
            ok_a2 = False
            say(f"    !! {nomeM} depende de {Fsym}")
say(f"    K_int = C_int = 0 simbolico: {'confirmado' if ok_a2 else 'FALHOU'}")
dep_W = any(sp.diff(W7[i, j], Fb) != 0 for i in range(7) for j in range(7))
say(f"    (sanidade/poder do assert: W7 depende de Fb? {dep_W} — esperado True)")
ok_a2 = ok_a2 and dep_W
say(f"  [A2 {'PASSA' if ok_a2 else 'FALHA'}]")
say("    => consequencia 2a: doenca CINETICA nao pode vir diretamente do")
say("       termo de quebra; doenca de MASSA pode (e o teste B2 mede se vem).")

# ==================================================================
# PARTE B — numerica, nos fundos do G1-b
# ==================================================================
say("")
say("-" * 72)
say("PARTE B — decomposicao de Goldstone + origem da massa (2b)")
say("-" * 72)

RHO_M0 = 0.3


def fundo_a10(B1e, B2v, B0v, B4v, mu):
    """Ponto fixo a=10 — copia inline (mesma de investigacao1/modulacao)."""
    kap = 1.0 / mu
    meff2 = mu / (1.0 + mu)
    a = 10.0
    rho_til = RHO_M0 * a**-3 / meff2
    rr = np.roots([kap * B4v - 3 * B2v, -3 * B1e,
                   3 * kap * B2v - B0v - rho_til, kap * B1e])
    r_esc = max(1e-14, 1e-6 * kap * B1e / max(rho_til, 1.0))
    reais = sorted(zr.real for zr in rr
                   if abs(zr.imag) < 1e-9 and zr.real > r_esc)
    if not reais:
        return None
    r = reais[0]
    dW = kap * (2 * B4v * r - B1e / r**2) - 3 * B1e - 6 * B2v * r
    drdN = -3.0 * rho_til / dW
    xi = r + drdN
    Vf = B4v + 3 * B2v / r**2 + B1e / r**3
    H2 = meff2 * r * r * Vf / (3.0 * mu)
    if H2 <= 0 or xi <= 0:
        return None
    H = np.sqrt(H2)
    rho_int = meff2 * (B0v + 3 * B1e * r + 3 * B2v * r**2)
    return r, xi, H, H / r, 3.0 * H2 - rho_int, a, r * a


LIVRES = (a_s, b_s, xi_s, H_s, Hf_s, Ub, ksym, b1, b2, b0, b4, Mf2, Meff2)
FIXOS = {Mg2: 1, m2: 1, chid_s: 0, chidd_s: 0, rho_s: 0,
         Hd_s: 0, Hfd_s: 0, xid_s: 0, Up: 0, Upp: sp.Rational(3, 10),
         b3: 0, Fp: 0, Fpp: 0}

say("")
say("[lambdify] full (Fb=1) e base (Fb=0), fundo fixo — tecnica do T1")
MF = {}
for nomeM, M in (('K', K7), ('C', C7), ('W', W7)):
    Msub = M.subs(FIXOS)
    MF[(nomeM, 'full')] = sp.lambdify(LIVRES, Msub.subs(Fb, 1), modules='numpy')
    MF[(nomeM, 'base')] = sp.lambdify(LIVRES, Msub.subs(Fb, 0), modules='numpy')
say("    pronto")


def classifica(w2, kN, H_val):
    om = np.sqrt(complex(w2))
    taxa = abs(om.imag) / H_val
    if taxa > TOL_SIG:
        return 'TAQUIAO', taxa
    if kN < -TOL_KN:
        return 'FANTASMA', taxa
    return 'limpo', taxa


def orbita_M4(bb, xi, Hf, kv):
    """colunas = (T, Tdot, Z, Zdot); linhas = (Phi_f, Psi_f, B_f, E_f).
    xid=0 no ponto fixo (FIXOS)."""
    return np.array([
        [0.0,          -1.0, 0.0,      0.0],
        [xi * Hf,       0.0, 0.0,      0.0],
        [xi / bb,       0.0, 0.0,      bb / (xi * kv)],
        [0.0,           0.0, 1.0 / kv, 0.0]], dtype=float)


CELULAS = [
    (0.3, 1.0, -0.4, "REF"),
    (1.0, 1.0, -0.4, "REF"),
    (3.0, 1.0, -0.4, "REF"),
    (10.0, 1.0, -0.4, "REF"),
    (0.1, 0.2, -1.0, "fresta"),
]
B0_V, B4_V = 1.0, 0.5
KG = [1.0, 10.0]

patologicos = []
todos = []
ok_dets = True
anc_sigma = None
anc_kn = None

for mu, B1v, B2v, tag in CELULAS:
    f = fundo_a10(B1v, B2v, B0_V, B4_V, mu)
    if f is None:
        say(f"  mu={mu} [{tag}]: fundo invalido — pulando (inesperado; verificar)")
        continue
    r, xi, H, Hf, Ubv, a, bb = f
    meff2 = mu / (1.0 + mu)
    say("")
    say(f"  mu={mu} [{tag}]  (beta1={B1v}, beta2={B2v}, r={r:.6f}, "
        f"xi={xi:.6f}, H={H:.6f})")
    for kv in KG:
        args = (a, bb, xi, H, Hf, Ubv, kv, B1v, B2v, B0_V, B4_V, mu, meff2)
        Kfull = np.array(MF[('K', 'full')](*args), float)
        Kbase = np.array(MF[('K', 'base')](*args), float)
        Cfull = np.array(MF[('C', 'full')](*args), float)
        Cbase = np.array(MF[('C', 'base')](*args), float)
        Wfull = np.array(MF[('W', 'full')](*args), float)
        Wbase = np.array(MF[('W', 'base')](*args), float)
        # belt-and-suspenders do A2, agora numerico
        dK = np.max(np.abs(Kfull - Kbase))
        dC = np.max(np.abs(Cfull - Cbase))
        if dK > 1e-12 or dC > 1e-12:
            raise RuntimeError(f"K_int/C_int != 0 numerico: {dK}, {dC}")
        Wint = Wfull - Wbase

        M4 = orbita_M4(bb, xi, Hf, kv)
        detM = np.linalg.det(M4)
        if abs(detM) < 1e-12:
            ok_dets = False
        col_norms = np.linalg.norm(M4, axis=0)

        pares = d1.agrupa_pares(d1.qep_modes(Kfull, Cfull, Wfull))
        pares.sort(key=lambda m: abs(m['omega2']))
        say(f"    k={kv:g}  (det orbita = {detM:+.3e})")
        for mm in pares:
            v = mm['v']
            w2 = mm['omega2']
            kN = mm['knorm']
            classe, taxa = classifica(w2, kN, H)
            p_f = float(sum(abs(v[i])**2 for i in IDX_F))
            p_mult = float(sum(abs(v[i])**2 for i in IDX_MULT))
            p_chi = float(abs(v[IDX_DCHI])**2)
            # decomposicao de Goldstone exata no bloco-f
            v_f = np.array([v[i] for i in IDX_F])
            c = np.linalg.solve(M4, v_f)
            resid = np.linalg.norm(M4 @ c - v_f)
            chat = np.abs(c * col_norms)**2
            tot = chat.sum() if chat.sum() > 0 else 1.0
            frac = chat / tot
            pi0 = frac[0] + frac[1]      # (T, Tdot)
            piL = frac[2] + frac[3]      # (Z, Zdot)
            # origem da massa
            wI = float(np.real(np.conjugate(v) @ Wint @ v))
            wB = float(np.real(np.conjugate(v) @ Wbase @ v))
            den = abs(wI) + abs(wB)
            rI = abs(wI) / den if den > 0 else float('nan')
            say(f"      w2={w2.real:+.3e}"
                f"{'' if abs(w2.imag) < 1e-6*max(1.0, abs(w2.real)) else f' {w2.imag:+.2e}i'}"
                f"  kN={kN:+.2e}  [{classe:8s}]")
            say(f"        blocos: orbita-f={p_f:.3f} mult={p_mult:.3f} "
                f"dchi={p_chi:.3f}   goldstone: pi0(T,Td)={pi0:.3f} "
                f"piL(Z,Zd)={piL:.3f}  (resid {resid:.1e})")
            say(f"        massa:  v'W_int v={wI:+.3e}  v'W_EH v={wB:+.3e}  "
                f"rI={rI:.3f}")
            reg = dict(mu=mu, tag=tag, k=kv, classe=classe, taxa=taxa, kN=kN,
                       p_f=p_f, p_mult=p_mult, p_chi=p_chi,
                       pi0=pi0, piL=piL, rI=rI, wI=wI, wB=wB)
            todos.append(reg)
            if classe in ('TAQUIAO', 'FANTASMA'):
                patologicos.append(reg)
            # ancoras de continuidade
            if tag == 'REF' and mu == 1.0 and kv == 1.0 and classe == 'TAQUIAO':
                anc_sigma = taxa
            if tag == 'fresta' and kv == 1.0 and classe == 'FANTASMA':
                anc_kn = kN

# ------------------------------------------------------------------
# ancoras de continuidade
# ------------------------------------------------------------------
say("")
say("[continuidade] sigma/H (REF mu=1, k=1) = "
    f"{anc_sigma if anc_sigma is None else f'{anc_sigma:.4f}'} (esperado 3.651)")
say("[continuidade] kN fantasma (fresta, k=1) = "
    f"{anc_kn if anc_kn is None else f'{anc_kn:+.3e}'} (esperado -1.6e-5)")
ok_anc = (anc_sigma is not None and abs(anc_sigma - 3.651) < 0.02 * 3.651
          and anc_kn is not None and abs(anc_kn - (-1.616e-5)) < 0.3e-5)
say(f"  [{'ANCORAS OK' if ok_anc else 'ANCORAS FALHARAM — nao interpretar'}]")

# ------------------------------------------------------------------
# veredito
# ------------------------------------------------------------------
say("")
say("=" * 72)
say("VEREDITO C1 (criterios pre-declarados no cabecalho)")
say("=" * 72)

crit1 = ok_a1 and ok_neg and ok_a2 and ok_dets
say(f"  C1 (estrutura, 2a): {'PASSA' if crit1 else 'FALHA'} — rotas batem, "
    f"controle negativo detecta, quebra=potencial puro, orbitas geram o bloco-f")

viol2 = [p for p in patologicos if (p['p_f'] + p['p_mult']) < 0.95]
crit2 = (len(patologicos) > 0) and not viol2
say(f"  C2 (composicao, 2b): {'PASSA' if crit2 else 'FALHA'} — "
    f"{len(patologicos)} modos patologicos, "
    f"{len(viol2)} fora de {{orbita+mult}}>=0.95")

taquioes = [p for p in patologicos if p['classe'] == 'TAQUIAO']
viol3 = [p for p in taquioes if not (p['rI'] >= 0.5)]
crit3 = (len(taquioes) > 0) and not viol3
say(f"  C3 (origem da massa, 2b): {'PASSA' if crit3 else 'FALHA'} — "
    f"{len(taquioes)} taquioes, {len(viol3)} com rI<0.5")
if viol3:
    for p in viol3:
        say(f"      mu={p['mu']} [{p['tag']}] k={p['k']}: rI={p['rI']:.3f} "
            f"(wI={p['wI']:+.3e}, wB={p['wB']:+.3e})")

say("")
if crit1 and crit2 and crit3 and ok_anc:
    say("  >>> CONFIRMA. A premissa estrutural da circularidade HR-Goldstone")
    say("  sobe a nivel 2a (derivada in-repo, duas rotas, controle negativo):")
    say("  no gauge plano-g, o setor de Goldstone das difeos relativas e o")
    say("  bloco-f inteiro, a quebra entra como potencial puro, e os modos")
    say("  patologicos (i) vivem em {orbita+multiplicadores} com projecao")
    say("  dchi ~ 0 e (ii) sentem um potencial dominado pelo termo de")
    say("  quebra — pseudo-Goldstones das difeos relativas, com a identidade")
    say("  pi0/piL reportada acima. O criterio anti-circularidade do")
    say("  gate1c secao 3 passa de argumento a resultado.")
elif ok_anc:
    say("  >>> RESULTADO MISTO ou ENFRAQUECE (gate1c secao 8(i)) — ver quais")
    say("  criterios falharam acima; reportar os numeros no doc de resultado")
    say("  sem arredondar a leitura.")
else:
    say("  >>> ANCORAS DE CONTINUIDADE FALHARAM — resultado NAO interpretavel;")
    say("  investigar a rota antes de qualquer leitura.")

say("")
say("LEITURA AUXILIAR:")
say("- pi0 = Goldstone TEMPORAL (T, Tdot: gera Phi_f/Psi_f e parte de B_f);")
say("  piL = Goldstone LONGITUDINAL (Z, Zdot: gera E_f e parte de B_f) —")
say("  o helicity-0 'classico' do gravitao massivo e o piL.")
say("- fantasmas: K_int=0 (A2) => a norma negativa nasce da eliminacao de")
say("  vinculos do setor EH na presenca do potencial de quebra; o rI deles")
say("  e diagnostico, nao criterio.")
say("- fundos e classificacao identicos ao G1-b/investigacao1 (continuidade")
say("  garantida pelas ancoras).")

os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
with open(os.path.join(HERE, "out", "stuckelberg_goldstone.txt"),
          "w", encoding="utf-8") as fh:
    fh.write("\n".join(OUT))
say("")
say("concluido. saida em auditoria/code/out/stuckelberg_goldstone.txt")
