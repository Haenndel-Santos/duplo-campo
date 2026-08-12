# R-3b — Família Pousada: Convergência e o Teste do Bombeamento — Resultado

**Data:** 2026-08-12. Script: `auditoria/code/r3b_pousada_parametrico.py`
(saída em `auditoria/code/out/r3b_pousada_parametrico.txt`). Follow-up
pré-declarado do achado §1.3 + caveat §3.4 de
`resultado_r3_rolagem.md`. Execução: autor (.venv), saída devolvida em
sessão.

**Pré-condições (todas passam):** R3b-BASE 0.003 (a rodada reproduz as
taxas oficiais da R-3 — sem drift de ambiente); **R3b-CONV 0.0031**
(halving no k do achado); R3b-CONT 0.0002 (o fundo amortecido é
idêntico ao original antes de a≈2100). Fundos conferem — nota: o DAM
pousa em r=0.504, χ/v=0.939 (vs 0.4979/0.932 do ORG); a própria
referência 0.932 do ORG é leitura *mid-anel* — a diferença é o drift
de aproximação, ver §2.

---

## 1. Os quatro resultados

### 1.1 O achado §1.3 é CONVERGIDO — o caveat §3.4 está resolvido

Halving (40000 pts) no k_c=12500: max|Δ taxa métrica| = **0.0031**
(critério < 0.05), janelas pouso e tardia. O crescimento tardio
~+1H da família pousada **não é artefato de resolução**. A linha
correspondente da estratificação do doc R-3 sobe de "2b provisório"
para **2b**.

### 1.2 A hipótese paramétrica é REFUTADA

Com as oscilações de χ amortecidas à mão (Γ=30 ligando em a=2400;
modo oscilatório morto em fração de e-fold), o crescimento tardio
**não cai — sobe**:

| braço | original | amortecido | veredito pré-declarado |
|---|---|---|---|
| k_c=12500 (tardia) | +0.98/H | **+1.12/H** | PERSISTE |
| k_c=1250 (tardia) | +1.05/H | **+1.87/H** | PERSISTE |
| k_c=25000 (tardia) | +0.06/H | +0.02/H | N/A (original já ~0) |

O bombeamento paramétrico pelas oscilações residuais **não é o
mecanismo** do crescimento tardio. Dois reforços independentes:
(i) a sonda de banda (D, k_c=25000, a_band≈8618 na tardia) mostra
taxas locais *negativas* na própria banda, e o burst do pouso de D
fica no MESMO lugar do de A (a∈[4000,6800]) apesar de a_band diferir
— o burst é **época-fixo, não k-fixo**; (ii) ω_χ medido (5.80,
ω_χ/H=4.99, 5 cruzamentos) está onde a hipótese previa, e ainda assim
o efeito não o rastreia.

**O que TEM componente de anel: o pouso.** C vs A no pouso:
+1.46 vs +2.37 (e E vs D: +1.42 vs +2.38) — amortecer o anel tardio
corta o burst do pouso a ~×0.6. Componente real, mas transiente e
menor que o swing de pouso em si (|desl|~0.2, idêntico nos dois
fundos porque antecede o amortecimento).

### 1.3 O crescimento tardio é IR — morre em k_phys ≳ 2

Estrutura em k na janela tardia (a∈[8000,18000]):

| k_c | k_phys na janela | taxa met máx |
|---|---|---|
| 1250 | 0.16→0.07 | +1.05 (ORG) / +1.87 (DAM) |
| 12500 | 1.56→0.69 | +0.98 / +1.12 |
| 25000 | 3.13→1.39 | **+0.06** / +0.02 |

Cresce em k_phys ≲ 1.5 e desliga acima. **Não é a instabilidade de
gradiente da literatura** (que cresce COM k) — é fenômeno IR
(escala ~horizonte, H≈1.14). Também não é a espinodal (χ já assentou;
U''>0).

### 1.4 O dado congelado-vs-real mais dramático da série

Âncora congelada (reduzida, pré-escalada) em a=15000, k_c=25000:
σ/H = **41.7** (ORG) / 52.8 (DAM). Taxa real na mesma janela:
**+0.06/H**. O instrumento congelado erra por três ordens de
grandeza de amplitude acumulada exatamente onde tem mais certeza.
E negK=1 em TODOS os braços e fundos (inclusive amortecido) — a
assinatura estrutural do R-2 é insensível a oscilações e ao drift
(insumo Gate F: é propriedade do ponto, não do transiente).

## 2. Autocrítica de instrumento — o que "PERSISTE" estabelece e o que não

