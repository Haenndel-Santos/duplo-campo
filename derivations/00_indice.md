# Índice das Derivações — Fechamento Matemático do Corpo TDCP

Consolidação do ciclo de derivações (PROMPT 2, 2026-08-05/06). Cada
item tem documento próprio (`NN_*.md`), script verificável
(`code/NN_*.py`) e saídas (`code/out/`). Numeração de capítulos:
**atual** (pós-renumeração; mapa no `plano_derivacoes.md`).

## Quadro geral

| # | Tema | Classificação | Resultado em uma linha |
|---|------|---------------|------------------------|
| 1 | K_ij, Ω_ij do setor escalar | **DERIVADO** | 3 modos em fundo congelado; par relativo fantasma no ramo dinâmico (c²=ξ²/r²) e degenerado na raiz algébrica; claims do Cap.15 §15.4/§15.5 refutadas |
| 2 | Ação TT e m_T² | **DERIVADO** | m_T² depende de ξ: prefator M_eff²[1/M_g²+ξ/(M_f²r³)] e fator r[β₁+β₂(ξ+r)]; Cap.16 errado no cinético e na massa; Anexo D §D.3 confirmado |
| 3 | ∂V/∂N_g com regra da cadeia | **DERIVADO** | ξ e β₄ cancelam exatamente; Anexo A §A.8 estava certo; Anexo B §B.5 tinha passo faltando |
| 4 | H²=(8πG/3)ρ/(1−η) de uma ação | **NÃO DERIVÁVEL SEM ACOPLAMENTO ADICIONAL** | η ausente da ação; extensão mínima Ω(η)R_g produz termo extra Hη̇/(1−η); forma postulada só vale no regime adiabático |
| 5 | ṙ no ramo dinâmico | **DERIVADO** | ṙ≡0 exatamente; §14.12 usa condição não-equivalente; r(t) genuíno exige β_n(φ) com raiz móvel (**hipótese adicional**) |
| 6 | μ(k,a), α(a) derivados | **DERIVADO** | μ multi-polo (7 polos; pares complexos/positivos no ramo instável); α_∞=0 exato; ansatz Yukawa do Cap.18 §18.3/§18.4/§18.7 refutado |
| 7 | Modo σ_k por Hankel | **DERIVADO SOB HIPÓTESE** (dS + Bunch–Davies) | σ_k∼k^(−ν), ν=√(9/4+\|m²\|/H²); k^(−3/2) só se \|m²\|≪H²; previsão nova n_σ−1≈−(2/3)\|m²\|/H² |
| 8 | Faixa m_S0∼(30–300)H₀ | **NÃO DERIVÁVEL SEM DADO EXTERNO** | é design observacional (posição do joelho); scan sem região viável (Higuchi real falha); o joelho único pressuposto não existe (ver 1/6) |

## Achados transversais (não previstos no prompt)

- **Sinal da fonte na equação de χ**: a ação (F.1) dá
  $\ddot\chi+3H\dot\chi+U'=-m^2M_{eff}^2F'V$; o Anexo E §E.3(3) declara
  **+**. Erratum objetivo.
- **Cone causal do setor f**: $c_f^2=\xi^2/r^2$ aparece de forma
  idêntica no setor tensorial (D2) e no par escalar relativo (D1) —
  assinatura estrutural robusta da teoria.
- **Ramo dinâmico duplamente inviável**: ṙ≡0 (D5) **e** par escalar
  fantasma/taquiônico (D1) — exatamente o ramo que o Anexo E §E.3(6)
  declara como "escolha TDCP principal". A via consistente é o ramo
  algébrico com raiz móvel β_n(φ) (D5 §4.1), que por sua vez leva o par
  relativo à degenerescência/forte acoplamento na raiz exata (D1,
  benchmark C) — o corpo precisa escolher e enfrentar uma das duas.
- **Metodologia**: fixar gauge na ação perde constraints; truncagem QS
  por símbolos viola a hierarquia da Friedmann; equação de momento sem
  fonte de velocidade contamina os potenciais — três armadilhas
  documentadas nos write-ups 1 e 6, todas pegas por calibração
  GR/auto-testes embutidos.

## Propostas de atualização do corpo principal (SEM editar nesta etapa)

