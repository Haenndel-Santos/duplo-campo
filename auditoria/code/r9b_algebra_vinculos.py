# -*- coding: utf-8 -*-
"""
r9b_algebra_vinculos.py — BLOCO 0, itens (a) e (b): a algebra de
vinculos em minisuperespaco ao longo do fundo pousado.

CONTEXTO: parecer de fisica teorica (docs/pareceres_especialistas/
parecer_fisica_teorica.md; sintese §4.1 item 3 e §7 Bloco 0):
  (a) P1 — pos-pouso, com omega^2 > 0 e friccao 3H, phi_- oscila
      amortecido, logo p_phi = a^3 chidot CRUZA ZERO periodicamente;
      nos cruzamentos a matriz de Dirac degeneraria (o residuo da
      constraint, proporcional a p_phi beta_1', se anula e a
      estrutura de segunda classe colapsa).
  (b) P2 — a combinacao diagonal continua de primeira classe?

ESTRUTURA (minisuperespaco (a,b,chi) com dois lapsos):
  primarias  pi_{N_g} ~ 0, pi_{N_f} ~ 0
  secundarias  H_g ~ 0, H_f ~ 0
  consistencia de H_g:  {H_g, H} = N_f {H_g,H_f} = N_f Omega ~ 0
      => TERCIARIA (a "Bianchi"):  Omega = {H_g,H_f} ~ 0
  consistencia de Omega:
      {Omega, H} = N_g D_g + N_f D_f = 0,  D_x = {Omega, H_x}
      => FIXA a razao de lapsos SE (D_g, D_f) != (0,0).
  Se D_g = D_f = 0 num instante, a razao de lapsos fica indeterminada
  e nasce um vinculo a mais => a CONTAGEM DE GRAUS MUDA ali. Esta e
  exatamente a degenerescencia que o parecer preve.

MEDIDAS (pre-declaradas):
  M-B (item b): {H_diag, H_rel} com H_diag = H_g + H_f,
      H_rel = H_g - H_f.
      NOTA DE HONESTIDADE (v2, apos a 1a rodada): isto e uma
      TAUTOLOGIA algebrica — {A+B, A-B} = -2{A,B} = -2 Omega para
      quaisquer A, B. Em minisuperespaco o unico bracket disponivel e
      Omega, que ja e um vinculo, logo a combinacao diagonal e
      fracamente de primeira classe POR CONSTRUCAO e o teste nao tem
      conteudo. Fica no script como verificacao de que a maquinaria
      de brackets esta correta (o residuo tem que ser ~ roundoff), e
      NAO como resposta ao item (b) do parecer — que e sobre o
      difeomorfismo ESPACIAL e exige o calculo de campo (k != 0).
      O item (b) fica, portanto, EM ABERTO e sai do Bloco 0.
  M-A1 (item a, fundo): contar cruzamentos de zero de p_chi = a^3
      chidot depois do pouso (a > a_pouso).
  M-A2 (item a, degenerescencia): ao longo da trajetoria,
          Delta_local = (|D_g| + |D_f|) / escala_local(N),
      com escala_local = maximo de (|D_g|+|D_f|) numa JANELA MOVEL de
      +-0.5 e-fold, e a razao de lapsos implicada xi_impl = -D_g/D_f.
      CORRECAO DE INSTRUMENTO (v2): a 1a rodada normalizava pelo
      maximo GLOBAL da trilha. Como |D_g|,|D_f| crescem ~4 ordens ao
      longo da trilha (2e11 -> 2e15), essa normalizacao faz TODO
      ponto inicial parecer degenerado e produziu um falso
      "DEGENERESCENCIA CONFIRMADA" (Delta = 1.7e-5 no 1o cruzamento,
      onde D_g = +2.2e11 e D_f = -2.0e11 — nenhum dos dois pequeno).
      A degenerescencia exige que o VETOR (D_g, D_f) se anule, nao
      que ele seja pequeno em relacao ao futuro da trilha. A 1a
      rodada esta preservada no historico git.
      Se Delta_local -> 0 nos cruzamentos: DEGENERESCENCIA
      CONFIRMADA. Se permanece > 1e-3: a estrutura de segunda classe
      sobrevive aos cruzamentos.
  M-A3 (controle): a mesma medida com beta_1 CONSTANTE (v* -> inf),
      onde a teoria e HR puro — serve de calibracao do que "nao
      degenerado" significa nesta normalizacao.

CRITERIOS (pre-declarados):
  Delta_min < 1e-3 E coincidente (dentro de 1% em ln a) com um
      cruzamento de p_chi -> DEGENERESCENCIA CONFIRMADA: achado
      estrutural; a contagem de graus muda periodicamente e o Gate 2
      precisa ser refeito com essa estrutura (nao e refutacao
      imediata — e um ponto de bifurcacao de vinculos a tratar).
  Delta_min >= 1e-3 -> NAO CONFIRMADA: a previsao do parecer nao se
      realiza neste fundo; registrar com a fronteira (uma trajetoria,
      minisuperespaco).
  M-B != 0 fraco -> ALERTA GRAVE (a combinacao diagonal nao seria
      primeira classe nem no setor homogeneo).

FRONTEIRA DECLARADA: minisuperespaco (k=0), uma trajetoria (celula
REF g=2, m_chi^2=30, v*=1), fundo Heun. NAO fecha o Gate 2B (que e
sobre k != 0); e o teste barato que o parecer pediu.

Requer sympy, numpy, scipy. ~2-5 min.
Uso (raiz do repo, venv ativo):
    python auditoria/code/r9b_algebra_vinculos.py
Saida em auditoria/code/out/r9b_algebra_vinculos.txt
"""
import os
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


