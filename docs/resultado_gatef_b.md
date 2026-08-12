# Gate F-b — Resultado: Sem Vínculo Escondido; o Fantasma é um Ramo Espectral Canônico a ω₀ ≈ 3–4·Λ₃ (H-SC, com número)

**Data:** 2026-08-12. Script: `auditoria/code/gatef_b_canonica.py`
(v2 — arquitetura de integração única + diagnóstico local; oficial em
`out/gatef_b_canonica.txt`; 1ª rodada preservada em
`out/gatef_b_canonica_rodada1.txt` com a autópsia no cabeçalho).
Execução: em sessão (autorização permanente do autor, 2026-08-12).

**Validações (todas passam):** V-ETA = 1.1e-15 (TᵀKT=η exato na grade
inteira); **V-RES = 0.001** (o resíduo da EOM canônica sobre a
trajetória real transformada — valida C_can/W_can/Ṫ exatamente onde
os diagnósticos usam); V-EQUIV-GR = 3.2e-5. Registro de instrumento:
a 1ª rodada reprovou no V-EQUIV por decoerência entre duas
integrações independentes (padrão: IC de velocidade 3.5e-4 ✓, ICs de
posição O(1–10) ✗) — fragilidade de desenho retirada na v2, não
física.

---

## 1. H-CONSTRAINT cai — em coordenadas válidas, por três linhas independentes

1. **Sem hierarquia:** R_can satura em ~10 (β₁=1) / ~5 (β₁=4.47) —
   nunca ≥100. A frequência da direção K<0 **satura** (12.0H / 7.4H,
   constante nos marcos finais). O "quer ser vínculo" do R-2
   (ω² → 1.4×10⁹ crescendo) era **artefato da base comóvel** — a
   lição do R-2 §2 aplicada ao próprio R-2.
2. **PODER falhou de novo** (superfícies real E falsa planas):
   consistente — sem rigidez, a eliminação adiabática não é o quadro
   certo para NENHUMA direção; o teste de superfície não tem objeto.
3. **DESAC:** a IC pura-x₀ injeta fração leve 0.77 / 0.96 — a direção
   negativa é **fortemente acoplada** ao setor leve, o oposto de
   "expulsa/desacoplada".

A hipótese favorita do gate (a mais bem suportada pelos indícios
congelados) morre no quadro válido. A disputa de contagem 3-vs-2 do
D1 se resolve: **3 graus dinâmicos**, um deles de norma negativa.

## 2. O que existe: um ramo propagante de norma negativa com frequência invariante

Nos marcos assentados (ε_W < 0.3), o modo pesado é:

| fundo | ω₀/H (invariante) | conteúdo x₀ | norma-η s |
|---|---|---|---|
| β₁=1 | **12.0** (satura) | 0.988 | **−0.98** |
| β₁=4.47 | **7.4** (satura) | 0.975 | **−0.95** |

A energia do fantasma estrutural, indecidível desde o R-2, **agora
tem número**: um ramo espectral genuíno, ~puro na direção K<0,
propagante (ω ~ real), com norma-η negativa — em TODOS os marcos
assentados dos dois fundos.

## 3. A aritmética do cutoff — e o fecho H-SC

Com m_T²/H² → 12 (setor tensorial; âncora REF, robustez O(1)
declarada) e M_Pl = Mg = 1:

| fundo | H | Λ₃=(m_T²M_Pl)^⅓ | Λ₃/H | ω₀/Λ₃ |
|---|---|---|---|---|
| β₁=1 | 0.557 | 1.55 | 2.8 | **4.3** |
| β₁=4.47 | 1.125 | 2.48 | 2.2 | **3.4** |

