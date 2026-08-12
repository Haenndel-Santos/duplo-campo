# Parecer — Astronomia Observacional

**Escopo:** avaliação independente da TDCP/F1 do ponto de vista de um
observador (surveys, CMB, lente fraca, cosmologia de precisão), com
base no estado do repositório **posterior ao Erratum-02 (2026-08-12)**.
Leitura: `manuscript-v2/09_programa_observacional.md`,
`manuscript-v2/01_tese.md`, `manuscript-v2/07_setor_escalar.md`,
`docs/resultado_r8a_quase_estatico.md`, `docs/resultado_r8b_limite_mH0.md`,
`docs/resultado_r7_cascata.md` §4–5, `docs/r8_dicionario_epocas_opcoes.md`,
`docs/resultado_ramo_finito.md`.

**Convenção deste parecer:** "[repo]" = derivado/registrado no
repositório; "[opinião]" = avaliação minha; "[verificar]" = número
externo citado de memória ou de resumo de busca, a conferir na fonte
primária antes de ir para o manuscrito. Nenhum número anterior a
2026-08-12 é usado como corrente (filtro de supersessão de
`docs/resultado_r7_cascata.md` §4).

---

## Resumo executivo

1. A retirada do excesso ISW foi correta e é o ato mais saudável do
   programa; o custo é que a F1 hoje **não tem nenhuma assinatura
   exótica estabelecida** — está observacionalmente indistinguível e
   não-excluída [repo].
2. O resultado sub-horizonte (|μ−1|, |Σ−1| ≤ 0.66%; ≤ 0.012% na janela
   z ≤ 1) é **folgado por 1–2 ordens** frente aos melhores vínculos
   atuais (DESI+CMB+DES-Y3: σ(μ₀) ≈ 0.22, σ(Σ₀) ≈ 0.047) [repo+externo].
3. Mas o piso de erro **da própria sonda** é ~2%, maior que a precisão
   que Stage-IV terá em Σ (~1–2%) [opinião]: em ~5 anos o dado será mais
   afiado que a teoria. O gargalo é teórico, não observacional.
4. A janela decisiva declarada (kh ≲ 22 ⟺ λ ≳ 1.2 Gpc ⟺ ℓ ≲ ~20) é
   **exatamente a região onde a variância cósmica é uma parede**: a
   amplitude de banda em 2 ≤ ℓ ≤ 20 não é mensurável melhor que ~7–8%,
   nunca, por nenhum experimento [opinião, cálculo abaixo].
5. Consequência dura: para ser falseável em baixo-ℓ TT, a F1 precisa
   prever um efeito de **fator ~2 no ISW** — precisamente a ordem do
   que acabou de ser retirado como artefato [opinião].
6. Achado mais importante deste parecer: **kh é função de época**. O
   critério kh ≲ 22 avaliado em z ≈ 1100 cobre k ≲ 0.14 h/Mpc, isto é,
   **ℓ ≲ ~1300** — todo o CMB primário. A sonda R-8a só sondou z ≲ 10
   [opinião, §Fracos 1].
7. E o próprio R-8a registra que **os desvios crescem quando r decresce**
   (era de matéria) [repo] — a extrapolação aponta para o regime que
   nunca foi testado.
8. m_T ≈ 2.3 H₀ é consistente com o que a literatura bimétrica já
   esperava (m_FP > 1.2 H₀ a 90%, Lüben et al. 2021) [verificar]: é
   **checagem de consistência, não discriminante**; e a família fixa
   H(z) por construção, o que apaga a única alavanca de fundo.
9. Pendências observacionais nunca tocadas pelo repo: **isocurvatura**
   (há um segundo campo primordial!), **setor tensorial B-mode** (m_T/H
   é O(2–3.5) em toda a história), Σm_ν, e o vínculo de lente do CMB.
10. Recomendação de dicionário: **C (feito) → B como gate de validação
    externa obrigatório → A**. Sem reproduzir um resultado bimétrico
    publicado, nenhum C_ℓ próprio deve ser afirmado.

---

## Pontos fortes

