# -*- coding: utf-8 -*-
"""
extrai_formulas.py — gera o esqueleto do Registro de Formulas da
auditoria matematica da TDCP.

Varre manuscript/capitulos/*.md e manuscript/apendices/*.md, extrai
todas as equacoes em destaque (linhas iniciadas por $, $$, "> $" ou
por LaTeX cru sem delimitador — artefato de conversao), atribui IDs
estaveis ([C05.03] = 3a equacao do Cap.5; [AB.07] = 7a do Anexo B;
[C06E.NN] = Cap.6.2) e escreve:

  auditoria/registro/<PREFIXO>.md   (um por capitulo/anexo)
  auditoria/registro_formulas.md    (indice-mestre com estatisticas)

Cada entrada traz: a formula, a secao, o contexto imediato, uma CLASSE
SUGERIDA por heuristica textual (a confirmar na auditoria) e campos
"Depende de"/"Veredito" a preencher.

POLITICA DE SOBRESCRITA: o script NAO sobrescreve um registro ja
existente (para nao apagar classificacoes/vereditos manuais). Use
--force para regenerar tudo do zero.

Uso:  python extrai_formulas.py [--force]
"""
import os
import re
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
MAN = os.path.normpath(os.path.join(HERE, '..', '..', 'manuscript'))
REG = os.path.normpath(os.path.join(HERE, '..', 'registro'))
INDEX = os.path.normpath(os.path.join(HERE, '..', 'registro_formulas.md'))


# ----------------------------------------------------------------------
# arquivos e prefixos (ordem de leitura da teoria)
# ----------------------------------------------------------------------
def lista_arquivos():
    out = []
    for n in range(1, 27):
        out.append((f"C{n:02d}", os.path.join(MAN, 'capitulos', f'Cap.{n}.md'),
                    f"Capítulo {n}"))
        if n == 6:
            out.append(("C06E", os.path.join(MAN, 'capitulos', 'Cap.6.2.md'),
                        "Capítulo 6 (versão expandida — Cap.6.2)"))
    for letra in 'ABCDEFGHIJKL':
        out.append((f"A{letra}",
                    os.path.join(MAN, 'apendices', f'Appendix-{letra}.md'),
                    f"Anexo {letra}"))
    return [(p, f, tt) for p, f, tt in out if os.path.exists(f)]


# ----------------------------------------------------------------------
# extracao
# ----------------------------------------------------------------------
RE_HEADER = re.compile(r'^\*\*(.+?)\*\*\s*$')
RE_EQ_START = re.compile(r'^(?:>\s*)?\$')
RE_LATEX_CRU = re.compile(r'^\\[A-Za-z]')


def extrai_equacoes(path):
    """Retorna lista de dicts {eq, secao, antes, depois, linha, flags}."""
    with open(path, encoding='utf-8') as fh:
        linhas = fh.read().splitlines()

    eqs = []
    secao = "(inicio do arquivo)"
    i = 0
    while i < len(linhas):
        ln = linhas[i]
        s = ln.strip()
        m = RE_HEADER.match(s)
        if m and not RE_EQ_START.match(s):
            secao = m.group(1)
            i += 1
            continue
        flags = []
        eq_txt = None
        if RE_EQ_START.match(s):
            corpo = s.lstrip('> ').strip()
            if corpo.startswith('$$') and not (len(corpo) > 2
                                               and corpo.rstrip().endswith('$$')):
                # bloco $$ de varias linhas
                bloco = [corpo]
                j = i + 1
                while j < len(linhas) and not linhas[j].strip().endswith('$$'):
                    bloco.append(linhas[j].strip())
                    j += 1
                if j < len(linhas):
                    bloco.append(linhas[j].strip())
                eq_txt = ' '.join(bloco)
                i = j
            else:
                eq_txt = corpo
            if s.startswith('>'):
                flags.append('em-citacao')
        elif RE_LATEX_CRU.match(s):
            eq_txt = s
            flags.append('sem-delimitador')

        if eq_txt is not None:
            antes = []
            j = i - 1
            while j >= 0 and len(antes) < 2:
                sj = linhas[j].strip()
                if sj and not RE_EQ_START.match(sj) and not RE_LATEX_CRU.match(sj):
                    antes.insert(0, sj)
                if sj and (RE_EQ_START.match(sj) or RE_LATEX_CRU.match(sj)):
                    antes.insert(0, "[equação anterior]")
                j -= 1
            depois = ""
            j = i + 1
            while j < len(linhas):
                sj = linhas[j].strip()
                if sj:
                    depois = ("[equação seguinte]"
                              if (RE_EQ_START.match(sj) or RE_LATEX_CRU.match(sj))
                              else sj)
                    break
                j += 1
            eqs.append(dict(eq=eq_txt, secao=secao, antes=antes,
                            depois=depois, linha=i + 1, flags=flags))
        i += 1
    return eqs


