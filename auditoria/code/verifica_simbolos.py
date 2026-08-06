# -*- coding: utf-8 -*-
"""
verifica_simbolos.py — Gate 0 do plano de reconstrucao v2.

Verifica o corpus contra o dicionario normativo
(docs/dicionario_simbolos.md): nenhum simbolo reservado pode carregar
um segundo significado.

Limitacao honesta: significado nao esta na sintaxe. O script NAO
adivinha o que um simbolo quer dizer. Ele faz duas coisas que sao
mecanicamente decidiveis:

  (1) DETECCAO DE VIOLACAO CONHECIDA — para cada colisao documentada
      pela auditoria, um padrao regex que casa com o *uso errado*
      especifico. Zero falsos negativos para o que ja conhecemos.

  (2) INVENTARIO — lista todo simbolo LaTeX usado, com frequencia e
      arquivos, para revisao humana de colisoes ainda nao catalogadas.

Uso:
    python verifica_simbolos.py              # corpus v1 (linha de base)
    python verifica_simbolos.py --alvo v2    # corpus v2, quando existir
    python verifica_simbolos.py --inventario # + inventario completo
"""
import argparse
import os
import re
import sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.normpath(os.path.join(HERE, '..', '..'))

ALVOS = {
    'v1': [
        os.path.join(RAIZ, 'manuscript', 'capitulos'),
        os.path.join(RAIZ, 'manuscript', 'apendices'),
    ],
    'v2': [
        os.path.join(RAIZ, 'manuscript-v2'),
    ],
}

# ---------------------------------------------------------------------
# (1a) COLISOES: simbolo com DOIS significados no mesmo corpus.
#      Ambiguidade genuina — o uso errado precisa ser renomeado.
#      (simbolo, regex do uso ERRADO, descricao, renomeacao exigida)
# ---------------------------------------------------------------------
COLISOES = [
    ("r", r"r\s*=\s*\\frac\{P_T\}",
     "r como razao tensor-escalar (colide com r=b/a)", "r_T"),
    ("r", r"r\s*\\approx\s*r_\{?\\text\{inflaton",
     "r como razao tensor-escalar (colide com r=b/a)", "r_T"),
    ("xi", r"F\(\\phi\)\s*=\s*1\s*\+\s*\\xi",
     "xi como acoplamento em F(phi) (colide com xi=N_f/N_g)", "lambda_F"),
    ("xi", r"1\s*\+\s*\\xi\s*e\^\{?\s*-\s*k",
     "xi como intensidade de correlacao em P(k) (colide com xi=N_f/N_g)", "A_c"),
    ("eta", r"1\s*\+\s*\\eta\s*\\sin",
     "eta como amplitude de modulacao em P(k) (colide com eta estrutural)",
     "A_mod"),
    ("U", r"U\(r\)\s*(\\equiv|=)\s*\\beta_0",
     "U(r) combinacao dos beta_n (colide com U(phi) potencial)", "V_g(r)"),
    ("U", r"\\tilde\s*U\(r\)\s*=\s*\\beta_4",
     "U~(r) combinacao do setor f (colide com U(phi) potencial)", "V_f(r)"),
    ("zeta", r"\\zeta\s*=\s*\\frac\{\\delta\\rho\}",
     "zeta = delta-rho/(rho+p) (colide com zeta curvatura)",
     "escrever por extenso"),
    ("zeta", r"\\frac\{\\rho_g\s*\\Psi_g\s*\+\s*\\rho_f\s*\\Psi_f\}",
     "zeta como media ponderada bimetrica (colide com zeta curvatura)",
     "zeta_b"),
    ("S", r"S\s*\\propto\s*\\Psi_f\s*-\s*\\Psi_g",
     "S como modo de isocurvatura (colide com S da acao)", "S_iso"),
    # --- colisao DESCOBERTA por este script, ausente da lista dos 8 da
    #     auditoria: chi e campo escalar E distancia comovel (Cap.23/25).
    #     Aqui so se flagra o uso como CAMPO; o uso como distancia
    #     (d\chi, \chi_max, \chi_*, W(\chi)) e padrao e permanece.
    ("chi", r"(?:[FUV]\(\\chi\)|\\dot\{?\\chi\}?|\\delta\\chi|"
            r"\\rho_\\chi|p_\\chi|S_\\chi|\\bar\{?\\chi\}?|"
            r"\\chi\(t\)|\\chi\(x\^)",
     "chi como campo escalar (colide com chi = distancia comovel, Cap.23/25)",
     "phi_- (v2 aposenta chi como campo)"),
]

# ---------------------------------------------------------------------
# (1b) BLOQUEIOS: simbolo cuja definicao depende de um gate ainda aberto.
#      Nao e ambiguidade de notacao — e fisica nao decidida.
# ---------------------------------------------------------------------
BLOQUEIOS = [
    ("eta/Gamma", r"\\dot\{?\\eta\}?\s*=\s*\\Gamma\s*\(H_1\s*-\s*H_2\)\^2",
     "lei de eta #1: [Gamma]=massa^-1", "Gate 9"),
    ("eta/Gamma", r"\\dot\{?\\eta\}?\s*=\s*\\Gamma\s*\\dot\{?\\chi\}?\^2",
     "lei de eta #2: [Gamma]=massa^-3 — incompativel com #1", "Gate 9"),
]

