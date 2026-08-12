# R-10c — As Duas Saídas Baratas: Ramo Infinito e Fundo Dinâmico

**Data:** 2026-08-13. Script: `auditoria/code/r10c_saidas_ramo_e_dinamico.py`
(saída em `out/`). Sequência do R-10a/R-10b (instabilidade de
gradiente confirmada). Testa as saídas 2 e 4 listadas em
`docs/resultado_r10a_gradiente.md` §4.

---

## Parte A — A exclusão do ramo infinito: **correta, mas mal
justificada no corpus**

`docs/resultado_ramo_finito.md` §2 descartava o ramo infinito porque
"dá ξ < 0, isto é, lapso negativo no setor f". A varredura de todas as
raízes reais positivas da cúbica mostra que a frase é **verdadeira
apenas no regime primordial**:

| a | raiz | r | ξ | H² | viável? |
|---|---|---|---|---|---|
| 0.001 | 0 | 1.7e−09 | +6.7e−09 | +1.0e08 | sim |
| 0.001 | **1** | 1.9e+04 | **−9.4e+03** | +2.9e07 | **não** |
| 0.1 | 1 | 19.7 | **−8.38** | +32.2 | **não** |
| 1 | **1** | 2.358 | **+1.985** | +0.334 | **SIM** |
| 10 | 1 | 2.227 | +2.227 | +0.288 | **SIM** |
| 10³ | 1 | 2.227 | +2.227 | +0.288 | **SIM** |

Idêntico em β₁ = 4.47 (segunda raiz viável a partir de a ≈ 1, com
r = 8.0).

**Leitura correta:** a segunda raiz tem ξ < 0 no primordial e ξ > 0 no
tardio, logo **ξ cruza zero** em algum a ∈ (0.1, 1). Uma trajetória
cosmológica contínua nesse ramo teria de atravessar ξ = 0 — lapso do
setor f anulando-se, ponto singular. **A exclusão para uma história
contínua está portanto CORRETA**; o que estava errado era a
justificativa ("dá ξ<0", sem qualificar época).

**Mas há um achado real:** existe uma **segunda solução tardia
viável** (r ≈ 2.23, ξ ≈ 2.23, H² > 0), completamente inexplorada pelo
repositório. Ela não se conecta ao nosso primordial, mas é uma
configuração de fundo legítima da mesma ação. Como o problema atual é
justamente o primordial, vale registrar: *o espaço de soluções do
fundo é maior do que a cascata assumiu.*

**Correção a aplicar:** `resultado_ramo_finito.md` §2 e o cap. 05 da
v2 devem dizer "ξ < 0 **no regime primordial**; a segunda raiz torna-se
viável em a ≳ 1 mas não conecta continuamente (ξ cruza zero)".

## Parte B — A modulação β₁(φ₋) **não** salva: a instabilidade sobrevive

Medido c_s²(a) ao longo do fundo dinâmico completo (célula REF,
condensação de φ₋, fatias moduladas com β₁′ e β₁″, kh = 30):

| a | r | φ₋/v | c_s² |
|---|---|---|---|
| 0.010 | ~0 | 0.001 | **−1.010** |
| 0.047 | 2e−04 | 0.001 | **−0.999** |
| 0.100 | 1.6e−03 | 0.001 | **−0.901** |
| 0.216 | 0.011 | 0.001 | **−0.287** |
| 0.465 | 0.026 | 0.002 | +0.698 |
| 1.0 | 0.030 | 0.003 | +0.974 |
| ≥10 | 0.031→0.50 | 0.015→0.93 | +1.01 a +2.17 |

**Resultado:** c_s² < 0 em 5/22 amostras, de a = 0.010 a a = 0.216 —
**3.07 e-folds** de instabilidade. O crescimento acumulado para o modo
kh = 30 é **lnA = 85.7**, muito acima do limiar de não-linearidade
(11.5). **A instabilidade sobrevive à modulação.**

Duas observações finas:

1. **A modulação muda o limiar, e para melhor.** No fundo β-constante
   a estabilidade só chega em r ≈ 0.17; no dinâmico, c_s² já é
   positivo com r ≈ 0.026 (a = 0.465). Ou seja, β₁(φ₋) *desloca* a
   fronteira — é a primeira vez que a modulação produz um efeito
   físico favorável mensurável. Mas o deslocamento não é suficiente:
   a era instável ainda dura 3 e-folds.
2. **A condensação chega tarde demais.** Em a = 0.465, φ₋/v = 0.002 —
   a condensação ainda não começou. O que estabiliza ali é a evolução
   de r pela diluição de ρ, não a modulação. A modulação só age em
   a ≳ 10³ (φ₋/v > 0.01), muito depois da era instável.

**Consequência de desenho:** se a modulação for para salvar a
implementação, ela precisa **ocorrer mais cedo** — o que significa
mexer em μ₋/λ_c (a época crítica da bifurcação), não em v★. Isso
conecta com o vínculo de paredes de domínio do parecer de fundamentos
quânticos (μ₋ ≲ λ₋^{1/3} MeV): as duas restrições agora apontam para o
mesmo parâmetro, em direções que precisam ser checadas juntas.

## Fronteiras e ressalvas

Uma trajetória (célula REF), sem radiação, kh = 30, 22 amostras. O
calibrador (espectador) fica em 0.997–1.023 — nos pontos tardios
desvia 2.3% de 1, acima do 1% ideal; os pontos da era instável têm
calibração 1.00000, portanto o achado principal não é afetado. Um
ponto (a = 4.6e3) reportou K₂ < 0 isoladamente, fora da era instável e
sem afetar o veredito — anotado para verificação.

## O que resta das saídas do R-10a §4

| Saída | Estado |
|---|---|
| 1. Screening / auto-invalidação linear | **Única viva** — não testada; agora é o único caminho conhecido |
| 2. Ramo infinito | **Fechada** (não conecta continuamente) — mas há segunda solução tardia inexplorada |
| 3. Varredura de forma-β | Aberta; o R-8b mostrou rigidez da forma sob rescala, falta varrer forma |
| 4. Corte de época pela modulação | **Fechada** — a modulação chega ~3 ordens tarde demais |

**Fila:** o teste de Vainshtein/validade linear passa de "item nº 1"
a **único item**: é a última saída conhecida antes de concluir que a
implementação F1, no ramo finito e com esta forma-β, tem uma era de
instabilidade de gradiente que nenhum mecanismo interno cura.
