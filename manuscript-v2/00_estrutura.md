# TDCP v2 (enxuta) — Estrutura

**Criado:** 2026-08-11, executando a Decisão 1
(`docs/decisao1_congelamento_v1.md`). Este arquivo é o esqueleto
comentado; cada capítulo vira um arquivo `NN_titulo.md` nesta pasta.

**REVISÃO 2026-08-12 (pós-Erratum-02):** o esqueleto original tinha o
no-go escalar como resultado central (cap. 07) e excluía os capítulos
observacionais por falta de base saudável. O Erratum-02
(`auditoria/erratum_02_reducao_numerica.md`) mostrou que o 3º DOF
escalar era artefato de um bug da redução numérica; a cascata R-7
(`docs/resultado_r7_cascata.md`, `resultado_r7e_saude_interna.md`)
estabeleceu o sistema físico de 2 DOFs são em todos os regimes
testados; R-8a/b (`resultado_r8a_quase_estatico.md`,
`resultado_r8b_limite_mH0.md`) abriram o confronto observacional.
Caps. 01–02 e 07–10 e a lista de exclusões foram atualizados abaixo;
caps. 03–06 ficam como estavam (fundo, Bianchi e tensor não mudaram).
*(Bloco preservado como registro. **Parcialmente superado** pela
revisão de 2026-08-13 abaixo: "são em todos os regimes testados" vale
só para a era tardia — a cobertura da cascata era a ≥ 100 — e a base
observacional que este bloco declarava aberta ficou de validade
restrita.)*

**REVISÃO 2026-08-13 (pós-R-10/R-11/R-12; supersede em parte a de
08-12):** o arco R-10a → R-11 → R-12 mediu o que a cascata R-7 nunca
tinha testado — a era inicial, a < 100 — e estabeleceu um **NO-GO DE
CLASSE POR GRADIENTE**: na classe F1 (β₃ = 0, matéria só em g, ramo
finito), o escalar métrico tem **c_s² = −1 exato em r → 0** para
*qualquer* (β₀, β₂, β₄, μ) — 108/108 células, |c_s²+1| ≤ 1.1e−7 — com
cinética **positiva** (é gradiente, não fantasma), e **c_s² = +1 exato**
na era tardia; na célula mínima (β₂ = β₄ = 0) isso é **teorema** em
forma fechada (R-12b). Das quatro saídas, **três estão fechadas**
(modulação β₁(φ₋), screening de Vainshtein, forma-β) e a do **ramo
infinito foi REABERTA pelo R-12i e NOVAMENTE FECHADA pelo
R-13a/R-13b — por outra razão, e a substituição é parte do enunciado**.
A exclusão original, por ξ cruzar zero, está **REVOGADA**: é ponto por
ponto o quique de `b` que 1407.4331 §II/§VI trata e defende como
físico, com três argumentos, e nada aqui a ressuscita. A exclusão
vigente é **independente e de outra natureza** — nas células IBB
genuínas (β₂ = β₃ = 0, β₁ > 0, `0 < β₄/β₁ < 2μ^{3/2}`) o ramo infinito
**viola a condição de Higuchi durante toda a história**: `r′ < 0` em
100% da história em **108/108 células**, Higuchi satisfeito em **0 de
64 800 pontos**, contra **400/400** do controle positivo no ramo
finito. A contagem volta a **quatro rotas fechadas**, mas com a
exclusão do IBB **inteiramente substituída**, não confirmada — e a
porta que resta entreaberta passa a ser **uma**: β₃ ≠ 0, que sai da
definição de F1. **A era
instável cobre a recombinação** — o CMB linear da F1 não é calculável
enquanto este quadro valer. No mesmo arco entra o **ERRATUM-03**
(R-12): o Ċ era derivado por `np.gradient` de 2ª ordem de R-7 a R-12c,
e o defeito contaminou **valores**, não **enunciados** (o domínio
R-7/R-8 é quantitativamente seguro; o R-8a sequer passa pela cadeia).

