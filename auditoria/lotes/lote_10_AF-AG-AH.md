# Auditoria — Lote 10: Anexos F, G e H (39 equações)

Data: 2026-08-06. Regras: `../regras_de_auditoria.md`. Vereditos em
`../registro/AF.md, AG.md, AH.md` (`../code/aplica_vereditos_lote10.py`).

Três anexos de fechamento: F mapeia o espaço de parâmetros, G é a
camada filosófica/ontológica, H é a "formalização canônica" —
consolidação final de postulados e equações. Como H em particular é
puramente um resumo, a maioria de seus problemas são heranças diretas
de achados já registrados, agora elevados a "postulado" ou "forma
final".

## Estatística

| Veredito | Qtde |
|---|---|
| CONFERE (inclui composições com CONFLITA) | 29 |
| CONFERE SOB HIPÓTESE | 3 |
| ERRO DE CÁLCULO | 2 |
| INCOMPLETA | 3 |
| NÃO-DERIVÁVEL | 2 |
| **Total** | **39** |

## Achados principais

### K1. Anexo H eleva o erro de sinal da equação de χ e a lei conflitante de η a "postulados formais"

`[AH.05]` (Postulado 4) e `[AH.12]` (equação fundamental 4) repetem o
sinal errado já identificado no Anexo E (lote 9) e nas âncoras D2/D8:
χ̈+3Hχ̇+U'(χ)=+m²M_eff²F'(χ)V, quando a ação dá sinal negativo. E
`[AH.06]` (Postulado 5) é literalmente a citação nominal do achado A2
(lote 1: "Anexo H Postulado 5") — a segunda lei de η (η̇=Γχ̇²)
incompatível com a do Cap.1/Cap.2. Como este anexo se propõe
explicitamente como o "núcleo lógico" e a "versão axiomática
consolidada" da TDCP, ambos os problemas — herdados, não novos —
ganham peso adicional: uma consolidação canônica com um postulado
dimensionalmente conflitante e uma equação fundamental com sinal
trocado não pode ser considerada fechada.

### K2. `[AH.16]` é a formulação mais proeminente da equação não-derivável da âncora D4 em todo o corpus

A "Forma Compacta Final da Teoria" (§H.6) é exatamente
H²=(8πG/3)(ρm+ρχ+ρint)/(1−η) — a fórmula que a âncora D4 já havia
classificado como não-derivável da ação bimétrica atual (η está
ausente da ação; uma extensão mínima Ω(η)R_g produziria um termo
extra não presente aqui). Encontrá-la aqui, apresentada como "a
essência da TDCP" resumida em uma única equação em caixa, é o ponto de
maior visibilidade desse problema — não um novo achado, mas o lugar
onde ele mais importa.

### K3. NOVO — μ_T² perde a dependência em ξ ao ser "canonizada" (Anexo F e Anexo H)

O Anexo D §D.4 (`[AD.09]`, lote 8) já escrevia honestamente
μ_T²(r,ξ,β_n,M_g,M_f) — com ξ explícito, refletindo o que a âncora D2
mostrou ser essencial. Tanto `[AF.06]` (Anexo F §F.3.2) quanto
`[AH.14]` (Anexo H, equação fundamental 6) **regridem** para
μ_T²(r,β_n,M_g,M_f) — omitindo ξ do próprio argumento da função, não
apenas de uma forma fechada específica. É um retrocesso de honestidade
notacional em relação ao Anexo D, marcado INCOMPLETA nos dois lugares
(e propagado a `[AF.07]`).

### K4. Anexo F §F.3.3 mistura um achado real de D1 com uma generalização que D1 refuta

`[AF.10]` afirma que a condição de ausência de ghost escalar é
"particularmente sensível" a B(r)=β₁+2β₂r+β₃r², degenerando quando
B(r)=0. A parte da degenerescência EM B(r)=0 é real — é exatamente o
benchmark C da âncora D1 (ramo algébrico, r=r★: par cinéticamente
degenerado). Mas a implicação mais ampla — que B(r) é o que "decide"
a saúde do setor escalar de forma geral — é o que D1 refuta
diretamente: o par fantasma dos benchmarks A/B (ramo dinâmico) está
presente **dos dois lados** de qualquer valor de B(r), sem relação com
seu sinal. Recebeu CONFERE SOB HIPÓTESE com a distinção explícita.

### K5. Anexo F §F.6.3 invoca GW170817 sem a qualificação que o achado C6 já exigia

`[AF.16]` argumenta que, como o modo massivo é ultraleve, ondas de
alta frequência não são afetadas — um argumento válido em si (sobre a
dispersão do modo massivo). Mas não cobre a ressalva do achado C6
(lote 3): o modo nominalmente "massless" h₊ só propaga exatamente em
c=1 se ξ=r (âncora D2: c_g²=1 mas c_f²=ξ²/r², e os dois setores não
são simultaneamente diagonalizáveis em geral). Invocar GW170817 como
"região segura" sem declarar essa condição é impreciso, mesmo que o
argumento sobre o modo massivo em si esteja correto.

## O que o lote confirma de sólido

A estrutura de postulados do Anexo H (H.2) é, à parte dos dois
problemas herdados (K1), bem organizada e coerente como axiomatização
— os Postulados 1, 2, 3 e 6 não têm problema algum. As equações de
Friedmann consolidadas `[AH.09]`/`[AH.10]` usam corretamente as formas
já corrigidas pela âncora D3 (sem ξ, sem β₄ no setor g). O Anexo G,
apesar de ser puramente conceitual, é internamente honesto sobre seus
próprios limites (§G.13: "não fornece quantização fundamental", "não
explica a origem última da bifurcação") — o mesmo padrão de
autoconsciência epistêmica já visto em pontos fortes de outros
capítulos (ex. achado F5/lote 5 sobre superluminalidade).

## Pendências que este lote empurra para frente

- K1 e K2 são as duas pendências mais visíveis do corpus inteiro
  para o futuro passe de correção — literalmente nos postulados e na
  "equação final" da teoria.
- K3 (omissão de ξ) deve ser corrigida junto com a forma fechada de
  μ_T² quando o Cap.16/Anexo D forem revisados (mesma âncora D2).
- Este lote fecha a leitura sequencial dos Anexos A–H (o bloco
  "técnico + filosófico + canônico"). Restam os Anexos I, J, K
  (linha de pesquisa exploratória, per `integration_assessment.md`) e
  L (ponte conceitual) — território ainda não coberto por nenhuma
  âncora D1–D8.
