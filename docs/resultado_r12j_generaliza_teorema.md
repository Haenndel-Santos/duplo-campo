# R-12j — o teorema de c_s² em outras células, e o limite do método

**Data:** 2026-08-17. Scripts: `auditoria/code/r12j_generaliza_teorema.py`
(forma fechada) e `auditoria/code/r12k_limite_por_serie.py` (série
truncada, **não fecha** — ver §3). Ataca o item nº 1 da fila aberta em
`docs/resultado_r12b_teorema_cs2.md` §6: generalizar a fórmula em
(β₀, β₂, β₄, μ).

> **Nota de rótulo.** Este estudo nasceu como "R-12i", mas esse rótulo
> já está ocupado, no branch `revisao-corpus-pos-r12`, pelo confronto
> com Könnig et al. (`docs/resultado_r12i_confronto_konnig.md`), que é
> outra coisa. Renomeado para **R-12j**.

---

## 1. O que fechou

A redução 2-DOF simbólica do R-12b foi repetida em outras células da
classe F1. **Duas fecharam em forma fechada**, e dão fórmulas
diferentes com os mesmos três limites:

| célula | c_s²(r) | r → 0 | r_∞ | m_ef²/H² |
|---|---|---|---|---|
| **C1** β₂=β₄=0, β₀=1, μ=1 | −(3r+1)(9r⁵−6r³+3r²−10r+2) / (2(3r²+1)²) | **−1** | **+1** | **5/2** |
| **C2** β₂=β₄=0, β₀=2, μ=3 | −(729r⁶+486r⁵−162r⁴+54r³−81r²−24r+2) / (2(9r²+1)²) | **−1** | **+1** | **5/2** |

Séries: C1 dá `−1 + 2r + O(r²)`; C2 dá `−1 + 12r + O(r²)`. **As funções
e até os coeficientes de r diferem** — como têm de diferir, já que a
trajetória r(a) depende dos β_n. O que é universal são os **limites**.

O `m_ef²/H² = 5/2` idêntico nas duas é um segundo invariante, e bate
com a medida numérica independente do R-12f/g nas 108 células.

**Gate V-C1:** o pipeline reproduz exatamente a forma fechada já
provada no R-12b (commit `548bf3e`) antes de qualquer célula nova ser
aceita.

## 2. O que NÃO fechou, e por quê

**C3** (β₂ = −2/5, β₄ = 0), **C4** (β₄ = 1/2) e a célula de
**benchmark** do R-10a/R-11 (β₂ e β₄ ambos não nulos) **não fecham em
forma fechada**. Medido:

| célula | ops(W) na entrada | inversão de W_XX | pós-inversão |
|---|---|---|---|
| C1 | 711 | 105 s | ~15 s |
| C2 | 715 | 103 s | ~17 s |
| C3 | 1245 | 596 s | **> 9 500 s, sem terminar** |
| C4 | 1533 | 887 s | **> 9 300 s, sem terminar** |

A entrada cresce 2× e o custo explode mais de 600×. É inchaço de
expressão em aritmética de funções racionais: cada complemento de
Schur multiplica os graus, e `cancel` em quatro variáveis degrada de
forma superexponencial. Os dois processos foram encerrados —
consumiam CPU normalmente (~2h50 cada, memória estável em ~130 MB),
ou seja **não travaram**: o algoritmo é que não termina.

## 3. A tentativa por série, e o que ela ensinou (R-12k)

Como só o **limite** interessa, tentou-se substituir a forma fechada
por série de Laurent truncada (r = ρ², H = w/ρ, eliminação de Gauss
truncada no lugar da adjugate). Ficou **8× mais rápido** por célula —
e ainda assim **não fecha**. Mas produziu um achado que vale registrar:

> **Os dois limites não comutam, e isso foi medido.** Expandir em ρ a
> **k fixo** é o regime **super-horizonte**, porque `kh = k/(aH) → 0`
> quando `H ~ 1/ρ → ∞`. Nessa ordem, o coeficiente ρ⁰ de
> `ω²/(k/a)²` dá **−2** na célula C1 — **estável** sob refino (NORD 10
> e 12 dão o mesmo), logo não é artefato de truncamento. O valor
> sub-horizonte é **−1**. A ordem dos limites é parte da definição de
> c_s², não um detalhe.

Foi o gate V-C1 que pegou isso — o script obteve um número
perfeitamente estável e perfeitamente errado. Corrigir exige escalar
`k = q/ρ` (mantendo kh fixo) e acrescentar `dN(q) = q·g/(2ρ²)` ao
operador; feito isso, o sistema 4×4 passa a resolver em 2 s, mas o
gargalo migra para as etapas seguintes (Ċ₃, E2, Ċ₂) e o cálculo segue
não terminando. O script fica no repositório com a escala corrigida e
este diagnóstico no cabeçalho.

## 4. O estatuto, por eixo de parâmetro

| eixo | nível | fonte |
|---|---|---|
| β₀, μ | **1** (forma fechada, duas células independentes) | R-12b + este |
| β₂, β₄ | **2b** (108/108 células, `\|c_s²+1\| ≤ 1.1e−7`) | R-12g |

Não é o que a fila pedia — ela pedia a fórmula geral. O que se
conseguiu foi elevar **(β₀, μ)** a nível 1 e demonstrar que a rota da
forma fechada **não escala** para (β₂, β₄) com esta maquinaria.

Nota de relevância: o branch `revisao-corpus-pos-r12` observa que o
ramo infinito viável exige `0 < β₄ < 2β₁`, e que a célula mínima deste
teorema tem β₄ = 0. Isso não afeta o teorema — ele é sobre o ramo
**finito** — mas torna a célula com β₄ ≠ 0 a mais valiosa das que
ficaram em aberto, porque responderia à objeção "a célula é especial".

## 5. Fila que este resultado deixa

1. **(β₂, β₄) em nível 1** continua em aberto. As rotas plausíveis:
   (a) expansão em ρ com a escala `k = q/ρ` já corrigida, mas com
   representação própria de Laurent truncado (dicionário de potências)
   em vez de expressões sympy — o gargalo atual é `cancel`/`series`,
   não a matemática; (b) eliminar `a` explorando a homogeneidade em
   (a, k), que tira uma variável de toda a aritmética.
2. O `m_ef²/H² = 5/2` como segundo invariante de classe merece o mesmo
   tratamento que o `c_s² = −1` recebeu.