# ----------------------------------------------------------------------
# classificacao heuristica (sugerida — a confirmar na auditoria)
# ----------------------------------------------------------------------
def _norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    return ''.join(c for c in s if unicodedata.category(c) != 'Mn')


CUES_DEF = ['defini', 'denotamos', 'chamamos', 'notacao', 'convencao',
            'representa', 'e dado por', 'e dada por', 'introduzimos']
CUES_POST = ['postulado', 'axioma', 'principio', 'assumimos', 'impomos que']
CUES_DERIV = ['logo', 'portanto', 'entao', 'obtemos', 'obtem-se', 'temos',
              'resulta', 'substituindo', 'derivando', 'integrando',
              'expandindo', 'dividindo', 'segue', 'fica', 'vira',
              'multiplicando', 'isolando', 'somando', 'tomando',
              'aplicando', 'combinando', 'usando', 'inserindo',
              'chegamos', 'implica', 'reduz-se', 'reescrev', 'variacao']
CUES_AFIRM = ['tipicamente', 'forma tipica', 'assume forma',
              'assume a forma', 'pode ser escrit', 'representativa',
              'ansatz', 'parametriz', 'aproximadamente', 'esquematic',
              'forma geral', 'toma forma', 'tem a forma', 'do tipo',
              'estrutura geral', 'algo como', 'em geral', 'comum']
CUES_IMPORT = ['hassan', 'rosen', 'higuchi', 'literatura', 'padrao',
               'usual', 'conhecid', 'classic', 'bunch', 'davies',
               'lcdm', 'na gr', 'em gr', 'gr:', 'relatividade geral',
               'modelo padrao']


def classifica(eq, antes):
    ctx1 = _norm(antes[-1]) if antes else ''
    ctx2 = _norm(' '.join(antes))
    eqn = _norm(eq)
    tem_igual = ('=' in eq and '\\neq' not in eq)
    desigualdade = any(x in eq for x in ('>', '<', '\\ge', '\\le',
                                         '\\gg', '\\ll', '\\gtrsim',
                                         '\\lesssim'))
    if desigualdade and not tem_igual:
        return 'condicao/vinculo'
    for c in CUES_POST:
        if c in ctx2:
            return 'postulado'
    for c in CUES_DEF:
        if c in ctx1:
            return 'definicao'
    if '\\equiv' in eq:
        return 'definicao'
    for c in CUES_DERIV:
        if c in ctx1:
            return 'derivada-no-texto'
    for c in CUES_AFIRM:
        if c in ctx2 or c in eqn:
            return 'afirmada-sem-derivacao'
    if '\\sim' in eq or '\\propto' in eq or '\\approx' in eq:
        return 'afirmada-sem-derivacao'
    for c in CUES_IMPORT:
        if c in ctx2:
            return 'importada-da-literatura'
    return 'pendente'


# ----------------------------------------------------------------------
# escrita
# ----------------------------------------------------------------------
def escreve_registro(prefixo, titulo, relpath, eqs):
    caminho = os.path.join(REG, f'{prefixo}.md')
    with open(caminho, 'w', encoding='utf-8') as fh:
        fh.write(f"# Registro de Fórmulas — {titulo}\n\n")
        fh.write(f"Fonte: `{relpath}` — {len(eqs)} equações em destaque.\n\n")
        fh.write("Classes sugeridas por heurística textual — **confirmar "
                 "na auditoria**. Preencher `Depende de` (IDs) e "
                 "`Veredito` durante o passe sequencial.\n\n---\n\n")
        for n, e in enumerate(eqs, 1):
            eid = f"{prefixo}.{n:02d}"
            fh.write(f"### [{eid}]  (linha {e['linha']})\n\n")
            fh.write(f"```\n{e['eq']}\n```\n\n")
            fh.write(f"- **Seção:** {e['secao']}\n")
            if e['antes']:
                fh.write(f"- **Contexto:** …{' / '.join(e['antes'])}\n")
            if e['depois']:
                fh.write(f"- **Segue:** {e['depois'][:120]}\n")
            if e['flags']:
                fh.write(f"- **Flags:** {', '.join(e['flags'])}\n")
            fh.write(f"- **Classe (sugerida):** {e['classe']}\n")
            fh.write("- **Depende de:** _(a preencher)_\n")
            fh.write("- **Veredito:** _(pendente)_\n\n")
    return caminho