Por capítulo/anexo, o que precisa mudar para refletir os resultados:

- **Cap.1 §1.6, Cap.2, Anexo E §E.7, Anexo H §H.6** — reclassificar
  $H^2=\tfrac{8\pi G}{3}\tfrac{\rho}{1-\eta}$ como extensão proposta
  (acoplamento não-mínimo + constraint) válida no regime adiabático
  $|\dot\eta|\ll H$, citando a Derivação 4; nunca como consequência da
  ação bimétrica.
- **Cap.5 / Cap.13 §13.6 / Cap.14 §§14.11–14.14** — substituir a
  narrativa do "ramo dinâmico com r(t)" pelo resultado ṙ≡0 (D5);
  renomear a via consistente como "ramo algébrico com raiz móvel
  r★(φ(t))" com a condição de adiabaticidade; remover a derivação de
  §14.12 (condição H_b=ξH_g não-equivalente).
- **Cap.6.2** — manter a contagem de 3 modos (confirmada), mas
  substituir as condições §6.6–6.8 pelas derivadas (a saúde do setor
  não é decidida por β₁+2β₂r).
- **Anexo C** — corrigir §C.3 (contagem 2 → 3 na análise congelada, com
  a ressalva da constraint temporal); reescrever §C.7/§C.10 com as
  matrizes reais (out/01_matrices.txt); rebaixar §C.11 a conjectura não
  demonstrada.
- **Cap.15** — §15.4/§15.5: substituir as claims pela estrutura real
  (par relativo patológico no ramo dinâmico; degenerescência na raiz);
  §15.6 ganha suporte parcial (a degenerescência na raiz é real, mas
  pela cinética, não pela massa).
- **Cap.16 / Anexo D** — §16.2: cinético corrigido para M_f²b³/ξ
  (Anexo D); §16.2/§16.4: m_mix² e m_T² substituídos pelas formas com ξ
  (D2, caixa §3.3); §16.6 (m_T²∼r·m_S²): remover (ambos os lados da
  relação caíram); §16.5/§16.8 e Anexo D §D.7: refazer Higuchi com o
  m_T² real — no ramo dinâmico do benchmark, m_T²<0.
- **Cap.17** — as cadeias EFT que usam m_T²∼r(β₁+2β₂r) herdam a
  correção de ξ; refazer §17.2–17.4 com a forma da D2.
- **Cap.10 §10.3** — corrigir σ_k∼k^(−3/2) para k^(−ν) com a condição
  |m_σ²|≪H² explícita; adotar a previsão n_σ−1≈−(2/3)|m_σ²|/H² (D7).
- **Cap.18** — §18.3/§18.4/§18.7: substituir o ansatz Yukawa e α(a)
  pela estrutura multi-polo derivada com α_∞=0 (D6; formas exatas em
  out/06_matrices.txt); a assinatura observacional correta é desvio em
  escalas intermediárias com Σ≈1.
- **Cap.19** — reclassificar m_S0∼(30–300)H₀ como benchmark de projeto
  (D8); reconstruir B1/B2 sobre a forma multi-polo; a seção EFT
  (§"escolher m_S0 não viola EFT") fica sem objeto até a nova
  parametrização.
- **Anexo B §B.5** — completar a regra da cadeia (D3) e alinhar o
  resultado citado ao Anexo A §A.8 (com F(χ)).
- **Anexo E** — §E.3(3): corrigir o sinal da fonte (−F′V); §E.3(6):
  a escolha do ramo dinâmico precisa ser revista à luz de D1/D5;
  §E.7: ver Cap.1 acima.
- **Anexo F** — a análise de pontos críticos que usa B(r)=β₁+2β₂r+β₃r²
  continua válida como estrutura, mas as conclusões de estabilidade
  associadas a B(r)>0 herdam a correção da D1.

## Como reproduzir

```
cd derivations/code
python tdcp_pert_lib.py            # auto-testes da biblioteca
python 02_setor_tensorial_mT2.py
python 07_bessel_sigma_k.py
python 08_mS0_background_scan.py
python 01_setor_escalar_K_Omega.py
python 06_mu_alpha_QS.py
```

Saídas oficiais das rodadas de 2026-08-06 em `code/out/`.
