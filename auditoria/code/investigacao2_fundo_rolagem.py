# -*- coding: utf-8 -*-
"""
investigacao2_fundo_rolagem.py — Investigacao 2, FASE A: o fundo de
rolagem (condensacao dinamica, p_phi != 0).

CONTEXTO. Todas as sondagens ate aqui viveram em fundos com a
constraint FATORADA: ou beta_n constante (dois ramos), ou modulacao com
<phi_-> ESTACIONARIO (p_phi=0, residuo nulo — modulacao_qep.py). O
unico regime nunca tocado e p_phi != 0 com beta_1' != 0, onde a
constraint secundaria NAO fatora (Gate 2: residuo -M_eff^2 m^2 p_phi
beta_1' — docs/gate2_ghost.md, auditoria/code/gate2_fatoracao.py). E a
saida n. 5 do veredito e o teste direto de R2
(docs/gate1_identidade_relacional.md). A C1 (stuckelberg) deu o alvo
extra: a doenca vive no BALANCO quebra x EH/vinculos, e p_phi != 0 muda
exatamente o lado EH (docs/resultado_stuckelberg_goldstone.md secao 6).

ESTRUTURA (derivada e verificada simbolicamente na PARTE 1 do script).
Minisuperespaco, N_g=1, materia = poeira (rho_m0/a^3), F1 (beta_3=0),
so beta_1 = beta_1(chi) modulado; chi == phi_-:

  Friedmann g :  3 M_g^2 H^2   = chid^2/2 + U(chi) + rho_m0/a^3
                                 + m^2 M_eff^2 Vgc(r,chi)
  Friedmann f :  3 M_f^2 H_f^2 = m^2 M_eff^2 Vfc(r,chi) / r^3
  eq. de chi  :  chidd + 3 H chid + U'(chi)
                                 = - m^2 M_eff^2 beta_1'(chi) (xi + 3 r)
  SECUNDARIA  :  {H_g, H_f} = 0, que em variaveis de velocidade e
      (prefator) * (H - r H_f) * B(r,chi)  =  m^2 M_eff^2 a^3 chid beta_1'
  com B = beta_1(chi) + 2 beta_2 r  (F1). Os DOIS fatores de ramo a
  esquerda; o residuo do Gate 2 a direita. A secundaria FIXA r a cada
  instante (deslocado dos dois ramos enquanto chid*beta_1' != 0); xi e
  fixado no nivel seguinte (consistencia de r ao longo do fluxo):
      xi = H (1 + dlnr/dN) / H_f.

  Limite de controle: chid*beta_1' -> 0  =>  a raiz continua do ramo
  finito, H = r H_f, que equivale a cubica m^2 M_eff^2 W(r) = rho_tot
  (verificado: e EXATAMENTE o fundo de ramo_dinamico_correto.py com a
  energia de chi incluida).

O QUE A FASE A DECIDE (criterios pre-declarados; endurecidos apos a
1a rodada, cuja janela ate a=100 so viu o INICIO da rolagem):
  G2a-SIMB (2a): a fatoracao simbolica confere — em beta_1'=0 a
      secundaria anula-se nos DOIS ramos; em H = r H_f o que sobra e
      EXATAMENTE -m^2 M_eff^2 a^3 chid beta_1'.
  G2a-CONTROLE (2b): sem campo (chi==0), a trajetoria reproduz o fundo
      conhecido do ramo finito (r(a=10) = 0.332259 na REF, ancora de
      fundo_a10/investigacao1). Passo halving: |Delta r|/r < 1e-3.
  G2a-EXISTE (2b): trajetorias completas (sem abortos: xi>0, H^2>0,
      H_f^2>0, raiz nao perdida).
  G2a-CONDENSA (2b): pelo menos uma rodada COMPLETA a condensacao
      (|chi/v| > 0.5) — sem isso a fase B nao tem regime p_phi!=0
      genuino para medir.
  G2a-PREVISAO (poder): a 1a rodada revelou que a interacao HR soma
      Delta = 2 m^2 Meff^2 b1_0 (xi+3r)/v*^2 a massa^2 da ORIGEM de
      chi (a fonte e linear em chi perto de 0) — a interacao RESISTE a
      condensacao. Limiar previsto: m_chi^2_crit = 2 Delta_infty com
      (xi+3r)_infty = 4 r_infty ~ 1.33 (REF, v*=1) => ~2.66. A
      varredura tem de confirmar condensa/estavel dos DOIS lados.
  G2a-DESLOCA (poder): durante uma condensacao COMPLETA, o fundo sai
      genuinamente dos dois ramos — max |H - r H_f|/H acima do ruido
      (senao a fase B e vacua).
  G2a-POUSO (2b): ao final (chid -> 0), r converge para a raiz da
      cubica com beta_1eff = beta_1(chi_final).
  Saida para a FASE B: janela de a com o maior deslocamento (o alvo
      das perturbacoes) e a adiabaticidade nessa janela.

POTENCIAL E MODULACAO (mesma parametrizacao de modulacao_qep.py):
  U(chi) = -(mu_-^2/2) chi^2 + (lam/4) chi^4 + mu_-^2 v^2/4,
  com mu_-^2 = m_chi^2/2, lam = mu_-^2/v^2  =>  U(v)=0, U''(v)=m_chi^2;
  beta_1(chi) = b1_0 (1 + chi^2/v*^2), v = g_end * v*.

Knobs varridos (2a rodada): g_end em {1, 2}, m_chi^2 em
{0.3, 3, 10, 30} (0.3 e 3 documentam o lado estavel/lento do limiar;
10 e 30 condensam dentro da janela), v* = 1, a ate 1e5; celula REF
(b1_0=1, b2=-0.4, b0=1, b4=0.5, mu=1). rho_m0 = 0.3. chi_0 = 1e-3 v,
chid_0 = 0, a_0 = 0.01.

METODO NUMERICO (declarado): integracao em N = ln a, Euler explicito
de passo fino, com r resolvido da secundaria por brentq a cada passo
(continuidade a partir do passo anterior; janela adaptativa) e
dr/dN por diferenca defasada (lag-1) — validado pelo controle
G2a-CONTROLE (ancora r(a=10)=0.332259) e pelo halving do passo. Nao e
DAE de alta ordem de proposito: a fase A pergunta EXISTENCIA e
ESTRUTURA, nao precisao fina.

Requer sympy, numpy, scipy. ~1-3 min.
Uso (raiz do repo, venv ativo):
    python auditoria/code/investigacao2_fundo_rolagem.py
Saida em auditoria/code/out/investigacao2_fundo_rolagem.txt
"""
import os
import sys
import time

