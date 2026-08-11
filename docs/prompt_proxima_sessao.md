# Prompt de continuação — próxima sessão

Copiar o bloco abaixo como primeira mensagem da próxima janela.
(Atualizado 2026-08-07, pós-veredito consolidado do setor escalar.)

---

Continuação do trabalho na Teoria do Duplo Campo Primordial (TDCP), em
C:\Haenndel Projects 2\Duplo Campo (repositório git local; commits
pequenos e descritivos em português por lote de trabalho; ambiente
.venv com requirements.txt fixado: sympy 1.14.0, numpy 2.5.1,
scipy 1.16.3).

ANTES DE QUALQUER COISA, leia nesta ordem:
1. docs/veredito_setor_escalar_final.md — O FECHAMENTO DO ARCO: cadeia
   completa de evidência (6 resultados com níveis), diagnóstico do
   mecanismo, enunciado do no-go com fronteira, e as 5 saídas
   restantes por custo.
2. auditoria/erratum_01_bianchi.md — o pivô: a constraint de Bianchi
   do corpus está ERRADA; a correta é B(r)(N_f·ȧ − N_g·ḃ)=0 (duas
   rotas independentes).
3. docs/resultado_ramo_finito.md, docs/resultado_setor_escalar.md,
   docs/no_go_beta_constante.md, docs/estrutura_par_relativo.md —
   a trilha do arco, em ordem.
4. docs/plano_v2_reconstrucao.md + docs/acao_v2.md + docs/gate2_ghost.md
   — o plano com gates; e auditoria/parecer_tecnico.md (Parte III-B =
   estratificação epistêmica, que é REGRA DE MÉTODO).

ESTADO ATUAL (2026-08-07, arco fechado, working tree limpo):
- Auditoria das 856 equações completa (lotes 1–11) + parecer técnico
  (artifact 🔭). ERRATUM 01 emitido e confirmado.
- RAMO FINITO CORRIGIDO: fundo funciona (ṙ≠0 via cúbica, limite GR
  exato, Ω_m~0.25) e o setor tensorial também (Higuchi 400/400;
  m_T²/H²→12 no primordial, independente de TODOS os parâmetros,
  inclusive μ).
- SETOR ESCALAR — NO-GO CONSOLIDADO (veredito final): o par relativo
  é patológico em toda a varredura:
  * taquião eterno (σ≈(3–4)H no ponto fixo) para β constantes com
    μ≥0.3 (~1500 pontos em 4D);
  * fantasma de norma |kN|~μ³ em μ=0.1 (hierarquia invertida);
  * a doença mora no SETOR DE VÍNCULOS: dubleto de shifts B_g±B_f em
    μ~1, lapso Φ_f em μ→0 (composição de autovetores);
  * a modulação β₁(φ₋) NÃO cura e piora: canal Fb anda dentro de um
    espaço-β integralmente doente; canal Fp/Fpp repele níveis na
    direção errada — confirmado nos DOIS regimes (μ=1 e μ=0.1).
- Maquinaria disponível e validada: fatias {Fb,Fp,Fpp}×{β₀..β₄} das
  matrizes de perturbação (modulacao_qep.py — permite modular QUALQUER
  coeficiente sem tocar a biblioteca), QEP com autovetores, fundos
  generalizados (β, μ livres), forma fechada do bloco de massa k=0.
- Gates do plano v2: Gate 0 ✓, Gate 1 ✓ (25/25), Gate 2 Parte A ✓;
  Parte B (ADM completo) aberta; constraint NÃO fatora com β₁(φ₋)
  (resíduo −M_eff²m²p_φβ₁′ — o canal de acoplamento).

TAREFA IMEDIATA — as duas investigações restantes, por ordem de custo:

