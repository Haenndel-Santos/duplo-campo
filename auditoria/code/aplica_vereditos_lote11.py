# -*- coding: utf-8 -*-
"""
aplica_vereditos_lote11.py — vereditos do Lote 11 (Anexos I+J+K, 38 eqs).
Linha de pesquisa exploratoria (nao integrada ao corpo F1) - usa
integration_assessment.md como ancora adicional (equivalente as D1-D8
para este territorio). Anexo L nao tem equacoes (0), nada a aplicar.
Casamento por substring; multi=True aplica a todas as ocorrencias
pendentes DENTRO DO MESMO ARQUIVO.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
REG = os.path.normpath(os.path.join(HERE, '..', 'registro'))

IA1 = "`integration_assessment.md` (Pergunta 1: g^(1)/g^(2) vs g/f)"
IA2 = "`integration_assessment.md` (Pergunta 2: L_int vs V(K))"
IA3 = "`integration_assessment.md` (Pergunta 3: Λ_ent vs η)"
IA4 = "`integration_assessment.md` (Pergunta 4: parâmetros paralelos)"

V = [
 # ================= AI (11) — colapso da função de onda primordial =================
 ("AI", r"\mid \Psi\rangle$$", "—",
  "CONFERE (notação padrão de mecânica quântica para o estado global — bem formada como objeto formal; ocorre duas vezes, §I.2 e §I.4, mesma nota)", True),
 ("AI", r"\mid \Psi\rangle = \alpha \mid g_{1}\rangle + \beta \mid g_{2}\rangle", IA1,
  f"NÃO-DERIVÁVEL — per {IA1}: o mecanismo de colapso |Ψ⟩=α|g1⟩+β|g2⟩ é uma construção de cosmologia quântica (tipo minisuperespaço/Wheeler-DeWitt) categoricamente distinta da ação clássica bimétrica dos Cap.2-5; nenhuma equação mostra como |Ψ⟩ se reduz a essa ação — a \"transição\" é afirmada narrativamente, não derivada; na melhor das hipóteses, é proposta de condição inicial pré-clássica, sem contato dinâmico com o formalismo já demonstrado", False),
 ("AI", r"t_{P} \approx 5.39 \times 10^{- 44}\text{ }s", "—",
  "CONFERE (valor padrão do tempo de Planck, importado, numericamente correto)", False),
 ("AI", r"g_{\mu\nu}^{(1)}", "—",
  f"CONFERE (notação — definição nominal da métrica pós-colapso; a identificação técnica com g do corpo F1 é avaliada em {IA1}: defensável apenas como reinterpretação narrativa, não como identificação técnica direta)", False),
 ("AI", r"g_{\mu\nu}^{(2)}", "AI.05",
  f"CONFERE (mesma nota de AI.05, para a segunda métrica pós-colapso — {IA1})", False),
 ("AI", r"\chi(x^{\mu})", "Cap.3 (campo estrutural)",
  f"CONFERE (nomeia o campo mediador — mesmo símbolo χ do corpo F1, usado aqui intencionalmente para sugerir o papel análogo, per {IA3})", False),
 ("AI", r"E = mc^{2}$$", "—",
  "CONFERE (relação padrão da relatividade restrita; ocorre duas vezes, §I.7 e §I.10, mesma nota)", True),
 ("AI", r"E_{tot} = E_{vac}^{(1)} + E_{vac}^{(2)} + E_{int}", "Cap.3 §3.4",
  f"CONFLITA COM Cap.3 §3.4 — per {IA1}: o tratamento simétrico de E_vac^(1) e E_vac^(2) (energia própria em AMBOS os domínios) conflita com a exigência estrutural do corpo F1 de que matéria/energia acopla apenas ao setor g (Cap.3 §3.4), da qual depende a contagem de graus de liberdade livre do fantasma de Boulware-Deser (Cap.6); acoplar energia a ambos os setores exigiria uma análise de fantasma própria que não existe em nenhum dos dois blocos", False),
 ("AI", r"M_{i} = \frac{E_{vac}^{(i)}}{c^{2}}", "AI.08, AI.09",
  "CONFERE (consequência algébrica trivial de AI.08, aplicada a cada domínio — mesma nota estrutural de AI.09 sobre o tratamento simétrico dos dois domínios)", False),

 # ================= AJ (11) — emaranhamento cosmológico e energia escura =================
 ("AJ", r"g_{\mu\nu}^{(1)} \quad \text{e} \quad g_{\mu\nu}^{(2)}", "Anexo I (AI.05/06)",
  "CONFERE (reprise da notação de AI.05/06)", False),
 ("AJ", r"\mid \Psi\rangle = \sum_{i} c_{i} \mid g_{1}^{(i)}\rangle \otimes \mid g_{2}^{(i)}\rangle", IA1,
  f"CONFERE SOB HIPÓTESE (forma padrão de estado emaranhado bipartido em QM — bem formada como objeto formal; mesma pendência do Apêndice I sobre a ponte com a ação clássica, nunca demonstrada, per {IA1})", False),
 ("AJ", r"S_{ent} = - Tr(\rho\ln\rho)", "—",
  "CONFERE (importada — entropia de von Neumann padrão, fórmula correta)", False),
 ("AJ", r"E_{tot} = E_{1} + E_{2} + E_{int}", "Anexo I (AI.09); Cap.3 §3.4",
  f"CONFLITA COM Cap.3 §3.4 — mesma nota de AI.09/{IA1} (tratamento simétrico de energia em ambos os domínios)", False),
 ("AJ", r"L_{int} = \lambda\chi\left( g_{\mu\nu}^{(1)}-g_{\mu\nu}^{(2)} \right)^{2}", IA2,
  f"NÃO-DERIVÁVEL — per {IA2}: a contração de índices de \"²\" não é especificada; na leitura mais natural (sem estrutura de traço explícita), o termo é ∝h_μνh^μν SEM a subtração −(h^μ_μ)² exigida pela combinação de Fierz-Pauli, a ÚNICA combinação quadrática que evita o sexto grau de liberdade fantasma no setor linear (Fierz-Pauli 1939/Hassan-Rosen 2011); se a contração for genérica, o termo reintroduz o fantasma de Boulware-Deser que a construção HR dos Cap.2-6 foi desenhada para eliminar — reconciliável com V(K)=Σβnen(K) apenas sob uma tunagem que o texto não verifica", False),
 ("AJ", r"$$\Lambda$$", "—",
  "CONFERE (notação padrão — constante cosmológica do modelo ΛCDM, citada para contraste)", False),
 ("AJ", r"\Lambda_{eff} = \Lambda_{0} + \Lambda_{ent}", IA3,
  f"CONFLITA COM Anexo E/H (η) — per {IA3}: Λ_eff é aditivo e Λ_ent não tem equação de movimento explícita (\"pode variar lentamente no tempo\" é qualitativo), ao contrário de η (η̇=Γχ̇², Anexo E/H), que é multiplicativo (fator 1/(1−η) sobre ρ_tot) e tem equação de movimento bem definida; Λ_ent, tal como escrita, é uma afirmação qualitativa sem conteúdo dinâmico verificável", False),
 ("AJ", r"\square h_{\mu\nu}^{(1)} + m_{g}^{2}h_{\mu\nu}^{(1)} = \kappa h_{\mu\nu}^{(2)}", "Anexo D (âncora D2)",
  "NÃO-DERIVÁVEL (forma assumida por analogia, sem derivação a partir de uma ação; estruturalmente parecida com o setor tensorial bimétrico real, onde a âncora D2 mostra que o termo de massa/mistura deve ter uma forma muito específica — proporcional a (h-ℓ)² — para evitar patologias; aqui κ é introduzido livremente, sem verificação de que a estrutura evita fantasma/gradiente, mesmo padrão de risco já identificado para L_int)", False),
 ("AJ", r"\ddot{\delta} + 2H\dot{\delta} = 4\pi G_{eff}\rho\delta", "Cap.8/Cap.18 (lotes 2/4)",
  "CONFERE (mesma forma padrão já confirmada no Cap.8/Cap.18 — lotes 2/4 — com G_eff no lugar de Gμ)", False),
 ("AJ", r"G_{eff} = G(1 + \epsilon)", "âncora D6",
  f"NÃO-DERIVÁVEL (ε é um parâmetro livre não conectado à estrutura μ(k,a) real derivada para o corpo F1 — âncora D6: μ real é multi-polo e depende de escala k, não uma constante (1+ε); mesmo padrão apontado em {IA4}: \"dois conjuntos de observáveis paralelos, não uma previsão unificada\")", False),
 ("AJ", r"w(z) \neq - 1", "—",
  "CONFERE (previsão qualitativa genérica — comum a qualquer modelo de energia escura dinâmica, não específica desta construção)", False),

 # ================= AK (16) — previsões observacionais =================
 ("AK", r"w = - 1", "—", "CONFERE (padrão, ΛCDM, citado para contraste)", False),
 ("AK", r"\rho_{DE} = \rho_{\Lambda} + \rho_{\chi}", "—",
  f"CONFERE SOB HIPÓTESE (parametrização razoável em si, mas não conectada à estrutura real de ρ_int(r) do corpo F1 — mesmo padrão de parâmetros paralelos, {IA4})", False),
 ("AK", r"w(z) = - 1 + \epsilon(z)", "—",
  "CONFERE (parametrização padrão de energia escura dinâmica, forma genérica — tipo CPL)", False),
 ("AK", r"\mid w + 1 \mid \sim 10^{- 2} - 10^{- 3}", "—",
  "NÃO-DERIVÁVEL (previsão numérica sem cálculo mostrado a partir de nenhum parâmetro do modelo — nem os da linha exploratória (χ,S_ent) nem os do corpo F1, m_S0/α0/p/q)", False),
 ("AK", r"\ddot{\delta} + 2H\dot{\delta} = 4\pi G_{eff}\rho_{m}\delta", "Anexo J (AJ.09)",
  "CONFERE (mesma forma padrão já confirmada, reprise de AJ.09/Cap.8/Cap.18)", False),
 ("AK", r"G_{eff} = G(1 + \alpha)", "Anexo J (AJ.10); âncora D6",
  "NÃO-DERIVÁVEL (mesma nota de AJ.10 — α não conectado à estrutura μ(k,a) real da âncora D6)", False),
 ("AK", r"f(z) = \Omega_{m}(z)^{\gamma}", "—",
  "CONFERE (importada — parametrização padrão do índice de crescimento γ, Peebles/Linder 2005)", False),
 ("AK", r"$$\gamma \approx 0.55$$", "—",
  "CONFERE (valor padrão de ΛCDM, aproximadamente correto — literatura dá γ≈0.545-0.55)", False),
 ("AK", r"\gamma \approx 0.55 + \Delta\gamma", "AK.08",
  "CONFERE SOB HIPÓTESE (parametrização razoável, mas Δγ não é calculado a partir de nenhuma estrutura derivada)", False),
 ("AK", r"\Delta\gamma \sim 0.01", "AK.09",
  "NÃO-DERIVÁVEL (previsão numérica sem cálculo mostrado, mesma nota de AK.04)", False),
 ("AK", r"P(k) = P_{0}(k)\left( 1 + \eta\sin(k/k_{*}) \right)", "—",
  "NÃO-DERIVÁVEL (forma fenomenológica assumida, sem cálculo mostrado a partir de S_ent ou de qualquer parâmetro derivado); NOVA sobrecarga de símbolo: η aqui é amplitude de modulação do espectro de potência primordial — um TERCEIRO uso de η no corpus, distinto do η de separação estrutural acumulada (Cap.1/Anexo E/H, achado A2) e do η_slip (Cap.18)", False),
 ("AK", r"(\square - m_{g}^{2})h_{\mu\nu} = \kappa h_{\mu\nu}^{(2)}", "Anexo J (AJ.08); âncora D2",
  "NÃO-DERIVÁVEL (mesma nota de AJ.08 — forma assumida por analogia, sem derivação a partir de uma ação; κ introduzido livremente sem verificação de ausência de patologia)", False),
 ("AK", r"\omega^{2} = k^{2} + m_{g}^{2}", "AK.12",
  "CONFERE (relação de dispersão padrão de um campo massivo, consequência trivial da parte homogênea de AK.12 — ω²=k²+m² para □h+m²h=0)", False),
 ("AK", r"m_{g} \sim 10^{- 33} - 10^{- 30}\text{ eV}", "Cap.19 (faixa m_S0~30-300H0)",
  "CONFERE SOB HIPÓTESE (ordem de grandeza plausível — comparável a m∼H0 até ∼10³H0, mesma faixa usada como benchmark no corpo F1 principal, Cap.19 — mas não é calculada aqui a partir de nenhum parâmetro desta linha exploratória, apenas citada)", False),
 ("AK", r"P(k) = P_{\Lambda CDM}(k)\left( 1+\xi e^{- k/k_{c}} \right)", "âncoras D1-D8 (ξ estrutural)",
  "NÃO-DERIVÁVEL (forma fenomenológica assumida); NOVA sobrecarga de símbolo — grave: ξ aqui é a intensidade de um termo de correlação no espectro de matéria, colidindo com ξ=N_f/N_g, a variável estrutural central de todo o corpo F1 (usada em todas as âncoras D1-D8); mesma classe de problema do achado E6/lote 4 (ξ reaproveitado em Cap.20)", False),
 ("AK", r"H_{0}^{TDCP} > H_{0}^{\Lambda CDM}", "—",
  "CONFERE (previsão qualitativa razoável em espírito — energia escura dinâmica tardia pode geralmente deslocar H0 inferido; não quantificada aqui)", False),
]


def main():
    aplicados = 0
    problemas = []
    arquivos = ("AI", "AJ", "AK")
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
