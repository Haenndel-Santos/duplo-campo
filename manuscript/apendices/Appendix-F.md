Perfeito.

Agora entramos no Anexo F, que fecha o bloco técnico com algo fundamental para qualquer teoria que queira ser levada a sério:

Um mapa claro do espaço de parâmetros,

regiões consistentes,

regiões proibidas,

e como os diferentes constraints se cruzam.

Este anexo organiza tudo o que foi derivado nos anexos A--E em forma de "cartografia teórica".

**ANEXO F**

**Espaço de Parâmetros da TDCP**

**Regiões Permitidas, Regiões Excluídas e Mapa de Consistência**

**F.1 Por que mapear o espaço de parâmetros?**

A TDCP não é apenas um conjunto de equações.

Ela depende de parâmetros fundamentais:

- m --- escala de massa do setor bimétrico,

- \beta_0,\dots,\beta_4 --- coeficientes do potencial HR,

- M_g, M_f --- escalas de Planck dos setores,

- U(\chi) --- potencial estrutural,

- F(\chi) --- modulação dinâmica,

- \Gamma --- taxa de acumulação irreversível.

Sem um mapa claro:

- a teoria vira espaço infinito de possibilidades,

- qualquer comportamento pode ser "forçado".

Este anexo mostra que não é o caso.

Existem regiões matematicamente proibidas.

**F.2 Estrutura básica do espaço de parâmetros**

Separaremos os parâmetros em três blocos:

**F.2.1 Bloco Gravitacional Bimétrico**

$\{ m,\beta_0,\beta_1,\beta_2,\beta_3,\beta_4,M_g,M_f \}$

Estes controlam:

- massa efetiva do modo tensorial,

- estrutura da constraint de Bianchi,

- estabilidade escalar,

- limite GR.

**F.2.2 Bloco Estrutural (χ)**

$\{ U(\chi),F(\chi),\Gamma \}$

Estes controlam:

- ativação tardia,

- crescimento de η,

- dinâmica da aceleração.

**F.2.3 Bloco Inicial**

$\chi_i,\dot\chi_i,r_i,\eta_i.$

Controla trajetória cosmológica específica.

**F.3 Restrições Fundamentais (Hard Constraints)**

Agora listamos restrições que são estruturais, não observacionais.

**F.3.1 Positividade de F(χ)**

Para evitar inversão de sinal do termo de massa:

$\boxed{F(\chi) > 0}$

Se F<0:

- massa tensorial muda sinal,

- setor escalar pode virar ghost,

- estrutura do potencial é invertida.

Região proibida absoluta.

**F.3.2 Condição de Higuchi**

Em regime acelerado:

$\boxed{m_T^2(t) \ge 2H^2}$

Como:

$m_T^2 = m^2F(\chi)\mu_T^2(r,\beta_n),$

então:

$m^2F(\chi)\mu_T^2 \ge 2H^2.$

Isso define uma superfície no espaço:

$\mathcal{S}_{\text{Higuchi}}.$

Abaixo dessa superfície → região excluída.

**F.3.3 Ausência de Ghost Escalar**

Do Anexo C:

$K_{11}>0, \quad K_{22}>0, \quad \det K>0.$

Isso impõe desigualdades envolvendo:

- $\beta_n,$

- r,

- $m^2F(\chi).$

Essa condição é particularmente sensível a:

$\mathcal{B}(r)=\beta_1+2\beta_2 r+\beta_3 r^2.$

Se \mathcal{B}(r)=0, sistema degenera (ponto crítico).

**F.3.4 Estabilidade de Gradiente**

$c_{s,\pm}^2>0.$

Tipicamente impõe:

- m^2F(\chi) não muito pequeno,

- \beta_2 não dominante com sinal incorreto.

Região de instabilidade aparece quando:

$m^2F(\chi) \to 0 \quad\text{ou}\quad r \to 0,\infty.$

**F.4 Regiões Estruturalmente Seguras**

A região mais simples e robusta é:

- $M_f \sim M_g,$

- $r\sim \mathcal{O}(1),$

- $\beta_1,\beta_2,\beta_3>0,$

- $m \sim H_0,$

- F(\chi)\sim 1 no regime primordial,

- F'(\chi) pequeno.

Esta região:

- respeita Higuchi,

- evita ghost escalar,

- gera aceleração suave,

- mantém GR local.

**F.5 Regiões Perigosas**

**(1) m \ll H_0**

→ massa muito pequena

→ violação Higuchi

→ helicidade-0 fantasma

**(2) m \gg H_0**

→ ativa cedo demais

→ conflito com CMB

→ crescimento estrutural alterado

**(3) \mathcal{B}(r)=0**

→ ponto crítico do potencial

→ degeneração dinâmica

→ possível perda de grau físico

**(4) F(\chi)\to 0**

→ massa tensorial desaparece

→ mistura escalar instável

→ possível singularidade efetiva

**F.6 Relação com Observações**

Agora adicionamos restrições observacionais:

**F.6.1 Crescimento de Estrutura**

$f\sigma_8(z)$

depende de:

$G_{\text{eff}}(k,z)$

Se m^2F(\chi) for grande demais:

- crescimento suprimido demais.

Se pequeno demais:

- crescimento exagerado.

**F.6.2 CMB**

- η deve ser pequeno em z\sim1100,

- χ congelado no regime primordial.

Impõe:

$\chi_i \approx 0, \quad \dot\chi_i \approx 0.$

**F.6.3 Ondas gravitacionais**

LIGO/Virgo impõe:

$|c_T - 1| \ll 10^{-15}.$

Na TDCP, como o termo de massa é ultraleve (\sim H_0),

não afeta ondas de alta frequência → região segura.

**F.7 Representação Geométrica do Espaço de Parâmetros**

Podemos imaginar o espaço como um hiper-volume 8--10 dimensional.

As superfícies críticas são:

- Higuchi → hipersuperfície

- Ghost escalar → região excluída interna

- Instabilidade gradiente → região externa

- CMB → região inicial restrita

- Aceleração tardia → banda estreita m \sim H_0

O espaço permitido é a interseção:

$$ \mathcal{R}_{\text{permitida}} = \mathcal{R}_{\text{Higuchi}} \cap \mathcal{R}_{\text{no-ghost}} \cap \mathcal{R}_{\text{grad}} \cap \mathcal{R}_{\text{CMB}} \cap \mathcal{R}_{\text{late-accel}}. $$

**F.8 Insight Conceitual Importante**

Este anexo mostra algo crucial:

A TDCP não é arbitrária.

A combinação:

- Higuchi

- Ghost-free

- CMB

- Crescimento estrutural

comprime fortemente o espaço de parâmetros.

Isso é bom.

Teorias boas são restritas.

**F.9 Conclusão do Anexo F**

O espaço de parâmetros da TDCP:

- não é livre,

- não é arbitrário,

- possui fronteiras matemáticas claras,

- possui superfícies de exclusão física,

- possui uma região estreita natural onde:

  - aceleração emerge,

  - estabilidade é mantida,

  - GR local é recuperada,

  - observações são respeitadas.

Este anexo encerra o bloco técnico.

Agora restam:

- Anexo G --- Expansão Filosófica Profunda

- Anexo H --- Formalização Canônica e Consolidação Final da Estrutura

Minha sugestão:

Agora entramos no Anexo G, que será mais conceitual, mas ainda rigoroso --- conectando:

- separação estrutural,

- flecha do tempo,

- ontologia geométrica,

- comparação com Penrose, entropia gravitacional e irreversibilidade.

Quer seguir para o Anexo G?
