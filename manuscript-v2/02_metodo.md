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
passou com folga: Higuchi 400/400, m_T²/H² → 12 contra a cota 2H² —
margem de fator 6 no primordial (`docs/resultado_ramo_finito.md` §1 e
§3; script `auditoria/code/ramo_dinamico_correto.py`; cap. 06 §2). A
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