**F1. A retirada do excesso ISW é conduta exemplar e observacionalmente
correta.**
`docs/resultado_r7_cascata.md` §5 e `manuscript-v2/07_setor_escalar.md`
§4 retiram a previsão de 2–8× em baixo-ℓ, a dispersão p=0.44 e a
localização da tensão-Akrami [repo]. Do ponto de vista de observador,
isto vale mais que qualquer previsão: uma comunidade que já viu
dezenas de "tensões" evaporarem lê a retirada auto-imposta como sinal
de calibração interna. Recomendo que o manuscrito **abra** com isto,
não que o esconda no cap. 07.

**F2. O fraseado de precisão do R-8a é o correto e deve virar padrão da
casa.**
"Nenhum desvio acima do piso QS (~2%) foi detectado" — com 0.66%
declarado como *valor central computado*, não como previsão de precisão
(`docs/resultado_r8a_quase_estatico.md` §2) [repo]. Esta é exatamente a
distinção que separa um resultado de survey de um press release. Boa
prática; mantenha em todo o cap. 09.

**F3. A construção μ/Σ como razão de resposta bimétrico/GR é
metodologicamente limpa.**
Mesma fonte, mesmo H(a), toda normalização cancela
(`docs/resultado_r8a_quase_estatico.md` §1) [repo]. Isso torna o
resultado imune à classe de bug que gerou o Erratum-02 (normalização) —
e é o que permite comparar com μ₀/Σ₀ da literatura sem tradução de
convenção.

**F4. A janela de crescimento observável está, por construção, na região
QS-confiável — e isso é verificável sem dicionário.**
kh = k/(aH) é adimensional; RSD e cisalhamento vivem em k ≳ 0.01 h/Mpc
⟺ kh ≳ 30 hoje (`manuscript-v2/09_programa_observacional.md` §1) [repo].
Confirmo a aritmética: com c/H₀ = 4448 Mpc (h = 0.674), k = 0.01 h/Mpc
= 6.7×10⁻³ Mpc⁻¹ ⟹ kh₀ = 30 [opinião]. O argumento é robusto e
independe dos 4 insumos do autor. É a única afirmação observacional que
a F1 pode fazer **hoje** sem fechar o dicionário.

**F5. A folga frente aos vínculos reais é grande, e vale citar os
números certos.**
Vínculos atuais de gravidade modificada (parametrização μ₀/Σ₀ com
μ(a) = 1 + μ₀ Ω_DE(a)/Ω_DE,0):
- DESI FS+BAO+BBN: μ₀ = 0.11 (+0.45/−0.54) [externo];
- DESI FS+BAO+CMB+DES-Y3 3×2pt: **μ₀ = 0.04 ± 0.22; Σ₀ = 0.044 ± 0.047**
  [externo: Ishak et al., *Modified gravity constraints from the full
  shape modeling of clustering measurements from DESI 2024*,
  JCAP 09 (2025) 053, arXiv:2411.12026].
A F1 prevê |μ−1| ≤ 0.66% (kh = 30) e ≤ 0.012% na janela z ≤ 1,
k = 0.05–0.15 h/Mpc [repo, R-8a §2 / R-8b §2]. Ou seja: ~33× abaixo da
sensibilidade atual em μ e ~7× em Σ. **A F1 passa sem ajuste, e passará
com folga também em Stage-IV.** Isto é um ponto forte de *viabilidade*
— e um ponto fraco de *testabilidade* (ver Fracos F-4).

**F6. m_T ≈ 2.3 H₀ satisfaz Higuchi com margem em toda a história, e o
fundo é primordialmente GR-exato.**
m_T²/H² → 12 no primordial, independente dos parâmetros
(`docs/resultado_ramo_finito.md` §3), ~5.1–5.8 hoje (m_T/H₀ ∈
[2.26, 2.41], R-8b §2), ~12 no Λ profundo [repo]. Higuchi (m_T² ≥ 2H²)
folgado por fator 2.5–6 sempre. Como corolário observacional que o repo
não explicita: **m_T/H ∈ [~2.3, ~3.5] em TODA a história cósmica**
[opinião]. E o limite GR primordial exato
(H²/(ρ/3M_g²) = 1.0000, `docs/resultado_ramo_finito.md` §1) protege
BBN automaticamente — relevante porque existe vínculo BBN publicado
para bimétricas [externo: arXiv:2106.09030, *Constraints on bimetric
gravity from Big Bang nucleosynthesis*] [verificar].

