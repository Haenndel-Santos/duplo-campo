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

## Âncoras já auditadas (Derivações 1–8, TODAS concluídas em 2026-08-06)

As fórmulas cobertas pelas derivações do diretório `derivations/`
apontam para lá em vez de refazer. Vereditos-âncora (detalhes e
propostas de correção em `derivations/00_indice.md`):

| Âncora | Fórmulas do registro afetadas | Veredito |
|---|---|---|
| D1 (`01_setor_escalar_K_Omega.md`) | Cap.15 §15.4/§15.5 (no-ghost e m_S²), Cap.6.2 §6.4/§6.6–6.8, Anexo C §C.3/§C.7/§C.10/§C.11 | claims §15.4/§15.5 **ERRO**; contagem 3 confirmada; §C.11 sem suporte |
| D2 (`02_setor_tensorial_mT2.md`) | Cap.16 §16.2/§16.4/§16.6, Anexo D §D.3/§D.5, Cap.17 (cadeias EFT) | Cap.16 **ERRO** (cinético e massa sem ξ); Anexo D §D.3 **CONFERE** |
| D3 (`03_dV_dNg_regra_cadeia.md`) | Anexo A §A.8, Anexo B §B.5 | A.8 **CONFERE**; B.5 **ERRO DE CÁLCULO** (regra da cadeia) |
| D4 (`04_friedmann_eta_acao.md`) | Cap.1 §1.6, Cap.2, Anexo E §E.7, Anexo H §H.6 | **NÃO-DERIVÁVEL** da ação atual (postulado/extensão) |
| D5 (`05_rdot_ramo_dinamico.md`) | Cap.14 §14.11–14.14, Cap.5, Cap.13 §13.6 | ṙ≡0 **DERIVADO**; §14.12 **ERRO** (condição trocada) |
| D6 (`06_mu_alpha_quase_estatico.md`) | Cap.18 §18.3/§18.4/§18.7, Cap.7 §7.6 | ansatz Yukawa/α/η_slip **ERRO** (multi-polo, α_∞=0) |
| D7 (`07_modo_sigma_bessel.md`) | Cap.10 §10.3 | **CONFERE SOB HIPÓTESE** (\|m²\|≪H²; expoente geral k^(−ν)) |
| D8 (`08_mS0_dinamica_F.md`) | Cap.19 §19.3, benchmarks B1/B2 | **NÃO-DERIVÁVEL** (design observacional; pressuposto refutado) |

Erratum transversal: sinal da fonte na eq. de χ (Anexo E §E.3(3)) — a
ação dá −m²M_eff²F′V.

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
