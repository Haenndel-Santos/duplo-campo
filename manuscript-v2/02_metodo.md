# 02 — Método

**Por que este capítulo vem antes da física:** o método pegou cinco
testes vácuos, um erro estrutural do corpus (Bianchi, Erratum-01) e —
o caso máximo — o resultado central anterior do próprio programa
(Erratum-02); e, um dia depois, o instrumento numérico com que o
resultado central atual havia sido medido (Erratum-03, com duas
retratações internas emitidas na mesma sessão que as produziu). Num
projeto onde a mesma equipe deriva, implementa e julga, o método não
é ornamento: é o único árbitro que restou de pé em todas as crises.
Este capítulo o expõe como resultado.

## 1. As regras

1. **Estratificação epistêmica declarada.** Todo resultado carrega um
   nível: **1** (derivado e verificado por duas rotas independentes),
   **2a** (derivado por uma rota, verificado numericamente), **2b**
   (numérico com fronteiras de varredura declaradas), **3**
   (literatura/adotado). Fronteiras de varredura sempre no enunciado.
2. **Gates com critério de falha pré-declarado.** O critério de
   sucesso/falha é escrito no cabeçalho do script ANTES da execução;
   o veredito sai só pelos critérios. Rodadas ruins são preservadas
   nos outputs (as "1ªs rodadas" dos scripts R-6/R-7/R-8 estão todas
   no histórico git, com o que ensinaram).
3. **Auto-teste de poder.** Um teste que não consegue reprovar um
   caso sabidamente falso não pode aprovar nada (os ramos "PODER"
   dos gates; o F-a teve o poder reprovado e por isso o seu SUP nunca
   foi interpretado).
4. **Rota dupla para resultados estruturais.** Duas derivações
   independentes ou nada (Bianchi: rota canônica + rota lagrangiana;
   equivalência de ações no Erratum-02: prova exata off-shell).
5. **Rastreabilidade** (Gate 10): nenhuma afirmação interpretativa
   sem apontar a derivação; toda afirmação quantitativa cita o doc de
   resultado E o script/saída versionados.
6. **Derivadas ao longo do fundo em forma fechada.** Onde a forma
   fechada não for possível, estêncil de **ordem ≥ 8 com teste de
   refino obrigatório** (dois passos h, exigir estabilidade);
   `np.gradient` fica proibido em qualquer cadeia que passe por uma
   redução mal condicionada. O caso que impôs a regra: Ċ₃/Ċ₂ por
   `np.gradient` (2ª ordem) contaminou o valor de c_s² de R-7 a
   R-12c, porque o erro O(h²) é amplificado pelo condicionamento da
   redução (cond ≈ 1e11 em a = 0.01). A causa foi **demonstrada, não
   conjecturada**: trocando *só* a ordem do estêncil, a 2ª ordem
   reproduz a tabela antiga dígito a dígito (−1.01033852661 contra
   −1.010339 do R-10a) e **move com h** (−1.26086 → −1.01309 →
   −1.00117 para h = 1e−3, 3e−4, 1e−4), enquanto a 8ª ordem é estável
   em 14 dígitos. Fonte: `docs/resultado_r12_instrumento_e_cs2.md`
   §2; saída `auditoria/code/out/r12g_isola_ruido_e_classe.txt`.
6b. **O passo `h` não pode ser pré-escolhido — ele é refinado até
   convergir, e o `h` necessário depende do FUNDO.** *(Emenda de
   2026-08-17; a regra 6 permanece, é necessária e não suficiente.)* O
   caso que a impôs: no ramo infinito, com `r ~ 10⁸`, o mesmo `h = 1e−3`
   e o mesmo estêncil de **8ª ordem** dão `c_s² = −18760.8`; refinando,
   `3e−4 → −25.4`, `1e−4 → +0.496`, `1e−5 → +0.4999999`. **O teste que
   distingue truncamento de arredondamento:** subir `dps` de 60 para 250
   **não move** o número; baixar `h` move em cinco ordens de grandeza —
   logo **reportar os dois eixos**. E há um terceiro: o resíduo em `kh`
   é **massa**, cai como `1/kh²` e **não deve ser exigido zero**; o gate
   correto é extrapolação de Richardson em `1/kh²`. Fonte:
   `docs/auditoria_r13.md` §4.2; saída
   `auditoria/code/out/r13aud_c_cs2_ibb.txt`.
