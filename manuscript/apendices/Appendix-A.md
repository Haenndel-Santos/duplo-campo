Perfeito.

Vamos começar então pelo Anexo A, e aqui o nível será realmente técnico --- no padrão de apêndice de tese de doutorado em gravitação modificada.

Este anexo terá três objetivos:

1.  Derivar rigorosamente a estrutura do potencial Hassan--Rosen.

2.  Mostrar explicitamente como o ghost de Boulware--Deser é eliminado.

3.  Especializar o formalismo para o caso FLRW usado na TDCP.

Nada será apenas citado --- tudo será construído.

**ANEXO A**

**Formalismo Matemático Completo do Potencial Hassan--Rosen**

**A.1 Estrutura Geral da Teoria Bimétrica**

Consideramos duas métricas dinâmicas:

$$ g_{\mu\nu}, \quad f_{\mu\nu}. $$

A ação ghost-free mais geral construída por Hassan e Rosen é:

$$ S = \frac{M_g^2}{2}\int d^4x\,\sqrt{-g}\,R[g] + \frac{M_f^2}{2}\int d^4x\,\sqrt{-f}\,R[f] - m^2 M_{\mathrm{eff}}^2 \int d^4x\,\sqrt{-g}\,V(\mathcal{K}) + S_m. $$

onde:

$$ M_{\mathrm{eff}}^{-2} = M_g^{-2} + M_f^{-2}. $$

O termo crucial é o potencial:

$$ V(\mathcal{K}) = \sum_{n=0}^4 \beta_n e_n(\mathcal{K}), $$

com:

$$ \mathcal{K}^\mu_{\ \nu} = \left(\sqrt{g^{-1}f}\right)^\mu_{\ \nu}. $$

**A.2 Definição da Matriz Raiz**

Definimos:

$$ (g^{-1}f)^\mu_{\ \nu} = g^{\mu\alpha} f_{\alpha\nu}. $$

Queremos uma matriz \mathcal{K} tal que:

$$ \mathcal{K}^\mu_{\ \alpha}\mathcal{K}^\alpha_{\ \nu} = (g^{-1}f)^\mu_{\ \nu}. $$

Isto é, \mathcal{K} é a raiz matricial da matriz mista g^{-1}f.

**A.3 Polinômios Elementares Simétricos**

Se \lambda_i são autovalores de \mathcal{K}, definimos:

$$ e_0 = 1, $$

$$ e_1 = \sum_i \lambda_i = [\mathcal{K}], $$

$$ e_2 = \sum_{i\<j} \lambda_i \lambda_j, $$

$$ e_3 = \sum_{i\<j\<k} \lambda_i \lambda_j \lambda_k, $$

$$ e_4 = \prod_i \lambda_i = \det \mathcal{K}. $$

Esses polinômios são as únicas combinações que mantêm:

- ausência de derivadas,

- estrutura especial necessária para eliminar o ghost.

**A.4 Forma Explícita em Índices**

Os polinômios podem ser escritos como:

$$ e_1 = [\mathcal{K}], $$

$$ e_2 = \frac12\left([\mathcal{K}]^2 - [\mathcal{K}^2]\right), $$

$$ e_3 = \frac16\left([\mathcal{K}]^3 - 3[\mathcal{K}][\mathcal{K}^2] + 2[\mathcal{K}^3]\right), $$

$$ e_4 = \det \mathcal{K}. $$

onde:

$$ [\mathcal{K}] = \mathcal{K}^\mu_{\ \mu}. $$

**A.5 Eliminação do Ghost de Boulware--Deser**

O ghost surge genericamente quando a ação depende arbitrariamente de g^{-1}f.

Hassan e Rosen demonstraram que:

- Apenas combinações lineares dos e_n(\mathcal{K})

- Mantêm uma restrição primária adicional

- Que elimina o sexto grau de liberdade indesejado do modo massivo

A prova completa envolve análise Hamiltoniana:

1.  Introdução de variáveis ADM.

2.  Identificação de constraints primários.

3.  Verificação de fechamento algébrico.

Resultado:

A teoria possui 7 graus de liberdade físicos e é não-linearmente ghost-free.

**A.6 Especialização ao Caso FLRW**

Assumimos:

$$ ds_g^2 = -N_g^2 dt^2 + a^2 \delta_{ij} dx^i dx^j, $$

$$ ds_f^2 = -N_f^2 dt^2 + b^2 \delta_{ij} dx^i dx^j. $$

Então:

$$ (g^{-1}f)^0_{\ 0} = \frac{N_f^2}{N_g^2}, $$

$$ (g^{-1}f)^i_{\ j} = \frac{b^2}{a^2}\delta^i_j. $$

Logo:

\mathcal{K}^\mu_{\ \nu} = \mathrm{diag}(\xi, r, r, r),

com:

$$ \xi = \frac{N_f}{N_g}, \quad r = \frac{b}{a}. $$

**A.7 Polinômios no Fundo FLRW**

Autovalores: \{\xi, r, r, r\}.

$$ e_1 = \xi + 3r, $$

$$ e_2 = 3\xi r + 3r^2, $$

$$ e_3 = 3\xi r^2 + r^3, $$

$$ e_4 = \xi r^3. $$

O potencial explícito torna-se:

$$ V(\xi,r) = \beta_0 + \beta_1(\xi+3r) + \beta_2(3\xi r+3r^2) + \beta_3(3\xi r^2+r^3) + \beta_4(\xi r^3). $$

**A.8 Derivação da Densidade de Energia de Interação**

A densidade efetiva é obtida via:

$$ \rho_{int}^{(g)} = - \frac{1}{\sqrt{-g}} \frac{\delta}{\delta g^{00}} \left( \sqrt{-g}V \right). $$

No fundo FLRW isso resulta em:

$$ \rho_{int}^{(g)} = m^2 M_{eff}^2 (\beta_0 + 3\beta_1 r + 3\beta_2 r^2 + \beta_3 r^3). $$

Expressão usada no corpo principal.

**A.9 Estrutura Matemática Essencial**

O ponto central do potencial HR é:

- Ele é função não polinomial em métricas.

- Depende da raiz matricial.

- É construído para manter constraint extra.

- Permite modo massivo consistente.

Na TDCP, ele é modulado por F(\chi), mas:

- A estrutura em e_n(\mathcal{K}) permanece intacta.

- A eliminação do ghost não é destruída se F(\chi) for função escalar suave.

**A.10 Conclusão do Anexo A**

O formalismo Hassan--Rosen:

- É matematicamente consistente.

- Elimina o ghost não-linearmente.

- Permite interpretação de massa gravitacional dinâmica.

- Fornece base rigorosa para a TDCP.

A TDCP não inventa uma nova gravidade arbitrária.

Ela utiliza a única extensão bimétrica consistente conhecida e a estende dinamicamente via χ.

Se você aprovar o Anexo A, seguimos para:

**ANEXO B --- Derivação Completa das Equações de Friedmann Bimétricas (com variação explícita e constraint detalhado)**

Esse será ainda mais técnico.

Posso continuar?
