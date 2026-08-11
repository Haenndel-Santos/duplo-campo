# G1-a — Tabela de Identidade da Cadeia {Φ₋, φ, χ, φ₋-v2, σ, S, r}

**Data:** 2026-08-11. Executa o G1-a de
`docs/gate1_identidade_relacional.md` §4 (documental; nível 1 — todo
item é verificável lendo o trecho citado do manuscrito, sem código).

**Cobertura:** Cap.1–19 e Apêndices B–L de `manuscript/` (todos os
arquivos que respondem ao grep por «modo diferencial | Φ₋ | φ₋ |
bifurca | grau relacional | variável relacional | tempo relacional»,
mais os vizinhos de contexto). Ocorrências recorrentes do mesmo uso
(ex.: "modo relativo" repetido em Cap.18/19 após o Cap.15) são
agrupadas numa linha — a classificação vale para o cluster.

**Critério do gate:** zero ocorrências sem classificação. ✔ (19
clusters, todos classificados abaixo.)

---

## 1. Classes de classificação

As três classes do protocolo, mais uma que o levantamento obrigou a
acrescentar:

| Classe | Significado |
|---|---|
| **DECRETO** | identificação afirmada sem derivação (interpretativa/normativa) |
| **INDEFINIDA** | dois nomes usados em lugares distintos sem o texto jamais dizer se são o mesmo objeto |
| **DISTINTA** | o corpus (ou uma âncora) distingue explicitamente os objetos, ou eles são formalmente distintos |
| **DERIVADA** | há álgebra genuína ligando os objetos — **nota:** nenhuma linha DERIVADA abaixo é uma *identificação* ("X é Y"); são acoplamentos ou propriedades. **Zero identificações da cadeia são derivadas.** |

## 2. A tabela

