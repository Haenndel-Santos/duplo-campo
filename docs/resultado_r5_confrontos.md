# R-5 — Os Três Confrontos Nível-Paper: ISW Aponta Tensão; Dispersão √k Discrimina da Literatura; Tensão-Akrami Localizada no Canto-β

**Data:** 2026-08-12. Script: `auditoria/code/r5_confrontos_paper.py`
(2ª rodada — oficial — em `out/r5_confrontos_paper.txt`; 1ª preservada
em `out/r5_confrontos_paper_rodada1.txt`; diferenças da v2: fit do
R5-B sem o gate de ε_W — é a *tendência* do ramo congelado-canônico,
com ε_W anotado — e a razão de transferência adicionada ao R5-A).
Execução: em sessão. R5-BASE OK (lnA âncora +3.97 = R-4b exato).

---

## 1. R5-A — a transferência f→g: o potencial-g CARREGA a banda

A banda vive no par f (Ψ_f, E_f); o observável são os potenciais-g,
que aqui são multiplicadores algébricos X = W′_XX⁻¹(C′_QXᵀQ̇ − W′_XQ Q).
Medido ao longo das soluções amplificadas:

- **Razão sustentada:** mediana |Φ_g|/|q_met| = **0.160** através da
  banda (kh 0.5–6; 60 marcos × 4 ICs), sem decaimento secular — a
  razão constante significa que o **fator de amplificação da banda
  aplica-se integralmente a Φ_g** (a razão fixa a normalização, não o
  crescimento).
- As taxas por componente entre marcos são ruidosas (log de componente
  única cruzando zeros; mediana +0.83 declarada NÃO-robusta) — o
  número robusto é a razão sustentada. Classificação de critério:
  "intermediário" pela letra; **CARREGA** pela evidência da razão
  (ressalva de método declarada; magnitudes em base comóvel são
  indicativas, a *constância* é o dado).

**A aritmética ISW (ordem de grandeza, dicionário mínimo):** os modos
da curva-B (R-4c) em kh_hoje 1–6 ↔ ℓ ≈ 3–19 (ℓ ≈ 3.2·kh). O imprint
SW (recombinação) é intocado (banda desligada na era de matéria —
R-4c); o ISW tardio é sourced por Φ̇ na era Λ — exatamente onde a
banda amplifica ×3.2–×6.6 em amplitude → contribuição ISW em potência
×10–×43. Com fração ISW ~10–25% do TT em ℓ≲20: realce total estimado
**~2–8× na potência do baixo-ℓ**. O TT observado em baixo-ℓ é
consistente com ΛCDM e, se algo, BAIXO — um excesso de fator 2–8 é
fortemente desfavorecido mesmo com variância cósmica.

> **Consequência honesta (revisa o "brando" do R-4c):** no dicionário
> mínimo, a banda é uma **previsão falsificável de excesso ISW em
> baixo-ℓ** — e a direção observada é a oposta. O confronto fino
> (C_ℓ completo, fora do brinquedo, com normalização primordial e
> matéria perturbada) é o item decisivo do paper; a aritmética de
> ordem de grandeza aponta **tensão real**, não conforto. Ressalvas
> declaradas: sem perturbações de matéria acopladas; transferência
> medida no brinquedo; janela Λ real ~0.7 e-fold (sensibilidade
> ~linear).

## 2. R5-B — a dispersão da banda: √k, não gradiente

Tendência do ramo congelado-canônico (legitimado onde assenta pelo
CONF-BANDA; ε_W anotado na tabela do out):

- **Fit σ_can = c·kh^p em kh∈[1.5,30]: p = 0.44** (c ≈ 1.5) — a
  instabilidade de gradiente da literatura (Comelli/Könnig) tem
  **p = 1**. Discriminada.
- **Saturação IR:** σ_can → 1.13/H em kh < 0.3 (cauda tipo-massa).
- Combinado com o R-4a (o "transiente de transição" de D2/R-1 era a
  banda cruzada pelos modos daquela época — o fundo já era de Sitter
  em a=15) e o R-4c (chave = fração bimétrica, não época de
  transição): **a banda é um fenômeno distinto da instabilidade de
  gradiente conhecida** — dispersão ~√k com saturação, era de domínio
  bimétrico, transiente por modo. Para o paper: a comparação
  fonte-a-fonte usa o posicionamento (docs/posicionamento_literatura)
  com este p como o discriminador quantitativo.

