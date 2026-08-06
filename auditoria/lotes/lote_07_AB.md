# Auditoria — Lote 7: Anexo B (71 equações)

Data: 2026-08-06. Regras: `../regras_de_auditoria.md`. Vereditos em
`../registro/AB.md` (`../code/aplica_vereditos_lote07.py`).

O maior arquivo do corpus (71 equações). É o "motor" do fundo
cosmológico: variação explícita da ação minisuperespaço nos dois
lapses N_g, N_f, e a dedução da constraint de Bianchi. Rico em
achados porque é aqui, na fonte, que a âncora D3 encontrou o erro que
se propaga por Cap.1, Cap.2, Cap.5, Cap.13 e Cap.14 — e é aqui também
que está a derivação original de ṙ≡0 que a âncora D5 confirmou.

## Estatística

| Veredito | Qtde |
|---|---|
| CONFERE | 61 |
| CONFERE SOB HIPÓTESE | 4 |
| ERRO DE CÁLCULO | 4 |
| INCOMPLETA | 1 |
| ARTEFATO DE CONVERSÃO | 1 |
| **Total** | **71** |

## Achados principais

### H1. §B.5 e §B.6 fazem a MESMA regra da cadeia lado a lado — uma corretamente, outra não

Este é o achado central do lote, e a âncora D3 já o havia previsto
antes de eu ler o texto-fonte: ao variar a ação em relação a N_g
(§B.5), o Anexo B calcula `∂/∂N_g(-m²M_eff²N_ga³FV) = -m²M_eff²a³FV`
(`[AB.28]`) — tratando V(ξ,r) como se não dependesse de N_g. Mas
ξ=N_f/N_g **depende explicitamente de N_g**, e a derivada completa
precisa do termo `-ξ∂V/∂ξ` que vem da regra da cadeia. Nas duas
seções seguintes depois, ao variar em N_f (§B.6), **o mesmo Anexo B
aplica a regra da cadeia corretamente**: `[AB.40]` escreve
explicitamente `∂/∂N_f(...) = ...·∂V/∂ξ·∂ξ/∂N_f` — o termo que falta
em `[AB.28]`. A assimetria entre as duas variações, feitas lado a lado
no mesmo texto, é a origem do erro: o erro de `[AB.28]` se propaga por
`[AB.32]` (soma), `[AB.34]` (Friedmann-g com V(ξ,r) não-corrigido) e
`[AB.36]` (definição citada de ρ_int^(g), que retém ξ e β₄ e
**conflita diretamente com o Anexo A §A.8/`[AA.30]`**, já confirmado
no lote 6). A forma corrigida — verificada por regra da cadeia
completa e por sympy na âncora D3 — é
ρ_int^(g)=m²M_eff²F(χ)(β₀+3β₁r+3β₂r²+β₃r³), idêntica ao Anexo A mais
o fator F(χ). É esta forma corrigida, não a de `[AB.36]`, que o corpo
principal usa consistentemente (Cap.14 §14.7, lote 3).

### H2. NOVO — a forma correta reaparece "de memória" mais adiante no próprio Anexo B, contradizendo B.5

No subcaso proporcional (§B.10), `[AB.68]` escreve
ρ_int^(g)=m²M_eff²F(χ)(β₀+3β₁c+3β₂c²+β₃c³) — usando a forma **sem**
ξ e **sem** β₄ (com r→c), exatamente a forma corrigida pela âncora D3,
e **não** a forma citada em `[AB.36]` poucas seções antes. Como neste
subcaso ξ=r=c simultaneamente, seria possível confundir as duas
formas, mas não são a mesma expressão (a forma de `[AB.36]` avaliada
em ξ=r=c daria β₀+4β₁c+6β₂c²+4β₃c³+β₄c⁴, com todos os quatro
coeficientes — não o que `[AB.68]` escreve). Isso é evidência adicional,
independente da rederivação da âncora D3, de que a forma "correta" é a
que o próprio autor tinha internalizada como resultado — `[AB.36]` é
um deslize pontual na passagem específica de N_g, não uma crença
diferente sobre a física.