| # | Alegação (termos do corpus) | Onde | Classe |
|---|---|---|---|
| 1 | A instabilidade de Φ₋ (m₋²<0) "é" a bifurcação/Big Bang | Cap.1 §1.4; Cap.2 §2.2 | DERIVADA a condição m₋²<0; **DECRETO** a leitura "= Big Bang" |
| 2 | O "campo primordial φ" que modula β_n é o mesmo φ de Cap.1–2 (φ₁,φ₂) | reuso tácito de símbolo, Cap.2→Cap.19 | **INDEFINIDA** |
| 3 | φ ≡ χ (dois nomes do modulador) | Cap.14 §14.1: "campo estrutural φ (ou χ)" | **DECRETO** (parentético, única ocorrência, sem derivação) |
| 4 | χ modulador (Anexos B/E/F/H) vs. χ modo reduzido de perturbação (Cap.6 §6.4, rascunho antigo) | Anexo B §B.1 vs. Cap.6 §6.4 | **INDEFINIDA** (colisão interna de símbolo — ver §5) |
| 5 | Bifurcação de Φ₋ ⇒ gera as duas métricas g,f (logo r≠1) | Cap.3 §3.1; Anexo H Post.2; Anexo L §L.2 | **DECRETO** — o próprio Anexo L o admite: "como glosa narrativa […] Nenhuma equação muda" |
| 6 | Tempo relacional = ∫(H_g−H_f)²dt | Cap.5 §5.8 ("pode ser reinterpretado como") | **DECRETO** |
| 7 | Tempo/flecha = ln r/ΔH | Cap.12 §12.3 | **DECRETO**, inconsistente com #6 e #9 |
| 8 | η canônico: η̇=Γχ̇², H²∝1/(1−η) | Anexo H Post.5–6, §H.6; Anexo G §G.5; Anexo E | forma boxed, mas nunca mostrada equivalente a #6; Anexo B §B.9 adverte explicitamente que r e η NÃO são o mesmo canal → **DISTINTA** (do r), **INDEFINIDA** (vs. #6) |
| 9 | Tempo cosmológico = ln σ | Cap.10 §10.6 | **DECRETO** — quarta fórmula de tempo, não conciliada |
| 10 | σ "é onde o vácuo dinâmico vive", "carrega a memória do entanglement estrutural/da bifurcação" | Cap.6.2 §6.9, §6.12; Cap.7 §7.7; Cap.9 §9.7 | **DECRETO** (o texto se anuncia: "Interpretando:", "filosofia e matemática se encontram") |
| 11 | A instabilidade primordial de σ gera "estrutura espacial da bifurcação" (σ assume o papel narrativo de Φ₋) | Cap.10 §10.1–10.3 | DERIVADA a EOM de σ; **DECRETO** a troca de papel σ↔Φ₋ (nunca se escreve σ=δΦ₋) |
| 12 | A massa efetiva de σ é "o que controla" m_S (σ ≈ S) | Cap.13; reusado em Cap.14/18/19 | **DECRETO** (via vocabulário compartilhado "modo relativo"; nunca σ≡S como equação) |
| 13 | S ∝ Ψ_f−Ψ_g "é" o modo relativo (mesmo rótulo de σ) | Cap.15 §15.2 | DERIVADA a fórmula de S; **INDEFINIDA** a identidade com o σ abstrato do Cap.6.2 (construções formais diferentes, mesmo rótulo) |
| 14 | m_S² ∝ β₁+2β₂r = 2β₂(r−r★) | Cap.15 §15.5–15.8 | **DERIVADA** (álgebra explícita — o único elo genuíno da cadeia, e liga r à *massa* de S, não à identidade de ninguém) |
| 15 | O desvio de r de r★ "é" o momento da bifurcação | Cap.15 §15.8 | **DECRETO** (camada interpretativa sobre #14) |
| 16 | "Modo relativo" aplicado ao modo tensorial h₋ | Anexo D §D.5 | **INDEFINIDA** (mesmo rótulo, objeto matemático não-relacionado — tensor, não escalar) |
| 17 | Gráviton massivo h_m "é a vibração da diferença estrutural", eco da bifurcação | Cap.11 §11.9 | **DECRETO** (mesmo padrão, tangencial à cadeia) |
| 18 | Quadro de colapso quântico (Anexos I/J) vs. formalismo bimétrico clássico | Anexos I, J; Anexo L §L.4 | **DISTINTA** — o próprio corpus flagra: "não tem ponte demonstrada com a ação clássica bimétrica" |
| 19 | Contagem escalar: 3 modos (ζ,σ,δφ — Cap.6.2 §6.4) vs. 2 (helicity-0, δχ — Anexo C §C.3) | Cap.6.2 vs. Anexo C | **DISTINTA — resolvida pela D1**: o QEP conta **3** modos físicos; Cap.6.2 estava certo, Anexo C errado |

## 3. Resumo por objeto

- **Φ₋** — definido só em Cap.1–2 e Anexo G; **formalmente abandonado
  depois do Cap.3** (sem EOM, sem propagador, sem reaparição nos
  capítulos de perturbação). O acoplamento de portal λΦ₋²H†H do Cap.2
  §2.4 nunca mais é mencionado nem conciliado com a maquinaria
  β_n(φ)/F(χ). Elo com r: decreto axiomático (Anexo H Post.2) e glosa
  declarada (Anexo L). Elo com φ/χ: silêncio notacional completo.
- **φ/χ** — duas linhas notacionais paralelas (φ nos capítulos, χ nos
  anexos técnicos), declaradas equivalentes exatamente uma vez, entre
  parênteses (Cap.14 §14.1). χ tem ainda uma segunda colisão interna
  (ver §5).
- **r** — o único objeto com definição e EOM limpos. Seus elos
  narrativos com "tempo relacional"/bifurcação são decretados três
  vezes de formas mutuamente inconsistentes; o Anexo B §B.9 adverte
  contra colapsar r e η num canal só. Seu único elo derivado é com a
  massa de S (#14) — um acoplamento, não uma identidade.
- **σ/S** — o par mais intensamente identificado *por vocabulário* e
  menos identificado *por equação*: "modo relativo" nomeia σ (Cap.6.2+),
  S (Cap.10/15+) e até um modo tensorial (Anexo D), sem que nenhuma
  equação σ≡S exista no corpus.

## 4. Veredito do G1-a

**A cadeia Φ₋ → φ/χ → r → σ tem ZERO elos de identidade derivados.**
Cada identificação entre dois dos quatro objetos é decreto (com o
próprio texto por vezes se anunciando como interpretação) ou é
simplesmente indefinida. As únicas linhas DERIVADAS da tabela são
propriedades internas de um objeto (EOM de σ, condição m₋²<0) ou um
acoplamento (r→m_S²) — nenhuma é da forma "X é Y".

Isto confirma documentalmente, em nível 1, a premissa do Gate 1: os
quatro objetos são ligados por interpretação, nunca por derivação. Em
conjunto com o G1-b (que passou: a patologia da F1 tem projeção zero em
δφ₋ — `docs/resultado_investigacao1_ramo_algebrico.md` §3), o quadro é
consistente: **não há razão derivada nem evidência empírica para
identificar o grau relacional primordial com o modo doente da F1.**
R1 se sustenta pelos dois lados.

## 5. Subprodutos para o Gate 0 (colisões novas)

O levantamento encontrou itens que pertencem ao
`dicionario_simbolos.md`:

1. **χ modulador × χ modo reduzido** — no rascunho antigo do Cap.6
   (§6.4, "Equação Escalar Efetiva"), χ nomeia o modo escalar efetivo
   reduzido (o objeto que o Cap.6.2 chama de σ), colidindo com o χ
   modulador dos anexos. Terceira vida do símbolo χ (além de campo e
   distância comóvel). Como a v2 já aposenta χ-campo e o Cap.6 foi
   revisado pelo Cap.6.2, a colisão é histórica — mas deve constar do
   catálogo.
2. **"modo relativo" como rótulo sobrecarregado** — nomeia σ, S e h₋
   (tensor). Qualquer corpus v2 precisa de três nomes.
3. **Quarta fórmula de tempo relacional** — o `plano_v2_reconstrucao.md`
   Passo 10 lista três (T=f(H₁−H₂), τ~ln σ, t~ln r/ΔH); o η̇=Γχ̇²
   canônico do Anexo H é uma quarta variante narrativa do mesmo
   conceito, tampouco conciliada. O Passo 10 deve tratar quatro, não
   três.

## 6. O que este documento NÃO faz

Não julga a física das identificações (isso é o G1-b/G1-c e a
Investigação 2); não corrige o manuscrito (aguarda a decisão 1 do
usuário sobre o destino da v1); não estende o veredito além do que os
trechos citados dizem.
