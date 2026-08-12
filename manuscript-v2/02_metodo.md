# 02 — Método

**Por que este capítulo vem antes da física:** o método pegou cinco
testes vácuos, um erro estrutural do corpus (Bianchi, Erratum-01) e —
o caso máximo — o resultado central anterior do próprio programa
(Erratum-02). Num projeto onde a mesma equipe deriva, implementa e
julga, o método não é ornamento: é o único árbitro que restou de pé
em todas as crises. Este capítulo o expõe como resultado.

## 1. As regras

1. **Estratificação epistêmica declarada.** Todo resultado carrega um
   nível: **1** (derivado e verificado por duas rotas independentes),
   **2a** (derivado por uma rota, verificado numericamente), **2b**
   (numérico com fronteiras de varredura declaradas), **3**
   (literatura/adotado). Fronteiras de varredura sempre no enunciado.
2. **Gates com critério de falha pré-declarado.** O critério de
   sucesso/falha é escrito no cabeçalho do script ANTES da execução;
   o veredito sai só pelos critérios. Rodadas ruins são preservadas
   nos outputs (as "1ªs rodadas" dos scripts R-6/R-7/R-8 estão todas
   no histórico git, com o que ensinaram).
3. **Auto-teste de poder.** Um teste que não consegue reprovar um
   caso sabidamente falso não pode aprovar nada (os ramos "PODER"
   dos gates; o F-a teve o poder reprovado e por isso o seu SUP nunca
   foi interpretado).
4. **Rota dupla para resultados estruturais.** Duas derivações
   independentes ou nada (Bianchi: rota canônica + rota lagrangiana;
   equivalência de ações no Erratum-02: prova exata off-shell).
5. **Rastreabilidade** (Gate 10): nenhuma afirmação interpretativa
   sem apontar a derivação; toda afirmação quantitativa cita o doc de
   resultado E o script/saída versionados.

## 2. O caso máximo: Erratum-02 em quatro lições

Entre 2026-08-11 e 08-12, uma rotina numérica de redução de vínculos
(`reduz_ponto`, replicada de script em script desde o D-2) contava o
termo de conexão Ċ **duas vezes** nas entradas fora da diagonal de
W_XX. O erro valia 1.4–6.1% das matrizes — pequeno e *suave*. O que
ele produziu não foi ruído: foi um **terceiro grau de liberdade
escalar coerente**, com fantasma canônico "assentado" (ω₀/H ≈ 7–12),
banda de amplificação (lnA ≈ +4), enunciado de strong coupling e uma
previsão observacional falsificável (excesso ISW 2–8× em baixo-ℓ) —
tudo internamente consistente, convergente em resolução e aprovado
pelos gates da época. (Cadeia completa e queda: cap. 07; fontes:
`auditoria/erratum_02_reducao_numerica.md`, saídas r6b–r6d.)

**Lição 1 — consistência interna não é correção.** O sistema espúrio
era um sistema dinâmico legítimo — só que não era o da teoria. Todos
os validadores *internos* (V-ETA, V-RES, halvings) passavam porque
validavam o sistema errado contra ele mesmo.

**Lição 2 — representação única é ponto cego.** O bug era invisível
em qualquer teste feito na mesma representação (Γ–Γ com absorção).
Caiu quando uma construção ADM independente (reauditoria externa)
deu det K = 0 simbólico — e o repositório provou que as duas ações
eram A MESMA (r6c: identidade exata, racional, off-shell, por peças)
e localizou o erro linha a linha (r6d). Institucionalizado como
**V-XREP-b**: Γ–Γ vs ADM obrigatório a cada mudança da maquinaria; e
**V-XREP-a**: dois canais independentes de Ċ (grade vs simbólico) em
toda trilha — que, na estreia, pegou uma inconsistência real do fundo
Euler (R-7c, 8/8 braços bloqueados até a correção).

**Lição 3 — normalização é onde artefatos nascem.** Três episódios da
mesma família: as energias do R-2 (descartadas por poluição de
normalização), o "assentamento" canônico do Gate F-b (dividir por
√|λ₀| com λ₀ espúrio fabrica frequências estáveis), e as taxas de
envelope do R-7e (+11H que a autópsia reduziu a artefato de ω²(t)
variável — com normalização congelada, o campo DECAI). Regra
resultante: ganhos e taxas sempre com **normalização congelada**;
variáveis **equilibradas** (B̃ = kB, Ẽ = k²E) antes de qualquer
redução.

**Lição 4 — o gate que segura é o pré-declarado.** O R-7e disparou
SUSPEITO exatamente como desenhado e a leitura errada ("amplificação
na janela") nunca foi publicada; a autópsia decidiu com medidas
robustas e halving fino (`auditoria/code/out/r7e_halving_fino.txt`).
O contraste com a v1 — que publicava interpretação antes de
derivação — é o argumento deste capítulo.

## 3. O placar do método

| Episódio | O que o método fez | Fonte |
|---|---|---|
| 5 testes vácuos (era da auditoria) | detectados por auto-teste de poder | `auditoria/parecer_tecnico.md` |
| Constraint de Bianchi errada no corpus | rota dupla derrubou; Erratum-01 | `auditoria/erratum_01_bianchi.md` |
| Vereditos congelados inválidos como dinâmica | D-2 (evolução real vs QEP congelado) | `docs/resultado_d2_evolucao.md` |
| O 3º DOF espúrio e toda a sua fenomenologia | auditoria externa + prova de mesma-ação + bug linha a linha; Erratum-02 | `auditoria/erratum_02_reducao_numerica.md`, r6c/r6d |
| Inconsistência Euler do fundo pousado | V-XREP-a na estreia (R-7c 1ª rodada) | `docs/resultado_r7_cascata.md` §3 |
| Artefato de envelope na janela | gate SUSPEITO + autópsia + halving fino | `docs/resultado_r7e_saude_interna.md` §2 |

O que este placar significa: os resultados dos caps. 05–09 não são
confiáveis por terem sido calculados com cuidado — são confiáveis
porque o processo que os produziu já demonstrou, seis vezes, que
derruba os próprios resultados quando estão errados.
