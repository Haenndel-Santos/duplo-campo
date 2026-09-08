# Revisão de literatura (scoping) — a cota de Higuchi em fundo bimétrico dinâmico com acoplamentos modulados β_n(φ), e o estado da instabilidade de gradiente

**Gerada:** 2026-09-07.
**Tipo:** *scoping review* — mapeia conceitos, métodos e lacunas em torno de uma pergunta do
corpus; protocolo de busca declarado e reprodutível (§2, §10), triagem de texto integral
**seletiva** (orientada pela pergunta), sem agregação quantitativa. Não é revisão sistemática.
**Janela:** 2011-06 (Hassan–Rosen) → 2026-09-07.
**Bases:** INSPIRE-HEP (API REST: rastreio de citações de oito âncoras + buscas por texto
integral/abstract/título), arXiv (API: sete consultas + duas listas de identificadores),
ar5iv (texto integral de 12 fontes, equações extraídas do `alttext` LaTeX), Consensus (três
buscas; plano gratuito devolve 3 resultados por busca), busca web (três consultas). Elicit:
**indisponível** (plano sem acesso à API). Semantic Scholar: não consultado.
**Scripts e saídas versionados:** `auditoria/code/litrev_check_ft_konnig.py` →
`auditoria/code/out/litrev_check_ft_konnig.txt` (verificação simbólica, seis gates
pré-declarados no cabeçalho); `auditoria/code/litrev_build_pool.py` (fusão, deduplicação e
marcação por palavra-chave) → `auditoria/code/out/litrev_pool_2026-09-07.csv` (563 registros
únicos, com fonte de cada um); `auditoria/code/litrev_ar5iv2txt.py` (conversor ar5iv → texto).

**Disciplina de níveis (herdada de `docs/posicionamento_literatura.md`).** Cada afirmação
abaixo carrega um de quatro rótulos: **V-texto** = texto integral lido (extração ar5iv, equação
citada por número); **V-abs** = título, abstract e referência bibliográfica verificados na API
(arXiv/INSPIRE); **B** = nível-de-busca (só título ou lista; *ausência nunca é prova*);
**CAS** = identidade verificada simbolicamente em `litrev_check_ft_konnig.py`. Tudo aqui é
literatura = **nível 3** do projeto. Nada substitui derivação própria; posiciona-a.

**Por que esta pergunta.** `docs/auditoria_r13.md` §6.3 declarou como "o item mais caro da
fila" saber se a eq. (14) de Könnig 2015 continua sendo a condição de Higuchi ponto a ponto sob
modulação `β_n(φ₋)`, registrando que isso "não foi derivado por ninguém"; e
`docs/posicionamento_literatura.md` §6 P-7 registra que Fasiello–Tolley 1308.1647 — a fonte
primária *real* da cota em FLRW — era citada desde a v1 sem ter sido aberta. Esta revisão
existe para fechar a segunda pendência e reformular a primeira.

---

## 0. Resumo executivo — o que esta revisão muda no corpus

1. **P-7 fecha: Fasiello–Tolley 1308.1647 foi aberta, e a cota bate letra por letra com o
   corpus (V-texto + CAS).** A cota de estabilidade cosmológica para bigravidade é a eq. (1.3)
   [= (3.18) = (7.1)]:

   $$\tilde m^{2}(H)\Big[H^{2}+\frac{H_f^{2}M_p^{2}}{M_f^{2}}\Big]\;\geq\;2H^{4},\qquad
   \tilde m^{2}(H)=\frac{m^{2}}{2M_p^{2}}\frac{H}{H_f}\Big[\beta_1^{\rm FT}+2\beta_2^{\rm FT}\frac{H}{H_f}+\beta_3^{\rm FT}\frac{H^{2}}{H_f^{2}}\Big]\quad\text{(1.2)}$$

   com forma simétrica (1.4). A ação (3.1) traz o potencial como `−(m²/2)Σβ_n^{FT}U_n(X)`,
   logo **`β_n^{FT} = 2M_ef²β_n`** em relação à normalização Hassan–Rosen do cap. 03 — é o
   fator ½ que a nota 3 de Könnig 2015 anunciava, agora conferido na fonte. No ramo dinâmico
   do vínculo de Bianchi vale `H/H_f = b/a = r` (os próprios F–T reescrevem as duas Friedmann
   em potências de `H/H_f`, §3.1). Com essas duas substituições a (1.3) é **idêntica** à
   "forma massa" do R-13a §2.2, `(m²M_ef²/M_f²)·ℬ(r)·(1+μr²)/r ≥ 2H²`, e à eq. (14) de Könnig
   via o mapa do R-13a §2.1 — gates G1–G3, resíduos simbólicos zero. O limite primordial do
   ramo finito da F1 dá `3` (G4), como o R-13a havia inferido.
   *Consequência:* a leitura do R-13a §3.2, marcada lá como *inferência*, é literalmente o que
   F–T escrevem — a expressão `m̃²(1+H_f²M_p²/(H²M_f²))` é chamada por eles de "the dynamical
   mass of the massive graviton". **O objeto de Higuchi não contém `ξ = N_f/N_g`.** A caixa de
   `m_T²` do cap. 06 (com `ξ` dinâmico) é a massa do modo helicidade-2, que na literatura
   carrega de fato o lapso de `f` (Cusin et al. 2015, eqs. 56–57), e coincide com o objeto de
   Higuchi só em `ξ = r`. Isto confirma e fecha o R-13a §3.3.

2. **A fronteira "eq. (14) sob `β_n(φ)` não foi derivada por ninguém" cai em parte (V-texto +
   CAS).** Na classe-irmã (bigravidade camaleônica), De Felice, Mukohyama, Oliosi & Watanabe
   2018 derivam, no limite sub-horizonte `k ≫ aH`, o autovalor cinético do gráviton escalar com
   **`β_i(φ)` gerais e individuais** — eq. (43) — e ele contém termos explícitos em
   `φ̇U_{,ξφ}`, `φ̇J_{,φ}` e `U_{,ξφ}²`. No limite `β` constante e no ramo dinâmico, `κ₁ ≥ 0`
   **reduz-se exatamente à cota de F–T/Könnig** (G5, resíduo zero). Logo a forma pontual (14)
   com `β_n → β_n(t)` **não sobrevive intacta**: as correções são ∝ `φ̇β′` (sinal indefinido)
   e ∝ `(β′)²` com coeficiente **negativo-definido** (G6) — esse termo só aperta a condição,
   para qualquer sinal de `φ̇`. Em de Sitter com solução de escala (De Felice–Mukohyama–Uzan
   2018, eq. 44) a cota modulada é estritamente mais forte que Higuchi:
   `m_T²/H² > 1 + √(1 + 6λ²κξ²(1+κξ²)) ≥ 2`, igualdade só em `λ = 0`.
   *O que continua sem derivação na literatura:* (i) a versão **IR/minisuperespaço** (a rota
   de F–T, que é a rota do Gate 2 do corpus) com `β_n(φ)`; (ii) o recorte específico do corpus
   — `β₁` único modulado, matéria mínima só em `g`, `φ₋` com potencial, espectador `φ₊`. A
   maquinaria geral existe e cobre esse recorte por especialização; traduzir a eq. (43) para as
   convenções do projeto é **trabalho de tradução** (como o R-13a fez com Könnig), não
   descoberta. A frase do `auditoria_r13.md` §6.3 deve ser reescrita nesses termos (§8).

3. **O vínculo de Bianchi com `β̇` (Erratum-01 / Gate 2) tem contraparte publicada (V-texto).**
   A eq. (14) de 1711.04655 resolve o lapso de `f` com o termo de modulação:
   `c = 12J(Hξ+ξ̇)/[ξ(12HJ + φ̇U_{,ξφ})]`. Sem modulação ela volta a `(Hξ+ξ̇) = cξH` (ramo
   dinâmico) ou `J = 0` (ramo algébrico); com modulação **a fatoração some** — o mesmo
   enunciado do cap. 04, na classe-irmã e nas variáveis deles (`ξ` deles = `r` nosso;
   `c` deles = `ξ/r` nosso).

