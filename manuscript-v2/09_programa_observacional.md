# 09 — O programa observacional: o que já foi medido e o que decide

**O novo centro de gravidade.** Com o setor escalar são (cap. 07), a
viabilidade da F1 é uma pergunta exclusivamente observacional. Este
capítulo registra as duas primeiras sondas (R-8a/b), a predição que
emergiu delas, e o desenho do teste decisivo — com as decisões de
dicionário declaradas como decisões.

## 1. Sonda 1 — sub-horizonte quase-estático (R-8a)

μ(a,k) e a razão de lensing definidos como **razões de resposta**
bimétrico/GR com a mesma fonte e o mesmo fundo H(a) — construção em
que toda convenção e normalização cancela. Gates: o desvio de slip do
ramo GR escala como C/kh² (C ≈ 9.2 — física subdominante
quase-estática, medida e usada para **definir** a região confiável
kh ≥ 22); μ(kh=300) → 1 a 7×10⁻⁵; queda ∝ kh⁻¹·⁸⁶ ≈ kh⁻²
(termo líder (m·a/k)² presente).

**Resultado** (região confiável, duas eras, dois fundos): valores
centrais |μ−1|, |Σ_lente−1| ≤ 0.66% (kh=30, era de matéria), ≤ 0.06%
em kh ≥ 100. **Fraseado de precisão vinculante:** o piso de erro da
própria sonda é ~2% na fronteira da região confiável; o enunciado
forte é *"nenhum desvio acima do piso QS foi detectado"* — 0.66% é
valor central computado, não previsão de precisão. A janela
quase-horizonte (kh ≲ 22) fica **indecidida** por esta sonda (os
números crus de até 17% lá são contaminação da própria aproximação —
não são enunciado). *Nível 2b; a_eq interna = 0.686 (β₁=1) / 0.429
(β₁=4.47).* *Fontes: `docs/resultado_r8a_quase_estatico.md`,
`auditoria/code/out/r8a_quase_estatico_mu_sigma.txt`.*

Como kh = k/(aH) é adimensional, uma consequência independe de
dicionário: a janela de crescimento/lensing observável (RSD,
cisalhamento; k ≳ 0.01 h/Mpc ⟺ kh ≳ 30 hoje) está inteira na região
onde nenhum desvio foi detectado. **No benchmark, a F1 passa pelos
vínculos de crescimento sem ajuste.**

## 2. Sonda 2 — a massa tensorial é predição (R-8b)

Para testar o postulado do corpus m ~ 30–300 H₀, construiu-se a
família β_n → s·β_n com vácuo de φ₋ (U₀) mantendo o H tardio — o
dial canônico que varre a escala da interação preservando a forma-β
e a história de expansão. Dois resultados:

**(a) O fundo dobra.** r²𝒱_f(r) tem mínimo positivo (0.3 em r=1) na
forma-β do benchmark; com H tardio fixo isso trava s ≤ 3μH*²/(0.3
m_eff²) ≈ 6.2 — verificado analítica e numericamente (fold em
s ≈ 5.7). **O postulado 30–300 H₀ é inalcançável por dial contínuo
nesta família.** Alcançá-lo exige outra forma-β (𝒱_f com zero em r
finito) — uma escolha estrutural nova, que ademais implica ajuste
fino (U₀ < 0 grande, vácuo de φ₋ cancelando a energia da interação).
A v2 registra o postulado como **não incorporado**: se um dia for
adotado, entra como hipótese estrutural declarada, não como
parâmetro livre.

**(b) Dentro da família, a massa é cravada.** m_T/H₀ ∈ [2.26, 2.41]
em toda a família alcançável (s = 0.25 → 5.5, todos os membros com
saúde cinética verificada), pela fórmula do projeto
(`derivations/02_setor_tensorial_mT2.md`, avaliada hoje; a razão é
função da época: ~2.3 em a₀, ~3.5 no Λ profundo). Os desvios de
crescimento na janela observacional: ≤ 0.012% — trivialmente dentro
de qualquer limite. **A massa do gráviton deixou de ser parâmetro e
virou predição da família: m_T ≈ 2.3 H₀.** *Nível 2b; fronteiras:
forma-β do benchmark sob rescala uniforme; ramo conectado por
continuação; limites observacionais adotados como referência de
ordem de grandeza (declarado).* *Fontes:
`docs/resultado_r8b_limite_mH0.md`,
`auditoria/code/out/r8b_limite_mH0.txt`.*

## 3. O que NÃO há mais

A previsão de excesso ISW 2–8× em baixo-ℓ (e a "tensão" associada),
a dispersão p=0.44 e a localização da tensão-Akrami — todas da era do
sistema espúrio — estão **retiradas** (cap. 07 §4;
`docs/resultado_r7_cascata.md` §5). A F1 atual não possui nenhuma
assinatura observacional exótica *estabelecida*: está, até aqui,
observacionalmente **indistinguível e não-excluída**.

## 4. O teste decisivo (fila, com critérios a pré-declarar)

Com m_T ≈ 2.3 H₀ cravado, toda a física bimétrica distintiva vive no
**quase-horizonte**: kh ≲ 22 ⟺ escalas ≳ Gpc ⟺ baixo-ℓ do CMB, ISW,
os maiores modos de P(k). Exatamente a janela onde a sonda
quase-estática não alcança e onde o sistema dinâmico 2-DOF validado
(R-7a) é a ferramenta certa. O R-8 completo:

1. matéria/radiação perturbadas (γ, ν, b, CDM) acopladas ao sistema
   2-DOF corrigido; potenciais gauge-invariantes; *convenção de
   potenciais da v2 (Ψ temporal) com o mapa para a convenção da
   biblioteca de scripts anotado*;
2. C_ℓ^{TT,TE,EE} em baixo-ℓ, P(k) em escalas ≳ Gpc, lensing;
3. dicionário de épocas (`docs/r8_dicionario_epocas_opcoes.md`) como
   decisão declarada — os insumos que só o autor fixa: a forma-β
   (manter benchmark ⇒ m_T ≈ 2.3 H₀ é predição testável; mudar ⇒
   declarar a escolha estrutural), a massa física de φ₋ hoje, a
   normalização primordial;
4. critérios de falseamento pré-declarados ANTES da primeira rodada,
   como manda o cap. 02.

Ativos da v1 reavaliados: os números CLASS/ISW da v1 são
inutilizáveis (sistema espúrio); o bloco aritmético Vainshtein/PPN e
o formalismo HR do Anexo A permanecem como material de partida,
a re-derivar sob a maquinaria atual quando o R-8 completo os
alcançar.
