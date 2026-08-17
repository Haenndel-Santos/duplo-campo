# 06 — Setor tensorial

**Porte de `derivations/02_setor_tensorial_mT2.md` (Derivação 2:
ação TT do zero, Γ–Γ + potencial HR a O(h²) + setor de φ₋ via √−g —
obrigatório: sem ele o gráviton ganharia massa espúria até em GR) e
de `docs/resultado_ramo_finito.md` §3–4. Scripts:
`derivations/code/02_setor_tensorial_mT2.py`,
`auditoria/code/ramo_dinamico_correto.py`.**

## 1. A ação TT correta (decide três formas incompatíveis da v1)

A v1 declarava três formas mutuamente incompatíveis do setor
tensorial (Cap.16 §16.2, §16.4; Anexo D §D.3/§D.5). A derivação
fechou:

**Cinéticos e propagação:**

$$K_{hh} = \frac{M_g^2 a^3}{4},\qquad
K_{\ell\ell} = \frac{M_f^2 b^3}{4\xi},\qquad
c_g^2 = 1,\qquad \boxed{c_f^2 = \frac{\xi^2}{r^2}}$$

— o modo do setor f propaga no cone causal de f (o Anexo D §D.3
estava certo; o Cap.16 §16.2, sem ξ, errado).

**Estrutura de massa:** com o fundo on-shell, a matriz de massa é
exatamente ∝ (h−ℓ)² (modo sem massa existe, det M = 0), e a massa
física:

$$\boxed{\,m_T^2 = m^2 M_{\rm eff}^2
\left(\frac{1}{M_g^2}+\frac{\xi}{M_f^2\,r^3}\right)
r\,\big[\beta_1+\beta_2(\xi+r)+\beta_3\,\xi r\big]\,}$$

(na forma v2, a modulação está absorvida nos β_n(φ₋); a fórmula
original carrega o fator F̄ da época). **Depende de ξ** — a forma do
Cap.16 só é recuperada no caso especial ξ = r; e o prefator soma os
dois setores (não é M_eff²/M_g²). Diagonalização exata exige a nota:
cinéticos dependem do tempo (condição adiabática) e c_g² ≠ c_f² não é
simultaneamente diagonalizável com a massa — a "diagonalização" do
Cap.16 §16.3 era aproximada. *Nível 2a (simbólico com auto-testes).*

## 2. m_T²/H² → 12 no primordial — universal

No ramo finito, com r → 0 e ξ = 4r (cap. 05), o termo dominante de
m_T² e a Friedmann do setor f dão

$$m_T^2 \simeq \frac{4m^2M_{\rm eff}^2\beta_1}{M_f^2\,r},\qquad
H^2 \to \frac{m^2M_{\rm eff}^2\beta_1}{3M_f^2\,r}
\;\;\Longrightarrow\;\;
\boxed{\frac{m_T^2}{H^2} \to 12}$$

**Todos os parâmetros cancelam** (M_f², M_eff², m², β₁). Verificação
numérica: 12.002 em a = 0.02 (`ramo_dinamico_correto.py`), e 11.9996 na
remedição por máquinaria independente do R-13b (§3.4, controle
positivo). *Nível 2a (estrutural) + 2b (verificação).*
*Fonte: resultado_ramo_finito §3; R-13b §3.4.*

### 2.1 O que o 12 **não** é: a margem de Higuchi é 1.5, não 6

O `12` é a razão do **objeto tensorial deste projeto** — a massa m_T²
da caixa do §1, com **ξ dinâmico**. O bound de Higuchi em FLRW **não é
essa caixa**. A leitura anterior — "Higuchi satisfeito com margem de
fator 6", de 12/2 = 6 — **cai**: ela dividia o nosso objeto por uma
cota escrita para outro.

O critério da fonte (Könnig 2015, arXiv:1503.07436 eq. 14; fonte
primária Fasiello–Tolley 1308.1647) não contém massa nenhuma — é um
funcional de `r` e dos β_n. Traduzido para as nossas variáveis, para μ
= M_f²/M_g² e β_n gerais, ele é **a caixa do §1 com ξ substituído por
r**:

$$m_T^2\big|_{\xi\to r}
=\frac{m^2M_{\rm eff}^2}{M_f^2}\,\mathcal B(r)\,\frac{1+\mu r^2}{r}
\;\ge\;2H^2,\qquad
\mathcal B(r)=\beta_1+2\beta_2 r+\beta_3 r^2$$

e é **equivalente a r′ ≥ 0**, isto é, a **ξ ≥ r**. No primordial do
ramo finito esse funcional vale **3**, não 12:

| objeto, primordial do ramo finito | valor |
|---|---|
| `m_T²/H²` — nosso, ξ dinâmico | **12.0000** |
| `m_T²\|_{ξ→r}/H²` — funcional de Higuchi FLRW | **3.000002** |