### H3. §B.9 contém a derivação original e correta de ṙ≡0 — a fonte do achado C1 (lote 3)

`[AB.65]` deriva `ṙ=0` substituindo diretamente a condição do ramo
dinâmico H_g=ξH_f (`[AB.58]`) em `ṙ=r(ξH_f-H_g)` (`[AB.64]`) — álgebra
trivial e correta, e exatamente o resultado que a âncora D5 verificou
independentemente por sympy. Isso mostra que o Anexo B **já tinha o
resultado certo**: o erro do Cap.14 §14.12 (achado C1, lote 3, que
troca a constraint por uma condição não-equivalente H_b=ξH_g para
"contornar" ṙ=0) não é herdado de nenhuma fonte anterior — é um desvio
introduzido só ali, contra o que o próprio corpus já estabelecia neste
anexo. O texto de §B.9 é notavelmente honesto sobre a sutileza: alerta
explicitamente contra o "erro interpretativo comum" de achar que
"dinâmico" exige ṙ≠0.

### H4. Uma equação (B.7) é honestamente marcada como esquemática pelo próprio texto

`[AB.51]` (equação de aceleração do setor g, tipo Raychaudhuri) é
apresentada "de modo esquemático", com o texto admitindo "as
expressões completas são extensas" — p_int^(g) nunca é calculado.
Classificado INCOMPLETA em vez de CONFERE/ERRO por essa razão: a forma
segue o padrão esperado, mas não há conta a verificar.

### H5. A constraint de Bianchi (`[AB.54]`/`[AB.56]`/`[AB.71]`) é citada, não derivada passo a passo

`[AB.53]` (∇_g^μX_μν=0) é importada corretamente do formalismo HR
(consistente com Cap.4 §4.4, achado A1/lote 1). Mas a passagem de
`[AB.53]` até a forma polinomial específica
(β₁+2β₂r+β₃r²)(H_g-ξH_f)=0 é feita por argumento qualitativo em
§B.8.1 ("isso se traduz em uma condição algébrica/dinâmica..."), não
por álgebra explícita — o texto anuncia "vamos mostrar por que essa
estrutura aparece" e depois não mostra. Recebeu CONFERE SOB HIPÓTESE:
o resultado é o padrão conhecido da literatura de gravidade bimétrica
HR (Comelli–Nesti–Pilo) e consistente com o uso confirmado em todo o
corpo principal (Cap.5/Cap.14, lotes 1/3) — mas a derivação em si, tal
como apresentada aqui, tem uma lacuna.

## O que o lote confirma de sólido

A redução da ação ao minisuperspace (§B.4, `[AB.17]`–`[AB.25]`) é
inteiramente verificável e verificada: `√-g=N_ga³`, a Lagrangiana do
setor χ, e a soma final termo a termo conferem por álgebra direta. A
equação de Friedmann do setor f (§B.6 completo, `[AB.37]`–`[AB.50]`)
está inteiramente correta — inclusive a mesma regra da cadeia que
falha em §B.5 é aplicada aqui com precisão, e o resultado final foi
usado pela âncora D3 como checagem cruzada independente do
cancelamento de β₄/ξ no setor g. A dinâmica de r(t) (§B.9) é o ponto
mais valioso do anexo: correta, e mais honesta sobre suas próprias
sutilezas do que o capítulo que a usa incorretamente depois.

## Pendências que este lote empurra para frente

- O erro de `[AB.28]`/`[AB.36]` (H1) já tinha correção fechada pela
  âncora D3 antes deste lote; agora está localizado precisamente na
  fonte (a linha exata onde a regra da cadeia falta) para o futuro
  passe de correção editorial.
- A lacuna de derivação da constraint de Bianchi (H5) é uma boa
  candidata a reforço futuro (a literatura HR tem a prova completa via
  análise Hamiltoniana, mencionada mas não refeita nem no Anexo A nem
  aqui) — não muda o veredito, mas vale registrar para quem quiser
  fechar o buraco com rigor total.
