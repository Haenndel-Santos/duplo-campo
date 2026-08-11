# Registro de Processo — 2026-08-11: o Dia da Reversão

**Natureza deste documento:** registro histórico-metodológico, pedido
pelo autor. Não é resultado científico novo — é a crônica de como o
método do projeto (estratificação epistêmica, critérios pré-declarados,
auto-testes de poder, antecipação de referee) funcionou num dia em que
o resultado central do programa foi construído, blindado e então
**revertido pelo próprio processo** — tudo com rastro completo em git
(14 commits, cada um com script + saída versionada + doc).

---

## 1. A cronologia (um dia, quatro atos)

**Ato I — o arco fecha (manhã).** Investigação 1 (ramo algébrico
pós-erratum): NO-GO, com G1-b embutido (R1 passa, projeção zero).
Gate 1 fechado (G1-a: zero elos derivados na cadeia; G1-c: prior
Weinberg–Witten parcialmente demolido, circularidade HR–Goldstone como
obstrução real). Decisão 1 do autor: v1 congelada, v2 enxuta iniciada.

**Ato II — o arco se aprofunda (tarde).** C1 (derivação de
Stückelberg): o taquião congelado de k=1 É o helicity-0 (π_L 0.995+);
mecanismo corrigido — massa taquiônica como resíduo de cancelamento
quebra×EH. Investigação 2 (Fases A e B): o fundo de rolagem p_φ≠0
existe, desloca ordem 1 dos ramos, a condensação dirige r (×16), e o
espectro congelado é *pior* lá. Conclusão do momento: "o arco
computacional da F1 está completo; escalar ✗ em todos os regimes".

**Ato III — a blindagem que virou bisturi (noite, parte 1).**
Posicionamento na literatura (4 agentes, disciplina
VERIFICADO-NA-FONTE): a literatura diz "instável cedo, saudável
tarde" — nosso taquião tardio seria novo *se físico*, e o referee
exigiria duas provas. D1 (redução explícita de vínculos, exata em
racionais): o par doente SOBREVIVE à eliminação dos multiplicadores —
espectro idêntico ao QEP, fantasma como assinatura invariante de
K_red. A primeira linha de defesa do taquião ficou pronta.

**Ato IV — a reversão (noite, parte 2).** D2 (evolução temporal real
do sistema reduzido, com os termos Ċ que faltavam à tentativa de DAE
de meses atrás): as taxas reais não batem o congelado. Sondas de
diagnóstico: as matrizes comóveis **nunca assentam** (K~a³,
|K̇|/|K|~2H no "ponto fixo") — o instrumento congelado descarta os
termos que dominam. Rodada oficial endurecida: no ponto fixo profundo
tudo dilui a −3/2·H; o crescimento real é transiente, limitado,
tipo-gradiente — **o quadro da literatura**. O "taquião eterno" caiu.
Todos os vereditos de saúde por espectro congelado foram suspensos
(`veredito_setor_escalar_final.md` §8).

## 2. O que pegou o quê (a taxonomia dos erros do projeto)

| Erro | Instrumento que o pegou | Quando |
|---|---|---|
| 115 erros de escrita do corpus | leitura sequencial (auditoria 856) | 08/2026 |
| Constraint de Bianchi errada (conteúdo, não escrita) | **recalcular** (duas rotas independentes) — Erratum 01 | 07/08 |
| Cinco testes vácuos | auto-testes de **poder de detecção** | ao longo |
| Três priors de literatura errados (M_f≫M_g "cura"; Higuchi D8; W–W forte demais) | **cálculo contra o prior** | ao longo |
| **O próprio instrumento de saúde (espectro congelado)** | **evolução temporal real**, forçada pela antecipação de referee do posicionamento | 11/08 |

A progressão é instrutiva: cada camada de erro exigiu um instrumento
mais forte que o anterior — e o último erro era do *instrumento*, não
do objeto. Leitura não pega erro de conteúdo; recálculo não pega
instrumento ruim; só a pergunta "o que exatamente esta medida
significa dinamicamente?" pegou.

## 3. Onde o método fez diferença concreta

1. **Critérios pré-declarados com ramo de falha.** O script do D2
   tinha, escrito ANTES de rodar: "se não-genérico → ENFRAQUECER o
   enunciado e reportar como está". Sem isso, a tentação de tratar a
   1ª rodada como "bug a consertar até dar o esperado" seria real.
2. **Antecipação de referee como pauta de trabalho.** O item D1/D2 do
   posicionamento não era burocracia: era exatamente a pergunta que
   derrubou o resultado. O custo de descobrir internamente: um dia.
   O custo de descobrir via referee (ou pós-publicação): a
   credibilidade do programa.
3. **Duas rotas + âncoras cruzadas em tudo.** A reversão só é crível
   porque o integrador foi validado em GR, o halving convergiu, as
   matrizes congeladas-de-verdade crescem como previsto, e a redução
   D1 tinha acabado de provar que QEP e redução explícita coincidem.
   A reversão não é "outro número": é o mesmo instrumental, com o
   tempo ligado.
4. **Nada foi apagado.** O taquião congelado continua nos documentos,
   reclassificado (caracterização de espectro congelado, não veredito
   dinâmico), com as datas e os motivos. A 1ª rodada do D2 está
   preservada. Quem ler o repositório vê o processo inteiro,
   inclusive o erro.
5. **A regra "ponto fixo = juiz sem caveat de congelamento" estava
   errada — e o registro mostra por quê**: ela congelava também os
   fatores explícitos de a(t), que não são taxa de fundo. A regra de
   método foi corrigida no ato (`resultado_d2_evolucao.md`).

## 4. O estado honesto ao fim do dia

- A TDCP-F1 **não está morta como se concluiu de manhã** — o setor
  escalar tardio é dinamicamente estável (linear) na célula testada, e
  a pergunta viva mudou: a **assinatura cinética indefinida**
  (fantasma estrutural, D1) é letal ou é mais um artefato de
  representação? Fila R-1..R-4 decide o que sobrevive do no-go.
- Os ativos que o dia consolidou independem da reversão: fundo ✓,
  tensor ✓, Erratum 01, o regime não-fatorado (Fase A), o limiar de
  back-reaction, a maquinaria de redução+evolução validada, o
  posicionamento na literatura, e o Gate 1 (cujas medidas de
  composição são sobre autovetores congelados — corretas como tais).
- O processo científico, funcionando: hipótese → teste → blindagem →
  autocrítica instrumentada → reversão → nova pergunta. Em um dia,
  com rastro completo.

*"Relatar como resultado, não como fracasso" — o plano v2 previa isso
para o no-go. Vale igualmente para o no-go do no-go.*
