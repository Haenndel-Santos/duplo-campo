# R-3 — Fase B por Evolução Real na Rolagem — Resultado

**Data:** 2026-08-12. Script: `auditoria/code/r3_faseB_evolucao_rolagem.py`
(saída em `auditoria/code/out/r3_faseB_evolucao_rolagem.txt`).
**Autoria colaborativa registrada:** script escrito pela sessão paralela
do autor sobre o estado pós-R-2; revisado, corrigido (3 iterações de
andaime: kination do fundo-controle GR → Λ_GR=3.0; janela tardia
adaptativa do controle; pré-escala do QEP em comóvel real) e executado
por esta sessão, com diagnóstico R3-MECANISMO adicionado pela paralela
durante a iteração. Execução autorizada (.venv).

**Controles (todos passam):** GR selfcheck ✓; R3-GR-A (nulo, k UV) ✓;
**R3-GR-B (positivo, k IR): o pipeline DETECTA crescimento espinodal
real (+0.53H ≥ 0.24)** — primeiro controle positivo de poder do
programa; R3-PODER nos dois k (congelado-de-verdade realiza o σ
congelado: +14.04 vs 12.44; +21.27 vs 22.63) ✓; halving 0.009 ✓;
fundo confere com a Fase A (r_fim, χ/v) ✓; ponte com a Fase B: âncora
congelada em a=1250/k_phys=1 dá σ/H=8.44, dentro do ~8–11 da tabela da
Fase B ✓ (o instrumento congelado é consistente entre convenções — a
dinâmica é que não o realiza).

---

## 1. Os três resultados

### 1.1 R3-ROLAGEM: NÃO-REALIZA (os dois k) — terceira confirmação do watershed

Na janela não-fatorada (a∈[760,2050]), com σ* congelado = 12.44/H
(k_c=1250) e 22.63/H (k_c=12500):

| k_c | taxa métrica máxima real | vs 0.5·σ* | veredito |
|---|---|---|---|
| 1250 (k_phys~1 no centro) | **−1.84/H** (decai!) | 6.22 | NÃO-REALIZA |
| 12500 (k_phys~10) | +0.47/H | 11.31 | NÃO-REALIZA |

**A extensão do no-go ao regime não-fatorado
(`resultado_investigacao2_faseB.md`) é vácua como veredito dinâmico** —
fica como caracterização do espectro congelado. O quadro D2/R-1 se
estende à rolagem. Com isto, TODAS as leituras congeladas de saúde do
programa foram testadas dinamicamente onde importava: nenhuma se
realizou.

### 1.2 O modo de condensação sobrevive à dinâmica real — e é o candidato do Cap.1

R3-SPINODAL + R3-MECANISMO, em dinâmica real:

- **δχ (condensação)**: cresce na rolagem **acompanhando a espinodal
  do fundo** (+1.09/H vs 0.95/H do fundo), **só em k IR** (em k UV
  decai: −0.38/H) — assinatura de **massa**; para de crescer no pouso
  e decai no tardio (k IR: −1.14/H). Duas instabilidades, destinos
  opostos — agora em tempo real.
- **Bloco métrico (transiente)**: cresce só em k alto (−1.84 IR vs
  +0.47 UV na rolagem) — assinatura de **gradiente**.

**Consequência para o `gate_fantasma_estrutural.md` §5:** a separação
mecânica é limpa. A bifurcação do Cap.1 (instabilidade de massa do
modo diferencial) mapeia no **modo de condensação** — dinamicamente
real, fisicamente sensato, auto-limitado — e não no setor métrico. A
ressalva "identificação prematura (aguarda R-3)" pode ser atualizada
para: *a identificação é agora suportada no nível de mecanismo
(tipo-massa, IR, acompanha o parâmetro de ordem, satura no pouso);
segue interpretativa no nível de derivação (a seta Φ₋→δχ→r continua
não-derivada — G1-a).*

### 1.3 NOVO: crescimento tardio real ~+1H na família modulada-pousada

R3-TARDIA deu **MISTO** nos dois k — e o conteúdo do "misto" é o
achado novo do R-3:

- k_c=12500: **todas as 4 ICs métricas crescem a +0.98/H** na janela
  tardia (a∈[8000,18000]; ln|y| da IC0: +3.8→+6.2, subindo no corte);
  o bloco δχ também (+1.25/H).
- k_c=1250: uma IC métrica (+1.05/H, q E_f); δχ decai.
- Taxa ≈ k-independente entre os dois casos que crescem.

É o **primeiro crescimento tardio real do programa** (R-1: 14/14
células β-constantes diluíam). Abaixo do limiar pré-declarado de
CRESCE (0.5·σ_anc = 1.17–1.40), portanto não classifica como
realização do congelado — é outra coisa. **Hipótese mecânica
(nível 3, nomeada):** bombeamento paramétrico pelas oscilações
residuais de χ do fundo pousado (ω_χ/H≈4.4; o anel residual
\|desl\|~1e-2 é declarado no desenho) — suportada por: o mesmo k_phys
na fase rolante DECAI (não é k_phys; é o estado do fundo), e o efeito
é mais forte no k que atravessa a ressonância. **Teste nomeado
(follow-up):** reintegrar o fundo com as oscilações de χ amortecidas
à mão (ou janela a>50000, pós-decaimento) — se o crescimento sumir, é
paramétrico (fenômeno tipo-preheating da família modulada, interessante
por si); se persistir, a família modulada-pousada tem instabilidade
tardia genuína ~1H e o R-4 herda a questão.

