# Prompt de continuação — próxima sessão

Copiar o bloco abaixo como primeira mensagem da próxima janela.
(Atualizado 2026-08-11, pós-fechamento do Gate 1, Investigação 1 e
Decisão 1 — v1 congelada, v2 enxuta iniciada.)

---

Continuação do trabalho na Teoria do Duplo Campo Primordial (TDCP).
Repositório: https://github.com/Haenndel-Santos/duplo-campo (público,
branch master). DUAS cópias de trabalho: máquina 1 =
C:\Haenndel Projects\Duplo Campo (tem .venv pronto); máquina 2 =
C:\Haenndel Projects 2\Duplo Campo (origem da v2). REGRA OBRIGATÓRIA:
`git pull` AGORA, antes de qualquer coisa; `git push` ao fechar; nunca
force-push. Cálculos oficiais SEMPRE pelo .venv (requirements fixado:
sympy 1.14.0, numpy 2.5.1, scipy 1.16.3; na máquina 2, criar o .venv se
ainda não existir).

ANTES DE QUALQUER COISA, leia nesta ordem:
1. docs/veredito_setor_escalar_final.md (com o §6 novo) — o arco
   completo: no-go do setor escalar, fronteiras, e o fechamento do
   ramo algébrico.
2. docs/gate1_identidade_relacional.md §§7–9 — GATE 1 FECHADO:
   G1-b (R1 passa, 17/17 com projeção 0.0000), G1-a (zero elos de
   identidade derivados na cadeia), G1-c (prior W–W parcialmente
   demolido; circularidade HR–Goldstone; critério anti-circularidade
   VINCULANTE para a Investigação 2).
3. docs/resultado_investigacao1_ramo_algebrico.md — ramo algébrico
   pós-erratum: degenerado E taquiônico (3.0H, k-independente) na raiz,
   sem corredor saudável em δ∈[−0.30,+0.30]. NO-GO.
4. docs/gate1c_nota_trilema.md — a nota do trilema inteira (é curta e
   é o documento de projeto da Investigação 2).
5. docs/decisao1_congelamento_v1.md + manuscript-v2/00_estrutura.md —
   DECISÃO 1 TOMADA: v1 congelada como registro histórico; v2 enxuta
   em manuscript-v2/ (esqueleto de 10 capítulos pronto).
6. Se precisar do fundo: auditoria/erratum_01_bianchi.md,
   docs/resultado_ramo_finito.md, docs/no_go_beta_constante.md,
   docs/estrutura_par_relativo.md, auditoria/parecer_tecnico.md
   (Parte III-B), docs/project-master.md (sincronização).

ESTADO ATUAL (2026-08-11, master sincronizado até 647c42e+, tree limpo):
- Auditoria 856/856 + parecer. ERRATUM 01 confirmado. RAMO FINITO:
  fundo ✓, tensor ✓ (m_T²/H²→12). SETOR ESCALAR: NO-GO consolidado
  (β constante ~1500 pts; modulação β₁(φ₋); ramo finito; ramo
  algébrico — TODAS as portas internas da F1 fechadas).
- GATE 1 FECHADO (a+b+c). R1 é o ENQUADRAMENTO OFICIAL do no-go: a
  patologia é da representação F1 (setor de vínculos: dubleto
  B_g±B_f / lapso Φ_f), não do grau relacional primordial (projeção
  zero em δφ₋). Trilema decidido: (a) fechado; (b) braço de trabalho,
  alvo (b1) = só o multiplete massivo emerge; (c) fallback declarado.
- DECISÃO 1 TOMADA: congelar v1 + v2 enxuta (manuscript-v2/, Gate 0
  ativo: verifica_simbolos.py --alvo v2 = zero violações).
- PENDÊNCIA MÁQUINA 2: commitar auditoria/code/out/ (git status lista
  após o pull) — início da próxima sessão de lá.

FILA (duas trilhas paralelas e independentes):
- TRILHA DE ESCRITA: v2 enxuta, capítulo a capítulo, seguindo
  manuscript-v2/00_estrutura.md (10 caps; regras vinculantes no topo
  do arquivo: Gate 0 a cada sessão, fonte versionada em toda afirmação
  quantitativa, nível epistêmico declarado, três nomes para o antigo
  "modo relativo"). Começar pelo 01 ou pelo 07 (o resultado central).
