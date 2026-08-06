# Regras de Auditoria Matemática do Corpus TDCP

Consolida o método usado nas Derivações 1–8 como protocolo para o passe
sequencial sobre as 856 fórmulas do `registro/`. Complementa (não
substitui) os skills do projeto — em especial
`mathematical-consistency-auditor`, cujo checklist está incorporado no
§4.

## 1. Objetivo

Verificar cada equação em destaque do corpus, em ordem de leitura, e
registrar um veredito rastreável no próprio `registro/<PREFIXO>.md` —
como um professor que confere as contas na sequência em que o texto as
constrói.

## 2. Regra de ouro sequencial

Cada fórmula é auditada **apenas contra o que vem antes dela** na ordem
de leitura (C01 → C26, depois AA → AL). Consequências:

- Uma fórmula que contradiz outra **posterior** não é penalizada aqui;
  a posterior recebe `CONFLITA COM [ID]` apontando para trás.
- Exceção controlada: quando a contradição envolve material posterior
  já **derivado com veredito** (âncoras D1–D8 ou lotes anteriores), o
  conflito é registrado nos DOIS lados, citando a âncora.
- Referências adiantadas (símbolo usado antes de definido) são
  registradas como nota, não como erro, se a definição existir adiante.

## 3. O que verificar, por classe

| Classe | Verificação principal |
|---|---|
| `definicao` | boa formação; símbolo novo (sem sobrecarga com definição anterior); dimensões declaráveis |
| `postulado` | coerência com postulados anteriores; dimensões dos parâmetros novos; unicidade (não redefinido adiante com outra lei) |
| `derivada-no-texto` | refazer a conta a partir das dependências citadas/implícitas; sinais, fatores, regimes |
| `afirmada-sem-derivacao` | é derivável? de quê? (se derivada em D1–D8, apontar a âncora) |
| `condicao/vinculo` | origem da condição (de onde ela segue), regime de validade, e se as quantidades envolvidas são as derivadas ou as postuladas |
| `importada-da-literatura` | transcrição fiel do resultado padrão (forma, fatores, regime) |

## 4. Checklist por fórmula (do skill `mathematical-consistency-auditor`)

1. Todos os símbolos definidos antes (ou nota de referência adiantada)?
2. Dimensões consistentes (inclusive de constantes novas — ex.: Γ)?
3. Sinais e fatores conferidos (na dúvida, refazer por Euler–Lagrange)?
4. Hipóteses/regime declarados (ramo, gauge, limite, aproximação)?
5. Consistente com TODAS as fórmulas anteriores (mesmo símbolo ⇒ mesma
   lei; mesma quantidade ⇒ mesma expressão)?
6. A conclusão anunciada ("logo", "portanto") segue mesmo da equação?
7. Proporcionalidade (~, ∝) não tratada como igualdade adiante?

## 5. Vereditos

`CONFERE` · `CONFERE SOB HIPÓTESE (qual)` · `ERRO DE CÁLCULO (correção)`
· `ERRO DE FORMULAÇÃO (mal-definida)` · `NÃO-DERIVÁVEL (o que falta)` ·
`INCOMPLETA (o que falta declarar)` · `CONFLITA COM [ID/âncora]` ·
`ARTEFATO DE CONVERSÃO`.

Regras de uso:
- O veredito começa com UMA dessas palavras-chave (para estatística);
  qualificações vêm depois, na mesma linha.
- `CONFLITA` pode compor com outro veredito ("CONFERE … ; CONFLITA COM
  …") quando a fórmula é correta em si mas incompatível com outra.
- Erros têm que vir com a **correção proposta** na própria linha.
- Preencher também `Depende de:` (seções ou IDs anteriores + âncoras).

## 6. Quando escrever script

Toda conta que exceda álgebra segura à mão (matrizes, expansões
perturbativas, integrais, limites não triviais) vai para
`auditoria/code/` com prefixo do lote — reusando `derivations/code/tdcp_pert_lib.py`
sempre que possível. Execução pesada é do usuário (VS Code); sondagens
curtas e auto-testes são permitidos em sessão.

## 7. Âncoras

As Derivações D1–D8 são vereditos prontos (tabela no
`registro_formulas.md`). Fórmula coberta por âncora recebe o veredito
com "âncora Dn" — não se refaz a conta.

## 8. Artefatos de conversão

Linhas com flag `sem-delimitador`/`em-citacao` e prosa dentro de `$`
recebem `ARTEFATO DE CONVERSÃO` e entram na lista de higiene do lote
(correção editorial, não matemática).

## 9. Processo por lote

1. Ler os capítulos do lote **na íntegra** (nunca por amostra).
2. Preencher `Depende de`/`Veredito` nos `registro/<PREFIXO>.md`
   (via `auditoria/code/aplica_vereditos_*.py`, que casa por conteúdo
   da fórmula — robusto a renumeração).
3. Escrever o sumário do lote em `auditoria/lotes/lote_NN_<faixa>.md`:
   estatística de vereditos + discussão só do que não é `CONFERE`.
4. Commit por lote; atualizar a tabela de progresso do
   `registro_formulas.md`.
