# Dicionário de Símbolos — TDCP v2

**Passo 0 do `plano_v2_reconstrucao.md`.** Documento normativo: nenhum
símbolo pode ter dois significados no corpus v2.

Verificação automatizada: `auditoria/code/verifica_simbolos.py`.

**Convenção de unidades:** naturais, ℏ=c=1. Dimensões expressas em
potências de massa (tempo = massa⁻¹).

---

## 1. Variáveis estruturais

| Símbolo | Significado | Dim. | Definido em |
|---|---|---|---|
| `g_{μν}` | métrica do setor visível (matéria acopla só a ela) | 0 | Ação |
| `f_{μν}` | métrica do setor estrutural | 0 | Ação |
| `𝒦` (`\mathcal K`) | `√(g⁻¹f)` — matriz raiz de HR | 0 | Ação |
| `e_n(𝒦)` | polinômios simétricos elementares | 0 | Ação |
| `r` | **`b/a`** — razão de fatores de escala | 0 | Fundo FLRW |
| `ξ` | **`N_f/N_g`** — razão de lapsos | 0 | Fundo FLRW |
| `r★` | raiz de `ℬ(r)=0` — ramo algébrico | 0 | Passo 3 |
| `ℬ(r)` | `β₁+2β₂r+β₃r²` — combinação da constraint de Bianchi | 0 | Passo 3 |

**`r` e `ξ` são intocáveis.** São as duas variáveis centrais, aparecem
em centenas de equações e em todas as âncoras D1–D8. Qualquer outro uso
renomeia.

## 2. Escalas e parâmetros

| Símbolo | Significado | Dim. | Nota |
|---|---|---|---|
| `M_g`, `M_f` | massas de Planck dos setores | 1 | |
| `M_eff` | `(M_g⁻²+M_f⁻²)^{-1/2}` | 1 | |
| `m` | escala de massa do potencial HR | 1 | nunca sozinho como massa física |
| `β_n(φ₋)` | coeficientes do potencial HR | 0 | **funções de φ₋ na v2** |
| `𝒱_g(r)` | `β₀+3β₁r+3β₂r²+β₃r³` — combinação do setor g | 0 | era `U(r)` na v1 |
| `𝒱_f(r)` | `β₄+3β₃r⁻¹+3β₂r⁻²+β₁r⁻³` — combinação do setor f | 0 | era `Ũ(r)`/`𝒰(r)` na v1 |
| `Λ₃` | escala de forte acoplamento | 1 | |

## 3. Campos escalares

| Símbolo | Significado | Dim. | Nota |
|---|---|---|---|
| `φ₁`, `φ₂` | par primordial correlacionado | 1 | Cap.1 usava `Φ₁,Φ₂` |
| `φ₊` | `(φ₁+φ₂)/√2` — modo comum | 1 | |
| `φ₋` | `(φ₁−φ₂)/√2` — modo diferencial | 1 | **é ele que modula β_n** — identificação normativa, NÃO derivada (G1-a) |
| `V(φ₊,φ₋)` | potencial dos campos primordiais | 4 | **explícito** — fecha achado A7 |
| `F(φ₋)` | modulação do potencial HR | 0 | era `F(φ)`/`F(χ)` |
| `δφ₊`, `δφ₋` | perturbações | 1 | |
| `χ` | **distância comóvel** | −1 | uso exclusivo na v2 — ver abaixo |

**`χ` é aposentado como campo.** A v1 usava `φ` e `χ` sem nunca dizer
se eram o mesmo campo (a única equivalência declarada é parentética:
Cap.14 §14.1, "campo estrutural φ (ou χ)"). Na v2 o campo que modula o
potencial HR **é** `φ₋`, o modo diferencial da bifurcação — é essa
identificação que costura a cadeia bifurcação → β_n → r★ → separação
estrutural.

**Flag epistêmica (G1-a, 2026-08-11):** essa identificação é
**normativa (decisão de dicionário), não derivada** — nenhum lugar do
corpus deriva que o modulador dos β_n é o modo diferencial primordial.
O levantamento completo da cadeia {Φ₋, φ, χ, φ₋-v2, σ, S, r}, com cada
ocorrência classificada (decreto/indefinida/distinta/derivada), está em
`gate1a_tabela_identidade.md`. Resultado: **zero elos de identidade
derivados** na cadeia inteira. O braço "modulador = φ₋" foi instanciado
por este decreto e testado pela v2: não cura o setor escalar
(`veredito_setor_escalar_final.md`); o G1-b mostrou que a patologia tem
projeção zero em δφ₋ (`resultado_investigacao1_ramo_algebrico.md` §3).

### Colisão nova: χ (campo) × χ (distância comóvel)

