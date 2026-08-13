# Prompt de continuação — próxima sessão

Copiar o bloco abaixo como primeira mensagem da próxima janela.
(Atualizado 2026-08-12, pós-ERRATUM-02 e reexecução R-7 da cascata.)

---

Continuação do trabalho na Teoria do Duplo Campo Primordial (TDCP).
Repositório: https://github.com/Haenndel-Santos/duplo-campo (público,
branch master). DUAS cópias de trabalho: máquina 1 =
C:\Haenndel Projects\Duplo Campo (tem .venv pronto); máquina 2 =
C:\Haenndel Projects 2\Duplo Campo. REGRA OBRIGATÓRIA: `git pull`
AGORA, antes de qualquer coisa; `git push` ao fechar; nunca
force-push. Cálculos oficiais SEMPRE pelo .venv (requirements fixado:
sympy 1.14.0, numpy 2.5.1, scipy 1.16.3).

ANTES DE QUALQUER COISA, leia nesta ordem:
1. auditoria/erratum_02_reducao_numerica.md — O EVENTO CENTRAL DE
   2026-08-12: o reduz_ponto numérico (usado de D-2 a R-5) dobrava Ċ
   nas entradas off-diagonais de W_XX. O "3º DOF escalar" e o
   fantasma do Gate F eram ARTEFATO. A lib simbólica sempre esteve
   correta. Origem: reauditoria externa (ChatGPT do autor; pacote em
   auditoria/external/r6_reaudit_chatgpt/) + verificação local
   r6→r6b→r6c→r6d (r6c provou que as duas L2 são a MESMA ação;
   r6d localizou e corrigiu o bug).
2. docs/resultado_r7_cascata.md — A REEXECUÇÃO COMPLETA (R-7a/b/c) e
   o ENUNCIADO OBSERVACIONAL v4. Resumo: sistema físico tem 2 DOFs
   escalares (1 métrico overdamped que DECAI + espectador δχ
   saudável); zero direções cinéticas negativas; BANDA-MORTA
   (estática: lnA −8.4 vs +4 antigo; pousado: −11.0…−14.7 em 8/8
   épocas vs −0.2…+4.8 antigo); Φ_g DECAI (o elo do R-5 caiu);
   previsão de excesso ISW RETIRADA; tensão observacional DISSOLVIDA
   (a previsão era artefato). Consistente com Hassan–Rosen /
   Comelli–Crisostomi–Pilo.
3. docs/veredito_setor_escalar_final.md + resultado_r2_fantasma.md +
   resultado_gatef_b.md etc. — REGISTRO HISTÓRICO. Tudo que dependia
   da dinâmica reduzida numérica (D-2, R-1, R-2, R-3*, R-4*, F-a/F-b,
   R-5) está SUBSTITUÍDO ou CAÍDO pela tabela do §4 do
   resultado_r7_cascata.md. NÃO citar números antigos sem esse filtro.
4. Se precisar do fundo: erratum_01_bianchi.md (Bianchi — fica de
   pé), resultado_ramo_finito.md (fundo/tensor — ficam de pé),
   decisao1_congelamento_v1.md (v1 congelada; v2 em manuscript-v2/).

ESTADO ATUAL (2026-08-12, fim de sessão):
- ERRATUM-02 emitido; cascata R-7 executada e commitada (r7a, r7b,
  r7c + doc). Gate F/R-2 caíram; R-4/R-5 substituídos (banda morta,
  ISW retirado); D-2/R-1 substituídos na classe β-constante.
- FICAM DE PÉ: background (rolagem/pouso — com nota: taxas Euler do
  fundo eram internamente inconsistentes ~1e-3, detectadas pelo
  V-XREP no R-7c e tratadas via splines), setor tensorial
  (m_T²/H²→12), Bianchi/erratum-01, Gate 1 (R1 como enquadramento),
  Stückelberg como MEDIDA, lib simbólica (tdcp_pert_lib).
- ATENÇÃO: o "no-go do setor escalar" da F1 está EFETIVAMENTE
  REVOGADO no benchmark β-constante — não há fantasma nem taquião
  letal no sistema 2-DOF corrigido; o setor é são e DECAI. Os no-gos
  antigos eram do sistema espúrio de 3 DOFs. O que segue em aberto é
  a VIABILIDADE OBSERVACIONAL (nenhum C_ℓ calculado ainda).
- MAQUINARIA NOVA OBRIGATÓRIA (qualquer redução numérica futura):
  (i) correção one-shot da absorção (S simétrica, Ċ uma vez por par);
  (ii) equilibração B̃=kB, Ẽ=k²E; (iii) V-XREP: dois canais de Ċ
  (grade vs dt_background simbólico), gates G1/G2/G3 pré-declarados —
  ver r7a_dinamica_2dof.py como referência de implementação.

