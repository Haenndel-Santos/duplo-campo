# 01 — O que este documento é

**Nível epistêmico deste capítulo:** enunciado de enquadramento; toda
afirmação quantitativa aponta capítulo e fonte versionada.

## A tese em uma página

Este documento apresenta três coisas distintas, e insiste em não as
confundir.

**Primeiro, uma hipótese conceitual.** A TDCP postula que o estado
primordial contém dois graus de liberdade fundamentais correlacionados
(φ₁, φ₂), cuja dinâmica diferencial — carregada pelo modo φ₋ — pode
produzir uma bifurcação cosmológica: a separação do universo em dois
setores geométricos correlacionados. A existência de dupla geometria,
de uma variável temporal relacional e de aceleração emergente são
**hipóteses a serem derivadas e testadas, não postulados
estabelecidos** (a "afirmação mínima" de
`docs/plano_v2_reconstrucao.md`, mantida aqui como enunciado de
partida).

**Segundo, uma implementação matemática.** A F1 realiza a hipótese
sobre a gravidade bimétrica de Hassan–Rosen: g_{μν} (setor visível,
matéria acopla só a ela), f_{μν} (setor estrutural), potencial
β_n-modulado com F(φ₋). A implementação foi levada até o fim — fundo,
vínculos, setores tensorial e escalar, perturbações — e sobreviveu ao
próprio processo: o programa produziu um no-go interno aparente,
depois o derrubou ao localizar um erro numérico na sua própria
máquina de redução (Erratum-02; cap. 07). O estado atual, com fontes:

- **Fundo** ✓ — ramo finito com ṙ = H_g(ξ−r), limite GR exato,
  ponto fixo tardio (cap. 05; `docs/resultado_ramo_finito.md`).
- **Setor tensorial** ✓ — m_T²/H² → 12 universal no primordial,
  Higuchi automático (cap. 06; `derivations/02_setor_tensorial_mT2.md`).
- **Setor escalar** — dois graus de liberdade (um modo métrico + o
  espectador δφ₋), **sem fantasma** (o do Gate F era artefato
  numérico) e **são na era tardia**; mas com **instabilidade de
  gradiente (c_s² → −1) em r → 0**, que a cobertura antiga da cascata
  (a ≥ 100) não alcançava, e que o R-11 mostrou ser **propriedade da
  classe F1, não da célula** — nenhuma forma-β a evita (cap. 07;
  `auditoria/erratum_02_reducao_numerica.md`,
  `docs/resultado_r11_nogo_gradiente.md`).
- **Observação** — sub-horizonte consistente com GR dentro do piso da
  sonda (~2%); a massa tensorial é *predição* da família do benchmark,
  m_T ≈ 2.3 H₀ hoje; a janela quase-horizonte está em aberto e é o
  teste decisivo (cap. 09; `docs/resultado_r8a_quase_estatico.md`,
  `docs/resultado_r8b_limite_mH0.md`).

**Terceiro, uma fronteira honesta.** A saúde da implementação **não
prova a ontologia**. A identificação "φ₋ é o grau relacional
primordial que modula β_n" permanece **normativa** — decidida, não
derivada (G1-a: zero elos de identidade derivados na cadeia;
`docs/gate1_identidade_relacional.md`). O que o Erratum-02 mudou não
foi a natureza dessa fronteira, mas sua urgência: antes, o problema
aberto era se a F1 sobrevivia; agora, é derivar o vínculo entre
Φ₋ primordial, φ₋ modulador e a separação estrutural r = b/a
(cap. 08).

## O que este documento NÃO afirma

1. Não afirma validação observacional — nenhum C_ℓ foi calculado
   sobre o sistema corrigido (cap. 09, fila).
2. Não afirma a derivação da dupla geometria a partir do par
   primordial — a costura é normativa (cap. 08).
3. Não reutiliza nenhum número da v1 ou dos documentos anteriores a
   2026-08-12 sem o filtro de supersessão de
   `docs/resultado_r7_cascata.md` §4 — a v1 permanece congelada como
   registro histórico (`docs/decisao1_congelamento_v1.md`), com a
   auditoria de 856 equações como ponte.

## Relação com a v1

A v1 (39 arquivos) nasceu de conversas salvas e carrega camadas de
interpretação sem derivação. A Decisão 1 congelou-a como registro; a
auditoria (`auditoria/parecer_tecnico.md`) mapeou seus 115 erros; os
dois erratums (`auditoria/erratum_01_bianchi.md`,
`erratum_02_reducao_numerica.md`) corrigem, respectivamente, um erro
estrutural do corpus e um erro da própria máquina de auditoria. Esta
v2 reconstrói apenas o que tem derivação — na ordem ação → derivação
→ resultado → interpretação, com a interpretação por último
(cap. 10).
