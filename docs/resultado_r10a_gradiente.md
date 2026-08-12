# R-10a (A1) — INSTABILIDADE DE GRADIENTE CONFIRMADA EM ALTO REDSHIFT

**Data:** 2026-08-13. Script: `auditoria/code/r10a_gradiente_alto_z.py`
(saída em `out/`). Origem: item A1 do Bloco 1, prioridade máxima da
síntese dos pareceres (`docs/pareceres_especialistas/00_sintese_cruzada.md`
§4.1 item 2 e §7). **Este é o achado mais grave desde o Erratum-02, e
ele vem em sentido contrário: não derruba um problema, cria um.**

---

## 1. O resultado

No benchmark β-constante, com a frequência efetiva correta
(`ω²_ef = (Ċ+W)/K`, conforme o R-9a), a velocidade de gradiente do
**escalar métrico** é:

| a | r | ξ/r | c_s² (kh=30) | c_s² (kh=100) | c_s²(espectador) | cond(W_XX) |
|---|---|---|---|---|---|---|
| 0.001 | 1.7e−09 | 4.000 | **−1.010** | **−1.261** | 1.00000 | 1.1e17 |
| 0.01 | 1.7e−06 | 4.000 | **−1.010** | **−1.261** | 1.00000 | 1.1e11 |
| 0.1 | 1.7e−03 | 3.989 | **−1.004** | **−1.243** | 1.00000 | 1.1e05 |
| 0.316 | 4.7e−02 | 3.654 | **−0.788** | **−0.814** | 1.00005 | **1.5e02** |
| 1 | 0.284 | 1.440 | +0.726 | +0.728 | 1.00046 | 9.3 |
| 3.16 | 0.331 | 1.016 | +1.000 | +1.000 | 1.00058 | 9.8 |
| ≥10 | 0.332 | 1.000 | +1.010 | +1.010 | 1.00058 | 9.8 |

Idêntico em β₁ = 4.47 (transição em r ≈ 0.19–0.50).

**c_s² < 0 em todo o regime r → 0 — exatamente onde
Könnig–Akrami–Amendola–Motta–Solomon ([arXiv:1407.4331]) declaram o
finite branch instável por gradiente.** A previsão da literatura, que
o `posicionamento_literatura.md` registrava sem nunca confrontar, **se
reproduz na nossa implementação**.

## 2. Os três controles que tornam o achado sólido

1. **É gradiente, não fantasma.** `K₂` do modo métrico é **positivo**
   em todos os pontos de alerta (a nulidade relativa 1e−26 é apenas a
   diferença de escala entre os dois modos diagonais, não
   degenerescência). Cinética sã + ω² < 0 no setor de k² = gradiente.
2. **O método está calibrado.** O espectador δφ₋ dá c_s² = 1.00000 em
   *todos* os pontos, inclusive nos de pior condicionamento — o
   instrumento funciona onde o achado aparece.
3. **Não depende de pontos mal condicionados.** O script marcou 8/24
   pontos de alerta com `cond(W_XX) < 1e6`; em particular **a = 0.316
   tem cond = 150 (excelente) e c_s² = −0.79**. O sinal negativo já
   está presente no regime bem condicionado, e é *estável* ao longo de
   12 ordens de condicionamento (−1.010 de a=0.001 a a=0.1) — o
   oposto do que um artefato numérico faria.

## 3. O que isto faz com o corpus

**Corrige uma afirmação central do cap. 07.** O enunciado "setor
escalar são em todos os regimes testados" era literalmente verdadeiro
e materialmente enganoso: *nunca testamos a < 100*. Toda a cascata
R-7 e as sondas R-8 rodaram em a ∈ [100, 80000], que neste brinquedo é
a era tardia (r = r_∞). O regime da alegação da literatura ficou fora
por construção — a mesma família de ponto cego do Erratum-02, agora no
eixo do tempo cósmico.

**Enunciado corrigido:** o setor escalar é são **na era tardia**
(r ≳ 0.28); em alto redshift (r ≲ 0.05) o escalar métrico tem
**instabilidade de gradiente com c_s² ≈ −1**, e a taxa é |c_s|k/a —
ou seja, ~30H para um modo com k/aH = 30. Para modos sub-horizonte na
era primordial isso é catastrófico em tempo linear.

**O que NÃO muda:** o Erratum-02 continua válido (o fantasma era
artefato); a contagem 2-DOF continua válida; o espectador continua
saudável; o fundo e o setor tensorial não são tocados.

## 3b. Severidade (R-10b): a instabilidade NÃO é só de "alto z"

O R-10b (`auditoria/code/r10b_severidade_instabilidade.py`) mediu o
perfil fino e o crescimento acumulado. Dois resultados que agravam
o quadro:

**(i) A época crítica é BAIXO redshift.** c_s² muda de sinal em
**a_cross = 0.574** (β₁=1; r = 0.171) e **0.360** (β₁=4.47). Com o
"hoje" da família (a₀ = 0.931, âncora Ω_m = 0.3 do R-8b), isso dá
**z_cross ≈ 0.62**. A instabilidade opera de todo o passado até
z ≈ 0.6 — não é um fenômeno primordial remoto, e o rótulo "alto z"
da literatura subestima o alcance nesta implementação.

**(ii) Modos bem dentro do horizonte saem do regime linear.**
Crescimento acumulado lnA = ∫|c_s|·(k/aH) dN por modo, rotulado pela
entrada no horizonte (β₁=1):