Esta **não estava na lista dos oito** levantada pela auditoria das 856
equações — foi encontrada pelo script do Gate 0, o que é um argumento
concreto a favor da verificação mecânica.

Na v1, `χ` é simultaneamente:

1. o campo escalar estrutural (Anexos B, E, F, H; Cap.13–14);
2. a **distância comóvel** nas integrais de Limber — `dχ`, `χ_max`,
   `χ_*`, `W(χ)`, `z(χ)` (Cap.23 §23.5, Cap.25 §25.5).

O uso (2) é notação universal em lensing fraco e **não deve ser
mexido**. Como a v2 já aposenta o uso (1) em favor de `φ₋`, a colisão
**se dissolve sozinha**: `χ` fica livre para significar distância
comóvel exclusivamente, que é o padrão da literatura.

O script distingue os dois por contexto — flagra `F(χ)`, `U(χ)`, `χ̇`,
`δχ`, `ρ_χ`, `S_χ`, `χ̄`, `χ(t)` (campo) e ignora `dχ`, `χ_max`,
`χ_*`, `W(χ)` (distância).

**Terceira vida de χ (achado do G1-a, 2026-08-11):** no rascunho
antigo do Cap.6 (§6.4, "Equação Escalar Efetiva"), `χ` nomeia ainda um
terceiro objeto — o **modo escalar efetivo reduzido** após eliminação
dos auxiliares (o que o Cap.6.2 chama de `σ`). Colisão histórica
(o Cap.6.2 revisa o Cap.6), mas catalogada. Relacionado: o rótulo
"**modo relativo**" também é sobrecarregado na v1 — nomeia `σ`
(Cap.6.2+), `S` (Cap.10/15+) e o modo **tensorial** h₋ (Anexo D §D.5).
Um corpus v2 precisa de três nomes distintos. Ver
`gate1a_tabela_identidade.md` §5.

## 4. Perturbações métricas

**Convenção fixada** (cosmológica padrão, tipo Ma–Bertschinger):

$$ds^2 = -(1+2\Psi)dt^2 + a^2(1-2\Phi)\delta_{ij}dx^idx^j$$

| Símbolo | Significado | Nota |
|---|---|---|
| `Ψ` | potencial **temporal** (newtoniano) | |
| `Φ` | potencial **espacial** (curvatura) | |
| `η_slip` | `Φ/Ψ` | =1 em GR sem anisotropic stress |
| `γ_PPN` | `Φ/Ψ` no regime solar | **é a mesma razão que η_slip** |
| `η_s` | variável do gauge síncrono | sempre subscrito, Ma–Bertschinger |
| `h_{ij}`, `ℓ_{ij}` | perturbações TT de g e f | |
| `ζ` | perturbação de curvatura comóvel | uso único |
| `ζ_b` | média ponderada bimétrica de Ψ's | era `ζ` no Cap.15 |

**Ganho não previsto:** com a convenção unificada, `γ_PPN` e `η_slip`
são **a mesma razão** (espacial/temporal), avaliada em regimes
diferentes. A v1 não podia ver isso porque Cap.18 e Cap.21 usavam
convenções invertidas. O vínculo de Cassini sobre γ e o observável
cosmológico η_slip passam a ser a mesma função — o que dá um teste
cruzado que a teoria não sabia que tinha.

## 5. Observáveis

| Símbolo | Significado | Nota |
|---|---|---|
| `μ(k,a)` | modificação de Poisson | **derivado**, nunca ansatz |
| `Σ(k,a)` | função de lentes | `Σ=(μ/2)(1+η_slip)` — v1 usava `η_slip⁻¹` |
| `G_eff` | `Gμ` | |
| `fσ₈` | taxa de crescimento × normalização | |
| `r_T` | razão tensor-escalar | era `r` no Cap.11 — **colisão grave** |
| `n_σ` | índice espectral do modo estrutural | previsão D7 |
| `D_V`, `D_A`, `D_C` | distâncias BAO | padrão |

## 6. Setor de estabilidade e screening

| Símbolo | Significado | Nota |
|---|---|---|
| `K_ij` | matriz cinética (romano) | Anexo C |
| `G_ij` | matriz de gradiente | Anexo C |
| `c_s²` | velocidade do som | autovalores de `K⁻¹G` |
| `m_T²` | massa do modo tensorial massivo | forma fechada: D2 |
| `π` | helicity-0 no limite de desacoplamento | Cap.20 |
| `ϕ` (`\varphi`) | flutuação de π | Cap.22 — **não confundir com φ** |
| `r_V` | raio de Vainshtein | |
| `Z`, `c₃`, `α_V` | coeficientes do galileon | **a derivar** — Passo 8 |
| `F_π/F_N` | razão de forças | sempre como razão |
| `S_iso` | modo de isocurvatura | era `S` — colide com ação |

