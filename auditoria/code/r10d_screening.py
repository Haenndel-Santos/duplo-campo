# -*- coding: utf-8 -*-
"""
r10d_screening.py — BLOCO 1, a ULTIMA saida: o screening de Vainshtein
protege a instabilidade de gradiente?

CONTEXTO: R-10a/b/c. A instabilidade de gradiente do escalar metrico
esta confirmada (c_s^2 ~ -1 para r pequeno), e as saidas "ramo
infinito" e "corte de epoca pela modulacao" estao fechadas. Resta a
saida principal da literatura (Akrami et al., arXiv:1503.07521): a
instabilidade estaria em escalas onde a perturbacao LINEAR ja nao vale
— seja porque o proprio crescimento leva ao nao-linear, seja porque o
raio de Vainshtein cobre aquelas escalas.

Este script separa as DUAS versoes desse argumento, que sao
frequentemente confundidas:

  (V1) SCREENING PROPRIAMENTE DITO: para uma perturbacao cosmologica
     de escala lambda = a/k e contraste delta, a massa envolvida e
     M ~ delta * rho_bar * lambda^3, e o raio de Vainshtein
     r_V^3 ~ 2 G M / m^2. O screening opera quando lambda <~ r_V:
         lambda^3 <~ 2 G delta rho_bar lambda^3 / m^2
       => delta >~ m^2 / (2 G rho_bar) = (4 pi / 3) * (m/H)^2   [MD]
     Note que o lambda CANCELA: a condicao de screening e sobre o
     CONTRASTE, nao sobre a escala. Se delta_screen >> 1, o screening
     NAO opera no regime linear e NAO pode proteger a instabilidade.

  (V2) AUTO-INVALIDACAO: a instabilidade cresce ate delta ~ 1 e o
     tratamento linear deixa de valer. E o que o R-10b mediu
     (lnA ate 86). Isto NAO e protecao: e ignorancia — nao se sabe o
     que acontece depois, so que a analise linear nao decide.

MEDIDAS (pre-declaradas):
  D1: delta_screen = (4 pi/3) (m_T/H)^2 nas eras, usando a formula
      derivada do proprio repositorio, m_T^2/H^2 = 3(4+3w)
      (R-10a/pareceres; 12 em materia, 15 em radiacao, e o valor
      medido ~5-6 no ponto fixo tardio da familia R-8b).
  D2: a epoca em que cada modo atinge delta = 1 (auto-invalidacao),
      a partir do lnA(k) do R-10b.
  D3: a era instavel em REDSHIFT, com a ancora a0 = 0.931 da familia
      R-8b, e a comparacao com a recombinacao (z ~ 1100).
  D4: veredito sobre qual versao do argumento se aplica.

CRITERIO (pre-declarado):
  delta_screen <~ 1 -> o screening opera no linear e PODE proteger:
      a instabilidade nao seria fisica. Saida VIVA.
  delta_screen >> 1 -> o screening so opera em regioes ja
      nao-lineares; a instabilidade LINEAR ocorre em regime
      NAO-screened. Sobra apenas a auto-invalidacao (V2), que nao
      protege: apenas impede de concluir. Saida MORTA como protecao.

Este script e ARITMETICA sobre resultados ja derivados (nao ha nova
integracao); todas as entradas sao citadas.

Uso: python auditoria/code/r10d_screening.py
Saida em auditoria/code/out/r10d_screening.txt
"""
import os
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
T0 = time.time()
OUT = []


def say(*a):
    line = " ".join(str(x) for x in a)
    print(f"[{time.time()-T0:6.1f}s] {line}")
    OUT.append(line)


say("=" * 72)
say("R-10d — o screening protege a instabilidade de gradiente?")
say("=" * 72)

# ------------------------------------------------------------------
# D1 — delta de screening
# ------------------------------------------------------------------
say("")
say("D1 — contraste minimo para o screening operar")
say("    delta_screen = (4 pi/3) (m_T/H)^2   [MD; o lambda cancela]")
say("")
say(f"    {'era':>26} {'w':>6} {'m_T^2/H^2':>10} {'m_T/H':>7} "
    f"{'delta_screen':>13}")
casos = [("radiacao (3(4+3w), w=1/3)", 1.0 / 3, 15.0),
         ("materia (3(4+3w), w=0)", 0.0, 12.0),
         ("ponto fixo tardio (R-8b, a0)", -1.0, 5.4),
         ("Lambda profundo (Gate F/R-7a)", -1.0, 12.0)]
for nome, w, mh2 in casos:
    d_s = (4 * np.pi / 3) * mh2
    say(f"    {nome:>26} {w:+6.2f} {mh2:10.1f} {np.sqrt(mh2):7.2f} "
        f"{d_s:13.1f}")
