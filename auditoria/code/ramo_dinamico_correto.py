# -*- coding: utf-8 -*-
"""
ramo_dinamico_correto.py — reavaliacao do ramo dinamico com a
constraint CORRIGIDA (Erratum 01).

Contexto. O Erratum 01 mostrou que a constraint de Bianchi correta e
    B(r) * (N_f adot - N_g bdot) = 0
e nao (H_g - xi H_f). No ramo dinamico correto, xi = bdot/adot, e:

    H_f = adot/b = H_g / r        (com N_g = 1)
    rdot = H_g (xi - r)  != 0     (r EVOLUI)

Combinando as duas Friedmann, H_g^2 se elimina e sobra uma relacao
ALGEBRICA que fixa r pela densidade:

    m^2 M_eff^2 * W(r) = rho,     W(r) = (M_g^2/M_f^2) r^2 V_f(r) - V_g(r)

Este script:
  1. resolve r(a) dessa relacao (cubica, familia F1)
  2. reconstroi H(a), xi(a), rdot(a)
  3. verifica que rdot != 0  (contra a ancora D5, agora superada)
  4. avalia HIGUCHI com o m_T^2 fechado da D2 — no fundo CORRETO
  5. faz um scan em (beta_0, beta_4) procurando regiao viavel

O item 4 e o decisivo: a D8 achou Higuchi violado em 60/60 pontos, mas
naquele fundo xi era imposto por xi = H_g/H_f, que NAO satisfaz a
constraint correta. Refazer no fundo certo pode mudar o veredito.

Requer numpy.  Uso:  python ramo_dinamico_correto.py
"""
import sys

try:
    import numpy as np
except ImportError:
    print("ERRO: precisa de numpy.  pip install numpy")
    sys.exit(2)


# ---------------------------------------------------------------------
# familia F1: (beta_0, beta_1, beta_2, 0, beta_4)
# valores de referencia dos benchmarks D1/D2
# ---------------------------------------------------------------------
B1, B2, B3 = 1.0, -0.4, 0.0
Mg2 = Mf2 = 1.0
Meff2 = 1.0 / (1.0/Mg2 + 1.0/Mf2)     # = 0.5
m2 = 1.0


def V_g(r, b0, b4):
    return b0 + 3*B1*r + 3*B2*r**2 + B3*r**3


def V_f(r, b0, b4):
    return b4 + 3*B3/r + 3*B2/r**2 + B1/r**3


def raizes_r(rho, b0, b4):
    """Todas as raizes reais positivas de  m^2 M_eff^2 W(r) = rho.

    Multiplicando W(r)=rho_til por r:
      (Mg2/Mf2)(b4 r^3 + 3B3 r^2 + 3B2 r + B1)
      - (b0 r + 3B1 r^2 + 3B2 r^3 + B3 r^4) = rho_til * r
    Para F1 (B3=0) fica cubica.
    """
    rt = rho / (m2 * Meff2)
    k = Mg2 / Mf2
    c3 = k*b4 - 3*B2
    c2 = 3*k*B3 - 3*B1
    c1 = 3*k*B2 - b0 - rt
    c0 = k*B1
    raizes = np.roots([c3, c2, c1, c0])
    return sorted(z.real for z in raizes
                  if abs(z.imag) < 1e-9 and z.real > 1e-10)


def resolve_r(rho, b0, b4, r_ref=None):
    """Raiz do RAMO FINITO.

    A cubica tem dois balancos dominantes em rho grande:
        c3 r^3 ~ rho_til r  ->  r ~ sqrt(rho)  -> INFINITO (patologico:
                                                  da xi < 0)
        rho_til r ~ B1      ->  r ~ 1/rho      -> FINITO (fisico)
    Selecao por CONTINUIDADE a partir de r_ref; sem referencia (ponto
    inicial, tempos tardios) pega a MENOR raiz positiva, que e a que
    conecta ao ramo finito.
    """
    rr = raizes_r(rho, b0, b4)
    if not rr:
        return np.nan
    if r_ref is None or not np.isfinite(r_ref):
        return rr[0]
    return min(rr, key=lambda z: abs(z - r_ref))