1. RAMO ALGÉBRICO PÓS-ERRATUM (recomendada; barata; nunca refeita com
   a constraint correta). Perguntas: (a) o que "estar no ramo
   algébrico" significa agora que a constraint não fatora quando φ₋
   evolui? (b) a degenerescência cinética que a D1 achou NA raiz exata
   (kN~1e-16, benchmark C) persiste no formalismo corrigido? (c) há
   corredor perto-da-raiz saudável? Reusar: tdcp_pert_lib + os fundos
   generalizados + a checagem de fantasma (lição: saúde = σ E kN,
   sempre, em k=1 E k=10).
2. CONDENSAÇÃO DINÂMICA (cara; o único regime genuinamente novo). Toda
   sondagem até aqui foi em fundo estacionário (p_φ=0), onde o termo
   novo da constraint secundária se anula. Com p_φ≠0 a estrutura de
   vínculos é genuinamente diferente (não-fatoração do Gate 2). Exige
   fundo com φ₋(t) rolando + perturbações sobre ele — provavelmente
   com as taxas de fundo verdadeiras e cuidado com o congelamento.

Se ambas fecharem negativas: o no-go vira o resultado central e
definitivo do programa; o passe seguinte é editorial (documentar,
atualizar o parecer/artifact, decidir o destino do manuscrito v1).

REGRAS DE MÉTODO (aprendidas a ferro; seguir sempre):
- Estratificação epistêmica (Nível 1/2a/2b/3). NUNCA CONFERE para o
  declarado-mas-não-derivado; "bate com a literatura" é Nível 3 (dois
  priors de literatura já foram refutados por cálculo nesta sessão).
- Todo teste novo com auto-teste de PODER DE DETECÇÃO; ancorar na
  MESMA rota e MESMO fundo da âncora (5 testes vácuos/errados
  catalogados na sessão; os que morreram alto morreram bem).
- Saúde espectral = σ E kN (taquião E fantasma), em k=1 E k=10 no
  mínimo — o 0/36 da região "saudável" caiu na checagem de kN.
- Seleção de raiz: menor raiz real positiva + filtros físicos que
  ABORTAM (ξ>0, H²>0); corte de positividade RELATIVO (r~κβ₁/ρ̃
  encolhe com μ e a⁻³).
- Ponto fixo = juiz sem caveat; k é COMÓVEL (k_phys=k/a; o benchmark
  da D1 rescalava a→1 — rótulos diferem entre scripts).
- Fatias por bilinearidade para modular coeficientes; d1.qep_modes JÁ
  retorna autovetores (chave 'v').

REGRAS DE EXECUÇÃO:
- DUAS cópias de trabalho (máquina 1: 'Haenndel Projects'; máquina 2:
  'Haenndel Projects 2'), mesmo master no GitHub: git pull ao ABRIR a
  sessão, git push ao FECHAR. Máquina 2: commitar auditoria/code/out/
  (o .gitignore já tem a exceção; git status vai listá-las).
- Cálculos pesados: usuário roda no VS Code (.venv) e devolve saídas;
  scripts salvam em auditoria/code/out/*.txt (a sessão pode ler
  direto). py_compile e sondagens numpy curtas na sessão são OK.
- Não editar manuscript/ nesta fase; NUNCA regenerar .docx/PDF.
- requirements fixado; mudou versão → re-rodar derivations/code/
  contra as saídas oficiais antes de commitar.

PENDÊNCIAS FORA DA LINHA PRINCIPAL:
- lote05_C22_galileon_stability.py nunca rodado (Z_t/Z_r/Z_Ω, Cap.22).
- Gate 2 Parte B (ADM completo) — só se a modulação voltar ao jogo.
- Passe de correção do manuscrito v1 (aguarda decisão editorial
  pós-veredito).
- Artifact do parecer (🔭): atualizar com o arco do erratum + no-go.
- Higuchi generalizado para μ≠1 nunca derivado (o critério usado é o
  de μ=1, marcado provisório).

Comece pela investigação 1 (ramo algébrico pós-erratum), escrevendo o
script e me passando para rodar.
