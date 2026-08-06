# -*- coding: utf-8 -*-
"""
aplica_vereditos_lote07.py — vereditos do Lote 7 (Anexo B / AB, 71 eqs).
Casamento por substring; multi=True aplica a todas as ocorrencias
pendentes DENTRO DO MESMO ARQUIVO.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
REG = os.path.normpath(os.path.join(HERE, '..', 'registro'))

D3 = "âncora D3 (derivations/03_dV_dNg_regra_cadeia.md)"
D5 = "âncora D5 (derivations/05_rdot_ramo_dinamico.md)"

V = [
 ("AB", r"S = \frac{M_g^2}{2}\int d^4x\,\sqrt{-g}\,R[g] + \frac{M_f^2}{2}\int d^4x\,\sqrt{-f}\,R[f] - m^2 M_{\mathrm{eff}}^2\int d^4x\,\sqrt{-g}\,F(\chi)\,V(\mathcal{K}) + S_\chi + S_m.",
  "Anexo A §A.1 (AA.02)",
  "CONFERE (reprise da ação HR de AA.02, agora com a modulação F(χ) — consistente com Cap.3/Cap.14/Cap.20)", False),
 ("AB", r"V(\mathcal{K})=\sum_{n=0}^4\beta_n e_n(\mathcal{K}), \qquad \mathcal{K}=\sqrt{g^{-1}f}.",
  "Anexo A §A.1 (AA.04/05)", "CONFERE (reprise de AA.04/05)", False),
 ("AB", r"S_\chi = \int d^4x\,\sqrt{-g}\left[-\frac12 g^{\mu\nu}\partial_\mu\chi\partial_\nu\chi - U(\chi)\right].",
  "—", "CONFERE (ação padrão de campo escalar mínimo, importada)", False),
 ("AB", r"ds_g^2 = -N_g^2(t)dt^2 + a^2(t)\delta_{ij}dx^i dx^j,", "Anexo A §A.6 (AA.18)",
  "CONFERE (reprise de AA.18)", False),
 ("AB", r"ds_f^2 = -N_f^2(t)dt^2 + b^2(t)\delta_{ij}dx^i dx^j.", "Anexo A §A.6 (AA.19)",
  "CONFERE (reprise de AA.19)", False),
 ("AB", r"H_g \equiv \frac{1}{N_g}\frac{\dot a}{a}, \qquad H_f \equiv \frac{1}{N_f}\frac{\dot b}{b}.",
  "Cap.14 §14.2", "CONFERE (definição padrão, consistente com Cap.14 §14.2)", False),
 ("AB", r"r(t)\equiv \frac{b(t)}{a(t)}, \qquad \xi(t)\equiv \frac{N_f(t)}{N_g(t)}.",
  "Anexo A §A.6 (AA.23)", "CONFERE (reprise de AA.23)", False),
 ("AB", r"\mathcal{K}=\mathrm{diag}(\xi,r,r,r).", "Anexo A §A.6 (AA.22)",
  "CONFERE (reprise de AA.22)", False),
 ("AB", r"e_0=1,", "Anexo A §A.7 (AA.24-27)",
  "CONFERE (reprise de AA.24-27, já verificada por álgebra explícita no lote 6)", False),
 ("AB", r"e_1=\xi+3r,", "Anexo A §A.7 (AA.24)", "CONFERE (reprise de AA.24, verificada)", False),
 ("AB", r"e_2=3\xi r+3r^2,", "Anexo A §A.7 (AA.25)", "CONFERE (reprise de AA.25, verificada)", False),
 ("AB", r"e_3=3\xi r^2+r^3,", "Anexo A §A.7 (AA.26)", "CONFERE (reprise de AA.26, verificada)", False),
 ("AB", r"e_4=\xi r^3.", "Anexo A §A.7 (AA.27)", "CONFERE (reprise de AA.27, verificada)", False),
 ("AB", r"V(\xi,r)= \beta_0 +\beta_1(\xi+3r) +\beta_2(3\xi r+3r^2) +\beta_3(3\xi r^2+r^3) +\beta_4(\xi r^3).",
  "Anexo A §A.7 (AA.28)", "CONFERE (reprise de AA.28)", True),
 ("AB", r"V\to F(\chi)V(\xi,r).", "Cap.3 §3.8/Cap.14",
  "CONFERE (modulação TDCP padrão, consistente com Cap.3 §3.8/Cap.14)", False),
 ("AB", r"S = \int dt\,\mathcal{L}(a,\dot a,N_g;\,b,\dot b,N_f;\,\chi,\dot\chi).", "—",
  "CONFERE (afirmação estrutural padrão da redução minisuperespaço)", False),
 ("AB", r"\mathcal{L}_g = -3M_g^2\,\frac{a\dot a^2}{N_g}.", "—",
  "CONFERE (forma padrão de redução minisuperespaço do termo de Einstein-Hilbert em FLRW — importada, consistente com o uso implícito em todo o corpus desde Cap.14)", False),
 ("AB", r"\mathcal{L}_f = -3M_f^2\,\frac{b\dot b^2}{N_f}.", "AB.17 (mesma forma, setor f)",
  "CONFERE (mesma forma padrão, setor f)", False),
 ("AB", r"\sqrt{-g} = N_g a^3.", "—",
  "CONFERE (verificado: det(g)=diag(-N_g²,a²,a²,a²) ⟹ det=-N_g²a⁶ ⟹ √-g=N_g a³)", False),
 ("AB", r"\mathcal{L}_{int} = - m^2 M_{eff}^2\,(N_g a^3)\,F(\chi)\,V(\xi,r).", "AB.19",
  "CONFERE (substituição direta de AB.19 no termo de interação da ação)", False),
 ("AB", r"\sqrt{-g}\left(-\frac12 g^{00}\dot\chi^2 - U(\chi)\right) = N_g a^3\left(\frac{1}{2N_g^2}\dot\chi^2 - U(\chi)\right).",
  "—",
  "CONFERE (álgebra verificada: g^00=-1/N_g² ⟹ -½g^00χ̇²=χ̇²/(2N_g²); multiplicando por √-g=N_g a³ dá exatamente a forma escrita)", False),
 ("AB", r"\mathcal{L}_\chi = a^3\left(\frac{1}{2N_g}\dot\chi^2 - N_g U(\chi)\right).", "AB.21",
  "CONFERE (simplificação algébrica direta de AB.21: N_g a³/(2N_g²)=a³/(2N_g) ✓)", False),
 ("AB", r"\delta S_m = -\frac12\int d^4x \sqrt{-g}\,T_{\mu\nu}\delta g^{\mu\nu}.", "—",
  "CONFERE (definição padrão de T_μν, importada)", False),
 ("AB", r"\mathcal{L}_m = -N_g a^3 \rho_m.", "AB.23",
  "CONFERE SOB HIPÓTESE (forma padrão para o setor de matéria em minisuperespaço — o passo intermediário ligando AB.23 a este resultado específico não é mostrado explicitamente, mas a forma final é a usual: T_00=ρ_m integrado com o elemento de volume N_g a³)", False),
 ("AB", r"\mathcal{L} = -3M_g^2\,\frac{a\dot a^2}{N_g} -3M_f^2\,\frac{b\dot b^2}{N_f} - m^2 M_{eff}^2 N_g a^3 F(\chi)V(\xi,r) + a^3\left(\frac{1}{2N_g}\dot\chi^2 - N_g U(\chi)\right) - N_g a^3 \rho_m.",
  "AB.17, 18, 20, 22, 24",
  "CONFERE (soma direta e correta de AB.17+18+20+22+24, termo a termo)", False),
 ("AB", r"\frac{\partial\mathcal{L}}{\partial N_g}=0.", "—",
  "CONFERE (princípio variacional padrão — N_g é multiplicador de Lagrange/lapso não-dinâmico, extremizar dá uma constraint)", False),
 ("AB", r"\frac{\partial}{\partial N_g}\left(-3M_g^2\frac{a\dot a^2}{N_g}\right) = -3M_g^2 a\dot a^2\left(-\frac{1}{N_g^2}\right) = \frac{3M_g^2 a\dot a^2}{N_g^2}.",
  "AB.17",
  "CONFERE (álgebra verificada: d/dN_g(1/N_g)=-1/N_g², sinais conferem)", False),
 ("AB", r"\frac{\partial}{\partial N_g}\left(-m^2M_{eff}^2 N_g a^3F V\right) = - m^2 M_{eff}^2 a^3 F V.",
  f"{D3}",
  "ERRO DE CÁLCULO — âncora D3: falta o termo da regra da cadeia. ξ=N_f/N_g depende explicitamente de N_g (∂ξ/∂N_g=-ξ/N_g), então V(ξ,r) TAMBÉM depende de N_g através de ξ — este cálculo trata V como se ∂ξ/∂N_g=0. A derivada completa é ∂/∂N_g(-m²M_eff²N_ga³FV) = -m²M_eff²a³F[V-ξ∂V/∂ξ], não -m²M_eff²a³FV; o próprio Anexo B, ao variar em N_f na seção seguinte (§B.6, ver AB.40), aplica a regra da cadeia corretamente — a assimetria de tratamento entre as duas variações é a origem do erro", False),
 ("AB", r"\frac{\partial}{\partial N_g}\left(a^3\frac{1}{2N_g}\dot\chi^2\right) = -\frac{a^3}{2N_g^2}\dot\chi^2,",
  "AB.22", "CONFERE (álgebra verificada: d/dN_g(1/N_g)=-1/N_g²)", False),
 ("AB", r"\frac{\partial}{\partial N_g}\left(-a^3 N_g U\right) = - a^3 U.", "AB.22",
  "CONFERE (derivada linear trivial, verificada)", False),
 ("AB", r"\frac{\partial}{\partial N_g}(-N_g a^3\rho_m)= -a^3\rho_m.", "AB.24",
  "CONFERE (derivada linear trivial, verificada)", False),
 ("AB", r"\frac{3M_g^2 a\dot a^2}{N_g^2} - m^2 M_{eff}^2 a^3F V - \frac{a^3}{2N_g^2}\dot\chi^2 - a^3U - a^3\rho_m =0.",
  f"AB.27+28+29+30+31; {D3}",
  "ERRO DE CÁLCULO (herda o erro de AB.28 — âncora D3: falta o termo -ξ∂V/∂ξ; correção: substituir \"-m²M_eff²a³FV\" por \"-m²M_eff²a³F[V-ξ∂V/∂ξ]\")", False),
 ("AB", r"H_g = \frac{1}{N_g}\frac{\dot a}{a} \quad\Rightarrow\quad \frac{\dot a^2}{N_g^2 a^2} = H_g^2.",
  "AB.06", "CONFERE (identidade trivial a partir de AB.06, elevada ao quadrado)", False),
 ("AB", r"3M_g^2 H_g^2 = \rho_m + \left(\frac12\frac{\dot\chi^2}{N_g^2}+U\right) + m^2M_{eff}^2 F(\chi)V(\xi,r).",
  f"AB.32, AB.33; {D3}",
  "ERRO DE CÁLCULO (herda o erro de AB.28/32 — âncora D3: o último termo deveria ser m²M_eff²F(χ)[V(ξ,r)-ξ∂V/∂ξ], que colapsa para m²M_eff²F(χ)(β0+3β1r+3β2r²+β3r³) — sem ξ, sem β4)", False),
 ("AB", r"3M_g^2 H_g^2 = \rho_m + \rho_\chi + \rho_{int}^{(g)},", "AB.34",
  "CONFERE (forma estrutural correta — reprise de AB.34 com nomes; a definição de ρ_int^(g) na equação seguinte é que carrega o erro herdado)", True),
 ("AB", r"\rho_\chi = \frac12\dot\chi^2+U(\chi), \qquad \rho_{int}^{(g)} = m^2M_{eff}^2F(\chi)V(\xi,r).",
  f"Anexo A §A.8 (AA.30); {D3}",
  "ERRO DE CÁLCULO ; CONFLITA COM [AA.30] — âncora D3: a definição de ρ_int^(g) aqui (=m²M_eff²F(χ)V(ξ,r), retendo ξ e β4) herda a derivada incompleta de AB.28 (falta o termo -ξ∂V/∂ξ); a forma correta, m²M_eff²F(χ)(β0+3β1r+3β2r²+β3r³), coincide com o Anexo A §A.8 (AA.30) e com o que todo o corpo principal usa (ex. Cap.14 §14.7); ρ_χ=½χ̇²+U(χ) está correta (densidade padrão de Klein-Gordon)", False),
 ("AB", r"\frac{\partial\mathcal{L}}{\partial N_f}=0.", "AB.26",
  "CONFERE (princípio variacional padrão, análogo a AB.26)", False),
 ("AB", r"-3M_f^2\frac{b\dot b^2}{N_f} \quad\Rightarrow\quad \frac{\partial}{\partial N_f} = \frac{3M_f^2 b\dot b^2}{N_f^2}.",
  "AB.18", "CONFERE (álgebra verificada, análoga a AB.27)", False),
 ("AB", r"\xi = \frac{N_f}{N_g}.", "AB.07",
  "CONFERE (reprise de AB.07, destacada aqui pela dependência relevante à regra da cadeia que segue)", False),
 ("AB", r"\frac{\partial}{\partial N_f}\left(-m^2M_{eff}^2N_ga^3F V(\xi,r)\right) = -m^2M_{eff}^2N_ga^3F \frac{\partial V}{\partial \xi} \frac{\partial\xi}{\partial N_f}.",
  "AB.20, AB.39",
  "CONFERE (regra da cadeia aplicada corretamente — diferente de AB.28, aqui não há termo de produto adicional pois N_g,a,F não dependem de N_f, só ξ dentro de V depende)", False),
 ("AB", r"\frac{\partial\xi}{\partial N_f}=\frac{1}{N_g}.", "AB.39",
  "CONFERE (álgebra verificada: derivada parcial trivial de ξ=N_f/N_g em relação a N_f, com N_g fixo)", False),
 ("AB", r"\frac{\partial\mathcal{L}_{int}}{\partial N_f} = -m^2M_{eff}^2a^3F \frac{\partial V}{\partial \xi}.",
  "AB.40, AB.41",
  "CONFERE (álgebra verificada: substituindo AB.41 em AB.40, N_g cancela exatamente)", False),
 ("AB", r"\frac{3M_f^2 b\dot b^2}{N_f^2} - m^2M_{eff}^2a^3F\frac{\partial V}{\partial \xi} =0.",
  "AB.38, AB.42", "CONFERE (soma direta e correta de AB.38+AB.42)", False),
 ("AB", r"\frac{3M_f^2 r^3 a^3}{a^3}\left(\frac{\dot b^2}{N_f^2 b^2}\right) = m^2M_{eff}^2F\frac{\partial V}{\partial \xi}.",
  "AB.43",
  "CONFERE (álgebra verificada: 3M_f²bḃ²/(N_f²a³) com b=ra reduz a 3M_f²r³(ḃ²/(N_f²b²)) — a manipulação a³/a³=1 é um passo redundante mas não afeta a correção)", False),
 ("AB", r"H_f = \frac{1}{N_f}\frac{\dot b}{b},", "AB.06", "CONFERE (reprise de AB.06)", False),
 ("AB", r"3M_f^2 r^3 H_f^2 = m^2M_{eff}^2F(\chi)\frac{\partial V}{\partial \xi}.", "AB.44, AB.45",
  "CONFERE (substituição direta de AB.45 em AB.44)", False),
 ("AB", r"\frac{\partial V}{\partial\xi} = \beta_1 +3\beta_2 r +3\beta_3 r^2 +\beta_4 r^3.", "AB.47",
  "CONFERE (álgebra verificada: derivada parcial de AB.47 em relação a ξ, termo a termo — ∂V/∂ξ=β1+3β2r+3β3r²+β4r³ ✓)", False),
 ("AB", r"3M_f^2 r^3 H_f^2 = m^2M_{eff}^2F(\chi)\left(\beta_1+3\beta_2 r+3\beta_3 r^2+\beta_4 r^3\right).",
  "AB.46, AB.48", "CONFERE (substituição direta de AB.48 em AB.46)", False),
 ("AB", r"3M_f^2 H_f^2 = m^2M_{eff}^2F(\chi)\left(\beta_4+3\beta_3 r^{-1}+3\beta_2 r^{-2}+\beta_1 r^{-3}\right).",
  "AB.49; verificação cruzada §3.4 da âncora D3",
  "CONFERE (álgebra verificada: divisão termo a termo de AB.49 por r³ ✓ — esta é a equação de Friedmann do setor f, já usada como checagem cruzada independente pela âncora D3 §3.4)", False),
 ("AB", r"M_g^2(2\dot H_g + 3H_g^2) = - (p_m + p_\chi + p_{int}^{(g)}),", "—",
  "INCOMPLETA (o próprio texto declara isso como esquemático — \"de modo esquemático\" — e que \"as expressões completas são extensas\"; a forma segue o padrão esperado de uma equação tipo Raychaudhuri para um fluido efetivo, mas p_int^(g) nunca é calculado explicitamente aqui nem em nenhum lugar anterior do corpus)", False),
 ("AB", r"p_\chi=\frac12\dot\chi^2-U(\chi),", "AB.36 (ρ_χ)",
  "CONFERE (pressão padrão de Klein-Gordon, complementar a ρ_χ=½χ̇²+U de AB.36)", False),
 ("AB", r"\nabla_g^\mu X_{\mu\nu}=0", "Cap.4 §4.4 (confirmado no lote 1, achado A1)",
  "CONFERE (importada — resultado padrão do formalismo HR: invariância por difeomorfismo do potencial de interação implica esta identidade tipo Bianchi; consistente com Cap.4 §4.4, já confirmado no lote 1 como a base correta do achado A1 — não há troca de energia entre setores, Q≡0)", False),
 ("AB", r"\left(\beta_1 + 2\beta_2 r + \beta_3 r^2\right)\left(H_g - \xi H_f\right)=0. $$",
  "AB.53; Cap.5/Cap.14 (lotes 1/3)",
  "CONFERE SOB HIPÓTESE (resultado padrão de gravidade bimétrica HR — Comelli-Nesti-Pilo e sucessores; a derivação explícita de AB.53 até esta forma polinomial específica não é mostrada em detalhe, \"vamos mostrar por que\" é seguido de um argumento qualitativo, não uma conta passo a passo — mas a forma é consistente com o uso confirmado em todo o corpo principal, ex. Cap.5/Cap.14, lotes 1/3)", False),
 ("AB", r"\nabla_g^\mu T^{(m)}_{\mu\nu}=0, \quad \nabla_g^\mu T^{(\chi)}_{\mu\nu} = (\Box\chi-U')\partial_\nu\chi,",
  "—",
  "CONFERE (identidades padrão: conservação de matéria por acoplamento mínimo, e a identidade de Klein-Gordon ∇^μT^(χ)_μν=(□χ-U')∂νχ — que se anula on-shell)", False),
 ("AB", r"\left(\beta_1 + 2\beta_2 r + \beta_3 r^2\right)\left(H_g - \xi H_f\right)=0 $$",
  "AB.54", "CONFERE SOB HIPÓTESE (reprise de AB.54)", False),
 ("AB", r"\beta_1 + 2\beta_2 r + \beta_3 r^2 = 0 \quad\Rightarrow\quad r = \text{constante}.",
  "AB.56; Cap.14 §14.10 (âncora D5)",
  "CONFERE (consequência lógica direta de AB.56: uma equação algébrica em r fixa r em suas raízes, que são constantes — consistente com a \"raiz r★\" usada extensivamente em Cap.14, âncora D5)", False),
 ("AB", r"H_g = \xi H_f.", "AB.56; Cap.14 §14.10",
  "CONFERE (a outra alternativa lógica de AB.56 — consistente com a constraint usada no Cap.14 §14.10, âncora D5)", False),
 ("AB", r"r=\frac{b}{a}.", "AB.07", "CONFERE (reprise de AB.07)", False),
 ("AB", r"\dot r = \frac{\dot b}{a} - \frac{b\dot a}{a^2} = r\left(\frac{\dot b}{b} - \frac{\dot a}{a}\right).",
  "AB.59", "CONFERE (álgebra verificada: regra do quociente padrão, d/dt(b/a)=ḃ/a-bȧ/a²=r(ḃ/b-ȧ/a))", False),
 ("AB", r"\frac{\dot b}{b}=N_f H_f, \quad \frac{\dot a}{a}=N_g H_g.", "AB.06",
  "CONFERE (rearranjo direto de AB.06)", False),
 ("AB", r"\dot r = r(N_f H_f - N_g H_g) = rN_g(\xi H_f - H_g).", "AB.60, AB.61, AB.07",
  "CONFERE (álgebra verificada: substituindo AB.61 em AB.60 e fatorando N_g com ξ=N_f/N_g)", False),
 ("AB", r"Se N_g=1:", "B.2",
  "ARTEFATO DE CONVERSÃO (prosa dentro de $, mesmo padrão de \"Se Q_0>0:\" no Cap.4/Cap.9 — condição de gauge N_g=1, válida por invariância de reparametrização temporal já mencionada em B.2)", False),
 ("AB", r"\dot r = r(\xi H_f - H_g).", "AB.62", "CONFERE (consequência direta de AB.62 com N_g=1)", False),
 ("AB", r"\dot r=0", f"AB.58, AB.64; {D5}",
  "CONFERE — âncora D5: ṙ≡0 verificado exatamente por substituição direta de H_g=ξH_f (o \"ramo dinâmico\", AB.58) em AB.64; esta é a derivação CORRETA que o Cap.14 §14.12 (lote 3, achado C1) contorna incorretamente ao trocar a constraint por uma condição não-equivalente (H_b-ξH_g=0) — o Anexo B, na fonte, já tinha o resultado certo; o erro do Cap.14 é dele mesmo, não herdado daqui", False),
 ("AB", r"f_{\mu\nu} = c^2 g_{\mu\nu}.", "Cap.13/Cap.14 (lote 3)",
  "CONFERE (mesmo ansatz proporcional já usado em Cap.13/Cap.14, lote 3)", False),
 ("AB", r"b = c a \Rightarrow r=c=\text{constante}.", "AB.66",
  "CONFERE (consequência direta de AB.66 no fundo FLRW: b²=c²a² ⟹ b=ca ⟹ r=b/a=c)", False),
 ("AB", r"\rho_{int}^{(g)} = m^2M_{eff}^2F(\chi) (\beta_0+3\beta_1 c+3\beta_2 c^2+\beta_3 c^3).",
  f"Anexo A §A.8 (AA.30); {D3}",
  "CONFERE — âncora D3: usa corretamente a forma sem ξ e sem β4 (idêntica ao Anexo A §A.8/AA.30, com r→c), diferente da citação errada de AB.36 na mesma seção B.5; NOTA: evidência adicional a favor do achado D3 — a forma correta reaparece aqui, de memória, dentro do próprio Anexo B", False),
 ("AB", r"3M_g^2 H_g^2=\rho_m+\rho_\chi+\rho_{int}^{(g)}.", "AB.35",
  "CONFERE (reprise estrutural de AB.35 — mesma nota: a definição de ρ_int^(g) é que carrega o erro, não esta forma)", False),
 ("AB", r"3M_f^2 H_f^2=\rho_{int}^{(f)}.", "AB.50",
  "CONFERE (reprise compacta e correta do resultado de AB.50, agora nomeado ρ_int^(f))", False),
 ("AB", r"(\beta_1+2\beta_2 r+\beta_3 r^2)(H_g-\xi H_f)=0.", "AB.54/56",
  "CONFERE SOB HIPÓTESE (reprise de AB.54/56)", False),
]


def main():
    aplicados = 0
    problemas = []
    arquivos = ("AB",)
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
