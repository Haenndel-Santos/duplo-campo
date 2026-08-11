# Investigação 1 — Ramo Algébrico Pós-Erratum + G1-b — Resultado

**Data:** 2026-08-11. Script: `auditoria/code/investigacao1_ramo_algebrico.py`
(saída em `auditoria/code/out/investigacao1_ramo_algebrico.txt`). Fecha o
item 3.4 de `docs/veredito_setor_escalar_final.md` (a última porta interna
da F1 declarada "genuinamente aberta") e o protocolo G1-b de
`docs/gate1_identidade_relacional.md` §4.

---

## 1. Placar

| # | Pergunta | Resultado | Nível |
|---|---|---|---|
| 1(a) | O que muda na definição do ramo algébrico pós-erratum? | Nada — B(r)=0 é o primeiro fator da constraint fatorada, intocado pelo erratum; com β_n constante o resíduo do Gate 2 (−M_eff²m²p_φβ₁′) se anula identicamente | 1 |
| 1(b) | A degenerescência cinética na raiz exata (D1 pré-erratum) persiste? | **Sim** — kN ~ 1e-14–1e-18 em k=1,10,100, mesma ordem da D1 pré-erratum | 2b |
| 1(b) | A raiz exata é só degenerada, ou também doente? | **Também doente** — par taquiônico com taxa Im(ω)/H = 3.0000 exata, idêntica em k=1,10,100 (assinatura de massa, não de gradiente) | 2b |
| 1(b) | Existe corredor saudável perto da raiz? | **Não encontrado** — nenhum δ=(r−r_star)/r_star ∈ [−0.30,+0.30] testado tem os três k (1,10,100) simultaneamente limpos; um par taquiônico sobrevive em toda a faixa | 2b (fronteira declarada) |
| G1-b (R1) | Os modos patológicos (em toda a F1, β_n constante) são δφ₋-dominados? | **Não — R1 PASSA**: 17/17 instâncias patológicas (μ∈{0.1,0.3,1,3,10}, k=1,10) com \|⟨v,δφ₋⟩\|² = 0.0000 (critério: <0.05) | 2b (fronteira declarada) |

**Veredito combinado:** o ramo algébrico reprova de forma independente do
ramo finito (item 3.4 fechado, NO-GO), e G1-b passa. Pelas condições do
`gate1_identidade_relacional.md` §5 item 4 — "se G1-b passar E o ramo
algébrico pós-erratum também reprovar" — **R1 vira o enquadramento
oficial do no-go**: o problema é da REPRESENTAÇÃO F1 (setor de vínculos
da realização bimétrica HR), não do grau relacional primordial δΦ₋.

---

## 2. Parte 1 — o ramo algébrico

### 2.1 (a) — o que "estar no ramo algébrico" significa agora

A constraint de Bianchi fatorada é
$$\mathcal B(r)\cdot(\text{segundo fator}) = 0,\qquad \mathcal B(r)=\beta_1+2\beta_2 r\ \ (\text{F1},\ \beta_3=0).$$

O Erratum 01 corrigiu apenas o **segundo fator** — de $(H_g-\xi H_f)$
para $(N_f\dot a - N_g\dot b)$. O **ramo algébrico** é definido por
$\mathcal B(r_\star)=0$, que anula a constraint multiplicando o segundo
fator **seja qual for sua forma**. A definição do ramo — $r_\star =
-\beta_1/(2\beta_2)$, constante no tempo — não muda com o erratum.

Com $\beta_n$ constante (o caso desta investigação), $\beta_1'=0$, e o
resíduo do Gate 2 ($-M_{\rm eff}^2m^2p_\phi\beta_1'$, que aparece quando
$\beta_1$ depende de $\phi_-$ e a constraint deixa de fatorar) se anula
**identicamente** — a constraint continua fatorando de forma limpa
neste ramo, sem a complicação que a modulação introduziria.

**Achado adicional (não previsto no prompt original):** a identidade
cinemática deste ramo — $r={\rm const}\Rightarrow \dot b/b=\dot a/a
\Rightarrow \xi=N_f/N_g=H_g/H_f$ — é **exatamente** a fórmula que o
corpus v1 usava, incorretamente, como constraint *geral* do "ramo
dinâmico" (o que produzia $\dot r\equiv0$ "sempre", o erro do Erratum
01). O erratum não invalida essa fórmula; mostra que ela é a identidade
cinemática correta, mas **só neste ramo** (algébrico), não no ramo
geral. Por isso o script usa o $\xi=H/H_f$ **natural** de
`tdcp_pert_lib.benchmark()` na raiz exata, sem o override manual
($\xi=1$) que o "benchmark C" original da D1 usava como teste de
controle.

