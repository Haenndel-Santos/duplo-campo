# 03 — A ação e o dicionário

**Porte de `docs/acao_v2.md` (Passo 1, Gate 1 fechado em nível 1;
verificação mecanizada em `auditoria/code/gate1_acao.py`). Notação
vinculada a `docs/dicionario_simbolos.md` — o dicionário é contrato:
nenhum símbolo com dois significados no corpus v2 (Gate 0
automatizado).**

## 0. O achado que determina o desenho

Na v1, a modulação estrutural era um fator global F(φ) multiplicando
todo o potencial HR. Mas o ramo algébrico fixa r na raiz de
ℬ(r) = β₁ + 2β₂r + β₃r² = 0, que na família F1 (β₃=0) dá
r★ = −β₁/(2β₂). Sob modulação global, β_n → Fβ_n:

$$r_\star \to -\frac{F\beta_1}{2F\beta_2} = r_\star$$

**O fator global cancela na razão; a raiz não se move.** O mecanismo
da v1 era estruturalmente incapaz de mover a estrutura — não por erro
de conta, mas por degenerescência da forma escolhida. Consequência de
desenho: a modulação precisa ser **diferencial** (ao menos uma razão
β_i/β_j dependente do campo); um F global é absorvível e a v2 o
elimina, trabalhando com β_n(φ₋) direto. *Nível 1 (álgebra de duas
linhas, mecanizada — critério (g) do Gate 1).*

## 1. A ação

$$
\begin{aligned}
S \;=\; & \frac{M_g^2}{2}\int d^4x\,\sqrt{-g}\,R[g]
\;+\; \frac{M_f^2}{2}\int d^4x\,\sqrt{-f}\,R[f] \\
& -\; m^2 M_{\rm eff}^2 \int d^4x\,\sqrt{-g}\,
      \sum_{n=0}^{4}\beta_n(\phi_-)\,e_n(\mathcal K) \\
& +\; \int d^4x\,\sqrt{-g}\left[
      -\tfrac12 (\partial\phi_+)^2
      -\tfrac12 (\partial\phi_-)^2
      - V(\phi_+,\phi_-)\right]
\;+\; S_m[g,\psi]
\end{aligned}
$$

com 𝒦 = √(g⁻¹f), M_eff⁻² = M_g⁻² + M_f⁻², φ± = (φ₁±φ₂)/√2, e matéria
acoplada **só a g** (exigência da contagem sem fantasma BD; cap. 04).

**Potencial primordial** (fecha o achado A7 da auditoria — a v1 nunca
o especificou):

$$V(\phi_+,\phi_-) = V_+(\phi_+) - \tfrac12\mu_-^2\phi_-^2
+ \tfrac14\lambda_-\phi_-^4 + \lambda_c\,\phi_+^2\phi_-^2$$

**Modulação diferencial mínima** (satisfaz a Z₂ e move a raiz):

$$\beta_1(\phi_-) = \beta_1^{(0)}\Big(1+\frac{\phi_-^2}{v_\ast^2}\Big),
\qquad \beta_{0,2,4} = \text{const},\qquad \beta_3 = 0$$

donde a raiz móvel r★(φ₋) = r★⁽⁰⁾(1+φ₋²/v★²). A dependência é em φ₋²
e não em φ₋ porque uma dependência linear quebraria a Z₂
**explicitamente** — e a bifurcação deixaria de ser bifurcação.

**Flag normativa (vinculante, G1-a):** a identificação "o modulador é
φ₋, o modo diferencial da bifurcação" é decisão de arquitetura, não
dedução — cap. 08.

## 2. Simetrias

| Simetria | Ação | Status |
|---|---|---|
| Difeomorfismo diagonal | g, f, φ±, ψ juntos | exata (HR quebra Diff_g×Diff_f na diagonal) |
| Z₂: φ₋ → −φ₋ (⟺ φ₁ ↔ φ₂) | paridade de V e dos β_n | exata na ação; **quebrada espontaneamente** |
| Matéria só em g | — | exigida (contagem BD) |

A Z₂ é a troca dos dois campos primordiais — é o que dá conteúdo
preciso à "bifurcação": estado simétrico ⟨φ₋⟩=0 (campos
indistinguíveis); a bifurcação é quebra espontânea padrão, com
parâmetro de ordem ⟨φ₋⟩. Massa efetiva do modo diferencial:

$$\partial^2_{\phi_-}V\big|_{\phi_-=0} = -\mu_-^2 + 2\lambda_c\phi_+^2$$

⟹ ponto crítico φ₊,crit² = μ₋²/(2λ_c): com φ₊ grande o estado
simétrico é estável; quando φ₊ rola abaixo do crítico, φ₋ condensa em
v²(φ₊) = (μ₋² − 2λ_cφ₊²)/λ₋, que cresce enquanto φ₊ rola — **a
separação estrutural evolui como consequência da dinâmica, não como
postulado**. *Nível 1 (Gate 1 critérios (b)–(d), (f)); a realização
dinâmica de fundo foi verificada adiante (Fase A; fundo reintegrado e
conferido em R-7c/e).*

## 3. Dimensões e verificação

Homogeneidade dimensional termo a termo (naturais, potências de
massa; [φ±]=1, [β_n]=0, [V]=4, [S]=0) mecanizada no script — critério
(a) do Gate 1. Tabela completa em `docs/acao_v2.md` §3.

## 4. Limite de recuperação — a ponte para os benchmarks

Com φ₋ = const, os β_n viram constantes e a ação é **Hassan–Rosen
padrão + dois escalares espectadores** (critério (e), simbólico). É
este limite que define o benchmark β-constante usado em toda a
cascata de perturbações (caps. 05–07) e que autoriza importar o
formalismo HR dos anexos da v1 sem reconstrução. Com φ₋=0 recupera-se
o ramo algébrico estático da v1 (§0).

## 5. O que a ação NÃO decide (e onde cada item foi parar)

- Ausência de fantasma BD com β_n(φ₋) — Gate 2: Parte A resolvida
  (cap. 04 §4); Parte B analítica aberta, com suporte dinâmico 2b
  (cap. 04 §4, cap. 07).
- Se ṙ★ é grande o bastante — respondido pelo fundo: a evolução
  estrutural nem precisa da modulação (cap. 05).
- Higuchi — resolvido no ramo finito (cap. 06).
- A forma de V₊(φ₊) — entrada do modelo (a bifurcação só exige φ₊
  decrescente).
- O destino de η — o símbolo não aparece nesta ação, de propósito
  (aposentado do núcleo; cap. 10).
