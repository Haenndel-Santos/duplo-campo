# No-Go Empírico: TDCP-F1 de β Constante no Ramo Finito

**Data:** 2026-08-07. Scripts: `escaneio_beta_ponto_fixo.py`,
`escaneio_hierarquia.py`, `caracteriza_mu01.py` (saídas em
`auditoria/code/out/`). Nível de evidência: **2b** (varredura com
fronteira declarada), com a estrutura apontando para um teorema (2a)
ainda não extraído.

## Enunciado

Na classe **TDCP-F1 com β_n constantes, ramo finito da constraint
corrigida** (Erratum 01), o setor escalar do par relativo é patológico
em **todos** os ~1500 pontos varridos do espaço de parâmetros:

| Região | Patologia |
|---|---|
| μ = M_f²/M_g² ∈ {0.3, 1, 3, 10, 30, 100}, toda a grade (β₁,β₂) | **taquião eterno** (σ/H ≈ 2.8–3.7 no ponto fixo) |
| μ = 0.1, células com σ=0 no ponto fixo (36) | **fantasma** (kN < 0 em k=1, todas as 36) |
| (β₀,β₄) ∈ [0.2,3]×[0.1,2] em μ=1 | taquião (225/225) |

## Fronteira declarada da varredura

β₁ ∈ [0.2, 2.0] (13 pts) × β₂ ∈ [−1.0, −0.05] (13 pts) ×
μ ∈ {0.1, 0.3, 1, 3, 10, 30, 100}, com β₀=1, β₄=0.5;
mais (β₀, β₄) ∈ [0.2,3]×[0.1,2] (15×15) em μ=1, β₁=1, β₂=−0.4;
k ∈ {1, 10} (fantasma), {1,10,100} (taquião). β₃=0 (F1). Fundo
congelado no transiente; **ponto fixo é exato** (quase-de Sitter,
ξ=r).

Não varrido: β₃≠0 (família F2), μ<0.1, k≪1 (fora do domínio confiável
da resposta), modulação β_n(φ) (é a v2), acoplamento de matéria não
mínimo.

## A estrutura que a varredura revela

1. **A direção μ→0 é de desacoplamento, não de cura.** Em μ=0.1 o
   taquião do ponto fixo desliga, mas sobra um fantasma de norma
   minúscula (−10⁻⁵ a −10⁻², crescendo com β₁). A patologia não sara:
   **enfraquece de acoplamento** conforme o setor f recua (μ→0 é o
   limite GR da literatura bimétrica, M_f/M_g→0). No limite exato o
   modo doente desacopla junto com todo o setor f — e a teoria deixa
   de ser bimétrica.
2. **Correção de prior (Nível 3 refutado):** a direção M_f≫M_g,
   apontada de memória como "cura padrão", é 100% taquiônica na
   varredura, com tendência que nunca aproxima zero (σ/H: 3.74→2.78
   de μ=1 a 100).
3. **O caráter transiente em μ=0.1 permanece interessante:** o
   taquião da era de matéria (σ/H~8→3) desligando rumo ao ponto fixo
   é a forma da narrativa da bifurcação — mas naquela região o ponto
   fixo abriga o fantasma, então a região não serve como alvo *com β
   constantes*.

## Ressalva técnica

O diagnóstico de fantasma (kN = v†Kv do autovetor QEP) **depende de
k** quando K, C, W não são simultaneamente diagonalizáveis (mesmo modo:
FANTASMA em k=1, LIMPA em k=10). É o diagnóstico estabelecido do
projeto (calibrado em GR pela D1), mas a afirmação invariante exige a
extração analítica — em curso (`estrutura_analitica_par.py`).

## O que segue vivo

- **A modulação β_n(φ₋) da v2** — nunca testada em perturbações
  (F′=F″=0 em tudo acima). O canal existe (Gate 2: resíduo
  −M_eff²m²p_φβ₁′ na constraint secundária) e a pergunta aberta é se
  a doença é de massa (modulação atua) ou cinética (não atua) — a
  extração analítica decide.
- **O fundo e o setor tensorial** — continuam saudáveis (limite GR
  exato, Higuchi 400/400, ṙ≠0). O no-go é do setor escalar.
- **Interpretação de condensação** — o taquião como a própria
  bifurcação, a estabilizar por ⟨φ₋⟩≠0. Depende da modulação.