ADENDO (mesma data, sessão continuada — R-7e/f EXECUTADOS,
commit 255a327): SAÚDE INTERNA FECHADA
(docs/resultado_r7e_saude_interna.md): Fase B SÃ (janela de
deslocamento estruturalmente limpa — W00 sem trocas, sem FJ-quebra,
negK=0; o σ/H≈13 antigo era artefato triplo: QEP congelado + 3-DOF
espúrio + normalização variável — a autópsia com normalização
CONGELADA deu G_win ≤ +0.4, campo métrico DECAINDO −3.6..−10.7 pela
janela; o transiente δχ ≤ e^{0.4} é a condensação da Fase A,
autocurável). NO-GO DE CLASSE RETIRADO (R-7f: scan μ×β₁ + fresta,
zero violações). LIÇÃO DE MÉTODO: envelope com ω²(t) variável é
armadilha de normalização — sempre normalização congelada para
ganhos; o gate SUSPEITO pré-declarado funcionou.

ADENDO 2 (mesma noite — R-8a EXECUTADO, commit 18c616b,
docs/resultado_r8a_quase_estatico.md): μ/Σ/η quase-estáticos como
razões bimétrico/GR. ALVO-SUBPERCENTUAL no sub-horizonte (|μ−1|,
|Σ−1| ≤ 0.66% em kh≥22, ≤0.06% em kh≥100, duas eras, dois fundos);
a janela quase-horizonte kh≲22 fica INDECIDIDA pela sonda QS (números
crus até 17% lá são QS-contaminados — nada se afirma) e é O ALVO do
R-8 completo. ALAVANCA IDENTIFICADA: desvio ~ (m/aH)²/kh² — se o
dicionário adotar o postulado do corpus m ~ 30–300 H₀, a escala de
Compton entra na janela observável e os dados de crescimento viram
LIMITE DIRETO sobre m/H₀ (confronto com o postulado).

ADENDO 3 (mesma noite — R-8b + review externo + escrita da v2,
commits ate 09e04db+):
- R-8b EXECUTADO (resultado_r8b_limite_mH0.md): a familia beta->s*beta
  com H tardio fixo DOBRA em s~5.7 (r^2 V_f tem minimo positivo 0.3) —
  postulado 30-300 H0 INALCANCAVEL por dial continuo (exige outra
  forma-beta + ajuste fino U0<0); m_T/H0 in [2.26, 2.41] em TODA a
  familia: a massa do graviton e PREDICAO (~2.3 H0 hoje); crescimento
  trivialmente satisfeito; o decisivo e o quase-horizonte.
