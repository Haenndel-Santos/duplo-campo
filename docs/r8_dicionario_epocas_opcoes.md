# R-8 — Dicionário de Épocas: Opções de Desenho (decisão do autor)

**Data:** 2026-08-12. Pré-requisito do R-8 (matéria/radiação + C_ℓ
sobre o sistema 2-DOF corrigido). Este doc só enumera opções e
custos; nenhum cálculo. Contexto: `docs/resultado_r7_cascata.md` §5-6.

## A decisão

O brinquedo atual é dust+Λ em unidades de código (m²M_eff² = ½,
H(100)=0.56, U″=0.3, k_c=45·H·a). Para confrontar C_ℓ/P(k) é preciso
fixar: (i) história de fundo com radiação; (ii) âncoras físicas
(H₀, Ω_m, z_eq); (iii) a escala de massa bimétrica m em unidades de
H₀; (iv) o papel de χ hoje (massa física de U″; espectador ou
dinâmico); (v) espectro primordial (normalização e transferência até
a era de matéria).

## Opção A — Porte mínimo do benchmark F1

Manter a estrutura F1 (β₀,β₂,β₄ fixos; β₁ o dial), adicionar ρ_r a⁻⁴
ao fundo e os setores perturbados (γ, ν, b, CDM) na L2; ancorar
r_∞ → Λ_eff = Λ_obs e m na faixa postulada pelo corpus (30–300 H₀ —
lembrar: é POSTULADO de desenho, não derivação; declarar).

- **Custo:** alto (hierarquia de Boltzmann completa na nossa
  maquinaria; validação V-XREP em cada era).
- **Entrega:** C_ℓ^{TT,TE,EE} e P(k) da F1 propriamente dita.
- **Risco:** construir tudo antes de saber se o setor escalar 2-DOF
  sequer produz desvio observável (pode ser ΛCDM-indistinguível no
  linear — resultado publicável, mas caro).

## Opção B — Alinhamento com a literatura bimétrica

Adotar a parametrização do "minimal bimetric model" (B₁-dominado,
Könnig–Amendola et al.) para o setor métrico e montar o χ da F1 por
cima. Ganha comparabilidade direta com vínculos publicados (incl.
Akrami et al.) e as ferramentas conceituais da literatura de
perturbações bimétricas.

- **Custo:** médio-alto (tradução de convenções + mesma hierarquia).
- **Entrega:** confronto direto com números publicados; menos
  "nosso", mais calibrável.
- **Risco:** a F1 não é exatamente o minimal model (χ-modulação);
  o mapeamento reintroduz decisões de identificação.

## Opção C — Estágio quase-estático primeiro (recomendada como 1º passo)

Antes da hierarquia completa: no regime sub-horizonte/quase-estático,
derivar μ(a,k) ≡ G_eff/G e Σ(a,k) (lensing) do sistema 2-DOF +
matéria não-perturbada→perturbada na aproximação quase-estática.
Compara com vínculos de crescimento (fσ₈, RSD) e responde barato à
pergunta decisiva: **o desvio de ΛCDM é O(quanto) e em que janela?**

- **Custo:** baixo (álgebra sobre as matrizes já validadas + 1
  script; sem Boltzmann).
- **Entrega:** o "tamanho do alvo" — se μ,Σ ≈ 1 em toda a janela
  observável, o C_ℓ completo vira formalidade e a F1 é viável-mas-
  indistinguível no linear; se há desvio, ele dimensiona o R-8 e
  escolhe entre A/B com dados.
- **Risco:** a aproximação quase-estática precisa de justificativa
  na banda kh ~ O(1) (checável com a maquinaria de evolução real que
  já temos — o próprio R-7a/M3 dá a dispersão).

## Recomendação

**C → depois A** (com B como calibração pontual se o desvio de C for
não-trivial). Racional: C custa ~1 sessão e transforma a decisão A/B
de aposta em escolha informada; e o resultado de C já é enunciado de
paper ("no linear sub-horizonte, a F1 corrigida prevê
μ−1, Σ−1 = ...").

## Insumos que só o autor pode fixar (qualquer opção)

1. m/H₀ (manter o postulado 30–300 H₀ do corpus ou re-derivar?);
2. massa física de χ hoje (U″=0.3 em unidades de código ↔ quê?) e
   se χ terminou de rolar antes de z_eq (o pouso em unidades reais);
3. β's: manter o par benchmark (β₁=1, 4.47) ou varrer;
4. normalização primordial (As, ns padrão? inflaton = χ ou externo?).