4. **IR vs UV, e o peso epistêmico de um ghost (V-texto).** A cota de F–T é condição **IR**
   (perturbações homogêneas e isotrópicas — nota 2 de 1702.04490, verbatim); a condição **UV**
   com `β` constantes é De Felice et al. 2014: `W > 0` (eq. 39), que sem matéria em `f` vira
   `dρ̂_m/d ln ξ > 0` (eq. 41) = Yamashita–Tanaka = eq. (16) de Könnig. Em bigravidade padrão
   as duas coincidem (`r′ ≥ 0`), e G5 mostra que a versão UV da camaleônica também coincide em
   `β` constante. **Nuance a registrar:** Gümrükçüoğlu, Mukohyama & Sotiriou 2016 mostram que
   ghosts taquiônicos de **baixa energia** não implicam decaimento catastrófico do vácuo. Isso
   não toca o veredito do R-13b — a condição violada no IBB é também a UV — mas qualifica a
   redação do §III D de Könnig ("fantasma ⇒ decaimento do vácuo"), que deve ser citada com essa
   ressalva.

5. **Instabilidade de gradiente: a leitura vigente (2019–2025) é a fraca, e ela se choca com
   o R-10d (V-texto / V-abs).** Lüben, Schmidt-May & Smirnov 2020: "the instabilities in
   linear cosmological perturbations in bimetric theory are the manifestation of the non-linear
   Vainshtein mechanism on an FRW background", com `m_FP` como escala de Vainshtein cosmológica;
   a perturbação linear quebra "exactly when the Stückelberg field becomes non-linear"
   (`H ~ m_FP`); apoiam-se em Aoki–Maeda–Namba 2015 e Högås–Torsello–Mörtsell 2020 (soluções
   não-lineares sem instabilidade). Högås & Mörtsell 2021a/b tratam a cota de Higuchi dinâmica
   como vínculo **duro** (garante `y′ > 0` e cosmologia contínua) e a instabilidade de gradiente
   como "desafio", não como exclusão. Isto decide o risco **R-a** do posicionamento a favor da
   leitura (ii) — e abre um **confronto novo**: o R-10d mediu que o screening não salva a F1
   (`δ_screen ≈ 20–60`, `λ` cancela), enquanto a literatura afirma que o screening opera
   precisamente onde a instabilidade linear aparece. Item novo de fila (§8).

6. **Ramo infinito e "portas" (V-texto / V-abs).** Högås & Mörtsell 2021a §5.1: *"Infinite
   branch (inconsistent) … These solutions are plagued by a Higuchi ghost and are therefore
   ruled out"*, e ainda `B₃ ≤ 0` conflita com Vainshtein — o R-13b está alinhado com a posição
   de 2021. Saídas conhecidas com `β` constantes: **(a)** `M_f` pequeno (Akrami, Hassan,
   Könnig, Schmidt-May & Solomon 2015): a instabilidade é empurrada para antes do BBN se
   `M_f ≲ escala eletrofraca` (`μ ≲ 10⁻³³`) — dezenas de ordens de grandeza abaixo de qualquer
   `μ` varrido no corpus, e ao custo de tornar o setor massivo quase invisível (BBN: mistura
   `θ ≲ 18°` para `m_FP ≳ 10⁻¹⁶ eV`, Högås–Mörtsell 2021c); **(b)** acoplamento duplo — com
   patologias próprias (Comelli–Crisostomi–Koyama–Pilo 2015: vetor exponencialmente instável;
   Gümrükçüoğlu–Heisenberg–Mukohyama–Tanahashi 2015: ghost tardio num ramo) e fortemente
   restringido pelo GW170817 (Akrami, Brax, Davis & Vardanyan 2018); **(c)** MTBG (De Felice,
   Larrouturou, Mukohyama & Oliosi 2021): remove o gráviton escalar por construção (4 DOF)
   mantendo os fundos FLRW de HR — sai de Hassan–Rosen; **(d)** `β₃ ≠ 0` com `β` constantes no
   ramo finito **já está fechada** pela classificação de 1407.4331 §V / 1503.07436 §V
   (V-12i / V-13a no corpus) — a "porta `β₃ ≠ 0`" do cap. 07 só tem sentido **com modulação**.
   Em massive gravity (métrica fixa), a teoria mínima de massa variável reporta cosmologia
   estável (Falah, Latief & Alatas 2025, **preprint**).

7. **Massa do gráviton `~H₀` (V-abs).** A síntese da literatura anterior feita na introdução
   de 1711.04655: em bigravidade padrão a estabilidade exige `m ≫ H₀` (Comelli–Crisostomi–Pilo
   2012; De Felice et al. 2014), o que impede a massa de explicar a aceleração. Contraposição
   2020–2025: Lüben–Schmidt-May–Weller 2020 e Högås–Mörtsell 2021a/b encontram auto-aceleração
   viável com screening; Caravano–Lüben–Weller 2021: o modelo só-`β₁` é excluído pela análise
   combinada; Högås–Mörtsell 2025: bigravidade melhora o ajuste ao DESI DR2 e infere
   `H₀ = 69.0 ± 0.4 km/s/Mpc`. O `m_T ≈ 2.3H₀` do R-8b cai exatamente no regime em que Lüben
   et al. situam a transição de Vainshtein (`H ~ m_FP`). Posicionar; não reivindicar.

---

## 1. Pergunta de pesquisa

| Eixo | Conteúdo |
|---|---|
| **Sistema** | Bigravidade de Hassan–Rosen em FLRW plano, matéria acoplada só a `g`; extensão em que os `β_n` dependem de um escalar dinâmico (TDCP-F1: `β₁(φ₋)`, cap. 03) |
| **Método** | Estabilidade linear: condição no-ghost do helicidade-0 (Higuchi generalizada), velocidade do som escalar (gradiente), setor tensorial; regime IR (`k → 0`) e UV (`k ≫ aH`) |
| **Comparador** | `β` constantes (ramo finito × ramo infinito); classes-irmãs com massa dependente de campo (bigravidade camaleônica, *scale-free*, MVMG, quasidilaton) |
| **Métrica** | Forma explícita da condição; presença de termos em `β̇_n`; regime de validade; veredito publicado sobre cada saída da instabilidade de gradiente |

Sub-perguntas: **Q1** qual é a forma primária da cota em FLRW e a sua normalização; **Q2**
existe derivação com `β_n(t)`; **Q3** IR e UV coincidem; **Q4** como a literatura pesa
ghost × gradiente e quais saídas propõe; **Q5** qual o estado observacional 2020–2026 para
`m_T ~ H₀`.

---

## 2. Estratégia de busca

**Âncoras** (rastreio de citações no INSPIRE, `refersto:recid:N`, `size=500`,
`sort=mostrecent`): 1206.3852, 1308.1647, 1404.0008, 1407.4331, 1410.0207, 1503.07436,
1702.04490, 1711.04655.

**Consultas por termo** (strings exatas no §10). Termos-chave: `Higuchi`, `gradient
instability`, `bimetric|bigravity`, `chameleon|varying mass|mass-varying|time-dependent
mass|dilaton|field-dependent|scalar-dependent`, `scalar field ∧ (interaction|potential|
coupling)`, `DESI|Hubble tension|BAO`.

**Lição de instrumento (registrada porque custou uma rodada):** no INSPIRE, `refersto:arxiv:ID`
**não** funciona pela API (devolveu 24 999 registros aleatórios); a forma correta é obter o
`control_number` com `q=arxiv:ID` e usar `refersto:recid:N`. Os quatro arquivos dessa rodada
foram descartados antes da fusão. A API do arXiv exige HTTPS com redirecionamento
(`curl -L`); o filtro de data por `submittedDate` não foi aplicado na consulta q5 (devolveu a
janela inteira) — compensado pela triagem por título.