**F7. O R-8b converteu um postulado em resultado — e isso é o padrão
correto.**
O postulado m ~ 30–300 H₀ do corpus foi mostrado inalcançável por dial
contínuo na família do benchmark (fold em s ≈ 5.7; s_max ≈ 6.2
analítico) [repo, R-8b §2a]. Matar um postulado por obstrução estrutural
— e não por dados — é exatamente o tipo de resultado que sobrevive à
revisão por pares.

**F8. Consistência com a literatura bimétrica no valor de m_FP.**
m_T ≈ 2.3 H₀ ≈ 3.3×10⁻³³ eV (usando H₀ = 1.45×10⁻³³ eV para h = 0.68)
[opinião, aritmética]. A literatura bimétrica encontra um **limite
inferior** m_FP ≳ 1.2 H₀ (90% cred.), ≈ 2.5h×10⁻³³ eV, de ajustes
CMB/BAO/SNIa [externo: Lüben, Schmidt-May, Smirnov, *Constraints on
bimetric gravity. Part II: Observational constraints*, JCAP 05 (2021)
002, arXiv:2101.08795] [verificar]. A F1 cai **dentro** da faixa
favorecida. É consistência genuína — leia-se também Fracos F-6.

---

## Pontos fracos e riscos

**W1. [CRÍTICO] "Sub-horizonte consistente com GR" é uma afirmação sobre
z ≲ 10, e está sendo lida como se valesse para o CMB. Não vale.**

kh = k/(aH) **depende da época**. Na era de matéria,
kh(a)/kh₀ = H₀/(aH) ≈ √(a/Ω_m). Consequências aritméticas [opinião]:

| onde | kh = 22 corresponde a | projeta em |
|---|---|---|
| hoje (a = 1) | k = 5.1×10⁻³ Mpc⁻¹ = 3.6×10⁻³ h/Mpc, λ = 1.22 Gpc | ℓ ≈ 6–17 (ISW tardio, χ = 1.2–3.3 Gpc); ℓ ≈ 71 se projetado de χ_* |
| na recombinação (z ≈ 1100, 1/aH ≈ 230 Mpc) | **k ≈ 0.096 Mpc⁻¹ = 0.14 h/Mpc** | **ℓ = kχ_* ≈ 1330** |

Isto é, os modos que hoje têm kh₀ ≈ 430 (profundamente "seguros" pela
sonda R-8a) **estavam dentro da janela indecidida kh ≲ 22 na época em
que o CMB foi formado.** A grade da sonda vai de a = 0.1 a 75000 em
unidades de código com a_eq(matéria–Λ) = 0.686/0.429
(`docs/resultado_r8a_quase_estatico.md` §2) — ou seja, a "era de
matéria" mais antiga sondada corresponde a z ≈ 8 em unidades físicas
[opinião, com Ω_m = 0.3 ⟹ a_eq,mΛ = 0.754]. **Nada foi testado acima de
z ~ 10, e o modelo sequer tem era de radiação** (o dicionário Opção A
ainda precisa *adicionar* ρ_r a⁻⁴, `docs/r8_dicionario_epocas_opcoes.md`).

Agravante, e vem do próprio repo: o R-8a registra que os **desvios
crescem para a era de matéria** — "r pequeno → setor-f responde mais"
(`docs/resultado_r8a_quase_estatico.md` §2) [repo]. A tendência medida
aponta na direção errada para uma extrapolação tranquilizadora.

Extrapolação de ordem de grandeza [opinião, a ser refutada ou
confirmada pelo R-8 completo]: com |μ−1| ≈ C·(m/H)²/kh² e m/H ≈ 3.5,
o primeiro pico acústico (k ≈ 0.05 h/Mpc ⟹ kh ≈ 8 na recombinação)
cairia em vários por cento. **Planck mede as alturas dos picos em
0.1–0.3%.** Ou a modulação desliga com r → 0 (e é preciso *mostrar*
isso, não presumir), ou a F1 já está excluída pelo CMB.

**Ação exigida:** o cap. 09 §4 deve dizer explicitamente que a validade
do "consistente com GR" é **z ≲ 10 e k ≳ 0.01 h/Mpc**, e listar o
regime (z ≳ 100, kh ≲ 22 naquela época) como *não testado e de alto
risco*, não como "janela onde a física distintiva vive".