- TRILHA DE CÁLCULO: Stückelberg (C1) EXECUTADA 2026-08-11
  (resultado_stuckelberg_goldstone.md): circularidade elevada a 2a+2b;
  taquião k=1 É o helicity-0 (π_L 0.995+); mecanismo corrigido —
  massa taquiônica = resíduo (~1%) de cancelamento quebra×EH.
  INVESTIGAÇÃO 2 FASE A EXECUTADA 2026-08-11
  (investigacao2_fundo_rolagem.py; docs/resultado_investigacao2_faseA.md):
  fundo de rolagem p_φ≠0 EXISTE, desloca ORDEM 1 dos dois ramos
  (|H−rH_f|/H até 0.48) e pousa de volta no ramo finito (6e-5); a
  condensação DIRIGE r (0.031→0.498, ×16) — narrativa da bifurcação
  realizada no fundo (saúde escalar em aberto). ACHADO: a interação HR
  resiste à condensação (soma Δ=2m²M_eff²b1₀(ξ+3r)/v*² à massa² da
  origem; limiar m_χ²≳2.7 na REF v*=1, confirmado 8/8 na releitura —
  critério codificado era defeituoso, reclassificação declarada no
  doc). χ* previsto 0.931 vs 0.932 observado. FASE B EXECUTADA
  (investigacao2_faseB_pert.py; docs/resultado_investigacao2_faseB.md):
  INVESTIGAÇÃO 2 CONCLUÍDA, NEGATIVA — o no-go se ESTENDE ao regime
  não-fatorado (σ/H sobe com o deslocamento até 13.08 na janela, sem
  ponto limpo; pousa em 4.25, dentro da família estacionária
  3.85–4.43 — continuidade perfeita); contagem 3 em toda parte (sem
  BD na rota numérica; não certificador); balanço rI varrido
  0.07–0.66 SEM ilha saudável; R1 REFORÇADO no dinâmico (patologia
  δφ₋-espectadora mesmo com F′≠0 e χ̇≠0; a instabilidade de
  condensação é δφ₋-dominada e SARA ao assentar — duas
  instabilidades, destinos opostos). Fronteira: uma trajetória
  (g=2, m30), célula REF, k∈{1,10}, leitura congelada (caveats no
  doc). COM ISSO: itens 3.4 E 3.5 do veredito FECHADOS — O ARCO
  COMPUTACIONAL DA F1 ESTÁ COMPLETO (fundo ✓, tensor ✓, escalar ✗ em
  todos os regimes acessíveis: constante, modulado-estacionário,
  algébrico, dinâmico não-fatorado). R2 só continua FORA da F1
  (critério anti-circularidade do gate1c). Restam na F1 só saídas de
  prior baixo (β₂/β₄; F2 β₃≠0) — opcionais. Pendência menor: abort
  g=1/m30 da Fase A (indeterminado; não bloqueia nada).