O desenho do braço amortecido tinha uma lacuna **não antecipada**:
com Γ=30, o modo oscilatório morre rápido (✓), mas a aproximação
sobreamortecida ao ponto fixo é LENTA — λ ≈ m²_eff/(Γ+3)H ≈ 0.7/H,
mais lenta que o decaimento a^(−3/2) do envelope original. Resultado
medido: na tardia, o fundo amortecido está MAIS LONGE do ponto fixo
que o original (|χ−χ_fim|/χ_fim = 3.7e-2 vs 1.6e-2), só que por
desvio **secular** em vez de oscilatório.

Portanto:
- **ESTABELECIDO (2b):** o crescimento tardio não é
  paramétrico/oscilatório (não precisa do anel; não rastreia a banda).
- **NÃO ESTABELECIDO:** que seja instabilidade do *vácuo pousado
  exato*. A alternativa viva: crescimento alimentado pelo **desvio
  residual** do ponto fixo (secular ou oscilatório — qualquer
  departure), i.e. um transiente de aproximação de cauda longa. O
  fato de a taxa SUBIR no fundo amortecido (que tem desvio maior)
  é *consistente* com essa alternativa.

O ramo impresso pelo script ("INSTABILIDADE TARDIA GENUINA") seguiu o
critério pré-declarado, que não antecipou a contaminação secular —
fica **qualificado** para: *não-paramétrica; genuína-ou-secular*.
Mesma disciplina do R-2: o instrumento sob escrutínio, o registro
corrige o veredito impresso.

## 3. Os dois discriminadores (R-3c — script pronto)

1. **β-constante β₁=4.47** (braço G): o fundo pousado tem
   β₁_eff = β₁(χ_fim) = 4.47 — FORA do retângulo amostrado pela R-1
   (β₁ ≤ 2). Um fundo β-constante estático com β₁=4.47 (sem modulação,
   sem χ dinâmico), mesma faixa de a e k: se crescer, o fenômeno é da
   **esquina β₁-grande da classe** (e a R-1 não o viu por amostragem),
   não da família modulada; se diluir, é específico do fundo
   modulado-pousado.
2. **Correlação taxa-vs-drift** (braços Γ=10 / Γ=100): Γ=10 aproxima
   RÁPIDO (λ≈1.8/H → desvio mínimo na tardia); Γ=100 aproxima LENTO
   (λ≈0.2/H → desvio máximo). Se a taxa acompanhar o desvio →
   **secular-fed** (transiente de aproximação; o enunciado vira
   "transiente de pouso de cauda longa", dano finito a computar); se
   a taxa ficar ~constante enquanto o desvio varia por fator ≳5 →
   **instabilidade do ponto fixo** (genuína; R-4 herda com prioridade
   máxima).

**ATUALIZAÇÃO (R-3c, 2026-08-12 — `resultado_r3c_mecanismo.md`):**
os dois discriminadores rodaram: (i) **PONTO-FIXO** — taxa plana
(0.98–1.21) com a distância real ao ponto fixo variando ~1%→~7%;
(ii) **ESQUINA-β₁** — o β-constante ESTÁTICO com β₁=4.47 cresce igual
(+1.08 na banda k_phys~H): o fenômeno é da classe β-constante, o
pousado herda do ponto onde senta. "Genuína-ou-secular" fecha em
genuína — mas o dono mudou: não é "da família pousada", é da região
(β₁ grande?, k_phys~H) da classe. Controle β₁=1 na banda e
transiente-vs-sustentada: R-4a.

## 4. Estratificação epistêmica

| Afirmação | Nível |
|---|---|
| Achado §1.3 (crescimento tardio ~+1H) convergido | 2b (halving no k do achado) |
| Hipótese paramétrica | **REFUTADA** (2b — A/B em três k + sonda de banda) |
| Crescimento tardio é IR (morre em k_phys≳2) | 2b |
| Burst do pouso: componente de anel real (~×0.6), época-fixa | 2b |
| σ congelado 41.7 vs real 0.06 (k=25000, a=15000) | 2b (mais um dado do watershed) |
| negK=1 insensível a oscilações/drift | 2b (insumo Gate F) |
| "Instabilidade do vácuo pousado" | **EM ABERTO** — genuína-ou-secular (R-3c decide) |

## 5. Fila

- **R-3c** (`auditoria/code/r3c_pousada_mecanismo.py`, pronto):
  braços G (β-const 4.47), H/I/K (Γ=10/100) — decide
  modulação-vs-β₁-grande e genuína-vs-secular.
- Depois: **R-4** com o enunciado correto do fenômeno tardio
  (mapa lnA + vínculos), **Gate F-a** inalterado.
- O §1.3 do doc R-3 recebe atualização apontando para este doc.
