# R-3c — O Mecanismo do Crescimento Tardio: Ponto Fixo, e a Esquina β₁-Grande — Resultado

**Data:** 2026-08-12. Script: `auditoria/code/r3c_pousada_mecanismo.py`
(saída em `auditoria/code/out/r3c_pousada_mecanismo.txt`). Execução:
autor (.venv). Fecha a forquilha declarada em
`resultado_r3b_pousada.md` §2–3 (genuína-vs-secular;
modulação-vs-β₁-grande).

**Controles:** R3c-CONT 0.005 ✓ (braço Γ=10 reproduz pré/rolagem
oficiais). **Consistência interna nova e forte:** nos braços
β-constantes (F′=0) a norma métrica das ICs de δχ é **0.00 exato** —
o espectador desacopla como a teoria manda (a fiação modulação↔δχ do
instrumento é real, não vazamento numérico). negK=1 em TODOS os braços
e âncoras — inclusive no β-constante estático β₁=4.47 (universalidade
do fantasma estrutural do R-1/R-2 estendida à esquina).

---

## 1. Os dois vereditos

### 1.1 R3c-DRIFT = PONTO-FIXO (na banda k_phys ~ H)

Curva taxa(desvio) em k_c=12500, tardia:

| fundo | Aosc tardia (vs próprio fim) | taxa met máx |
|---|---|---|
| ORG (Γ=0) | 1.55e-2 | +0.98 |
| Γ=10 (aprox. rápida) | 1.07e-2 | **+1.21** |
| Γ=30 (R-3b) | 3.74e-2 | +1.12 |
| Γ=100 (aprox. lenta) | 3.12e-2 | +1.02 |

Taxa **plana** (spread 1.23×, levemente ANTI-correlacionada: o menor
desvio deu a maior taxa) com desvio nominal variando 3.5×. E o
contraste verdadeiro é MAIOR: o Γ=100 não converge até a=10⁵
(χ/v_fim=0.975 vs assíntota ~0.93–0.94; aproximação 0.22/H), então seu
Aosc "vs próprio fim" subestima a distância real ao ponto fixo —
distância verdadeira varia ~1%→~7% entre os braços, taxa imóvel. **O
crescimento na banda não é alimentado pelo desvio residual.** A
alternativa secular do R-3b §2 morre; sobra instabilidade do ponto.

### 1.2 R3c-BETA = ESQUINA-β₁: o β-constante ESTÁTICO cresce igual

O fundo β-constante puro com β₁=4.47 (sem modulação, sem χ dinâmico,
sem pouso; r=0.516, H=1.125, ξ=0.516 — quase o ponto onde o fundo
pousado senta, r~0.50/H~1.14):

- **G1 (k_c=12500):** cresce em TODAS as épocas — pré +1.55, rolagem
  +1.46, pouso +1.95, tardia **+1.08** (≈ a taxa da família pousada).
- **G2 (k_c=1250):** tardia DILUI (−1.1 a −2.0); cresce só cedo
  (janelas com k_phys/H ≳ 0.3).

**Conclusão:** o crescimento tardio da "família pousada" na banda
k_phys~H é, na verdade, **da família β-constante** — o fundo pousado
herda a instabilidade do ponto da classe onde pousa (β₁_eff=4.47). A
R-1 não o viu por DUPLA lacuna de amostragem: β₁ ≤ 2 no retângulo, E
k_phys/H ≲ 0.5 nas janelas tardias (k_c ≤ 100 com a ≤ 2000).

**Caveat de atribuição (declarado):** "esquina β₁-grande" é
provisório — o controle β₁=1 NA banda k_phys~H tardia não existe
ainda; pode ser a esquina, pode ser a classe inteira na banda. O R-4a
decide (varredura β₁ × k, com controle GR na banda como portão).

**RESOLVIDO (R-4a, 2026-08-12):** β₁=1 cresce na banda (+0.93) — é a
**classe inteira**, não a esquina; GR-NULL passa; transiente de
cruzamento nos dois fundos. Ver `resultado_r4a_mapa.md`.

## 2. A síntese em k_phys/H — e a releitura da "estrutura IR"

Juntando R-3/R-3b/R-3c, o padrão por janela (bloco métrico):