## 3. R5-C — a escada de μ: tensão-Akrami confirmada e localizada

lnA de passagem (métrica limpa, kh 20→0.2) + espectro canônico:

| célula | β₁ | β₂ | μ | lnA_pass | ω₀/H | ω₀/Λ₃ | σ_can tardio |
|---|---|---|---|---|---|---|---|
| âncora | 1.0 | −0.4 | 1.0 | +3.97 | 12.0 | 4.3 | 1.13 |
| fresta | 0.2 | −1.0 | **0.1** | **+5.91** | n/a† | n/a† | n/a† |
| fresta | 0.2 | −1.0 | 1.0 | **+6.21** | n/a† | n/a† | n/a† |
| REF | 1.0 | −0.4 | 0.3 | +3.73 | 14.9 | 4.9 | 0.75 |
| REF | 1.0 | −0.4 | 3.0 | +3.84 | 11.2 | 4.1 | 1.20 |
| REF | 1.0 | −0.4 | 10.0 | +5.24 | 12.6 | 4.7 | 1.20 |

† o quadro canônico não se aplica/assenta na fresta — é a célula do
"fantasma quase-nulo" da R-1 (autovalor negativo ~−3e-4): a
normalização |λ₀|^{−1/2} é singular-adjacente. Fronteira declarada
(tratamento dedicado se o paper precisar).

- **TENSÃO-AKRAMI CONFIRMADA na métrica limpa** (+1.93 acima da
  âncora na fresta μ=0.1) — **e refinada: é o canto-β, não o μ**
  (fresta μ=1 dá +6.21; a escada de μ na REF varia só 3.7→5.2). A
  região de escape da literatura (canto β₁ pequeno/β₂ grande-negativo,
  μ pequeno) carrega lnA_pass ≈ 6 (×370 em amplitude por passagem
  completa; proporcionalmente ~×16 na integral parcial da era Λ real,
  estimativa linear declarada) — **o confronto ISW é mais duro
  exatamente na rota de escape**.
- **ω₀/Λ₃ = 4.1–4.9 em todas as células mensuráveis** — o fecho H-SC
  do Gate F é uniforme na amostra (nenhuma célula com o fantasma
  abaixo do cutoff → F-c não revive em lugar algum medido).

## 4. Estratificação epistêmica

| Afirmação | Nível |
|---|---|
| Transferência f→g sustentada (razão 0.16 constante na banda) | 2b (razão robusta; magnitude absoluta = indicativa, base comóvel) |
| Aritmética ISW: realce ~2–8× na potência ℓ≲20 | estimativa de ordem de grandeza no dicionário mínimo (cadeia declarada) — nível 3 quantificado; C_ℓ completo pendente |
| p = 0.44 (dispersão √k; não-gradiente) | 2b como tendência do ramo congelado-canônico (ε_W anotado; assentado só no IR) |
| Saturação IR σ_can→1.13 = taxa real | 2b (CONF-BANDA) |
| Tensão-Akrami: canto-β com lnA_pass ≈ 6 | 2b (métrica limpa; 6 células) |
| ω₀/Λ₃ ≈ 4–5 uniforme | 2b (proxy Λ₃ REF-ancorado declarado) |
| Fresta: quadro canônico singular-adjacente | fronteira declarada |

## 5. Consequências e fila

1. **O enunciado do cap. 07 ganha a forma final (v5):** o setor
   escalar sobrevive a todos os testes internos (dinâmica, vínculo,
   cutoff) e converge para UMA previsão observacional dura: excesso
   ISW/baixo-ℓ de fator ~2–8 na potência (pior no canto-β) — em
   tensão com o TT observado. O item decisivo do paper é o C_ℓ
   completo; o brinquedo entregou tudo o que podia (amplitude, banda,
   chave, transferência, dispersão).
2. Trilha de escrita: cap. 07 com v5 + a comparação de literatura
   (posicionamento + p=0.44 + a releitura de época).
3. Fronteiras que ficam: C_ℓ completo (fora do brinquedo); fresta
   canônica; anomalia IR do pousado; par E_f cedo; perturbações de
   matéria (limitação de programa).
