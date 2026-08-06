# Auditoria — Lote 6: Anexo A (30 equações)

Data: 2026-08-06. Regras: `../regras_de_auditoria.md`. Vereditos em
`../registro/AA.md` (`../code/aplica_vereditos_lote06.py`).

Início da auditoria dos anexos (AA→AL, 278 equações restantes após os
26 capítulos principais). O Anexo A é o formalismo canônico
Hassan–Rosen que todo o corpo principal já vinha citando — as
definições de ξ, r, K, e_n(K) usadas desde o Cap.3 têm sua origem
exatamente aqui.

## Estatística

| Veredito | Qtde |
|---|---|
| CONFERE | 29 |
| CONFERE SOB HIPÓTESE | 1 |
| **Total** | **30** |

Lote mais limpo da auditoria até agora — nenhum ERRO, nenhuma
INCOMPLETA, nenhum artefato de conversão.

## Achados

### G1. Anexo A confirma, na origem, o que os capítulos principais só citavam

Os polinômios simétricos elementares e₁–e₄ do fundo FLRW
(`[AA.24]`–`[AA.27]`, autovalores {ξ,r,r,r}) foram verificados por
álgebra explícita nesta auditoria e reproduzem exatamente os mesmos
valores que o Cap.14 §14.2 já usava (confirmados por auto-teste no
lote 3) — o Anexo A é a fonte, o Cap.14 a reprise. O mesmo vale para
ξ=N_f/N_g e r=b/a (`[AA.23]`): esta é a definição canônica citada em
todo o corpus desde então.

### G2. `[AA.02]` (ação HR completa) resolve a pendência do achado A4 (lote 1)

O achado A4 do lote 1 apontava que o Cap.3 §3.4 escreve as equações de
campo com prefator `m²` sem normalização, quando o correto seria
`m²M_eff²/M_g²`. A ação completa do Anexo A traz o potencial com
prefator `m²M_eff²` (não `m²` isolado) multiplicando `√-g V(K)`
— exatamente a normalização que, ao variar a ação (dividindo pela
normalização `M_g²/2` do termo de Einstein-Hilbert), produz o fator
`M_eff²/M_g²` que o achado A4 esperava. O Anexo A não *deriva*
explicitamente as equações de campo variadas (isso é tarefa do Anexo
B, próximo lote), mas fornece a ação de onde o prefator correto viria.

### G3. `[AA.30]` (ρ_int no fundo FLRW) é a mesma fórmula já verificada pela âncora D3

A densidade de interação `ρ_int^(g) = m²M_eff²(β₀+3β₁r+3β₂r²+β₃r³)`
é exatamente o resultado que a Derivação 3 (`derivations/03_dV_dNg_regra_cadeia.md`)
verificou por regra da cadeia completa — ξ e β₄ cancelam exatamente ao
converter ∂V/∂N_g nessa densidade. É a mesma quantidade já usada e
confirmada no Cap.14 (lote 3); o Anexo B §B.5, que tenta chegar ao
mesmo resultado por um caminho diferente, é onde a âncora D3 encontra
o erro (ver próximo lote).

### G4. Único ponto sem confirmação de livro-texto único: a prescrição de ρ_int via derivada funcional

`[AA.29]` (`ρ_int^(g) = -(1/√-g)(δ/δg^00)(√-g V)`) é uma técnica
razoável e padrão em espírito (análoga à definição de T₀₀ a partir da
ação de matéria), mas não é uma fórmula citável de um único
livro-texto — é a prescrição operacional adotada pelo corpus. Recebeu
CONFERE SOB HIPÓTESE por essa razão; o resultado que produz (`[AA.30]`)
está, de todo modo, independentemente confirmado pela âncora D3.

## O que o lote confirma de sólido

Praticamente o anexo inteiro: a ação HR, a definição de K como raiz
matricial, as identidades de Newton para e₂ e e₃ em termos de traços
(verificadas: e₂=(p₁²−p₂)/2, e₃=(p₁³−3p₁p₂+2p₃)/6 — formas-padrão
corretas), a especialização FLRW com lapses, e a álgebra completa dos
e_n(ξ,r,r,r). Não há achado a levar adiante deste lote além dos já
registrados (G2 aponta para o Anexo B, que é o próximo).