import numpy as np
import sympy as sp
from scipy.optimize import brentq

HERE = os.path.dirname(os.path.abspath(__file__))
T0 = time.time()
OUT = []


def say(*a):
    line = " ".join(str(x) for x in a)
    print(f"[{time.time()-T0:7.1f}s] {line}")
    OUT.append(line)


say("=" * 72)
say("INVESTIGACAO 2 — FASE A: fundo de rolagem (p_phi != 0)")
say("=" * 72)

# ==================================================================
# PARTE 1 — simbolica: a secundaria nao-fatorada, exata
# ==================================================================
say("")
say("PARTE 1 — {H_g, H_f} com beta_1(chi): fatoracao e residuo (alvo 2a)")

a_, b_, ch_ = sp.symbols('a b chi', positive=True)
pa_, pb_, pch_ = sp.symbols('p_a p_b p_chi', real=True)
Mg2s, Mf2s, Me2s, m2s = sp.symbols('Mg2 Mf2 Meff2 m2', positive=True)
b0s, b2s, b4s = sp.symbols('beta_0 beta_2 beta_4', real=True)
Hs, Hfs, chds = sp.symbols('H H_f chidot', real=True)
b1F = sp.Function('beta_1')(ch_)
UF = sp.Function('U')(ch_)

rr_ = b_ / a_
Vgc = b0s + 3 * rr_ * b1F + 3 * rr_**2 * b2s               # F1: beta_3 = 0
Vfc = b1F + 3 * rr_ * b2s + rr_**3 * b4s
# materia = poeira: sqrt(-g) rho = N_g a^3 (rho_m0/a^3) = N_g rho_m0
# => termo CONSTANTE em H_g; nao contribui a nenhum bracket.
rho0 = sp.Symbol('rho_m0', nonnegative=True)
Hg = (-pa_**2 / (12 * Mg2s * a_) + pch_**2 / (2 * a_**3)
      + a_**3 * UF + rho0 + m2s * Me2s * a_**3 * Vgc)