| entra em a | kh em a_cross | lnA | fator | linear? |
|---|---|---|---|---|
| 0.0015 | 16.2 | 32.4 | 1e14 | **NÃO** |
| 0.0065 | 7.8 | 14.6 | 2e6 | **NÃO** |
| 0.013 | 5.4 | 9.5 | 1.3e4 | sim (formalmente) |
| 0.058 | 2.6 | 3.5 | 35 | sim |
| 0.25 | 1.3 | 0.7 | 2.0 | sim |

Fronteira em **kh(a_cross) ≈ 7–8**: acima disso, |Φ| ~ 1 antes do fim
da era instável (com δ_i = 1e-5 adotado como referência). β₁=4.47 dá
o mesmo quadro com fronteira em kh ≈ 6.9.

**Leitura conjunta.** A saída de Akrami et al. **se aplica** — nas
escalas mais violentas a perturbação linear se auto-invalida, e a
instabilidade linear não é, por si, uma refutação. Mas o mesmo
argumento tem preço alto: (a) nada linear pode ser afirmado em
kh ≳ 8 antes de z ≈ 0.6, o que inclui parte da janela observável;
(b) as escalas intermediárias (kh ~ 1–7) permanecem *formalmente*
lineares e ainda assim crescem por fatores de 2 a 10⁴ — uma
deformação enorme da função de transferência, que precisa ser
calculada e confrontada, não ignorada; (c) o modo que cresce é o
escalar métrico do sistema reduzido, e o R-7b mediu |Φ_g|/A_met ≈
0.04–0.09 constante — ou seja, o potencial observável herda o
crescimento salvo cancelamento não demonstrado.

## 4. As saídas — e por que a próxima medida é o Vainshtein

Esta instabilidade é conhecida na literatura bimétrica e tem uma
resolução padrão candidata, que o repositório precisa agora testar:

1. **Screening / validade linear** (a rota principal): Akrami et al.
   ([arXiv:1503.07521], "Bimetric gravity is cosmologically viable")
   argumentam que, para massa de gráviton suficientemente grande, a
   instabilidade ocorre em escalas **abaixo do raio de Vainshtein**,
   onde a teoria de perturbação linear já não vale — a instabilidade
   linear não seria física. Isso conecta diretamente com a exigência
   do parecer de astrofísica (Vainshtein/PPN nunca re-derivado). *É a
   candidata mais forte e o próximo teste obrigatório.*
2. **Ramo infinito**: é o que a literatura promove; nós o descartamos
   por ξ < 0 (lapso negativo no setor f) — revisitar essa exclusão com
   a álgebra atual.
3. **Região de parâmetros**: varrer β₂, β₄ e μ procurando janela com
   c_s² > 0 em alto z. O R-8b mostrou que a forma-β do benchmark é
   rígida (fold em s ≈ 5.7); a varredura precisa ser em forma, não em
   escala.
4. **Corte de época**: se a condensação de φ₋ (que no fundo dinâmico
   ocorre em a ~ 10³) mudar o regime, a janela instável pode não ser
   fisicamente realizada. Requer refazer esta medida no **fundo
   dinâmico** — não feito aqui (fronteira declarada).

## 5. Fronteiras declaradas

Fundos β-constantes (a alegação da literatura é sobre HR com β
constante — este é o confronto correto); matéria só como ρ de fundo,
**sem era de radiação** (o brinquedo não a tem; é o item (f) do Bloco
1 e muda o mapa a ↔ z); dois valores de kh; sistema 2-DOF reduzido.
Não medido aqui: a taxa de crescimento integrada, o fundo dinâmico, e
o raio de Vainshtein.

## 6. Fila — reordenada por este resultado

1. **Vainshtein/validade linear** (era Bloco 2, sobe para o topo): a
   instabilidade está acima ou abaixo da escala de screening? É o que
   decide se este achado mata a implementação ou é inócuo. Conecta
   astrofísica (r_V) + cosmologia (c_s²) num só teste.
2. **A janela intermediária kh ~ 1–7** (nova, criada pelo R-10b): é o
   único lugar onde a teoria é simultaneamente *linear* e
   *drasticamente diferente de GR* (fatores 2–10⁴). Deixa de ser
   "região indecidida" e passa a ser **a previsão observacional mais
   forte que a implementação já produziu** — com o sinal errado, mas
   forte. Calculá-la é agora mais informativo que o C_ℓ completo.
3. Refazer A1/A2 no **fundo dinâmico** (com a condensação de φ₋) e com
   **era de radiação** (item (f)) — a janela instável pode mudar; e
   com radiação a_cross se move.
4. Reexaminar a exclusão do ramo infinito.
5. O resto do Bloco 1 (A2 w_eff, varredura de μ, paredes de domínio)
   segue válido mas perde prioridade relativa: **não faz sentido
   ajustar previsões observacionais de um ramo cuja validade linear
   está em questão até z ≈ 0.6**.

## 7. Estatuto e o que este resultado NÃO diz

Nível 2b com fronteiras declaradas (§5). **Não** é uma refutação da
TDCP: (i) a saída de screening é real e não foi testada; (ii) o
brinquedo não tem radiação, e a_cross depende da história; (iii) o
fundo dinâmico com condensação de φ₋ não foi medido aqui; (iv) o modo
que cresce é métrico-do-sistema-reduzido — o acoplamento à matéria
perturbada (nunca calculado) é que decide o observável. **É**, sim, a
demonstração de que a afirmação de saúde do cap. 07 foi feita sobre
uma janela temporal estreita, e que o programa observacional do
cap. 09 não pode prosseguir como estava.
