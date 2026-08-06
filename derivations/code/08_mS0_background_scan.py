# -*- coding: utf-8 -*-
"""
08_mS0_background_scan.py — Derivacao 8 (plano P8.0–P8.5).

Pergunta: a dinamica de F(chi) + fundo cosmologico produz naturalmente
m_S0 ~ (30–300) H_0, ou essa faixa e uma escolha observacional externa
(Cap.19 §19.1–19.3)?

ESTRUTURA (e o achado estrutural ja antecipado no plano):
  - Ramo algebrico exato (F1, beta_n constantes): r = r_star = -b1/(2b2)
    e CONSTANTE, e o fator (beta1 + 2 beta2 r_star) = 0 IDENTICAMENTE.
    Se m_S^2 for proporcional a esse fator (Cap.15 §15.5), entao
    m_S == 0 no ramo algebrico exato — nenhuma faixa de m_S0 e
    derivavel. O script verifica e reporta isso explicitamente.
  - Modo exploratorio (OFFSET_DELTA != 0): r = r_star (1 + delta) fixo,
    fora do ramo exato (hipotese adicional declarada), para quantificar
    a sensibilidade de m_S0 ao desvio da raiz.

HIPOTESES ADICIONAIS DECLARADAS (P8.0): o corpus nao fixa F(chi) nem
U(chi); usamos as formas de referencia
    F(chi) = exp(lamF chi / M_g),   U(chi) = U0 exp(-lamU chi / M_g).

PLUG-INS (atualizar com os resultados dos scripts 01/02/06):
    CS_NORM : normalizacao de m_S^2 = CS_NORM * m^2 F * (b1 + 2 b2 r)
    MT2     : formula de m_T^2 (default: resultado derivado no script 02)
    ALPHA   : formula de alpha(a) (default: parametrizacao Cap.18 §18.4)

Fundo integrado (tempo cosmico, unidades H0=1, Mg=1):
    H^2 = (rho_m + chidot^2/2 + U + rho_int)/3,
    rho_int = m2 Meff2 F(chi) (b0 + 3 b1 r + 3 b2 r^2)      [Derivacao 3]
    chidd = -3 H chidot - U' - m2 Meff2 F'(chi) V(xi, r)     [sinal da acao]
    H_f^2 = m2 Meff2 F (b4 + 3 b2/r^2 + b1/r^3)/(3 Mf2)     [F.4]
    xi = H/H_f                                               [ramo dinamico]
    etadot = Gamma chidot^2                                  [passivo]

Uso:  python 08_mS0_background_scan.py   (saida em out/08_output.txt)
"""
import os
import numpy as np
from scipy.integrate import solve_ivp

OUT = []


def say(*args):
    line = " ".join(str(x) for x in args)
    print(line)
    OUT.append(line)


# ----------------------------------------------------------------------
# PLUG-INS (defaults; substituir pelos resultados de 01/02/06)
# ----------------------------------------------------------------------
CS_NORM = 1.0          # m_S^2 = CS_NORM * m2 * F * (b1 + 2 b2 r)  [Cap.15 §15.5]
OFFSET_DELTA = 0.0     # 0 = ramo algebrico exato; !=0 = exploratorio


def MT2(m2_, Meff2_, F_, r_, xi_, Mg2_, Mf2_, b1_, b2_):
    """m_T^2 derivado no script 02 (F1: beta3=0)."""
    return (m2_ * Meff2_ * F_ * (1.0 / Mg2_ + xi_ / (Mf2_ * r_**3))
            * r_ * (b1_ + b2_ * (xi_ + r_)))


def ALPHA(r_, Mg2_, Mf2_):
    """alpha(a) — parametrizacao do Cap.18 §18.4 (substituir pela D6)."""
    e2 = Mf2_ * r_**2 / Mg2_
    return e2 / (1.0 + e2)