- REVIEW EXTERNO (5 pontos) TODO CORRIGIDO: v2 skeleton reescrito;
  Phi_g 31/32 esclarecido; halving fino kh=10 EXECUTADO (dG=0.191<0.3,
  A4 pleno); V-XREP renomeado a/b; a_eq do R-8a corrigido
  (0.686/0.429) + fraseado de precisao ("nenhum desvio acima do piso
  QS ~2%"; 0.66% e valor central).
- V2: ESPINHA + REFRAMES ESCRITOS, Gate 0 PASSA (6 arquivos):
  01_tese, 02_metodo (erratum-02 como caso maximo, 4 licoes, placar),
  07_setor_escalar (3 atos + tabela de supersessao),
  08_identificacao_normativa (G1 relido: G1-a intocado, G1-b sem
  objeto, G1-c de pe; problema aberto reformulado),
  09_programa_observacional (R-8a/b + o que nao ha mais + R-8
  completo com criterios a pre-declarar).


ADENDO 4 (2026-08-13 — PARECERES + BLOCO 0 + BLOCO 1; commits ate
1ca171f). ESTADO MUDOU QUALITATIVAMENTE:

1. CINCO PARECERES ESPECIALIZADOS (docs/pareceres_especialistas/,
   com 00_sintese_cruzada.md): convergencia unanime de que a F1 era
   "sa, blindada e quase-invisivel"; e o achado metodologico de que
   os gates do R-7 eram CEGOS A GRADIENTE por construcao.

2. BLOCO 0 (R-9): o "omega^2 < 0" do R-7e era RAZAO ERRADA (falta o
   Cdot: om2_ef = (Cdot+W)/K). p_phi cruza zero mas a matriz de
   Dirac NAO degenera. O item (b) era tautologico -> Bloco 2.
   QUATRO comparadores descartados no caminho — licao: quando um
   gate reprova, a primeira suspeita e o comparador.

3. BLOCO 1 (R-10/R-11) — NO-GO DE CLASSE POR GRADIENTE:
   c_s^2 -> -1 em r -> 0 (alto z), com K2 > 0 (gradiente genuino,
   nao fantasma), calibrador exato. A era instavel COBRE A
   RECOMBINACAO (z_cross ~ 0.62 no beta-const). As QUATRO saidas
   foram testadas e FECHADAS: ramo infinito (nao conecta),
   modulacao (tarde demais), screening (delta_screen ~ 20-60; o
   lambda cancela), forma-beta (108/108 celulas dao
   c_s^2 = -1.010 +- 6e-6 — CONSTANTE ESTRUTURAL DA CLASSE).

O QUE ISSO SIGNIFICA: cai a SUFICIENCIA da implementacao F1 como
cosmologia. NAO cai a TDCP como hipotese, nem os erratums, nem o
fundo, nem o tensor (m_T^2/H^2 -> 12; m_T ~ 2.3 H0), nem o
espectador, nem o metodo. A unica porta entreaberta e beta_3 != 0 —
que sai da definicao de F1 (seria uma F2) e exige refazer a cubica
do fundo.


ADENDO 5 (2026-08-13, mesma data — R-12 EXECUTADO; commits ate
1698979). DUAS COISAS, e a segunda e um erratum de instrumento:

1. TEOREMA: c_s^2 EM FORMA FECHADA (docs/resultado_r12b_teorema_cs2.md).
   O item 1 da fila esta FEITO. Na celula minima da classe F1
   (beta_2 = beta_4 = 0), a reducao 2-DOF fecha simbolicamente:

       c_s^2(r) = -(3r+1)(9r^5 - 6r^3 + 3r^2 - 10r + 2) / (2(3r^2+1)^2)

       r -> 0    : c_s^2 = -1  EXATO   (serie: -1 + 2r + 39r^2/2 + ...)
       r = r_inf : c_s^2 = +1  EXATO   (r_inf = (sqrt13 - 1)/6)
       m_ef^2/H^2 -> 5/2 em r -> 0

   O PASSO QUE FAZ FECHAR: eliminar beta_1 pela Friedmann do setor f
   (beta_1 = 3(1+mu)H^2 r - beta_4 r^3 - 3 beta_2 r), o que torna
   (a, r, k, H) coordenadas livres e mantem tudo racional. Gate que
   legitima: dN(beta_1) = 0 identicamente. Tratar H como livre com o
   vinculo guardado para o fim NAO funciona (K3[0,:] = 0 deixa de valer
   identicamente) — os dois modos de falha estao no git.
   ALCANCE: nivel 1 para a celula minima; nivel 2b para a classe
   (R-12g: 108/108 celulas, |c_s^2+1| <= 1.1e-7).

2. ERRATUM-03 — INSTRUMENTO (docs/resultado_r12_instrumento_e_cs2.md).
   Cdot3 e Cdot2 eram calculados por np.gradient (2a ORDEM) de R-7 a
   R-12c. O erro O(h^2) e amplificado pelo condicionamento da reducao
   (cond ~ 1e11 em a = 0.01). DEMONSTRADO, nao conjecturado: trocando
   SO a ordem do estencil, a 2a ordem reproduz a tabela do R-10a digito
   a digito (-1.01033852661 vs -1.010339; -1.2608602308 vs -1.260860;
   -0.585509139414 vs -0.585509) e MOVE com h; a 8a ordem e estavel em
   14 digitos.
   VALORES LIMPOS: c_s^2(kh=30) = -0.99717 em vez de -1.010;
   om2/H^2 = -kh^2 + 5/2 (nao ha termo k^4 — o "k^4 do R-9a" era o
   mesmo artefato: 1.9287 em kh=1000 vira 1.0000079); era tardia
   c_s^2 = +1 exato; a_cross = 0.578 e z_cross = 0.61 (antes 0.574 e
   0.62 — o R-10b sobrevive praticamente intacto).
   ENUNCIADOS NAO MUDAM. O no-go de classe por gradiente esta de pe e
   mais forte. O que muda sao os VALORES nas tabelas de R-9a, R-10a,
   R-10b e R-11 (banners de supersessao ja postos).

   RETRATACAO INTERNA: o R-12a e o R-12c (desta mesma sessao)
   concluiram que c_s^2 saturava em -0.687 e que o "-1" era artefato de
   extrapolacao. ERRADO — herdaram o canal sujo. Ficam no git como
   registro; nao citar como resultado.

   DUAS REGRAS NOVAS PARA O CAP. 02:
   (i) derivadas ao longo do fundo em FORMA FECHADA; onde nao der,
       estencil de ordem >= 8 COM teste de refino obrigatorio.
       np.gradient proibido em cadeia que passe por reducao mal
       condicionada.
   (ii) DECLARACAO DE CEGUEIRA DE GATE (com caso concreto): o
       calibrador do espectador dchi deu 1.00000 em todos os pontos
       enquanto o modo metrico errava na primeira casa — porque dchi
       nao tem termo giroscopico e o calibrador e CEGO ao canal Cdot.
       Todo gate declara o que nao consegue ver.

FILA (pos-R-12):
1. Generalizar a formula de c_s^2 em (beta_0, beta_2, beta_4, mu) —
   provavelmente por Laurent em r, ja que a forma fechada exata so
   fecha na celula minima.
2. Confrontar a formula fechada com Konnig et al. (arXiv:1407.4331) —
   agora ha formula, nao so numero. [verificar contra a fonte]
3. REFAZER O R-8a (mu/Sigma quase-estaticos) com o instrumento limpo:
   os numeros la sao sub-percentuais e o defeito e da mesma ordem.
4. Cap. 09: o enunciado honesto de validade restrita (opcao 3 do
   R-10 consolidado) continua valendo.
5. Pendencias herdadas (inalteradas): Gate 2B + difeo espacial,
   Vainshtein/PPN, paredes de dominio, radiacao, varredura de mu, a 2a
   solucao tardia do fundo.

LEITURA OBRIGATORIA (substitui a lista do adendo 4):
docs/resultado_r12b_teorema_cs2.md e
docs/resultado_r12_instrumento_e_cs2.md; depois
docs/resultado_r11_nogo_gradiente.md e resultado_r10_consolidado.md
(ambos com banner de supersessao de VALOR); depois
docs/pareceres_especialistas/00_sintese_cruzada.md; so entao o
historico (erratum_02, resultado_r7_cascata §4).

FILA (adendo 4) — SUPERSEDED pelo adendo 5:
FILA (nova):
1. PROVAR c_s^2 = -1 analiticamente no limite r -> 0. Alvo limpo,
   resultado de CLASSE, nivel 1, o mais publicavel do programa.
2. Reescrever cap. 07 (ja atualizado com o arco) e sobretudo o
   cap. 09: nao ha programa observacional linear enquanto a era
   instavel cobrir a recombinacao. Enunciado honesto = validade
   restrita (opcao 3 do resultado_r10_consolidado.md).
3. Pendencias herdadas: Gate 2B + difeo espacial (Bloco 2, mesmo
   calculo de campo); Vainshtein/PPN astrofisico; paredes de
   dominio (mu_-); radiacao; varredura de mu; a 2a solucao tardia
   do fundo (r ~ 2.23) nunca explorada.

LEITURA OBRIGATORIA ANTES DE QUALQUER COISA (substitui a lista
anterior como ponto de partida): docs/resultado_r11_nogo_gradiente.md
e docs/resultado_r10_consolidado.md; depois
docs/pareceres_especialistas/00_sintese_cruzada.md; so entao o
historico (erratum_02, resultado_r7_cascata §4 = tabela de
supersessao).

FILA (ordem recomendada — SUPERSEDED pelo adendo 4):
1. **v2 — capitulos restantes**: 03 (acao+dicionario; fonte
   docs/acao_v2.md), 04 (Bianchi/erratum-01), 05 (fundo), 06
   (tensor) — ports de docs estaveis; 10 (interpretacao) POR ULTIMO.
   Gate 0 a cada sessao. Convencoes vinculantes: phi- modulador
   (chi so como distancia comovel; token `dchi` apenas em backticks),
   V_g/V_f caligraficas, Psi TEMPORAL na v2 (lib usa Phi_g temporal —
   anotar o mapa), Sigma=(mu/2)(1+eta_slip).
2. **R-8 completo** (o gate de fisica restante): materia/radiacao no
   2-DOF, C_ell baixo-ell/P(k)/lensing na janela kh<~22; insumos do
   autor: forma-beta (manter benchmark => m_T~2.3H0 e predicao
   testavel), massa de phi- hoje, normalizacao primordial; criterios
   pre-declarados antes da 1a rodada.
2. Propagação editorial do erratum-02: banners de supersessão nos
   docs históricos afetados (ou nota única no índice); revisão do
   cap. 07 da v2 (o resultado central mudou: de "fantasma/H-SC" para
   "setor escalar são em todos os regimes; questão aberta = C_ℓ").
3. Housekeeping (não bloqueia): fundo pousado com integrador 2ª ordem
   completo (Heun atual tem cadeia rp de 1ª ordem, M0=3e-4; os lnA do
   pousado carregam ±O(1) de sistemática — BANDA-MORTA intacta);
   halving fino do modo kh=10 da autópsia; ramo algébrico (deferido,
   declarado — porte do arranjo da investigacao1).

DISCIPLINA (inalterada): critérios pré-declarados em cabeçalho antes
de rodar; veredito só pelos critérios; rodadas ruins preservadas nos
outs; commits granulares por etapa executada; V-XREP obrigatório.
