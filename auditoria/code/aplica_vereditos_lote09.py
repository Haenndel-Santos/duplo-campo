# -*- coding: utf-8 -*-
"""
aplica_vereditos_lote09.py — vereditos do Lote 9 (Anexo E / AE, 57 eqs).
Casamento por substring; multi=True aplica a todas as ocorrencias
pendentes DENTRO DO MESMO ARQUIVO.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
REG = os.path.normpath(os.path.join(HERE, '..', 'registro'))

D1 = "âncora D1 (derivations/01_setor_escalar_K_Omega.md)"
D2 = "âncora D2 (derivations/02_setor_tensorial_mT2.md)"
D3 = "âncora D3 (derivations/03_dV_dNg_regra_cadeia.md)"
D4 = "âncora D4 (derivations/04_friedmann_eta_acao.md)"
D5 = "âncora D5 (derivations/05_rdot_ramo_dinamico.md)"
A2 = "achado A2 (lote 1: duas leis incompatíveis para η)"

V = [
 ("AE", r"r(t)=\frac{b(t)}{a(t)}, \qquad \xi(t)=\frac{N_f(t)}{N_g(t)}.", "Anexo A/B (AA.23/AB.07)",
  "CONFERE (reprise)", False),
 ("AE", r"N_g=1.", "Anexo B §B.2",
  "CONFERE (escolha de gauge padrão, consistente com Anexo B §B.2/E.2)", False),
 ("AE", r"H \equiv \frac{\dot a}{a}, \qquad H_f = \frac{1}{N_f}\frac{\dot b}{b} = \frac{1}{\xi}\frac{\dot b}{b}.",
  "Anexo B §B.2 (AB.06)", "CONFERE (consistente com AB.06, especializado a N_g=1, logo H=H_g)", False),
 ("AE", r"3M_g^2 H^2 = \rho_m + \rho_\chi + \rho_{int}^{(g)}.", "Anexo B §B.5 (AB.35)",
  "CONFERE (reprise de AB.35, com H=H_g pois N_g=1)", False),
 ("AE", r"\rho_\chi = \frac12\dot\chi^2 + U(\chi),", "Anexo B §B.5 (AB.36)",
  "CONFERE (reprise de AB.36 — densidade padrão de Klein-Gordon)", False),
 ("AE", r"\rho_{int}^{(g)} = m^2M_{eff}^2 F(\chi) \left(\beta_0 + 3\beta_1 r + 3\beta_2 r^2 + \beta_3 r^3\right).",
  f"Anexo A §A.8 (AA.30); {D3}",
  "CONFERE — âncora D3: forma correta (sem ξ, sem β4), idêntica ao Anexo A §A.8/AA.30 e à correção da âncora D3 para o Anexo B §B.5 (AB.36) — esta é a forma que o corpo principal de fato usa", False),
 ("AE", r"3M_f^2 H_f^2 = \rho_{int}^{(f)},", "Anexo B §B.11 (AB.70)",
  "CONFERE (reprise de AB.70)", False),
 ("AE", r"\rho_{int}^{(f)} = m^2M_{eff}^2 F(\chi) \left(\beta_4 + 3\beta_3 r^{-1} + 3\beta_2 r^{-2} + \beta_1 r^{-3}\right).",
  "Anexo B §B.6 (AB.50)",
  "CONFERE (reprise exata de AB.50, já verificada por álgebra explícita no lote 7)", False),
 ("AE", r"\ddot\chi + 3H\dot\chi + U'(\chi) = m^2 M_{eff}^2 F'(\chi)\,W(r,\xi),",
  "âncora D2/D8 (erratum de sinal)",
  "ERRO DE CÁLCULO (sinal da fonte trocado) — verificado por Euler-Lagrange nesta auditoria: variando a ação (termo -m²M_eff²√-g F(χ)V(K)) em relação a χ, e usando a convenção padrão do EOM livre de KG (χ̈+3Hχ̇+U'=0), obtém-se χ̈+3Hχ̇+U'(χ)=-m²M_eff²F'(χ)V(K) — sinal NEGATIVO, não positivo como escrito; mesmo erratum já documentado nas âncoras D2/D8 (\"a ação dá −m²M_eff²F′V\")", False),
 ("AE", r"W(r,\xi) = V(\xi,r)", "AE.09",
  "CONFERE (a identificação W=V(ξ,r) é a estrutura correta — a única dependência em χ do termo de interação é via F(χ), então a fonte é proporcional a F'(χ)V(K); o problema não está aqui, mas no sinal geral já presente em AE.09)", False),
 ("AE", r"\ddot\chi + 3H\dot\chi + U'(\chi) = m^2 M_{eff}^2 F'(\chi)\,V(\xi,r).",
  "AE.09/10; âncora D2/D8",
  "ERRO DE CÁLCULO (mesmo erro de sinal de AE.09, agora com W especializado — deveria ser χ̈+3Hχ̇+U'(χ)=−m²M_eff²F'(χ)V(ξ,r); erratum documentado nas âncoras D2/D8)", True),
 ("AE", r"\dot\eta = \Gamma \dot\chi^2.", f"Cap.1 §1.6/Cap.2 §2.7; {A2}",
  "CONFERE (forma internamente razoável, dimensionalmente coerente como definição isolada) ; CONFLITA COM Cap.1 §1.6/Cap.2 §2.7 — duas leis incompatíveis para η̇ no mesmo corpus (achado A2/lote 1): lá η̇=Γ(H1-H2)² com [Γ]=tempo, aqui η̇=Γχ̇² com Γ de dimensão diferente; nenhuma das duas declara a dimensão de Γ", False),
 ("AE", r"\dot\rho_m + 3H\rho_m = 0 \quad\Rightarrow\quad \rho_m = \rho_{m0} a^{-3}.", "—",
  "CONFERE (conservação padrão de matéria fria, importada)", False),
 ("AE", r"(\beta_1 + 2\beta_2 r + \beta_3 r^2)(H - \xi H_f)=0.", "Anexo B §B.8 (AB.54/56/71)",
  "CONFERE (reprise da constraint de Bianchi, Anexo B §B.8)", False),
 ("AE", r"H = \xi H_f.", f"{D1}, {D5}",
  "CONFLITA COM âncoras D1, D5 — esta é a \"escolha TDCP principal\" (ramo dinâmico) citada nominalmente pelas duas derivações como o ramo duplamente inviável: D5 mostra ṙ≡0 exatamente nesse ramo (ver AE.50/51 abaixo — não produz r(t) genuíno), e D1 encontra um par fantasma/taquiônico genuíno nesse mesmo ramo em todos os benchmarks testados. A equação em si (um dos dois ramos logicamente possíveis de AE.14) está correta; o problema é apresentá-la como \"escolha principal\" sem mencionar essas duas patologias já derivadas", False),
 ("AE", r"H = \xi H_f \quad\Rightarrow\quad H_f = \frac{H}{\xi}.", f"AE.15; {D1}, {D5}",
  "CONFERE (rearranjo direto de AE.15 — mesma nota sobre o ramo dinâmico, âncoras D1/D5)", False),
 ("AE", r"N\equiv \ln a, \qquad \frac{d}{dt} = H\frac{d}{dN}.", "—",
  "CONFERE (definição padrão de variável temporal N=ln a)", False),
 ("AE", r"x \equiv \frac{\dot\chi}{\sqrt{6}M_g H}, \qquad y \equiv \frac{\sqrt{U(\chi)}}{\sqrt{3}M_g H}, \qquad \Omega_m \equiv \frac{\rho_m}{3M_g^2 H^2}.",
  "—",
  "CONFERE (importada — variáveis adimensionais padrão da literatura de sistemas dinâmicos de quintessência, ex. Copeland-Sahni-Tsujikawa)", False),
 ("AE", r"\Omega_{int} \equiv \frac{\rho_{int}^{(g)}}{3M_g^2 H^2}.", "AE.18",
  "CONFERE (definição análoga a AE.18, para o setor de interação)", False),
 ("AE", r"1 = \Omega_m + x^2 + y^2 + \Omega_{int}.", "AE.04, AE.18, AE.19",
  "CONFERE (álgebra verificada: dividindo AE.04 por 3M_g²H² e usando χ̇=√6M_gHx, U=3M_g²H²y² das definições de AE.18, obtém-se exatamente esta forma)", False),
 ("AE", r"\frac{d\chi}{dN} = \frac{\dot\chi}{H} = \sqrt{6}M_g x.", "AE.18",
  "CONFERE (álgebra verificada: rearranjo direto de AE.18)", False),
 ("AE", r"\ddot\chi + 3H\dot\chi + U'(\chi) = m^2 M_{eff}^2 F'(\chi)V(\xi,r).",
  "AE.11; âncora D2/D8",
  "ERRO DE CÁLCULO (repete o erro de sinal de AE.11 — deveria ser −m²M_eff²F'(χ)V(ξ,r); erratum documentado nas âncoras D2/D8)", False),
 ("AE", r"\dot\chi = \sqrt{6}M_g H x,", "AE.21",
  "CONFERE (mesma relação de AE.21, forma direta)", False),
 ("AE", r"\ddot\chi = \sqrt{6}M_g\left(\dot H x + H\dot x\right) = \sqrt{6}M_g H^2\left(\frac{d x}{dN} + x\frac{d\ln H}{dN}\right).",
  "AE.23",
  "CONFERE (álgebra verificada: regra do produto em AE.23 + conversão para derivadas em N via Ḣ=H²dlnH/dN e ẋ=Hdx/dN)", False),
 ("AE", r"\sqrt{6}M_g H^2\left(\frac{dx}{dN}+x\frac{d\ln H}{dN}\right) + 3H(\sqrt{6}M_g H x) + U'(\chi) = m^2 M_{eff}^2 F'(\chi)V.",
  "AE.22, AE.24; âncora D2/D8",
  "ERRO DE CÁLCULO (herda o erro de sinal de AE.22 — o lado direito deveria ter sinal negativo)", False),
 ("AE", r"\frac{dx}{dN}+x\frac{d\ln H}{dN}+3x + \frac{U'(\chi)}{\sqrt{6}M_g H^2} = \frac{m^2 M_{eff}^2}{\sqrt{6}M_g H^2}F'(\chi)V.",
  "AE.25; âncora D2/D8",
  "ERRO DE CÁLCULO (divisão de AE.25 por √6M_gH² algebricamente correta, mas herda o erro de sinal)", False),
 ("AE", r"\lambda(\chi) \equiv M_g\frac{U'(\chi)}{U(\chi)}, \qquad \Rightarrow \frac{U'}{H^2} = 3M_g^2 \lambda y^2.",
  "AE.18",
  "ERRO DE CÁLCULO — verificado por álgebra direta nesta auditoria: de λ≡M_gU'/U e y²=U/(3M_g²H²) (AE.18), segue U'=λU/M_g=λ(3M_g²H²y²)/M_g=3M_gH²λy², logo U'/H²=3M_gλy² (um fator de M_g), não 3M_g²λy² (dois fatores) como escrito; o erro NÃO se propaga — a equação seguinte (AE.28) usa implicitamente o valor correto", False),
 ("AE", r"\frac{U'}{\sqrt{6}M_g H^2} = \sqrt{\frac{3}{2}}\lambda y^2.", "AE.27",
  "CONFERE (verificado: usa implicitamente o valor CORRETO de U'/H²=3M_gλy² — não a versão com M_g² erroneamente escrita em AE.27 — resultando exatamente em √(3/2)λy²: 3M_gλy²/(√6M_g)=（3/√6)λy²=√(3/2)λy²)", False),
 ("AE", r"\frac{dx}{dN} = -3x - x\frac{d\ln H}{dN} - \sqrt{\frac{3}{2}}\lambda y^2 + \mathcal{S}(r,\xi,\chi)\frac{m^2}{H^2}",
  "AE.26, AE.28; âncora D2/D8",
  "ERRO DE CÁLCULO (álgebra de combinação de AE.26+AE.28 verificada e correta EM SI, mas herda o erro de sinal de AE.09/11/22: o último termo deveria ser −𝒮(r,ξ,χ)m²/H², não +)", False),
 ("AE", r"\mathcal{S}(r,\xi,\chi)= \frac{ M_{eff}^2}{\sqrt{6}M_g}F'(\chi)V(\xi,r).", "AE.26, AE.28",
  "CONFERE (definição de conveniência, consistente algebricamente com a extração de AE.26/28 — o sinal do termo em que aparece em AE.29 é que carrega o erro herdado, não esta definição em si)", False),
 ("AE", r"\dot\eta = \Gamma \dot\chi^2 \Rightarrow \frac{d\eta}{dN} = \frac{\dot\eta}{H} = \Gamma \frac{\dot\chi^2}{H}.",
  f"AE.12; {A2}",
  "CONFERE (rearranjo correto para N; mesma nota de AE.12 — CONFLITA COM Cap.1 §1.6/Cap.2 §2.7, achado A2/lote 1)", False),
 ("AE", r"\dot\chi^2 = 6M_g^2 H^2 x^2,", "AE.23",
  "CONFERE (álgebra verificada: quadrado direto de AE.23)", False),
 ("AE", r"\frac{d\eta}{dN} = 6\Gamma M_g^2 H x^2", f"AE.31, AE.32; {A2}",
  "CONFERE (álgebra verificada: substituição direta de AE.32 em AE.31; mesma nota de AE.12/31 sobre a lei conflitante de η)", False),
 ("AE", r"De \rho_m\propto a^{-3}:", "—",
  "ARTEFATO DE CONVERSÃO (prosa dentro de $ — \"De ρm∝a⁻³:\" é frase introdutória, não fórmula; mesmo padrão de outros fragmentos de prosa capturados pelo extrator)", False),
 ("AE", r"\frac{d\ln\rho_m}{dN}=-3.", "—",
  "CONFERE (consequência direta de ρm∝a⁻³: d(ln ρm)/dN=-3)", False),
 ("AE", r"\Omega_m = \frac{\rho_m}{3M_g^2H^2},", "AE.18",
  "CONFERE (reprise de AE.18)", False),
 ("AE", r"\frac{d\ln\Omega_m}{dN} = -3 - 2\frac{d\ln H}{dN}.", "AE.35, AE.36",
  "CONFERE (álgebra verificada: derivada logarítmica de AE.36 usando AE.35)", False),
 ("AE", r"\frac{d\Omega_m}{dN} = \Omega_m\left(-3 -2\frac{d\ln H}{dN}\right).", "AE.37",
  "CONFERE (álgebra verificada: rearranjo direto de AE.37)", False),
 ("AE", r"H^2 = \frac{8\pi G}{3}\frac{\rho_{tot}}{1-\eta}.", D4,
  "NÃO-DERIVÁVEL — âncora D4: esta forma não é derivável da ação bimétrica atual (η está ausente da ação); uma extensão mínima Ω(η)R_g produziria um termo extra Hη̇/(1−η) não presente aqui; a forma só vale, quando muito, no regime adiabático |η̇|≪H — deve ser reclassificada como extensão proposta, não consequência da ação (mesma nota de Cap.1 §1.6/Cap.2 §2.7/Anexo H §H.6, lote 1)", False),
 ("AE", r"\ln H^2 = \ln\rho_{tot} - \ln(1-\eta) + const.", f"AE.39; {D4}",
  "CONFERE (álgebra correta — logaritmo de AE.39; herda o status de extensão postulada, não derivada da ação — âncora D4; flag sem-delimitador)", False),
 ("AE", r"\frac{d\ln H^2}{dN} = \frac{d\ln\rho_{tot}}{dN} + \frac{1}{1-\eta}\frac{d\eta}{dN}.", f"AE.40; {D4}",
  "CONFERE (álgebra verificada: derivada de AE.40 — mesma nota de extensão postulada, âncora D4)", False),
 ("AE", r"\frac{d\ln H}{dN} = \frac12\frac{d\ln\rho_{tot}}{dN} + \frac{1}{2(1-\eta)}\frac{d\eta}{dN}.", f"AE.41; {D4}",
  "CONFERE (álgebra verificada: divisão de AE.41 por 2 — mesma nota de extensão postulada, âncora D4)", False),
 ("AE", r"w_{\text{eff}}(N) = -1 + \frac{1}{3(1-\eta)}\frac{d\eta}{dN},", "—",
  "CONFERE SOB HIPÓTESE (o próprio texto apresenta isto como escolha de conveniência — \"é comum: usar diretamente\" — não uma consequência direta e rigorosa de AE.39-42 mostrada explicitamente nesta seção)", True),
 ("AE", r"\frac{d\ln H}{dN} = -\frac32\left(1+w_{\text{eff}}\right)\left(1-\Omega_r\right)+\cdots", "AE.42, AE.43",
  "INCOMPLETA (o próprio texto declara que a forma depende de \"quais componentes foram incluídos\" e usa reticências \"+⋯\" — fórmula esquemática, não fechada)", False),
 ("AE", r"H=\xi H_f \Rightarrow H_f = \frac{H}{\xi}.", f"AE.16; {D1}, {D5}",
  "CONFERE (reprise de AE.16 — mesma nota sobre o ramo dinâmico, âncoras D1/D5)", False),
 ("AE", r"3M_f^2 H_f^2 = m^2M_{eff}^2F(\chi) \left(\beta_4+3\beta_3 r^{-1}+3\beta_2 r^{-2}+\beta_1 r^{-3}\right).",
  "AE.07, AE.08", "CONFERE (substituição direta de AE.08 em AE.07 — reprise, já verificada em AB.50)", False),
 ("AE", r"3M_f^2 \frac{H^2}{\xi^2} = m^2M_{eff}^2F(\chi)\,\mathcal{U}(r),", "AE.45, AE.46",
  "CONFERE (substituição direta de AE.45 em AE.46, com a bracket renomeada 𝒰(r) — definida a seguir em AE.48)", False),
 ("AE", r"\mathcal{U}(r)\equiv \beta_4+3\beta_3 r^{-1}+3\beta_2 r^{-2}+\beta_1 r^{-3}.", "AE.08/46",
  "CONFERE (definição, idêntica à bracket de AE.08/46)", False),
 ("AE", r"\xi(N) = H\sqrt{\frac{3M_f^2}{m^2M_{eff}^2F(\chi)\mathcal{U}(r)}}", "AE.47",
  "CONFERE (álgebra verificada: solução direta de AE.47 para ξ, com a ressalva honesta do próprio texto sobre a escolha de sinal)", False),
 ("AE", r"r=\frac{b}{a} \Rightarrow \dot r = r(N_fH_f - H)= r(\xi H_f - H).", "Anexo B §B.9 (AB.60-62)",
  "CONFERE (álgebra verificada, consistente com Anexo B §B.9/AB.60-62 especializado a N_g=1)", False),
 ("AE", r"\dot r = 0.", f"AE.15, AE.50; {D5}",
  "CONFERE — âncora D5: ṙ≡0 confirmado de novo (também em Anexo B §B.9/AB.65) — mas ao contrário do Cap.14 §14.12 (achado C1/lote 3), este anexo NÃO tenta contornar o resultado: a prosa que segue (E.9.A/E.9.B) reconhece honestamente a implicação e propõe r constante como a prática mais simples, na linha do que a âncora D5 recomenda (raiz móvel/algébrica em vez de \"r(t) dinâmico\" genuíno no ramo H=ξHf)", False),
 ("AE", r"H(z) \quad\text{com}\quad 1+z=a^{-1}.", "—",
  "CONFERE (relação padrão redshift-fator de escala)", False),
 ("AE", r"w_{\text{eff}}(N) = -1 + \frac{1}{3(1-\eta)}\frac{d\eta}{dN}.", "AE.43",
  "CONFERE SOB HIPÓTESE (reprise de AE.43 — mesma nota sobre ser uma parametrização de conveniência)", False),
 ("AE", r"\Omega_m(N),\quad \Omega_\chi(N),\quad \Omega_{int}(N).", "AE.18/19",
  "CONFERE (lista de observáveis, consistente com as definições de AE.18/19; nota: Ω_χ não foi explicitamente definida antes — presumivelmente x²+y² por AE.20 — pequena incompletude notacional)", False),
 ("AE", r"m_T^2(N)=m^2F(\chi)\mu_T^2(\cdots).", f"Anexo D §D.4 (AD.09); {D2}",
  "CONFERE (reprise da estrutura de AD.09 — âncora D2 para a forma exata de μ_T²)", False),
 ("AE", r"m_T^2(N) \ge 2H^2(N).", f"{D2}",
  "CONFERE (reprise do bound de Higuchi — âncora D2 para a forma exata de m_T²)", False),
 ("AE", r"(m,\beta_n,M_g,M_f, U(\chi), F(\chi), \Gamma).", "—",
  "ARTEFATO DE CONVERSÃO (resíduo de blockquote Markdown \">\" preso dentro do \"$\", mesmo padrão de Anexo B §B.11/Cap.16 §16.9; conteúdo é apenas uma lista de parâmetros a fixar, não uma equação)", False),
]


def main():
    aplicados = 0
    problemas = []
    arquivos = ("AE",)
    textos = {}
    for pref in arquivos:
        with open(os.path.join(REG, pref + ".md"), encoding="utf-8") as fh:
            textos[pref] = re.split(r"(?=### \[)", fh.read())
    for pref, key, dep, ver, multi in V:
        blocos = textos[pref]
        hits = [i for i, b in enumerate(blocos)
                if b.startswith("### [") and key in b and "_(pendente)_" in b]
        if not hits:
            problemas.append(f"{pref}: '{key[:60]}' -> 0 pendentes")
            continue
        if len(hits) > 1 and not multi:
            problemas.append(f"{pref}: '{key[:60]}' -> {len(hits)} blocos")
            continue
        for i in hits:
            b = blocos[i]
            b = b.replace("- **Depende de:** _(a preencher)_",
                          f"- **Depende de:** {dep}")
            b = b.replace("- **Veredito:** _(pendente)_",
                          f"- **Veredito:** {ver}")
            blocos[i] = b
            aplicados += 1
    for pref in arquivos:
        texto = "".join(textos[pref])
        with open(os.path.join(REG, pref + ".md"), "w", encoding="utf-8") as fh:
            fh.write(texto)
        print(f"{pref}: {texto.count('_(pendente)_')} pendentes")
    print(f"\naplicados: {aplicados}")
    for p in problemas:
        print("  -", p)


if __name__ == "__main__":
    main()