POSICIONAMENTO NA LITERATURA FEITO (2026-08-11,
docs/posicionamento_literatura.md — 4 verificações paralelas com
disciplina fonte-verificada): a instabilidade conhecida do ramo finito
é de GRADIENTE (∝k) e transiente — nosso taquião de MASSA persistente
no dS tardio é novo SE físico (tensão com a literatura ⇒ carga de
prova alta); Higuchi-automático é conhecido (Könnig 1503.07436 — citar,
não reivindicar); m_T²/H²→12 é novo mas POR ERA (radiação daria outra
constante); a classe-irmã é o chameleon bigravity (1702.04490 —
análise de vínculos é LACUNA explícita deles, nossa oportunidade); o
fenômeno "fora dos dois ramos com pouso" não tem precedente; a medida
Stückelberg é nova COMO MEDIDA (citar Aoki-Maeda-Namba 1506.04543 como
precedente qualitativo); (b1) tem genealogia (ISS 1971 f-dominance;
FQH chiral graviton Nature 2024) e checklist de obstáculos. ITENS
PRÉ-PAPER (do §2 do doc): D1 EXECUTADO E RESOLVIDO A FAVOR
(d1_reducao_vinculos.py; docs/resultado_d1_reducao.md): redução FJ
exata = espectro idêntico ao QEP nos 4 pontos; taquião persiste;
fantasma = autovalor negativo de K_red (invariante — supera a ressalva
de k-dependência); disputa 2-vs-3 do corpus resolvida (3 = congelado,
dupla rota; 2 = esperado pós-secundária); NOTA DE CONVENÇÃO: k físico
(a→1) vs k comóvel a=10 da Investigação 1 — valores batem sob
k_phys=k/10. D2 EXECUTADO 2026-08-11 (noite) COM REVERSÃO MAIOR
(d2_evolucao_reduzida.py, 2 rodadas + sondas;
docs/resultado_d2_evolucao.md — LER PRIMEIRO NA PRÓXIMA SESSÃO):
⚠ O TAQUIÃO TARDIO CONGELADO NÃO É DINÂMICO. Evolução real do sistema
reduzido (redução dependente do tempo com termos Ċ, validada em GR,
halving ✓): no ponto fixo TODAS as soluções diluem (−3/2·H, oscilador
saudável) contra σ congelado 3–6.8H persistente; projeção no automodo
taquiônico drenada; crescimento real só TRANSIENTE e tipo-gradiente
na transição (a∈[15,45], taxa ∝ k, lnA~4), convergindo com a
literatura ("saudável tarde"). CAUSA: matrizes comóveis nunca
assentam (K~a³, |K̇|/|K|~2H no ponto fixo) — o congelado descarta os
termos dominantes. CONSEQUÊNCIA (veredito §8): TODOS os vereditos de
saúde escalar por espectro congelado (no-go β-constante, modulação,
ramo algébrico, Fase B) estão SUSPENSOS como vereditos dinâmicos —
válidos só como caracterização do espectro congelado. FICA: fundo ✓,
tensor ✓, Fase A (fundo não-fatorado), limiar de back-reaction, e a
ASSINATURA CINÉTICA INDEFINIDA (fantasma estrutural, D1 — a evolução
linear não testa fantasma; letalidade é a pergunta central agora).
R-1 EXECUTADA 2026-08-11 (noite;
r1_reavaliacao_nogo_evolucao.py; docs/resultado_r1_reavaliacao.md):
14/14 CÉLULAS TARDIA-DILUI, ZERO CRESCEM — o no-go tardio congelado é
VÁCUO em todo o espaço amostrado (escada de μ 0.3–100 na REF; lei de
escala; fresta μ=0.1; cantos; k_c=10 e 100). Setor escalar tardio da
F1 β-constante é LINEARMENTE ESTÁVEL nas células testadas. DOIS
ACHADOS ESTRUTURAIS: (i) negK=1 UNIVERSAL — o fantasma estrutural
(uma direção cinética negativa em K_red a=400) é propriedade da
CLASSE, não de um canto; letalidade é A pergunta restante; (ii)
amplificação transiente lnA_max varia 3.9→14.6 (fresta μ=0.1 é a
PIOR, e^14.6≈2e6) — a instabilidade real da classe é a transiente de
transição tipo-gradiente (consistente com a literatura), dano depende
de célula/k. R-2 EXECUTADA 2026-08-11 (noite;
r2_fantasma_estrutural.py; docs/resultado_r2_fantasma.md — o doc
CORRIGE o veredito impresso pelo script, autocrítica de instrumento):
SÓLIDO (invariante): a assinatura negativa de K_red é UNIFORME em k
(1..300 — a velha ambiguidade do kN não existe no reduzido),
PERSISTENTE em a (30..1900) e universal nas células; em k baixo o
modo é Ψ_f-puro com E<0; em k alto funde com o taquião em quarteto
complexo (assinatura congelada de mistura). DESCARTADO (poluição de
normalização): magnitudes de E entre configurações e a escala-μ
(expoente 0.19 não significa nada; a lei μ³ antiga também era
normalização-dependente). CONCLUSÃO: a LETALIDADE do fantasma é
INDECIDÍVEL na ordem quadrática — exige normalização canônica/strong
coupling (fronteira do programa; a literatura está no MESMO impasse).
ENUNCIADO HONESTO DO SETOR ESCALAR (rascunho do veredito p/ cap. 07,
resultado_r2_fantasma.md §3): dinamicamente estável no tardio;
instabilidade real = transiente de transição; direção cinética
negativa estrutural universal com letalidade aberta — A TDCP-F1 NÃO
ESTÁ EXCLUÍDA no nível em que o programa pode julgar; o no-go fica
reclassificado para "sem veredito de exclusão".
DECISÃO DE PRIORIDADE DO AUTOR (2026-08-11, noite;
docs/gate_fantasma_estrutural.md): NÃO partir para TDCP-2 — a F1
ganhou sobrevida real. FILA REORDENADA: (1) R-3 EXECUTADA 2026-08-12
(r3_faseB_evolucao_rolagem.py, colaboração das duas sessões — 3
iterações de andaime documentadas; docs/resultado_r3_rolagem.md;
controles TODOS passam, incl. o primeiro controle POSITIVO de poder do
programa): (i) R3-ROLAGEM NÃO-REALIZA nos dois k (bloco métrico DECAI
−1.84H onde congelado diz +12.4H; PODER prova que congelado-de-verdade
realiza) — a extensão do no-go ao não-fatorado é VÁCUA como dinâmica,
3ª confirmação do watershed; (ii) MODO DE CONDENSAÇÃO SOBREVIVE à
dinâmica real como o candidato do Cap.1: tipo-MASSA, só IR, acompanha
a espinodal do fundo (+1.09 vs 0.95/H), satura no pouso, decai tarde —
identificação suportada no nível de MECANISMO (identidade segue
interpretativa, G1-a); transiente métrico é tipo-GRADIENTE; (iii) NOVO:
crescimento tardio REAL ~+1H na família modulada-POUSADA (k_c=12500:
todas as ICs; ~k-independente; abaixo do limiar CRESCE) — hipótese
nomeada: bombeamento paramétrico pelas oscilações residuais de χ
(ω_χ/H≈4.4; mesmo k_phys na fase rolante DECAI); teste declarado:
reintegrar com oscilações amortecidas ou janela a>50000. R-3b
EXECUTADA 2026-08-12 (docs/resultado_r3b_pousada.md): achado
CONVERGIDO (halving k=12500, Δ=0.0031 — caveat §3.4 resolvido);
hipótese paramétrica REFUTADA (crescimento persiste e sobe com χ
amortecido: +0.98→+1.12 em k=12500, +1.05→+1.87 em k=1250; sonda de
banda negativa — burst do pouso é época-fixo, não k-fixo); ESTRUTURA
IR: k_c=25000 NÃO cresce na tardia (+0.06 onde o congelado diz 41.7 —
o dado congelado-vs-real mais dramático da série) — o crescimento
vive em k_phys≲1.5; pouso tem componente de anel real (~×0.6);
negK=1 insensível a oscilações/drift. AUTOCRÍTICA DECLARADA: o fundo
amortecido (Γ=30) aproxima o ponto fixo MAIS DEVAGAR (0.7/H) que o
envelope original (3/2 H) — na tardia carrega desvio secular MAIOR
(3.7e-2 vs 1.6e-2); logo "PERSISTE" estabelece NÃO-PARAMÉTRICA, mas
genuína-vs-secular fica ABERTO. R-3c EXECUTADA
2026-08-12 (docs/resultado_r3c_mecanismo.md): PONTO-FIXO (taxa plana
0.98–1.21 sob distância real ao ponto fixo ~1%→7% — não é secular) E
ESQUINA-β₁: o β-constante ESTÁTICO β₁=4.47 cresce igual (+1.08 na
banda, com δχ desacoplado EXATO — consistência de fiação) — o
fenômeno é DA CLASSE β-constante na região (β₁?, k_phys~H); o pousado
herda do ponto onde senta; releitura por cruzamento de horizonte
(k_c=25000 cruza fora da janela — a "estrutura IR" era isso); duas
componentes de modo (par E_f cresce cedo em todos os fundos; par Ψ_f
na banda tardia); anomalia IR do pousado k=1250 (cresce só com
dinâmica residual; morre no estático e no Γ=100) DECLARADA ABERTA.
R-4A EXECUTADA 2026-08-12 (docs/resultado_r4a_mapa.md) — O RESULTADO
QUE FIXA O ENUNCIADO: (i) R4a-NULL PASSA (GR com cruzamento DENTRO da
janela: tudo negativo — a banda não é artefato); (ii) R4a-MAPA:
β₁=1 CRESCE na banda (+0.93; β₁=2/3/4.47: +0.81/+0.93/+1.06) — a
AMPLIFICAÇÃO DE BANDA É DA CLASSE INTEIRA β-constante, taxa ~
+0.8–1.1/H quase independente de β₁, ativa em k_phys/H ~ 0.5–30
(componente E_f em kh alto, par Ψ_f perto do cruzamento), morta no IR
profundo — SEM contradição com R-1/D2: as janelas antigas tinham
kh≤0.5 ("estável tarde" = estável no IR amostrado; atualização
anotada no doc R-1), e o "transiente de transição" do D2 era muito
provavelmente esta banda cruzada pelos modos daquela época (kh
1.2→0.4 em [15,45]!); (iii) R4a-EXT: TRANSIENTE-DE-CRUZAMENTO nos
dois fundos (tardia2 kh 0.37→0.16: −1.06/−0.72) — amplificação POR
MODO com lnA finito (lnA_met 11–18 nos braços; base comóvel). NOVO
RASCUNHO DO ENUNCIADO no §4 do doc R-4a (substitui o do R-2 §3 como
candidato p/ cap. 07): a viabilidade é OBSERVACIONAL — e^lnA dos
modos que cruzam nas épocas relevantes vs vínculos. negK=1 universal
até a=70000 (Gate F reforçado). R-4B EXECUTADA 2026-08-12
(docs/resultado_r4b_forma.md) — OS NÚMEROS DO CONFRONTO: NULL passa
(GR passagem = −4.33) e AUTOSIM passa (Δ=0.33 — uma medida por fundo
vale p/ todo k). lnA_PASSAGEM (kh 20→0.2) UNIVERSAL: +3.97 (β₁=1;
k×3: +3.64), +3.62 (β₁=4.47) — cada modo métrico ganha e^{3.6–4.0} ≈
40–55× na amplitude (contraste líquido vs GR: e^~8; LIMITE INFERIOR:
kh 40–20 já cresce +2.7–4.1, banda completa ≈ e^{6–7}). AVISOS DE
LEITURA (doc §2): máximos por janela SOBRECONTAM ~2× (rotação de
componentes E_f↔Ψ_f — a estatística robusta é a passagem líquida por
IC); o próprio GR tem positivos de janela até +1.25 no freeze-out.
POUSADO modula: supressão pré/durante condensação (−0.21 em
a_cross=500, U₀ domina H²; vale +1.57 em 1600) e realce no anel
(+4.80 em 4000; bursts época-fixos +8.8/+11.4), convergindo a
~+4.0–4.5 no pousado profundo. negK=1 em tudo. SEQUÊNCIA DECIDIDA PELO AUTOR (2026-08-12): Gate F-a ANTES do bloco 3
(o F-a3 certifica a banda contra a dúvida do vínculo). GATE F-a
EXECUTADO 2026-08-12 (docs/resultado_gatef_a.md): (i) F-a3 ENTREGOU —
**BANDA-FÍSICA nos dois fundos** (lnA na superfície do candidato =
genérico: 3.98 vs 3.97 em β₁=1; 3.15 vs 3.62 em 4.47, marginal
Δ=0.47; BASE reproduz R-4b ao centésimo) → a banda NÃO é alimentada
pela componente fora-da-superfície da direção K<0 → BLOCO 3 LIBERADO;
(ii) F-a1/F-a2 INCONCLUSIVOS POR INSTRUMENTO — o portão abortivo
PODER disparou como desenhado (nenhuma conclusão falsa): o QEP
agrupado NÃO vê o modo rígido verdadeiro (o ω²~10⁹ do R-2 nunca
aparece; sobrevivente ω/H≤18.5 com R≈1) e a construção de superfície
na base própria de K_red comóvel herda a POLUIÇÃO DE NORMALIZAÇÃO do
R-2 §2 (δ_rel≡0.000 na superfície real E na falsa; genéricas O(1)) —
autovetores escala-dominados, teste sem dente. Saída pré-declarada:
H-CONSTRAINT NÃO DECIDIDA → **F-b necessário** (normalização canônica
simplética por ponto com termos ∝Ṫ retidos; o F-a vira o "antes" do
par antes/depois). Dado descritivo: proj(pesado-sobrevivente, K<0) =
1.000 tardio, ω/H 5.6→18.5. FILA ATUAL: (1) BLOCO 3 DO R-4 = DECISÃO
DO AUTOR (dicionário de épocas modelo-brinquedo → história cósmica;
confronto e^lnA vs vínculos Comelli/Könnig/Akrami; notas de desenho:
a era Λ real tem ~0.7 e-fold → lnA real é integral PARCIAL p/ modos
saindo; o cenário modos-ENTRANDO na era de matéria nunca foi sondado
— braço com ρ₀ grande; opções A/B/C, recomendação B+C); (2) F-b;
(iv) lnA_met
14.2–17.8 — transientes GRANDES; aviso: contagens do QEP 7×7 nas
âncoras comóveis extremas não são interpretáveis (pareamento instável;
usar a reduzida 3×3). (2) R-4 = mapa lnA(célula,k) do transiente vs
vínculos + follow-up do crescimento paramétrico (§1.3 do doc R-3) — a
sobrevida é CONDICIONAL a isto; AGORA URGENTE; (3) GATE F = letalidade da direção K<0, três etapas com
critérios pré-declarados: F-a teste da constraint secundária
linearizada (H-CONSTRAINT — hipótese MAIS BEM SUPORTADA: contagem
3-congelado vs 2-esperado + frequência do modo crescendo com a,
"quer ser vínculo"; barato, fazer primeiro), F-b normalização
canônica (H-NORM/H-SC), F-c interações (H-GHOST, só se F-b indicar
fantasma físico). Ramos de saída pré-declarados no doc. (4) enunciado
final → cap. 07 → paper. Programa de emergência (trilema b1) EM
ESPERA — reativável só se Gate F der H-GHOST. Gate 1 ganhou §11
(pós-D2: a motivação "σ emergente porque taquiônico" está anulada; o
achado documental G1-a permanece). D3 segue barato. EIXO DO PAPER:
aviso metodológico + reconciliação + fundo/tensor/não-fatorado +
Gate F como pergunta central.

