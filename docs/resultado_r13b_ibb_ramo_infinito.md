# R-13b — MEDIÇÃO DO RAMO INFINITO EM CÉLULAS IBB: r′ < 0 em 108/108, ξ cruza zero uma vez, e m_T²/H² < 2 em toda a janela

**Data:** 2026-08-13. Script: `auditoria/code/r13b_ibb_ramo_infinito.py`
(saída versionada: `auditoria/code/out/r13b_ibb_ramo_infinito.txt`, 501
linhas). Executado por `.venv\Scripts\python.exe`.

**Contexto.** O corpus excluía o ramo infinito porque ξ cruza zero. O
R-12i (`docs/resultado_r12i_confronto_konnig.md` §1.6) derrubou esse
argumento: o quique de `b` é tratado e **defendido como físico** pela
fonte primária (1407.4331 §II e §VI). A saída está **REABERTA**. Surgiu
então um argumento independente candidato, de outra natureza (Könnig
2015, arXiv:1503.07436, verificado na fonte pelo autor): saúde de
Higuchi em universo em expansão exigiria **r′ > 0**, enquanto o ramo
infinito tem **r′ < 0**.

**Este documento MEDE.** Ele **não** conclui que o IBB está excluído
nem que está aprovado. O `docs/resultado_r13a_criterio_higuchi_fonte.md`
**não existia** quando esta medição começou e **passou a existir** antes
dela terminar; o confronto com o critério **da fonte** está no **§8**,
com o caveat de nível que o próprio R-13a declara e com a verificação
por CAS que ele pedia (§8.2).

---

## 0. Nível epistêmico e fronteiras declaradas

**Nível: 2a + 2b.** As três relações centrais (§4) são **fechadas**,
derivadas por álgebra explícita e verificadas numericamente a
10⁻¹⁵–10⁻¹⁶ (nível 2a). A varredura de 108 células é numérica com
fronteiras declaradas (nível 2b).

**Fronteiras de varredura (todas no enunciado, regra 1):**

| Eixo | Faixa varrida |
|---|---|
| forma-β | IBB **genuíno**: β₂ = β₃ = 0, **β₀ = 0**, β₁ = 1 (normalização) |
| β₄/β₁ | 12 valores, `f = (β₄/β₁)/y_max(μ)` ∈ linspace(0.05, 0.98) — a **faixa inteira** da janela |
| μ = M_f²/M_g² | 9 valores, logspace(−1, 1) = 0.1 … 10 — **nunca varrido antes no corpus** |
| células | **9 × 12 = 108** |
| história | a ∈ [10⁻⁴, 30], 600 pontos em N = ln a |
| conteúdo | matéria pura, ρ = ρ_m0 a⁻³ (sem radiação, sem vácuo escalar) |
| "hoje" | Ω_m(a = 1) = 0.3 (dicionário do R-8b) |
| β₀ ≠ 0 | eixo de **robustez secundário**, β₀ ∈ {0, 0.25, 0.5, 1, 2} em μ = 1, β₄ = 1 (§7) |

**Não varrido / não sondado:** radiação; vácuo escalar ou φ₋ dinâmico;
β₂ ≠ 0 ou β₃ ≠ 0 sobre o ramo infinito; a ≥ 30 (o supremo em a → ∞ é
obtido em forma fechada, §4, não por grade); acoplamento duplo da
matéria.

---

## 1. DECLARAÇÃO DE CEGUEIRA DO GATE (regra 7 — obrigatória)

> **Este teste mede Higuchi/helicidade-0 e o setor TENSORIAL. ELE NÃO
> MEDE GRADIENTE. Se o IBB passar aqui, isso não diz nada sobre `c_s²`
> lá — e vice-versa.**

Cegueiras adicionais, declaradas:

- **não mede `c_s²`** nem estabilidade de gradiente. O no-go de classe
  do R-11 (`c_s² = −1` em 108/108) foi medido no ramo **finito**; nada
  aqui o transporta para o infinito, e nada aqui o refuta lá;
- **não mede fantasma escalar** (autovalores de K₂) neste fundo;
- **não mede** validade EFT, screening, f·σ₈;
- **não mede a helicidade-0 fora do limite de de Sitter.** A cota
  `m_T² ≥ 2H²` é a cota de Higuchi **de de Sitter** — é a forma que o
  repositório usa hoje (cap. 06 §2; `resultado_ramo_finito.md` §3), e é
  a que foi medida. A forma correta em bigravidade com fundo dinâmico é
  objeto do R-13a e **não** foi calculada aqui;
- **o confronto com o critério da fonte (§8) NÃO levanta esta
  cegueira.** O R-13a §1.6 registra que a própria fonte separa três
  canais — Higuchi/helicidade-0 (§III A), tensorial/helicidade-2
  (§III C, = sinal do lapso, `ξ > 0`) e gradiente escalar (§IV) — e que
  **só os dois primeiros** entram no critério medido aqui. O terceiro
  continua não medido, e a própria fonte o classifica como **não
  fatal**.