**W2. A cadeia "kh ≲ 22 ⟺ escalas ≳ Gpc ⟺ baixo-ℓ" tem um elo que não é
equivalência.**
As duas primeiras são equivalentes (confirmo: k = 22H₀ ⟹ λ = 1.22 Gpc
comóvel) [opinião]. A terceira não: o ℓ que um dado k ocupa depende da
distância comóvel até **onde a física age** (ℓ ≈ kχ). Para ISW tardio,
ℓ ≈ 6–17; projetado da última superfície de espalhamento, ℓ ≈ 71
[opinião]. Isto é *bom* para a teoria (mais modos ⟹ menos variância
cósmica: a banda 30 ≤ ℓ ≤ 70 tem 4141 modos, σ_A/A ≈ 2.2% com f_sky = 1,
contra 6.8% em 2 ≤ ℓ ≤ 20). Mas exige que o pipeline **não** se
pré-restrinja a ℓ ≤ 20.

**W3. [CRÍTICO] A variância cósmica é uma parede, e o alvo declarado
está atrás dela.**
Com σ(C_ℓ)/C_ℓ = √(2/((2ℓ+1)f_sky)) [opinião, cálculo padrão]:

| ℓ | erro por multipolo (f_sky = 1) |
|---|---|
| 2 | 63% |
| 5 | 43% |
| 10 | 31% |
| 20 | 22% |
| 30 | 18% |

Amplitude de banda (N_modos = Σ(2ℓ+1) = (ℓ_max+1)² − 4;
σ_A/A = √(2/N)/√f_sky):

| banda | N_modos | σ_A/A (f_sky = 0.7) |
|---|---|---|
| 2 ≤ ℓ ≤ 10 | 117 | **15.6%** |
| 2 ≤ ℓ ≤ 20 | 437 | **8.1%** |
| 2 ≤ ℓ ≤ 30 | 957 | **5.5%** |

Como o ISW tardio contribui O(10%) da potência TT em ℓ ≲ 10
[verificar], um efeito puramente ISW só cruza 3σ se
ΔISW/ISW ≳ 1.5 — **fator ~2.5 no ISW**. É *exatamente* a ordem do
"2–8×" retirado. Traduzindo: fora daquele artefato, a F1 não tem
nenhuma chance de ser vista em baixo-ℓ TT — e nem terá, porque Planck
já é limitado por variância cósmica em TT até ℓ ~ 1600. **LiteBIRD e
CMB-S4 não melhoram TT em ℓ ≲ 20 nem um pouco** [externo/opinião;
cf. arXiv:2411.03459, JCAP 06 (2025) 035, que diz explicitamente que a
variância cósmica em TT já foi atingida por Planck e que o ganho de
LiteBIRD é em **E-modes** de grande escala].

**W4. Escalas de Gpc em P(k) são inacessíveis por LSS single-tracer —
demonstravelmente.**
N_modos(k) = V k²Δk/(2π²). Em k = 10⁻³ h/Mpc, com Δk = k e um volume
DESI-like V ≈ 20 (Gpc/h)³: N ≈ 1 modo, σ(P)/P ≈ 141% [opinião].
Para chegar a 10% em P(k) nessa escala seria preciso
V ≈ 3.9×10³ (Gpc/h)³ ≈ 1.1×10⁴ Gpc³ — **o volume do universo
observável inteiro** [opinião]. Portanto: o item 2 da fila do cap. 09
("P(k) em escalas ≳ Gpc") não é um teste; é uma impossibilidade, salvo
por multi-tracer (ver Propostas P5).

**W5. O piso de erro da teoria (~2%) já é pior que a precisão futura do
dado (~1–2% em Σ).**
Hoje: σ(Σ₀) ≈ 0.047 [externo, DESI+CMB+DES-Y3]. Stage-IV (Euclid +
Rubin + CMB lensing) deve chegar a σ(Σ₀) ~ 0.01–0.02 e σ(μ₀) ~ 0.03–0.05
[verificar; cf. Euclid Collaboration, Blanchard et al., A&A 642, A191
(2020), arXiv:1910.09273]. O R-8a declara honestamente piso ~2% na
fronteira kh = 22 [repo]. **Em ~2030 a teoria será o elo fraco.** Sem
uma sonda de ordem seguinte (QS-NLO ou dinâmica completa) com erro
declarado ≤ 0.5%, a F1 não terá o que dizer quando o dado chegar.

