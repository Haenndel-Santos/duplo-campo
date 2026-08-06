# -*- coding: utf-8 -*-
"""
aplica_vereditos_lote10.py — vereditos do Lote 10 (Anexos F+G+H).
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
A2 = "achado A2 (lote 1: duas leis incompatíveis para η)"
SINAL = "âncoras D2/D8 (erratum de sinal na equação de χ)"

V = [
 # ================= AF (17) — espaço de parâmetros =================
 ("AF", r"\{ m,\beta_0,\beta_1,\beta_2,\beta_3,\beta_4,M_g,M_f \}", "—",
  "CONFERE (lista de parâmetros, consistente com o corpo principal)", False),
 ("AF", r"\{ U(\chi),F(\chi),\Gamma \}", "—", "CONFERE (lista de parâmetros)", False),
 ("AF", r"\chi_i,\dot\chi_i,r_i,\eta_i.", "—", "CONFERE (lista de condições iniciais)", False),
 ("AF", r"F(\chi) > 0", "Anexo C §C.7 (AC.11)",
  "CONFERE (reprise da condição de positividade já em AC.11/Anexo C §C.7)", False),
 ("AF", r"m_T^2(t) \ge 2H^2", "Anexo D §D.7 (AD.14)",
  "CONFERE (bound de Higuchi padrão, repete AD.14/AC.17)", False),
 ("AF", r"m_T^2 = m^2F(\chi)\mu_T^2(r,\beta_n),", f"{D2}",
  "INCOMPLETA (μ_T² aqui é listada como função de (r,βn) apenas, omitindo ξ — ao contrário da forma mais completa do Anexo D §D.4/AD.09, μ_T²(r,ξ,βn,M_g,M_f); a âncora D2 mostra que a dependência em ξ é essencial, inclusive determinante de sinal)", False),
 ("AF", r"m^2F(\chi)\mu_T^2 \ge 2H^2.", "AF.06",
  "INCOMPLETA (herda a omissão de ξ de AF.06)", False),
 ("AF", r"\mathcal{S}_{\text{Higuchi}}.", "—",
  "CONFERE (notação — define o nome da superfície de Higuchi no espaço de parâmetros)", False),
 ("AF", r"K_{11}>0, \quad K_{22}>0, \quad \det K>0.", "Anexo C §C.10 (AC.19)",
  f"CONFERE (reprise direta de Anexo C §C.10/AC.19 — mesma nota sobre a contagem de 2 modos refutada pela âncora D1, real: 3 modos)", False),
 ("AF", r"\mathcal{B}(r)=\beta_1+2\beta_2 r+\beta_3 r^2.", f"Anexo D §D.5 (AD.10); {D1}",
  "CONFERE SOB HIPÓTESE — a claim de que a degenerescência em B(r)=0 é um \"ponto crítico\" é consistente com o benchmark C da âncora D1 (ramo algébrico, r=r★: par degenerado, kN∼10⁻¹⁶); mas a caracterização de B(r) como o que a saúde do ghost é \"particularmente sensível\" superclaima — D1 mostra que o par fantasma dos benchmarks A/B persiste nos DOIS lados de qualquer cruzamento de B(r), não é B(r) que decide a saúde geral", False),
 ("AF", r"c_{s,\pm}^2>0.", "Anexo C §C.8/C.10 (AC.14/20)",
  "CONFERE (reprise de AC.14/20)", False),
 ("AF", r"m^2F(\chi) \to 0 \quad\text{ou}\quad r \to 0,\infty.", "—",
  "CONFERE SOB HIPÓTESE (qualitativa, plausível como comportamento assintótico genérico, não derivada explicitamente aqui)", False),
 ("AF", r"f\sigma_8(z)", "Cap.8/Cap.23", "CONFERE (nomeia observável já definido, Cap.8/Cap.23)", False),
 ("AF", r"G_{\text{eff}}(k,z)", "Cap.9 (lote 2)",
  "CONFERE (nomeia observável já definido no corpo principal — G_eff=Gμ, Cap.9/lote 2)", False),
 ("AF", r"\chi_i \approx 0, \quad \dot\chi_i \approx 0.", "Cap.10 (lote 2)",
  "CONFERE (consistente com a discussão do modo adiabático do Cap.10, já confirmada no lote 2)", False),
 ("AF", r"|c_T - 1| \ll 10^{-15}.", "Cap.11 §11.4 (achado C6/lote 3)",
  "CONFERE SOB HIPÓTESE (o argumento de supressão por massa ultraleve é válido para o modo MASSIVO não perturbar sinais de alta frequência; mas não cobre a ressalva do achado C6/lote 3 sobre o modo nominalmente massless: c_g²=1 mas c_f²=ξ²/r² — a combinação h_+ só propaga exatamente em c=1 se ξ=r, condição que precisa ser declarada antes de invocar GW170817 como \"região segura\" sem qualificação)", False),
 ("AF", r"\mathcal{R}_{\text{permitida}} = \mathcal{R}_{\text{Higuchi}} \cap \mathcal{R}_{\text{no-ghost}} \cap \mathcal{R}_{\text{grad}} \cap \mathcal{R}_{\text{CMB}} \cap \mathcal{R}_{\text{late-accel}}.",
  "—",
  "CONFERE (qualitativa — estrutura conceitual razoável de interseção de restrições, sem conteúdo matemático específico a verificar)", False),

 # ================= AG (5) — fundamentos filosóficos =================
 ("AG", r"G_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi G T_{\mu\nu}", "—",
  "CONFERE (importada — equação de campo de Einstein com constante cosmológica, padrão, citada aqui só para contraste conceitual com ΛCDM)", False),
 ("AG", r"\phi_1, \phi_2,", "Cap.1",
  "CONFERE (qualitativa — nomeia os graus de liberdade correlacionados do estado primordial, consistente com a narrativa de bifurcação do Cap.1)", False),
 ("AG", r"\Phi_+,\Phi_-", "Cap.1/Cap.2 (achado A7/lote 1)",
  "CONFERE (qualitativa — mesma notação Φ± do Cap.1/Cap.2, cuja especificação V(Φ±) permanece em aberto per achado A7/lote 1)", False),
 ("AG", r"\dot\eta = \Gamma \dot\chi^2 \ge 0.", f"Anexo E (AE.12/31/33); {A2}",
  "CONFERE (consequência trivial: Γχ̇²≥0 dado Γ>0, já que χ̇² é sempre não-negativo) ; CONFLITA COM Cap.1 §1.6/Cap.2 §2.7 — mesma lei de η já identificada no achado A2 (lote 1) e revisitada no Anexo E (lote 9); a interpretação filosófica de \"irreversibilidade\" (§G.5-G.9) depende de qual das duas leis conflitantes é a correta", False),
 ("AG", r"H^2 = \frac{8\pi G}{3}\frac{\rho}{1-\eta}.", f"Anexo E §E.7 (AE.39); {D4}",
  "NÃO-DERIVÁVEL — âncora D4, mesma nota de AE.39; a interpretação filosófica construída sobre ela (§G.9, \"aceleração como relaxamento\") herda a mesma pendência — é uma extensão proposta, não uma consequência derivada da ação", False),

 # ================= AH (17) — formalização canônica final =================
 ("AH", r"g_{\mu\nu} = f_{\mu\nu}, \quad \chi = 0, \quad \eta = 0.", "Cap.1",
  "CONFERE (postulado razoável — estado primordial simétrico como condição inicial, consistente com a narrativa de bifurcação do Cap.1)", False),
 ("AH", r"r = \frac{b}{a} \neq 1.", "—",
  "CONFERE (postulado — consequência da instabilidade declarada, consistente com r=b/a já definido)", False),
 ("AH", r"V(\mathcal{K}) = \sum_{n=0}^4 \beta_n e_n(\mathcal{K}), \quad \mathcal{K}=\sqrt{g^{-1}f}.",
  "Anexo A §A.1", "CONFERE (reprise da estrutura HR padrão)", False),
 ("AH", r"V \rightarrow F(\chi)V.", "Cap.3 §3.8", "CONFERE (reprise da modulação TDCP)", False),
 ("AH", r"\ddot\chi + 3H\dot\chi + U'(\chi) = m^2M_{eff}^2 F'(\chi)V.", SINAL,
  "ERRO DE CÁLCULO (mesmo erro de sinal já identificado em Anexo E §E.3(3)/AE.09/11 — âncoras D2/D8: deveria ser −m²M_eff²F'(χ)V; aqui elevado a \"Postulado 4\" da formalização canônica, o que amplifica a necessidade de correção)", False),
 ("AH", r"\dot\eta = \Gamma \dot\chi^2, \quad \Gamma>0.", f"{A2}",
  "CONFERE (postulado internamente coerente, com Γ>0 declarado explicitamente aqui pela primeira vez) ; CONFLITA COM Cap.1 §1.6/Cap.2 §2.7 (achado A2/lote 1) — esta é literalmente a citação \"Anexo H Postulado 5\" que o achado A2 menciona pelo nome como a segunda lei incompatível de η; elevada a postulado formal aqui, a incompatibilidade precisa de resolução editorial antes que a \"formalização canônica\" possa ser considerada fechada", False),
 ("AH", r"\eta(t) \text{ é monotônica crescente.}", "AH.06",
  "CONFERE (consequência lógica correta de AH.06, dado Γ>0; flag sem-delimitador — a extração capturou uma frase, não uma fórmula)", False),
 ("AH", r"\chi \to 0, \quad \eta \to 0, \quad r \to 1,", "—",
  "CONFERE (postulado razoável de recuperação de GR)", False),
 ("AH", r"3M_g^2 H^2 = \rho_m + \frac12\dot\chi^2 + U(\chi) + m^2M_{eff}^2F(\chi)\mathcal{V}(r).",
  f"Anexo E §E.3 (AE.04-06); {D3}",
  "CONFERE (consolidação correta — usa 𝒱(r) sem ξ, consistente com a forma corrigida da âncora D3/AA.30/AE.06)", False),
 ("AH", r"3M_f^2 H_f^2 = m^2M_{eff}^2F(\chi)\mathcal{U}(r).", "Anexo E §E.8 (AE.46-48)",
  "CONFERE (consolidação correta, consistente com AE.46-48/AB.50)", False),
 ("AH", r"(\beta_1 + 2\beta_2 r + \beta_3 r^2)(H - \xi H_f)=0.", "Anexo B §B.8",
  "CONFERE (reprise da constraint de Bianchi)", False),
 ("AH", r"\ddot\chi + 3H\dot\chi + U'(\chi) = m^2M_{eff}^2F'(\chi)V(\xi,r).", SINAL,
  "ERRO DE CÁLCULO (repete o erro de sinal de AH.05/AE.09/11 — âncoras D2/D8)", False),
 ("AH", r"\dot\eta = \Gamma \dot\chi^2.", f"AH.06; {A2}",
  "CONFERE (reprise de AH.06) ; CONFLITA COM Cap.1 §1.6/Cap.2 §2.7 — achado A2/lote 1", False),
 ("AH", r"m_T^2(t) = m^2F(\chi)\mu_T^2(r,\beta_n,M_g,M_f).", f"{D2}",
  "INCOMPLETA (mesma omissão de ξ de AF.06/Anexo F §F.3.2 — μ_T² deveria depender de ξ também, per a âncora D2/Anexo D §D.4/AD.09)", False),
 ("AH", r"m_T^2 \ge 2H^2.", "AH.14", "CONFERE (reprise do bound de Higuchi)", False),
 ("AH", r"H^2 = \frac{8\pi G}{3} \frac{\rho_m + \rho_\chi + \rho_{int}} {1-\eta}", f"Anexo E §E.7 (AE.39); {D4}",
  "NÃO-DERIVÁVEL — âncora D4, mesma pendência de AE.39/AG.05, aqui elevada a \"forma compacta final da teoria\" (H.6) — a formulação mais proeminente desta equação em todo o corpus; precisa ser reclassificada como extensão proposta (acoplamento não-mínimo Ω(η)R_g + constraint), válida no regime adiabático |η̇|≪H, antes de servir como resumo canônico da TDCP", False),
 ("AH", r"\rho_{int} = m^2M_{eff}^2F(\chi)\mathcal{V}(r), \quad \dot\eta=\Gamma\dot\chi^2.", f"AH.09; {A2}",
  "CONFERE (ρ_int=m²M_eff²F(χ)𝒱(r) consistente com a forma corrigida da âncora D3) ; CONFLITA COM Cap.1 §1.6/Cap.2 §2.7 (η̇=Γχ̇² — achado A2/lote 1, mesma nota de AH.06/13)", False),
]


def main():
    aplicados = 0
    problemas = []
    arquivos = ("AF", "AG", "AH")
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
