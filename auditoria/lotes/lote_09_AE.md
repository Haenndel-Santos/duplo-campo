# Auditoria — Lote 9: Anexo E (57 equações)

Data: 2026-08-06. Regras: `../regras_de_auditoria.md`. Vereditos em
`../registro/AE.md` (`../code/aplica_vereditos_lote09.py`).

O "manual operacional" da TDCP — converte o formalismo em um sistema
de ODEs em N=ln a pronto para integração numérica. É também o
capítulo mais denso em conexões com achados e âncoras anteriores: o
erratum de sinal da equação de χ (D2/D8), a "escolha TDCP principal"
citada nominalmente por D1 e D5, a segunda lei de η (achado A2/lote
1) e a equação H²∝ρ/(1−η) (âncora D4) aparecem todas aqui, na fonte
operacional que os outros documentos citam por número de seção.

## Estatística

| Veredito | Qtde |
|---|---|
| CONFERE | 43 |
| CONFERE SOB HIPÓTESE | 2 |
| CONFLITA COM (âncora) | 1 |
| ERRO DE CÁLCULO | 7 |
| INCOMPLETA | 1 |
| NÃO-DERIVÁVEL | 1 |
| ARTEFATO DE CONVERSÃO | 2 |
| **Total** | **57** |

## Achados principais

### J1. O erratum de sinal da equação de χ está na origem (§E.3(3)) e se propaga por 6 equações em cascata