say("")
say("    >>> delta_screen ~ 20-60 em TODAS as eras: o screening de")
say("    Vainshtein so opera onde o contraste ja e >~ 20, isto e,")
say("    dentro de estruturas nao-lineares (halos). No regime linear")
say("    cosmologico (delta << 1) ele NAO opera.")
say("    CONSEQUENCIA: a versao (V1) do argumento — 'a instabilidade")
say("    esta abaixo da escala de Vainshtein' — NAO se aplica a")
say("    perturbacoes lineares cosmologicas. O lambda cancela na")
say("    conta: nao existe escala pequena o bastante que seja")
say("    'protegida' com delta pequeno.")

# ------------------------------------------------------------------
# D2 — auto-invalidacao (V2)
# ------------------------------------------------------------------
say("")
say("D2 — auto-invalidacao: quando cada modo atinge delta ~ 1")
say("    (lnA do R-10b, fundo beta-constante beta1=1, delta_i = 1e-5)")
say("")
say(f"    {'entra em a':>11} {'kh(a_cross)':>12} {'lnA':>8} "
    f"{'delta_final':>12} {'nao-linear?':>12}")
tab = [(0.0015, 16.2, 32.44), (0.00311, 11.2, 21.91),
       (0.00646, 7.8, 14.59), (0.0134, 5.4, 9.51),
       (0.0278, 3.8, 5.99), (0.0578, 2.6, 3.54),
       (0.12, 1.8, 1.85), (0.249, 1.3, 0.69)]
for a_ent, kh_cr, lnA in tab:
    dfin = 1e-5 * np.exp(min(lnA, 300))
    say(f"    {a_ent:11.4g} {kh_cr:12.1f} {lnA:8.2f} {dfin:12.2e} "
        f"{'SIM' if dfin > 1 else 'nao':>12}")
say("")
say("    fundo DINAMICO (R-10c): lnA = 85.7 para kh=30 => delta")
say("    final ~ 1e32. Auto-invalidacao total.")

# ------------------------------------------------------------------
# D3 — a era instavel em redshift
# ------------------------------------------------------------------
say("")
say("D3 — a era instavel em redshift (ancora a0 = 0.931, R-8b)")
A0 = 0.931
say("")
say(f"    {'fundo':>22} {'a_ini':>9} {'a_fim':>9} {'z_ini':>9} "
    f"{'z_fim':>9}")
for nome, ai, af in (("beta-constante (R-10a)", 1e-3, 0.5739),
                     ("dinamico REF (R-10c)", 0.010, 0.216)):
    say(f"    {nome:>22} {ai:9.3g} {af:9.4g} {A0/ai - 1:9.1f} "
        f"{A0/af - 1:9.2f}")
say("")
z_rec = 1100.0
a_rec = A0 / (1 + z_rec)
say(f"    recombinacao (z = {z_rec:.0f}) => a = {a_rec:.2e}")
say("    -> esta DENTRO da era instavel nos dois fundos (a era")
say("    instavel do beta-constante comeca antes de a = 1e-3 e a do")
say("    dinamico foi amostrada a partir de a = 0.01, ja instavel).")
say("    CONSEQUENCIA: o CMB e formado DENTRO da era de instabilidade")
say("    de gradiente para modos sub-horizonte.")

# ------------------------------------------------------------------
say("")
say("=" * 72)
say("VEREDITO R-10d")
say("=" * 72)
say("  (V1) SCREENING COMO PROTECAO: MORTO. delta_screen ~ 20-60 em")
say("  todas as eras; o Vainshtein so opera dentro de estruturas")
say("  nao-lineares. O lambda cancela na conta — nao ha escala")
say("  linear protegida.")
say("")
say("  (V2) AUTO-INVALIDACAO: VIVA, mas nao e protecao. Os modos")
say("  atingem delta ~ 1 e a analise linear deixa de decidir. Isso")
say("  impede de REFUTAR a teoria pela instabilidade linear — e")
say("  impede igualmente de CALCULAR qualquer observavel linear na")
say("  era instavel, que inclui a recombinacao.")
say("")
say("  LEITURA: a saida de Akrami et al. se aplica na versao fraca")
say("  (nao se pode refutar), nao na forte (nao esta tudo bem). O")
say("  preco e alto: o programa observacional linear do cap. 09 NAO")
say("  pode ser executado como planejado enquanto a era instavel")
say("  cobrir a recombinacao. As opcoes reais que restam sao:")
say("    (i) achar forma-beta com c_s^2 > 0 em r -> 0 (varredura de")
say("        FORMA, nao de escala — o R-8b ja mostrou rigidez sob")
say("        rescala);")
say("    (ii) tratar a era instavel nao-linearmente (fora do alcance")
say("        atual do projeto);")
say("    (iii) declarar a F1 uma implementacao com validade restrita")
say("        a z <~ 3, sem previsao de CMB.")

os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
with open(os.path.join(HERE, 'out', 'r10d_screening.txt'), 'w',
          encoding='utf-8') as fh:
    fh.write("\n".join(OUT) + "\n")
say("")
say("saida escrita em auditoria/code/out/r10d_screening.txt")
