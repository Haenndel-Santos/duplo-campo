# 05 — O fundo do ramo finito

**Porte de `docs/resultado_ramo_finito.md` (2026-08-07, consequência
do Erratum-01; script `auditoria/code/ramo_dinamico_correto.py`), com
as notas de continuação numérica aprendidas em R-8b.**

## 1. A cúbica e as duas famílias de raiz

No ramo cinemático (cap. 04), r é fixado instante a instante pela
densidade: a combinação das duas Friedmann dá uma cúbica
m²M_eff²𝒲(r) = ρ com duas famílias:

- **ramo infinito**, r ~ √ρ̃ → ∞: produz ξ < 0 (lapso negativo no
  setor f) **no regime primordial**; descartado — ver a qualificação
  de época abaixo;
- **ramo finito**, r ~ β₁/ρ̃ → 0 no primordial: físico.

*Qualificação de época (R-10c):* a exclusão está **correta**, mas a
justificativa herdada do corpus ("dá ξ < 0", sem qualificar época)
não. A varredura de todas as raízes reais positivas da cúbica mostra
que essa raiz tem ξ < 0 só no primordial (ξ ≈ −9.4e3 em a = 0.001;
−8.38 em a = 0.1) e ξ > 0 a partir de a ≈ 1 (r = 2.358, ξ = +1.985),
logo **ξ cruza zero** em algum a ∈ (0.1, 1): uma história cosmológica
contínua nesse ramo teria de atravessar lapso nulo no setor f — ponto
singular. É *isso* que exclui o ramo, e não a patologia em toda época.
Fica registrado o achado colateral: existe uma **segunda solução
tardia viável** (r ≈ 2.23, ξ ≈ 2.23, H² > 0), que não se conecta ao
nosso primordial e que o repositório **nunca explorou** — o espaço de
soluções do fundo é maior do que a cascata assumiu. *Nível 2b; fonte:
`docs/resultado_r10c_saidas.md` Parte A.*

*Nota numérica (lição do R-8b):* a seleção de raiz "menor positiva"
só é segura com ρ̃ > 0; em extensões com vácuo escalar (ρ̃ efetivo
negativo) a seleção deve ser por **continuação** (raiz mais próxima
da anterior), sob pena de salto de ramo. *Fonte:
`docs/resultado_r8b_limite_mH0.md` §1.*

## 2. O que o ramo finito entrega

| | Resultado | Nível |
|---|---|---|
| Evolução estrutural | ṙ ≠ 0; r cresce de ~0 até r_∞ ≈ 0.33 (benchmark) | 2a |
| Primordial | r ∝ a³ ⟹ dr/dN = 3r ⟹ **ξ = 4r > 0** | 2a |
| Limite GR | H²/(ρ/3M_g²) = 1.0000 — exato | 2a |
| Lapso físico | ξ > 0 em toda a história | 2b (trilha) |
| Ponto fixo tardio | raiz da cúbica com ρ=0; universo acelera | 2a |
| Cosmologia | Ω_m ≈ 0.25 no "hoje" natural desse fundo | 2b |

Sobre o "hoje": cada fundo/família define o seu — o resultado acima
usa o ponto natural do benchmark original; a família do R-8b ancora
Ω_m(a₀) = 0.3 como escolha de dicionário. Comparações entre docs
devem citar a âncora. *Fontes: resultado_ramo_finito §1–2,
resultado_r8b §1.*

## 3. O mecanismo de separação estrutural — sem modulador

**É este o mecanismo que a v1 procurava.** No ramo finito, r evolui
porque ρ cai — sem β_n(φ₋), sem campo modulador, sem hipótese
adicional. A separação estrutural (r: ~0 → 0.33) é consequência da
constraint correta + Friedmann.

Isso reordenou a arquitetura (resultado_ramo_finito §6): a modulação
β₁(φ₋) deixou de ser necessidade e virou **extensão** — e a ordem de
teste passou a ser "primeiro β constantes, depois modulação". A
cascata pós-Erratum-02 executou exatamente essa ordem e fechou as duas
etapas, **com o alcance que o cap. 07 §4 declara e não mais que ele**:
com β constantes o setor escalar é são **na era tardia** (benchmark =
HR + espectadores) e tem **instabilidade de gradiente de classe em
r → 0** (c_s² = −1 exato, para qualquer forma-β;
`docs/resultado_r11_nogo_gradiente.md`). Com a modulação ligada, a
trajetória de rolagem/condensação existe, desloca ordem-1, pousa de
volta no ramo finito e mantém a saúde perturbativa na janela (Fase A +
R-7c/e) — janela que está inteira dentro da cobertura tardia da cascata
(a ≥ 100) e portanto não enuncia nada sobre r → 0; testada depois
*como saída* para a instabilidade, a modulação reprovou (R-10c).

## 4. O fundo dinâmico completo (rolagem e pouso)

A realização com φ₋ dinâmico (célula de referência g=2, m²=30,
v★=1): condensação dirige r de 0.031 a 0.498 (×16), deslocamento
ordem-1 dos dois ramos na janela a ∈ [225, 7086] (máx. 0.476), pouso
limpo de volta no ramo finito (r_fim = 0.4979; φ₋/v = 0.932 — âncoras
reproduzidas em três reintegrações independentes: original, Euler do
R-7c, Heun do R-7e). *Nível 2b; fronteira: uma trajetória, uma
célula.* *Notas de integrador declaradas:* as taxas armazenadas do
fundo Euler eram internamente inconsistentes ~1e-3 (detectado pelo
V-XREP-a; corrigido com taxas spline-consistentes) e o Heun atual tem
M0 = 3e-4 (cadeia rp de 1ª ordem) — suficiente para tudo que foi
medido; um integrador de 2ª ordem completo está na fila de
housekeeping. *Fontes: resultado_investigacao2_faseA.md,
resultado_r7_cascata §3, resultado_r7e_saude_interna §1.*