def fundo(a_grid, rho_m0, b0, b4):
    """Reconstroi r, H, xi, rdot ao longo da grade em a.

    Integra do FUTURO para o PASSADO (rho crescente), seguindo o ramo
    por continuidade — a forma robusta de nao pular de ramo.
    """
    n = len(a_grid)
    r = np.full(n, np.nan)
    ref = None
    for i in range(n-1, -1, -1):                 # de a grande para a pequeno
        r[i] = resolve_r(rho_m0*a_grid[i]**-3, b0, b4, ref)
        if np.isfinite(r[i]):
            ref = r[i]
    ok = np.isfinite(r)
    # H^2 = m^2 M_eff^2 r^2 V_f(r) / (3 M_f^2)      [Friedmann f]
    H2 = m2*Meff2*r**2*V_f(r, b0, b4)/(3*Mf2)
    H = np.where(H2 > 0, np.sqrt(np.abs(H2)), np.nan)
    # xi = r + dr/dN,  N = ln a
    lnA = np.log(a_grid)
    drdN = np.gradient(r, lnA)
    xi = r + drdN
    rdot = H*(xi - r)
    # FILTRO FISICO: xi = N_f/N_g e razao de lapsos -> tem de ser > 0.
    # xi < 0 e a assinatura do ramo infinito (patologico).
    return r, H, xi, rdot, ok & (H2 > 0) & (xi > 0)


def m_T2(r, xi, b0, b4):
    """Forma fechada da ancora D2 (F=1, beta_3=0)."""
    pref = Meff2*(1.0/Mg2 + xi/(Mf2*r**3))
    fator = B1 + B2*(xi + r)          # + B3*xi*r, com B3=0
    return m2*pref*r*fator