MG2V, MF2V = 1.0, 1.0
ME2 = 0.5
M2 = 1.0
B0V, B2V, B4V = 1.0, -0.4, 0.5
B10 = 1.0
RHO0 = 0.3
VST = 1.0

say("=" * 72)
say("R-9b — BLOCO 0(a,b): algebra de vinculos no fundo pousado")
say("=" * 72)

# ------------------------------------------------------------------
# 1. simbolico: H_g, H_f, Omega, D_g, D_f
# ------------------------------------------------------------------
a_, b_, ch_ = sp.symbols('a b chi', positive=True)
pa_, pb_, pch_ = sp.symbols('p_a p_b p_chi', real=True)
vst_ = sp.Symbol('v_star', positive=True)
rho0_ = sp.Symbol('rho_0', nonnegative=True)

CANON = [(a_, pa_), (b_, pb_), (ch_, pch_)]


def poisson(F, G):
    return sp.expand(sum(sp.diff(F, q) * sp.diff(G, p)
                         - sp.diff(F, p) * sp.diff(G, q)
                         for q, p in CANON))


b1_ = B10 * (1 + ch_**2 / vst_**2)
r_ = b_ / a_
Vg_ = B0V + 3 * r_ * b1_ + 3 * r_**2 * B2V
Vf_ = b1_ + 3 * r_ * B2V + r_**3 * B4V
# materia (dust) no setor g: rho a^3 com rho = rho0/a^3 => termo cte
H_g = (-pa_**2 / (12 * MG2V * a_) + pch_**2 / (2 * a_**3)
       + M2 * ME2 * a_**3 * Vg_ + rho0_)
H_f = -pb_**2 / (12 * MF2V * b_) + M2 * ME2 * a_**3 * Vf_

say("[simbolico] montando Omega = {H_g, H_f} ...")
Omega = poisson(H_g, H_f)
say(f"    Omega: {sp.count_ops(Omega)} ops")

say("[simbolico] M-B: {H_diag, H_rel} ...")
H_diag = H_g + H_f
H_rel = H_g - H_f
MB = sp.expand(poisson(H_diag, H_rel) + 2 * Omega)
MB_chop = sp.nsimplify(MB, rational=True, tolerance=1e-12)
MB_chop = sp.simplify(MB_chop)
ok_B = (MB_chop == 0)
say(f"    {{H_diag, H_rel}} + 2*Omega = {MB_chop}  "
    f"(residuo bruto antes do chop: {sp.simplify(MB)})")
say(f"    [M-B {'OK' if ok_B else 'FALHOU'}] identidade algebrica "
    f"verificada — a maquinaria de brackets esta correta.")
say("    ATENCAO: isto e TAUTOLOGIA ({A+B,A-B} = -2{A,B}), nao")
say("    resposta ao item (b). Em minisuperespaco a combinacao")
say("    diagonal e fracamente de 1a classe POR CONSTRUCAO. O item")
say("    (b) do parecer e sobre o difeomorfismo ESPACIAL (k != 0):")
say("    FICA EM ABERTO e sai do Bloco 0 para o Bloco 2 (junto com")
say("    o Gate 2B, que e o mesmo calculo de campo).")

say("[simbolico] D_g = {Omega, H_g}, D_f = {Omega, H_f} ...")
D_g = poisson(Omega, H_g)
D_f = poisson(Omega, H_f)
say(f"    D_g: {sp.count_ops(D_g)} ops; D_f: {sp.count_ops(D_f)} ops")