**W6. m_T ≈ 2.3 H₀ tem risco sério de ser infalsificável na prática.**
Quatro razões [opinião]:
- **(a) A família apaga a própria alavanca.** U₀ é resolvido por s para
  manter o H tardio do benchmark (`docs/resultado_r8b_limite_mH0.md`
  §1) [repo]. Um parâmetro ajustado para eliminar a diferença
  observável em H(z) não pode depois ser reivindicado como testável via
  H(z). Isso é ajuste, ainda que declarado.
- **(b) A escala é 10 ordens de grandeza abaixo de qualquer limite
  direto.** m_T ≈ 3.3×10⁻³³ eV vs. LVK/GWTC-3: m_g < 1.27×10⁻²³ eV
  [verificar]. Dispersão em banda LIGO: |c_g/c − 1| ~ (m/ω)²/2 ~ 10⁻⁴⁰ —
  contra o vínculo GW170817/GRB170817A de ~5×10⁻¹⁶ [externo, PRL 119,
  251301 (2017)]. **Nenhum detector de ondas gravitacionais jamais verá
  isso**; oscilações de gráviton têm comprimento cosmológico.
- **(c) Não há barra de erro teórica.** m_T/H₀ ∈ [2.26, 2.41] é a
  dispersão ao longo de **um** dial (rescala uniforme dos β_n), com a
  forma-β congelada [repo]. Sob mudança de forma-β o número muda — e o
  próprio R-8b diz que outra forma-β é necessária se o postulado
  30–300 H₀ for perseguido. Sem varrer a forma-β, "2.3" é um número, não
  uma predição.
- **(d) O número não é distintivo.** m_FP ~ O(H₀) é o resultado
  *genérico* de qualquer bimétrica auto-acelerada — é o que faz o termo
  de interação funcionar como Λ. Ver F8. Concordar com a expectativa
  genérica da classe é consistência, não discriminação.

**W7. Ω_m ≈ 0.25 no fundo original está excluído, e o manuscrito o
chama de "razoável".**
`docs/resultado_ramo_finito.md` §1 registra "Ω_m ≈ 0.25 hoje, universo
acelerando — **razoável**" [repo]. Não é razoável: Planck 2018 dá
Ω_m = 0.3153 ± 0.0073 [externo, A&A 641 A6, arXiv:1807.06209]; DESI DR2
BAO+CMB fica em ~0.30. 0.25 está a **~8–9σ** [opinião]. A família R-8b
já reancora corretamente em Ω_m(a₀) = 0.3 [repo], mas o manuscrito
carrega as duas âncoras sem hierarquia. **Ação:** marcar o Ω_m = 0.25 do
`resultado_ramo_finito.md` como *superado pela reancoragem R-8b* na
tabela de supersessão, ou o primeiro referee vai usá-lo para fechar o
paper.

**W8. Isocurvatura: um segundo campo primordial e zero linhas sobre o
assunto.**
A TDCP postula **dois** graus de liberdade primordiais correlacionados
(`manuscript-v2/01_tese.md`) e o setor escalar corrigido tem um
espectador δφ₋ com ω² = k²/a² + U″ que sobrevive
(`manuscript-v2/07_setor_escalar.md` Ato 3) [repo]. Isso é a definição
de um candidato a modo de isocurvatura. Planck limita isocurvatura CDI
não-correlacionada a β_iso < ~0.038 (95%) e, no caso totalmente
correlacionado, a nível ~10⁻³ [verificar; Planck 2018 X, arXiv:1807.06211].
Este é, na minha avaliação, **o vínculo mais provável de matar ou
validar a TDCP**, e é o único que ataca a hipótese *conceitual* (dois
campos), não só a implementação bimétrica. O repo não o menciona em
lugar algum.

