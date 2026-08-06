# Registro de Fórmulas — Índice-Mestre da Auditoria

**O que é:** catálogo de todas as equações em destaque do corpus
(capítulos + anexos), com ID estável, contexto, classe e campos de
dependência/veredito. É a base do passe de auditoria sequencial:
cada fórmula será verificada **apenas contra o que vem antes dela**
na ordem de leitura.

**Gerado por:** `auditoria/code/extrai_formulas.py` (não re-rodar sem
`--force`; o script protege edições manuais). As classes vêm de
heurística textual e são **sugestões a confirmar**.

## Esquema de IDs

- `[Cnn.mm]` — mm-ésima equação do Capítulo nn (ex.: `[C05.03]`)
- `[C06E.mm]` — Cap.6.2 (versão expandida do Cap.6)
- `[Ax.mm]` — Anexo x (ex.: `[AB.07]` = 7ª equação do Anexo B)

## Taxonomia de classes

| Classe | Significado |
|---|---|
| `definicao` | introduz símbolo/quantidade; audita-se consistência e não-sobrecarga |
| `postulado` | assumida como princípio; audita-se coerência com o resto |
| `derivada-no-texto` | o texto afirma obtê-la de equações anteriores; audita-se a conta |
| `afirmada-sem-derivacao` | declarada por analogia/"forma típica"; audita-se se é derivável |
| `condicao/vinculo` | desigualdade/critério de estabilidade; audita-se a origem |
| `importada-da-literatura` | resultado padrão externo; audita-se a transcrição |
| `pendente` | heurística não decidiu; classificar na auditoria |

## Taxonomia de vereditos (preencher no passe de auditoria)

`CONFERE` · `CONFERE SOB HIPÓTESE (qual)` · `ERRO DE CÁLCULO (correção)`
· `NÃO-DERIVÁVEL (o que falta)` · `CONFLITA COM [ID]` ·
`ARTEFATO DE CONVERSÃO`

## Âncoras já auditadas (Derivações 1–8)

As fórmulas cobertas pelas derivações do diretório `derivations/`
apontam para lá em vez de refazer: D3 (ρ_int/regra da cadeia),
D4 (Friedmann com 1/(1−η)), D5 (ṙ no ramo dinâmico), D2 (setor
tensorial), D7 (modo σ_k), D1/D6/D8 (em andamento).

## Estatísticas

**Total: 856 equações** em 39 arquivos.

| Prefixo | Fonte | Equações |
|---|---|---|
| C01 | Capítulo 1 | 10 |
| C02 | Capítulo 2 | 12 |
| C03 | Capítulo 3 | 11 |
| C04 | Capítulo 4 | 24 |
| C05 | Capítulo 5 | 29 |
| C06 | Capítulo 6 | 42 |
| C06E | Capítulo 6 (versão expandida — Cap.6.2) | 21 |
| C07 | Capítulo 7 | 21 |
| C08 | Capítulo 8 | 11 |
| C09 | Capítulo 9 | 14 |
| C10 | Capítulo 10 | 13 |
| C11 | Capítulo 11 | 17 |
| C12 | Capítulo 12 | 1 |
| C13 | Capítulo 13 | 11 |
| C14 | Capítulo 14 | 69 |
| C15 | Capítulo 15 | 26 |
| C16 | Capítulo 16 | 28 |
| C17 | Capítulo 17 | 24 |
| C18 | Capítulo 18 | 48 |
| C19 | Capítulo 19 | 19 |
| C20 | Capítulo 20 | 34 |
| C21 | Capítulo 21 | 31 |
| C22 | Capítulo 22 | 30 |
| C23 | Capítulo 23 | 17 |
| C24 | Capítulo 24 | 5 |
| C25 | Capítulo 25 | 3 |
| C26 | Capítulo 26 | 7 |
| AA | Anexo A | 30 |
| AB | Anexo B | 71 |
| AC | Anexo C | 24 |
| AD | Anexo D | 19 |
| AE | Anexo E | 57 |
| AF | Anexo F | 17 |
| AG | Anexo G | 5 |
| AH | Anexo H | 17 |
| AI | Anexo I | 11 |
| AJ | Anexo J | 11 |
| AK | Anexo K | 16 |
| AL | Anexo L | 0 |

**Classes sugeridas (heurística):**

| Classe | Quantidade |
|---|---|
| pendente | 370 |
| condicao/vinculo | 162 |
| derivada-no-texto | 129 |
| afirmada-sem-derivacao | 102 |
| definicao | 51 |
| importada-da-literatura | 29 |
| postulado | 13 |

**Notas de extração:** Cap.12 (1 eq.) e Anexo L (0 eq.) são capítulos
conceituais — contagens conferidas contra a fonte, não são falha do
extrator. Linhas de LaTeX cru sem `$` (artefato da conversão .docx)
entram com flag `sem-delimitador`; equações dentro de citação, com flag
`em-citacao`.

## Progresso da auditoria

| Lote | Status |
|---|---|
| Registro extraído | feito |
| Classificação revisada | pendente |
| Regras de auditoria (regras_de_auditoria.md) | pendente |
| Passes sequenciais C01–C26, AA–AL | pendente |
