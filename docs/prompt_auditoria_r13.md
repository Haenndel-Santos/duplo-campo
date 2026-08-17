# Prompt — auditoria adversarial do R-13a e R-13b

Copiar o bloco abaixo como primeira mensagem da sessão de auditoria.
Escrito em 2026-08-17, logo após o merge de `revisao-corpus-pos-r12`,
pela sessão que produziu o Erratum-03 e o teorema de c_s².

**Por que esta auditoria.** O R-13a/R-13b substituiu a exclusão do ramo
infinito (o argumento `ξ = 0` foi revogado; entrou o ghost de Higuchi)
e requalificou um resultado de topo do corpus (`m_T²/H² → 12`). São
mudanças estruturais, e a sessão anterior não as auditou — leu títulos,
mensagens de commit e os trechos que o merge exibiu. Dado que o
Erratum-03 nasceu exatamente desse tipo de escrutínio, o mesmo
tratamento se justifica aqui.

**Duas suspeitas óbvias já foram levantadas e caíram** — estão listadas
no prompt como "não refazer", para não gastar sessão com elas.

---

```
Auditoria adversarial do R-13a e R-13b (TDCP).
Repositório: C:\Haenndel Projects\Duplo Campo (branch master, já com o
merge de revisao-corpus-pos-r12). `git pull` AGORA. Cálculos pelo .venv
(sympy 1.14.0, numpy 2.5.1, scipy 1.16.3). `git push` ao fechar; nunca
force-push.

LEIA NESTA ORDEM:
1. docs/resultado_r13a_criterio_higuchi_fonte.md
2. docs/resultado_r13b_ibb_ramo_infinito.md
3. auditoria/code/r13b_ibb_ramo_infinito.py + out/
4. docs/posicionamento_literatura.md (a tabela de novidade)
5. docs/resultado_r12_instrumento_e_cs2.md (Erratum-03) e
   docs/resultado_r12b_teorema_cs2.md (o teorema do ramo finito)

O QUE JÁ FOI VERIFICADO — NÃO REFAZER:
- o r13b PROÍBE np.gradient por monkey-patch (regra 6). O Erratum-03
  não o atinge.
- `0 < β₄ < 2β₁` é o caso μ=1 de `0 < β₄/β₁ < 2μ^{3/2}` (a fonte fixa
  M_f = M_g, nota 6 de 1503.07436). Já reconciliado no corpus.

ALVOS, em ordem de alavancagem:

A. A TRADUÇÃO `Higuchi ⟺ ξ ≥ r ⟺ r′ ≥ 0`. É o passo que sustenta todo
   o veredito. Re-derive do zero, por rota independente da usada no
   R-13a. Confira em particular o mapa `r_K = √μ r`,
   `β_n^K = A μ^{−n/2} β_n`, alegado sobredeterminado pelas duas
   Friedmann: mostre que ele fecha, ou onde não fecha.

B. A ARMADILHA DE SINAL entre 1407.4331 (`X ∝ e^{iωN}`) e 1503.07436
   (`Ξ_i ∝ e^{ωt}`), com a alegação de que `ω² < 0` significa ESTÁVEL
   na segunda e instável na primeira. É de alta alavancagem porque
   reconcilia duas fontes; se estiver invertida, o veredito de
   complementaridade inverte junto. Verifique nas fontes.

C. O ELO NÃO MEDIDO INTERNAMENTE. O corpus declara que "o gradiente do
   IBB é saudável SEGUNDO A FONTE, não medido por nós". A frase de
   complementaridade — o achado do arco — apoia-se metade em medida
   própria (Higuchi) e metade em literatura (gradiente). Meça o
   `c_s²` do IBB com a maquinaria limpa do R-12f/g (fundo em forma
   fechada + estêncil de 8ª ordem, jamais np.gradient) e feche o elo,
   ou registre por que não é possível.

D. `m_T²/H² = 3, não 12`. O R-13a conclui que o funcional FLRW de
   Higuchi da fonte dá 3 onde o corpus dizia 12, e isso rebaixou um
   resultado de 1º para 2º no ranking. Toca a predição m_T ≈ 2.3 H₀.
   Estabeleça exatamente: o 12 continua correto na NOSSA convenção? O
   que exatamente mudou — o número, o objeto, ou só o rótulo?

E. A BORDA. `r′ < 0` em 100% com `max r′ = −6.05e−5`. Essa margem é
   estreita. Varra a vizinhança das fronteiras da janela
   (β₄/β₁ → 0⁺ e → 2μ^{3/2}⁻) com resolução maior e em precisão
   estendida: o sinal de r′ sobrevive, ou há célula onde ele cruza?
   E o que define "célula IBB genuína" — há teste de que a raiz é o
   ramo infinito e não um espúrio?

F. CEGUEIRA DOS GATES. O R-13b declara que não mede gradiente. Liste o
   que MAIS ele não consegue ver, e diga se alguma dessas cegueiras
   morde o veredito.

DISCIPLINA (obrigatória):
- critérios pré-declarados no cabeçalho de cada script, antes de rodar;
  veredito só pelos critérios.
- V-XREP: todo número decisivo por dois canais independentes.
- derivadas de fundo em FORMA FECHADA; onde não der, estêncil de ordem
  ≥ 8 COM teste de refino. np.gradient proibido.
- todo gate declara o que NÃO consegue ver.
- rodadas ruins preservadas nos outs; commits granulares.
- distinga sempre ENUNCIADO de VALOR: o Erratum-03 corrigiu valores sem
  derrubar enunciados; use a mesma separação.

RESULTADO ESPERADO: um doc `docs/auditoria_r13.md` com veredito por
alvo (CONFIRMADO / CORRIGIDO / REFUTADO / INDECIDIDO), e os banners de
supersessão que forem necessários. Se nada cair, isso é resultado: diga
com as medidas que o sustentam.
```

---

## Nota de prioridade

**C é o alvo mais valioso.** A frase de complementaridade que fecha o
arco tem uma perna medida (Higuchi, nossa) e outra emprestada
(gradiente do IBB, da fonte). Esta sessão exibiu os dois modos de falha
possíveis desse arranjo: número do repositório errado com literatura
certa (o `c_s² = −1`, que o Erratum-03 resgatou), e literatura
registrada durante meses sem confronto (a instabilidade de gradiente do
ramo finito, que só o R-10a foi medir).

**D é o que mais pode doer**, porque toca a única previsão falseável
viva do programa (m_T ≈ 2.3 H₀).

**E é o mais barato** e pode ser decisivo sozinho: uma margem de
`6e−5` em 108 células é estreita o bastante para que a fronteira da
janela mereça varredura própria.