O que isso muda **neste esqueleto**: (i) caps. 01 e 07 reescritos — o
07 ganha um **quarto ato** e deixa de terminar na revogação de um no-go
para terminar no estabelecimento de outro; (ii) o cap. 09 **deixa de
ser o centro de gravidade**: o teste decisivo que ele desenhava não é
executável, e o enunciado honesto é o de **validade restrita** (opção 3
de `docs/resultado_r10_consolidado.md` §4); (iii) o cap. 02 recebe as
duas regras novas do Erratum-03 (derivadas ao longo do fundo em forma
fechada, ou estêncil de ordem ≥ 8 com teste de refino obrigatório; e
declaração de cegueira de todo gate); (iv) a lista de exclusões volta a
excluir a reconstrução observacional — agora por falta de era
calculável, não por falta de implementação sã; (v) caps. 03–06 não são
tocados pelo arco, com uma única correção de escopo no cap. 05 §3 ("com
β constantes o setor escalar é são" → "são na era tardia"); e o cap. 08
§2–3 corrigido (o enquadramento R1 volta a ter objeto).
*Fontes: `docs/resultado_r10_consolidado.md`,
`resultado_r11_nogo_gradiente.md`,
`resultado_r12_instrumento_e_cs2.md`, `resultado_r12b_teorema_cs2.md`.*

**Estado da pasta (2026-08-13):** existem os arquivos `00`–`09`. O
**cap. 10 (Interpretação) ainda NÃO foi escrito** — não há
`10_interpretacao.md`. O esqueleto abaixo o descreve como plano, não
como texto existente.

**Regras da pasta (vinculantes):**

1. **Ordem do plano:** ação → derivação → resultado → interpretação por
   último (`docs/plano_v2_reconstrucao.md`). Nenhuma afirmação
   interpretativa sem apontar a derivação que a sustenta (Gate 10).
2. **Gate 0 ativo:** `python auditoria/code/verifica_simbolos.py --alvo v2`
   contra esta pasta a cada sessão de escrita; critério = zero
   violações. O `docs/dicionario_simbolos.md` é normativo — inclusive
   as flags epistêmicas (a identificação "φ₋ modula β_n" é normativa,
   não derivada; G1-a).
3. **Toda afirmação quantitativa cita fonte versionada** — o doc de
   resultado E o script/saída em `derivations/code/out/` ou
   `auditoria/code/out/`.
4. **Nível epistêmico declarado** (1/2a/2b/3) em todo resultado
   enunciado; fronteiras de varredura sempre declaradas.
5. **Três nomes distintos** para o que a v1 chamava "modo relativo"
   (σ escalar, S isocurvatura, h₋ tensorial) — a sobrecarga catalogada
   no G1-a não entra na v2.

---

## Esqueleto

### 01 — O que este documento é
A tese em uma página: uma hipótese conceitual (dois campos primordiais
correlacionados; separação estrutural), uma implementação matemática
(TDCP-F1 sobre Hassan–Rosen) levada até o fim — incluindo a queda do
no-go que o próprio programa havia produzido (Erratum-02) e, depois, o
no-go de classe que ele encontrou com o instrumento já corrigido. O
resultado honesto atual: fundo ✓, setor tensorial ✓, setor escalar com
2 DOFs (1 métrico overdamped + espectador δφ₋), **sem fantasma** e
**são na era tardia**, mas com **instabilidade de gradiente
(c_s² → −1) em r → 0** — que a cobertura antiga da cascata (a ≥ 100)
não alcançava e que o R-11 mostrou ser propriedade da CLASSE F1, não da
célula; nenhuma validação observacional (sub-horizonte consistente com
GR na era tardia; o quase-horizonte deixou de ser "em aberto" e passou
a **não executável** — validade restrita, cap. 09); a identificação
ontológica (φ₋ como
grau primordial) segue normativa, não derivada — o que mudou nela foi a
urgência, não a natureza. Relação com a v1 (congelada; auditoria como
ponte).
*Fontes: decisao1, erratum-02, resultado_r7_cascata,
resultado_r7e_saude_interna, resultado_r8a/b,
resultado_r11_nogo_gradiente, resultado_r12b_teorema_cs2.*

### 02 — Método (agora com o caso máximo)
Estratificação epistêmica (1/2a/2b/3); gates com critério de falha
pré-declarado; auto-teste de poder; rota dupla. O capítulo ganha seu
caso definitivo: o ERRATUM-02 — um bug de 1.4–6% numa rotina de
redução produziu, por meses, um "3º DOF", um fantasma, uma banda e
uma previsão observacional, tudo internamente consistente e validado
pelos gates de representação única; a queda veio de auditoria externa
independente + prova de equivalência de ações (r6c) + localização
linha a linha (r6d). Lições codificadas: V-XREP-a/b, equilibração de
variáveis, normalização congelada para ganhos, gates SUSPEITO. O
método não é ornamento: derrubou cinco testes vácuos, um erro
estrutural do corpus (Bianchi) e o próprio resultado central anterior.
*Fontes: parecer Parte III-B, erratum-01 §8, erratum-02,
resultado_r7_cascata §0.*

### 03 — A ação e o dicionário
A ação completa (F1), simetrias, dimensões; o potencial V(φ₊,φ₋)
explícito; o dicionário como contrato de notação. A escolha
arquitetural "modulador = φ₋" apresentada COM a flag: decisão
normativa (G1-a), não derivada — e testada adiante em duas etapas com
resultados distintos (cap. 07): pós-Erratum-02 a modulação é **sã** na
janela em que foi testada (era tardia, rolagem/condensação/pouso
inclusos — Ato 3); e **reprovou depois**, já como *saída* para a
instabilidade de gradiente, porque age ~3 ordens de grandeza tarde
demais (R-10c; Ato 4).
*Fontes: docs/acao_v2.md, dicionario_simbolos.md, gate1a (flag).*

### 04 — Vínculos e a constraint de Bianchi correta
Minisuperespaço; as duas rotas (canônica e lagrangiana) para
B(r)·(N_f·ȧ−N_g·ḃ)=0; por que a forma do corpus v1 era impossível
(constraint canônica não contém lapso); os dois ramos da fatoração; o
resíduo −M_eff²m²p_φβ₁′ quando β₁=β₁(φ₋) (a constraint não fatora com
modulação — Gate 2). Aqui o Erratum 01 vira conteúdo, não errata.
*Fontes: erratum_01_bianchi.md, gate2_ghost.md, gate2_bracket.py,
bianchi_rota_lagrangiana.py.*

### 05 — O fundo do ramo finito
ṙ=H_g(ξ−r); a cúbica e a seleção de raiz (menor positiva + filtros
que abortam); r∝a³ e ξ=4r no primordial; limite GR exato; ponto fixo
tardio; Ω_m≈0.25. O mecanismo de separação estrutural que a v1
procurava — sem campo modulador nenhum.
*Fontes: resultado_ramo_finito.md, ramo_dinamico_correto.py.*

### 06 — Setor tensorial
m_T²/H²→12 universal no primordial (todos os parâmetros cancelam); a
razão ≈4 hoje. **Higuchi automático — mas com margem 1.5, não 6**
(§2.1, `[REVISADO 2026-08-13, R-13a/R-13b]`): o "6" saía de aplicar o
bound 2 ao nosso m_T² com ξ dinâmico, e o funcional FLRW de Higuchi da
literatura é a forma em ξ→r, que no primordial dá **3**. O 12 fica; o
veredito fica (400/400 pelas duas formas); só a margem cai. A
invalidação do 0/60 da D8 como estudo de caso do método (fundo errado
⇒ resultado errado por construção).
*Fontes: resultado_ramo_finito.md §3–4, D2 (forma fechada),
resultado_r13a_criterio_higuchi_fonte.md, resultado_r13b_ibb_ramo_infinito.md.*

### 07 — O setor escalar: do falso no-go à saúde tardia, e daí ao no-go de classe por gradiente (resultado central)
A história completa em quatro atos, com números: (i) o no-go aparente
(taquião/fantasma/1500 pontos) e o que ele realmente media — o
sistema espúrio de 3 DOFs criado pelo bug da redução (Erratum-02);
(ii) a queda: auditoria externa (det K=0 simbólico) + prova local de
mesma-ação (r6c, exato) + o bug linha a linha (r6d) + reprodução
independente; (iii) o setor corrigido: 2 DOFs (1 métrico overdamped
decadente + espectador δφ₋ saudável), zero direções cinéticas
negativas em toda a cobertura testada — que era a era tardia, a ≥ 100
(benchmarks, classe μ×β₁ incl. fresta, trajetória de rolagem/pouso
incl. janela de deslocamento — W00 sem trocas, sem FJ-quebra),
consistente com o teorema HR e Comelli–Crisostomi–Pilo, com banda, ISW
e "strong coupling" retirados como artefatos; (iv) o no-go real, na era
inicial: c_s² = −1 exato em r → 0 para qualquer (β₀, β₂, β₄, μ) da
classe F1 (108/108 células), com cinética positiva — é **gradiente**,
não fantasma —, c_s² = +1 exato na era tardia, teorema em forma fechada
na célula mínima; quatro saídas testadas, **quatro novamente fechadas
— com a exclusão do ramo infinito inteiramente substituída**: o
argumento `ξ = 0` está REVOGADO (R-12i) e no lugar dele entra o **ghost
de Higuchi** (R-13a/R-13b), que reprova o IBB em toda a história
(108/108 células, 0/64 800 pontos); a era instável
cobre a recombinação; e o ERRATUM-03, que corrige *valores* sem tocar
*enunciados*. O quarto ato fecha na **complementaridade**: ramo finito
= Higuchi OK / gradiente ruim; IBB = gradiente saudável segundo a fonte
/ Higuchi ruim. Fronteiras e pendências declaradas (ramo algébrico
deferido; Vainshtein/validade linear no topo da fila; **uma** porta
entreaberta — β₃ ≠ 0, que leva para fora da F1; `c_s²` no IBB como
validação adicional desejável, não requisito do veredito).
*Fontes: erratum_02_reducao_numerica.md, resultado_r7_cascata.md,
resultado_r7e_saude_interna.md, resultado_r10_consolidado.md,
resultado_r11_nogo_gradiente.md, resultado_r12_instrumento_e_cs2.md,
resultado_r12b_teorema_cs2.md, resultado_r13a_criterio_higuchi_fonte.md,
resultado_r13b_ibb_ramo_infinito.md, saídas r6c/r6d/r7a–f/r10a–r13b.*

### 08 — O enquadramento R1 e a identificação normativa (a fronteira que fica)
Gate 1 completo, RELIDO pós-erratum: os quatro objetos identificados
só por decreto (G1-a) continuam por decreto — a saúde da F1 NÃO prova
a identidade φ₋ ↔ grau primordial; a projeção-δφ₋ (G1-b) e o trilema
(G1-c) mantêm-se como delimitação do que está derivado vs postulado.
O que muda **[REVISADO 2026-08-13]**: o problema aberto continua sendo
a DERIVAÇÃO do vínculo Φ₋/φ₋/r, e não a sobrevivência da implementação
— mas não porque a implementação esteja sã (ela é sã só na era tardia).
O G1-b ficou **sem objeto** (media modos do sistema espúrio, que não
existem), enquanto o enquadramento R1 **volta a ter objeto**: há
patologia real a enquadrar (a instabilidade de gradiente de classe). A
projeção do novo modo patológico sobre δφ₋ **não foi medida** —
pergunta aberta declarada, não conclusão.
*Fontes: gate1_identidade_relacional.md, gate1a, gate1c; releitura:
resultado_r7e_saude_interna §6, resultado_r11_nogo_gradiente.md.*

### 09 — O programa observacional: o que foi medido, e por que o teste decisivo não é executável
**[REVISADO 2026-08-13] Deixou de ser o centro de gravidade.** O que as
duas sondas do R-8 mediram fica de pé — o sub-horizonte quase-estático
e a massa tensorial como predição da família do benchmark (com o
postulado do corpus registrado como *não incorporado*) —, e nenhuma das
duas passa pela cadeia defeituosa do Erratum-03. O que muda é o
estatuto do resto: o teste decisivo que este capítulo desenhava — C_ℓ
de baixo-ℓ, P(k) nas maiores escalas, lensing sobre o sistema 2-DOF —
**não pode ser executado como planejado**, porque o objeto que ele
calcularia é linearmente indefinido na época em que o CMB se forma
(cap. 07 §4). O enunciado honesto do capítulo passa a ser o de
**validade restrita** (opção 3 de `docs/resultado_r10_consolidado.md`
§4): implementação de domínio tardio, sem previsão de CMB, com os
critérios de falseamento pré-declarados aplicáveis só dentro desse
domínio; o dicionário de épocas segue como decisão declarada. Ativos da
v1 que atravessam, reavaliados.
*Fontes: resultado_r8a_quase_estatico.md, resultado_r8b_limite_mH0.md,
resultado_r10_consolidado.md, resultado_r12_instrumento_e_cs2.md §6,
r8_dicionario_epocas_opcoes.md.*

### 10 — Interpretação (por último, como manda o plano) — **NÃO ESCRITO**
**Estado (2026-08-13): este capítulo não existe como arquivo.** A pasta
tem `00`–`09`; não há `10_interpretacao.md`. O que segue é plano, não
texto — e vale como plano *revisado*, porque o arco R-10/R-11/R-12 mexe
no que ele teria de dizer.

O que a narrativa significa À LUZ do estado atual: a separação
estrutural existe e evolui (cap. 05); a implementação F1 é sã na era
tardia mas não basta como cosmologia (cap. 07 §4), e a "memória da
bifurcação" segue SEM portador derivado (cap. 08 — a fronteira honesta
não mudou de natureza; mudou de urgência primeiro, e depois de
contexto); as fórmulas de tempo relacional da v1 continuam metáfora até
derivação; η aposentado do núcleo. O que os dois episódios significam
para o programa: a teoria sobreviveu ao seu próprio processo duas vezes
— derrubando um no-go que era artefato do seu instrumento e depois
encontrando, com o instrumento corrigido, o no-go verdadeiro. O
resultado é o par (método que se autocorrige, implementação cuja
suficiência cosmológica caiu), não uma validação.
*Fontes: caps. anteriores; plano_v2 Passos 9–10;
resultado_r10_consolidado.md §4, resultado_r11_nogo_gradiente.md §4.*