**W9. O setor tensorial nunca foi levado a B-modes — e é onde m_T/H ~ O(1)
tem consequência.**
Com m_T/H ∈ [2.3, 3.5] em toda a história [derivado de repo, ver F6],
o modo tensorial massivo **nunca** está no regime "massa desprezível
frente ao horizonte": a transição k = m_T a ocorre sempre em kh ≈ 2–3.5,
isto é, sempre no cruzamento de horizonte [opinião]. A física tensorial
distintiva vive, portanto, na *mesma* janela quase-horizonte que a
escalar — mas com um canal observacional que o repo ignora: o ângulo de
mistura entre o gráviton sem massa (que carrega as ondas primordiais
congeladas) e o massivo é fixado pelos mesmos β_n e por r = b/a, e
suprime a amplitude tensorial observada em relação a r inflacionário
[opinião]. LiteBIRD mira σ(r) ~ 0.001 [verificar]. **Isto é uma previsão
potencialmente afiada que está sobre a mesa e não foi colhida.**

**W10. Risco de reincidência numérica: dois erratums, um deles inventou
uma previsão observacional.**
`manuscript-v2/07_setor_escalar.md` Ato 2: um bug de 1.4–6.1%, *suave*
ao longo da trilha, convergente em resolução, gerou fantasma, banda e
o ISW 2–8× [repo]. Um pipeline de C_ℓ é 10–100× mais complexo que a
redução que falhou. **Nenhuma afirmação observacional deve sair do R-8
completo antes de reproduzir um resultado bimétrico publicado.** Ver
Propostas P1.

**W11. Um sinal externo emergente que precisa ser monitorado (e pode ser
oportunidade ou sentença).**
A busca retornou um trabalho de 2026 alegando *evidência de desvio na
deflexão gravitacional da luz em relação à RG em escalas cosmológicas*,
com KiDS-Legacy + lente do CMB [externo: arXiv:2602.03110] [verificar —
li apenas o título; **não** cite sem ler]. Se um sinal em Σ se
consolidar em escalas de dezenas–centenas de Mpc, a F1 tem
|Σ−1| ≤ 0.66% ali [repo] e **não o explica** — seria uma refutação
suave. Ao mesmo tempo, o quadro S8 se moveu: KiDS-Legacy dá
S8 = 0.815 (+0.016/−0.021), a 0.73σ de Planck [externo, arXiv:2503.19442],
enquanto DES-Y6 permanece baixo [verificar]. **A tensão S8 não é mais um
alvo confiável para a TDCP mirar.**

---

## Propostas de modelagem/observação (priorizadas)

**P1 — [PRIORIDADE MÁXIMA] Gate de validação externa antes de qualquer
C_ℓ próprio.**
Dicionário: **Opção B como gate obrigatório entre C (feito) e A** —
não como alternativa a A. Concretamente: implementar o *minimal
bimetric model* (β₁-dominado) na maquinaria da casa e reproduzir
μ(a,k)/Σ(a,k) e/ou C_ℓ^TT publicados da literatura bimétrica dentro de
**≤ 2%** em 2 ≤ ℓ ≤ 200. Critério pré-declarado, saída versionada,
gate nomeado (sugiro **V-EXT**). Racional: o Erratum-02 mostrou que o
pipeline interno pode convergir lindamente para o objeto errado; a
única defesa é um alvo externo. Custo: ~1 sessão a mais que a Opção A
crua. Retorno: transforma o R-8 de aposta em resultado publicável.
*Referência de calibração:* Könnig–Amendola et al. e
Lüben–Schmidt-May–Smirnov (arXiv:2101.08795) [verificar edição exata].

**P2 — [ALTA] Fechar o buraco de época do W1 antes de qualquer C_ℓ.**
Rodar a mesma sonda QS do R-8a — sem mudar nada além do fundo — em
**z = 30, 300, 1100** (após adicionar ρ_r a⁻⁴ ao fundo), em
kh = 5, 10, 22, 50, 100. Pergunta única e pré-declarada: **|μ−1| e
|Σ−1| crescem, saturam ou desligam quando r → 0?** Custo baixíssimo
(é o script existente com uma grade nova). Critério de falha:
se |μ−1| > 1% em kh ≥ 22 na recombinação, a F1 está em conflito direto
com as alturas dos picos de Planck (medidas a 0.1–0.3%) e isso precisa
ser sabido **antes** de investir na hierarquia de Boltzmann. Este é o
item de maior relação valor/custo de toda a fila, na minha opinião.