Hf = -pb_**2 / (12 * Mf2s * b_) + m2s * Me2s * a_**3 * Vfc

CANON = [(a_, pa_), (b_, pb_), (ch_, pch_)]
Om = sp.expand(sum(sp.diff(Hg, q) * sp.diff(Hf, p)
                   - sp.diff(Hg, p) * sp.diff(Hf, q) for q, p in CANON))

# variaveis de velocidade (N_g = 1):
#   p_a = -6 Mg2 a^2 H ; p_b = -6 Mf2 b^2 H_f ; p_chi = a^3 chidot
Om_v = sp.expand(Om.subs({pa_: -6 * Mg2s * a_**2 * Hs,
                          pb_: -6 * Mf2s * b_**2 * Hfs,
                          pch_: a_**3 * chds}))

ok_noU = not Om_v.has(UF)
say(f"    U(chi) ausente de {{H_g,H_f}}: {ok_noU} (esperado True)")

# T1a: com beta_1 CONSTANTE, anula-se nos DOIS ramos
b1c = sp.Symbol('beta_1c', real=True)
Om_c = Om_v.subs(b1F, b1c)
res_fin = sp.simplify(Om_c.subs(Hs, rr_ * Hfs))            # ramo finito
res_alg = sp.simplify(Om_c.subs(b_, -a_ * b1c / (2 * b2s)))  # ramo algebrico
ok_t1a = (res_fin == 0) and (res_alg == 0)
say(f"    beta_1'=0: anula no ramo finito ({res_fin == 0}) e no "
    f"algebrico ({res_alg == 0})")

# T1b: em H = r H_f, sobra EXATAMENTE  -m^2 Meff^2 a^3 chidot beta_1'
res_mod = sp.simplify(Om_v.subs(Hs, rr_ * Hfs))
alvo = -m2s * Me2s * a_**3 * chds * sp.diff(b1F, ch_)
ok_t1b = sp.simplify(res_mod - alvo) == 0
say(f"    residuo em H=r*H_f == -m^2 Meff^2 a^3 chidot beta_1': {ok_t1b}")

# controle negativo (poder de detecao): alvo com sinal trocado DIVERGE
ok_t1neg = sp.simplify(res_mod - (-alvo)) != 0
say(f"    controle negativo (sinal trocado diverge): {ok_t1neg}")

ok_simb = ok_noU and ok_t1a and ok_t1b and ok_t1neg
say(f"  [G2a-SIMB {'PASSA' if ok_simb else 'FALHA'}]")
if not ok_simb:
    say("  !! estrutura simbolica nao confere — abortando")
    sys.exit(1)

# lambdify da secundaria com a forma concreta de beta_1(chi)
b10s, vsts = sp.symbols('b1_0 v_star', positive=True)
b1_conc = b10s * (1 + ch_**2 / vsts**2)
Om_conc = Om_v.subs(b1F, b1_conc).doit()
Om_fn = sp.lambdify((a_, b_, ch_, chds, Hs, Hfs,
                     Mg2s, Mf2s, Me2s, m2s, b0s, b2s, b4s, b10s, vsts),
                    sp.expand(Om_conc), modules='math')

# ==================================================================
# PARTE 2 — numerica: o fundo de rolagem
# ==================================================================
say("")
say("PARTE 2 — integracao do fundo (Heun em N, r por brentq, lag-1)")

MU = 1.0
MG2, MF2 = 1.0, MU
ME2 = MU / (1.0 + MU)
M2 = 1.0
B0V, B2V, B4V = 1.0, -0.4, 0.5
B10 = 1.0
RHO0 = 0.3


def beta1(ch, vst):
    return B10 * (1.0 + ch * ch / (vst * vst))


def dbeta1(ch, vst):
    return 2.0 * B10 * ch / (vst * vst)


def U_pot(ch, mu2, lam, U0):
    return -0.5 * mu2 * ch * ch + 0.25 * lam * ch**4 + U0


def dU_pot(ch, mu2, lam):
    return -mu2 * ch + lam * ch**3


