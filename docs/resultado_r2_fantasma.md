# R-2 — O Fantasma Estrutural: Caracterização e Limites — Resultado

**Data:** 2026-08-11 (noite). Script:
`auditoria/code/r2_fantasma_estrutural.py` (saída em
`auditoria/code/out/r2_fantasma_estrutural.txt`). Execução em sessão
autorizada. **Este documento corrige a leitura do próprio veredito
impresso pelo script** — parte dos critérios codificados revelou-se
poluída por normalização, e o registro disso é parte do resultado
(mesmo padrão do dia: o instrumento sob escrutínio).

---

## 1. O que ficou estabelecido (invariante, 2b)

1. **A direção cinética negativa é robusta como ASSINATURA** — o
   invariante de Sylvester (nº de autovalores negativos de K_red):
   - uniforme em k: 1 direção negativa em TODOS os k_c∈{1..300}
     (REF μ=1, a=400) — a velha ambiguidade do kN (que flipava com k
     no espaço de 7 campos) **não existe no sistema reduzido**;
   - persistente em a: presente em a∈{30, 100, 400, 1900};
   - (da R-1) universal nas 14 células amostradas.
2. **Em k baixo, o modo fantasma congelado é Ψ_f-puro** (composição
   1.00 em k_phys≈0.025) e tem energia conservada negativa (sinal
   invariante). **Em k alto (k_c≥100), ele se funde com o taquião num
   quarteto complexo** — a assinatura congelada clássica de mistura
   fantasma-taquião. Nota: "congelada" — e o D2 mostrou que o
   congelado não é árbitro dinâmico; o significado físico da fusão
   herda essa suspeita.
3. **A frequência congelada do modo cresce com a** (ω²: ~6e3→~1.4e9
   na trilha em a, em base comóvel) — comportamento de direção que
   "quer" ser vínculo (consistente com a hipótese, do D1, de que essa
   é a direção que a constraint secundária removeria; não provado).

## 2. O que o script tentou medir e NÃO sustenta (autocrítica)

- **Magnitudes de energia** entre pontos/k/μ: E por modo com autovetor
  unitário em base comóvel não é comparável entre configurações (a
  base carrega potências de a e k; eig(K_red) varre 5 ordens). O SINAL
  de E num ponto é invariante; a comparação de magnitudes, não.
- **A escala-μ (expoente 0.19)**: idem — não refuta nem confirma a
  velha lei μ³ (que era, ela também, dependente de normalização).
- **O critério R2-E "sem E<0 em k alto"**: artefato de classificação
  (o modo virou complexo e saiu do filtro de ω real), não
  desaparecimento do fantasma.
- **Aviso numérico**: no detalhe da REF, o pareamento ±λ do QEP listou
  5 "pares" de um sistema de 3 dof — mau condicionamento (cond(K)~1e5
  entre autovalores). Não afeta a assinatura (eigvalsh direto), afeta
  listagens de modo.

**Consequência:** qualquer quantificação de "letalidade" do fantasma
exige normalização canônica das variáveis (transformação simplética
por ponto) — i.e., a análise de strong coupling de verdade. Isso está
**além da maquinaria quadrática-congelada-comóvel atual**, e é
exatamente onde o debate da literatura está (instabilidade física vs
"breakdown of linear perturbation theory", 2507.11526).

## 3. O enunciado honesto do setor escalar da F1 ao fim de D2+R-1+R-2

> No nível quadrático-linear, com dinâmica real: o setor escalar
> tardio do ramo finito β-constante é **dinamicamente estável** nas
> células amostradas (D2, R-1); a instabilidade real da classe é a
> **transiente de transição** (tipo-gradiente, dano k/célula-
> dependente — R-4 mapeia); e existe uma **direção cinética negativa
> estrutural universal** (assinatura invariante, robusta em k e a)
> cuja letalidade **não é decidível na ordem quadrática** — nem por
> nós, nem, até onde o posicionamento apurou, pela literatura.
>
> **A TDCP-F1 não está excluída no nível em que este programa pode
> julgar.** O antigo no-go fica reclassificado: de "setor escalar
> patológico" para "setor escalar sem veredito de exclusão, com uma
> questão de fantasma estrutural aberta na fronteira quadrática".

## 4. Estratificação epistêmica

| Afirmação | Nível |
|---|---|
| Assinatura negativa: uniforme em k, persistente em a, universal nas células | 2b (invariante de congruência; amostras declaradas) |
| Fusão fantasma-taquião em quarteto complexo em k alto (congelado) | 2b (congelado — significado dinâmico herda a suspeita do D2) |
| Ψ_f-dominância do modo em k baixo | 2b |
| Frequência congelada crescente com a ("quer ser vínculo") | 2b descritivo; interpretação nível 3 |
| Letalidade do fantasma | **indecidível na ordem quadrática** — fronteira declarada do programa |
| Magnitudes de E e escala-μ desta rodada | **descartadas** (poluição de normalização — autocrítica §2) |

## 5. Fila

- **R-3** (Fase B da Investigação 2 por evolução real na rolagem) e
  **R-4** (k grandes + mapa lnA vs vínculos) seguem na fila — decidem
  o quadro transiente e o regime não-fatorado.
- A questão do fantasma migra para a fronteira do programa: ou
  normalização canônica + análise de interações (custo alto, talvez
  sessão dedicada), ou fica declarada como aberta no paper — em boa
  companhia, porque a literatura está exatamente no mesmo impasse.
- O enunciado do §3 é o rascunho do veredito final para o cap. 07.
