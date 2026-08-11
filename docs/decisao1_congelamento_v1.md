# Decisão 1 — Destino do Manuscrito v1: CONGELAR + v2 ENXUTA

**Data:** 2026-08-11. **Decisão do autor**, tomada após o fechamento da
Investigação 1 e do Gate 1 (condição que a decisão aguardava desde o
veredito consolidado).

---

## 1. A decisão

Das três opções em aberto — corrigir a v1 no lugar (115 erros
mapeados) / congelar + escrever v2 enxuta / híbrido — fica decidido:

> **Congelar a v1 como registro histórico e escrever uma v2 enxuta a
> partir do parecer + veredito + ramo finito** (a direção implícita do
> `plano_v2_reconstrucao.md`).

## 2. O que "congelar" significa operacionalmente

1. **`manuscript/` vira registro histórico imutável.** Nenhum dos 115
   erros mapeados é corrigido no lugar; a auditoria
   (`auditoria/parecer_tecnico.md` + lotes + Erratum 01) É o registro
   das correções. Quem ler a v1 lê junto o parecer.
2. **Os `.docx` originais permanecem intocados** (regra que já valia).
3. **Supersede da etapa final do passe editorial de 2026-08-05:** o
   `project-master.md` previa regenerar os `.docx` a partir de
   `manuscript/` ao fim daquele passe. Com a v1 congelada como registro
   histórico em Markdown, essa regeneração fica **cancelada** — o
   corpus Markdown auditado é a forma de referência da v1. (Consistente
   com a regra vigente de nunca regenerar .docx/PDF sem pedido direto.)
4. **A flag menor pendente** (Erratum 01 na tabela de âncoras do
   `registro_formulas.md`) continua válida — é documentação da
   auditoria, não edição do manuscrito.

## 3. O que a "v2 enxuta" é — e não é

**É:** o documento honesto do que foi *estabelecido*, escrito na ordem
do plano (ação → derivação → resultado → interpretação por último),
citando em cada afirmação o script e a saída versionada que a sustenta.
Fontes primárias: `auditoria/parecer_tecnico.md`, Erratum 01,
`docs/veredito_setor_escalar_final.md`, `docs/resultado_ramo_finito.md`
e todo o arco de docs de resultado, `docs/acao_v2.md`,
`docs/gate2_ghost.md`, Gate 1 completo (a/b/c).

**Não é:** a reconstrução dos 26 capítulos; não é um texto de defesa da
TDCP; não espera a Investigação 2 (o programa aberto é um capítulo
dela, não um pré-requisito).

**Casa:** `manuscript-v2/` — o diretório que o Gate 0 já espera
(`dicionario_simbolos.md`: "Quando manuscript-v2/ for criado, o script
roda contra ele e o resultado esperado é zero violações"). O dicionário
é normativo; `verifica_simbolos.py --alvo v2` passa a rodar contra a
v2 a cada sessão de escrita.

**Estrutura proposta:** `manuscript-v2/00_estrutura.md` (esqueleto
comentado, criado junto com esta decisão).

## 4. Relação com as decisões ainda abertas

- **Decisão 2 (formato de publicação do no-go):** permanece aberta. A
  v2 enxuta não a decide, mas cria o vehículo natural — o capítulo do
  no-go pode ser extraído como nota técnica/paper se o autor decidir.
- **Decisão 3 (artifact do parecer 🔭):** permanece aberta.

## 5. Efeito na fila de trabalho

A fila passa a ter duas trilhas paralelas e independentes:

| Trilha | Passos | Natureza |
|---|---|---|
| **Escrita** | v2 enxuta, capítulo a capítulo, Gate 0 rodando | documental; sessões de escrita |
| **Cálculo** | (opcional) derivação de Stückelberg (sobe G1-c a 2a) → Investigação 2 (p_φ≠0, teste de R2) | computacional; a Investigação 2 é o passo caro |

Nenhuma bloqueia a outra; resultados da trilha de cálculo entram na v2
no capítulo do programa aberto conforme amadurecem.