**ATUALIZAÇÃO (R-3b, 2026-08-12 — `resultado_r3b_pousada.md`):**
convergido (halving k=12500, Δ=0.0031 ✓); hipótese paramétrica
**REFUTADA** (o crescimento persiste — e sobe — com as oscilações
amortecidas; a sonda de banda dá negativo); estrutura **IR** (morre em
k_phys≳2; k_c=25000 dá +0.06 onde o congelado diz 41.7); o braço
amortecido revelou lacuna de desenho (drift secular > oscilação
original), então genuína-vs-secular segue em teste → R-3c.

**ATUALIZAÇÃO (R-3c, 2026-08-12 — `resultado_r3c_mecanismo.md`):**
PONTO-FIXO (taxa plana sob desvio ~1%→7%) **e** presente no
β-constante ESTÁTICO β₁=4.47 (+1.08 na banda k_phys~H, δχ desacoplado
exato) — o fenômeno é **da classe β-constante**, não do
pouso/modulação; o pousado herda do ponto onde senta. A "estrutura IR"
relê-se como cruzamento de horizonte (k_c=25000 cruza fora da
janela). Fronteira em β₁, transiente-vs-sustentada e a anomalia IR do
k=1250 → R-4a.

## 2. O dano transiente (insumo do R-4)

lnA_met máximo: **14.17** (k_c=1250) / **17.80** (k_c=12500) —
acumulado desde a=100, incluindo o crescimento pré-janela (+2.13/H na
fase U₀-dominada) e o transiente. Ordem de grandeza igual ou acima do
pior caso da R-1 (14.6). O mapa lnA(célula, k, trajetória) vs janela
observacional é agora claramente **a** questão de viabilidade da F1 —
o R-4 deixa de ser opcional.

## 3. Avisos numéricos declarados

1. As contagens do QEP **7×7** nas âncoras oscilam (3–6) mesmo com
   pré-escala — pareamento ±λ instável nas escalas comóveis extremas
   (entradas ~1e11). **Não interpretáveis como contagem/BD.** As
   âncoras confiáveis são as da reduzida 3×3 (contagem fixa = 3).
2. Convenção comóvel real: k_phys varia fator ~200 no range —
   declarado no desenho; as janelas fixas em a misturam k_phys
   diferentes entre k_c (a comparação IR/UV do MECANISMO usa a mesma
   janela, não o mesmo k_phys).
3. Três iterações de andaime do controle GR antes do run limpo —
   registradas no script com comentários datados; a física bimétrica
   nunca falhou nas iterações.
4. **O halving da rodada cobriu só k_c=1250** (Δ=0.009). O crescimento
   tardio de §1.3 vive em k_c=12500, que ficou **sem controle de
   convergência dedicado** nesta rodada. A favor da realidade do
   efeito: taxa moderada e sustentada (+0.98/H — instabilidade de
   integrador estoura, não cresce a ~1H), coerência entre as 6 ICs, e
   a dependência de FASE (o mesmo k_phys na fase rolante decai).
   Ainda assim, o follow-up de §1.3 deve **abrir pelo halving em
   k_c=12500** (barato: uma rerodada com NPTS dobrado) antes de
   qualquer enunciado apoiado no achado.
   **RESOLVIDO (R-3b, 2026-08-12):** Δ(halving k=12500) = 0.0031
   < 0.05 — o achado é convergido; a linha da estratificação sobe
   para 2b.

## 4. Estratificação epistêmica

| Afirmação | Nível |
|---|---|
| σ congelado da rolagem não se realiza (dois k; PODER ✓) | 2b (uma trajetória, célula REF, k_c={1250,12500}) |
| Condensação: tipo-massa, IR, acompanha o fundo, satura | 2b |
| Transiente métrico: tipo-gradiente | 2b (dois k) |
| Crescimento tardio real ~1H na família pousada | 2b provisório (observado; mecanismo em aberto; halving do k alto pendente — §3.4) |
| Hipótese paramétrica para 1.3 | 3 (nomeada, com teste declarado) |
| Identificação condensação ↔ narrativa Cap.1 | mecanismo: 2b; identidade: segue interpretativa (G1-a) |

## 5. Fila

- **R-4** (agora urgente): mapa lnA(célula, k) vs vínculos + o
  follow-up do crescimento tardio paramétrico (§1.3), abrindo pelo
  halving em k_c=12500 (§3.4).
- **Gate F** inalterado (F-a primeiro).
- O enunciado final do setor escalar ganha o §1.3 como item novo.
