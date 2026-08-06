# -*- coding: utf-8 -*-
"""
aplica_vereditos_lote06.py — vereditos do Lote 6 (Anexo A / AA).
Casamento por substring; multi=True aplica a todas as ocorrencias
pendentes DENTRO DO MESMO ARQUIVO.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
REG = os.path.normpath(os.path.join(HERE, '..', 'registro'))

D3 = "âncora D3 (derivations/03_dV_dNg_regra_cadeia.md)"

V = [
 ("AA", r"g_{\mu\nu}, \quad f_{\mu\nu}.", "—",
  "CONFERE (definição básica, consistente com todo o corpus desde Cap.3)", False),
 ("AA", r"S = \frac{M_g^2}{2}\int d^4x\,\sqrt{-g}\,R[g] + \frac{M_f^2}{2}\int d^4x\,\sqrt{-f}\,R[f] - m^2 M_{\mathrm{eff}}^2 \int d^4x\,\sqrt{-g}\,V(\mathcal{K}) + S_m.",
  "Cap.3/Cap.14/Cap.20 (reprises já confirmadas)",
  "CONFERE (ação HR completa — mesma estrutura já confirmada em todo o corpus desde Cap.3; NOTA: esta é a definição que sana a pendência do achado A4/lote 1 — o prefator m²M_eff² aqui, não m² isolado, é a origem do fator M_eff²/M_g² esperado nas equações de campo após variação)", False),
 ("AA", r"M_{\mathrm{eff}}^{-2} = M_g^{-2} + M_f^{-2}.", "—",
  "CONFERE (importada — definição padrão de M_eff em gravidade bimétrica de Hassan-Rosen)", False),
 ("AA", r"V(\mathcal{K}) = \sum_{n=0}^4 \beta_n e_n(\mathcal{K}),", "—",
  "CONFERE (reprise — estrutura já usada em todo o corpus)", False),
 ("AA", r"\mathcal{K}^\mu_{\ \nu} = \left(\sqrt{g^{-1}f}\right)^\mu_{\ \nu}.", "—",
  "CONFERE (definição padrão de K como raiz matricial)", False),
 ("AA", r"(g^{-1}f)^\mu_{\ \nu} = g^{\mu\alpha} f_{\alpha\nu}.", "—",
  "CONFERE (definição algébrica direta)", False),
 ("AA", r"\mathcal{K}^\mu_{\ \alpha}\mathcal{K}^\alpha_{\ \nu} = (g^{-1}f)^\mu_{\ \nu}.", "AA.05/06",
  "CONFERE (definição da raiz matricial — consistente com AA.05)", False),
 ("AA", r"e_0 = 1,", "—", "CONFERE (definição padrão de polinômio simétrico elementar)", False),
 ("AA", r"e_1 = \sum_i \lambda_i = [\mathcal{K}],", "—",
  "CONFERE (definição padrão)", False),
 ("AA", r"e_2 = \sum_{i<j} \lambda_i \lambda_j,", "—", "CONFERE (definição padrão)", False),
 ("AA", r"e_3 = \sum_{i<j<k} \lambda_i \lambda_j \lambda_k,", "—", "CONFERE (definição padrão)", False),
 ("AA", r"e_4 = \prod_i \lambda_i = \det \mathcal{K}.", "—", "CONFERE (definição padrão)", False),
 ("AA", r"e_1 = [\mathcal{K}],", "AA.09",
  "CONFERE (reprise em forma de traço)", False),
 ("AA", r"e_2 = \frac12\left([\mathcal{K}]^2 - [\mathcal{K}^2]\right),", "—",
  "CONFERE (verificado: identidade de Newton padrão e2=(p1²-p2)/2, com p1=[K], p2=[K²] — forma correta)", False),
 ("AA", r"e_3 = \frac16\left([\mathcal{K}]^3 - 3[\mathcal{K}][\mathcal{K}^2] + 2[\mathcal{K}^3]\right),", "—",
  "CONFERE (verificado: identidade de Newton padrão e3=(p1³-3p1p2+2p3)/6 — forma correta)", False),
 ("AA", r"e_4 = \det \mathcal{K}.", "AA.12",
  "CONFERE (reprise)", False),
 ("AA", r"[\mathcal{K}] = \mathcal{K}^\mu_{\ \mu}.", "—",
  "CONFERE (definição padrão de traço)", False),
 ("AA", r"ds_g^2 = -N_g^2 dt^2 + a^2 \delta_{ij} dx^i dx^j,", "—",
  "CONFERE (ansatz FLRW padrão com lapse)", False),
 ("AA", r"ds_f^2 = -N_f^2 dt^2 + b^2 \delta_{ij} dx^i dx^j.", "—",
  "CONFERE (ansatz FLRW padrão com lapse)", False),
 ("AA", r"(g^{-1}f)^0_{\ 0} = \frac{N_f^2}{N_g^2},", "AA.18/19",
  "CONFERE (álgebra verificada: g^00 f_00 = (-1/N_g²)(-N_f²) = N_f²/N_g² ✓)", False),
 ("AA", r"(g^{-1}f)^i_{\ j} = \frac{b^2}{a^2}\delta^i_j.", "AA.18/19",
  "CONFERE (álgebra verificada: g^ij f_kj = (δ^ik/a²)(b²δ_kj) = (b²/a²)δ^i_j ✓)", False),
 ("AA", r"\mathcal{K}^\mu_{\ \nu} = \mathrm{diag}(\xi, r, r, r),", "AA.20/21/23",
  "CONFERE (consequência da raiz quadrada de uma matriz diagonal com entradas positivas — consistente com AA.23)", False),
 ("AA", r"\xi = \frac{N_f}{N_g}, \quad r = \frac{b}{a}.", "—",
  "CONFERE (definições fundamentais de ξ e r — consistentes com todo o corpus; esta é a definição canônica que os capítulos posteriores citam, ex. Cap.14 §14.2)", False),
 ("AA", r"e_1 = \xi + 3r,", "AA.09, AA.22/23",
  "CONFERE (álgebra verificada: e1=ξ+r+r+r=ξ+3r — mesmos valores já confirmados em Cap.14 §14.2/lote 3)", False),
 ("AA", r"e_2 = 3\xi r + 3r^2,", "AA.10, AA.22/23",
  "CONFERE (álgebra verificada: pares (ξ,r)×3 + (r,r)×3 = 3ξr+3r² ✓)", False),
 ("AA", r"e_3 = 3\xi r^2 + r^3,", "AA.11, AA.22/23",
  "CONFERE (álgebra verificada: triplas (ξ,r,r)×3 + (r,r,r)×1 = 3ξr²+r³ ✓)", False),
 ("AA", r"e_4 = \xi r^3.", "AA.12, AA.22/23",
  "CONFERE (álgebra verificada: ξ·r·r·r=ξr³ ✓)", False),
 ("AA", r"V(\xi,r) = \beta_0 + \beta_1(\xi+3r) + \beta_2(3\xi r+3r^2) + \beta_3(3\xi r^2+r^3) + \beta_4(\xi r^3).",
  "AA.04, AA.24-27",
  "CONFERE (substituição direta e correta de AA.24-27 em V=Σβn·en)", False),
 ("AA", r"\rho_{int}^{(g)} = - \frac{1}{\sqrt{-g}} \frac{\delta}{\delta g^{00}} \left( \sqrt{-g}V \right).",
  "—",
  "CONFERE SOB HIPÓTESE (técnica padrão de extrair densidade efetiva via derivada funcional em g^00, análoga à definição de T_00 a partir da ação de matéria; prescrição operacional razoável, não uma definição de livro-texto único)", False),
 ("AA", r"\rho_{int}^{(g)} = m^2 M_{eff}^2 (\beta_0 + 3\beta_1 r + 3\beta_2 r^2 + \beta_3 r^3).",
  f"{D3}; Cap.14 §F.3 (confirmado no lote 3)",
  "CONFERE — âncora D3: verificada explicitamente por regra da cadeia completa (ξ e β4 cancelam exatamente ao converter ∂V/∂N_g em ρ_int); esta é a forma CORRETA que o Anexo B §B.5 erra ao tentar reproduzir; mesma quantidade já confirmada nos capítulos principais (Cap.14 §14.7/F.3, lote 3)", False),
]


def main():
    aplicados = 0
    problemas = []
    arquivos = ("AA",)
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