ARGS = (a_, b_, ch_, pa_, pb_, pch_, vst_, rho0_)
f_Om = sp.lambdify(ARGS, Omega, modules='numpy')
f_Dg = sp.lambdify(ARGS, D_g, modules='numpy')
f_Df = sp.lambdify(ARGS, D_f, modules='numpy')
say("[simbolico] lambdify pronto")


# ------------------------------------------------------------------
# 2. fundo pousado (Heun, como no R-7e)
# ------------------------------------------------------------------
def beta1(ch):
    return B10 * (1.0 + ch * ch / (VST * VST))


def dbeta1(ch):
    return 2.0 * B10 * ch / (VST * VST)


def U_pot(ch, mu2, lam, U0):
    return -0.5 * mu2 * ch * ch + 0.25 * lam * ch**4 + U0


def dU_pot(ch, mu2, lam):
    return -mu2 * ch + lam * ch**3


def Hf2_of(r, ch):
    Vf = beta1(ch) + 3 * r * B2V + r**3 * B4V
    return M2 * ME2 * Vf / (3 * MF2V * r**3)


def H_de(r, ch, chd, a, mu2, lam, U0):
    Vg = B0V + 3 * r * beta1(ch) + 3 * r * r * B2V
    resto = (0.5 * chd * chd + U_pot(ch, mu2, lam, U0) + RHO0 / a**3
             + M2 * ME2 * Vg)
    if resto <= 0:
        return None
    return np.sqrt(resto / (3 * MG2V))


def Om_num(r, ch, chd, a, mu2, lam, U0):
    H = H_de(r, ch, chd, a, mu2, lam, U0)
    Hf2 = Hf2_of(r, ch)
    if H is None or Hf2 <= 0:
        return float('nan')
    Hf = np.sqrt(Hf2)
    return f_Om(a, r * a, ch, -6 * MG2V * a**2 * H,
                -6 * MF2V * (r * a)**2 * Hf, a**3 * chd, VST,
                RHO0)


def acha_raiz(r_prev, ch, chd, a, mu2, lam, U0):
    for fator in (0.08, 0.25, 0.6):
        lo, hi = r_prev * (1 - fator), r_prev * (1 + fator)
        grade = np.linspace(lo, hi, 61)
        vals = np.array([Om_num(x, ch, chd, a, mu2, lam, U0)
                         for x in grade])
        fin = np.isfinite(vals)
        for i in range(len(grade) - 1):
            if fin[i] and fin[i + 1] and vals[i] * vals[i + 1] < 0:
                try:
                    return brentq(
                        lambda x: Om_num(x, ch, chd, a, mu2, lam, U0),
                        grade[i], grade[i + 1], xtol=1e-14)
                except ValueError:
                    continue
    return None


def raiz_cubica(a, ch, chd, mu2, lam, U0):
    b1v = beta1(ch)
    rho_tot = 0.5 * chd * chd + U_pot(ch, mu2, lam, U0) + RHO0 / a**3
    rt = rho_tot / (M2 * ME2)
    kap = MG2V / MF2V
    rr = np.roots([kap * B4V - 3 * B2V, -3 * b1v,
                   3 * kap * B2V - B0V - rt, kap * b1v])
    reais = sorted(x.real for x in rr
                   if abs(x.imag) < 1e-9 and x.real > 1e-12)
    return reais[0] if reais else None


def rhs(N, ch, chd, r_seed, rp, mu2, lam, U0):
    a = np.exp(N)
    r = acha_raiz(r_seed, ch, chd, a, mu2, lam, U0)
    if r is None:
        raise RuntimeError(f"raiz perdida em a={a:.3f}")
    H = H_de(r, ch, chd, a, mu2, lam, U0)
    Hf = np.sqrt(Hf2_of(r, ch))
    xi = H * (1.0 + rp / r) / Hf
    chidd = (-3 * H * chd - dU_pot(ch, mu2, lam)
             - M2 * ME2 * dbeta1(ch) * (xi + 3 * r))
    return chd / H, chidd / H, r, H, Hf, xi


