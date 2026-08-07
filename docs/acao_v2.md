# TDCP v2 — Passo 1: A Ação Mínima

**Passo 1 do `plano_v2_reconstrucao.md`.** Notação conforme
`dicionario_simbolos.md`. Verificação: `auditoria/code/gate1_acao.py`.

---

## 0. Achado que determina o desenho

Antes da ação, um resultado de duas linhas que reorienta a arquitetura.

Na v1, a modulação estrutural era um fator **global** `F(φ)`
multiplicando todo o potencial HR. Mas o ramo algébrico fixa `r` na
raiz de `ℬ(r)=β₁+2β₂r+β₃r²=0`, que na família F1 (β₃=0) dá

$$r_\star = -\frac{\beta_1}{2\beta_2}$$

Sob uma modulação global `β_n → F(φ)β_n`:

$$r_\star \to -\frac{F\beta_1}{2F\beta_2} = -\frac{\beta_1}{2\beta_2} = r_\star$$

**O fator global cancela na razão. A raiz não se move.**

Ou seja: o mecanismo de modulação da v1 era **estruturalmente incapaz**
de produzir evolução de `r` no ramo algébrico — não por um erro de
conta, mas por uma degenerescência da forma escolhida. Isso explica por
que a v1 precisou apelar para o ramo dinâmico, onde `ṙ≡0` a matou de
outra maneira. **Os dois ramos estavam mortos pela mesma razão de
fundo: nenhum dos dois tinha um mecanismo capaz de mover a estrutura.**

**Consequência para a v2:** a modulação precisa ser **diferencial** —
ao menos uma razão `β_i/β_j` deve depender do campo. Um `F(φ)` global
é redundante e é absorvido: `F(φ)Σβ_n e_n = Σ[F(φ)β_n]e_n`. A v2
elimina `F` como função separada e trabalha com `β_n(φ₋)` direto.

---

## 1. A ação

$$
\begin{aligned}
S \;=\; & \frac{M_g^2}{2}\int d^4x\,\sqrt{-g}\,R[g]
\;+\; \frac{M_f^2}{2}\int d^4x\,\sqrt{-f}\,R[f] \\[4pt]
& -\; m^2 M_{\rm eff}^2 \int d^4x\,\sqrt{-g}\,
      \sum_{n=0}^{4}\beta_n(\phi_-)\,e_n(\mathcal K) \\[4pt]
& +\; \int d^4x\,\sqrt{-g}\left[
      -\tfrac12 g^{\mu\nu}\partial_\mu\phi_+\partial_\nu\phi_+
      -\tfrac12 g^{\mu\nu}\partial_\mu\phi_-\partial_\nu\phi_-
      - V(\phi_+,\phi_-)\right] \\[4pt]
& +\; S_m[g,\psi]
\end{aligned}
$$

com $\mathcal K = \sqrt{g^{-1}f}$, $M_{\rm eff}^{-2}=M_g^{-2}+M_f^{-2}$,
e os campos primordiais em base normal:

$$\phi_\pm = \frac{\phi_1 \pm \phi_2}{\sqrt2}$$

### 1.1 Potencial dos campos primordiais

$$V(\phi_+,\phi_-) = V_+(\phi_+)
\;-\;\tfrac12\mu_-^2\phi_-^2
\;+\;\tfrac14\lambda_-\phi_-^4
\;+\;\lambda_c\,\phi_+^2\phi_-^2$$

Isto **fecha o achado A7** do Lote 1: a v1 nunca especificou $V(\Phi_\pm)$
em lugar nenhum, o que deixava $m_-^2<0$ como hipótese narrada em vez de
consequência. Aqui a instabilidade do modo diferencial decorre do
potencial.

$V_+(\phi_+)$ fica como entrada do modelo (uma escolha tipo
$V_+=\tfrac12 m_+^2\phi_+^2$ ou exponencial resolve o Passo 3); a
bifurcação não depende de sua forma, só de $\phi_+$ decrescer.

### 1.2 Modulação diferencial dos β_n

Forma mínima que satisfaz a Z₂ (ver §2) e move a raiz:

$$\boxed{\;\beta_1(\phi_-) = \beta_1^{(0)}\left(1+\frac{\phi_-^2}{v_\ast^2}\right),
\qquad \beta_2 = \beta_2^{(0)},\qquad \beta_3 = 0\;}$$

$\beta_0$ e $\beta_4$ permanecem constantes na versão mínima
($\beta_0$ é a peça tipo-Λ de $\rho_{\rm int}$; $\beta_4$ só entra no
setor f). $v_\ast$ é a escala de modulação — naturalmente da ordem do
VEV de $\phi_-$, mas é parâmetro livre.

Daí a raiz móvel:

$$\boxed{\;r_\star(\phi_-) = -\frac{\beta_1^{(0)}}{2\beta_2^{(0)}}
\left(1+\frac{\phi_-^2}{v_\ast^2}\right)\;}$$

Pré-bifurcação ($\phi_-=0$): $r_\star = r_\star^{(0)}$. Com
$\phi_-\to\pm v$: $r_\star = r_\star^{(0)}(1+v^2/v_\ast^2)$. Escolhendo
$v_\ast \sim v$, a raiz dobra — evolução ampla, sem tuning fino.

**Por que $\phi_-^2$ e não $\phi_-$:** a paridade é exigida pela Z₂
(§2). Uma dependência linear quebraria a simetria **explicitamente**,
não espontaneamente — e a bifurcação deixaria de ser bifurcação.

---

## 2. Simetrias declaradas