def main():
    force = '--force' in sys.argv
    os.makedirs(REG, exist_ok=True)
    ja = [f for f in os.listdir(REG) if f.endswith('.md')]
    if ja and not force:
        print(f"[!] {len(ja)} registros ja existem em {REG}.")
        print("    O script nao sobrescreve (protege edicoes manuais).")
        print("    Use --force para regenerar TUDO do zero.")
        sys.exit(1)

    arquivos = lista_arquivos()
    stats = []
    classes_tot = {}
    total = 0
    for prefixo, path, titulo in arquivos:
        eqs = extrai_equacoes(path)
        for e in eqs:
            e['classe'] = classifica(e['eq'], e['antes'])
            classes_tot[e['classe']] = classes_tot.get(e['classe'], 0) + 1
        rel = os.path.relpath(path, os.path.join(MAN, '..')).replace('\\', '/')
        escreve_registro(prefixo, titulo, rel, eqs)
        stats.append((prefixo, titulo, len(eqs)))
        total += len(eqs)
        print(f"  {prefixo:5s} {len(eqs):4d} eqs  <- {rel}")

    with open(INDEX, 'w', encoding='utf-8') as fh:
        fh.write("""# Registro de Fórmulas — Índice-Mestre da Auditoria

**O que é:** catálogo de todas as equações em destaque do corpus
(capítulos + anexos), com ID estável, contexto, classe e campos de
dependência/veredito. É a base do passe de auditoria sequencial:
cada fórmula será verificada **apenas contra o que vem antes dela**
na ordem de leitura.

**Gerado por:** `auditoria/code/extrai_formulas.py` (não re-rodar sem
`--force`; o script protege edições manuais). As classes vêm de
heurística textual e são **sugestões a confirmar**.

## Esquema de IDs

- `[Cnn.mm]` — mm-ésima equação do Capítulo nn (ex.: `[C05.03]`)
- `[C06E.mm]` — Cap.6.2 (versão expandida do Cap.6)
- `[Ax.mm]` — Anexo x (ex.: `[AB.07]` = 7ª equação do Anexo B)

## Taxonomia de classes

| Classe | Significado |
|---|---|
| `definicao` | introduz símbolo/quantidade; audita-se consistência e não-sobrecarga |
| `postulado` | assumida como princípio; audita-se coerência com o resto |
| `derivada-no-texto` | o texto afirma obtê-la de equações anteriores; audita-se a conta |
| `afirmada-sem-derivacao` | declarada por analogia/"forma típica"; audita-se se é derivável |
| `condicao/vinculo` | desigualdade/critério de estabilidade; audita-se a origem |
| `importada-da-literatura` | resultado padrão externo; audita-se a transcrição |
| `pendente` | heurística não decidiu; classificar na auditoria |

## Taxonomia de vereditos (preencher no passe de auditoria)

`CONFERE` · `CONFERE SOB HIPÓTESE (qual)` · `ERRO DE CÁLCULO (correção)`
· `NÃO-DERIVÁVEL (o que falta)` · `CONFLITA COM [ID]` ·
`ARTEFATO DE CONVERSÃO`

## Âncoras já auditadas (Derivações 1–8)

As fórmulas cobertas pelas derivações do diretório `derivations/`
apontam para lá em vez de refazer: D3 (ρ_int/regra da cadeia),
D4 (Friedmann com 1/(1−η)), D5 (ṙ no ramo dinâmico), D2 (setor
tensorial), D7 (modo σ_k), D1/D6/D8 (em andamento).

## Estatísticas

""")
        fh.write(f"**Total: {total} equações** em {len(arquivos)} arquivos.\n\n")
        fh.write("| Prefixo | Fonte | Equações |\n|---|---|---|\n")
        for prefixo, titulo, n in stats:
            fh.write(f"| {prefixo} | {titulo} | {n} |\n")
        fh.write("\n**Classes sugeridas (heurística):**\n\n")
        fh.write("| Classe | Quantidade |\n|---|---|\n")
        for c, n in sorted(classes_tot.items(), key=lambda x: -x[1]):
            fh.write(f"| {c} | {n} |\n")
        fh.write("\n## Progresso da auditoria\n\n")
        fh.write("| Lote | Status |\n|---|---|\n")
        fh.write("| Registro extraído | feito |\n")
        fh.write("| Classificação revisada | pendente |\n")
        fh.write("| Regras de auditoria (regras_de_auditoria.md) | pendente |\n")
        fh.write("| Passes sequenciais C01–C26, AA–AL | pendente |\n")

    print(f"\nTOTAL: {total} equacoes registradas.")
    print(f"Indice: {INDEX}")


if __name__ == '__main__':
    main()
