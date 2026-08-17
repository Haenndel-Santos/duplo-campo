# Externos NÃO EXECUTADOS — infraestrutura R6-A / R7 da janela de 2026-08-12

**Proveniência:** mesmo agente externo e mesma janela que produziram o
pacote em `../scripts/` (a reauditoria ADM que resultou no
**Erratum-02**). Os arquivos aqui estão **verbatim**, como o resto do
pacote — nenhum banner foi inserido no código; todo o estatuto está
neste README.

**Por que não estão em `../scripts/`.** O `../reports/execution_manifest.json`
declara a regra *"Only completed successful runs are used"* e lista os
estágios efetivamente executados (R6-B a R6-I). Nenhum dos três abaixo
está nessa lista: o R6-A não produziu veredito, e os dois R7 nunca
foram executados. Misturá-los com `scripts/` quebraria a regra do
próprio manifesto.

**Por que não estão em `auditoria/code/`.** Lá a convenção é
*script executado → `out/*.txt` → `docs/resultado_*.md`*. Colocá-los
naquela pasta sugeriria que integram a cascata executada, o que é
falso — e, no caso do primeiro, seria ativamente enganoso (ver abaixo).

---

## 1. `r6_cutoff_consistency.py` — princípio VIVO, números MORTOS

**O que é.** Auditoria (R6-A) da alegação de cutoff do Gate F-b.
Separa quatro coisas que não podem ser confundidas: os parâmetros
fundamentais da ação; as escalas Λ₃ construídas do parâmetro de massa
nu (Λ₃,g, Λ₃,f, Λ₃,eff); a massa tensorial cosmológica m_T²; e a
frequência canônica ω₀ do Gate F.

**O que continua válido — e é o mais importante do arquivo.** O gate
epistemológico (linhas ~265–283): sem uma escala não linear
independente passada por `--lambda-nonlinear`, o script se recusa a
concluir e imprime

```
R6-NONLINEAR: NOT RUN
R6-RIGOROUS: OPEN
```

Isto é, **um cálculo quadrático não pode determinar rigorosamente o
próprio cutoff não linear.** O princípio segue correto e é da mesma
família das regras que o cap. 02 vem acumulando.

> ⚠️ **NÃO RODAR COMO RESULTADO FÍSICO.** A linha 223 traz
> `known = {1.0: 12.0, 4.47: 7.4}` — os ω₀/H do Gate F entram
> **hardcoded**. Esses valores são do fantasma que o **Erratum-02**
> demonstrou ser artefato numérico (o Ċ contado duas vezes em
> `reduz_ponto`). O modo não sobreviveu à redução ADM/FJ. Portanto
> **toda razão ω₀/Λ calculada por este script é sobre um objeto que
> não existe.** Quem o executar obterá números bem formados e sem
> sentido físico.
> *Fonte: `auditoria/erratum_02_reducao_numerica.md`.*

## 2. `r7_class_reference.py` — VÁLIDO, nunca executado

Roda o **CLASS oficial, sem modificação**, e guarda o que um futuro
backend TDCP-CLASS teria de reproduzir no limite GR: C_ℓ^TT/EE/TE
(brutos e lensados), C_ℓ^φφ, H(z) e x_e(z). O cabeçalho é explícito:
*"This script does NOT implement TDCP. It is the regression/validation
anchor."*

Requer CLASS compilado e o wrapper `classy` no venv — não instalados
neste repositório. Escreve em `auditoria/code/out/`, então **precisa
ser invocado da raiz**, não desta pasta.

Serve de âncora de regressão: com a interação TDCP desligada, o backend
novo tem obrigação de voltar ao CLASS original. Ativo real, e não
falhou — apenas nunca chegou a rodar.

## 3. `r7_isw_from_transfer.py` — VÁLIDO como cross-check, nunca executado

Integrador independente de ISW tardio: recebe um `.npz` com
(k, η, Φ_B, Ψ_B, P_R, η₀), monta
`Δ_ℓ^ISW(k) = ∫dη (Φ_B′+Ψ_B′) j_ℓ[k(η₀−η)]` e depois
`C_ℓ^ISW = 4π ∫dln k P_R(k) |Δ_ℓ^ISW(k)|²`, por padrão em 2 ≤ ℓ ≤ 30.

Não é o C_ℓ^TT completo (sem Sachs–Wolfe primário, Doppler, picos
acústicos, reionização, polarização, lensing, nem a hierarquia de
fótons/neutrinos), e não substitui as correlações cruzadas do TT total.
A função dele sempre foi verificar independentemente o termo ISW que o
CLASS reportar.

**Ressalva do próprio autor, preservada:** a reconstrução de Bardeen a
partir do gauge plano de g (`Ψ_B = A + a(HB + Ḃ)`, `Φ_B = −aHB`) tem
sinal e normalização a validar no limite GR antes de qualquer uso
científico.

---

## 4. O estatuto dos dois R7, hoje — leia antes de planejar com eles

O relatório que acompanha estes arquivos é **anterior ao R-9…R-13** e
projeta como próximo passo o "R7 verdadeiro": 2 DOFs escalares +
matéria/radiação/fótons/neutrinos → Φ_B, Ψ_B → CLASS → C_ℓ, P(k).

**Esse plano está superado.** O R-10/R-11/R-12 estabeleceram que o
escalar métrico tem instabilidade de gradiente com **c_s² = −1 exato**
em r → 0 (teorema em forma fechada: `docs/resultado_r12b_teorema_cs2.md`),
e que a era instável **cobre a recombinação**. O cap. 09 do manuscrito
v2 é hoje intitulado *"o programa observacional: o que foi medido, e
por que o teste decisivo não é executável"* e afirma que **o CMB da F1
não é calculável linearmente** enquanto esse quadro valer. A previsão
de excesso ISW continua **retirada** desde o R-7.

Logo os dois R7 mudam de estatuto: deixam de ser "próxima etapa" e
passam a ser **infraestrutura condicional**, sob a rubrica que o
cap. 09 §6.4 já criou — *"Se um pipeline de C_ℓ um dia for
construído"*. Ficam aqui até que essa condição se realize.

*Docs relevantes: `docs/resultado_r10_consolidado.md`,
`docs/resultado_r11_nogo_gradiente.md`,
`docs/resultado_r12_instrumento_e_cs2.md`,
`docs/resultado_r12b_teorema_cs2.md`,
`manuscript-v2/09_programa_observacional.md`.*
