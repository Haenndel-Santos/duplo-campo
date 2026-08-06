# Registro de Fórmulas — Anexo H

Fonte: `manuscript/apendices/Appendix-H.md` — 17 equações em destaque.

Classes sugeridas por heurística textual — **confirmar na auditoria**. Preencher `Depende de` (IDs) e `Veredito` durante o passe sequencial.

---

### [AH.01]  (linha 43)

```
$g_{\mu\nu} = f_{\mu\nu}, \quad \chi = 0, \quad \eta = 0.$
```

- **Seção:** Postulado 1 --- Estrutura Primordial Simétrica
- **Contexto:** …**Postulado 1 --- Estrutura Primordial Simétrica** / Existe um estado primordial estruturalmente simétrico caracterizado por:
- **Segue:** Esse estado é instável sob perturbações estruturais.
- **Classe (sugerida):** postulado
- **Depende de:** Cap.1
- **Veredito:** CONFERE (postulado razoável — estado primordial simétrico como condição inicial, consistente com a narrativa de bifurcação do Cap.1)

### [AH.02]  (linha 51)

```
$r = \frac{b}{a} \neq 1.$
```

- **Seção:** Postulado 2 --- Bifurcação Estrutural
- **Contexto:** …**Postulado 2 --- Bifurcação Estrutural** / A instabilidade do modo antissimétrico gera separação estrutural entre dois setores geométricos:
- **Segue:** A bifurcação é interpretada como transição crítica.
- **Classe (sugerida):** postulado
- **Depende de:** —
- **Veredito:** CONFERE (postulado — consequência da instabilidade declarada, consistente com r=b/a já definido)

### [AH.03]  (linha 59)

```
$$ V(\mathcal{K}) = \sum_{n=0}^4 \beta_n e_n(\mathcal{K}), \quad \mathcal{K}=\sqrt{g^{-1}f}. $$
```

- **Seção:** Postulado 3 --- Dinâmica Bimétrica Ghost-Free
- **Contexto:** …**Postulado 3 --- Dinâmica Bimétrica Ghost-Free** / A interação entre as métricas é descrita por:
- **Segue:** A estrutura em e_n garante ausência do ghost de Boulware--Deser.
- **Classe (sugerida):** postulado
- **Depende de:** Anexo A §A.1
- **Veredito:** CONFERE (reprise da estrutura HR padrão)

### [AH.04]  (linha 67)

```
$V \rightarrow F(\chi)V.$
```

- **Seção:** Postulado 4 --- Modulação Estrutural Dinâmica
- **Contexto:** …**Postulado 4 --- Modulação Estrutural Dinâmica** / O potencial é modulado por uma função escalar suave:
- **Segue:** O campo \chi evolui segundo:
- **Classe (sugerida):** postulado
- **Depende de:** Cap.3 §3.8
- **Veredito:** CONFERE (reprise da modulação TDCP)

### [AH.05]  (linha 71)

```
$\ddot\chi + 3H\dot\chi + U'(\chi) = m^2M_{eff}^2 F'(\chi)V.$
```

