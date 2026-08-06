# Registro de Fórmulas — Anexo J

Fonte: `manuscript/apendices/Appendix-J.md` — 11 equações em destaque.

Classes sugeridas por heurística textual — **confirmar na auditoria**. Preencher `Depende de` (IDs) e `Veredito` durante o passe sequencial.

---

### [AJ.01]  (linha 33)

```
$$g_{\mu\nu}^{(1)} \quad \text{e} \quad g_{\mu\nu}^{(2)}$$
```

- **Seção:** J.1 Introdução
- **Contexto:** …primordial do espaço-tempo. / Após o colapso quântico inicial, duas métricas independentes emergem:
- **Segue:** Essas duas geometrias evoluem como universos distintos, mas permanecem
- **Classe (sugerida):** pendente
- **Depende de:** Anexo I (AI.05/06)
- **Veredito:** CONFERE (reprise da notação de AI.05/06)

### [AJ.02]  (linha 62)

```
$$\mid \Psi\rangle = \sum_{i} c_{i} \mid g_{1}^{(i)}\rangle \otimes \mid g_{2}^{(i)}\rangle$$
```

- **Seção:** J.2 Emaranhamento Cosmológico Primordial
- **Contexto:** …não são completamente independentes. / O estado quântico global pode ser descrito como um estado emaranhado:
- **Segue:** onde:
- **Classe (sugerida):** pendente
- **Depende de:** `integration_assessment.md` (Pergunta 1: g^(1)/g^(2) vs g/f)
- **Veredito:** CONFERE SOB HIPÓTESE (forma padrão de estado emaranhado bipartido em QM — bem formada como objeto formal; mesma pendência do Apêndice I sobre a ponte com a ação clássica, nunca demonstrada, per `integration_assessment.md` (Pergunta 1: g^(1)/g^(2) vs g/f))

### [AJ.03]  (linha 76)

```
$$S_{ent} = - Tr(\rho\ln\rho)$$
```

- **Seção:** J.2 Emaranhamento Cosmológico Primordial
- **Contexto:** …Esse fenômeno pode ser descrito por uma **entropia de emaranhamento / cosmológico**:
- **Segue:** onde $\rho$ é a matriz densidade reduzida de um dos universos.
- **Classe (sugerida):** pendente
- **Depende de:** —
- **Veredito:** CONFERE (importada — entropia de von Neumann padrão, fórmula correta)

### [AJ.04]  (linha 87)

```
$$E_{tot} = E_{1} + E_{2} + E_{int}$$
```

- **Seção:** J.3 Energia de Vácuo e Acoplamento Entre Universos
- **Contexto:** …de um termo de interação. / A energia total do sistema pode ser escrita como:
- **Segue:** onde:
- **Classe (sugerida):** afirmada-sem-derivacao
- **Depende de:** Anexo I (AI.09); Cap.3 §3.4
- **Veredito:** CONFLITA COM Cap.3 §3.4 — mesma nota de AI.09/`integration_assessment.md` (Pergunta 1: g^(1)/g^(2) vs g/f) (tratamento simétrico de energia em ambos os domínios)

### [AJ.05]  (linha 99)

```
$$L_{int} = \lambda\chi\left( g_{\mu\nu}^{(1)}-g_{\mu\nu}^{(2)} \right)^{2}$$
```

- **Seção:** J.3 Energia de Vácuo e Acoplamento Entre Universos
- **Contexto:** …- $E_{int}$ é a energia de acoplamento. / Esse termo de interação pode assumir uma forma efetiva como:
- **Segue:** onde:
- **Classe (sugerida):** pendente
- **Depende de:** `integration_assessment.md` (Pergunta 2: L_int vs V(K))
- **Veredito:** NÃO-DERIVÁVEL — per `integration_assessment.md` (Pergunta 2: L_int vs V(K)): a contração de índices de "²" não é especificada; na leitura mais natural (sem estrutura de traço explícita), o termo é ∝h_μνh^μν SEM a subtração −(h^μ_μ)² exigida pela combinação de Fierz-Pauli, a ÚNICA combinação quadrática que evita o sexto grau de liberdade fantasma no setor linear (Fierz-Pauli 1939/Hassan-Rosen 2011); se a contração for genérica, o termo reintroduz o fantasma de Boulware-Deser que a construção HR dos Cap.2-6 foi desenhada para eliminar — reconciliável com V(K)=Σβnen(K) apenas sob uma tunagem que o texto não verifica

### [AJ.06]  (linha 112)

```
$$\Lambda$$
```

