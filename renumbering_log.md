# Log de Renumeração (Tarefa 2d)

## Convenção adotada para o sufixo "X.2"

O sufixo "X.2" aparecia no corpus com três significados diferentes:

- `Cap.6.2` era uma revisão real e mais aprofundada do Capítulo 6 (mesmo
  escopo, tratamento técnico expandido).
- `Cap.12.2` era conteúdo novo, sem sobreposição de escopo com o
  Capítulo 12 (quatro tópicos de validação: ajuste de β_n, isocurvatura,
  massa do gravitón, consistência EFT — que se tornam, eles mesmos, os
  Capítulos 14–17 depois da renumeração abaixo).
- `Cap.26.2` era um capítulo sequencial distinto do Cap.26 (emaranhamento
  cosmológico vs. colapso da função de onda primordial), não uma revisão.

**Convenção única adotada:** o sufixo `.2` é reservado exclusivamente para
uma **revisão/expansão do mesmo capítulo** (mesmo escopo, versão técnica
mais completa). Qualquer conteúdo que não seja uma revisão — ou seja, que
introduza escopo novo ou dê sequência lógica a outro — recebe um número
inteiro novo, inserido na posição de leitura correta da sequência
principal.

Aplicando essa convenção:

- `Cap.6.2` **permanece** `Cap.6.2` (é de fato uma revisão do Cap.6).
- `Cap.12.2` **deixa de existir como tal** e passa a ser um capítulo
  numerado (novo Cap.13), com todos os capítulos posteriores da família
  F1 deslocados em +1 para abrir espaço.
- `Cap.26.2` (em inglês, ainda não traduzido) recebe numeração provisória
  no fim da sequência atual (ver Tarefa 3); seu destino final depende do
  veredito de integração da Tarefa 4 (Tarefa 5).

## Mapeamento antigo → novo (arquivos em `manuscript/capitulos/`)

| Arquivo antigo | Arquivo novo | Motivo |
|---|---|---|
| `Cap.12.2.md` | `Cap.13.md` | Promovido a capítulo numerado (conteúdo novo, não revisão) |
| `Cap.13.md` | `Cap.14.md` | Deslocado +1 |
| `Cap.14.md` | `Cap.15.md` | Deslocado +1 |
| `Cap.15.md` | `Cap.16.md` | Deslocado +1 |
| `Cap.16.md` | `Cap.17.md` | Deslocado +1 |
| `Cap.17.md` | `Cap.18.md` | Deslocado +1 |
| `Cap.18.md` | `Cap.19.md` | Deslocado +1 |
| `Cap.19.md` | `Cap.20.md` | Deslocado +1 |
| `Cap.20.md` | `Cap.21.md` | Deslocado +1 |
| `Cap.21.md` | `Cap.22.md` | Deslocado +1 |
| `Cap.22.md` | `Cap.23.md` | Deslocado +1 |
| `Cap.23.md` | `Cap.24.md` | Deslocado +1 |
| `Cap.24.md` | `Cap.25.md` | Deslocado +1 |
| `Cap.25.md` | `Cap.26.md` | Deslocado +1 |
| `Cap.26.md` (inglês) | `Cap.27.md` | Numeração provisória (Tarefa 3) |
| `Cap.26.2.md` (inglês) | `Cap.28.md` | Numeração provisória (Tarefa 3) |
| `Cap.27.md` (inglês) | `Cap.29.md` | Numeração provisória (Tarefa 3) |
| `Cap.1.md`–`Cap.12.md`, `Cap.6.2.md` | *(sem alteração)* | Fora da faixa deslocada |

Arquivos **não afetados**: `Cap.1`–`Cap.12`, `Cap.6.2`, todos os Apêndices
A–H, e `Eng Version/CHAPTER 1` (permanece como está — é uma versão em
inglês condensada e paralela dos Capítulos 1–14, não parte da numeração
principal).

## Referências cruzadas internas atualizadas

Toda menção interna a um capítulo/seção deslocado (títulos próprios como
"CAPÍTULO 13", numeração de subseção própria como "13.1"–"13.16", e
citações cruzadas de outros capítulos como "Cap.13", "Capítulos 17, 18 e
21", "Cap.19--20", "§14.4") foi localizada e incrementada em +1 de forma
consistente com o deslocamento de arquivo, para que a leitura sequencial
continue coerente. Nenhuma referência a capítulos fora da faixa 13–25
(por exemplo, Cap.1–12, ou valores físicos como `10^{-14}` ou `16\pi^2`)
foi tocada.

Isso foi verificado programaticamente: para cada um dos 14 arquivos
afetados, todo número de capítulo/seção no intervalo 13–26 encontrado no
arquivo após a atualização corresponde exatamente ao valor original +1,
na mesma posição sequencial — nenhuma referência ficou para trás, e
nenhuma foi incrementada duas vezes.

## Atualização (Tarefa 5) — destino final dos capítulos 27–29 provisórios

A Tarefa 3 traduziu o conteúdo para português nos arquivos provisórios
`Cap.27.md`/`Cap.28.md`/`Cap.29.md`. A Tarefa 4 (`integration_assessment.md`)
concluiu **integração parcial** (não integração total) desse conteúdo ao
corpo F1. Consequentemente, na Tarefa 5, esses três arquivos **não**
permaneceram na sequência numerada de capítulos: foram movidos para

| Arquivo provisório (Tarefa 3) | Destino final (Tarefa 5) |
|---|---|
| `manuscript/capitulos/Cap.27.md` | `manuscript/apendices/Appendix-I.md` |
| `manuscript/capitulos/Cap.28.md` | `manuscript/apendices/Appendix-J.md` |
| `manuscript/capitulos/Cap.29.md` | `manuscript/apendices/Appendix-K.md` |

Cada um foi renumerado internamente (títulos "CAPÍTULO N" → "APÊNDICE
X"; subseções "N.M" → "X.M") e recebeu um preâmbulo explicando seu status
de linha de pesquisa exploratória, com referência ao veredito da Tarefa 4.
Um quarto arquivo novo, `manuscript/apendices/Appendix-L.md`, foi
adicionado como ponte curta documentando **apenas** a reinterpretação
considerada absorvível ao corpo F1 (ver `integration_assessment.md`,
seção "O que pode ser incorporado").

O corpo principal de capítulos numerados da TDCP-F1 é, portanto,
**Capítulo 1 ao Capítulo 26** (mais o Cap.6.2 como revisão do Cap.6),
com os Apêndices A–L cobrindo o material técnico de suporte (A–H),
a linha de pesquisa exploratória (I–K) e a ponte conceitual entre elas (L).