7. **Declaração de cegueira do gate.** Todo gate declara
   explicitamente **qual patologia ele seria incapaz de ver**, e essa
   declaração entra no cabeçalho junto com os critérios de falha.
   A regra foi proposta por **duas fontes independentes** — o próprio
   Erratum-03 e a síntese dos cinco pareceres, sem contato entre si
   (`docs/resultado_r12_instrumento_e_cs2.md` §5;
   `docs/pareceres_especialistas/00_sintese_cruzada.md` §2) —, que é
   o mesmo padrão de convergência que validou o Erratum-02. Dois
   casos concretos: **(a)** o calibrador do espectador δφ₋ (o `dchi`
   do código) deu `1.000000` em todos os pontos, de R-9a a R-12c,
   enquanto o modo métrico errava na primeira casa decimal — porque
   δφ₋ não tem termo giroscópico e o calibrador é **cego ao canal Ċ**
   (registro na saída da rodada retratada,
   `auditoria/code/out/r12a_forma_de_k.txt`); **(b)** os gates da
   cascata R-7 (autovalores de K₂, W00, envelope, lnA) são **cegos a
   instabilidade de gradiente por construção** — nenhum deles é
   sign(c_s²) — e foi exatamente por ali que o no-go de classe passou
   despercebido.
8. **Ansatz temporal declarado antes de comparar sinais.** Antes de
   comparar sinais de relação de dispersão entre fontes, **declarar o
   ansatz temporal de cada uma**; `sign(ω²)` não é grandeza comparável
   entre papers sem essa tradução. O caso que impôs a regra tem as duas
   fontes do **mesmo autor**, mesmo modelo, anos consecutivos:
   **Könnig et al. 2014** (arXiv:1407.4331) usa `X ∝ e^{iωN}` — logo
   `ω² > 0` é **oscilatório** e `ω² < 0` é **exponencial/instável**;
   **Könnig 2015** (arXiv:1503.07436 §IV) usa `Ξ ∝ e^{ωt}`,
   exponencial **real** — logo `ω² > 0` é **crescimento/decaimento
   exponencial** e `ω² < 0` é **oscilação**. O mesmo `ω² < 0` significa
   coisas opostas nos dois, e quem importar a eq. (24) de 1503.07436
   sem notar a troca lê estável como instável. Que é a mesma física,
   verificado: em w = 0 a eq. (40) de 1503.07436 dá
   `ω² = −c_{s,K}²(k/ℋ)²` com exatamente o `c_s²` que o R-12i extraiu
   de 1407.4331 — mesmo objeto, sinal trocado **pelo ansatz**, não pela
   dinâmica. **É a mesma família do erro do "0.28"** (cap. 07, Ato 4,
   nota sobre o limiar): tomar por comensuráveis objetos de convenções
   diferentes — lá o limiar de **outro modelo** lido como se fosse o
   nosso; aqui o sinal sob **outro ansatz**; e no cap. 06 §2.1 a
   margem de Higuchi, onde o nosso objeto tensorial era dividido por
   uma cota escrita para o funcional da fonte. Fonte:
   `docs/resultado_r13a_criterio_higuchi_fonte.md` §1.7 e §4.1;
   `docs/resultado_r12i_confronto_konnig.md` §1.5.

## 2. O caso máximo: Erratum-02 em quatro lições

Entre 2026-08-11 e 08-12, uma rotina numérica de redução de vínculos
(`reduz_ponto`, replicada de script em script desde o D-2) contava o
termo de conexão Ċ **duas vezes** nas entradas fora da diagonal de
W_XX. O erro valia 1.4–6.1% das matrizes — pequeno e *suave*. O que
ele produziu não foi ruído: foi um **terceiro grau de liberdade
escalar coerente**, com fantasma canônico "assentado" (ω₀/H ≈ 7–12),
banda de amplificação (lnA ≈ +4), enunciado de strong coupling e uma
previsão observacional falsificável (excesso ISW 2–8× em baixo-ℓ) —
tudo internamente consistente, convergente em resolução e aprovado
pelos gates da época. (Cadeia completa e queda: cap. 07; fontes:
`auditoria/erratum_02_reducao_numerica.md`, saídas r6b–r6d.)

**Lição 1 — consistência interna não é correção.** O sistema espúrio
era um sistema dinâmico legítimo — só que não era o da teoria. Todos
os validadores *internos* (V-ETA, V-RES, halvings) passavam porque
validavam o sistema errado contra ele mesmo.