### 2.2 (b) — raiz exata: degenerescência E taquião

Na raiz exata ($\delta=0$, $r=r_\star=1.25$), com $\xi=H/H_f$ natural:

| k | modo | w² | kN | Im(ω)/H | classe |
|---|---|---|---|---|---|
| 1 | espectador | +1.892 | +0.124 | 0 | limpo |
| 1 | par relativo (×2, conjugados) | +3.894 ± 21.5i | −1.8e-18 | **3.0000** | TAQUIAO |
| 10 | espectador | +100.9 | +0.458 | 0 | limpo |
| 10 | par relativo (×2) | +782.9 ± 169i | +7.9e-17 | **3.0000** | TAQUIAO |
| 100 | espectador | +1.000e4 | +0.459 | 0 | limpo |
| 100 | par relativo (×2) | +7.869e4 ± 1680i | −1.4e-14 | **3.0000** | TAQUIAO |

A degenerescência cinética de D1 (kN ~ 1e-16) **persiste tal e qual**
no formalismo corrigido — mesma ordem de grandeza, mesmo par relativo.
O achado novo é que o mesmo par, ao mesmo tempo, é **taquiônico com
taxa exatamente 3.0H, idêntica nos três k** — assinatura de instabilidade
de **massa** (não de gradiente, que escalaria com k). A raiz exata do
ramo algébrico não é apenas patológica por degenerescência: é
patológica por instabilidade também.

### 2.3 (b) — corredor: não encontrado

Varredura $\delta=(r-r_\star)/r_\star \in \{\pm0.002,\pm0.01,\pm0.04,
\pm0.10,\pm0.20,\pm0.30\}$, cada ponto classificado em k=1, 10 E 100
(critério do projeto: saúde espectral em pelo menos dois k; aqui, três).

**Resultado: nenhum $\delta$ testado tem os três k simultaneamente
"limpo".** Em praticamente toda a faixa, k=1 e k=10 mostram uma mistura
"TAQUIAO/limpo" — ou seja, o par taquiônico da raiz **sobrevive** ao
sair da raiz; o que desaparece ao sair da raiz é só a degenerescência
numérica de kN (que passa de ~1e-18 para ~1e-2–1e-4), não a patologia
em si. Em $\delta=-0.30$ (o extremo mais afastado testado), o quadro
piora: um dos modos vira FANTASMA em vez de apenas taquiônico.

**Conclusão:** sair da raiz exata cura a degenerescência cinética, mas
não cura a doença — não há corredor saudável na faixa
$\delta\in[-0.30,+0.30]$ testada. O ramo algébrico reprova tanto NA
raiz (degenerado E taquiônico) quanto PERTO dela (não-degenerado, mas
ainda taquiônico e às vezes também fantasma).

**Fronteira declarada (nível 2b):** faixa testada $\delta\in[-0.30,
+0.30]$ apenas, no benchmark padrão ($\beta_1=1,\beta_2=-0.4$,
$M_g^2=M_f^2=1$). Não se pode excluir corredor saudável fora dessa
faixa ou em outros $(\beta_1,\beta_2)$ — mas dado que o próprio ramo
finito já reprova em ~1500 pontos do espaço de parâmetros
(`docs/no_go_beta_constante.md`), o prior para uma exceção aqui é baixo.

---

## 3. Parte 2 — G1-b: a patologia é δφ₋-dominada?

Protocolo (`docs/gate1_identidade_relacional.md` §4): projetar TODOS os
modos (sadios e patológicos) em δφ₋ (campo `dchi`, índice 6 dos 7 campos
da D1), no ponto fixo do ramo finito (mesmo fundo do no-go), μ∈{0.1,
0.3,1,3,10}, k=1 E k=10, β_n constante.

**Cobertura de μ=0.1:** a célula de referência (β₁,β₂)=(1,−0.4) não tem
fundo físico válido em μ=0.1 ($H^2\le0$ ou $\xi\le0$ — a cúbica não tem
raiz real positiva compatível ali). Para cobrir μ=0.1 de fato, o script
usa a célula da "fresta" já caracterizada em
`docs/no_go_beta_constante.md`/`modulacao_qep.py` ETAPA 2
(β₁=0.2, β₂=−1.0), onde μ=0.1 tem fundo válido e hospeda o fantasma
quase-nulo.