# ----------------------------------------------------------------------
# fundo
# ----------------------------------------------------------------------
def run_background(params, a_ini=1e-3, a_end=1.0):
    """
    Integra o fundo em N = ln a. Retorna dict com trajetorias ou None
    se a integracao falhar (H^2 < 0 etc.).
    """
    m2_ = params['m2']
    lamF = params['lamF']
    lamU = params['lamU']
    U0 = params['U0']
    Gam = params['Gamma']
    b0_, b1_, b2_, b4_ = params['b0'], params['b1'], params['b2'], params['b4']
    Mf2_ = params['Mf2']
    Meff2_ = 1.0
    Mg2_ = 1.0
    rho_m0 = params['rho_m0']

    r_star = -b1_ / (2.0 * b2_)
    r_ = r_star * (1.0 + OFFSET_DELTA)

    Pg = b0_ + 3 * b1_ * r_ + 3 * b2_ * r_**2
    Pf = b4_ + 3 * b2_ / r_**2 + b1_ / r_**3
    if Pf <= 0:
        return None

    def F(chi):
        return np.exp(lamF * chi)

    def U(chi):
        return U0 * np.exp(-lamU * chi)

    def H2_of(N, chi, chid):
        rho_m = rho_m0 * np.exp(-3 * N)
        rho_int = m2_ * Meff2_ * F(chi) * Pg
        return (rho_m + 0.5 * chid**2 + U(chi) + rho_int) / (3.0 * Mg2_)

    def rhs(N, y):
        chi, chid, eta = y
        H2 = H2_of(N, chi, chid)
        if H2 <= 0:
            return [np.nan] * 3
        H = np.sqrt(H2)
        Hf = np.sqrt(m2_ * Meff2_ * F(chi) * Pf / (3.0 * Mf2_))
        xi = H / Hf
        V = (b0_ + b1_ * (xi + 3 * r_) + b2_ * (3 * xi * r_ + 3 * r_**2)
             + b4_ * xi * r_**3)
        Up = -lamU * U(chi)
        Fp = lamF * F(chi)
        chidd = -3 * H * chid - Up - m2_ * Meff2_ * Fp * V
        # d/dN = (1/H) d/dt
        return [chid / H, chidd / H, Gam * chid**2 / H]

    Ni, Ne = np.log(a_ini), np.log(a_end)
    sol = solve_ivp(rhs, (Ni, Ne), [params['chi_i'], 0.0, 0.0],
                    rtol=1e-8, atol=1e-10, dense_output=True, max_step=0.05)
    if not sol.success or np.any(np.isnan(sol.y)):
        return None

    Ns = np.linspace(Ni, Ne, 400)
    chi, chid, eta = sol.sol(Ns)
    H2s = np.array([H2_of(N, c, cd) for N, c, cd in zip(Ns, chi, chid)])
    if np.any(H2s <= 0):
        return None
    Hs = np.sqrt(H2s)
    Fs = F(chi)
    Hfs = np.sqrt(m2_ * Meff2_ * Fs * Pf / (3.0 * Mf2_))
    xis = Hs / Hfs
    rho_m = rho_m0 * np.exp(-3 * Ns)
    Om = rho_m / (3 * Mg2_ * H2s)
    # w_eff via d ln H / dN
    dlnH = np.gradient(np.log(Hs), Ns)
    w_eff = -1.0 - (2.0 / 3.0) * dlnH

    mS2 = CS_NORM * m2_ * Fs * (b1_ + 2 * b2_ * r_)
    mT2 = MT2(m2_, Meff2_, Fs, r_, xis, Mg2_, Mf2_, b1_, b2_)
    alpha = ALPHA(r_, Mg2_, Mf2_)

    return dict(N=Ns, H=Hs, Om=Om, w_eff=w_eff, chi=chi, eta=eta,
                mS2=mS2, mT2=mT2, alpha=alpha, xi=xis, r=r_,
                fator=b1_ + 2 * b2_ * r_, params=params)


def viable(tr):
    """filtros de viabilidade (E8.c + normalizacao de fundo)."""
    H0 = tr['H'][-1]
    Om0 = tr['Om'][-1]
    w0 = tr['w_eff'][-1]
    checks = {
        'H0 ~ 1 (0.8-1.2)': 0.8 <= H0 <= 1.2,
        'Omega_m0 ~ 0.3 (0.25-0.35)': 0.25 <= Om0 <= 0.35,
        'w_eff0 ~ -1 (-1.15,-0.85)': -1.15 <= w0 <= -0.85,
        'eta < 1 sempre': np.all(tr['eta'] < 1.0),
        'sem ghost escalar (fator>0)': tr['fator'] > 0 or abs(tr['fator']) < 1e-12,
    }
    return checks