def main():
    print("=" * 72)
    print("RAMO DINAMICO CORRETO — reavaliacao pos-Erratum 01")
    print("=" * 72)

    b0, b4 = 1.0, 0.5
    rho_m0 = 0.3
    a_grid = np.logspace(-2, 0.3, 400)

    r, H, xi, rdot, ok = fundo(a_grid, rho_m0, b0, b4)

    print(f"\nparametros: beta_1={B1}, beta_2={B2}, beta_3={B3}, "
          f"beta_0={b0}, beta_4={b4}")
    print(f"            M_g^2=M_f^2={Mg2}, M_eff^2={Meff2}, m^2={m2}")
    print(f"            rho_m0={rho_m0}\n")

    print("(0) DIAGNOSTICO DE RAMO — a cubica tem duas familias\n")
    for a_t in [0.02, 1.0]:
        rr = raizes_r(rho_m0*a_t**-3, b0, b4)
        print(f"    a={a_t:5.2f}  raizes reais positivas: "
              f"{[f'{z:.4f}' for z in rr]}")
    print("\n    r ~ sqrt(rho) -> ramo INFINITO (da xi<0: lapso negativo)")
    print("    r ~ 1/rho     -> ramo FINITO (fisico)")
    print("    Selecao: menor raiz no futuro + continuidade para o passado.\n")

    print("(1) O FUNDO — amostras em a\n")
    print(f"    {'a':>8} {'z':>7} {'r':>9} {'xi':>9} {'H':>9} "
          f"{'rdot':>11} {'m_T^2':>10} {'2H^2':>9}")
    for a in [0.02, 0.05, 0.1, 0.25, 0.5, 1.0, 2.0]:
        i = int(np.argmin(np.abs(a_grid - a)))
        if not ok[i]:
            continue
        mt2 = m_T2(r[i], xi[i], b0, b4)
        print(f"    {a_grid[i]:8.3f} {1/a_grid[i]-1:7.2f} {r[i]:9.4f} "
              f"{xi[i]:9.4f} {H[i]:9.4f} {rdot[i]:11.4e} "
              f"{mt2:10.4f} {2*H[i]**2:9.4f}")

    print("\n(2) rdot != 0 ?  (contra a ancora D5, agora superada)\n")
    i0 = int(np.argmin(np.abs(a_grid - 1.0)))
    nz = np.nanmax(np.abs(rdot[ok]))
    print(f"    max|rdot| na grade = {nz:.4e}")
    print(f"    rdot hoje (a=1)    = {rdot[i0]:.4e}")
    print(f"    xi - r hoje        = {xi[i0]-r[i0]:.4e}")
    print(f"  [{'CONFIRMA' if nz > 1e-6 else 'FALHA   '}] "
          f"r EVOLUI no ramo dinamico correto")
    print("      (a v1 concluia rdot=0 a partir da constraint errada)")

    print("\n(3) SANIDADE: recupera Friedmann padrao em rho grande?\n")
    i_e = 0
    razao = H[i_e]**2 / (rho_m0*a_grid[i_e]**-3/(3*Mg2))
    print(f"    a={a_grid[i_e]:.4f}:  H^2/(rho/3M_g^2) = {razao:.4f}")
    print(f"  [{'OK' if 0.5 < razao < 2 else 'VER'}] "
          f"esperado ~1 se o ramo recupera GR no inicio")

    print("\n(4) HIGUCHI COM O FUNDO CORRETO — o teste decisivo\n")
    print("    (a D8 achou 60/60 violacoes, mas no fundo com xi=H_g/H_f,")
    print("     que nao satisfaz a constraint correta)\n")
    mt2 = m_T2(r, xi, b0, b4)
    hig = mt2 >= 2*H**2
    val = ok & np.isfinite(mt2)
    n_ok = int(np.sum(hig[val]))
    n_tot = int(np.sum(val))
    print(f"    pontos com m_T^2 >= 2H^2:  {n_ok}/{n_tot}")
    print(f"    m_T^2 > 0 em:              {int(np.sum(mt2[val] > 0))}/{n_tot}")
    print(f"    fator estrutural B1+B2(xi+r) hoje = "
          f"{B1 + B2*(xi[i0]+r[i0]):.4f}")
    print(f"  [{'PASSA' if n_ok == n_tot else 'PARCIAL' if n_ok else 'FALHA'}]"
          f" Higuchi neste ponto de parametros")

    print("\n(5) SCAN em (beta_0, beta_4)\n")
    b0s = np.linspace(0.2, 3.0, 15)
    b4s = np.linspace(0.1, 2.0, 15)
    viaveis = []
    for x in b0s:
        for y in b4s:
            rr, HH, xx, _, okk = fundo(a_grid, rho_m0, x, y)
            mm = m_T2(rr, xx, x, y)
            v = okk & np.isfinite(mm)
            if v.sum() < 0.9*len(a_grid):
                continue
            if np.all(mm[v] >= 2*HH[v]**2):
                viaveis.append((x, y))
    print(f"    grade: {len(b0s)}x{len(b4s)} = {len(b0s)*len(b4s)} pontos")
    print(f"    pontos com Higuchi satisfeito em TODA a historia: "
          f"{len(viaveis)}")
    if viaveis:
        print(f"    exemplos: {viaveis[:6]}")
        print()
        print("    *** REGIAO VIAVEL EXISTE ***")
        print("    A D8 concluiu 0/60. No fundo corrigido, a conclusao")
        print("    muda — o que confirma que aquele resultado era")
        print("    artefato do ramo incorreto.")
    else:
        print()
        print("    Nenhum ponto viavel nesta grade. Se o padrao se")
        print("    mantiver em grades maiores, a dificuldade de Higuchi")
        print("    e real e independe do erro da constraint.")

    print("\n" + "=" * 72)
    print("O QUE ISTO DECIDE")
    print()
    print("  Se rdot != 0 e existe regiao com Higuchi: o ramo dinamico")
    print("  corrigido entrega evolucao estrutural SEM precisar de")
    print("  beta_n(phi_-). A arquitetura da v2 fica mais simples — e a")
    print("  motivacao original da TDCP (r evoluindo) se sustenta.")
    print()
    print("  Falta ainda o setor escalar (fantasma/gradiente) neste")
    print("  fundo — a D1 precisa ser refeita aqui. Este script nao")
    print("  substitui isso.")
    print("=" * 72)
    return 0


if __name__ == '__main__':
    sys.exit(main())