**P3 — [ALTA] Converter m_T ≈ 2.3 H₀ em predição com barra de erro.**
Varrer a **forma-β** (não só a rescala uniforme s) em ≥ 2 dimensões,
mantendo fixos: H(z) de ΛCDM dentro de 1%, Ω_m(a₀) = 0.315,
Ω_m h² = 0.1430, e saúde cinética. Entregar o **intervalo de
m_T/H₀ compatível com a família viável**, não um valor. Se sair
m_T/H₀ = 2.3 ± 0.2, é predição e pode ser confrontada com o limite
inferior bimétrico (m_FP ≳ 1.2 H₀). Se sair [1.5, 10], deve ser
declarado como tal, e "m_T ≈ 2.3 H₀ é predição" sai do cap. 01 e do
cap. 09.

**P4 — [ALTA] Abrir o canal tensorial/B-mode (W9).**
Calcular o ângulo de mistura g–f no setor tensorial ao longo da
história e a supressão resultante de r_observado/r_inflacionário.
Alvos: banda de reionização ℓ ≈ 2–10 e banda de recombinação ℓ ≈ 80.
Sensibilidade-alvo: **LiteBIRD σ(r) ≲ 0.001** [verificar]; CMB-S4 com
delensing na mesma faixa. Este é o único canal que consegue ser
**cosmic-variance-favorável e simultaneamente sensível à massa do
gráviton**, porque B-modes primordiais têm fundo nulo em ΛCDM sem
tensores. Se a F1 previr uma supressão de r de ~10% ou mais, isso é uma
previsão de verdade, no ℓ certo, com um instrumento voando.

**P5 — [MÉDIA] Trocar "P(k) em escalas ≳ Gpc" por multi-tracer de
escala ultra-grande.**
Dado o W4, o único caminho para k ~ 10⁻³ h/Mpc é a supressão de
variância cósmica por multi-tracer (razão entre traçadores de biases
diferentes no mesmo volume). Alvos concretos: SKA1/2 HI + contínuo, e
SKA×Euclid/Rubin, com forecasts de σ(f_NL) ~ 1–3 [verificar]. O produto
que a F1 deve entregar para entrar nesse jogo é uma **assinatura em
bias efetivo dependente de escala** ou um Σ(k) em k ≲ 0.005 h/Mpc, não
um P(k) absoluto. Reescrever o cap. 09 §4 item 2 nesses termos.

**P6 — [MÉDIA] ISW por correlação cruzada, não por TT.**
A correlação cruzada CMB×LSS isola a componente ISW e escapa
parcialmente da parede de variância cósmica de W3. Estado atual:
detecção Planck×LSS a ~3–4σ [verificar; Planck 2015 XXI, A&A 594 A21],
ou seja σ(A_ISW)/A_ISW ~ 25–35%. Com Euclid/Rubin/DESI: ~5–6σ
[verificar], σ(A_ISW)/A_ISW ~ 15–20%. **Limiar de falseabilidade
prático: ΔISW/ISW ≳ 0.4 (2σ).** Se o R-8 completo produzir um efeito
menor que isso, a honestidade manda escrever no paper "indetectável em
princípio", não "aguarda dados futuros".

**P7 — [MÉDIA] Testar isocurvatura (W8).**
Calcular a fração de isocurvatura induzida por δφ₋ e o coeficiente de
correlação com a adiabática. Confrontar com Planck (β_iso < ~0.038
não-correlacionada; ~10⁻³ correlacionada) [verificar] e com LiteBIRD,
que melhora exatamente a faixa ℓ ≲ 30 em EE. Se a TDCP não gerar
isocurvatura, **isso em si é uma predição não-trivial de um modelo de
dois campos** e deve ser dito. Se gerar, pode já estar excluída.

**P8 — [MÉDIA] Âncoras do dicionário — recomendação explícita.**
- **H₀:** não ajustar; rodar **duas** cadeias, H₀ = 67.4 (CMB-ancorado)
  e H₀ = 73.0 (escada de distâncias), reportando Δχ² em ambas. Como a
  família fixa o H tardio por construção [repo], a F1 **não tem
  mecanismo para a tensão H₀** — dizer isso explicitamente no cap. 09 é
  melhor que deixar o leitor esperar.
- **Ω_m / z_eq:** ancorar em **Ω_m h² = 0.1430 ± 0.0011** (não em Ω_m
  isolado), que fixa **z_eq = 3387 ± 21** [externo, Planck 2018 VI]. z_eq
  deve ser *entrada*, não saída — ele controla o envelope dos picos e a
  posição do turnover k_eq, e um erro aqui desloca todo o C_ℓ.