**Fluxo.** 1 283 registros brutos → **563** únicos após deduplicação (ordem: id arXiv → DOI →
título normalizado) → marcação automática por palavra-chave (59 registros "bimétrico ∧
tópico" + 69 "lado massive gravity: Higuchi/massa variável") → triagem manual por
título/abstract → **12 textos integrais** (ar5iv) + ≈ 45 abstracts lidos.

---

## 3. Critérios de inclusão e exclusão

**Inclusão:** (i) bigravidade HR ou massive gravity dRGT em fundo FLRW; (ii) trata cota de
Higuchi / no-ghost, instabilidade de gradiente ou setor tensorial; **ou** (iii) promove
parâmetros do potencial a funções de um campo; (iv) 2011–2026; (v) inglês; (vi) preprints
admitidos e **rotulados**.
**Exclusão (com razão):** cota de Higuchi em inflação / *swampland* / cordas (objeto diferente:
espectador de spin-2 em dS, não gráviton massivo autointeragente); buracos negros e objetos
compactos; propagação de GW apenas (mantida como contexto observacional); teorias bimétricas
não-HR (teleparalela, afim, velocidade da luz variável); duplicatas e teses sem preprint.
As marcas de triagem estão na coluna `flags` do CSV; os textos integrais lidos estão em §4.

---

## 4. Sumário da evidência (tabela de extração)

Colunas: estudo · tipo · sistema/fundo · método · resultado-chave · limitação declarada · nível.

| Estudo | Tipo | Sistema | Método | Resultado-chave | Limitação | Nível |
|---|---|---|---|---|---|---|
| Fasiello & Tolley 2012 [1206.3852] | primário | dRGT, métrica de referência FLRW | Hamiltoniano de perturbações | `m̃²(H) ≥ 2H²` generalizada a FRW arbitrário; tensão Higuchi × Vainshtein exclui FRW plano em massive gravity | métrica fixa | V-abs (+ trechos V-texto) |
| Fasiello & Tolley 2013 [1308.1647] | primário | bigravidade HR, matéria só em `g`, CC em `f` | minisuperespaço + limite Λ₃ | eqs. (1.2)–(1.4), (3.18), (7.1); `β` const; válida para qualquer FRW; `Ḣ` não entra no termo cinético (§5.2) | **IR**; `β` constantes | **V-texto + CAS** |
| Hassan, Schmidt-May & von Strauss 2013 [1208.1797] | primário | HR, fundos maximalmente simétricos | simetria de gauge na cota | parâmetros PM saturam Higuchi | dS | V-abs |
| Sakakihara, Soda & Takahashi 2013 [1211.5976] | primário | HR, dS | perturbações anisotrópicas | bifurcação de ramos dS coincide com a cota de Higuchi | dS | V-abs |
| De Felice et al. 2014 [1404.0008] | primário | HR, dois fluidos | ação quadrática, UV | `W > 0` (eq. 39) estende Higuchi; sem matéria em `f` ⟺ `dρ̂_m/dlnξ > 0` (eq. 41); automático no ramo saudável; `c_s²` pode ser `< 0` | `β` const | V-texto (§ lidos) |
| Yamashita & Tanaka 2014 [1401.4336] | primário | HR ↔ mundo-brana | mapeamento | condição `ρ_{,r} ≤ 0` (creditada por Könnig e De Felice) | não lida | V-abs |
| Könnig, Patil & Amendola 2014 [1312.3208] | primário | HR, fundo | viabilidade | `r′ < 0` nos ramos infinitos; sem cruzamento phantom | fundo | V-abs |
| Könnig et al. 2014 [1407.4331] | primário | HR, ramos finito/infinito | 10 → 2 DOF | classificação; IBB; §VIII leitura fraca | — | V-12i (corpus) |
| Comelli, Crisostomi & Pilo 2014 [1403.5679] | primário | HR + 2º setor de matéria | perturbações FRW | instabilidades exponenciais sub-horizonte inevitáveis cedo → "premature departure from the perturbative regime" | — | V-abs (+ trechos) |
| Lagos & Ferreira 2014 [1410.0207] | primário | HR | escalar/vetor/tensor completo | instabilidades exponenciais genéricas; subclasse escalar-estável tem vetor/tensor crescentes | — | V-abs |
| Cusin, Durrer, Guarato & Motta 2015 [1412.5979] | primário | HR, modelo `β₁β₄` (IBB) | tensores | eqs. (56)–(57): termo de massa tensorial com o lapso `c` de `f`; instabilidade tensorial cedo | modelo específico | V-texto (§ lidos) |
| Könnig 2015 [1503.07436] | primário | HR | classificação | eqs. (14)–(19); teorema §V | `β` const; `M_f = M_g` | V-13a (corpus) |
| Akrami et al. 2015 [1503.07521] | primário | HR, `M_f ≪ M_g` | fundo + perturbações | instabilidades empurradas para antes do BBN se `M_f ≲` EW; helicidade-0 sem acoplamento forte | GR + Λ efetivo | V-abs |
| Aoki, Maeda & Namba 2015 [1506.04543] | primário | HR, perturbação esférica | não-linear no helicidade-0 | instabilidades resolvidas por não-linearidades em parte do espaço de parâmetros | fundo proporcional | V-abs |
| Mörtsell & Enander 2015 [1506.04977] | primário | HR | Vainshtein assumido | instabilidades cedo têm impacto desprezível; `z_i ≈ 0.5` no modelo `β₁` | hipótese de screening | V-abs |
| Gümrükçüoğlu, Mukohyama & Sotiriou 2016 [1606.00618] | primário | escalar em GR | transformação canônica | ghost taquiônico IR = instabilidade de Jeans; não catastrófico | — | V-abs |
| Cusin, Khosravi & Noller 2017 [1608.06643] | primário | HR *scale-free* (`m → Φ`, fator global) | ação quadrática cosmológica | mistura `δφ`–métrica só na matriz de massa antes de resolver vínculos; condição no-ghost/Higuchi **adiada** | não deriva a cota | V-texto (§ lidos) |
| De Felice, Mukohyama & Uzan 2018 [1702.04490] | primário | camaleônica: `β_i(φ)` + `A(φ)` | dS com escala | eq. (43) `m_T²/H²` só função de `ξ`; eq. (44) cota **mais forte** que Higuchi para `λ ≠ 0`; nota 2 (IR/UV) | dS | **V-texto** |
| De Felice, Mukohyama, Oliosi & Watanabe 2018 [1711.04655] | primário | camaleônica, FLRW geral | ação quadrática UV | eq. (43): `κ₁` com `φ̇U_{,ξφ}`, `φ̇J_{,φ}`, `U_{,ξφ}²`; eq. (14): lapso com `β̇`; exemplo numérico rad→mat→dS estável | UV; matéria em `A²g` | **V-texto + CAS** |
| Gümrükçüoğlu, Hinterbichler, Lin, Mukohyama & Trodden 2013 [1304.0449] | primário | MVMG e quasidilaton | perturbações | eqs. (90)–(91): `ρ_σ + p_σ = σ̇²` entra no no-ghost escalar; dS-like: `R > 6` | métrica fixa | V-texto (§III) |
| Huang, Piao & Zhou 2012 [1206.5678]; Hinterbichler, Stokes & Trodden 2013 [1301.4993] | primário | MVMG | vínculos; fundo | livre de BD (dois vínculos); *big brake* | métrica fixa | V-abs |
| Kenna-Allison, Gümrükçüoğlu & Koyama 2019 [1812.05496] / Lüben, Mörtsell & Schmidt-May 2020 [1812.08686] | primário / réplica | HR | Poisson + 2ª ordem | incompatibilidade Vainshtein × cosmologia primordial / contra-exemplos | — | V-abs |
| Lüben, Schmidt-May & Smirnov 2020 [1912.09449] | primário | HR | *twist* `μ(r)`, raio de Vainshtein cosmológico | instabilidade linear = Vainshtein em FLRW; escala `m_FP`; phantom alivia `H₀` | — | V-texto (§IV.2, §V) |
| Högås, Torsello & Mörtsell 2020 [1910.01651] | primário | HR | modelo analítico | sem instabilidade física de estrutura | modelo simples | V-abs |
| Högås & Mörtsell 2021a [2101.08794] | primário | HR, parametrização física | analítico | Higuchi dinâmico (5.12)–(5.13) com `m_eff²` **só em `y`**; ramo infinito "inconsistent" (§5.1); `y′ > 0` | — | V-texto (§5, §7, Ap. C) |
| Högås & Mörtsell 2021b [2101.08795]; 2021c [2106.09030]; Caravano, Lüben & Weller 2021 [2101.08791]; Lüben, Schmidt-May & Weller 2020 [2003.03382] | primário | HR | CMB+BAO+SNe; BBN | viável com screening e sem Higuchi; `θ ≲ 18°`; só-`β₁` excluído | — | V-abs |
| De Felice, Larrouturou, Mukohyama & Oliosi 2021 [2012.01073] | primário | MTBG | construção | 4 DOF; mesmos fundos FLRW de HR | fora de HR | V-abs |
| Dwivedi & Högås 2024 [2407.04322]; Högås & Mörtsell 2025 [2507.03743]; Bassi et al. 2023 [2301.11000]; Brizuela, de Cesare & Soler Oficial 2026 [2507.11526] | primário | HR | dados 2023–2025 | 2D-BAO e `H₀`; DESI DR2 (`H₀ = 69.0 ± 0.4`); LSS; nova cota GW170817 | — | V-abs |
| Gialamas & Tamvakis 2025 [2503.16598]; Brax & Valageas 2018 [1712.04520]; Falah, Latief & Alatas 2025 [2507.21542, **preprint**] | vizinhos | massa de spin-2 por vev escalar; escalar-bimétrica; MTMVMG | — | massa de Fierz–Pauli ∝ vev; auto-aceleração por funções de acoplamento; cosmologia estável | — | V-abs |

---

## 5. Síntese temática

### T1 — A cota de Higuchi em FLRW bimétrico: forma, proveniência, normalização

*Evidência mais forte:* 1308.1647 (V-texto + CAS). A derivação é dupla — minisuperespaço com
campos de Stückelberg (§2–3) e limite de desacoplamento Λ₃ (§5) — e a cota nasce da
positividade do termo cinético do helicidade-0 `π` após diagonalizar `δχ` (com `b/a = e^χ`)
contra a perturbação de matéria (§3, eqs. 3.13–3.18). Três fatos da fonte importam ao corpus:

- **Normalização.** Ação (3.1): `S = ∫ ½[M_p²√−g R[g] + M_f²√−f R[f] − m²Σβ_n U_n(X)]`, `X =
  √(g⁻¹f)`, `U_n` = os mesmos polinômios simétricos `e_n` (eqs. 2.4–2.7). Contra a HR do cap.
  03 (`−m²M_ef²Σβ_n e_n`): **`β_n^{FT} = 2M_ef²β_n`**. Os `β_n^{FT}` têm dimensão de massa²
  (F–T exemplificam com `β₁ = 2M_p²`, `β₂ = M_p²`). Quem citar 1308.1647 diretamente herda esse
  fator — como a nota 3 de Könnig avisava.
- **`H/H_f = r`.** `H_f ≡ ḃ/(Ñb)`; no ramo dinâmico `Ñȧ = Nḃ` dá `H_f = H/r`. F–T usam isso
  eles mesmos ao reescrever as Friedmann em `H/H_f` (§3.1). Portanto a "massa vestida" (1.2) é
  `m̃² = (m²M_ef²/M_g²)·r·ℬ(r)`, e a (1.3) é a forma-massa do R-13a com **resíduo zero** (G1).
  A (1.4) difere da (1.3) por `H_f³/H > 0` (G2); a (14) de Könnig, via o mapa `r_K = √μ r`,
  `β_n^K = Aμ^{−n/2}β_n` verificado em `auditoria_r13.md` §1, difere da forma-massa por
  `3M_f r/(2M_p) > 0` (G3). **Três formas, uma desigualdade.**
- **Por que a cota em FRW tem a cara da de dS.** §5.2, verbatim no essencial: a dependência em
  `Ḣ` e `Ḣ_f` "will not affect the resulting coefficient of the kinetic term for π", porque só
  `h̄_ij`, `v̄_ij` e `Π̄_ij` acoplam a termos com duas derivadas temporais de `δπ` — "a simple
  explanation of the result first observed in [F–T 2012] that the bound on FRW is identical to
  the bound on de Sitter". Os termos de gradiente, sim, são modificados por `Ḣ`; e F–T já
  registram em 2013 a instabilidade de Jeans sub-horizonte apontada por Comelli et al., com a
  leitura fraca: "short wavelength scalar fluctuations will become strong coupled and cannot be
  treated using linearized perturbation theory".

*A massa tensorial é outro objeto.* Cusin et al. 2015, eqs. (56)–(57), para o modelo `β₁β₄`:
`h_g″ + 2ℋh_g′ + k²h_g + m²a²rβ₁(h_g − h_f) = 0` e
`h_f″ + […]h_f′ + c²k²h_f − m²β₁(ca²/r)(h_g − h_f) = 0` — o termo de massa do setor `f` traz
o fator de lapso `c`. A combinação massiva tem massa ∝ `r(1 + c/r²)`, que é a estrutura da
caixa do cap. 06 (`1/M_g² + ξ/(M_f²r³)`) e **não** a de Higuchi (`1 + 1/(μr²)`). Coincidem sse
`c = 1` (`ξ = r`). Högås & Mörtsell 2021a usam, para a cota de Higuchi dinâmica, exatamente o
objeto só-em-`y`: `m_eff² ≡ (1 + 1/(tan²θ y²))(B₁y + 2B₂y² + B₃y³)` (eq. 5.13), com
`m_eff² > 2Ω̃_DE` (5.12) e a identidade `−y dΩ_m/dy = m_eff² − 2Ω̃_DE` (5.15) — que é a
cadeia `(14) ⟺ (16) ⟺ (18)` de Könnig na parametrização deles. **A convenção "massa
dinâmica = objeto em `r`, sem lapso" é a da literatura de 2013 a 2021.**

### T2 — Acoplamentos dependentes de campo: o que está derivado

- **Bigravidade camaleônica (De Felice–Mukohyama–Uzan 2018; De Felice–Mukohyama–Oliosi–
  Watanabe 2018).** Ação: `S_m = M_g²m²∫Σ_i β_i(φ)U_i[s]√−g` (sinal e normalização diferentes
  da HR: `β_i^{DMO} = −(M_ef²/M_g²)β_i`), `S_φ` canônico em `g`, matéria em `g̃ = A²(φ)g`. As
  equações de fundo (8)–(14) e as condições de estabilidade (42)–(53) estão escritas para
  `U(ξ,φ)` **genérico** — `β_i(φ)` individuais; a especialização `β_i = −c_i e^{−λφ/M_g}`,
  `A = e^{βφ/M_g}` (eq. 6) entra só na solução de escala e no exemplo numérico. A eq. (43):

  $$\kappa_1=\frac{a^{4}m^{2}M_g^{2}}{8H\kappa}\Big\{3m^{2}(H-H\kappa\xi^{2}+2H_f\kappa\xi^{3})J^{2}
  +2\kappa\xi^{2}J\Big[3H_fH(2H_f\xi-3H)-\tfrac14 m^{2}\dot\phi\,U_{,\xi\phi}\Big]
  +2H\kappa\xi^{2}\Big[3H_f\xi(H-H_f\xi)J_{,\xi}-3H_f\dot\phi J_{,\phi}-\tfrac1{16}m^{2}M_g^{2}U_{,\xi\phi}^{2}\Big]\Big\}$$

  com `J = R_{,ξ}/3`, `R = U − ξU_{,ξ}/4`, `U = −(β₄ξ⁴+4β₃ξ³+6β₂ξ²+4β₁ξ+β₀)`. Em `β`
  constante e `H_f = H/ξ`: `κ₁ → (a⁴m²M_g²/8Hκ)·3HJ·[m²(1+κξ²)J − 2κξH²]` (G5a), e o colchete,
  no mapa para a HR (`ξ → r`, `κ → μ`), é a forma-massa de F–T/Könnig com resíduo zero (G5b).
  Os termos de modulação são (G6):
  `−(M_g²a⁴m²ξ²/64)[48H_f J_{,φ}φ̇ + 4JU_{,ξφ}m²φ̇/H + M_g²m²U_{,ξφ}²]`; o coeficiente de
  `U_{,ξφ}²` é `−M_g⁴a⁴m⁴ξ²/64 < 0`. Nota de leitura: `J_{,φ} = U_{,ξφ}/4 − ξU_{,ξξφ}/12`, então
  os três termos não são independentes; a afirmação de sinal vale para o termo quadrático
  isolado, a fundo fixo.
  *Em de Sitter com escala* (1702.04490, eqs. 43–44): `m_T²/H² = 3(1+κξ²)(c₃ξ²+2c₂ξ+c₁)/(c₄ξ³+
  3c₃ξ²+3c₂ξ+c₁)` — o objeto de Higuchi em `ξ` (= nosso `r`), independente do ambiente — e o
  no-ghost escalar `m_T²/H² > 1 + √(1+6λ²κξ²(1+κξ²))`, "a relation stronger than the usual
  Higuchi bound" para `λ ≠ 0`.
- **Vínculo com `β̇`.** Eq. (14) de 1711.04655 (T0, item 3 acima): a contraparte publicada do
  resíduo `∝ p_φβ₁′` do cap. 04. A observação do posicionamento §1.2 ("a análise de vínculos
  nunca foi feita" na camaleônica) permanece: o que existe é a solução do lapso e a análise
  linear UV; não há análise hamiltoniana da classe.
- **Massa variável em métrica fixa (Gümrükçüoğlu et al. 2013, §III).** Eq. (91), com
  referência de Minkowski: `[(ρ_σ+p_σ)/(4M_p²H²) − 3/2]⁻¹ k²/a² > (ρ_m+p_m)/M_p²` — a energia
  cinética `σ̇² = ρ_σ + p_σ` do escalar que fixa a massa entra na condição no-ghost; em
  expansão quase-dS reduz a `R > 6`, `R ≡ −(ρ_m+p_m)/(H²M_p²)`. Mesma lição estrutural: a
  variação temporal da massa entra no termo cinético do helicidade-0.
- ***Scale-free* bigravity (Cusin, Khosravi & Noller 2017).** `m → Φ` (fator global) com
  termo cinético e potencial. Verbatim: "The mixing is only in the mass matrix (the kinetic
  structure is standard) of scalar perturbations" — dito da ação quadrática **antes** de
  resolver os vínculos — e "it would be interesting to consider the Higuchi bound for it. A
  full analysis of this type is quite involved and deserves a separate investigation". A
  condição no-ghost com `Φ̇ ≠ 0` **não** está derivada ali.
- **Vizinhos com estrutura diferente.** Brax & Valageas 2018 (escalar acopla via funções nos
  vierbeins das métricas de matéria); Gialamas & Tamvakis 2025 (massa de Fierz–Pauli
  proporcional ao vev de um escalar em quadro Weyl-invariante Einstein–Cartan; espectro com
  gráviton sem massa, spin-2 massivo e pseudo-escalares); Aoki & Mukohyama 2017 (gráviton
  massivo como matéria escura com massa dependente do ambiente via camaleão). Nenhum deriva a
  cota em fundo dinâmico com `β_n(t)`.

**Balanço para a fronteira do corpus.** A pergunta "a eq. (14) sobrevive intacta sob
`β_n(φ₋)`?" tem resposta publicada no UV para a classe-irmã: **não** — eq. (43). O que não
existe é (i) a versão IR (minisuperespaço, rota F–T/Gate 2) com modulação e (ii) a
especialização ao recorte da F1. A regra prática do `auditoria_r13.md` §6.2 — sob modulação o
diagnóstico é `𝒲′(r) > 0`, não o sinal de `r′` — é compatível com (43) mas não a esgota: (43)
tem termos que não são função de `r` e `β_n` apenas.

### T3 — IR vs UV, e o peso epistêmico de um ghost

A nota 2 de 1702.04490 é a formulação mais clara: a cota de F–T é para "homogeneous and
isotopic perturbation and thus is the condition for the avoidance of an IR ghost, which a
priori is not necessarily the right condition for theoretical consistency", com a UV derivada
em De Felice et al. 2014. Em bigravidade padrão os dois regimes dão a mesma condição
(`W > 0` ⟺ `dρ̂_m/dlnξ > 0` sem matéria em `f`, eq. 41 de 1404.0008; ⟺ `r′ ≥ 0`), e G5
mostra que o mesmo vale na camaleônica em `β` constante. O R-13b mediu a forma comum. A
ressalva de Gümrükçüoğlu–Mukohyama–Sotiriou 2016 ("low-energy tachyonic ghosts do not lead to a
catastrophic quantum vacuum instability") aplica-se a ghosts **só IR**; o do IBB é UV também.
Onde o corpus citar o §III D de Könnig ("Hamiltoniano ilimitado por baixo ⟹ decaimento do
vácuo", com Woodard 2007 e Sbisà 2015), deve acrescentar a qualificação de regime.

### T4 — A instabilidade de gradiente: leitura vigente e as saídas

Cronologia com fontes: **2012–2014** — instabilidades exponenciais sub-horizonte no ramo
finito (Comelli–Crisostomi–Pilo 2014; Könnig–Amendola 2014; Könnig et al. 2014; Lagos–Ferreira
2014), com a leitura fraca já em Comelli et al. ("premature departure from the perturbative
regime") e em F–T 2013 §5.2. **2015** — três saídas: `M_f` pequeno (Akrami et al.),
não-linearidade do helicidade-0 (Aoki–Maeda–Namba), screening assumido + estrutura
(Mörtsell–Enander); e Könnig 2015 fixa o peso: ghost fatal, gradiente "will not necessarily
rule out the theory". **2018–2020** — controvérsia Kenna-Allison et al. × Lüben et al. sobre
Vainshtein e cosmologia primordial; MTBG como saída estrutural. **2020–2021** — posição que se
tornou operacional: Lüben–Schmidt-May–Smirnov ("the instabilities are indeed an artifact of the
linear approximation and … the Vainshtein mechanism is active also on a time-dependent
background"), Högås–Torsello–Mörtsell ("no physical instability"), Högås–Mörtsell 2021a
(gradiente = "challenge"; Higuchi dinâmico = vínculo). **2023–2025** — uso observacional sem
tratar a era instável como excludente (Bassi et al.; Dwivedi–Högås; Högås–Mörtsell 2025).

Dois pontos para o corpus. **(a) R-a:** a recomendação (ii) do posicionamento ("era em que a
teoria de perturbações linear é inválida em escalas sub-horizonte") é o que a literatura de
2020–2025 escreve. **(b) R-10d contra Lüben et al.:** a literatura afirma que a quebra da
linearidade ocorre "exactly when the Stückelberg field becomes non-linear", i.e. onde o
screening opera, e identifica `m_FP` como a escala; o R-10d mediu na F1 `δ_screen ≈ 20–60` com
`λ` cancelando, concluindo que o screening não é saída. As duas afirmações não podem ser ambas
verdadeiras sem qualificação de modelo e de observável. Este é o confronto mais barato e mais
consequente que a revisão deixa (§8, fila).

### T5 — Estado observacional 2020–2026 e a massa do gráviton

Parametrização física (`m_FP`, `θ`, `Λ`, `ᾱ`) de Lüben–Schmidt-May–Weller 2020;
constraints com screening e sem ghost de Higuchi (Högås–Mörtsell 2021b); BBN (`θ ≲ 18°` para
`m_FP ≳ 10⁻¹⁶ eV`, 2021c); só-`β₁` excluído (Caravano–Lüben–Weller 2021); DESI DR2 + CMB +
SNe: `H₀ = 69.0 ± 0.4` (Högås–Mörtsell 2025); 2D-BAO (Dwivedi–Högås 2024); GW170817 e
propagação tardia (Brizuela–de Cesare–Soler Oficial 2026). O `w_mg ≤ −1` do R-13a §4.3 é a
mesma assinatura phantom que Lüben et al. 2020 e Högås–Mörtsell 2025 usam para aliviar `H₀`.

### T6 — Vizinhos conceituais (massa de spin-2 gerada por escalar)

Linhagem MVMG (D'Amico et al. 2011 → Huang–Piao–Zhou 2012 → Leon–Saavedra–Saridakis 2013 →
Gümrükçüoğlu et al. 2013) e quasidilaton (D'Amico–Gabadadze–Hui–Pirtskhalava 2012; Mukohyama
2014; Gümrükçüoğlu–Koyama–Mukohyama 2017), *scale-free* (2017), camaleônica (2018), MTMVMG
(2025, preprint), Gialamas–Tamvakis 2025. A nota 3 de 1702.04490 registra que promover
coeficientes a funções de um escalar "is not new" em massive gravity (crédito a D'Amico et
al.). O recorte "`β₁` único, `Z₂`, `φ₋` modulador" continua sem estudo dedicado (**B**).

---

## 6. Confiança por afirmação

| Afirmação | Confiança | Base |
|---|---|---|
| F–T (1.3) ⟺ Könnig (14) ⟺ forma-massa do R-13a, com `β^{FT} = 2M_ef²β` e `H/H_f = r` | **alta** | V-texto + CAS (G1–G4) |
| O objeto de Higuchi da literatura 2013–2021 não contém o lapso; a massa tensorial contém | **alta** para F–T/Könnig/Högås–Mörtsell; **média** para a identificação estrutural com a caixa do cap. 06 (só o modelo `β₁β₄` de Cusin et al. foi lido) | V-texto |
| Condição no-ghost UV com `β_i(φ)` gerais existe e tem termos em `φ̇β′` e `(β′)²`; reduz a F–T em `β` const | **alta** | V-texto + CAS (G5–G6) |
| Não existe versão IR/minisuperespaço com `β_n(φ)` nem especialização ao recorte da F1 | **média** | nível de busca (crawl de 8 âncoras + 6 buscas por texto integral); ausência ≠ prova |
| Consenso operacional 2020–2025: gradiente não excludente, Higuchi excludente | **alta** | V-texto (Lüben et al.; Högås–Mörtsell 2021a) + V-abs |
| IBB excluído por Higuchi é posição da literatura de 2021 | **alta** | V-texto (§5.1 de 2021a) |
| Saída `M_f ≲` EW empurra a instabilidade para antes do BBN | **média** | V-abs apenas |
| MTMVMG estável com massa variável | **baixa** | preprint, V-abs |

---

## 7. Lacunas e limitações

**Da literatura.** (i) Cota de Higuchi IR (minisuperespaço) com `β_n(φ)`; (ii) análise
hamiltoniana de vínculos da classe `β_n(φ)` em bigravidade; (iii) tratamento não-linear da era
instável **com** modulação; (iv) a cota de Higuchi no modelo *scale-free* (explicitamente
adiada pelos autores); (v) gradiente no ramo infinito com modulação; (vi) qualquer estudo do
recorte `β₁(φ₋)` com `Z₂`.

**Desta revisão.** Elicit indisponível; Consensus limitado a 3 resultados por busca; Semantic
Scholar e Google Scholar não consultados; a busca por abstract no INSPIRE com termos de massa
variável devolveu zero (provável problema de sintaxe, não de conteúdo — coberta pelas buscas
por texto integral); o filtro de data da consulta q5 do arXiv não se aplicou; apenas 12 textos
integrais; a extração ar5iv pode perder equações renderizadas como figura; 1407.4331 e
1503.07436 **não** foram relidos aqui (apoio nos níveis V-12i/V-13a do corpus); a tradução da
eq. (43) para as convenções do projeto **não** foi feita — só o seu limite `β` constante e o
sinal de um termo; o mapa `tan²θ ↔ μ` de Högås–Mörtsell não foi verificado.

---

## 8. Efeito no corpus — edições propostas (nenhuma executada)

1. **`docs/posicionamento_literatura.md`:** §4 (Higuchi: 1308.1647 passa a **V-texto**); §4c
   item 4 (fator ½ conferido — `β^{FT} = 2M_ef²β`); §5 item 7 (**FEITO**) e item 8
   (reformular: a cota em fundo dinâmico **já é** a de F–T — o que falta é com `β_n(φ)`); §6
   P-7 (**FECHADA**); §1.2 linha "Classe `β_n(φ)` em bigravity" (a camaleônica é `β_i(φ)`
   gerais na formulação, não só fator global; citar eq. 43); §1.1b (o nível de literatura da
   forma-massa sobe de inferência a V-texto).
2. **`docs/auditoria_r13.md` §6.3 e `docs/resultado_r13a_criterio_higuchi_fonte.md` §2.2
   (hipótese 2) e §5:** substituir "não foi verificado por ninguém" por "derivado no UV para a
   classe-irmã com `β_i(φ)` gerais (1711.04655 eq. 43); não derivado no IR; não especializado à
   F1".
3. **`manuscript-v2/06_setor_tensorial.md` §2 e §4:** atribuição — o objeto de Higuchi é a
   massa dinâmica de F–T (só em `r`); a caixa com `ξ` é a massa do helicidade-2 (estrutura das
   eqs. 56–57 de Cusin et al.). O `12` fica como razão tensorial; o `3` é o de F–T.
4. **R-a e D4 do posicionamento:** acrescentar Lüben–Schmidt-May–Smirnov 2020 e
   Högås–Torsello–Mörtsell 2020 como posição vigente; registrar o confronto com o R-10d.
5. **`manuscript-v2/07_setor_escalar.md` §4 ("porta `β₃ ≠ 0`"):** qualificar — fechada com
   `β` constantes por 1407.4331 §V; só existe com modulação.
6. **Fila (itens novos):** (i) traduzir a eq. (43) para as convenções do projeto, especializar
   a `β₁(φ₋)` com `φ₊` espectador, verificar por CAS o limite `φ̇ = 0` e **medir** `κ₁` na
   trajetória de rolagem/pouso (R-7c) — o primeiro teste de Higuchi **modulado** do programa;
   (ii) derivar a versão IR pela rota de F–T §3 com `β₁(φ₋)` — a maquinaria do Gate 2 já
   existe; (iii) confrontar o R-10d com a construção de Lüben et al. (`μ(r)`, raio de
   Vainshtein cosmológico, `H_* ≃ m_FP`); (iv) onde o corpus citar Könnig §III D, qualificar
   IR/UV.

---

## 9. Referências

Referência de periódico e DOI verificados na API do INSPIRE em 2026-09-07; preprints
marcados. Ordem cronológica.

1. Huang, Q.-G., Piao, Y.-S. & Zhou, S.-Y., *Mass-Varying Massive Gravity*, Phys. Rev. D 86, 124014 (2012) [arXiv:1206.5678], doi:10.1103/PhysRevD.86.124014.
2. Fasiello, M. & Tolley, A. J., *Cosmological perturbations in Massive Gravity and the Higuchi bound*, JCAP 11 (2012) 035 [arXiv:1206.3852], doi:10.1088/1475-7516/2012/11/035.
3. Hassan, S. F., Schmidt-May, A. & von Strauss, M., *On Partially Massless Bimetric Gravity*, Phys. Lett. B 726 (2013) 834 [arXiv:1208.1797], doi:10.1016/j.physletb.2013.09.021.
4. Sakakihara, Y., Soda, J. & Takahashi, T., *On Cosmic No-hair in Bimetric Gravity and the Higuchi Bound*, PTEP 2013, 033E02 [arXiv:1211.5976], doi:10.1093/ptep/ptt004.
5. Hinterbichler, K., Stokes, J. & Trodden, M., *Cosmologies of extended massive gravity*, Phys. Lett. B 725 (2013) 1 [arXiv:1301.4993], doi:10.1016/j.physletb.2013.07.009.
6. Gümrükçüoğlu, A. E., Hinterbichler, K., Lin, C., Mukohyama, S. & Trodden, M., *Cosmological perturbations in extended massive gravity*, Phys. Rev. D 88, 024023 (2013) [arXiv:1304.0449], doi:10.1103/PhysRevD.88.024023.
7. Fasiello, M. & Tolley, A. J., *Cosmological Stability Bound in Massive Gravity and Bigravity*, JCAP 12 (2013) 002 [arXiv:1308.1647], doi:10.1088/1475-7516/2013/12/002.
8. Könnig, F., Patil, A. & Amendola, L., *Viable cosmological solutions in massive bimetric gravity*, JCAP 03 (2014) 029 [arXiv:1312.3208], doi:10.1088/1475-7516/2014/03/029.
9. Yamashita, Y. & Tanaka, T., *Mapping the ghost free bigravity into braneworld setup*, JCAP 06 (2014) 004 [arXiv:1401.4336], doi:10.1088/1475-7516/2014/06/004.
10. Könnig, F. & Amendola, L., *Instability in a minimal bimetric gravity model*, Phys. Rev. D 90, 044030 (2014) [arXiv:1402.1988], doi:10.1103/PhysRevD.90.044030.
11. Comelli, D., Crisostomi, M. & Pilo, L., *FRW Cosmological Perturbations in Massive Bigravity*, Phys. Rev. D 90, 084003 (2014) [arXiv:1403.5679], doi:10.1103/PhysRevD.90.084003.
12. De Felice, A., Gümrükçüoğlu, A. E., Mukohyama, S., Tanahashi, N. & Tanaka, T., *Viable cosmology in bimetric theory*, JCAP 06 (2014) 037 [arXiv:1404.0008], doi:10.1088/1475-7516/2014/06/037.
13. Könnig, F., Akrami, Y., Amendola, L., Motta, M. & Solomon, A. R., *Stable and unstable cosmological models in bimetric massive gravity*, Phys. Rev. D 90, 124014 (2014) [arXiv:1407.4331], doi:10.1103/PhysRevD.90.124014.
14. Lagos, M. & Ferreira, P. G., *Cosmological perturbations in massive bigravity*, JCAP 12 (2014) 026 [arXiv:1410.0207], doi:10.1088/1475-7516/2014/12/026.
15. Cusin, G., Durrer, R., Guarato, P. & Motta, M., *Gravitational waves in bigravity cosmology*, JCAP 05 (2015) 030 [arXiv:1412.5979], doi:10.1088/1475-7516/2015/05/030.
16. Comelli, D., Crisostomi, M., Koyama, K., Pilo, L. & Tasinato, G., *Cosmology of bigravity with doubly coupled matter*, JCAP 04 (2015) 026 [arXiv:1501.00864], doi:10.1088/1475-7516/2015/04/026.
17. Gümrükçüoğlu, A. E., Heisenberg, L., Mukohyama, S. & Tanahashi, N., *Cosmology in bimetric theory with an effective composite coupling to matter*, JCAP 04 (2015) 008 [arXiv:1501.02790], doi:10.1088/1475-7516/2015/04/008.
18. Könnig, F., *Higuchi Ghosts and Gradient Instabilities in Bimetric Gravity*, Phys. Rev. D 91, 104019 (2015) [arXiv:1503.07436], doi:10.1103/PhysRevD.91.104019.
19. Akrami, Y., Hassan, S. F., Könnig, F., Schmidt-May, A. & Solomon, A. R., *Bimetric gravity is cosmologically viable*, Phys. Lett. B 748 (2015) 37 [arXiv:1503.07521], doi:10.1016/j.physletb.2015.06.062.
20. Aoki, K., Maeda, K.-i. & Namba, R., *Stability of the Early Universe in Bigravity Theory*, Phys. Rev. D 92, 044054 (2015) [arXiv:1506.04543], doi:10.1103/PhysRevD.92.044054.
21. Mörtsell, E. & Enander, J., *Scalar instabilities in bimetric gravity: The Vainshtein mechanism and structure formation*, JCAP 10 (2015) 044 [arXiv:1506.04977], doi:10.1088/1475-7516/2015/10/044.
22. Melville, S. & Noller, J., *Generalised matter couplings in massive bigravity*, JHEP 01 (2016) 094 [arXiv:1511.01485], doi:10.1007/JHEP01(2016)094.
23. Cusin, G., Durrer, R., Guarato, P. & Motta, M., *A general mass term for bigravity*, JCAP 04 (2016) 051 [arXiv:1512.02131], doi:10.1088/1475-7516/2016/04/051.
24. Gümrükçüoğlu, A. E., Mukohyama, S. & Sotiriou, T. P., *Low energy ghosts and the Jeans' instability*, Phys. Rev. D 94, 064001 (2016) [arXiv:1606.00618], doi:10.1103/PhysRevD.94.064001.
25. Cusin, G., Khosravi, N. & Noller, J., *On scale-free extensions of massive (bi-)gravity*, JHEP 02 (2017) 098 [arXiv:1608.06643], doi:10.1007/JHEP02(2017)098.
26. Gümrükçüoğlu, A. E., Koyama, K. & Mukohyama, S., *Stable cosmology in ghost-free quasidilaton theory*, Phys. Rev. D 96, 044041 (2017) [arXiv:1707.02004].
27. Aoki, K. & Mukohyama, S., *Massive graviton dark matter with environment dependent mass*, Phys. Rev. D 96, 104039 (2017) [arXiv:1708.01969].
28. De Felice, A., Mukohyama, S. & Uzan, J.-P., *Extending applicability of bimetric theory: chameleon bigravity*, Gen. Rel. Grav. 50 (2018) 21 [arXiv:1702.04490], doi:10.1007/s10714-018-2342-z.
29. De Felice, A., Mukohyama, S., Oliosi, M. & Watanabe, Y., *Stable cosmology in chameleon bigravity*, Phys. Rev. D 97, 024050 (2018) [arXiv:1711.04655], doi:10.1103/PhysRevD.97.024050.
30. Brax, P. & Valageas, P., *Self-acceleration in scalar-bimetric theories*, Phys. Rev. D 97, 103516 (2018) [arXiv:1712.04520], doi:10.1103/PhysRevD.97.103516.
31. Akrami, Y., Brax, P., Davis, A.-C. & Vardanyan, V., *Neutron star merger GW170817 strongly constrains doubly coupled bigravity*, Phys. Rev. D 97, 124010 (2018) [arXiv:1803.09726], doi:10.1103/PhysRevD.97.124010.
32. Kenna-Allison, M., Gümrükçüoğlu, A. E. & Koyama, K., *On the viability of bigravity cosmology*, Phys. Rev. D 99, 104032 (2019) [arXiv:1812.05496], doi:10.1103/PhysRevD.99.104032.
33. Lüben, M., Mörtsell, E. & Schmidt-May, A., *Bimetric cosmology is compatible with local tests of gravity*, Class. Quant. Grav. 37 (2020) 047001 [arXiv:1812.08686], doi:10.1088/1361-6382/ab4f9b.
34. Högås, M., Torsello, F. & Mörtsell, E., *On the stability of bimetric structure formation*, JCAP 04 (2020) 046 [arXiv:1910.01651], doi:10.1088/1475-7516/2020/04/046.
35. Lüben, M., Schmidt-May, A. & Smirnov, J., *Vainshtein Screening in Bimetric Cosmology*, Phys. Rev. D 102, 123529 (2020) [arXiv:1912.09449], doi:10.1103/PhysRevD.102.123529.
36. Lüben, M., Schmidt-May, A. & Weller, J., *Physical parameter space of bimetric theory and SN1a constraints*, JCAP 09 (2020) 024 [arXiv:2003.03382], doi:10.1088/1475-7516/2020/09/024.
37. De Felice, A., Larrouturou, F., Mukohyama, S. & Oliosi, M., *Minimal Theory of Bigravity: construction and cosmology*, JCAP 04 (2021) 015 [arXiv:2012.01073], doi:10.1088/1475-7516/2021/04/015.
38. Högås, M. & Mörtsell, E., *Constraints on bimetric gravity. Part I. Analytical constraints*, JCAP 05 (2021) 001 [arXiv:2101.08794], doi:10.1088/1475-7516/2021/05/001.
39. Högås, M. & Mörtsell, E., *Constraints on bimetric gravity. Part II. Observational constraints*, JCAP 05 (2021) 002 [arXiv:2101.08795], doi:10.1088/1475-7516/2021/05/002.
40. Caravano, A., Lüben, M. & Weller, J., *Combining cosmological and local bounds on bimetric theory*, JCAP 09 (2021) 035 [arXiv:2101.08791], doi:10.1088/1475-7516/2021/09/035.
41. Högås, M. & Mörtsell, E., *Constraints on bimetric gravity from Big Bang nucleosynthesis*, JCAP 11 (2021) 001 [arXiv:2106.09030], doi:10.1088/1475-7516/2021/11/001.
42. Bassi, A., Adil, S. A., Rajvanshi, M. P. & Sen, A. A., *Cosmological Evolution in Bimetric Gravity: Observational Constraints and LSS Signatures*, Eur. Phys. J. C 83 (2023) 525 [arXiv:2301.11000], doi:10.1140/epjc/s10052-023-11707-4.
43. Dwivedi, S. & Högås, M., *2D BAO vs 3D BAO: solving the Hubble tension with an alternative cosmological model*, Universe 10 (2024) 406 [arXiv:2407.04322], doi:10.3390/universe10110406.
44. Gialamas, I. D. & Tamvakis, K., *Dynamically induced spin-2 mass in a Weyl-invariant framework*, Phys. Rev. D 112, 084051 (2025) [arXiv:2503.16598].
45. Högås, M. & Mörtsell, E., *Bimetric gravity improves the fit to DESI BAO and eases the Hubble tension*, Phys. Rev. D 112, 103515 (2025) [arXiv:2507.03743].
46. Brizuela, D., de Cesare, M. & Soler Oficial, A., *Gravitational wave propagation in bigravity in the late universe*, JCAP 01 (2026) 048 [arXiv:2507.11526], doi:10.1088/1475-7516/2026/01/048.
47. Falah, A. K., Latief, A. O. & Alatas, H., *Stable Cosmology from Minimal Theory of Mass-Varying Massive Gravity*, **preprint** [arXiv:2507.21542] (2025).

Citadas via o corpus (níveis V-12i/V-13a já registrados em `docs/posicionamento_literatura.md`
§4): Woodard 2007; Sbisà, Eur. J. Phys. 36 (2015) 015009 [arXiv:1406.4550]; Schmidt-May &
von Strauss, J. Phys. A 49 (2016) 183001 [arXiv:1512.00021].

---

## 10. Log de busca

Data de todas as consultas: 2026-09-07. Resultados brutos fundidos e deduplicados em
`auditoria/code/out/litrev_pool_2026-09-07.csv` (coluna `sources` diz de quais consultas cada
registro veio).

| Base | Consulta (string exata) | Filtro | Resultados |
|---|---|---|---:|
| INSPIRE | `refersto:recid:1118524` (cita 1206.3852) | size 500, mostrecent | 160 |
| INSPIRE | `refersto:recid:1246930` (cita 1308.1647) | idem | 181 |
| INSPIRE | `refersto:recid:1288027` (cita 1404.0008) | idem | 128 |
| INSPIRE | `refersto:recid:1306601` (cita 1407.4331) | idem | 136 |
| INSPIRE | `refersto:recid:1319615` (cita 1410.0207) | idem | 92 |
| INSPIRE | `refersto:recid:1355521` (cita 1503.07436) | idem | 65 |
| INSPIRE | `refersto:recid:1513449` (cita 1702.04490) | idem | 18 |
| INSPIRE | `refersto:recid:1635858` (cita 1711.04655) | idem | 14 |
| INSPIRE | `(abstracts:higuchi or t:higuchi) and (abstracts:bimetric or abstracts:bigravity or t:bimetric or t:bigravity)` | — | 3 |
| INSPIRE | `fulltext:higuchi and (t:bimetric or t:bigravity or abstracts:bimetric or abstracts:bigravity) and date>2016` | — | 32 |
| INSPIRE | `(abstracts:bimetric or abstracts:bigravity) and (abstracts:chameleon or abstracts:"varying mass" or abstracts:dilaton or abstracts:"scalar field" or abstracts:"field-dependent")` | — | 0 (consulta suspeita) |
| INSPIRE | `fulltext:higuchi and (fulltext:"varying mass" or fulltext:"mass-varying" or fulltext:"time-dependent mass" or fulltext:"field-dependent" or fulltext:chameleon or fulltext:"scalar-dependent" or fulltext:quasidilaton or fulltext:quasi-dilaton) and (t:"massive gravity" or t:bigravity or t:bimetric or t:quasidilaton or t:"quasi-dilaton" or t:"varying mass" or t:"mass-varying")` | — | 59 |
| INSPIRE | `fulltext:"generalized Higuchi" or fulltext:"generalised Higuchi" or fulltext:"generalized Higuchi bound" or t:"Higuchi"` | — | 31 |
| INSPIRE | `(t:bimetric or t:bigravity or t:"bi-gravity") and (t:"scalar field" or t:scalar or t:dilaton or t:chameleon or t:varying or t:"scalar-tensor" or t:quintessence)` | — | 16 |
| arXiv API | `(all:bimetric OR all:bigravity) AND all:Higuchi` | max 300 | 11 |
| arXiv API | `(all:bigravity OR all:bimetric) AND (all:"gradient instability" OR all:"gradient instabilities")` | max 300 | 6 |
| arXiv API | `(all:bigravity OR all:bimetric) AND (all:chameleon OR all:"varying mass" OR all:"mass-varying" OR all:"time-dependent mass" OR all:dilaton OR all:"field-dependent" OR all:"scalar-dependent" OR all:"scalar field dependent")` | max 300 | 9 |
| arXiv API | `all:Higuchi AND (all:FLRW OR all:FRW OR all:cosmological OR all:"time-dependent" OR all:varying) AND (all:"massive gravity" OR all:bigravity OR all:bimetric OR all:"spin-2")` | max 300 | 16 |
| arXiv API | `(abs:bigravity OR abs:bimetric OR abs:"bimetric gravity") AND (abs:cosmolog* OR abs:Higuchi OR abs:instabilit*)` | filtro de data **não** aplicado | 183 |
| arXiv API | `(all:bigravity OR all:bimetric) AND all:"scalar field" AND (all:interaction OR all:potential OR all:coupling) AND (all:ghost OR all:stabilit* OR all:Higuchi)` | max 300 | 7 |
| arXiv API | `abs:Higuchi AND (abs:bound OR abs:ghost)` | max 300 | 46 |
| arXiv API | `(abs:bimetric OR abs:bigravity) AND (abs:DESI OR abs:"Hubble tension" OR abs:BAO)` | max 50 | 6 |
| arXiv API | `id_list` (34 ids de status/saídas) | — | 34 |
| arXiv API | `id_list` (30 ids de vizinhos/recentes) | — | 30 |
| Consensus | *Higuchi bound bimetric gravity cosmology time-dependent interaction parameters scalar field coupled* | plano gratuito | 3 |
| Consensus | *bimetric gravity scalar perturbations gradient instability early universe finite branch* | idem | 3 |
| Consensus | *generalized Higuchi bound time-dependent graviton mass FRW massive gravity helicity-0 kinetic term* | idem | 3 |
| Web | três consultas (chameleon bigravity Higuchi; bimetric gradient instability Vainshtein 2024–2025; Higuchi time-dependent mass FLRW) | — | ~30 links |
| ar5iv | texto integral: 1206.3852, 1308.1647, 1304.0449, 1403.5679, 1404.0008, 1410.0207, 1412.5979, 1608.06643, 1702.04490, 1711.04655, 1912.09449, 2101.08794 | — | 12 |

Totais: 1 283 brutos → 563 únicos → 128 marcados por palavra-chave → 12 textos integrais.