**Lição 2 — representação única é ponto cego.** O bug era invisível
em qualquer teste feito na mesma representação (Γ–Γ com absorção).
Caiu quando uma construção ADM independente (reauditoria externa)
deu det K = 0 simbólico — e o repositório provou que as duas ações
eram A MESMA (r6c: identidade exata, racional, off-shell, por peças)
e localizou o erro linha a linha (r6d). Institucionalizado como
**V-XREP-b**: Γ–Γ vs ADM obrigatório a cada mudança da maquinaria; e
**V-XREP-a**: dois canais independentes de Ċ (grade vs simbólico) em
toda trilha — que, na estreia, pegou uma inconsistência real do fundo
Euler (R-7c, 8/8 braços bloqueados até a correção).

**Lição 3 — normalização é onde artefatos nascem.** Três episódios da
mesma família: as energias do R-2 (descartadas por poluição de
normalização), o "assentamento" canônico do Gate F-b (dividir por
√|λ₀| com λ₀ espúrio fabrica frequências estáveis), e as taxas de
envelope do R-7e (+11H que a autópsia reduziu a artefato de ω²(t)
variável — com normalização congelada, o campo DECAI). Regra
resultante: ganhos e taxas sempre com **normalização congelada**;
variáveis **equilibradas** (B̃ = kB, Ẽ = k²E) antes de qualquer
redução.