- **Ω_m(a₀):** 0.315 ± 0.007 (Planck) ou ~0.30 (DESI DR2). Aposentar o
  0.25 (W7).
- **τ:** 0.0544 ± 0.0073 (Planck), com LiteBIRD projetando σ(τ) ≈ 0.002
  [verificar]. **Atenção à degenerescência:** qualquer modificação da
  F1 em EE de baixo-ℓ compete diretamente com o bump de reionização, na
  *mesma* faixa de ℓ. Só a **forma em ℓ** quebra a degenerescência —
  logo o pipeline precisa entregar a forma, não a amplitude.
- **S8/σ8:** **não mirar a tensão S8** (W11). Reportar σ8 e deixar.

**P9 — [BAIXA, mas obrigatória antes de submeter] Checklist mínimo de um
C_ℓ crível.**
1. **Normalização primordial** — A_s, n_s no pivô k = 0.05 Mpc⁻¹,
   **variados na cadeia**, nunca fixos. Se a F1 altera o platô
   Sachs–Wolfe, o efeito é degenerado com A_s e⁻²τ; a única quebra é a
   razão baixo-ℓ/alto-ℓ, que Planck já mede a ~5–8%.
2. **Reionização** — τ e a forma de x_e(z); o bump EE em ℓ ≲ 10 é o
   território de LiteBIRD e da F1 ao mesmo tempo.
3. **Lensing do CMB** — obrigatório, porque Σ entra direto no potencial
   de lente e altera o *smoothing* dos picos. Cruzar com a reconstrução
   de lente (ACT DR6/Planck), não só com o efeito em TT.
4. **Condições iniciais** — adiabáticas puras declaradas; e o teste de
   isocurvatura de P7 rodado separadamente.
5. **Radiação e neutrinos** — ρ_r a⁻⁴ e N_eff = 3.044; Σm_ν como
   nuisance. Nota: DESI+CMB já empurra Σm_ν < ~0.06 eV (95%)
   [verificar], em tensão leve com a hierarquia normal mínima. Uma
   teoria que suprime crescimento agrava; que amplifica, alivia. **É um
   eixo de falseabilidade real e barato de reportar.**
6. **Convenções** — o mapa entre a convenção de potenciais da v2
   (Ψ temporal) e a da biblioteca já está sinalizado no cap. 09 §4.1
   [repo]; deve virar um teste unitário, não uma nota.
7. **V-XREP obrigatório** + o gate externo V-EXT de P1.
8. **Critérios de falseamento pré-declarados**, com sinal e magnitude,
   ANTES da primeira rodada — como manda o cap. 02 do próprio
   manuscrito [repo]. Sugestão de formato: "se |ΔC_ℓ/C_ℓ| < 5% em
   2 ≤ ℓ ≤ 30, declaramos a F1 indistinguível de ΛCDM em baixo-ℓ e
   encerramos essa linha".

---

## Veredito do especialista

A F1 pós-Erratum-02 é **viável e não-excluída, mas ainda não é uma
teoria testável**: seu único número distintivo (m_T ≈ 2.3 H₀) coincide
com a expectativa genérica da classe bimétrica, está 10 ordens de
grandeza abaixo de qualquer limite direto, e nasce de uma família que
fixa H(z) por construção. A janela declarada como decisiva (ℓ ≲ 20,
λ ≳ Gpc) é, por variância cósmica, a **menos** decisiva do céu — ~8% de
erro irredutível em 2 ≤ ℓ ≤ 20 e ~1 modo em P(k) a k = 10⁻³ h/Mpc — de
modo que o risco dominante não é a refutação, é a indistinguibilidade
por construção. Em contrapartida, o perigo não declarado é o oposto:
**z ≳ 100 nunca foi sondado, kh ≲ 22 na recombinação cobre ℓ ≲ 1300, e
a tendência medida no próprio R-8a diz que os desvios crescem quando
r decresce.** Antes de qualquer C_ℓ, rode P2; antes de qualquer
afirmação, rode P1; e mire os canais com futuro real — B-modes (P4),
isocurvatura (P7), multi-tracer ultra-grande (P5) — não o ISW.
