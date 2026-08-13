# R-12b — TEOREMA: c_s²(r) em forma fechada, com c_s² = −1 exato em r → 0

**Data:** 2026-08-13. Script: `auditoria/code/r12b_prova_simbolica_cs2.py`
(saída em `out/`). Fecha o item nº 1 da fila do R-11. Ler junto com
`docs/resultado_r12_instrumento_e_cs2.md` (Erratum-03), que estabelece
o instrumento numérico limpo contra o qual este resultado é conferido.

---

## 1. O enunciado

> **TEOREMA (célula mínima da classe F1).** No ramo finito da bimétrica
> de Hassan–Rosen com β₃ = 0, matéria acoplada só a g, na célula
> β₂ = β₄ = 0 (o modelo mínimo β₀–β₁), a velocidade de gradiente do
> escalar métrico do sistema 2-DOF é a função racional do fundo
>
> $$c_s^2(r) \;=\; -\,\frac{(3r+1)\,(9r^5 - 6r^3 + 3r^2 - 10r + 2)}{2\,(3r^2+1)^2}$$
>
> e portanto
>
> $$\lim_{r\to 0} c_s^2 = -1 \qquad\text{(exato)},\qquad
>   c_s^2\big|_{r=r_\infty} = +1 \qquad\text{(exato)},$$
>
> com $r_\infty = (\sqrt{13}-1)/6$ o atrator tardio (ρ̃ = 0).

Série em torno do regime primordial:

$$c_s^2(r) = -1 + 2r + \tfrac{39}{2}r^2 + O(r^3).$$

Relação de dispersão sub-horizonte completa:

$$\omega^2 = c_s^2(r)\,(k/a)^2 + m_{\rm ef}^2(r) + O(k^{-2}),\qquad
  \frac{m_{\rm ef}^2}{H^2}\ \xrightarrow[r\to0]{}\ \frac52 .$$

**Os dois limites são exatamente ±1.** O modo métrico sai de
`c_s² = −1` no passado profundo e chega a `c_s² = +1` no atrator de
de Sitter, passando por zero em a_cross ≈ 0.578 (z ≈ 0.61).

## 2. Por que isto vale mais que a medida

O R-11 conjecturou `c_s² = −1` extrapolando dois pontos; o R-12g
mediu `−1` com `|c_s²+1| ≤ 1.1e−7` em 108/108 células. Este resultado
não é medida: é **identidade algébrica**. Ele mostra que o −1 não é
coincidência numérica nem propriedade de uma janela de k — é o valor
de uma função racional do fundo num ponto onde ela é regular. E o `+1`
do atrator tardio, que os canais numéricos davam como `1.0000079`,
sai como identidade exata.

## 3. O passo que faz a conta fechar (e o modo de falha que ele evita)

A redução simbólica só é possível **eliminando β₁** em favor de (r, H)
pela equação de Friedmann do setor f:

$$\beta_1 \;=\; 3(1+\mu)H^2 r - \beta_4 r^3 - 3\beta_2 r .$$

Com isso `(a, r, k, H)` viram coordenadas **livres**, tudo permanece no
corpo das funções racionais, e não aparece nenhuma extensão algébrica
nem raiz quadrada em lugar nenhum do cálculo.

A legitimidade é um gate de uma linha, **V-B1: dN(β₁) ≡ 0**. Como o
operador de derivada ao longo do fundo é tangente à superfície onde β₁
é constante, a derivada calculada em (r, H) coincide com a verdadeira a
β₁ fixo.

**O modo de falha evitado** (preservado no git, v2 do script): tratar H
como símbolo livre e guardar o vínculo H² = HH(r) para o fim **não
funciona** — a identidade estrutural `K3[0,:] = 0`, que diz que Ψ_f é
auxiliar, deixa de valer identicamente e a redução não pode ser feita.
Antes disso, uma v1 tentou fatorar `C = H·Ĉ` por paridade t → −t e
reprovou por razão física: `B_g` e `B_f` vêm de g₀ᵢ e são **ímpares**,
de modo que a paridade de H em W_ij é p_i p_j, não +1.

## 4. Gates (todos aprovados)