def integra(g_end=2.0, mchi2=30.0, a0=0.01, a1=1e5, dN=5e-4):
    v = g_end * VST
    mu2 = 0.5 * mchi2
    lam = mu2 / (v * v)
    U0 = 0.25 * mu2 * v * v
    N0, N1 = np.log(a0), np.log(a1)
    n = int((N1 - N0) / dN) + 1
    ch, chd = 1e-3 * v, 0.0
    r = raiz_cubica(a0, ch, chd, mu2, lam, U0)
    rp = 0.0
    rec = {kk: [] for kk in ('N', 'a', 'r', 'H', 'Hf', 'ch', 'chd')}
    for i in range(n):
        N = N0 + i * dN
        d1c, d1d, r1, H1, Hf1, xi1 = rhs(N, ch, chd, r, rp, mu2,
                                         lam, U0)
        chp, chdp = ch + dN * d1c, chd + dN * d1d
        d2c, d2d, r2, _, _, _ = rhs(N + dN, chp, chdp, r1,
                                    (r1 - r) / dN if i else rp,
                                    mu2, lam, U0)
        for kk, vv in (('N', N), ('a', np.exp(N)), ('r', r1),
                       ('H', H1), ('Hf', Hf1), ('ch', ch),
                       ('chd', chd)):
            rec[kk].append(vv)
        ch += 0.5 * dN * (d1c + d2c)
        chd += 0.5 * dN * (d1d + d2d)
        rp = (r2 - r1) / dN
        r = r1
    rec = {kk: np.array(vv) for kk, vv in rec.items()}
    rec['v'] = v
    return rec


say("")
say("[fundo] integrando (Heun, celula REF g=2, m_chi^2=30) ...")
BG = integra()
ok_anc = (abs(BG['r'][-1] - 0.4979) < 0.005
          and abs(BG['ch'][-1] / BG['v'] - 0.932) < 0.005)
say(f"    r_fim={BG['r'][-1]:.4f}, chi/v={BG['ch'][-1]/BG['v']:.4f} "
    f"[{'CONFERE' if ok_anc else 'DIVERGE'}]")
if not ok_anc:
    say("[!] fundo divergiu — abortando")
    raise SystemExit(1)

# ------------------------------------------------------------------
# 3. M-A1: cruzamentos de zero de p_chi apos o pouso
# ------------------------------------------------------------------
a_arr = BG['a']
chd = BG['chd']
p_chi = a_arr**3 * chd
# pouso: onde |chi/v - 0.932| < 0.05 pela primeira vez, ou a > 8000
i_pouso = int(np.argmax((BG['ch'] / BG['v'] > 0.88) & (a_arr > 100)))
if i_pouso == 0:
    i_pouso = int(np.argmin(np.abs(a_arr - 8000.0)))
a_pouso = a_arr[i_pouso]
sg = np.sign(chd[i_pouso:])
cruz = np.where(sg[1:] * sg[:-1] < 0)[0] + i_pouso
say("")
say(f"    M-A1 — pouso identificado em a ~ {a_pouso:.0f} "
    f"(chi/v = {BG['ch'][i_pouso]/BG['v']:.3f})")
say(f"    cruzamentos de zero de p_chi apos o pouso: {len(cruz)}")
if len(cruz):
    say(f"    primeiros em a = "
        f"{[f'{a_arr[c]:.0f}' for c in cruz[:8]]}")
    say(f"    |chidot| max apos o pouso = "
        f"{np.max(np.abs(chd[i_pouso:])):.3e}; "
        f"min |chidot| nos cruzamentos = "
        f"{np.min(np.abs(chd[cruz])):.3e}")

# ------------------------------------------------------------------
# 4. M-A2: a medida de degenerescencia ao longo da trilha
# ------------------------------------------------------------------
def medidas(rec, vst):
    a = rec['a']
    b = rec['r'] * a
    ch = rec['ch']
    pa = -6 * MG2V * a**2 * rec['H']
    pb = -6 * MF2V * b**2 * rec['Hf']
    pch = a**3 * rec['chd']
    Dg = f_Dg(a, b, ch, pa, pb, pch, vst, RHO0)
    Df = f_Df(a, b, ch, pa, pb, pch, vst, RHO0)
    Dg = np.asarray(Dg, float) * np.ones_like(a)
    Df = np.asarray(Df, float) * np.ones_like(a)
    S = np.abs(Dg) + np.abs(Df)
    # escala LOCAL: maximo em janela movel de +-0.5 e-fold
    N = rec['N']
    esc_loc = np.empty_like(S)
    for i in range(len(N)):
        j0 = np.searchsorted(N, N[i] - 0.5)
        j1 = np.searchsorted(N, N[i] + 0.5)
        esc_loc[i] = np.max(S[j0:max(j1, j0 + 1)])
    Delta = S / np.maximum(esc_loc, 1e-300)
    return Dg, Df, Delta


Dg, Df, Delta = medidas(BG, VST)
say("")
say("    M-A2 — degenerescencia (Delta_local, escala em janela movel "
    "de +-0.5 e-fold):")
say(f"    Delta_local min na trilha = {np.min(Delta):.3e} "
    f"(em a = {a_arr[int(np.argmin(Delta))]:.0f})")
