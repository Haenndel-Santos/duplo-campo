# Setor Escalar no Ramo Finito — Resultado da Sondagem

**Data:** 2026-08-07. Script: `auditoria/code/d1_ramo_finito.py`
(rodada 2; saída em `auditoria/code/out/d1_ramo_finito.txt`).
Companheiro de `resultado_ramo_finito.md` — este é o teste da metade
escalar do antigo "duplamente morto".

---

## 1. Placar honesto

| Setor | Fundo errado (v1/D1) | Ramo finito correto |
|---|---|---|
| Fundo (ṙ, limite GR) | ṙ≡0 (premissa errada) | ṙ≠0, GR exato ✓ |
| Tensorial (Higuchi) | violado (m_T²<0) | **400/400 ✓** |
| **Escalar (par relativo)** | par fantasma/taquiônico | **taquião persiste** ✗ |

**O fundo correto curou Higuchi mas não curou o par escalar.** A
patologia do setor relativo é mais robusta que a escolha de fundo.

## 2. O que exatamente foi encontrado

Três pontos (a=0.5, 1, 2), maquinaria idêntica à D1 (auto-teste GR
aprovado, espectador δχ calibrando exato em todos os pontos:
c_s²=1.000000, m²=+0.300, kN=+0.5).

O par relativo:

- **massa taquiônica** m² ≈ −67.8 (a=0.5), −8.45 (a=1), −4.78 (a=2);
- **normas cinéticas quase nulas** de sinais mistos (10⁻³–10⁻⁸) —
  regime quase-degenerado;
- **ω² complexos** para k≥10, em pares conjugados;
- **c² = ξ²/r² exato** em todos os pontos (2.0726 em a=1, conferindo
  com a previsão estrutural impressa) — o par propaga no cone causal
  do setor f, mesma assinatura da D1/D2. A maquinaria mede o objeto
  certo.

## 3. A estrutura da instabilidade — três fatos que restringem o diagnóstico

**(i) NÃO é catástrofe UV.** Im(ω)/H é aproximadamente constante em k
(a=1: 3.88 em k=10, 3.90 em k=100, 2.60 em k=1000), não crescente.
Instabilidade de gradiente teria Im(ω)∝k. Excluída.

**(ii) A taxa é √|m²| — um taquião genuíno.** Verificação nos três
pontos: √67.8/1.015=8.1 ✓ (medido 8.1); √8.45/0.627=4.6 ✓ (medido
3.9–4.6); √4.78/0.566=3.9 ✓ (medido 3.8–3.9). Em k alto o taquião se
mistura em pares complexos preservando a taxa.

**(iii) Enfraquece rumo ao ponto fixo.** Taxa ~6.6H em a=0.5 → ~3.9H
em a=1 → ~3.1H em a=2; e em a=2, k=1000, os modos caem para
Im(ω)/H≈0.83 (**inofensivo**). O padrão: instável enquanto r evolui
rápido, estabilizando quando r assenta.

## 4. Caveats — por que isto ainda não é veredito final

1. **Fundo congelado com |Ḣ/H²|≈0.3.** As taxas encontradas são
   ~poucos×H — exatamente a escala onde o congelamento é menos
   confiável. **Teste de robustez pendente** (v3 do script: a=1
   congelado vs. taxas verdadeiras, lado a lado).
2. **Normas cinéticas quase nulas.** O par está quase desacoplado
   (kN ~ 10⁻⁴–10⁻⁸ contra 0.5 do espectador). Perto de norma zero, a
   análise quadrática é marginal — e o dano observável depende do
   acoplamento aos setores físicos, não só da taxa. Uma análise tipo
   D6 (resposta μ) neste fundo diria se a instabilidade vaza para os
   observáveis.
3. **Nota de literatura (Nível 3, a verificar):** o ramo finito da
   cosmologia bimétrica é conhecido por ter instabilidade escalar em
   tempos primordiais que desliga em tempos tardios. O padrão
   encontrado é qualitativamente parecido; a versão conhecida é de
   gradiente (∝k), a nossa satura em √|m²|. Não usar como argumento
   até conferir na fonte.

## 5. Interpretações em aberto

**(a) Reparo por modulação** — a rota do plano v2. O taquião reativa
`β_n(φ₋)` como mecanismo de reparo, agora por motivo **verificado**
(era por premissa herdada). O Gate 2 Parte B (constraint secundária no
ADM) volta a ser o próximo obstáculo técnico.