**`𝒦` (script) ≠ `K` (romano).** A matriz raiz de HR e a matriz
cinética são objetos completamente diferentes e a distinção é apenas
tipográfica — risco alto. Exigir `\mathcal K` sempre para a primeira.

## 7. Símbolos com definição BLOQUEADA

| Símbolo | Situação |
|---|---|
| `η` | **bloqueado até o Gate 9.** Ver abaixo. |
| `Γ` | **bloqueado junto com η.** |

A v1 tem duas leis incompatíveis para η, e a incompatibilidade é
**dimensional**, não só de forma:

- `η̇ = Γ(H₁−H₂)²` ⟹ `[Γ] = massa⁻¹` (= tempo)
- `η̇ = Γχ̇²` ⟹ `[Γ] = massa⁻³`

Duas potências de massa de diferença. Nenhum `Γ` serve às duas, e
nenhuma das duas ocorrências jamais declarou sua dimensão.

Não se decide isso por decreto de notação: **o Passo 9 decide se η é
derivado (funcional de φ₋ acumulado) ou aposentado.** Até lá, o símbolo
não entra em nenhuma equação da v2. Se for aposentado, `η` e `Γ` ficam
livres para outros usos.

`Γ^μ_{νρ}` (Christoffel) é distinguível por índices e não conflita.

---

## 8. Renomeações obrigatórias (v1 → v2)

| v1 | v2 | Onde | Motivo |
|---|---|---|---|
| `r` (tensor-escalar) | `r_T` | Cap.11 §11.7 | colide com `r=b/a` |
| `ξ` (acoplamento em F) | `λ_F` | Cap.20 §20.2 | colide com `ξ=N_f/N_g` |
| `ξ` (correlação em P(k)) | `A_c` | Anexo K §K.6 | idem |
| `η` (modulação em P(k)) | `A_mod` | Anexo K §K.4 | colide com η estrutural |
| `U(r)` | `𝒱_g(r)` | Cap.14 §14.9 | colide com `U(φ)` |
| `Ũ(r)` / `𝒰(r)` | `𝒱_f(r)` | Cap.14, Anexo E | simetria com `𝒱_g` |
| `ζ` (média ponderada) | `ζ_b` | Cap.15 §15.2 | colide com ζ curvatura |
| `ζ = δρ/(ρ+p)` | escrever por extenso | Cap.10 | ocorrência única |
| `F(β_n,r)`, `𝓕` | usar a forma fechada da D2 | Cap.11, Cap.13 | placeholder desnecessário |
| `S` (isocurvatura) | `S_iso` | Cap.13, Cap.15 | colide com ação |
| `χ` (campo) | `φ₋` | todo o corpus | colide com χ = distância comóvel |
| `Φ/Ψ` (convenção solar) | inverter | Cap.20–22 | unificar com Cap.18 |

---

## Linha de base medida na v1

Rodando `verifica_simbolos.py` contra os 39 arquivos do manuscrito v1:

| Categoria | Tipos | Ocorrências |
|---|---|---|
| Colisões (dois significados) | 10 | 153 |
| Bloqueios (η/Γ, pendente do Gate 9) | 2 | 7 |
| Erros de álgebra rastreados | 2 | 5 |

**Validação cruzada:** o script encontrou o `Σ` com `η_slip` invertido
em **quatro** lugares (Cap.18 ×2, Cap.19, Cap.23) — exatamente as
quatro ocorrências que a auditoria manual havia registrado, obtidas por
caminho independente. E encontrou as **duas** leis de η, incluindo a do
Cap.1 §1.6 que só aparece na forma `\dot{\eta}` com chaves.

---

## Gate 0 — critério de passagem

- **Critério:** nenhum símbolo reservado usado com segundo significado
  no corpus v2; toda constante nova com dimensão declarada.
- **Nível exigido:** 1 (verificação mecânica).
- **Como testar:** `python auditoria/code/verifica_simbolos.py --alvo v2`
- **Se falhar:** renomear antes de escrever a próxima equação.

**Status atual:** o gate mede a v1 como linha de base e **não passa**
(esperado — a v1 é o corpus que gerou o dicionário). O gate se aplica
ao corpus v2, que ainda não existe. Quando `manuscript-v2/` for criado,
o script roda contra ele e o resultado esperado é zero violações.

**Limitação declarada:** o script detecta violações **conhecidas** — os
padrões catalogados acima. Ele não adivinha significado, porque
significado não está na sintaxe. Para colisões ainda não catalogadas,
use `--inventario`, que lista todo símbolo LaTeX por frequência e
número de arquivos, para revisão humana. Foi assim que a colisão do `χ`
apareceu.