# ---------------------------------------------------------------------
# (1c) ERROS DE ALGEBRA rastreados pela auditoria (nao sao notacao)
# ---------------------------------------------------------------------
ALGEBRA = [
    ("Sigma",
     r"\\Sigma\(k,a\)\s*(?:=|\\approx)\s*\\frac\{\\mu[^}]*\}\{2\}"
     r"[^$]*?\\eta_\{\\rm slip\}\^\{-1\}",
     "Sigma com eta_slip INVERTIDO (correto: (mu/2)(1+eta_slip))",
     "corrigir a algebra"),
    ("Phi/Psi", r"ds_g\^2\s*=\s*-\(1\s*\+\s*2\\Phi\(r\)\)",
     "convencao invertida: Phi temporal (padrao v2: Psi temporal)",
     "inverter para Psi temporal"),
]

# simbolos reservados que exigem forma tipografica especifica
TIPOGRAFIA = [
    (r"(?<!\\mathcal\s)(?<!\\mathcal)\bK\s*=\s*\\sqrt\{g\^\{-1\}f\}",
     "matriz raiz de HR deve ser \\mathcal{K} (K romano = matriz cinetica)"),
]

SIMBOLO_RE = re.compile(r"\\([A-Za-z]+)")
MATH_RE = re.compile(r"\$\$?(.+?)\$\$?", re.DOTALL)


def arquivos(alvo):
    saida = []
    for d in ALVOS[alvo]:
        if not os.path.isdir(d):
            continue
        for nome in sorted(os.listdir(d)):
            if nome.endswith('.md'):
                saida.append(os.path.join(d, nome))
    return saida


def rel(caminho):
    return os.path.relpath(caminho, RAIZ).replace('\\', '/')


def varre(alvo, mostrar_inventario):
    fichs = arquivos(alvo)
    if not fichs:
        print(f"[!] nenhum arquivo .md encontrado para o alvo '{alvo}'.")
        if alvo == 'v2':
            print("    (esperado — o corpus v2 ainda nao existe)")
        return 0

    grupos = {
        'COLISOES': (COLISOES, defaultdict(list)),
        'BLOQUEIOS': (BLOQUEIOS, defaultdict(list)),
        'ALGEBRA': (ALGEBRA, defaultdict(list)),
    }
    tipografia = defaultdict(list)
    inventario = Counter()
    inv_arquivos = defaultdict(set)

    for caminho in fichs:
        with open(caminho, encoding='utf-8') as fh:
            texto = fh.read()

        for nome, (regras, achados) in grupos.items():
            for regra in regras:
                if nome == 'BLOQUEIOS':
                    simbolo, padrao, descricao, correcao = regra
                else:
                    simbolo, padrao, descricao, correcao = regra
                for m in re.finditer(padrao, texto):
                    linha = texto[:m.start()].count('\n') + 1
                    achados[(simbolo, descricao, correcao)].append(
                        (rel(caminho), linha))

        for padrao, descricao in TIPOGRAFIA:
            for m in re.finditer(padrao, texto):
                linha = texto[:m.start()].count('\n') + 1
                tipografia[("tipografia", descricao, "usar \\mathcal{K}")]\
                    .append((rel(caminho), linha))

        if mostrar_inventario:
            for bloco in MATH_RE.findall(texto):
                for s in SIMBOLO_RE.findall(bloco):
                    inventario[s] += 1
                    inv_arquivos[s].add(os.path.basename(caminho))

    TITULOS = {
        'COLISOES': 'COLISOES (simbolo com dois significados)',
        'BLOQUEIOS': 'BLOQUEIOS (definicao depende de gate aberto)',
        'ALGEBRA': 'ERROS DE ALGEBRA rastreados pela auditoria',
    }

    print(f"=== Gate 0 — verificacao de simbolos (alvo: {alvo}) ===")
    print(f"arquivos varridos: {len(fichs)}\n")

    total_tipos = sum(len(a) for _, a in grupos.values()) + len(tipografia)

    for nome, (_, achados) in grupos.items():
        if not achados:
            continue
        n_oc = sum(len(v) for v in achados.values())
        print(f"--- {TITULOS[nome]}: {len(achados)} tipos, "
              f"{n_oc} ocorrencias ---\n")
        for (simbolo, descricao, correcao), locais in sorted(
                achados.items(), key=lambda kv: -len(kv[1])):
            print(f"  [{simbolo}] {descricao}")
            print(f"      -> exigido: {correcao}")
            for arq, ln in locais[:5]:
                print(f"         {arq}:{ln}")
            if len(locais) > 5:
                print(f"         ... e mais {len(locais)-5} ocorrencia(s)")
            print()

    if tipografia:
        print(f"--- TIPOGRAFIA: {len(tipografia)} tipos ---\n")
        for (_, descricao, correcao), locais in tipografia.items():
            print(f"  {descricao}")
            print(f"      -> exigido: {correcao}")
            for arq, ln in locais[:5]:
                print(f"         {arq}:{ln}")
            print()

    if total_tipos == 0:
        print("NENHUMA VIOLACAO CONHECIDA. Gate 0: PASSA.")
    else:
        print(f"Gate 0: NAO PASSA — {total_tipos} tipos de violacao.")

    resultado = total_tipos

    if mostrar_inventario:
        print("\n=== Inventario de simbolos (revisao humana) ===")
        print("Simbolos em >=4 arquivos distintos — candidatos a colisao:\n")
        for s, n in inventario.most_common():
            arqs = inv_arquivos[s]
            if len(arqs) >= 4:
                print(f"  \\{s:<16} {n:>5} usos em {len(arqs):>2} arquivos")

    return resultado


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--alvo', default='v1', choices=sorted(ALVOS))
    ap.add_argument('--inventario', action='store_true')
    args = ap.parse_args()
    n = varre(args.alvo, args.inventario)
    sys.exit(1 if n else 0)


if __name__ == '__main__':
    main()