| Simetria | Ação sobre os campos | Status |
|---|---|---|
| Difeomorfismo diagonal | $g,f,\phi_\pm,\psi$ transformam juntos | **exata** — HR quebra $\mathrm{Diff}_g\times\mathrm{Diff}_f$ na diagonal |
| $\mathbb{Z}_2$: $\phi_-\to-\phi_-$ | equivale a $\phi_1\leftrightarrow\phi_2$ | **exata na ação, quebrada espontaneamente** |
| Acoplamento de matéria | só a $g_{\mu\nu}$ | **exigido** — é do que depende a contagem sem fantasma BD |

**A Z₂ é a simetria de troca dos dois campos primordiais.** É exatamente
isto que dá conteúdo preciso à narrativa de "bifurcação": o estado
simétrico tem $\langle\phi_-\rangle=0$ (os dois campos indistinguíveis);
a bifurcação é a **quebra espontânea** dessa troca. Não é metáfora — é
quebra espontânea de simetria padrão, com o parâmetro de ordem
$\langle\phi_-\rangle$.

Verificações de paridade que o Gate 1 exige:
$V(\phi_+,-\phi_-)=V(\phi_+,\phi_-)$ e $\beta_n(-\phi_-)=\beta_n(\phi_-)$.

---

## 3. Dimensões (naturais, ℏ=c=1, em potências de massa)

| Objeto | Dim. | Objeto | Dim. |
|---|---|---|---|
| $d^4x$ | −4 | $\phi_\pm$ | 1 |
| $g_{\mu\nu}$, $\sqrt{-g}$, $\mathcal K$, $e_n$ | 0 | $\partial_\mu\phi$ | 2 |
| $R[g]$ | 2 | $V(\phi_+,\phi_-)$ | 4 |
| $M_g$, $M_f$, $M_{\rm eff}$, $m$ | 1 | $\mu_-$ | 1 |
| $\beta_n$ | 0 | $\lambda_-$, $\lambda_c$ | 0 |
| $v_\ast$ | 1 | $r$, $\xi$ | 0 |

Cada termo da densidade lagrangiana tem dimensão 4, e $[d^4x]=-4$, logo
$[S]=0$. Verificação termo a termo no script.

---

## 4. Mecanismo da bifurcação

Massa efetiva do modo diferencial em torno do estado simétrico:

$$\frac{\partial^2V}{\partial\phi_-^2}\bigg|_{\phi_-=0}
= -\mu_-^2 + 2\lambda_c\phi_+^2$$

(o fator 2 vem da segunda derivada de $\phi_-^2$ no termo de portal —
uma versão anterior desta proposta trazia $\lambda_c\phi_+^2$ sem o 2).

**Ponto crítico:**

$$\phi_{+,\rm crit}^2 = \frac{\mu_-^2}{2\lambda_c}$$

**Cronologia:** no universo primordial, $\phi_+$ grande ⟹ massa efetiva
positiva ⟹ $\phi_-=0$ estável, os dois campos indistinguíveis. Conforme
$\phi_+$ rola e cruza $\phi_{+,\rm crit}$, o estado simétrico
desestabiliza e $\phi_-$ rola para

$$v^2(\phi_+) = \frac{\mu_-^2 - 2\lambda_c\phi_+^2}{\lambda_-}$$

Como $\phi_+$ continua rolando, $v$ continua crescendo — e portanto
$r_\star$ continua se movendo. **A separação estrutural evolui em tempo
cósmico como consequência da dinâmica, não como postulado.**

---

## 5. Limite de recuperação

Com $\phi_-$ = const, os $\beta_n$ viram constantes e a ação é
**Hassan–Rosen padrão** mais dois escalares espectadores. Todo o
formalismo dos Anexos A e B se aplica sem modificação — é o que
autoriza importar aqueles ativos em vez de reconstruí-los.

Adicionalmente, com $\phi_-=0$: $r_\star=r_\star^{(0)}$, e recupera-se
exatamente o ramo algébrico da v1 (que era estático — §0).

---

## 6. O que este passo NÃO decide

Declarado explicitamente para não repetir o vício da v1 de tratar
escolha como derivação:

- **Ausência de fantasma BD com $\beta_n(\phi_-)$** — Gate 2. Há
  argumento a priori favorável (os $\beta_n$ não contêm o lapso, logo a
  linearidade em $N_g$ que sustenta a constraint primária é intocada),
  mas argumento não é prova.
- **Se $\dot r_\star$ é grande o bastante** para importar — Gate 3.
- **Se Higuchi sobrevive** neste fundo — Gate 3.5.
- **A forma de $V_+(\phi_+)$** — fixada no Passo 3, conforme o que o
  fundo exigir.
- **O destino de η** — Gate 9. O símbolo não aparece nesta ação, de
  propósito.

---

## Gate 1 — critério de passagem

| Critério | Verificação |
|---|---|
| (a) homogeneidade dimensional | script, termo a termo |
| (b) simetrias declaradas | script: paridade Z₂ de $V$ e $\beta_n$ |
| (c) $V(\phi_+,\phi_-)$ explícito | §1.1 — fecha A7 |
| (d) $\beta_n(\phi_-)$ com forma funcional | §1.2 |
| (e) reduz a HR padrão com $\phi_-$=const | script, limite simbólico |
| (f) a raiz de fato se move | script: $\partial r_\star/\partial\phi_-\neq0$ |
| (g) modulação global **não** move a raiz | script — confirma o achado §0 |

**Nível exigido:** 1 (álgebra fechada; o script apenas mecaniza).

**Se falhar:** o modo de falha previsto é (d) contra (c) — não existir
$\beta_n(\phi_-)$ que admita bifurcação e mantenha os $\beta_n$ em faixa
sensata. Nesse caso, testar $\phi_+$ como modulador, ou um terceiro
campo, e reabrir a escolha de arquitetura.
