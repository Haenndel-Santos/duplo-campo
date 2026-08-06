# Derivação 8 — A Faixa m_S0 ~ (30–300)H₀ é Derivável da Dinâmica?

**Skill invocado:** `eft-and-screening-validator`.
**Script:** `code/08_mS0_background_scan.py` (saída: `code/out/08_output.txt`;
plug-in de m_T² já com o resultado real da Derivação 2).

## 1. O que está sendo derivado e por que é necessário

O Cap.19 usa $m_{S0}\sim(30\text{–}300)H_0$ como benchmark central do
confronto observacional (B1/B2). O prompt pede derivar essa faixa da
dinâmica real de F(φ) e do fundo, em vez do ajuste a posteriori.

## 2. Achado documental (P8.0/E8.d)

No próprio Cap.19 §19.1–19.3 a faixa **não é dinâmica**: ela é obtida
invertendo a posição desejada do "joelho Yukawa" dentro da janela de
LSS, $k_\star\in[0.01,0.1]\,h/\mathrm{Mpc}$, com
$k_{H0}\approx3.3\times10^{-4}\,h/\mathrm{Mpc}$:
$0.01/k_{H0}\approx30$ e $0.1/k_{H0}\approx300$. É **design
observacional** — escolhe-se onde se quer o joelho e lê-se m_S0.

## 3. Resultados do scan de fundo (rodada executada)

Sistema do Anexo E integrado em N=ln a (ramo algébrico, F(χ)=e^{λχ},
U=U₀e^{−λ_Uχ}, grade 60 combinações), com os vínculos E8.c:

1. **Ramo algébrico exato (β_n constantes): $m_S\equiv0$
   identicamente** sob a proporcionalidade do Cap.15 §15.5
   ($\beta_1+2\beta_2r_\star=0$ por definição da raiz). Nenhuma faixa é
   derivável nesse ramo.
2. **Higuchi com o m_T² real (Derivação 2, dependente de ξ): violado em
   toda a grade** — nenhuma trajetória viável (a coluna Higuchi=False
   em 60/60 casos). O fundo consegue chegar perto de
   (H₀, Ω_m0, w₀) razoáveis (ex.: m²=1, λ_F=1, U₀=1 → H₀=1.004,
   Ω_m=0.298, w=−0.71), mas nunca passa o conjunto completo de filtros.

## 4. Supersedência pelas Derivações 1 e 6

A pergunta "qual m_S0?" **pressupõe** que μ tem a forma Yukawa de 1 polo
com uma única massa m_S(a). As Derivações 1 e 6 mostraram que:

- não existe "o" modo relativo com $m_S^2\propto\beta_1+2\beta_2r$
  (setor relativo é um par patológico — fantasma no ramo dinâmico,
  degenerado na raiz algébrica);
- μ real tem ~7 polos com $\alpha_\infty=0$ — não existe um único
  "joelho Yukawa" a posicionar.

Portanto a faixa (30–300)H₀ não é derivável **nem em princípio** na
formulação atual: o objeto que ela parametriza não sobrevive à
derivação.

## 5. Resultado final

$$ \boxed{\ m_{S0}\sim(30\text{–}300)H_0\ \text{é uma escolha de design observacional (posição do joelho),}\ } $$
$$ \boxed{\ \text{não uma consequência da dinâmica — e o joelho único que ela posiciona não existe na teoria derivada.}\ } $$

## 6. Classificação final

**NÃO DERIVÁVEL SEM DADO EXTERNO** — em três camadas independentes:
(i) o corpus não fixa F(χ) nem U(χ) (entradas livres do Anexo E §E.8);
(ii) mesmo com formas de referência declaradas, o scan não produz
região viável (Higuchi com o m_T² real falha em toda a grade; na raiz
exata m_S≡0); (iii) a própria parametrização-alvo (Yukawa de 1 polo)
foi refutada pelas Derivações 1/6. O Cap.19 deve reclassificar
(30–300)H₀ como benchmark de projeto e reconstruir o confronto sobre a
forma multi-polo derivada.