- **Seção:** J.4 Origem da Energia Escura na TDCP
- **Contexto:** …Na cosmologia padrão, a energia escura é introduzida como uma constante / cosmológica:
- **Segue:** Na TDCP, propõe-se uma origem diferente.
- **Classe (sugerida):** importada-da-literatura
- **Depende de:** —
- **Veredito:** CONFERE (notação padrão — constante cosmológica do modelo ΛCDM, citada para contraste)

### [AJ.07]  (linha 121)

```
$$\Lambda_{eff} = \Lambda_{0} + \Lambda_{ent}$$
```

- **Seção:** J.4 Origem da Energia Escura na TDCP
- **Contexto:** …acoplamento entre os dois domínios cosmológicos**. / O termo de constante cosmológica efetiva seria então:
- **Segue:** onde:
- **Classe (sugerida):** derivada-no-texto
- **Depende de:** `integration_assessment.md` (Pergunta 3: Λ_ent vs η)
- **Veredito:** CONFLITA COM Anexo E/H (η) — per `integration_assessment.md` (Pergunta 3: Λ_ent vs η): Λ_eff é aditivo e Λ_ent não tem equação de movimento explícita ("pode variar lentamente no tempo" é qualitativo), ao contrário de η (η̇=Γχ̇², Anexo E/H), que é multiplicativo (fator 1/(1−η) sobre ρ_tot) e tem equação de movimento bem definida; Λ_ent, tal como escrita, é uma afirmação qualitativa sem conteúdo dinâmico verificável

### [AJ.08]  (linha 139)

```
$$\square h_{\mu\nu}^{(1)} + m_{g}^{2}h_{\mu\nu}^{(1)} = \kappa h_{\mu\nu}^{(2)}$$
```

- **Seção:** J.5 Ondas Gravitacionais Entre Domínios
- **Contexto:** …em um domínio podem gerar efeitos no outro. / A equação de propagação para ondas gravitacionais pode ser escrita como:
- **Segue:** onde:
- **Classe (sugerida):** afirmada-sem-derivacao
- **Depende de:** Anexo D (âncora D2)
- **Veredito:** NÃO-DERIVÁVEL (forma assumida por analogia, sem derivação a partir de uma ação; estruturalmente parecida com o setor tensorial bimétrico real, onde a âncora D2 mostra que o termo de massa/mistura deve ter uma forma muito específica — proporcional a (h-ℓ)² — para evitar patologias; aqui κ é introduzido livremente, sem verificação de que a estrutura evita fantasma/gradiente, mesmo padrão de risco já identificado para L_int)

### [AJ.09]  (linha 185)

```
$$\ddot{\delta} + 2H\dot{\delta} = 4\pi G_{eff}\rho\delta$$
```

- **Seção:** J.7 Crescimento de Estruturas em Larga Escala
- **Contexto:** …gravitacionais se formam. / A equação de crescimento da densidade pode adquirir uma correção:
- **Segue:** onde:
- **Classe (sugerida):** pendente
- **Depende de:** Cap.8/Cap.18 (lotes 2/4)
- **Veredito:** CONFERE (mesma forma padrão já confirmada no Cap.8/Cap.18 — lotes 2/4 — com G_eff no lugar de Gμ)

### [AJ.10]  (linha 189)

```
$$G_{eff} = G(1 + \epsilon)$$
```

- **Seção:** J.7 Crescimento de Estruturas em Larga Escala
- **Contexto:** …[equação anterior] / onde:
- **Segue:** e $\epsilon$ depende da intensidade do acoplamento entre os dois
- **Classe (sugerida):** pendente
- **Depende de:** âncora D6
- **Veredito:** NÃO-DERIVÁVEL (ε é um parâmetro livre não conectado à estrutura μ(k,a) real derivada para o corpo F1 — âncora D6: μ real é multi-polo e depende de escala k, não uma constante (1+ε); mesmo padrão apontado em `integration_assessment.md` (Pergunta 4: parâmetros paralelos): "dois conjuntos de observáveis paralelos, não uma previsão unificada")

### [AJ.11]  (linha 210)

```
$$w(z) \neq - 1$$
```

- **Seção:** 1. Variação temporal suave da energia escura
- **Contexto:** …**1. Variação temporal suave da energia escura** / Equação de estado:
- **Segue:** **2. Modos adicionais de ondas gravitacionais**
- **Classe (sugerida):** pendente
- **Depende de:** —
- **Veredito:** CONFERE (previsão qualitativa genérica — comum a qualquer modelo de energia escura dinâmica, não específica desta construção)