| k_phys/H na janela | comportamento | evidência |
|---|---|---|
| ≳ 2–3 | ~0 (não cresce) | D/E tardia (+0.06); k=25000 |
| ~0.3–1.5 (cruzamento) | **cresce ~ +1 a +2/H** | G1 todas; pousada k=12500 tardia; G2 pré/rolagem |
| ≲ 0.1–0.2 (super profundo) | dilui no estático | G2 pouso/tardia; K (Γ=100) |
| ≲ 0.1 no POUSADO com dinâmica residual | cresce (+1.05/+1.87) | ORG/Γ30 k=1250 — **anomalia** |

- k_phys/H = 1 cruza em a≈11000 p/ k_c=12500 (dentro da tardia ✓) e
  a≈22000 p/ k_c=25000 (**fora** — por isso o +0.06 do R-3b: o modo
  não tinha cruzado). A "morte em k_phys≳2" era isso.
- A exceção sub-horizonte: o crescimento cedo (pré) é **IC-específico**
  (par E_f: IC1/IC4; o par Ψ_f dilui) em todos os fundos — enquanto o
  crescimento da banda tardia é Ψ_f-dominado (G1 tardia: IC0/IC4
  crescem, IC1 fica em +0.06). Duas componentes de modo distintas;
  decomposição registrada, mecanismo aberto.
- **Anomalia IR do pousado** (k=1250 tardia): cresce no ORG (+1.05) e
  Γ=30 (+1.87), morre no estático (G2 −1.08) e no Γ=100 (K −0.12).
  Estado-sensível, NÃO é ponto-fixo, NÃO é paramétrico simples (R-3b
  F persistiu com Γ=30). Sub-estrutura declarada ABERTA — aguarda o
  mapa (não bloqueia o quadro principal).

## 3. Instrumento congelado: agora erra nos dois sentidos

No estático 4.47 o congelado dá σ/H=1.66–1.72 e a dinâmica real dá
+1.08 (primeira vez que ficam na mesma ordem); no G2 dá 3.12 contra
−1.85 real; no k=25000 dava 41.7 contra +0.06. O congelado não tem
correlação com a dinâmica nesta classe — em nenhuma direção. (Mais um
tijolo do aviso metodológico do paper.)

## 4. Estratificação epistêmica

| Afirmação | Nível |
|---|---|
| Banda k_phys~H: taxa plana sob desvio 1%→7% (ponto-fixo, não secular) | 2b |
| Mesma banda cresce no β-constante ESTÁTICO β₁=4.47 (+1.08) | 2b |
| Logo: fenômeno da classe β-constante; pousado herda do ponto | 2b (na esquina testada) |
| "β₁-grande" como fronteira da região instável | **provisório** — controle β₁=1 na banda pendente (R-4a) |
| Releitura por cruzamento de horizonte (liga ~cruzamento, morre super-profundo) | 2b descritivo; mecanismo nível 3 |
| Anomalia IR do pousado (k=1250) | 2b observacional; mecanismo ABERTO |
| Par E_f cresce cedo em todos os fundos (IC-específico) | 2b descritivo; interpretação aberta |
| δχ desacopla exato com F′=0; negK=1 inclusive no estático 4.47 | 2b (consistência do instrumento; insumo Gate F) |

## 5. Fila — o R-4 abre pelo mapa

- **R-4a** (`auditoria/code/r4a_mapa_tardio.py`, pronto): (i) controle
  GR **na banda** (k_phys/H~1 na tardia, fundo estático — o portão de
  credibilidade que nenhum controle anterior cobriu; abortivo);
  (ii) varredura β₁ ∈ {1, 2, 3, 4.47} × k ∈ {banda, 3×, 0.1×} nos
  fundos estáticos — fronteira da região instável em β₁ (se β₁=1
  crescer na banda: é a CLASSE inteira, e o "estável tarde" de
  D2/R-1 era artefato de amostragem em k — reescreve o enunciado);
  (iii) extensão em a (até 80000): a banda é TRANSIENTE de cruzamento
  (lnA finito por modo) ou SUSTENTADA (no-go dinâmico real da região)?
  — nos fundos estático-4.47 E pousado.
- Depois: R-4b (lnA e vínculos com o quadro certo), Gate F-a.
- Enunciado do cap. 07: aguarda R-4a (o fenômeno mudou de dono duas
  vezes em dois scripts — disciplina de não escrever antes do mapa).