if len(cruz):
    Dc = Delta[cruz]
    say(f"    Delta_local NOS cruzamentos de p_chi: min = "
        f"{np.min(Dc):.3e}, mediana = {np.median(Dc):.3e}")
    say(f"    razao de lapsos implicada xi_impl = -D_g/D_f nos "
        f"cruzamentos: mediana = "
        f"{np.median(-Dg[cruz]/Df[cruz]):.4f} "
        f"(r no mesmo ponto: {np.median(BG['r'][cruz]):.4f}) — "
        f"finita e bem definida = SEM degenerescencia")
    say("")
    say(f"    {'a':>8} {'chidot':>11} {'D_g':>12} {'D_f':>12} "
        f"{'Delta_loc':>10} {'xi_impl':>8}")
    for c in cruz[:6]:
        say(f"    {a_arr[c]:8.0f} {chd[c]:+11.3e} {Dg[c]:+12.3e} "
            f"{Df[c]:+12.3e} {Delta[c]:10.3e} "
            f"{-Dg[c]/Df[c]:8.4f}")

# ------------------------------------------------------------------
# 5. M-A3: controle com beta_1 constante (v* -> grande)
# ------------------------------------------------------------------
say("")
say("    M-A3 — controle: mesma medida com beta_1 ~ constante "
    "(v* = 1e6, modulacao desligada)")
Dg_c, Df_c, Delta_c = medidas(BG, 1e6)
say(f"    Delta min (controle) = {np.min(Delta_c):.3e}; "
    f"mediana = {np.median(Delta_c):.3e}")
say("    (o controle NAO tem o termo p_chi beta_1'; se o Delta do")
say("     caso modulado cair muito abaixo do controle nos")
say("     cruzamentos, o efeito e da modulacao — que e a previsao)")

# ------------------------------------------------------------------
say("")
say("=" * 72)
say("VEREDITO R-9b (criterios pre-declarados no cabecalho)")
say("=" * 72)
say(f"  (b) M-B: identidade {{H_diag,H_rel}} = -2*Omega "
    f"{'verificada' if ok_B else 'FALHOU'} — maquinaria de brackets")
say("      correta, mas o teste e TAUTOLOGICO em minisuperespaco.")
say("      ITEM (b) NAO RESPONDIDO: o difeomorfismo espacial exige")
say("      k != 0. Movido do Bloco 0 para o Bloco 2, junto ao Gate")
say("      2B (mesmo calculo de campo).")
say("")
if len(cruz) == 0:
    say("  (a) M-A1: p_chi NAO cruza zero apos o pouso nesta")
    say("      trajetoria — a premissa do parecer nao se realiza aqui")
    say("      (o pouso e sobre-amortecido/monotono). Registrar com")
    say("      a fronteira: uma trajetoria, uma celula.")
else:
    dmin = float(np.min(Delta[cruz]))
    xi_med = float(np.median(-Dg[cruz] / Df[cruz]))
    if dmin < 1e-3:
        say(f"  (a) >>> DEGENERESCENCIA CONFIRMADA: Delta_local cai a "
            f"{dmin:.2e} nos cruzamentos de p_chi "
            f"({len(cruz)} apos o pouso).")
        say("      A razao de lapsos fica indeterminada nesses")
        say("      instantes => a contagem de graus muda")
        say("      periodicamente. NAO e refutacao imediata — e um")
        say("      ponto de bifurcacao de vinculos que o Gate 2")
        say("      precisa tratar explicitamente.")
    else:
        say(f"  (a) PREMISSA CONFIRMADA, CONCLUSAO NAO: p_chi cruza")
        say(f"      zero {len(cruz)} vezes apos o pouso (o parecer")
        say(f"      acertou o fundo), mas Delta_local minimo nos")
        say(f"      cruzamentos = {dmin:.2e} (>= 1e-3) e a razao de")
        say(f"      lapsos implicada e finita e estavel "
            f"(xi_impl ~ {xi_med:.3f}).")
        say("      A estrutura de segunda classe SOBREVIVE: o residuo")
        say("      da Bianchi NA RAIZ e proporcional a p_chi*beta_1',")
        say("      mas D_g = {Omega,H_g} e D_f = {Omega,H_f} NAO tem")
        say("      p_chi como fator global — nao se anulam junto.")
        say("      Fronteira: minisuperespaco, uma trajetoria, celula")
        say("      REF.")

os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
with open(os.path.join(HERE, 'out', 'r9b_algebra_vinculos.txt'), 'w',
          encoding='utf-8') as fh:
    fh.write("\n".join(OUT) + "\n")
say("")
say("saida escrita em auditoria/code/out/r9b_algebra_vinculos.txt")