def H2_of(r, ch, chd, a, vst, mu2, lam, U0):
    b1v = beta1(ch, vst)
    Vg = B0V + 3 * r * b1v + 3 * r * r * B2V
    return (0.5 * chd * chd + U_pot(ch, mu2, lam, U0) + RHO0 / a**3
            + M2 * ME2 * Vg) / (3 * MG2)


def Hf2_of(r, ch, vst):
    b1v = beta1(ch, vst)
    Vf = b1v + 3 * r * B2V + r**3 * B4V
    return M2 * ME2 * Vf / (3 * MF2 * r**3)


def Om_num(r, ch, chd, a, vst, mu2, lam, U0):
    """secundaria em (r; estado). nan fora da regiao fisica."""
    H2 = H2_of(r, ch, chd, a, vst, mu2, lam, U0)
    Hf2 = Hf2_of(r, ch, vst)
    if H2 <= 0 or Hf2 <= 0:
        return float('nan')
    return Om_fn(a, r * a, ch, chd, np.sqrt(H2), np.sqrt(Hf2),
                 MG2, MF2, ME2, M2, B0V, B2V, B4V, B10, vst)


def acha_raiz(r_prev, ch, chd, a, vst, mu2, lam, U0):
    """raiz da secundaria por continuidade; janela adaptativa."""
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


def raiz_cubica_controle(a, ch, chd, vst, mu2, lam, U0):
    """raiz do ramo finito: m^2 Meff^2 W(r) = rho_tot (menor positiva)."""
    b1v = beta1(ch, vst)
    rho_tot = 0.5 * chd * chd + U_pot(ch, mu2, lam, U0) + RHO0 / a**3
    rt = rho_tot / (M2 * ME2)
    kap = MG2 / MF2
    rr = np.roots([kap * B4V - 3 * B2V, -3 * b1v,
                   3 * kap * B2V - B0V - rt, kap * b1v])
    reais = sorted(x.real for x in rr if abs(x.imag) < 1e-9 and x.real > 1e-12)
    return reais[0] if reais else None


