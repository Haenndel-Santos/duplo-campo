# R-4a — O Mapa do Fenômeno Tardio: a Banda é da Classe Inteira, e é Transiente de Cruzamento — Resultado

**Data:** 2026-08-12. Script: `auditoria/code/r4a_mapa_tardio.py`
(saída em `auditoria/code/out/r4a_mapa_tardio.txt`). Execução: autor
(.venv). Bloco 1 do R-4; fecha as três perguntas declaradas em
`resultado_r3c_mecanismo.md` §5.

**Portão de credibilidade:** R4a-NULL **PASSA** — GR com o cruzamento
DENTRO da janela tardia (k_phys/H 1.37→0.61) dá taxas negativas em
todas as janelas e nos dois k (−0.08 a −1.64). A banda de crescimento
bimétrica não é artefato do pipeline. negK=1 em TODAS as âncoras de
TODOS os braços (β₁=1→4.47, estáticos, pousado, até a=70000) — a
assinatura estrutural é da classe, período (insumo Gate F).

---

## 1. R4a-MAPA: a banda é da CLASSE INTEIRA

Taxa métrica máxima na tardia (janela com k_phys/H 1.38→0.61 nos
braços "banda", calibrada por fundo):

| β₁ | banda | 3× (kh 4.1→1.8) | 0.1× (kh 0.14→0.06) |
|---|---|---|---|
| 1.00 | **+0.93** | +1.60 | −0.98 |
| 2.00 | +0.81 | +0.91 | +0.24 |
| 3.00 | +0.93 | +0.64 | −1.23 |
| 4.47 | +1.06 | +0.44 | −1.03 |

**β₁=1 cresce na banda.** O ramo pré-declarado CLASSE-INTEIRA
dispara: o fenômeno não é esquina — é a família β-constante toda, com
taxa ~ +0.8–1.1/H quase independente de β₁. E o crescimento não é só
na janela do cruzamento: nos fundos estáticos ele aparece em todas as
janelas com k_phys/H ≳ 0.5 (rolagem kh 14→5: +0.9–1.5; pouso kh
5.2→1.6: +1.5–2.2), morre no infravermelho profundo (0.1× em
pouso/tardia: negativo) e tem uma componente E_f-específica em kh
alto (pré, kh 73→24: só o par E_f cresce; em kh 220→73 nada cresce).
Faixa ativa observada: **k_phys/H ~ 0.5 a ~30** (bordas por
componente; forma fina → R-4b).

## 2. Sem contradição com D2/R-1 — e a reinterpretação

Recalculando as janelas antigas em k_phys/H (H≈0.557 do fundo REF, já
de Sitter em a≳1):

- R-1 "tardia" [400,1900], k_c=10: kh = 0.045→0.009; k_c=100:
  0.45→0.09 — **fora/na borda inferior da banda** → DILUI ✓ (nossos
  braços 0.1× reproduzem). O enunciado "estável tarde" era verdadeiro
  APENAS no infravermelho amostrado.
- D2 "transição" [15,45], k_c=10: kh = 1.20→0.40 — **dentro da
  banda**; k_c=100: kh 12→4 — idem (região do "3×"). O "transiente de
  transição tipo-gradiente" do D2/R-1 era muito provavelmente **esta
  mesma banda**, vista de raspão por modos que cruzavam naquela época
  (o fundo já era de Sitter em a=15 — a "época de transição" era dos
  MODOS, não do fundo). Reinterpretação consistente com os números
  antigos (rate ∝ k observado = subida da banda); confirmação fina
  fica para o R-4b (nível 3 → 2b barato).

## 3. R4a-EXT: transiente de cruzamento — por modo, lnA finito

| fundo | tardia (kh 1.4→0.6) | tardia2 (kh 0.37→0.16) | veredito |
|---|---|---|---|
| β-const 4.47 | +1.08 | **−1.06** | TRANSIENTE-DE-CRUZAMENTO |
| pousado | +0.98 | **−0.72** | TRANSIENTE-DE-CRUZAMENTO |

Cada modo cresce enquanto está na faixa ativa e **dilui depois do
cruzamento profundo**. Não é instabilidade sustentada do vácuo — é
**amplificação de banda por modo, com lnA total finito**. lnA_met dos
braços: 11–18 (medida em base comóvel, caveat de base declarado desde
o R-3; comparação relativa entre braços é o que vale).

## 4. O enunciado que emerge (rascunho para o cap. 07, v2 do rascunho R-2 §3)

> O setor escalar tardio da TDCP-F1 β-constante não é nem o "taquião
> eterno" congelado (vácuo — D2/R-1) nem simplesmente estável: **toda
> a classe** tem uma **amplificação transiente de banda** — modos com
> k_phys/H ~ 0.5–30 crescem a ~1–2/H (GR-limpa, ponto-fixo,
> não-paramétrica, presente em fundos estáticos e dinâmicos), cada
> modo por tempo finito ao redor do seu cruzamento, com lnA(k, célula,
> época) grande (≳ 10 nos casos medidos). Os instrumentos congelados
> nunca a viram (σ congelado não correlaciona em nenhuma direção:
> 1.7 vs +1.1; 3.1 vs −1.9; 41.7 vs +0.06); a amostragem dinâmica
> anterior a perdeu por estar fora da banda. A viabilidade da F1 no
> setor escalar é, portanto, uma questão **observacional**: o dano
> e^lnA nos modos que cruzam nas épocas relevantes versus vínculos —
> mapa em curso (R-4b). A direção cinética negativa estrutural
> (negK=1) permanece universal e independente disso (Gate F).

## 5. Estratificação epistêmica

| Afirmação | Nível |
|---|---|
| R4a-NULL: banda ausente em GR no mesmo pipeline/kh | 2b |
| Banda presente em β₁=1,2,3,4.47 estáticos (~+0.8–1.1 na banda) | 2b |
| Logo CLASSE-INTEIRA (dentro do retângulo amostrado + esquina 4.47) | 2b |
| Transiente de cruzamento (tardia2 dilui nos dois fundos, a→80000) | 2b |
| Faixa ativa kh~0.5–30 com estrutura por componente (E_f alto-kh) | 2b descritivo (bordas grossas; forma → R-4b) |
| Reinterpretação do "transiente de transição" de D2/R-1 como a banda | consistência 2b; confirmação dedicada pendente |
| "Estável tarde" de R-1 restrito a kh≲0.5 | 2b (atualização anotada no doc R-1) |
| lnA absolutos | 2b instrumental (base comóvel — comparação relativa) |
| negK=1 universal (agora até a=70000, todos os fundos) | 2b |

## 6. Fila

- **R-4b** (`auditoria/code/r4b_forma_da_banda.py`, pronto): a FORMA
  da banda — taxa(kh) por janelas de kh (não de a), lnA de passagem
  completa por modo (kh 20→0.2, excluindo a componente E_f de
  entrada), fundos β₁={1, 4.47} estáticos (em fundo estático o lnA de
  passagem é universal em k — uma medida por fundo) + pousado com
  grade de k por época de cruzamento (a_cross ∈ [500, 30000] — a
  rolagem/pouso modula a banda?) + GR-null de passagem completa.
- **Bloco 2 do R-4 (com o autor):** dicionário do modelo-brinquedo
  para épocas físicas (que a corresponde a que era; onde entram os
  vínculos de Comelli/Könnig/Akrami) — decisão de desenho do autor,
  não do instrumento.
- Depois: enunciado final → **Gate F-a** → cap. 07.
- Anomalia IR do pousado (k=1250): segue aberta, fora do quadro
  principal.