def main():
    say("=" * 70)
    say("DERIVACAO 8 — m_S0 a partir da dinamica de F(chi) e do fundo")
    say("=" * 70)
    say("")
    say(f"config: CS_NORM = {CS_NORM}, OFFSET_DELTA = {OFFSET_DELTA}")
    say("")

    # ------------------------------------------------------------------
    # achado estrutural (P8.0/P8.1)
    # ------------------------------------------------------------------
    b1_, b2_ = 1.0, -0.4
    r_star = -b1_ / (2 * b2_)
    fator_na_raiz = b1_ + 2 * b2_ * r_star
    say("ACHADO ESTRUTURAL:")
    say(f"  ramo algebrico exato: r_star = {r_star}, "
        f"beta1 + 2 beta2 r_star = {fator_na_raiz}")
    say("  => se m_S^2 ~ (beta1+2 beta2 r) (Cap.15 §15.5), entao m_S = 0")
    say("     IDENTICAMENTE no ramo algebrico exato de F1 com beta_n")
    say("     constantes. A faixa m_S0 ~ 30-300 H0 do Cap.19 NAO e")
    say("     derivavel nesse ramo — ela exige (a) desvio da raiz, ou")
    say("     (b) beta_n(phi) com raiz movel (Derivacao 5 §4.1), ou")
    say("     (c) m_S^2 real com termos alem do fator (verificar na D1).")
    say("")
    if OFFSET_DELTA == 0.0:
        say("  [OFFSET_DELTA = 0: o scan abaixo confirma m_S = 0 exato;")
        say("   rode novamente com OFFSET_DELTA = 0.02 etc. p/ o modo")
        say("   exploratorio fora da raiz]")
    say("")

    # ------------------------------------------------------------------
    # varredura de parametros
    # ------------------------------------------------------------------
    say("varredura (grade modesta; unidades H0-alvo = 1, Mg=1, Meff=1):")
    say("")
    grid_m2 = [0.5, 1.0, 3.0, 10.0, 100.0]
    grid_lamF = [-1.0, -0.3, 0.3, 1.0]
    grid_U0 = [0.5, 1.0, 2.0]
    base = dict(b0=-1.0, b1=b1_, b2=b2_, b4=0.5, Mf2=1.0,
                lamU=1.0, Gamma=0.1, chi_i=0.0, rho_m0=0.9)

    resultados = []
    n_run = n_ok = 0
    for m2_ in grid_m2:
        for lamF in grid_lamF:
            for U0 in grid_U0:
                p = dict(base, m2=m2_, lamF=lamF, U0=U0)
                tr = run_background(p)
                n_run += 1
                if tr is None:
                    continue
                ch = viable(tr)
                ok = all(ch.values())
                if ok:
                    n_ok += 1
                H0 = tr['H'][-1]
                mS0 = (np.sqrt(tr['mS2'][-1]) / H0
                       if tr['mS2'][-1] > 0 else 0.0)
                # p_eff = -dln m_S/dln a hoje
                if np.all(tr['mS2'] > 0):
                    lnmS = 0.5 * np.log(tr['mS2'])
                    p_eff = -np.gradient(lnmS, tr['N'])[-1]
                else:
                    p_eff = np.nan
                hig = np.all(tr['mT2'] >= 2 * tr['H']**2)
                resultados.append((p, tr, ch, ok, mS0, p_eff, hig))

    say(f"integracoes: {n_run}; trajetorias viaveis (todos os filtros): {n_ok}")
    say("")
    say("  m2     lamF   U0   | H0     Om0    w0     | mS0/H0  p_eff  "
        "Higuchi | viavel")
    say("  " + "-" * 78)
    for p, tr, ch, ok, mS0, p_eff, hig in resultados:
        H0 = tr['H'][-1]
        say(f"  {p['m2']:6.1f} {p['lamF']:+5.1f} {p['U0']:4.1f} | "
            f"{H0:6.3f} {tr['Om'][-1]:6.3f} {tr['w_eff'][-1]:+6.2f} | "
            f"{mS0:7.3f} {p_eff:6.2f}  {str(hig):7s} | {ok}")

    say("")
    viaveis = [x for x in resultados if x[3]]
    if viaveis:
        mS0s = [x[4] for x in viaveis]
        say(f"faixa de m_S0/H0 na regiao viavel: "
            f"[{min(mS0s):.3f}, {max(mS0s):.3f}]")
        say("comparar com o benchmark observacional (30-300)H0 do Cap.19.")
    else:
        say("nenhuma trajetoria passou todos os filtros nesta grade —")
        say("relaxar grade/filtros ou usar OFFSET_DELTA != 0.")

    say("")
    say("NOTA (P8.5): a faixa 30-300 H0 do Cap.19 e derivada da POSICAO")
    say("do joelho Yukawa dentro de k em [0.01, 0.1] h/Mpc (design")
    say("observacional), nao da dinamica. Este scan mostra o que a")
    say("dinamica com as hipoteses declaradas produz de fato.")

    os.makedirs("out", exist_ok=True)
    with open("out/08_output.txt", "w", encoding="utf-8") as fh:
        fh.write("\n".join(OUT))
    say("\nconcluido. saida em out/08_output.txt")


if __name__ == '__main__':
    main()