DECISÕES EM ABERTO DO USUÁRIO (não decidir sozinho):
2. Formato de publicação do no-go (nota técnica / paper / abertura da
   v2 — o cap. 07 da v2 é o vehículo natural se decidir extrair;
   estratégia em camadas recomendada em sessão: v2+Zenodo/DOI →
   paper arXiv/journal → essay opcional).
3. Atualização do artifact do parecer (🔭) com o arco erratum+no-go.

REGRAS DE MÉTODO (aprendidas a ferro; seguir sempre):
- Estratificação epistêmica (Nível 1/2a/2b/3). NUNCA "CONFERE" para o
  declarado-mas-não-derivado; "bate com a literatura" é Nível 3 (dois
  priors de literatura já caíram por cálculo; o W–W foi o terceiro a
  ser cortado — sobrealcançava).
- Todo teste novo com auto-teste de PODER DE DETECÇÃO, mesma rota e
  mesmo fundo.
- Saúde espectral = σ E kN, em k=1 E k=10 no mínimo. k é COMÓVEL.
- Seleção de raiz: menor raiz real positiva + filtros físicos que
  ABORTAM (ξ>0, H²>0).
- Ponto fixo = juiz sem caveat de congelamento.
- CRITÉRIO ANTI-CIRCULARIDADE (novo, gate1c §3): construção R2 que
  quebra difeos relativas sem demonstrar saída do domínio varrido é
  F1 renomeada — reprovada por herança.

REGRAS DE EXECUÇÃO:
- Cálculos pesados: usuário roda no VS Code (.venv) e devolve saídas;
  py_compile e sondagens curtas na sessão são OK.
- manuscript/ (v1) é REGISTRO HISTÓRICO CONGELADO — não editar. NUNCA
  regenerar .docx/PDF (a regeneração planejada em 2026-08-05 foi
  CANCELADA pela Decisão 1). Escrita nova: só manuscript-v2/.
- Mudou versão de dependência → re-rodar derivations/code/ contra as
  saídas oficiais antes de commitar.

PENDÊNCIAS MENORES (fora da linha principal): flag do Erratum 01 na
tabela de âncoras do registro_formulas.md (D5/D8 — 1 linha);
lote05_C22_galileon_stability.py nunca rodado; Gate 2 Parte B (ADM
completo) só se a modulação voltar; Higuchi generalizado μ≠1
provisório.

Comece por: git pull → escolher a trilha da sessão (escrita: próximo
capítulo da v2 | cálculo: Stückelberg ou Investigação 2) → trabalhar.