def integra(g_end, mchi2, vst=1.0, a0=0.01, a1=100.0, dN=5e-4,
            sem_campo=False, verbose=True):
    """integra o fundo; devolve dict com trajetoria e status."""
    v = g_end * vst
    mu2 = 0.5 * mchi2
    lam = mu2 / (v * v) if v > 0 else 0.0
    U0 = 0.25 * mu2 * v * v

    N0, N1 = np.log(a0), np.log(a1)
    n = int((N1 - N0) / dN) + 1
    ch = 0.0 if sem_campo else 1e-3 * v
    y = 0.0                                    # y = dchi/dN
    a = a0
    r = raiz_cubica_controle(a, ch, 0.0, vst, mu2, lam, U0)
    if r is None:
        return dict(status='sem raiz inicial')
    rp = 3.0 * r                               # dr/dN primordial (r ~ a^3)
    Hprev = None
    traj = dict(N=[], a=[], r=[], xi=[], H=[], ch=[], chd=[],
                B=[], desl=[], adiab=[])
    status = 'ok'
    for i in range(n):
        N = N0 + i * dN
        a = np.exp(N)
        # chd consistente: chd = H*y precisa de H que depende de chd —
        # resolve o escalar: 3Mg2 H^2 = y^2 H^2/2 + resto
        b1v = beta1(ch, vst)
        Vg = B0V + 3 * r * b1v + 3 * r * r * B2V
        resto = U_pot(ch, mu2, lam, U0) + RHO0 / a**3 + M2 * ME2 * Vg
        den = 3 * MG2 - 0.5 * y * y
        if den <= 0 or resto <= 0:
            status = f'abort H^2 (den={den:.3f}, resto={resto:.3f}) em a={a:.4f}'
            break
        H2 = resto / den
        H = np.sqrt(H2)
        chd = H * y
        Hf2 = Hf2_of(r, ch, vst)
        if Hf2 <= 0:
            status = f'abort H_f^2<0 em a={a:.4f}'
            break
        Hfv = np.sqrt(Hf2)
        xi = H * (1.0 + rp / r) / Hfv
        if i > 10 and xi <= 0:
            status = f'abort xi={xi:.4f}<=0 em a={a:.4f}'
            break
        # eq. de chi:  chidd = -3H chd - U' - m2 Meff2 beta1' (xi+3r)
        chidd = (-3 * H * chd - dU_pot(ch, mu2, lam)
                 - M2 * ME2 * dbeta1(ch, vst) * (xi + 3 * r))
        Hp = 0.0 if Hprev is None else (H - Hprev) / dN
        yp = chidd / H2 - (Hp / H) * y
        # registro (subamostrado)
        if i % max(1, n // 4000) == 0:
            desl = (H - r * Hfv) / H
            adiab = abs(chidd / (3 * H * chd)) if abs(chd) > 1e-12 else 0.0
            for kk, vv in (('N', N), ('a', a), ('r', r), ('xi', xi),
                           ('H', H), ('ch', ch), ('chd', chd),
                           ('B', b1v + 2 * B2V * r), ('desl', desl),
                           ('adiab', adiab)):
                traj[kk].append(vv)
        # passo de Euler explicito em (ch, y); r re-resolvido a seguir
        if not sem_campo:
            ch = ch + dN * y
            y = y + dN * yp
        a_next = np.exp(N + dN)
        chd_next = 0.0
        if not sem_campo:
            # chd no proximo ponto (para a raiz): usa H atual como proxy
            chd_next = H * y
        r_new = acha_raiz(r, ch, chd_next, a_next, vst, mu2, lam, U0)
        if r_new is None:
            status = f'abort raiz perdida em a={a_next:.4f}'
            break
        rp = (r_new - r) / dN
        r = r_new
        Hprev = H
    fim = dict(status=status, a_fim=a, r_fim=r, ch_fim=ch,
               chd_fim=(H * y if status == 'ok' and not sem_campo else 0.0),
               v=v, vst=vst, mu2=mu2, lam=lam, U0=U0)
    fim['traj'] = {kk: np.array(vv) for kk, vv in traj.items()}
    return fim


# ---------------- G2a-CONTROLE: sem campo, reproduz o ramo finito ----
say("")
say("G2a-CONTROLE — sem campo (chi==0): reproduz fundo_a10?")
ctl = integra(g_end=1.0, mchi2=0.0, sem_campo=True, a1=12.0, dN=5e-4)
ok_ctl = False
if ctl['status'] == 'ok':
    tr = ctl['traj']
    i10 = int(np.argmin(np.abs(tr['a'] - 10.0)))
    r10 = tr['r'][i10]
    say(f"    r(a=10) = {r10:.6f}  (ancora fundo_a10: 0.332259)")
    ok_ctl = abs(r10 - 0.332259) < 1e-3
    # halving do passo
    ctl2 = integra(g_end=1.0, mchi2=0.0, sem_campo=True, a1=12.0, dN=2.5e-4)
    if ctl2['status'] == 'ok':
        tr2 = ctl2['traj']
        j10 = int(np.argmin(np.abs(tr2['a'] - 10.0)))
        dh = abs(tr2['r'][j10] - r10) / r10
        say(f"    halving do passo: |Delta r|/r = {dh:.2e} (criterio <1e-3)")
        ok_ctl = ok_ctl and dh < 1e-3
else:
    say(f"    controle abortou: {ctl['status']}")
say(f"  [G2a-CONTROLE {'PASSA' if ok_ctl else 'FALHA'}]")

# ---------------- limiar de condensacao (previsao pre-declarada) ----
# A fonte da EOM de chi perto da origem e linear em chi:
#   -m^2 Meff^2 beta_1'(chi) (xi+3r) = -[2 m^2 Meff^2 b1_0 (xi+3r)/v*^2] chi
# => a interacao SOMA Delta = 2 m^2 Meff^2 b1_0 (xi+3r)/v*^2 a massa^2
# da origem. Condensa sse mu_-^2 = m_chi^2/2 > Delta_infty, com
# (xi+3r)_infty = 4 r_infty do ponto fixo NAO-modulado (chi~0).
R_INF_UNMOD = 0.332259                     # ancora fundo_a10 REF
VST_PREV = 1.0
DELTA_INF = 2 * M2 * ME2 * B10 * 4 * R_INF_UNMOD / VST_PREV**2
MCHI2_CRIT = 2 * DELTA_INF
say("")
say(f"PREVISAO (pre-declarada): Delta_infty = {DELTA_INF:.4f}  =>")
say(f"    m_chi^2 < {MCHI2_CRIT:.3f}: origem ESTAVEL (nao condensa);")
say(f"    m_chi^2 > {MCHI2_CRIT:.3f}: condensa (tanto mais rapido quanto maior).")
say("    O proprio termo de interacao HR e uma back-reaction que RESISTE")
say("    a condensacao de phi_- — teste de poder: a varredura tem de")
say("    confirmar o limiar dos dois lados.")

# ---------------- varredura de knobs --------------------------------
say("")
say("VARREDURA — g_end x m_chi^2 (v*=1, REF mu=1, a ate 1e5)")
say(f"    {'g':>5} {'mchi2':>6} {'status':<30} {'max|desl|':>10} "
    f"{'a(max)':>9} {'r_fim':>8} {'chi/v':>7} {'pouso':>10}")

resultados = []
for g_end in (1.0, 2.0):
    for mchi2 in (0.3, 3.0, 10.0, 30.0):
        res = integra(g_end=g_end, mchi2=mchi2, vst=1.0, a1=1e5)
        tr = res.get('traj', {})
        max_desl, a_max, pouso = float('nan'), float('nan'), float('nan')
        if len(tr.get('a', [])) > 10:
            idesl = int(np.nanargmax(np.abs(tr['desl'])))
            max_desl = tr['desl'][idesl]
            a_max = tr['a'][idesl]
        if res['status'] == 'ok':
            # pouso: |H - r H_f|/H no fim + r vs cubica com beta1(v-final)
            desl_fim = tr['desl'][-1]
            r_cub = raiz_cubica_controle(res['a_fim'], res['ch_fim'],
                                         0.0, res['vst'], res['mu2'],
                                         res['lam'], res['U0'])
            pouso = (abs(res['r_fim'] - r_cub) / r_cub
                     if r_cub else float('nan'))
        chfrac = res.get('ch_fim', 0.0) / res['v'] if res.get('v') else 0.0
        condensou = abs(chfrac) > 0.5
        prev = 'condensa' if mchi2 > MCHI2_CRIT else 'estavel'
        obs = 'condensou' if condensou else 'nao'
        acerto = (mchi2 > MCHI2_CRIT) == condensou
        say(f"    {g_end:5.1f} {mchi2:6.1f} {res['status']:<30} "
            f"{max_desl:+10.2e} {a_max:9.1f} {res.get('r_fim', float('nan')):8.4f} "
            f"{chfrac:7.3f} {pouso:10.2e}  prev={prev}/obs={obs} "
            f"[{'OK' if acerto else 'ERRA'}]")
        res.update(g_end=g_end, mchi2=mchi2, max_desl=max_desl, pouso=pouso,
                   condensou=condensou, previsao_ok=acerto)
        resultados.append(res)

# ---------------- detalhe do melhor caso ----------------------------
ok_runs = [r for r in resultados if r['status'] == 'ok']
cond_runs = [r for r in ok_runs if r.get('condensou')]
if ok_runs:
    base = cond_runs if cond_runs else ok_runs
    melhor = max(base, key=lambda r: abs(r['max_desl'])
                 if np.isfinite(r['max_desl']) else 0.0)
    tr = melhor['traj']
    say("")
    say(f"DETALHE — caso com maior deslocamento"
        f"{' (entre os que CONDENSARAM)' if cond_runs else ''}: "
        f"g={melhor['g_end']}, m_chi^2={melhor['mchi2']}")
    say(f"    {'a':>8} {'r':>8} {'xi':>8} {'H':>8} {'chi/v':>7} "
        f"{'B(r)':>8} {'desl':>10} {'adiab':>8}")
    idx = np.linspace(0, len(tr['a']) - 1, 25).astype(int)
    for i in idx:
        say(f"    {tr['a'][i]:8.3f} {tr['r'][i]:8.4f} {tr['xi'][i]:8.4f} "
            f"{tr['H'][i]:8.4f} {tr['ch'][i]/melhor['v']:7.3f} "
            f"{tr['B'][i]:8.4f} {tr['desl'][i]:+10.2e} {tr['adiab'][i]:8.3f}")
    # janela alvo p/ fase B: |desl| > 50% do maximo
    dabs = np.abs(tr['desl'])
    lim = 0.5 * np.nanmax(dabs)
    dentro = tr['a'][dabs >= lim]
    if len(dentro):
        say("")
        say(f"    JANELA-ALVO (fase B): a em [{dentro.min():.3f}, "
            f"{dentro.max():.3f}]  (|desl| >= 50% do max)")
        mask = dabs >= lim
        say(f"    adiabaticidade na janela: max|chidd/(3H chid)| = "
            f"{np.nanmax(tr['adiab'][mask]):.3f}")

# ---------------- veredito ------------------------------------------
say("")
say("=" * 72)
say("VEREDITO FASE A (criterios pre-declarados)")
say("=" * 72)
say(f"  G2a-SIMB (2a): {'PASSA' if ok_simb else 'FALHA'}")
say(f"  G2a-CONTROLE (2b): {'PASSA' if ok_ctl else 'FALHA'}")
existe = len(ok_runs) > 0
say(f"  G2a-EXISTE (2b): {'PASSA' if existe else 'FALHA'} — "
    f"{len(ok_runs)}/{len(resultados)} trajetorias completas")
condensa = len(cond_runs) > 0
say(f"  G2a-CONDENSA (2b): {'PASSA' if condensa else 'FALHA'} — "
    f"{len(cond_runs)}/{len(ok_runs)} trajetorias completam a condensacao "
    f"(|chi/v| > 0.5)")
previsao = existe and all(r.get('previsao_ok') for r in ok_runs)
say(f"  G2a-PREVISAO (poder): {'PASSA' if previsao else 'FALHA'} — "
    f"o limiar m_chi^2 = {MCHI2_CRIT:.2f} previu condensa/estavel em "
    f"todas as rodadas")
RUIDO = 1e-6
desloca = condensa and any(np.isfinite(r['max_desl'])
                           and abs(r['max_desl']) > RUIDO
                           for r in cond_runs)
say(f"  G2a-DESLOCA (poder): {'PASSA' if desloca else 'FALHA'} — "
    f"o fundo sai dos dois ramos alem do ruido ({RUIDO:g}) DURANTE uma")
say("      condensacao completa (criterio endurecido apos a 1a rodada,")
say("      em que a janela curta so viu o inicio da rolagem)")
pousa = existe and all(np.isfinite(r['pouso']) and r['pouso'] < 1e-2
                       for r in ok_runs)
say(f"  G2a-POUSO (2b): {'PASSA' if pousa else 'FALHA'} — "
    f"chid->0 devolve a trajetoria ao ramo finito")
say("")
if ok_simb and ok_ctl and condensa and desloca:
    say("  >>> FASE A CUMPRIDA: o fundo de rolagem existe, condensa de")
    say("  fato, e genuinamente nao-fatorado durante a condensacao, e a")
    say("  janela-alvo da fase B esta identificada acima. Proximo script:")
    say("  perturbacoes (QEP com chid != 0 e fatias por coeficiente) na")
    say("  janela-alvo — com o diagnostico do balanco (rI) da C1 acoplado.")
    say("  ACHADO ESTRUTURAL da fase A: a interacao HR e uma back-reaction")
    say("  que RESISTE a condensacao de phi_- (limiar m_chi^2 >")
    say(f"  {MCHI2_CRIT:.2f} para v*=1) — a bifurcacao nao e livre; ela")
    say("  compete com o proprio setor que deveria estabilizar.")
elif ok_simb and ok_ctl and existe:
    say("  >>> fundo existe mas nenhuma rodada completou a condensacao")
    say("  com deslocamento genuino — ver limiar e janelas; ajustar knobs")
    say("  (m_chi^2 maior ou v* menor) antes da fase B.")
else:
    say("  >>> fase A NAO cumprida — ver falhas acima. Se G2a-EXISTE")
    say("  falhou em todos os knobs, a inconsistencia do fundo de rolagem")
    say("  e ELA MESMA um resultado (o regime p_phi!=0 nao suporta fundo")
    say("  fisico nesta celula) — documentar com os abortos e fronteiras.")

os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
with open(os.path.join(HERE, "out", "investigacao2_fundo_rolagem.txt"),
          "w", encoding="utf-8") as fh:
    fh.write("\n".join(OUT))
say("")
say("concluido. saida em auditoria/code/out/investigacao2_fundo_rolagem.txt")