**Lição 4 — o gate que segura é o pré-declarado.** O R-7e disparou
SUSPEITO exatamente como desenhado e a leitura errada ("amplificação
na janela") nunca foi publicada; a autópsia decidiu com medidas
robustas e halving fino (`auditoria/code/out/r7e_halving_fino.txt`).
O contraste com a v1 — que publicava interpretação antes de
derivação — é o argumento deste capítulo.

## 3. O segundo ciclo: Erratum-03 e mais três lições

Em 2026-08-13 apareceu um segundo defeito de instrumento, desta vez
de **ordem de estêncil**, não de álgebra (regra 6): Ċ₃/Ċ₂ por
`np.gradient` em toda a cadeia de R-7 a R-12c. Ele é o inverso do
Erratum-02 num ponto que importa — não fabricou um resultado falso,
**inflou um resultado verdadeiro** e depois levou a "refutá-lo". Na
mesma sessão, o R-12a e o R-12c haviam concluído que c_s² saturava
num platô de −0.687 e que o c_s² = −1 era artefato de extrapolação:
**errado**, os dois herdaram o canal sujo e ficam **retratados** —
preservados no git como registro, não citáveis como resultado. Com o
instrumento limpo, o enunciado sobreviveu mais forte que antes:
c_s² = −1 em 108/108 células com |c_s² + 1| ≤ 1.1e−7, e o valor
passou de aproximado a exato. (Fonte:
`docs/resultado_r12_instrumento_e_cs2.md` §§1–4; saída
`auditoria/code/out/r12g_isola_ruido_e_classe.txt`.)

**Lição 5 — um erratum tem raio de alcance, e o raio se mede.** A
pergunta "o que precisa ser refeito?" não se responde por prudência
nem por pânico: mede-se. O R-12h comparou três variantes de Ċ no
mesmo ponto — A8 (Ċ₇ simbólico + estêncil de 8ª ordem, referência),
A2 (= R-10a…R-12c) e N2 (= R-1…R-8b, onde o defeito entra duas
vezes). No domínio do R-7/R-8 (a ∈ [100, 8e4] × kh ∈ [0.2, 20]) o
desvio máximo é 3.6e−4 em ω², 2.3e−4 nos autovalores de K₂ e 2.0e−6
em W00, e os **sinais** de (λK₂¹, λK₂², W00) são idênticos nas três
variantes em 16/16 pontos (sempre `++−`): a cascata R-7/R-8 é segura
estrutural e quantitativamente, e **dois itens caíram da fila** sem
serem executados. O controle positivo em a = 0.01, kh = 30 dá desvio
3.9e−2 — o harness reproduz o defeito onde ele existe, isto é, tem
poder (regra 3). E a fronteira não é só em `a`: na era tardia o
desvio vai de 3.6e−4 em kh = 20 a 9.3e−1 em kh = 1000, o que condena
a Parte B do R-9a e absolve a Parte A. Declarado como não-sondado: a
faixa a ∈ (0.05, 100) e o fato de o mapa ser amostragem em 16 pontos,
não escaneio contínuo. (Fonte:
`docs/resultado_r12_instrumento_e_cs2.md` §6; saída
`auditoria/code/out/r12h_raio_de_alcance.txt`.)

**Lição 6 — quando um gate reprova, o primeiro suspeito é o
comparador.** No R-9, três comparadores sucessivos foram descartados
antes de a autópsia achar a causa comum: o V-OM original comparava
taxas de envelope com a raiz local do oscilador (56%); o segundo usou
o invariante adiabático (31%, pior); o terceiro, a frequência local,
falhou por resolução (25%). A causa comum não estava no objeto: as
ICs do teste não eram adiabáticas, logo a taxa de envelope media
**transiente, não WKB**. A versão reportada — a quarta, por fase
acumulada, com os marcos sem resolução declarados — só existe porque
o instrumento foi julgado três vezes seguidas antes do objeto.
(Fonte:
`docs/resultado_r9_bloco0.md` §1 e §5 item 3; saída
`auditoria/code/out/r9a_omega2_diagnostico.txt`; as versões
descartadas ficam no histórico git.)

**Lição 7 — a lista de riscos herda a cegueira dos gates.** O
`docs/plano_v2_reconstrucao.md` fecha com "Onde o plano provavelmente
morre, se morrer", que ordena quatro candidatos por probabilidade de
falha: Gate 3.5 (Higuchi), Gate 4(d) (corredor seguro), Gate 6
(região viável) e Gate 2 (ghost). O que de fato derrubou a
suficiência da F1 como cosmologia foi o **Gate 4(b) — c_s² > 0**, que
**não está na lista**; e o Gate 3.5, apontado como o mais provável,
passou: Higuchi 400/400 no benchmark, pelas duas formas equivalentes
(R-13b §8.3). *A margem, porém, não é a que este capítulo anunciava:*
o `m_T²/H² → 12` é o **nosso** objeto tensorial, com ξ dinâmico,
enquanto o funcional de Higuchi em FLRW é a mesma expressão com ξ → r
e vale **3** no primordial — passa a cota 2 com margem de **1.5×**,
não de 6× (cap. 06 §2.1;
`docs/resultado_r13a_criterio_higuchi_fonte.md` §3.2;
`docs/resultado_r13b_ibb_ramo_infinito.md` §8.4;
`docs/resultado_ramo_finito.md` §1 e §3, anotados; script
`auditoria/code/ramo_dinamico_correto.py`). Que a correção tenha vindo
de comparar objetos de convenções diferentes é a regra 8 em ação. A
calibração de expectativa falhou na direção específica em que os
gates eram cegos: não havia gate de sign(c_s²) na cascata (regra 7,
caso (b)) e não havia c_s² na lista de riscos. É a mesma família de
ponto cego, agora visível um nível acima — no documento que existia
justamente para prever onde o programa morreria.

## 4. O placar do método

| Episódio | O que o método fez | Fonte |
|---|---|---|
| 5 testes vácuos (era da auditoria) | detectados por auto-teste de poder | `auditoria/parecer_tecnico.md` |
| Constraint de Bianchi errada no corpus | rota dupla derrubou; Erratum-01 | `auditoria/erratum_01_bianchi.md` |
| Vereditos congelados inválidos como dinâmica | D-2 (evolução real vs QEP congelado) | `docs/resultado_d2_evolucao.md` |
| O 3º DOF espúrio e toda a sua fenomenologia | auditoria externa + prova de mesma-ação + bug linha a linha; Erratum-02 | `auditoria/erratum_02_reducao_numerica.md`, r6c/r6d |
| Inconsistência Euler do fundo pousado | V-XREP-a na estreia (R-7c 1ª rodada) | `docs/resultado_r7_cascata.md` §3 |
| Artefato de envelope na janela | gate SUSPEITO + autópsia + halving fino | `docs/resultado_r7e_saude_interna.md` §2 |
| Ċ por `np.gradient` (2ª ordem) contaminando c_s² de R-7 a R-12c | causa demonstrada por troca de estêncil; retratação interna do R-12a/R-12c na mesma sessão; Erratum-03 | `docs/resultado_r12_instrumento_e_cs2.md`, saída r12g |
| Raio de alcance do próprio erratum | R-12h mediu o que precisava e o que **não** precisava ser refeito (cascata R-7/R-8 segura; dois itens caíram da fila) | `docs/resultado_r12_instrumento_e_cs2.md` §6, `auditoria/code/out/r12h_raio_de_alcance.txt` |

O que este placar significa: os resultados dos caps. 05–09 não são
confiáveis por terem sido calculados com cuidado — são confiáveis
porque o processo que os produziu já demonstrou, oito vezes, que
derruba os próprios resultados quando estão errados — e, quando o
erro é do instrumento e não do resultado, mede até onde ele foi antes
de decidir o que refazer.
