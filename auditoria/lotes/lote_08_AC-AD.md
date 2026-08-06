# Auditoria — Lote 8: Anexos C e D (43 equações)

Data: 2026-08-06. Regras: `../regras_de_auditoria.md`. Vereditos em
`../registro/AC.md, AD.md` (`../code/aplica_vereditos_lote08.py`).

Dois anexos pequenos, cada um o "coração matemático" de uma âncora já
concluída: o Anexo C (setor escalar) é território direto da âncora D1;
o Anexo D (setor tensorial) é território direto da âncora D2. Ambas as
derivações citam seções específicas destes anexos por número — este
lote é, em boa parte, aplicar essas citações já prontas.

## Estatística

| Veredito | AC | AD | Total |
|---|---|---|---|
| CONFERE | 20 | 15 | 35 |
| CONFERE SOB HIPÓTESE | 1 | 3 | 4 |
| ERRO / ERRO DE FORMULAÇÃO / DE CÁLCULO | 2 | 1 | 3 |
| NÃO-DERIVÁVEL | 1 | 0 | 1 |
| **Total** | **24** | **19** | **43** |

## Achados principais

### I1. Anexo C §C.3 ("2 modos"): a claim central do anexo é a que a âncora D1 refuta — mas é prosa, não uma equação numerada

A frase-chave de §C.3 ("O resultado físico esperado (linear) é... Total:
2 modos escalares físicos") é justamente o que a âncora D1 contradiz: a
análise de fundo congelado encontra **3** modos, não 2 — a mesma
contagem do Cap.6.2 §6.4 (já confirmada no lote 2). D1 registra
explicitamente essa tensão ("Cap.6.2 §6.4 = 3 vs Anexo C §C.3 = 2") e
resolve a favor de 3, com a ressalva honesta de que uma redução para 2
via constraint secundária dependente do tempo "permanece não
demonstrada no corpus". Como a frase de §C.3 é prosa (não capturada
como fórmula pelo extrator), não recebe um ID/veredito individual —
mas todas as equações subsequentes que dependem dessa contagem
(`[AC.08]`, `[AC.19]`, `[AC.20]`) foram marcadas com a ressalva.

### I2. §C.9's "K₁₁↔Higuchi" é uma analogia de campo único que não sobrevive ao cálculo explícito

`[AC.18]` afirma que K₁₁ (o bloco cinético do modo massivo) troca de
sinal exatamente no limiar de Higuchi de um único campo massivo
genérico (m_eff²=2H²) — uma extrapolação por analogia da física de
gravidade massiva de campo único. A âncora D1, calculando a matriz
K real, encontra algo estruturalmente diferente: um par
fantasma/degenerado presente **nos dois lados** de qualquer
cruzamento de raiz β₁+2β₂r (benchmarks A→B), não uma transição suave
em um único K₁₁. `[AC.21]` (a versão condensada em §C.10) herda o
mesmo problema.

### I3. §C.11: a preservação do ghost BD não implica ausência de outras patologias — achado que a âncora D1 já cravou

`[AC.23]` argumenta que, como F(χ) não introduz derivadas de métrica,
a estrutura de constraints do HR (que remove o ghost de
Boulware-Deser) permanece intacta. A âncora D1 classifica isso como
"SEM SUPORTE nos fundos testados": mesmo que o argumento sobre o BD
ghost especificamente esteja correto, ele nada diz sobre o par
fantasma/taquiônico genuíno que D1 encontra no ramo dinâmico — uma
patologia diferente, não coberta pelo argumento qualitativo do texto.

### I4. Anexo D §D.3 é a fonte confirmada da ação tensorial correta — inclusive a base de diagonalização ponderada que o Cap.16 deveria ter usado

`[AD.04]`/`[AD.05]` reproduzem exatamente a estrutura que a âncora D2
verificou como correta (K_ℓℓ=M_f²b³/ξ, c_f²=ξ²/r² — verificado nesta
auditoria por álgebra direta a partir do termo N_f²k²/b² escrito no
texto). Mais importante: `[AD.06]`/`[AD.07]` são a "base ponderada do
Anexo D §D.4" que a própria âncora D2 cita como a forma correta de
diagonalização — superior à combinação ingênua M_gh+M_frℓ do Cap.16
§16.3 (lote 4, achado E1), pois usa o expoente r^{3/2} correto e
normalização adequada (ortogonalidade verificada nesta auditoria:
h₊·h₋∝M_g·M_fr^{3/2}+M_fr^{3/2}·(−M_g)=0). O Anexo D, portanto, tinha
a ferramenta certa; o Cap.16 não a usou.

### I5. Anexo D §D.5: a única equação realmente errada do lote, e a âncora D2 já a substitui de forma fechada

`[AD.11]` propõe m_T²∝m²F(χ)B(r)(1+r)/r — sem dependência em ξ. A
âncora D2 mostra que a forma exata é
m_T²=m²F·M_eff²(1/M_g²+ξ/(M_f²r³))·r[β₁+β₂(ξ+r)+β₃ξr], que depende de
ξ de forma essencial (inclusive determina o sinal de m_T² no benchmark
testado) e cujo fator estrutural β₁+β₂(ξ+r) só coincide com B(r) se
ξ=r. O próprio texto já qualifica `[AD.11]` como "uma forma
representativa... reabsorvendo fatores" — mas mesmo como forma
representativa, a ausência de ξ não é um detalhe reabsorvível, é uma
lacuna estrutural.

## O que o lote confirma de sólido

O aparato de perturbações escalares (§C.2, ansatz de 4 potenciais por
setor, decomposição em variáveis relativas) e o setor tensorial via
Anexo D §D.3/§D.4 (cinético, gradiente e a base de diagonalização
ponderada) são as partes do corpus mais diretamente confirmadas pelas
próprias derivações simbólicas D1/D2 — não por analogia ou
plausibilidade, mas por matrizes explícitas computadas e comparadas
termo a termo. O critério genérico de ausência de fantasma (K
positiva definida) e o problema de autovalor generalizado para c_s²
(§C.8) são formulações-padrão corretas, independentes de qualquer
disputa sobre dimensão da matriz.

## Pendências que este lote empurra para frente

- A contagem "2 modos" de §C.3 (I1) e a identificação K₁₁↔Higuchi de
  §C.9 (I2) precisam de correção editorial conjunta com o Cap.6.2/Cap.15
  quando o passe de correção do manuscrito acontecer — mesma âncora D1.
- `[AD.11]` (I5) deve ser substituída pela forma fechada da âncora D2
  quando o Anexo D for revisado, junto com a correção já pendente do
  Cap.16 (lote 4, achado E1).
