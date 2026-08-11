# Prompt de continuação — próxima sessão

Copiar o bloco abaixo como primeira mensagem da próxima janela.
(Atualizado 2026-08-10, pós-sincronização das duas máquinas, Gate 1 da
2ª geração e resolução da infraestrutura.)

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
1. docs/veredito_setor_escalar_final.md — o fechamento do arco v2:
   cadeia de evidência, no-go do setor escalar com fronteira, 5 saídas.
2. auditoria/erratum_01_bianchi.md — a constraint de Bianchi do corpus
   estava ERRADA; correta: B(r)·(N_f·ȧ − N_g·ḃ)=0 (duas rotas).
   Supersede D5 (premissa errada) e inverte o Higuchi da D8.
3. docs/gate1_identidade_relacional.md — NOVO: hipóteses R1/R2 e o
   Gate 1 da 2ª geração (a cadeia Φ₋ → φ/χ → r → σ tem QUATRO objetos
   identificados só por decreto; a doença mora nos vínculos, não em
   δφ₋ — protocolo G1-a/b/c com critérios pré-declarados).
4. docs/resultado_ramo_finito.md + docs/resultado_setor_escalar.md +
   docs/no_go_beta_constante.md + docs/estrutura_par_relativo.md — a
   trilha do arco, em ordem.
5. docs/plano_v2_reconstrucao.md + auditoria/parecer_tecnico.md
   (Parte III-B = estratificação epistêmica, REGRA DE MÉTODO) +
   docs/project-master.md (seção de sincronização).

ESTADO ATUAL (2026-08-10, master sincronizado, working tree limpo):
- Auditoria 856/856 completa (lotes 1–11) + parecer técnico.
- ERRATUM 01 confirmado. RAMO FINITO: fundo ✓ (ṙ=H_g(ξ−r), limite GR
  exato, Ω_m~0.25) e tensor ✓ (Higuchi automático; m_T²/H²→12
  universal no primordial).
- SETOR ESCALAR: NO-GO CONSOLIDADO (taquião σ≈(3–4)H p/ μ≥0.3 em
  ~1500 pontos 4D; fantasma |kN|~μ³ em μ=0.1; doença no SETOR DE
  VÍNCULOS — dubleto de shifts B_g±B_f / lapso Φ_f; modulação β₁(φ₋)
  não cura e piora nos dois canais).
- GATE 1 (2ª geração) formalizado: R1 = o no-go é sobre a REPRESENTAÇÃO
  F1, não sobre o grau relacional primordial (suporte 2b: composição
  dos autovetores patológicos ≠ δφ₋); R2 = natureza coletiva/parâmetro
  de ordem. Trilema da seta Φ₋→(g,f) declarado (prior Weinberg-Witten,
  nível 3).
- INFRA resolvida: .gitignore versiona derivations/code/out/ e
  auditoria/code/out/; .venv na máquina 1; repo TDCP vazio ARQUIVADO.
  PENDÊNCIA MÁQUINA 2: commitar auditoria/code/out/ (git status vai
  listá-las após o pull) — fazer no início da próxima sessão de lá.

TAREFA IMEDIATA — Investigação 1: RAMO ALGÉBRICO PÓS-ERRATUM (barata;
nunca refeita com a constraint correta), COM O G1-b EMBUTIDO:
(a) o que "estar no ramo algébrico" significa agora que a constraint
    não fatora quando φ₋ evolui (resíduo −M_eff²m²p_φβ₁′ do Gate 2)?
(b) a degenerescência cinética NA raiz exata (kN~1e-16, benchmark C da
    D1) persiste no formalismo corrigido? há corredor saudável
    perto-da-raiz?
(c) G1-b (carona nas MESMAS rodadas): projetar os autovetores de TODOS
    os modos em δφ₋ e nas direções métricas-relativas, μ∈{0.1,0.3,1,3,10},
    ponto fixo, k=1 E k=10. R1 passa se |⟨v_patológico,δφ₋⟩|²<0.05 em
    toda a varredura; falha se algum modo patológico for δφ₋-dominado.
Reusar: derivations/code/tdcp_pert_lib.py + fundos generalizados +
modulacao_qep.py (fatias {Fb,Fp,Fpp}×{β₀..β₄}; qep_modes retorna
autovetores na chave 'v'). Fluxo: escrever o script → usuário roda no
.venv → devolve saídas (auditoria/code/out/*.txt, agora versionadas).

DEPOIS, EM ORDEM: G1-a (tabela de identidade no dicionário; documental)
→ G1-c (nota do trilema) → Investigação 2 (condensação dinâmica,
p_φ≠0 — teste direto de R2, caro). Se Investigação 1 reprovar E G1-b
passar: R1 vira o enquadramento oficial do no-go.

DECISÕES EM ABERTO DO USUÁRIO (não decidir sozinho; lembrar quando
os resultados amadurecerem):
1. Destino do manuscrito v1: corrigir no lugar (115 erros mapeados) vs
   congelar + escrever v2 enxuta vs híbrido. Aguarda Investigação 1.
2. Formato de publicação do no-go (nota técnica / paper / abertura da v2).
3. Atualização do artifact do parecer (🔭) com o arco erratum+no-go.

REGRAS DE MÉTODO (aprendidas a ferro; seguir sempre):
- Estratificação epistêmica (Nível 1/2a/2b/3). NUNCA "CONFERE" para o
  declarado-mas-não-derivado; "bate com a literatura" é Nível 3 (dois
  priors de literatura já caíram por cálculo).
- Todo teste novo com auto-teste de PODER DE DETECÇÃO, ancorado na
  MESMA rota e MESMO fundo.
- Saúde espectral = σ E kN (taquião E fantasma), em k=1 E k=10 no
  mínimo. k é COMÓVEL (k_phys=k/a; benchmark da D1 rescala a→1).
- Seleção de raiz: menor raiz real positiva + filtros físicos que
  ABORTAM (ξ>0, H²>0); corte de positividade RELATIVO.
- Ponto fixo = juiz sem caveat de congelamento.

REGRAS DE EXECUÇÃO:
- Cálculos pesados: usuário roda no VS Code (.venv) e devolve saídas;
  py_compile e sondagens curtas na sessão são OK.
- Não editar manuscript/ nesta fase; NUNCA regenerar .docx/PDF.
- Mudou versão de dependência → re-rodar derivations/code/ contra as
  saídas oficiais antes de commitar.

PENDÊNCIAS MENORES (fora da linha principal): flag do Erratum 01 na
tabela de âncoras do registro_formulas.md (D5/D8 — 1 linha);
lote05_C22_galileon_stability.py nunca rodado; Gate 2 Parte B (ADM
completo) só se a modulação voltar; Higuchi generalizado μ≠1
provisório; passe de correção do manuscrito aguarda decisão 1.

Comece por: git pull → escrever o script da Investigação 1 (com G1-b)
→ me passar para rodar.