Esta é exatamente a separação de canais que o R-12i §1.6 já havia
nomeado: 1407.4331 declara o IBB estável **no canal de gradiente**;
1503.07436 o ataca **pelo Higuchi**; são perguntas distintas. Este
documento fica **inteiramente do lado do Higuchi/tensorial**.

---

## 2. A armadilha, nomeada e demonstrada

`auditoria/code/ramo_dinamico_correto.py`, função `resolve_r()`: sem
referência devolve `rr[0]` = **menor raiz positiva**. Essa é a seleção
do ramo **finito** e é a seleção **errada** para o ramo infinito.

Demonstração na saída (célula β₀=0, β₁=1, β₂=β₃=0, β₄=1, μ=1):

| ρ̃ | raízes positivas de 𝒲(r) = ρ̃ |
|---|---|
| 10⁶ | 1.000e−6 · · · **1001.5** |
| 10³ | 9.99997e−4 · · · **33.1579** |
| 10 | 0.0972545 · · · **4.97114** |
| 1 | 0.460811 · · · **3.21432** |
| 0 | 0.652704 · · · **2.87939** |

A menor raiz é `r ~ β₁/(μρ̃) → 0` (finito); a maior é
`r ~ √(μρ̃/β₄) → ∞` (infinito). Este script usa **seleção por
continuação** (raiz mais próxima da anterior), semeada pela **assíntota
analítica** do ramo infinito no passado profundo e caminhando **para o
futuro** — a lição do R-8b (`docs/resultado_r8b_limite_mH0.md` §1;
`manuscript-v2/05_fundo_ramo_finito.md` §1, nota numérica).

---

## 3. Os gates de máquinaria (todos pré-declarados no cabeçalho do script)

### 3.1 M1 — "estou mesmo no ramo infinito?"

| Critério | Resultado |
|---|---|
| (a) r(a_min)/r(a_max) ≥ 10² | **108/108** |
| (b) dr/dN < 0 em 100% dos pontos | **108/108** |
| (c) \|r(a_min)/r_assint − 1\| ≤ 10⁻², r_assint = √(μρ̃/β₄) | **108/108** (máx. desvio 6.57e−7) |
| (d) \|r(a_max)/r_c − 1\| ≤ 5e−2, r_c = ponto fixo | **108/108** (máx. desvio 1.31e−4) |
| (e) r_c é a **maior** raiz positiva de 𝒲 = 0 | **108/108** |

Faixa de r no passado (a = 10⁻⁴): **3.68e5 … 7.42e7**. Faixa de r_c:
**0.3585 … 94.83**. O gate está satisfeito: r é grande no passado,
decresce monotonicamente e pousa no ponto fixo **superior**.

### 3.2 M2, M3 — consistência do fundo

| | medido | critério |
|---|---|---|
| max \|H²_g/H²_f − 1\| (as duas Friedmann, F.3 e F.4) | **8.88e−16** | ≤ 1e−10 |
| max resíduo da cúbica \|𝒲(r) − ρ̃\| | **1.17e−13** | ≤ 1e−12 |

Limite GR no passado, medido: `H²/(ρ/3M_g²) = 1.000001` em a = 10⁻⁴ —
o ramo infinito **também** recupera Friedmann padrão no primordial.

### 3.3 M4 — regra 6 (derivada em forma fechada + refino)

`np.gradient` está **proibido** e o script instala uma **trava**
(qualquer chamada levanta exceção). A derivada é **fechada**:

$$\frac{dr}{dN} = -\frac{3\tilde\rho}{\mathcal W'(r)},\qquad
\mathcal W'(r)=\frac{1}{\mu}\Big(2\beta_4 r+3\beta_3-\frac{\beta_1}{r^2}\Big)
-\big(3\beta_1+6\beta_2 r+3\beta_3 r^2\big)$$

(de derivar 𝒲(r(N)) = ρ̃(N) com dρ̃/dN = −3ρ̃). Cross-check por estêncil
central de **8ª ordem** em N, com r(N+jh) resolvido pela mesma rota
raiz+Newton, em **dois passos** h:

| célula | a | fechada | d8(h=1e−3) | d8(h=3e−4) | refino | canais |
|---|---|---|---|---|---|---|
| μ=1, y=1.0 | 0.01 | −3.4980371948e3 | idem | idem | 5.0e−13 | 1.3e−13 |
| μ=1, y=1.0 | 1 | −3.0192043028 | idem | idem | 9.3e−13 | 8.0e−13 |
| μ=1, y=1.9 | 0.01 | −1.8054044758e3 | idem | idem | 2.2e−13 | 4.2e−13 |
| μ=0.25, y=0.2 | 1 | −3.8929805985 | idem | idem | 5.4e−13 | 4.4e−13 |
| μ=10, y=30 | 1 | −1.0045706508 | idem | idem | 6.8e−13 | 4.6e−13 |

Critério M4: refino ≤ 1e−8 **e** canais ≤ 1e−8. **Passa em 8/8 pontos**,
com margem de cinco ordens de grandeza. *(Tabela completa: saída, seção
[M4].)*

### 3.4 M5 — controle positivo: a máquinaria reproduz o ramo finito?

Alvo: `docs/resultado_ramo_finito.md` §§1–3 (benchmark
β = (1, 1, −0.4, 0, 0.5), M_g² = M_f² = 1, m² = 1, ρ_m0 = 0.3,
a ∈ [10⁻², 10^0.3], 400 pontos).

| item | alvo do corpus | medido aqui | veredito |
|---|---|---|---|
| ξ > 0 em toda a história | sim | min(ξ) = **+6.67e−6** | OK |
| ponto fixo tardio | r_∞ ≈ 0.33 | **0.332314** | OK |
| primordial dr/dN = 3r | exato | dr/dN/(3r) = **0.999996** | OK |
| ξ/r primordial | 4 | **3.999989** | OK |
| m_T²/H² em a = 0.02 | 12.002 | **11.9996** | OK |
| Higuchi | 400/400 | **400/400** | OK |
| limite GR | 1.0000 | **1.000002** | OK |

**A máquinaria reproduz o que o repositório já sabe**, inclusive o
`ξ = 4r` e o `m_T²/H² → 12` — e agora com dr/dN em forma fechada, não
por `np.gradient` como no script original.

### 3.5 M6 — poder do gate (regra 3) — **com emenda declarada**

Caso sabidamente falso: o fundo da D8 / `derivations/02` §3.4
(r = 1.2, ξ = 3.497, β₂ = −0.4), onde `m_T² < 0`. O gate **reprova**.
Fator estrutural medido: **−0.8788**, contra o −0.88 declarado. OK.

> **EMENDA DECLARADA (a 1ª execução REPROVOU o item numérico; a rodada
> ruim está preservada, regra 2).** O critério original exigia
> `m_T² = −3.19 ± 0.05`. Medimos **−1.5944** — exatamente **metade**.
> Causa localizada e demonstrada no próprio script: `derivations/02`
> §3.4 avaliou o número com **M_eff² = 1**, enquanto
> `ramo_dinamico_correto.py` (e este script) usam
> `M_eff² = 1/(1/M_g² + 1/M_f²) = 0.5` para M_g² = M_f² = 1. Razão
> medida: **2.000000**. É uma **inconsistência de normalização entre
> dois documentos do corpus**, não erro de física — o fator estrutural
> e o sinal batem, e `m_T²/H²` (a única quantidade interpretada neste
> documento) é **invariante** por M_eff² e por m². Verificado: ao
> reescalar m² por 7 e M_g², M_f² por 3 com μ fixo, a razão muda em
> **0.000e+00**. Critério M6 emendado para: (a) m_T² < 0; (b) fator
> = −0.88 ± 0.005; (c) −3.19 ± 0.05 **se** M_eff² = 1 — os três passam.
> *Item de housekeeping registrado: `derivations/02` §3.4 e
> `manuscript-v2/06` §4 citam um número com normalização diferente da
> do script de fundo.*

### 3.6 M7 — fronteira de existência, e o primeiro achado do eixo μ

Com β₀ = β₂ = β₃ = 0 o ponto fixo tardio resolve
`y r³ − 3μ r² + 1 = 0` (y ≡ β₄/β₁). O mínimo local está em r = 2μ/y e
vale `1 − 4μ³/y²`; duas raízes positivas existem **⟺ y < 2μ^{3/2}**.
Confrontado com bissecção numérica em 7 valores de μ: diferença
**≤ 5.0e−14**.

> **ACHADO (varredura em μ).** A janela IBB **não é** `0 < β₄ < 2β₁` em
> geral — ela é
> $$\boxed{\;0<\frac{\beta_4}{\beta_1}<2\,\mu^{3/2},\qquad \mu=\frac{M_f^2}{M_g^2}\;}$$
> O intervalo da fonte é o **caso particular μ = 1** (verificado:
> y_max(1) = 2.0000000000). *Nível 2a.*

---

## 4. As três relações fechadas (o núcleo do resultado)

Derivadas neste script e verificadas numericamente em todas as 108
células.

**(F-1) O valor de m_T²/H² no ponto fixo tardio.** Com β₀=β₂=β₃=0 e
𝒲(r_c)=0 vale `β₄r_c³ + β₁ = 3μβ₁r_c²`; substituindo na caixa do
cap. 06:

$$\boxed{\;\frac{m_T^2}{H^2}\Big|_{r=r_c}=1+\frac{1}{\mu r_c^{2}}\;}$$

E a fronteira de existência dá `r_c > 2μ/y > μ^{−1/2}`, isto é
**μr_c² > 1 em toda a janela IBB**. Logo

$$\boxed{\;1<\frac{m_T^2}{H^2}\Big|_{\rm ponto\ fixo}<2\quad\text{(estrito, sempre)}\;}$$

com o supremo 2 atingido **só** no limite y → 2μ^{3/2}, onde o ponto
fixo degenera em raiz dupla e o ramo deixa de existir. Verificação:
max \|razão(a=30) − (1+1/(μr_c²))\| = **5.59e−4**; min(μr_c²) =
**1.284908** (> 1); max da razão no ponto fixo = **1.778266** (< 2).

**(F-2) O locus de ξ = 0, fechado.** `ξ = 0 ⟺ r𝒲′(r) = 3𝒲(r)`, o que
com β₀=β₂=β₃=0 dá

$$\boxed{\;\beta_4 r^3-6\mu\beta_1 r^2+4\beta_1=0\;}$$

(compare com o ponto fixo, `β₄r³ − 3μβ₁r² + β₁ = 0`). Confrontado com
o cruzamento medido por bissecção nas 108 células: **máx. \|dif rel\| =
1.78e−15**.

**(F-3) μ é PURA REESCALA no IBB genuíno.** A tabela da varredura
mostra degenerescência **exata** em μ a `f = y/y_max` fixo. A causa é
fechada: pondo

$$r=\mu^{-1/2}u,\qquad \frac{\beta_4}{\beta_1}=2\mu^{3/2}f,\qquad
\hat\rho=\mu^{1/2}\tilde\rho$$

a cúbica vira `2f u³ − 3u² − ρ̂ u + 1 = 0`, e

$$\Omega_m=1-\frac{3u^2}{2fu^3+1},\qquad
\frac{m_T^2}{H^2}=\frac{3\,(u^2+\chi/u)}{2fu^3+1},\quad \chi=u+\frac{du}{dN}$$

— **funções só de (f, ρ̂)**. Verificação numérica: as histórias de
m_T²/H² a f fixo, com μ variando por duas ordens de grandeza,
coincidem em **≤ 4.0e−15**.

> **Consequência metodológica.** A varredura em μ — a lacuna que o
> parecer de astrofísica identificou como decisiva — **fecha** o
> enunciado em vez de abri-lo: neste bloco de células μ não é um eixo
> físico novo, ele apenas reescala r e a largura da janela de β₄.
> *Nível 2a.*

---

## 5. O que foi medido — a varredura de 108 células

### 5.1 Resumo de classe

| | medido |
|---|---|
| **R1** — r′ < 0 em 100% da história | **108/108 células** |
| max(r′) sobre **todos** os pontos de **todas** as células | **−6.0501e−5** (negativo ⟹ r′ < 0 sempre) |
| **R2** — ξ cruza zero | **108/108 células**, exatamente **1 cruzamento** cada |
| a do cruzamento | **0.6740 … 0.7130** (z = 0.403 … 0.484) |
| **R3** — m_T²/H² no ponto fixo tardio | **1.001112 … 1.778266** |
| m_T²/H² máximo na grade | 1.001089 … 1.777707 |
| m_T²/H² monótona crescente em N | **108/108** ⟹ o supremo sobre a história **inteira** (a → ∞) é o valor no ponto fixo |
| **R4** — Higuchi `m_T² ≥ 2H²`, por ponto | **0 / 64 800** |
| células com Higuchi em 100% da história | **0/108** |
| células com Higuchi em 0% da história | **108/108** |
| **R5** — m_T² > 0 em 100% da história | **108/108 células** |

### 5.2 Tabela por célula (fatia μ = 1 — a faixa inteira de β₄/β₁ da fonte)

*Fonte: `auditoria/code/out/r13b_ibb_ramo_infinito.txt`, seção
[R1..R5], linhas 232–243.*

| β₄/β₁ | f | r_c | r(a=10⁻⁴) | r′<0 | max r′ | a(ξ=0) | m_T²/H² @a=1 | máx | @ponto fixo | Higuchi | m_T²>0 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.100 | 0.05 | 29.989 | 2.35e7 | 100% | −2.04e−3 | 0.6740 | 0.6954 | 1.0011 | 1.0011 | 0/600 | 600/600 |
| 0.269 | 0.135 | 11.119 | 8.72e6 | 100% | −7.64e−4 | 0.6745 | 0.6961 | 1.0081 | 1.0081 | 0/600 | 600/600 |
| 0.438 | 0.219 | 6.797 | 5.35e6 | 100% | −4.75e−4 | 0.6754 | 0.6975 | 1.0216 | 1.0216 | 0/600 | 600/600 |
| 0.607 | 0.304 | 4.871 | 3.86e6 | 100% | −3.49e−4 | 0.6768 | 0.6994 | 1.0421 | 1.0422 | 0/600 | 600/600 |
| 0.776 | 0.388 | 3.774 | 3.01e6 | 100% | −2.81e−4 | 0.6787 | 0.7019 | 1.0702 | 1.0702 | 0/600 | 600/600 |
| 0.946 | 0.473 | 3.060 | 2.47e6 | 100% | −2.39e−4 | 0.6811 | 0.7050 | 1.1067 | 1.1068 | 0/600 | 600/600 |
| 1.115 | 0.557 | 2.554 | 2.09e6 | 100% | −2.13e−4 | 0.6841 | 0.7085 | 1.1532 | 1.1533 | 0/600 | 600/600 |
| 1.284 | 0.642 | 2.172 | 1.81e6 | 100% | −1.97e−4 | 0.6878 | 0.7123 | 1.2119 | 1.2120 | 0/600 | 600/600 |
| 1.453 | 0.726 | 1.868 | 1.59e6 | 100% | −1.91e−4 | 0.6924 | 0.7164 | 1.2866 | 1.2867 | 0/600 | 600/600 |
| 1.622 | 0.811 | 1.613 | 1.42e6 | 100% | −1.97e−4 | 0.6979 | 0.7206 | 1.3844 | 1.3845 | 0/600 | 600/600 |
| 1.791 | 0.895 | 1.383 | 1.28e6 | 100% | −2.28e−4 | 0.7046 | 0.7245 | 1.5224 | 1.5226 | 0/600 | 600/600 |
| 1.960 | 0.980 | 1.134 | 1.16e6 | 100% | −4.43e−4 | 0.7130 | 0.7279 | 1.7777 | 1.7783 | 0/600 | 600/600 |

As outras 8 fatias de μ reproduzem estas colunas **dígito a dígito** a f
fixo — é o corolário (F-3).

### 5.3 Uma história completa (μ = 1, β₄/β₁ = 0.9455, r_c = 3.0601)

*Fonte: saída, seção [HISTORIA DETALHADA].*

| a | z | r | r′ | ξ | H² | m_T² | m_T²/H² | Hig |
|---|---|---|---|---|---|---|---|---|
| 1.0e−4 | 9999 | 2.468e6 | −3.703e6 | −1.234e6 | 9.60e11 | 1.234e6 | 0.00000 | NÃO |
| 9.9e−4 | 1007 | 7.896e4 | −1.184e5 | −3.948e4 | 9.82e8 | 3.948e4 | 0.00004 | NÃO |
| 1.0e−2 | 98.4 | 2448.8 | −3670.8 | −1222.0 | 9.45e5 | 1224.4 | 0.00130 | NÃO |
| 0.0998 | 9.02 | 79.885 | −117.40 | −37.515 | 1005.6 | 39.940 | 0.03972 | NÃO |
| 0.2983 | 2.35 | 16.819 | −22.609 | −5.7906 | 44.583 | 8.3991 | 0.18839 | NÃO |
| 0.5049 | 0.980 | 8.6380 | −10.078 | −1.4399 | 11.777 | 4.3093 | 0.36592 | NÃO |
| **0.6811** | **0.468** | — | — | **0** | — | — | — | NÃO |
| 0.9904 | 0.010 | 4.5112 | −3.2450 | +1.2661 | 3.2437 | 2.2867 | 0.70496 | NÃO |
| 1.984 | −0.496 | 3.3122 | −0.6975 | +2.6147 | 1.7790 | 1.7752 | 0.99790 | NÃO |
| 5.011 | −0.800 | 3.0771 | −0.0506 | +3.0265 | 1.5462 | 1.6984 | 1.09843 | NÃO |
| 30 | −0.967 | 3.0602 | −2.39e−4 | +3.0600 | 1.5301 | 1.6935 | 1.10675 | NÃO |

A estrutura é a do IBB da fonte: r desce de ~10⁶ para r_c; ξ é
**negativo** no passado (ξ → −r/2 quando r ~ a^{−3/2}), **quica uma
vez** em a ≈ 0.68, e assenta em ξ → r_c > 0. A razão m_T²/H² sobe
monotonicamente de ~0 até 1+1/(μr_c²) e **nunca alcança 2**.

---

## 6. Os enunciados de classe

> **(E1) SINAL DE r′.** Na classe IBB genuína (β₀ = β₂ = β₃ = 0,
> β₁ > 0, 0 < β₄/β₁ < 2μ^{3/2}), o ramo infinito tem **r′ < 0 em toda a
> história, em 108/108 células**, com max(r′) = −6.05e−5 sobre a
> varredura inteira. Isto **confirma numericamente**, nas convenções do
> projeto, a caracterização que 1503.07436 usa para definir o ramo.
> *Nível 2b, fronteiras em §0.* Em forma fechada: `dr/dN = −3ρ̃/𝒲′(r)`
> com ρ̃ > 0 e 𝒲′ > 0 em todo o ramo infinito (§4). *Nível 2a.*

> **(E2) ZERO DO LAPSO.** ξ cruza zero **exatamente uma vez** em
> 108/108 células, em a = 0.674 … 0.713 (z = 0.40 … 0.48), com locus em
> forma fechada `β₄r³ − 6μβ₁r² + 4β₁ = 0`. É **um quique**, não uma
> sequência de singularidades — a mesma estrutura que a fonte primária
> descreve e defende (R-12i §1.6). *Nível 2a + 2b.*

> **(E3) SETOR TENSORIAL — m_T² > 0.** m_T² é **positivo em 100% da
> história em 108/108 células**. Não há taquiônico/ghost tensorial no
> ramo infinito nesta classe — nem sequer na travessia de ξ = 0. Isto
> **contrasta** com o fundo da D8 (m_T² < 0 por construção) e com a
> preocupação herdada do corpus. *Nível 2b.*

> **(E4) A INEQUAÇÃO DO REPOSITÓRIO.** Contra a cota que o repositório
> usa hoje, `m_T² ≥ 2H²`: **0 de 64 800 pontos** a satisfazem;
> **0/108 células** a satisfazem em qualquer época. E o enunciado é
> **fechado**, não amostral: o supremo de m_T²/H² sobre a história
> inteira é `1 + 1/(μr_c²)`, e `μr_c² > 1` em **toda** a janela de
> existência, logo
> $$1<\sup_{\rm história}\frac{m_T^2}{H^2}<2$$
> em todo o bloco IBB genuíno, para **todo** μ. *Nível 2a (fechado) +
> 2b (verificado em 108 células).*

*(O quinto enunciado, **(E5)** — o critério **da fonte** medido nas
mesmas 108 células — está no §8.5, porque depende do R-13a.)*

**Contraste com o ramo finito, medido na mesma rodada e com a mesma
máquinaria:** lá m_T²/H² → **12** no primordial e Higuchi passa
**400/400**. Aqui o máximo é **1.78** e Higuchi passa **0/64 800**. A
razão estrutural está visível nas fórmulas: no ramo finito o termo
`ξ/(M_f²r³)` **explode** (ξ = 4r, r → 0); no ramo infinito ele é
subdominante e a razão fica ancorada perto de 1.

---

## 7. Eixo de robustez em β₀ (secundário, fora do IBB genuíno)

O IBB da fonte tem β₀ = 0 (sem constante cosmológica explícita para g).
Ligar β₀ **não** muda os dois enunciados de sinal:

| β₀ | r_c | r′<0 | a(ξ=0) | m_T²/H² @a=1 | máx | Higuchi |
|---|---|---|---|---|---|---|
| 0 | 2.8794 | 100% | 0.6780 | 0.7060 | 1.1206 | 0/600 |
| 0.25 | 2.9708 | 100% | 0.6780 | 0.6926 | 1.0829 | 0/600 |
| 0.5 | 3.0565 | 100% | 0.6639 | 0.6801 | 1.0498 | 0/600 |
| 1 | 3.2143 | 100% | 0.6639 | 0.6576 | 0.9937 | 0/600 |
| 2 | 3.4909 | 100% | 0.6639 | 0.6198 | 0.9085 | 0/600 |

(μ = 1, β₄ = 1.) Ligar β₀ **piora** a razão em vez de melhorá-la.
*Nível 2b; 5 pontos, uma fatia — declarado como amostragem, não
varredura.* *Nota de resolução: nesta tabela secundária o a(ξ=0) é o
ponto de grade da troca de sinal (resolução ≈ 2% em a), não o valor
bissectado; os a(ξ=0) do §5.1–5.2 são bissectados.*

---

## 8. Confronto com o critério da fonte — o R-13a **existe**

`docs/resultado_r13a_criterio_higuchi_fonte.md` **não existia** quando
esta medição começou e **passou a existir** antes dela terminar (o
script detecta o arquivo e imprime o status na saída). Ele é **citado**,
não adotado como instrução.

**Caveat de nível, declarado pelo próprio R-13a (§5):** a tradução ali é
**álgebra à mão, não verificada por CAS**. Tudo nesta seção é
condicional a ela — com a exceção verificada abaixo.

### 8.1 O que o R-13a entrega

Nas nossas variáveis (R-13a §2.2 e §3.1): a condição de Higuchi de
Könnig (eq. 14) **não** é uma inequação de massa na fonte; traduzida,
ela é a caixa do cap. 06 **com ξ substituído por r**:

$$m_T^2\big|_{\xi\to r}=\frac{m^2M_{\rm ef}^2}{M_f^2}\,\mathcal B(r)\,\frac{1+\mu r^2}{r}\;\ge\;2H^2,
\qquad \mathcal B(r)=\beta_1+2\beta_2 r+\beta_3 r^2$$

e é equivalente a `r′ ≥ 0` (eq. 18) ⟺ `ξ ≥ r`.

### 8.2 O que **este** script acrescenta: a verificação por CAS

O R-13a lista como **item 1 da sua fila** e única fronteira epistêmica
real "passar tudo isso por sympy". Este script o faz, por **rota
independente** — partindo da nossa própria 𝒲(r) e da nossa forma
fechada `dr/dN = −3ρ̃/𝒲′(r)`, não da álgebra deles:

| verificação simbólica (sympy, β_n e μ **gerais**, poeira) | resíduo |
|---|---|
| (i) `−μr²𝒲′(r)` == LHS da (15) traduzida ⟹ `r′ ≥ 0 ⟺ (15)` | **0** |
| (ii) caixa do cap. 06 com ξ→r == caixa do R-13a §2.2 | **0** |
| (iii) `(m_T²\|_{ξ→r} − 2H²)·3M_f²r/(m²M_ef²)` == LHS da (15) | **0** |

> **A cadeia `Könnig(14) ⟺ Könnig(15) ⟺ 𝒲′(r) ≤ 0 ⟺ r′ ≥ 0` é EXATA
> nas convenções deste projeto, para β_n e μ gerais, com matéria de
> poeira.** *Nível 1 (duas rotas independentes: a álgebra à mão do
> R-13a e a rota 𝒲(r) deste script, ambas fechando em resíduo zero).*

*Nota de rodada, preservada:* a 1ª versão do teste (iii) usou o fator
`r²` em vez de `r` e **reprovou**, com resíduo `(r−1)·LHS(15)`. O erro
era do fator deste script, **não** da tradução do R-13a. Registrado na
saída, não escondido (regra 2).

### 8.3 Poder do teste de concordância (regra 3)

No ramo infinito os dois lados da equivalência são **falsos** em todo
ponto — logo "64 800/64 800 de concordância" seria trivial sozinho. O
teste só tem poder se houver um caso **verdadeiro**. O controle
positivo (ramo finito, r′ = 3r > 0) o fornece:

| | ramo finito (controle) | ramo infinito (108 células) |
|---|---|---|
| `r′ ≥ 0` | **400/400** | **0/64 800** |
| Higuchi da fonte, `m_T²\|_{ξ→r} ≥ 2H²` | **400/400** | **0/64 800** |
| concordância entre as duas formas | **400/400** | **64 800/64 800** |

**O teste aprova o ramo finito e reprova o infinito, pelas duas formas
equivalentes.** Tem poder.

### 8.4 Confirmação numérica de uma previsão que o R-13a não verificou

O R-13a §3.2 afirma, como "consequência algébrica direta … **não
re-verificada numericamente**", que no ramo finito primordial o objeto
de Könnig dá **3** onde o nosso `m_T²/H²` dá **12**. Medido aqui:

| | medido |
|---|---|
| `m_T²/H²` (ξ dinâmico, caixa do cap. 06) | **12.0000** |
| `m_T²\|_{ξ→r}/H²` (objeto de Könnig) | **3.000002** |

**Confirmado.** *Nível 2a.*

### 8.5 A medida no ramo infinito

`m_T²|_{ξ→r}/H² = 3ℬ(r)(1+μr²)/(r³V_f(r))` — com β₂=β₃=0, isso é
`3β₁(1+μr²)/(β₄r³+β₁)`. Amostra (tabela completa na saída):

| μ | β₄/β₁ | @a=1 | máx | @ponto fixo | Higuchi(fonte) | r′≥0 |
|---|---|---|---|---|---|---|
| 0.1 | 0.003162 | 0.69571 | 1.00109 | 1.00111 | 0/600 | 0/600 |
| 0.178 | 0.08358 | 0.74332 | 1.15325 | 1.15329 | 0/600 | 0/600 |
| 1 | 1.115 | 0.74332 | 1.15325 | 1.15329 | 0/600 | 0/600 |
| 3.16 | 9.12 | 0.80107 | 1.38443 | 1.38450 | 0/600 | 0/600 |
| 10 | 19.2 | 0.70925 | 1.04213 | 1.04215 | 0/600 | 0/600 |

**As duas razões coincidem no ponto fixo** (onde ξ = r, logo
`m_T² = m_T²|_{ξ→r}`) e divergem fora dele; o supremo das duas é o
mesmo `1 + 1/(μr_c²) < 2`.

> **(E5) O critério da fonte, traduzido pelo R-13a e medido aqui, é
> REPROVADO em 0/64 800 pontos das 108 células IBB genuínas — pelas
> duas formas equivalentes, que concordam ponto a ponto.** *Nível 2b,
> condicional ao mapa de convenções do R-13a §2.1 (que é entrada, não
> saída, deste script).*

### 8.6 O que continua PENDENTE, e o que este documento NÃO conclui

- **O mapa de convenções do R-13a §2.1** (`r_K = √μ r`,
  `β_n^K = A μ^{−n/2} β_n`) é **entrada** deste script, não saída.
  Não foi reverificado aqui. O que ficou verificado por CAS é a cadeia
  **interna** (14)⟺(15)⟺(18) nas nossas variáveis, **dado** esse mapa.
- **A leitura interpretativa do R-13a §3.2** — de que a forma "massa"
  do bound de FLRW é o bound de de Sitter avaliado no fundo
  proporcional instantâneo — é inferência declarada lá e **não é
  testada aqui**.
- **Fasiello–Tolley 1308.1647**, fonte primária real do bound, continua
  não aberta (fronteira declarada pelo próprio R-13a §5).
- **A modulação β_n(φ₋)**: com β_n dependentes do tempo, o R-13a §2.2
  hipótese 2 avisa que a cadeia (14)→(16)→(18) **não sobrevive
  intacta**. Toda esta seção vale para **β_n constantes**.

**Este documento não conclui que o IBB está excluído nem que está
aprovado.** O que ele estabelece é: (i) a máquinaria mede o ramo
infinito de forma auditada (M1–M7, controle positivo incluído);
(ii) `r′ < 0` é fato de classe nas convenções do projeto;
(iii) o zero de ξ é um quique único, com locus fechado; (iv) o bloco
IBB genuíno inteiro fica em `1 < m_T²/H² < 2` contra a inequação que o
repositório usa hoje; (v) o critério da fonte, na tradução do R-13a, é
reprovado em todos os pontos, e essa tradução ficou verificada por CAS
na sua cadeia interna. **O passo que falta para um veredito não é mais
o critério — é o canal cego (§1).**

**Fila aberta por este documento:**

1. **`c_s²` no ramo infinito.** Este gate é **cego** a ele (§1). O
   no-go de classe do R-11 (`c_s² = −1`) vale no ramo **finito**; a
   fonte declara o IBB **estável no gradiente** (R-13a §1.5: 1503.07436
   **confirma** o resultado de 1407.4331 e mata o IBB por outro canal).
   Medir `c_s²` **lá**, com a máquinaria limpa do R-12, é o teste que
   fecha o arco — e ele não está feito.
2. **O mapa de convenções do R-13a §2.1 por CAS** (§8.6).
3. A cota de Higuchi **em fundo dinâmico bimétrico**, derivada — não
   herdada de de Sitter nem da forma ξ→r.
4. Housekeeping: a normalização de M_eff² em `derivations/02` §3.4 e
   `manuscript-v2/06` §4 (§3.5).
5. β₂ ≠ 0 / β₃ ≠ 0 sobre o ramo infinito (fora da célula IBB genuína);
   radiação (`1 + w_tot > 0` continua válido, mas a cúbica muda).
6. O observável `w_mg ≤ −1` do R-13a §4.3, que este script não mediu.

---

## 9. Rastreabilidade

| Afirmação | Fonte |
|---|---|
| cúbica, duas famílias de raiz, seleção por continuação | `docs/resultado_ramo_finito.md` §2; `manuscript-v2/05_fundo_ramo_finito.md` §1; `docs/resultado_r8b_limite_mH0.md` §1 |
| caixa de m_T² | `manuscript-v2/06_setor_tensorial.md` §1; `derivations/02_setor_tensorial_mT2.md` §3.3 |
| F.3 / F.4 (as duas Friedmann) | `derivations/plano_derivacoes.md` §0 |
| reabertura da saída, IBB, `0 < β₄ < 2β₁` | `docs/resultado_r12i_confronto_konnig.md` §1.6 |
| regra 6 (forma fechada / 8ª ordem / `np.gradient` proibido) | `manuscript-v2/02_metodo.md` §1 r.6; `docs/resultado_r12_instrumento_e_cs2.md` §2 |
| regra 7 (cegueira do gate) | `manuscript-v2/02_metodo.md` §1 r.7 |
| alvos do controle positivo | `docs/resultado_ramo_finito.md` §§1–3 |
| caso falso do teste de poder | `derivations/02_setor_tensorial_mT2.md` §3.4 |
| dicionário Ω_m(a₀) = 0.3 | `docs/resultado_r8b_limite_mH0.md` §1 |
| tradução do critério da fonte (§8), caveat de nível, "3" do §8.4, separação de canais | `docs/resultado_r13a_criterio_higuchi_fonte.md` §§1.5–1.6, 2.1–2.3, 3.1–3.3, 5 |
| **todos os números deste documento** | `auditoria/code/out/r13b_ibb_ramo_infinito.txt` (script `auditoria/code/r13b_ibb_ramo_infinito.py`) |
