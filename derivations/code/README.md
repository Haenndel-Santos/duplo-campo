# Scripts das Derivações — Guia de Execução

Todos os scripts são autocontidos (dependem apenas de `tdcp_pert_lib.py`
no mesmo diretório, mais `sympy`, `numpy`, `scipy`). Cada um imprime o
resultado no console **e** grava em `out/NN_output.txt` (matrizes
completas em `out/NN_matrices.txt` quando aplicável) — para retornar os
resultados, basta enviar os arquivos de `out/`.

## Ordem de execução

```
python tdcp_pert_lib.py            # 0. auto-testes da biblioteca (~5 s)
python 02_setor_tensorial_mT2.py   # Derivação 2 (~1 min)
python 07_bessel_sigma_k.py        # Derivação 7 (~1 min)
python 08_mS0_background_scan.py   # Derivação 8 (~2 min)
python 01_setor_escalar_K_Omega.py # Derivação 1 (pesado: 10–40 min)
python 06_mu_alpha_QS.py           # Derivação 6 (pesado: 10–40 min)
```

01, 02 e 07 são independentes entre si; 06 usa a mesma máquina do 01
(mas roda sozinho); 08 tem *plug-ins* no topo do arquivo (`CS_NORM`,
`MT2`, `ALPHA`, `OFFSET_DELTA`) que devem ser atualizados com os
resultados de 01/02/06 numa segunda rodada.

## Segunda rodada do 08 (após 01/02/06)

1. Substituir `CS_NORM`/fórmula de `m_S^2` pela expressão real derivada
   no 01 (se ela não for proporcional a β₁+2β₂r, editar a linha `mS2 =`
   em `run_background`).
2. `MT2` já vem com o resultado derivado no 02; conferir.
3. `ALPHA` — substituir pela forma derivada no 06.
4. Rodar com `OFFSET_DELTA = 0.0` (ramo exato) e depois com
   `OFFSET_DELTA = 0.02` (modo exploratório fora da raiz).

## O que cada script decide

| Script | Pergunta que responde | Claim sob teste |
|---|---|---|
| 01 | K_ij, Ω_ij explícitas do setor escalar; posto; no-ghost; m_S² | Cap.15 §15.4/§15.5, Cap.6.2 §6.4 vs Anexo C §C.3 |
| 02 | ação TT correta; estrutura (h−ℓ)²; m_T² com todos os fatores | Cap.16 §16.2/§16.4/§16.6 vs Anexo D §D.3/§D.5 |
| 06 | μ, η_slip, Σ exatos no QS; nº de polos; α(a) derivado | Cap.18 §18.3 (ansatz Yukawa), §18.4, §18.7; Cap.7 §7.6 |
| 07 | solução exata do modo σ_k; expoente super-horizonte | Cap.10 §10.3 (σ_k ~ k^{−3/2}) |
| 08 | m_S0 produzido pela dinâmica com hipóteses declaradas | Cap.19 §19.3 (m_S0 ~ 30–300 H₀) |

## Convenções

- Métricas: assinatura (−,+,+,+); gauge N_g=1; modos cos(kz)/sin(kz)
  com média espacial (fator global ½ — irrelevante para razões,
  autovalores e condições de sinal).
- EH na forma Γ–Γ (só primeiras derivadas; igual a √(−g)R a menos de
  derivada total — validada por assert contra o minisuperespaço do
  Anexo B §B.4.5).
- Fundo on-shell: aceleração-g, aceleração-f (Euler–Lagrange da F.1),
  Friedmann g/f, equação de χ. Atenção: o sinal da fonte na equação de
  χ derivado da ação é **−m²M_eff²F′V** (o Anexo E §E.3(3) declara +).