**O ramo de norma negativa vive um fator ~3–4 ACIMA do cutoff Λ₃**
(e ~2–3.5× acima de m_T). Pelo critério F-b2 pré-declarado do gate:
**H-SC** — a direção está fora do alcance da ordem quadrática; sua
"letalidade" não é uma pergunta que a EFT quadrática possa responder.
É exatamente a posição da literatura (2507.11526: "breakdown of
linear perturbation theory rather than physical instability") — mas
agora **com o número invariante** que a literatura não tinha: ω₀ =
3.4–4.3·Λ₃, medido em variáveis canônicas com conexão retida e
validação de resíduo. F-c (interações) fica **fora de validade EFT**
neste nível — desnecessário salvo decisão contrária do autor (o gate
doc §2 já condicionava F-c a "fantasma físico ABAIXO do cutoff").

Consistência com tudo o que foi medido: a dinâmica LINEAR real é
estável no IR profundo e transiente na banda (D2/R-1/R-4) — um ramo
de norma negativa acima do cutoff não contradiz nada disso; ele
apenas marca onde a descrição quadrática termina.

## 4. CONF-BANDA: a reabilitação do instrumento congelado

| fundo | ε_W tardio | σ_can/H tardio | taxa real da banda (R-4a) |
|---|---|---|---|
| β₁=1 | 0.040 | 1.13 | +0.93 |
| β₁=4.47 | 0.030 | 1.41 | +1.06 |

**CONF-BANDA SIM nos dois fundos.** No quadro canônico K é constante
e W assenta — e o espectro congelado canônico **prevê a banda** que a
evolução real mede. O aviso metodológico do programa ganha a sua
resolução construtiva:

> O espectro congelado em base comóvel NÃO é árbitro de saúde nesta
> classe (D2 — matrizes que nunca assentam). O espectro congelado em
> base CANÔNICA (K=η constante; W assentada; conexão retida) É — e
> reproduz a taxa da banda com |Δ| < 0.5/H.

## 5. Estratificação epistêmica

| Afirmação | Nível |
|---|---|
| H-CONSTRAINT falsificada (sem hierarquia; saturação de ω₀; DESAC acoplado) | 2b (dois fundos; coordenadas validadas por V-RES) |
| Ramo propagante s≈−0.97 com ω₀ invariante 7.4–12.0H (satura) | 2b |
| ω₀/Λ₃ ≈ 3.4–4.3 (acima do cutoff) | 2b com âncora m_T²=12H² (REF; robustez O(1) declarada) |
| Fecho H-SC ("fora do alcance quadrático"; setor não exclui a F1) | consequência pré-declarada (F-b2) |
| Congelado canônico é árbitro e prevê a banda (CONF-BANDA) | 2b (dois fundos; ±0.5) |
| Contagem: 3 dof dinâmicos (disputa D1 resolvida) | 2b |
| Letalidade além do cutoff / interações | fora do alcance declarado (F-c só por decisão do autor) |

## 6. O Gate F fecha — e o enunciado final do setor escalar (v4)

> **Setor escalar da TDCP-F1 β-constante (nível linear, programa
> completo):** dinamicamente estável no infravermelho profundo
> tardio; UMA instabilidade real — a amplificação transiente de
> banda (k_phys/H ~ 0.5–30, ~e⁴ por passagem, classe inteira,
> GR-limpa), com chave física na fração bimétrica (desliga sob
> matéria → LSS ileso) e dano observável ≤ ×6.6 confinado a escalas
> ~horizonte hoje (alvo ISW/baixo-ℓ, não óbito); o modo de
> condensação δφ₋ realiza a condensação (tipo-massa) e assenta
> (candidato do Cap. 1 no nível de mecanismo); e a direção cinética
> negativa estrutural é um **ramo espectral canônico de norma
> negativa com frequência invariante ω₀ ≈ 3–4·Λ₃** — acima do
> cutoff: a teoria quadrática declara sua própria fronteira ali, em
> alinhamento (agora quantificado) com a literatura. **A F1 não está
> excluída no nível em que este programa pode julgar — e o programa
> julgou tudo o que esse nível contém.**

**Decisões do autor pendentes:** (i) sancionar o fecho H-SC do Gate F
(recomendado) ou encomendar F-c mesmo assim como estimativa
fora-de-validade; (ii) nível paper: confronto ISW/baixo-ℓ fino,
comparação quantitativa Comelli/Könnig, fresta μ=0.1 vs rota de
Akrami. Sub-estruturas abertas (não bloqueiam): anomalia IR do
pousado; par E_f cedo.
