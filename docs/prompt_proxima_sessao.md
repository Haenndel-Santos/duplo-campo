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

FILA (ordem recomendada):
1. **Decisão do autor — dicionário de épocas**
   (docs/r8_dicionario_epocas_opcoes.md): o item de maior
   alavancagem é m/H₀ (ver adendo 2). Com a decisão:
   R-8b = confronto μ(a,k) vs vínculos de crescimento reais +
   limite sobre m/H₀; R-8 completo (dinâmico) = janela kh≲22 +
   C_ℓ de baixo-ℓ com o sistema 2-DOF validado (R-7a).
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