| Gate | O que testa | Resultado |
|---|---|---|
| **V-BG** | fundo simbólico == fundo do código numérico (ρ̃′ = dW; d²r/dN² pela cadeia) | 0 e 0 |
| **V-B1** | dN(β₁) ≡ 0 — legitima as coordenadas livres | 0 |
| **V-K3** | linha 0 de K₃ (Ψ_f) identicamente nula | **exata** — o gate G1 do numérico (\|·\| < 1e−10) vira identidade |
| **V-EVEN** | ω² par em H (t → −t com p(B) = −1) | 0 |
| **V-SPEC** | espectador δχ em forma fechada | **ω² = (k/a)² + U″** — c_s² = 1 exato e massa = U″; mais forte que o calibrador numérico, que só via 1 + U″/(k/a)² |
| **V-A** | a e k só aparecem via k/a | invariante sob (a,k) → (λa, λk) |

## 5. Alcance e fronteiras

**Nível 1 (forma fechada)** para a célula β₂ = β₄ = 0, β₀ = 1, μ = 1,
β₃ = 0, ramo finito, matéria só como ρ de fundo, sem radiação,
F′ = F″ = 0, sistema 2-DOF do setor escalar.

**Nível 2b para a classe:** a extensão a (β₀, β₂, β₄, μ) é numérica
(R-12g: 108/108 células, `|c_s²+1| ≤ 1.1e−7`, instrumento limpo). A
célula β₂ = β₄ = 0 foi escolhida porque é a única em que o fundo fica
pequeno o bastante para a redução fechar exatamente — a inversão
simbólica de W_XX na célula de benchmark não terminou em ~40 min de
CPU.

**Não provado aqui:** a fórmula geral em (β₀, β₂, β₄, μ); β₃ ≠ 0 (que
sai da F1); o acoplamento à matéria perturbada.

## 6. O que isto faz com o programa

O **no-go de classe por gradiente** deixa de ser um resultado numérico
e passa a ter um núcleo analítico: `c_s² = −1` é identidade, não
ajuste. Nada mais muda — a era instável continua cobrindo a
recombinação, as quatro saídas continuam fechadas, e a única porta
entreaberta continua sendo β₃ ≠ 0 (que leva para fora da F1).

> **[REABERTURA — 2026-08-13, R-12i]** *Nota acrescentada; o parágrafo
> acima permanece intacto.* A contagem caiu: são **três saídas
> fechadas e uma reaberta**. A exclusão do ramo infinito por "ξ cruza
> zero" não se sustenta — como `b = ra`, `ξ = X/a` com o `X ≡ ḃ/ℋ` de
> Könnig et al., **mesmo sinal e mesmo zero**, e é o quique de `b` que
> 1407.4331 §II/§VI trata e defende como físico, com três argumentos.
> Reexame pendente, e o alvo é o ramo infinito **com β₄ ≠ 0** (o IBB
> viável exige `0 < β₄ < 2β₁`; a célula mínima — justamente a deste
> teorema — tem β₄ = 0). Logo as portas entreabertas são duas:
> β₃ ≠ 0 e esse reexame. **O teorema deste documento não é afetado:**
> ele é sobre o ramo finito. *Fonte:
> `docs/resultado_r12i_confronto_konnig.md` §1.6 e §6 (risco R-b).*
>
> **[VEREDITO — 2026-08-13, R-13a + R-13b: o reexame foi feito.]** A
> contagem volta a **quatro fechadas**, mas com a exclusão do ramo
> infinito **inteiramente substituída** — nunca cite a contagem sem a
> substituição. O argumento `ξ = 0` **permanece REVOGADO**; o que
> exclui o ramo agora é o **ghost de Higuchi**: `Higuchi ⟺ ξ ≥ r ⟺
> r′ ≥ 0` (tradução verificada na fonte e re-verificada por CAS em rota
> independente), e nas células IBB genuínas `r′ < 0` em 100% da
> história em **108/108**, com Higuchi satisfeito em **0 de 64 800**
> pontos. Logo **a porta entreaberta volta a ser uma só: β₃ ≠ 0.** O
> teorema deste documento continua não sendo afetado. *Fontes:
> `docs/resultado_r13a_criterio_higuchi_fonte.md`,
> `docs/resultado_r13b_ibb_ramo_infinito.md`.*

**Fila que este resultado abre:**

1. **Generalizar a fórmula** em (β₀, β₂, β₄, μ) — provavelmente
   factível com expansão de Laurent em r em vez de forma fechada
   exata.
2. **Confrontar com Könnig et al. ([arXiv:1407.4331])**: agora há uma
   fórmula fechada para comparar, não só um número. *[verificar contra
   a fonte]*
3. A interpretação de `c_s² = ±1` nos dois extremos — o valor `+1` no
   atrator sugere que o modo métrico se torna um escalar de gradiente
   canônico lá, e `−1` sugere assinatura invertida no passado; vale
   procurar a forma canônica que torna isso manifesto.