> **The project tensor-mass ratio approaches `m_T²/H² → 12`, while the
> corresponding FLRW Higuchi functional approaches `3`, satisfying the
> bound `2` with a factor-1.5 margin.**

**Por que os dois números diferem.** São **objetos distintos** avaliados
no mesmo fundo. O nosso carrega ξ dinâmico; o da fonte é avaliado em
ξ → r. A razão entre eles é o produto de dois fatores,

$$\frac{m_T^2}{m_T^2|_{\xi\to r}}
=\underbrace{\frac{\mu r^3+\xi}{\mu r^3+r}}_{\text{cinético}}\cdot
\underbrace{\frac{\beta_1+\beta_2(\xi+r)+\beta_3\xi r}
{\beta_1+2\beta_2r+\beta_3r^2}}_{\text{massa}}$$

e no primordial (r → 0, ξ = 4r) o segundo tende a 1 e o primeiro a
ξ/r = 4 — daí **12 = 4 × 3**, exatamente. **Os dois coincidem quando
ξ = r** (⟺ r′ = 0 ⟺ fundo proporcional, ponto fixo): ali a caixa do §1
e o bound da fonte são a **mesma** inequação, termo a termo, para μ
arbitrário e todos os β_n. É uma validação cruzada — duas maquinarias
independentes (ação TT + Sylvester de um lado; eq. 14 da fonte do
outro) reencontram o mesmo objeto no limite em que devem.

**O que sobrevive e o que cai.** Sobrevive `m_T²/H² → 12`: é enunciado
sobre o **nosso** objeto e foi reproduzido por rota independente
(11.9996, R-13b §3.4). Sobrevive o veredito: o ramo finito **satisfaz**
o bound — 3 > 2, e pelo critério equivalente `r′ ≥ 0`, que o ramo
finito tem por construção (r′ = 3r > 0 no primordial, cap. 05). Cai
**só a margem**: de 6× para **1.5×**. *Nível 2a (a identidade ξ → r,
verificada por CAS em duas rotas independentes — R-13b §8.2, resíduo
zero para β_n e μ gerais) + 2b (o 3.000002 medido).*
*Fonte: `docs/resultado_r13a_criterio_higuchi_fonte.md` §§2.2, 3.1–3.2;
`docs/resultado_r13b_ibb_ramo_infinito.md` §§8.2–8.4.*

## 3. A razão hoje — com a época e o fundo declarados

A razão m_T²/H² é função da época e do fundo; citar sem âncora gera
falsa contradição:

| Fundo / época | m_T²/H² | Fonte |
|---|---|---|
| Primordial (universal) | → 12 | resultado_ramo_finito §3 |
| Λ profundo (benchmark β-const) | ≈ 12 (m_T/H ≈ 3.5) | gate F-b/R-7a (tag de escala) |
| "Hoje" do ramo finito original (Ω_m ≈ 0.25) | ≈ 4 | resultado_ramo_finito §3 |
| a₀ da família R-8b (Ω_m = 0.3), pela fórmula em caixa | 5.1–5.8 (m_T/H₀ = 2.26–2.41) | resultado_r8b §2 |

**Atenção ao objeto (§2.1):** todos os valores da tabela são do
**nosso** m_T²/H², com ξ dinâmico — não do funcional de Higuchi FLRW,
que é a mesma expressão com ξ → r. Quem responde ao bound é o segundo.
No ramo finito os dois vereditos coincidem: no benchmark, o funcional
da fonte passa em **400/400 pontos**, e o critério equivalente `r′ ≥ 0`
também, ponto a ponto (R-13b §8.3). **O que a correção muda é a
margem, não o veredito.** E o resultado estrutural do R-8b (cap. 09):
dentro da família do benchmark com a história de expansão fixa, m_T/H₀
é **cravado** ≈ 2.3 — predição, não parâmetro.

## 4. A invalidação da D8 — estudo de caso do método

A âncora D8 da auditoria concluiu Higuchi violado em 60/60 pontos —
"o resultado mais preocupante da auditoria". O scan impunha
ξ = H_g/H_f, que não satisfaz a constraint correta (no ramo certo,
H_g/H_f = r; cap. 04): com r=1.2, ξ=3.497, o fator estrutural
β₁+β₂(ξ+r) = −0.88 < 0 forçava m_T² < 0 **por construção**. No fundo
correto o mesmo fator vale +0.72 hoje. Fundo errado ⟹ resultado
errado por construção — o mesmo padrão do Erratum-02, três escalas
menor (cap. 02). O achado documental da D8 (a faixa 30–300 H₀ é
design observacional, não dinâmica) permaneceu — e o R-8b o elevou a
obstrução estrutural (cap. 09 §2). *Fonte: resultado_ramo_finito §4.*