`[AE.09]`/`[AE.11]` escrevem χ̈+3Hχ̇+U'(χ)=+m²M_eff²F'(χ)V(ξ,r).
Rederivando por Euler-Lagrange nesta auditoria (variando o termo de
interação -m²M_eff²√-g F(χ)V(K) da ação, combinado com a convenção
padrão do EOM livre de Klein-Gordon χ̈+3Hχ̇+U'=0): o sinal correto é
**negativo** — χ̈+3Hχ̇+U'(χ)=−m²M_eff²F'(χ)V(ξ,r). Confirma
exatamente o erratum já documentado nas âncoras D2/D8. O erro se
propaga por toda a seção E.6.2, que deriva a equação de evolução de x
a partir da equação de χ: `[AE.22]`, `[AE.25]`, `[AE.26]` e o
resultado final em caixa `[AE.29]` (dx/dN=...+𝒮m²/H², deveria ser
−𝒮m²/H²) herdam o sinal trocado — mas a álgebra de cada passo
(regra do produto, mudança de variável para N, divisão) foi verificada
independentemente do sinal e está correta em si.

### J2. NOVO — erro de álgebra autocontido em §E.6.2, que não se propaga

`[AE.27]` define λ≡M_g·U'/U e afirma U'/H²=3M_g²λy². Refazendo a
conta (U'=λU/M_g, U=3M_g²H²y² pela definição de y em `[AE.18]`):
U'=3M_gH²λy², logo U'/H²=3M_gλy² — **um** fator de M_g, não dois.
A boa notícia: o erro não se propaga — `[AE.28]` (U'/(√6M_gH²)=√(3/2)λy²)
usa implicitamente o valor CORRETO (3M_gλy²/(√6M_g)=√(3/2)λy², batendo
exatamente); a versão com M_g² daria √(3/2)M_gλy², que não é o que
aparece. É um deslize isolado de digitação em `[AE.27]`, não um erro
conceitual — mas vale a correção editorial.

### J3. A "escolha TDCP principal" (H=ξH_f) é citada aqui, na fonte que D1 e D5 nomeiam

`[AE.15]` apresenta o ramo dinâmico H=ξH_f como "escolha TDCP
principal" logo após a constraint de Bianchi `[AE.14]`. Esta é
literalmente a passagem que as âncoras D1 e D5 citam pelo nome
("Anexo E §E.3(6) declara como 'escolha TDCP principal'") ao descrever
o ramo como duplamente inviável — D5 mostra ṙ≡0 nesse ramo (não produz
r(t) genuíno) e D1 encontra um par fantasma/taquiônico genuíno em
todos os benchmarks testados nesse mesmo ramo. A equação em si é uma
consequência lógica válida de `[AE.14]`; o problema é a apresentação
como escolha preferencial sem essas duas ressalvas.

### J4. ṙ≡0 aparece pela terceira vez — e desta vez com framing honesto

`[AE.50]`/`[AE.51]` rederivam ṙ=r(ξH_f−H) e, no ramo dinâmico, ṙ=0 —
mesmo resultado de Anexo B §B.9 (lote 7) e confirmado pela âncora D5.
Diferente do Cap.14 §14.12 (achado C1/lote 3, que contorna o resultado
trocando a constraint), este anexo reconhece a implicação
explicitamente e propõe r constante como "a prática mais simples e
útil" — indo na direção que a própria âncora D5 recomenda (raiz
algébrica/móvel em vez de "r(t) dinâmico" genuíno).

### J5. A segunda lei de η (achado A2) está aqui, junto com a equação H²∝ρ/(1−η) (âncora D4)

`[AE.12]`/`[AE.31]`/`[AE.33]` usam η̇=Γχ̇² — a lei já identificada no
lote 1 como incompatível com a lei do Cap.1 §1.6/Cap.2 §2.7
(η̇=Γ(H1−H2)², com [Γ] diferente). E `[AE.39]`–`[AE.42]`
(H²=8πGρ_tot/(1−η) e sua cadeia de derivadas logarítmicas) é
exatamente a fórmula que a âncora D4 classifica como não-derivável da
ação atual — reafirmada aqui como "o formalismo TDCP efetivo", sem
qualificação como extensão proposta. A álgebra de `[AE.40]`–`[AE.42]`
(logaritmo e suas derivadas) está correta *dado* `[AE.39]` como
premissa — o problema é só a premissa em si, não a manipulação.

### J6. §E.7 mistura uma relação bem verificada com uma parametrização de conveniência não fechada

`[AE.43]` (w_eff via dη/dN) é introduzida com "é comum: usar
diretamente" — o próprio texto sinaliza que é uma escolha, não uma
consequência derivada de `[AE.39]`–`[AE.42]` nesta seção. `[AE.44]`
é ainda mais explícita sobre sua própria incompletude: termina em
"+⋯" e o texto admite que a forma "depende de quais componentes foram
incluídos" — INCOMPLETA por declaração própria, não por achado desta
auditoria.

## O que o lote confirma de sólido

A conversão inteira do sistema para variáveis adimensionais (x,y,Ωm,
Ωint) e para a variável temporal N=ln a é verificada por álgebra
direta em cada passo — inclusive o constraint de Friedmann
`[AE.20]` (1=Ωm+x²+y²+Ωint), obtido corretamente a partir das
definições. As equações de fundo `[AE.04]`–`[AE.08]` usam as formas
JÁ CORRIGIDAS de ρ_int^(g)/ρ_int^(f) (sem ξ, sem β4 no setor g — âncora
D3), não a versão errada do Anexo B §B.5 — o Anexo E herdou a forma
certa. O fechamento algébrico de ξ(N) via a Friedmann-f (§E.8,
`[AE.45]`–`[AE.49]`) é verificado passo a passo e correto, com a
ressalva honesta do próprio texto sobre a escolha de sinal físico.

## Pendências que este lote empurra para frente

- O erratum de sinal (J1) já estava documentado nas âncoras D2/D8;
  este lote localiza precisamente as 6 equações afetadas (`[AE.09]`,
  `[AE.11]`, `[AE.22]`, `[AE.25]`, `[AE.26]`, `[AE.29]`) para o futuro
  passe de correção.
- O deslize isolado de `[AE.27]` (J2) é uma correção editorial trivial
  e autocontida — não depende de nenhuma âncora.
- A lei de η (J5) permanece pendente de decisão editorial desde o
  lote 1 (achado A2) — o Anexo H (próximos lotes) é onde a segunda
  ocorrência dessa lei também vive, per a nota original do achado A2.