---

## O que fica de fora (por decisão, não esquecimento)

- **[REVISADO 2026-08-13 — supersede a revisão de 08-12]** Reconstrução
  dos capítulos observacionais da v1 (Cap.18–25): **continua fora**. A
  revisão de 08-12 dizia que "a base saudável para μ/Σ/fσ₈ EXISTE agora
  (R-8a/b)" e condicionava a reconstrução ao R-8 completo; isso não se
  sustenta com validade restrita — a base é sã apenas na era tardia, e
  a era instável cobre a recombinação, de modo que não há observável
  linear calculável na época em que o CMB se forma. A condição real
  passa a ser: **ou** uma saída que devolva c_s² > 0 em r → 0 (hoje só
  β₃ ≠ 0, que sai da F1 e obriga a refazer o fundo), **ou** um
  tratamento não-linear da era instável (fora do alcance do projeto
  hoje) — e, enquanto nenhuma das duas existir, o que cabe é o
  enunciado de validade restrita do cap. 09. Os números da v1 seguem
  inutilizáveis pelo motivo antigo, inalterado: eram do sistema
  espúrio.
- Anexos I–K (linha exploratória quântica): permanecem na v1
  congelada; sem ponte com a ação (G1-a linha 18).
- O ramo algébrico e a Investigação 2 original: substituídos pela
  releitura pós-erratum (R-7e/f); o ramo algébrico segue deferido com
  prior declarado.