**(b) O taquião É a bifurcação (Nível 3 — especulação, registrada
com o rótulo).** Um modo relativo taquiônico, forte no início e
enfraquecendo conforme a estrutura assenta, é a narrativa do Cap.1
("estado primordial instável no modo diferencial → separação →
estabilização") em linguagem de perturbação. Se o taquião condensa —
rola para um vácuo com ⟨modo relativo⟩≠0, como no potencial
V(φ₊,φ₋) da v2 — a instabilidade é o mecanismo fundacional, não um
defeito. **Obstáculo:** em a=1 a taxa ainda é 3.9H; sem um mecanismo
de saturação, é tarde demais. As duas leituras convergem para a mesma
matemática: o setor relativo precisa de um potencial que o estabilize
— que é o que a modulação fornece.

## 6. Decisão de gate

**Gate "setor escalar do ramo finito puro" (β_n constantes): NÃO PASSA
nesta sondagem** — pendente do teste de robustez do congelamento (v3).

Se a v3 confirmar o taquião: a TDCP-F1 com β_n constantes é
inconsistente no setor escalar, e a v2 (modulação) deixa de ser
opcional. Se a v3 desfizer o taquião: o congelamento era o artefato, e
o ramo finito puro segue vivo — nesse caso, próxima verificação é uma
análise com evolução temporal genuína (não-QEP).

---

## 7. FECHAMENTO (2026-08-07, `evolucao_temporal_escalar.py`)

Dois episódios de método antes do resultado, registrados porque fazem
parte dele:

- A v3 do teste de robustez era **vácua**: alimentar Ḣ/Ḣ_f/ξ̇
  verdadeiros deu saída bit a bit idêntica — a forma Γ–Γ só tem
  primeiras derivadas do fundo, então as matrizes não contêm esses
  símbolos. O congelamento está no ansatz, não nos valores.
- A integração DAE (v1 do script de evolução) morreu no próprio
  auto-teste: os multiplicadores **não** têm linhas nulas de K
  (velocidades de lapso/shift aparecem em termos cruzados na Γ–Γ); o
  espaço nulo é não-alinhado e gira com o fundo. A guarda abortou
  alto, como desenhada.

O caminho que decidiu: **rastreio σ(N) denso (47 pontos, a=0.1→10)
com adiabaticidade, e o ponto fixo como juiz assintótico.**

### O veredito

$$\boxed{\ \sigma/H \approx 3.0\text{–}3.7\ \text{no ponto fixo }(a=10,\ r=r_\infty=0.3323,\ \dot r\approx0)\ }$$

nos três k testados (1, 10, 100). No ponto fixo o fundo é
quase-de Sitter **exato** — o congelamento não é aproximação ali. Logo:

**O taquião é genuíno e eterno. O ramo finito puro (β_n constantes)
REPROVA o setor escalar. Definitivo — sem caveat de congelamento.**

Dados de suporte:

- adiabaticidade η = 0.31–0.58 para k=10, 100 (congelado confiável em
  toda a trajetória; o η=7.1 de k=1 vem de um único ponto de grade com
  provável artefato de agrupamento — ver nota abaixo);
- crescimento acumulado na janela observacional (a=0.25→2):
  **ln A ≈ 10** (amplificação ~2×10⁴) — catastrófico para teoria
  linear se o modo acopla aos observáveis;
- auto-teste: rota lambdify reproduziu a rodada 2 (rota sympy-subs
  independente) em a=1, k=1.

**Nota de qualidade de dados:** o ponto (k=1, a≈0.50) mostra
σ/H=2.06, inconsistente com a rodada 2 no mesmo instante (8.1) e com
os vizinhos da própria trilha — provável artefato de agrupamento de
modos em k baixo, onde há cruzamentos violentos. As trilhas k=10 e
k=100 são lisas e batem com a rodada 2. O veredito do ponto fixo não
depende desse ponto.

### Placar final do ramo finito puro

| Teste | Resultado |
|---|---|
| Evolução estrutural (ṙ≠0) | ✓ |
| Limite GR primordial | ✓ (exato) |
| Higuchi / setor tensorial | ✓ (400/400) |
| **Setor escalar** | **✗ — taquião eterno, σ≈(3–4)H** |

### Consequência para o plano v2

A modulação β_n(φ₋) **deixa de ser opcional**: é o mecanismo de
estabilização necessário, agora com motivação verificada em três
níveis (o taquião existe; persiste no ponto fixo; e o canal de
acoplamento entre o par relativo e φ₋ é exatamente o termo
p_φ·β₁′ que o Gate 2 encontrou na constraint secundária).

E a convergência registrada na §5(b) ganha força: a teoria com β_n
constantes tem uma direção taquiônica no modo relativo; o potencial
V(φ₊,φ₋) da v2 é, por construção, um estabilizador de direção
taquiônica (quártica + condensação). O reparo e a narrativa da
bifurcação são a mesma matemática. **Próximo passo computacional:**
estender a maquinaria de perturbações para modulação por coeficiente
(β₁(φ₋) individual, não F global) e verificar se existe
(v_∗, λ₋, λ_c, μ₋) que positiviza o par no fundo com ⟨φ₋⟩=v — o
Gate 4 do plano renasce como "estabilização verificada".