**Cross-validação (não planejada, mas decisiva):** nessa célula, o
script encontrou um modo com kN=−1.616e-05 em k=1, virando limpo em
k=10 — batendo, com quatro dígitos, com o kN_min=−1.6e-5 já reportado
em `docs/no_go_beta_constante.md`/`estrutura_analitica_par.py` para a
mesma célula, e reproduzindo exatamente a assinatura de dependência-em-k
já documentada ("FANTASMA em k=1, LIMPA em k=10"). Isso confirma que a
maquinaria de projeção de autovetores está calibrada corretamente contra
resultados independentes já estabelecidos.

### 3.1 Resultado

| μ | célula | k | modos patológicos | \|⟨v,δφ₋⟩\|² |
|---|---|---|---|---|
| 0.1 | fresta (0.2,−1.0) | 1 | 1× FANTASMA (kN=−1.6e-5) | 0.0000 |
| 0.1 | fresta (0.2,−1.0) | 10 | nenhum (todos limpos) | — |
| 0.3 | REF (1,−0.4) | 1, 10 | 1× TAQUIAO + 1× FANTASMA por k | 0.0000 (4/4) |
| 1.0 | REF (1,−0.4) | 1, 10 | 1× TAQUIAO + 1× FANTASMA por k | 0.0000 (4/4) |
| 3.0 | REF (1,−0.4) | 1, 10 | 1× TAQUIAO + 1× FANTASMA por k | 0.0000 (4/4) |
| 10.0 | REF (1,−0.4) | 1, 10 | 2× TAQUIAO (k=10 tem dois) | 0.0000 (4/4) |

**17 instâncias patológicas no total, todas com projeção em δφ₋ no
zero de ponto flutuante** (não apenas abaixo do limiar de 0.05 — o
próprio código do modo doente não toca δφ₋ nesta representação). O modo
espectador (dchi puro, m²=+0.3) aparece sempre limpo e com
\|⟨v,δφ₋⟩\|²=1.0000, como esperado — confirma que a decomposição está
correta e que o desacoplamento de δφ₋ dos modos doentes não é um
artefato de normalização.

### 3.2 Veredito de R1

**R1 PASSA**, com folga ampla (0.0000 << 0.05 em toda a varredura). A
composição espectral confirma o suporte de nível 2b já existente em
`docs/estrutura_par_relativo.md`: o dubleto de shifts $B_g\pm B_f$
(μ≥0.3) e o lapso $\Phi_f$ quase-nulo (μ=0.1) são os portadores da
doença — δφ₋ é espectador em ambos.

---

## 4. Consequência

Os dois braços do gate se fecharam na mesma sessão:

1. **Investigação 1 reprova** — o ramo algébrico não é uma saída para o
   no-go do setor escalar (item 3.4 de `docs/veredito_setor_escalar_final.md`
   fechado: NO-GO, não mais "genuinamente aberto").
2. **G1-b passa** — a patologia, em toda a F1 testada (ramo finito, β_n
   constante), não alcança δφ₋.

Pela condição declarada em `docs/gate1_identidade_relacional.md` §5
item 4: **R1 vira o enquadramento oficial do no-go**. Isto é, o
resultado central do programa (`docs/veredito_setor_escalar_final.md`)
passa a ser lido como: *"a representação F1 (helicity-0 da realização
bimétrica HR) não admite setor escalar saudável — mas nada até aqui
demonstra que o grau relacional primordial δΦ₋, enquanto tal, seja o
modo doente."* O trilema Φ₋→(g,f) (`gate1_identidade_relacional.md` §3)
permanece aberto entre os ramos (a) modulador testado e reprovado, (b)
g/f efetivas de um coletivo 𝓡 (R2 — a condensação dinâmica, próxima da
fila), (c) grau relacional sem segunda métrica.

## 5. O que ainda falta

- **G1-a** (tabela documental de identidade, custo ~zero) —
  **CONCLUÍDO 2026-08-11**: `docs/gate1a_tabela_identidade.md` (zero
  elos de identidade derivados na cadeia; flag epistêmica adicionada ao
  dicionário).
- **G1-c** (nota do trilema, teórico) — próximo passo.
- **Investigação 2** (condensação dinâmica, $p_\phi\neq0$) — agora
  promovida a teste direto de R2, conforme `gate1_identidade_relacional.md`
  §5 item 4.
