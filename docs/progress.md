# Duplo Campo Progress

## 2026-07-02

Project path: `C:\Haenndel Projects\Duplo Campo`

Action performed: initialized the project as a new local Git repository and created an initial operational baseline.

Previous state: no Git repository existed in this workspace. That absence was treated as expected project state, not as a relocation error.

Important files and folders found:

- `Duplo Campo/`: main chapter and appendix `.docx` files.
- `Eng Version/`: English-version material.
- `Duplo Campo/.agents/skills/`: local TDCP skills and instructions for future agent work.
- `Duplo Campo.zip`: archive preserved in the workspace and ignored by default.

Next recommendations:

- Inspect `Duplo Campo.zip` later because it contains some `.docx` entries that do not match files outside the archive by hash.
- Consider adding a root `AGENTS.md` in a future task if persistent workspace-level agent instructions are needed.
- Continue using small, descriptive commits for future project changes.

## 2026-08-05

Executada a Tarefa 1 completa do "PROMPT 1" (higienização, correção
estrutural, renumeração, tradução e avaliação de integração dos 39
capítulos/apêndices). Resumo por tarefa:

### Infraestrutura: `manuscript/` como fonte de trabalho em Markdown

Antes de editar, converti os 39 `.docx` (30 capítulos incluindo
Cap.6.2/12.2/26.2, 8 apêndices A–H, Eng Version/CHAPTER 1) para Markdown
via Pandoc, em `manuscript/{capitulos,apendices,eng-version}/`. Motivo:
diffs de `.docx` binário não são revisáveis; diffs de Markdown são.
Descoberta durante a conversão: 36 dos 39 arquivos nunca usaram objetos
de equação reais do Word — toda fórmula era texto puro em notação LaTeX;
apenas Cap.26/26.2/27 (inglês) e Eng Version/CHAPTER 1 usam OMML real.
Um pós-processamento (`md_cleanup.py`, não versionado — script de
scratchpad) converte esse "LaTeX-como-texto" em Markdown+LaTeX de
verdade (`$...$`/`$$...$$`), preservando 100% do conteúdo. Os `.docx`
originais permanecem intactos em `Duplo Campo/`; serão regenerados a
partir do Markdown finalizado ao final de todo o trabalho de edição.

### Tarefa 1 — Higienização

Removido, de todos os 39 arquivos, resíduo de coautoria conversacional
(saudações, confirmações, perguntas ao leitor, menus de opção A/B/C e
emoji numerado, emojis-marcador). Cada remoção foi decidida após leitura
do parágrafo em contexto — perguntas retóricas legítimas e listas de
status técnico (ex.: "Estado Atual da TDCP" com checkmarks) foram
preservadas como conteúdo, apenas com o emoji-marcador removido. Log
completo em `hygiene_log.md`. Duas rodadas de correção subsequentes
encontraram e removeram alguns resíduos que a varredura original havia
deixado passar (documentado no próprio log).

### Tarefa 2 — Correções estruturais

- **Cap.8** (idêntico ao Cap.7 no original): reconstruído a partir do
  Capítulo 8 real e completo encontrado em `Eng Version/CHAPTER 1.docx`
  — descoberta importante: esse arquivo, apesar do nome, é uma versão em
  inglês condensada dos Capítulos 1–14 inteiros, não apenas do Capítulo 1.
  Traduzido, não inventado. Marcado "RASCUNHO RECONSTRUÍDO — REVISAR".
- **Cap.22/23** (só preservavam o fim do capítulo): aberturas
  reconstruídas com base no que os capítulos anteriores já anunciavam
  (pipeline BAO/RSD/WL; implementação em CLASS), usando somente
  formalismo já derivado.
- **Cap.24/25** (idênticos, só traziam o fim do Cap.23 + seções 25.5–25.8):
  Cap.24 completo e seções 25.1–25.4 reconstruídos (impacto no CMB via
  ISW tardio; estratégia de likelihood conjunta).
- **Convenção "X.2"**: padronizada como revisão-do-mesmo-capítulo apenas.
  Cap.6.2 mantido; Cap.12.2 promovido a capítulo numerado (novo Cap.13),
  com Cap.13–25 deslocados para Cap.14–26. Toda referência cruzada
  interna (~400 ocorrências) atualizada programaticamente e verificada
  arquivo por arquivo. Mapeamento completo em `renumbering_log.md`.

### Tarefa 3 — Tradução

Cap.26/26.2/27 (inglês) traduzidos para português preservando notação e
equações, com numeração provisória 27/28/29.

### Tarefa 4 — Avaliação de integração

`integration_assessment.md`: os três capítulos traduzidos descrevem um
mecanismo cosmogônico (colapso de função de onda, dois domínios
emaranhados, L_int, Λ_ent) que **não** se integra sem ajuste ao
formalismo bimétrico F1 já demonstrado. Achados centrais: (i) o
acoplamento de matéria simétrico aos dois domínios conflita com a
contagem de graus de liberdade livre de fantasma (Cap.3/Cap.6); (ii) o
cálculo explícito de linearização de V(K) mostra que L_int, como escrito,
arrisca reintroduzir o fantasma de Boulware–Deser; (iii) Λ_ent não tem
equação de movimento (ao contrário de η, que tem: η̇=Γχ̇², canônico no
Anexo H). Veredito: **integrável apenas parcialmente**.

### Tarefa 5 — Consolidação

Como o veredito não foi de integração total, os capítulos 27–29
provisórios foram movidos para `manuscript/apendices/Appendix-{I,J,K}.md`
como "Linha de Pesquisa Exploratória", fora da numeração de capítulos, com
um `Appendix-L.md` novo documentando a reinterpretação (não as equações)
que pode ser absorvida ao corpo F1. Corpo principal final: Capítulos 1–26
(mais Cap.6.2), Apêndices A–L.

Próximo passo: regenerar os `.docx` finais (e PDFs) a partir do Markdown
consolidado em `manuscript/`, substituindo os arquivos em `Duplo Campo/`.