- **Seção:** Postulado 4 --- Modulação Estrutural Dinâmica
- **Contexto:** …[equação anterior] / O campo \chi evolui segundo:
- **Segue:** **Postulado 5 --- Irreversibilidade Estrutural**
- **Classe (sugerida):** pendente
- **Depende de:** âncoras D2/D8 (erratum de sinal na equação de χ)
- **Veredito:** ERRO DE CÁLCULO (mesmo erro de sinal já identificado em Anexo E §E.3(3)/AE.09/11 — âncoras D2/D8: deveria ser −m²M_eff²F'(χ)V; aqui elevado a "Postulado 4" da formalização canônica, o que amplifica a necessidade de correção)

### [AH.06]  (linha 77)

```
$\dot\eta = \Gamma \dot\chi^2, \quad \Gamma>0.$
```

- **Seção:** Postulado 5 --- Irreversibilidade Estrutural
- **Contexto:** …**Postulado 5 --- Irreversibilidade Estrutural** / Existe uma variável acumulativa:
- **Segue:** Logo:
- **Classe (sugerida):** postulado
- **Depende de:** achado A2 (lote 1: duas leis incompatíveis para η)
- **Veredito:** CONFERE (postulado internamente coerente, com Γ>0 declarado explicitamente aqui pela primeira vez) ; CONFLITA COM Cap.1 §1.6/Cap.2 §2.7 (achado A2/lote 1) — esta é literalmente a citação "Anexo H Postulado 5" que o achado A2 menciona pelo nome como a segunda lei incompatível de η; elevada a postulado formal aqui, a incompatibilidade precisa de resolução editorial antes que a "formalização canônica" possa ser considerada fechada

### [AH.07]  (linha 81)

```
$\eta(t) \text{ é monotônica crescente.}$
```

- **Seção:** Postulado 5 --- Irreversibilidade Estrutural
- **Contexto:** …[equação anterior] / Logo:
- **Segue:** **Postulado 6 --- Recuperação de GR**
- **Classe (sugerida):** derivada-no-texto
- **Depende de:** AH.06
- **Veredito:** CONFERE (consequência lógica correta de AH.06, dado Γ>0; flag sem-delimitador — a extração capturou uma frase, não uma fórmula)

### [AH.08]  (linha 87)

```
$\chi \to 0, \quad \eta \to 0, \quad r \to 1,$
```

- **Seção:** Postulado 6 --- Recuperação de GR
- **Contexto:** …**Postulado 6 --- Recuperação de GR** / No limite:
- **Segue:** a teoria recupera GR padrão.
- **Classe (sugerida):** postulado
- **Depende de:** —
- **Veredito:** CONFERE (postulado razoável de recuperação de GR)

### [AH.09]  (linha 97)

```
$$ 3M_g^2 H^2 = \rho_m + \frac12\dot\chi^2 + U(\chi) + m^2M_{eff}^2F(\chi)\mathcal{V}(r). $$
```

- **Seção:** (1) Friedmann visível
- **Contexto:** …A TDCP é completamente definida pelas seguintes equações: / **(1) Friedmann visível**
- **Segue:** **(2) Friedmann estrutural**
- **Classe (sugerida):** pendente
- **Depende de:** Anexo E §E.3 (AE.04-06); âncora D3 (derivations/03_dV_dNg_regra_cadeia.md)
- **Veredito:** CONFERE (consolidação correta — usa 𝒱(r) sem ξ, consistente com a forma corrigida da âncora D3/AA.30/AE.06)

### [AH.10]  (linha 101)

```
$3M_f^2 H_f^2 = m^2M_{eff}^2F(\chi)\mathcal{U}(r).$
```

- **Seção:** (2) Friedmann estrutural
- **Contexto:** …[equação anterior] / **(2) Friedmann estrutural**
- **Segue:** **(3) Constraint de Bianchi**
- **Classe (sugerida):** pendente
- **Depende de:** Anexo E §E.8 (AE.46-48)
- **Veredito:** CONFERE (consolidação correta, consistente com AE.46-48/AB.50)

### [AH.11]  (linha 105)

```
$(\beta_1 + 2\beta_2 r + \beta_3 r^2)(H - \xi H_f)=0.$
```

- **Seção:** (3) Constraint de Bianchi
- **Contexto:** …[equação anterior] / **(3) Constraint de Bianchi**
- **Segue:** **(4) Equação de χ**
- **Classe (sugerida):** pendente
- **Depende de:** Anexo B §B.8
- **Veredito:** CONFERE (reprise da constraint de Bianchi)

### [AH.12]  (linha 109)

```
$$ \ddot\chi + 3H\dot\chi + U'(\chi) = m^2M_{eff}^2F'(\chi)V(\xi,r). $$
```

- **Seção:** (4) Equação de χ
- **Contexto:** …[equação anterior] / **(4) Equação de χ**
- **Segue:** **(5) Irreversibilidade**
- **Classe (sugerida):** pendente
- **Depende de:** âncoras D2/D8 (erratum de sinal na equação de χ)
- **Veredito:** ERRO DE CÁLCULO (repete o erro de sinal de AH.05/AE.09/11 — âncoras D2/D8)

### [AH.13]  (linha 113)

```
$\dot\eta = \Gamma \dot\chi^2.$
```

- **Seção:** (5) Irreversibilidade
- **Contexto:** …[equação anterior] / **(5) Irreversibilidade**
- **Segue:** **(6) Massa tensorial efetiva**
- **Classe (sugerida):** pendente
- **Depende de:** AH.06; achado A2 (lote 1: duas leis incompatíveis para η)
- **Veredito:** CONFERE (reprise de AH.06) ; CONFLITA COM Cap.1 §1.6/Cap.2 §2.7 — achado A2/lote 1

### [AH.14]  (linha 117)

```
$m_T^2(t) = m^2F(\chi)\mu_T^2(r,\beta_n,M_g,M_f).$
```

- **Seção:** (6) Massa tensorial efetiva
- **Contexto:** …[equação anterior] / **(6) Massa tensorial efetiva**
- **Segue:** **(7) Higuchi**
- **Classe (sugerida):** pendente
- **Depende de:** âncora D2 (derivations/02_setor_tensorial_mT2.md)
- **Veredito:** INCOMPLETA (mesma omissão de ξ de AF.06/Anexo F §F.3.2 — μ_T² deveria depender de ξ também, per a âncora D2/Anexo D §D.4/AD.09)

### [AH.15]  (linha 121)

```
$m_T^2 \ge 2H^2.$
```

- **Seção:** (7) Higuchi
- **Contexto:** …[equação anterior] / **(7) Higuchi**
- **Segue:** **H.4 Estrutura Conceitual Compacta**
- **Classe (sugerida):** condicao/vinculo
- **Depende de:** AH.14
- **Veredito:** CONFERE (reprise do bound de Higuchi)

### [AH.16]  (linha 161)

```
$$ \boxed{ H^2 = \frac{8\pi G}{3} \frac{\rho_m + \rho_\chi + \rho_{int}} {1-\eta} } $$
```

- **Seção:** H.6 Forma Compacta Final da Teoria
- **Contexto:** …**H.6 Forma Compacta Final da Teoria** / Podemos escrever a essência da TDCP como:
- **Segue:** com:
- **Classe (sugerida):** pendente
- **Depende de:** Anexo E §E.7 (AE.39); âncora D4 (derivations/04_friedmann_eta_acao.md)
- **Veredito:** NÃO-DERIVÁVEL — âncora D4, mesma pendência de AE.39/AG.05, aqui elevada a "forma compacta final da teoria" (H.6) — a formulação mais proeminente desta equação em todo o corpus; precisa ser reclassificada como extensão proposta (acoplamento não-mínimo Ω(η)R_g + constraint), válida no regime adiabático |η̇|≪H, antes de servir como resumo canônico da TDCP

### [AH.17]  (linha 165)

```
$$ \rho_{int} = m^2M_{eff}^2F(\chi)\mathcal{V}(r), \quad \dot\eta=\Gamma\dot\chi^2. $$
```

- **Seção:** H.6 Forma Compacta Final da Teoria
- **Contexto:** …[equação anterior] / com:
- **Segue:** Essa equação resume:
- **Classe (sugerida):** pendente
- **Depende de:** AH.09; achado A2 (lote 1: duas leis incompatíveis para η)
- **Veredito:** CONFERE (ρ_int=m²M_eff²F(χ)𝒱(r) consistente com a forma corrigida da âncora D3) ; CONFLITA COM Cap.1 §1.6/Cap.2 §2.7 (η̇=Γχ̇² — achado A2/lote 1, mesma nota de AH.06/13)

