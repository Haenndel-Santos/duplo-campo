# R-11 — NO-GO DE CLASSE POR GRADIENTE: c_s² → −1 em r → 0, independente da forma-β

**Data:** 2026-08-13. Script: `auditoria/code/r11_varredura_forma_beta.py`
(saída em `out/`). Fecha a última saída listada em
`docs/resultado_r10_consolidado.md` §4.

---

## 1. O resultado

Varredura de **108 células** da forma do potencial — β₀ ∈ {0.5, 1, 2},
β₂ ∈ {−2, −1, −0.4, −0.1}, β₄ ∈ {0.1, 0.5, 2}, μ = M_f²/M_g² ∈
{0.3, 1, 3} — avaliadas em a = 0.01 (r ≈ 1.7e−6, fundo do regime
instável), com β₁ = 1 e β₃ = 0 (a família F1 por definição da ação):

| | valor |
|---|---|
| células interpretáveis | **108/108** (0 fundo inválido, 0 descartadas por calibração) |
| c_s² com sinal positivo | **0** |
| c_s² mínimo / máximo | −1.01034 / −1.01032 |
| mediana | −1.01034 |
| **desvio-padrão** | **6.3 × 10⁻⁶** |
| calibrador (espectador) | 1.00000 em todas |

**A dispersão é nula sobre quatro parâmetros de forma variados em
faixas de até 20×.** c_s²(r → 0) não é função dos β_n: é **constante
estrutural da classe**.

## 2. O enunciado

> **NO-GO DE CLASSE POR GRADIENTE.** Na classe F1 (bimétrica de
> Hassan–Rosen com β₃ = 0, matéria acoplada só a g, ramo finito), o
> escalar métrico tem c_s² → −1 no regime r → 0, para **qualquer**
> escolha de β₀, β₂, β₄ e da razão de massas de Planck. A
> instabilidade de gradiente em alto redshift não é uma propriedade
> da célula de benchmark: é uma propriedade da classe.

Nota fina: o valor medido é −1.010 em kh = 30 e −1.261 em kh = 100. A
extrapolação para k → ∞ do par (removendo o termo ~k⁴ já identificado
no R-9a) dá **c_s² ≈ −0.986 ≈ −1**. O valor exato −1 sugere origem
estrutural limpa — é um **candidato a teorema analítico**, e provar
`c_s² = −1` em forma fechada seria o resultado mais forte, e mais
publicável, que este programa produziu. *(Se coincidir com a forma
analítica de Könnig et al. [arXiv:1407.4331], é confirmação
independente — [verificar] contra a fonte.)*

## 3. O balanço final das saídas

| Saída | Estado |
|---|---|
| Ramo infinito | **fechada** (ξ cruza zero; não conecta) — R-10c |
| Modulação β₁(φ₋) | **fechada** (chega ~3 ordens tarde) — R-10c |
| Screening de Vainshtein | **fechada** (δ_screen ≈ 20–60; o λ cancela) — R-10d |
| Forma-β | **fechada** (constante estrutural) — R-11 |
| Auto-invalidação linear | viva, mas **não é proteção**: impede refutar e impede calcular |

**Nenhuma saída conhecida resta dentro da implementação F1.**

## 4. O que a TDCP é, hoje

Com o mesmo rigor que derrubou o no-go anterior (Erratum-02), o
programa agora produz um no-go novo — e este é **de classe, não de
célula**, o que o torna qualitativamente mais forte que o antigo:

- **O antigo** (fantasma/taquião) era artefato de um bug numérico e
  caiu quando o instrumento foi corrigido.
- **Este** foi medido com o instrumento já corrigido e validado
  (calibrador exato em 108/108 células), é insensível a todos os
  parâmetros da forma, e reproduz uma previsão independente da
  literatura que o repositório registrava sem ter confrontado.

**Fica de pé, sem alteração:** o Erratum-01 (Bianchi) e o Erratum-02;
o fundo do ramo finito; o setor tensorial (m_T²/H² → 12 primordial,
Higuchi automático); a predição m_T ≈ 2.3 H₀; o espectador δφ₋
saudável em toda a história; a contagem 2-DOF; o Gate 1 e o
enquadramento R1; e todo o método.

**Cai:** a suficiência da implementação F1 como cosmologia. Não a
TDCP como hipótese conceitual — que continua sem implementação que
feche, exatamente como o Gate 1 já dizia por outra via.

## 5. O que fazer com isto

1. **Provar analiticamente c_s² = −1** em r → 0. Alvo limpo,
   resultado de classe, publicável. É o próximo cálculo natural e
   fecha o enunciado em nível 1.
2. **Reescrever o cap. 07 da v2** com o arco completo: falso no-go →
   correção → saúde tardia → no-go real de classe por gradiente. A
   história metodológica ficou mais forte, não mais fraca: o programa
   derrubou o próprio erro e depois encontrou o problema verdadeiro.
3. **Reorientar o cap. 09**: não há programa observacional linear a
   executar enquanto a era instável cobrir a recombinação. O
   enunciado honesto é o da opção (3) do R-10 consolidado —
   implementação com validade restrita.
4. **Fronteira que pode reabrir tudo**: β₃ ≠ 0 sai da definição de F1,
   mas é a única direção não varrida do potencial (a varredura
   manteve β₃ = 0 por fidelidade à ação do cap. 03). Testá-la exige
   refazer o fundo (a cúbica muda). É a única porta que este
   resultado deixa entreaberta — e ela leva para fora da F1, isto é,
   para uma F2.

## 6. Fronteiras declaradas

Um ponto de época (a = 0.01) por célula, kh = 30, β₁ = 1 fixo (o R-8b
mostrou que a rescala uniforme é dial degenerado), β₃ = 0, matéria só
como ρ de fundo, sem radiação. O calibrador exato em 108/108 é o que
autoriza a leitura. Não medido: dependência em k além de dois valores;
β₃ ≠ 0; acoplamento a matéria perturbada.
