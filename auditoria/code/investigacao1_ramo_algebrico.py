# -*- coding: utf-8 -*-
"""
investigacao1_ramo_algebrico.py — Investigacao 1 da fila pos-Erratum 01
(docs/veredito_setor_escalar_final.md item 3.4), com o G1-b embutido
(docs/gate1_identidade_relacional.md).

CONTEXTO. O erratum corrigiu o SEGUNDO fator (cinematico) da constraint
de Bianchi, de (H_g - xi H_f) para (N_f adot - N_g bdot). O "ramo
dinamico" foi reavaliado (ramo_dinamico_correto.py, d1_ramo_finito.py,
evolucao_temporal_escalar.py): fundo saudavel, Higuchi automatico, mas
setor escalar com taquiao eterno (docs/resultado_setor_escalar.md) —
sobrevive a beta_n constante em todo o espaco varrido
(docs/no_go_beta_constante.md) e a modulacao beta_1(phi_-)
(docs/veredito_setor_escalar_final.md).

O RAMO ALGEBRICO (B(r)=beta_1+2 beta_2 r=0, r=r_star CONSTANTE) e a
OUTRA raiz da constraint fatorada e NUNCA foi reavaliado com a forma
corrigida — e o item 3.4 do veredito consolidado, "generinamente
aberto", barato. Pre-erratum (benchmark C da D1, script
derivations/code/01_setor_escalar_K_Omega.py), a raiz exata mostrou
DEGENERESCENCIA CINETICA (kN ~ 1e-16): o par relativo fica quase
desacoplado, nao-propagante na ordem quadratica.

PARTE 1 responde (a) e (b) do prompt:
  (a) o que "estar no ramo algebrico" significa agora — ver a nota
      impressa abaixo (o erratum NAO muda a definicao do ramo: B(r) e
      o PRIMEIRO fator, intocado; com beta_n CONSTANTE o residuo do
      Gate 2 [-M_eff^2 m^2 p_phi beta_1'] se anula identicamente, pois
      beta_1'=0 — a constraint continua fatorando de forma limpa);
  (b) a degenerescencia cinetica na raiz exata persiste no formalismo
      corrigido? existe corredor saudavel perto-da-raiz? — varredura
      de kN em funcao da distancia a r_star.

PARTE 2 e o G1-b (protocolo do docs/gate1_identidade_relacional.md
secao 4): projetar os autovetores de TODOS os modos (sadios e
patologicos) em delta-phi_- (campo 'dchi', indice 6 na ordem de campos
da D1) e nas direcoes metricas-relativas (complemento ortogonal), no
PONTO FIXO do ramo finito (mesmo fundo do no-go: docs/no_go_beta_constante.md,
auditoria/code/modulacao_qep.py, secao "fundo_a10"), beta_n CONSTANTES
(sem modulacao), mu em {0.1,0.3,1,3,10}, k=1 E k=10.
  R1 passa se |<v_patologico, dchi>|^2 < 0.05 em toda a varredura;
  R1 falha se algum modo patologico for dchi-dominado.

Reusa integralmente: derivations/code/tdcp_pert_lib.py (biblioteca de
perturbacoes) e derivations/code/01_setor_escalar_K_Omega.py (montagem
da Lagrangiana quadratica 7x7, QEP numerico, auto-teste GR) — mesma
maquinaria de todas as ancoras da familia D1/no-go. A geracao do fundo
do ponto fixo (fundo_a10) e uma copia inline da funcao homonima de
auditoria/code/modulacao_qep.py (nao importada como modulo porque esse
script executa a varredura completa do no-go no top-level ao ser
importado).

Requer sympy, numpy, scipy. Demora alguns minutos (montagem simbolica
7x7 e reusada uma unica vez; depois, ~70 resolucoes de QEP numerico,
rapidas).
Uso (da raiz do repo, com o venv ativo):
    python auditoria/code/investigacao1_ramo_algebrico.py
Saida tambem salva em auditoria/code/out/investigacao1_ramo_algebrico.txt
"""
import importlib.util
import os
import sys
import time

import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
DCODE = os.path.normpath(os.path.join(HERE, '..', '..', 'derivations', 'code'))
sys.path.insert(0, DCODE)

spec = importlib.util.spec_from_file_location(
    "d1mod", os.path.join(DCODE, "01_setor_escalar_K_Omega.py"))
d1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(d1)

from tdcp_pert_lib import (a_s, b_s, xi_s, H_s, Hf_s, Hd_s, Hfd_s, xid_s,
                           chid_s, chidd_s, Mg2, Mf2, m2, Meff2,
                           b0, b1, b2, b3, b4, Fb, Fp, Fpp,
                           Ub, Up, Upp, rho_s, k as ksym,
                           quadratic_matrices, benchmark)

T0 = time.time()
OUT = []


def say(*a):
    line = " ".join(str(x) for x in a)
    print(f"[{time.time()-T0:7.1f}s] {line}")
    OUT.append(line)


FIELDS_NAMES = ['Phi_g', 'B_g', 'Phi_f', 'Psi_f', 'B_f', 'E_f', 'dchi']
IDX_DCHI = 6
TOL_SIG = 0.05      # taxa Im(omega)/H acima disso = taquiao
TOL_KN = 1e-9        # kN abaixo de -isto = fantasma
TOL_R1 = 0.05        # criterio do G1-b: |<v,dchi>|^2 < 0.05 p/ passar


# ------------------------------------------------------------------
# montagem simbolica — uma unica vez, reusa a maquinaria da D1
# ------------------------------------------------------------------
say("=" * 72)
say("INVESTIGACAO 1 — ramo algebrico pos-Erratum 01 (+ G1-b embutido)")
say("=" * 72)

gr_ok = d1.gr_selfcheck()
if not gr_ok:
    say("[!] auto-teste GR falhou — abortando leitura dos resultados")
    sys.exit(1)

L2s, fields, vels = d1.build_L2()
say("[montagem] blocos simbolicos K,C,W (7x7) ...")
K7, C7, W7 = quadratic_matrices(L2s, fields, vels)
nomes_reais = [str(f) for f in fields]
if nomes_reais != FIELDS_NAMES:
    raise RuntimeError(f"ordem de campos mudou: {nomes_reais} != {FIELDS_NAMES}")
say(f"    campos (ordem): {FIELDS_NAMES}  [dchi = delta-phi_- no indice {IDX_DCHI}]")


def classifica(w2, kN, H_val):
    om = np.sqrt(complex(w2))
    taxa = abs(om.imag) / H_val if H_val else float('nan')
    if taxa > TOL_SIG:
        return 'TAQUIAO', taxa
    if kN < -TOL_KN:
        return 'FANTASMA', taxa
    return 'limpo', taxa


def espectro_anotado(Kn, Cn, Wn, H_val, label, coletor=None):
    """QEP + classificacao de saude + projecao em dchi (indice 6) p/ TODOS
    os modos. Se coletor (lista) for dado, acrescenta um dict por modo."""
    pares = d1.agrupa_pares(d1.qep_modes(Kn, Cn, Wn))
    pares.sort(key=lambda m: abs(m['omega2']))
    say(f"  {label}")
    for mm in pares:
        w2 = mm['omega2']
        kN = mm['knorm']
        v = mm['v']
        nv2 = float(np.real(np.vdot(v, v)))     # ~1 (v ja normalizado)
        p_dchi = float(np.real(v[IDX_DCHI] * np.conjugate(v[IDX_DCHI]))) / nv2
        p_metric = 1.0 - p_dchi
        classe, taxa = classifica(w2, kN, H_val)
        imag_flag = '' if abs(w2.imag) < 1e-6 * max(1.0, abs(w2.real)) \
            else f'  Im(w2)={w2.imag:+.2e}'
        say(f"    w2={w2.real:+.4e}{imag_flag}  kN={kN:+.3e}  "
            f"Im(w)/H={taxa:8.4f}  [{classe:8s}]  "
            f"|<v,dchi>|^2={p_dchi:.4f}  |<v,metrica>|^2={p_metric:.4f}")
        if coletor is not None:
            coletor.append(dict(classe=classe, taxa=taxa, kN=kN, p_dchi=p_dchi))
    return pares


# ==================================================================
# PARTE 1 — RAMO ALGEBRICO: r = r_star exato + corredor
# ==================================================================
say("")
say("-" * 72)
say("PARTE 1 — ramo algebrico (B(r_star)=0, r=const) pos-erratum")
say("-" * 72)
say("")
say("(a) O que muda na definicao do ramo — NADA na algebra do ramo em")
say("    si. B(r) = beta_1 + 2 beta_2 r (familia F1, beta_3=0) e o")
say("    PRIMEIRO fator da constraint fatorada; o erratum corrigiu o")
say("    SEGUNDO fator, de (H_g - xi H_f) para (N_f adot - N_g bdot).")
say("    No ramo algebrico B(r_star)=0 anula a constraint MULTIPLICANDO")
say("    o segundo fator, qualquer que seja a forma dele — a definicao")
say("    do ramo (r=r_star=-beta_1/(2 beta_2)) e a mesma antes e depois")
say("    do erratum.")
say("    Com beta_n CONSTANTE (o caso desta investigacao), beta_1'=0,")
say("    entao o residuo do Gate 2 (-M_eff^2 m^2 p_phi beta_1') se anula")
say("    IDENTICAMENTE — a constraint continua fatorando de forma limpa")
say("    neste ramo, sem a complicacao que a modulacao introduziria.")
say("    Identidade cinematica do ramo (nao mudou com o erratum): r=")
say("    const => bdot/b=adot/a => xi=N_f/N_g=H_g/H_f. Esta e EXATAMENTE")
say("    a formula que o corpus v1 usava, de forma errada, como")
say("    constraint GERAL do 'ramo dinamico' (o que produziu rdot=0")
say("    'sempre' — Erratum 01). O erratum nao a invalida: ele mostra")
say("    que ela e a identidade cinematica CORRETA, mas so NESTE ramo")
say("    (algebrico), nao no ramo geral. tdcp_pert_lib.benchmark() ja")
say("    monta xi = H/H_f a partir da Friedmann f — e o valor NATURAL")
say("    aqui, sem overrides arbitrarios (ao contrario do benchmark C")
say("    original da D1, que fixava xi=1 manualmente 'de controle').")

b1v, b2v = benchmark()[b1], benchmark()[b2]
r_star = float(-b1v / (2 * b2v))
say(f"    r_star = -beta_1/(2 beta_2) = {r_star:.6f}  "
    f"(beta_1={float(b1v)}, beta_2={float(b2v)} — params do benchmark padrao)")

say("")
say("(b) degenerescencia cinetica na raiz exata + corredor.")
say("    CAVEAT declarado: delta != 0 usa o MESMO xi=H/H_f do benchmark,")
say("    que so e a identidade cinematica CORRETA exatamente em delta=0")
say("    (r=r_star). Fora da raiz isto e uma sonda MATEMATICA de kN em")
say("    funcao da distancia (nao uma trajetoria fisica autoconsistente")
say("    — essa e o ramo finito, ja mapeado em resultado_setor_escalar.md,")
say("    que para estes betas nunca chega perto de r_star=1.25, pois")
say("    r_infinito~0.33 la). O que se testa aqui e puramente estrutural:")
say("    a degenerescencia e um fenomeno localizado em B(r)~0, e quao")
say("    largo e o corredor onde ela desaparece.")
say("")

DELTAS = [-0.30, -0.20, -0.10, -0.04, -0.01, -0.002, 0.0,
          0.002, 0.01, 0.04, 0.10, 0.20, 0.30]
KCORR = [1.0, 10.0, 100.0]

say(f"    {'delta':>7} {'r':>9} {'B(r)':>10} " +
    "  ".join(f"kN_min(k={kv:g})".rjust(16) for kv in KCORR) +
    "   classes(k=1,10,100)")
corredor = []
delta_limpo = None
for delta in DELTAS:
    vb = benchmark(sp.nsimplify(delta))
    vb[Ub] = vb[Ub] + vb[rho_s]
    vb[rho_s] = sp.Integer(0)
    rv = float(vb[b_s] / vb[a_s])
    Br = float(b1v + 2 * b2v * rv)
    Hv = float(vb[H_s])
    kNs = []
    classes_kv = []
    for kv in KCORR:
        subs = dict(vb)
        subs[ksym] = sp.Rational(kv)
        Kn = d1.to_numpy(K7, subs)
        Cn = d1.to_numpy(C7, subs)
        Wn = d1.to_numpy(W7, subs)
        pares = d1.agrupa_pares(d1.qep_modes(Kn, Cn, Wn))
        kNs.append(min(p['knorm'] for p in pares))
        classes = {classifica(p['omega2'], p['knorm'], Hv)[0] for p in pares}
        classes_kv.append('limpo' if classes == {'limpo'} else '/'.join(sorted(classes)))
    todo_limpo = all(c == 'limpo' for c in classes_kv)
    if todo_limpo and delta_limpo is None:
        delta_limpo = delta
    corredor.append((delta, rv, Br, kNs, classes_kv))
    say(f"    {delta:+7.3f} {rv:9.4f} {Br:+10.4f} " +
        "  ".join(f"{v:+16.3e}" for v in kNs) +
        "   " + ",".join(classes_kv))

say("")
say("    Detalhe espectral NA RAIZ EXATA (delta=0), k=1,10,100:")
vb0 = benchmark(sp.Integer(0))
vb0[Ub] = vb0[Ub] + vb0[rho_s]
vb0[rho_s] = sp.Integer(0)
H0 = float(vb0[H_s])
for kv in KCORR:
    subs = dict(vb0)
    subs[ksym] = sp.Rational(kv)
    Kn = d1.to_numpy(K7, subs)
    Cn = d1.to_numpy(C7, subs)
    Wn = d1.to_numpy(W7, subs)
    espectro_anotado(Kn, Cn, Wn, H0, f"raiz exata (delta=0), k={kv:g}")

say("")
say("    Detalhe espectral NAS BORDAS do corredor (delta=+-0.30), k=1:")
for delta in (-0.30, 0.30):
    vb = benchmark(sp.nsimplify(delta))
    vb[Ub] = vb[Ub] + vb[rho_s]
    vb[rho_s] = sp.Integer(0)
    Hd = float(vb[H_s])
    subs = dict(vb)
    subs[ksym] = sp.Rational(1)
    Kn = d1.to_numpy(K7, subs)
    Cn = d1.to_numpy(C7, subs)
    Wn = d1.to_numpy(W7, subs)
    espectro_anotado(Kn, Cn, Wn, Hd, f"delta={delta:+.2f}, k=1")

kN_root = min(abs(v) for v in corredor[len(DELTAS) // 2][3])  # delta=0 esta no meio
kN_edge = min(abs(v) for pair in (corredor[0], corredor[-1]) for v in pair[3])
say("")
say(f"    LEITURA (b) — MAGNITUDE: |kN|_min na raiz exata ~ {kN_root:.3e}; "
    f"|kN|_min nas bordas do corredor ~ {kN_edge:.3e}.")
say("    A magnitude por si so NAO decide 'corredor saudavel': kN deixar de")
say("    ser numericamente degenerado (~0) nao significa o espectro ficar")
say("    limpo — o mesmo modo pode continuar taquionico ou fantasma com kN")
say("    finito. O criterio real e a coluna 'classes' da tabela acima:")
if delta_limpo is not None:
    say(f"    [ACHADO] delta={delta_limpo:+.3f} tem TODOS os modos 'limpo' em "
        f"k=1,10,100 — corredor saudavel EXISTE nesta varredura.")
else:
    say("    [ACHADO] NENHUM delta testado tem os tres k simultaneamente")
    say("    'limpo' — em toda a faixa escaneada (delta em "
        f"[{DELTAS[0]:+.2f},{DELTAS[-1]:+.2f}]) sobra pelo menos um modo")
    say("    taquionico e/ou fantasma. Sair da raiz exata cura a")
    say("    DEGENERESCENCIA CINETICA (kN deixa de ser ~0) mas NAO cura a")
    say("    PATOLOGIA (taquiao e/ou fantasma persistem) — nao ha corredor")
    say("    saudavel nesta faixa. O ramo algebrico reprova tanto NA raiz")
    say("    (degenerado E taquionico) quanto PERTO dela (nao-degenerado")
    say("    mas ainda doente).")


# ==================================================================
# PARTE 2 — G1-b: projecao em delta-phi_- no ponto fixo do ramo finito
# ==================================================================
say("")
say("-" * 72)
say("PARTE 2 — G1-b: |<v,delta-phi_->|^2 no ponto fixo, beta_n constante")
say("-" * 72)
say("    Protocolo (docs/gate1_identidade_relacional.md secao 4):")
say("    R1 passa se |<v_patologico,dchi>|^2 < 0.05 em toda a varredura")
say("    (mu in {0.1,0.3,1,3,10}, ponto fixo, k=1 E k=10); falha se algum")
say("    modo patologico for dchi-dominado.")
say("")

RHO_M0 = 0.3
B1_0, B2_V, B0_V, B4_V = 1.0, -0.4, 1.0, 0.5   # mesma REF do no-go/modulacao_qep


def fundo_a10(B1e, B2v, B0v, B4v, mu):
    """Fundo do ponto fixo (a=10), copia inline de modulacao_qep.py —
    nao importado como modulo pois aquele script roda a varredura
    completa do no-go no top-level ao ser carregado."""
    kap = 1.0 / mu
    meff2 = mu / (1.0 + mu)
    a = 10.0
    rho_til = RHO_M0 * a**-3 / meff2
    rr = np.roots([kap * B4v - 3 * B2v, -3 * B1e,
                   3 * kap * B2v - B0v - rho_til, kap * B1e])
    r_esc = max(1e-14, 1e-6 * kap * B1e / max(rho_til, 1.0))
    reais = sorted(z.real for z in rr
                   if abs(z.imag) < 1e-9 and z.real > r_esc)
    if not reais:
        return None
    r = reais[0]
    dW = kap * (2 * B4v * r - B1e / r**2) - 3 * B1e - 6 * B2v * r
    drdN = -3.0 * rho_til / dW
    xi = r + drdN
    Vf = B4v + 3 * B2v / r**2 + B1e / r**3
    H2 = meff2 * r * r * Vf / (3.0 * mu)
    if H2 <= 0 or xi <= 0:
        return None
    H = np.sqrt(H2)
    rho_int = meff2 * (B0v + 3 * B1e * r + 3 * B2v * r**2)
    return r, xi, H, H / r, 3.0 * H2 - rho_int, a, r * a


MUS = [0.1, 0.3, 1.0, 3.0, 10.0]
KG1B = [1.0, 10.0]

FIXOS_SUBS = {chid_s: 0, chidd_s: 0, rho_s: 0, Hd_s: 0, Hfd_s: 0, xid_s: 0,
              Fb: 1, Fp: 0, Fpp: 0, Mg2: 1, m2: 1,
              b0: B0_V, b1: B1_0, b2: B2_V, b3: 0, b4: B4_V,
              Up: 0, Upp: sp.Rational(3, 10)}

todos_modos = []       # coletor global p/ o veredito final
violacoes = []


def roda_celula(mu, B1e, B2v, B0v, B4v, tag):
    f = fundo_a10(B1e, B2v, B0v, B4v, mu)
    if f is None:
        say(f"  mu={mu} [{tag}]: fundo invalido (H^2<=0 ou xi<=0) — pulando")
        return
    r, xi, H, Hf, Ubv, a, bb = f
    meff2 = mu / (1.0 + mu)
    say("")
    say(f"  mu={mu} [{tag}]  (beta1={B1e}, beta2={B2v}, r={r:.6f}, "
        f"xi={xi:.6f}, H={H:.6f}, Mf2={mu}, Meff2={meff2:.6f})")
    subs_base = dict(FIXOS_SUBS)
    subs_base.update({b1: B1e, b2: B2v, b0: B0v, b4: B4v})
    for kv in KG1B:
        subs = dict(subs_base)
        subs.update({a_s: sp.Float(a), b_s: sp.Float(bb), xi_s: sp.Float(xi),
                     H_s: sp.Float(H), Hf_s: sp.Float(Hf), Ub: sp.Float(Ubv),
                     Mf2: sp.Float(mu), Meff2: sp.Float(meff2),
                     ksym: sp.Rational(kv)})
        Kn = d1.to_numpy(K7, subs)
        Cn = d1.to_numpy(C7, subs)
        Wn = d1.to_numpy(W7, subs)
        modos_kv = []
        espectro_anotado(Kn, Cn, Wn, H, f"    k={kv:g}", coletor=modos_kv)
        for mm in modos_kv:
            mm.update(mu=mu, k=kv, tag=tag)
            todos_modos.append(mm)
            if mm['classe'] in ('TAQUIAO', 'FANTASMA') and mm['p_dchi'] >= TOL_R1:
                violacoes.append(mm)


for mu in MUS:
    roda_celula(mu, B1_0, B2_V, B0_V, B4_V, "REF")

say("")
say("  mu=0.1 na celula REF (1,-0.4) nao tem fundo valido (acima) — a")
say("  celula REF simplesmente nao alcanca um ponto fixo fisico ali.")
say("  Cobertura completa do protocolo (mu=0.1 tem de entrar na varredura):")
say("  reusando a celula da 'fresta' de docs/no_go_beta_constante.md /")
say("  modulacao_qep.py ETAPA 2 (beta1=0.2, beta2=-1.0), onde mu=0.1 TEM")
say("  fundo valido e hospeda o fantasma quase-nulo (kN~-1.6e-5) — a")
say("  familia de patologia estruturalmente DIFERENTE do dubleto de")
say("  shifts (mu>=0.3): la e o lapso Phi_f puro (estrutura_par_relativo.md).")
roda_celula(0.1, 0.2, -1.0, B0_V, B4_V, "fresta mu=0.1 (0.2,-1.0)")

# ------------------------------------------------------------------
# veredito do G1-b
# ------------------------------------------------------------------
say("")
say("=" * 72)
say("VEREDITO G1-b")
say("=" * 72)
patologicos = [m for m in todos_modos if m['classe'] in ('TAQUIAO', 'FANTASMA')]
say(f"  modos patologicos encontrados na varredura: {len(patologicos)}")
if patologicos:
    p_max = max(m['p_dchi'] for m in patologicos)
    say(f"  max |<v_patologico,dchi>|^2 na varredura = {p_max:.4f}  "
        f"(criterio: < {TOL_R1})")
else:
    say("  nenhum modo patologico encontrado nesta varredura — inesperado")
    say("  dado o no-go ja estabelecido; VERIFICAR antes de interpretar R1.")

if violacoes:
    say("")
    say(f"  R1 FALHA — {len(violacoes)} modo(s) patologico(s) dchi-dominado(s):")
    for mm in violacoes:
        say(f"    mu={mm['mu']} [{mm['tag']}], k={mm['k']}: classe={mm['classe']}, "
            f"|<v,dchi>|^2={mm['p_dchi']:.4f}")
    say("")
    say("  => a doenca alcanca o grau primordial mesmo dentro da F1;")
    say("     o trilema (docs/gate1_identidade_relacional.md sec.3) colapsa")
    say("     para os ramos (b)/(c) diretamente.")
elif patologicos:
    say("")
    say(f"  R1 PASSA — todos os {len(patologicos)} modos patologicos tem")
    say(f"  |<v,dchi>|^2 < {TOL_R1} em toda a varredura (mu, k=1 e k=10).")
    say("  => a patologia e espectadora de delta-phi_-: o no-go e sobre a")
    say("     REPRESENTACAO (setor de vinculos da F1), nao sobre o grau")
    say("     relacional primordial. Consistente com o suporte de nivel 2b")
    say("     ja existente (docs/estrutura_par_relativo.md: dubleto de")
    say("     shifts / lapso Phi_f, delta-phi_- desacoplado com F'=0).")

say("")
say("=" * 72)
say("RESUMO PARA O PROXIMO PASSO")
say("=" * 72)
say("  Parte 1(b): ver a razao |kN|_bordas/|kN|_raiz acima — decide se o")
say("  ramo algebrico tem corredor saudavel ou degenerescencia estrutural.")
say("  Parte 2 (G1-b): ver veredito acima. Se G1-b PASSAR e o ramo")
say("  algebrico tambem REPROVAR (sem corredor saudavel a ponto de")
say("  competir com o ramo finito), R1 vira o enquadramento oficial do")
say("  no-go (docs/gate1_identidade_relacional.md secao 5, item 4).")
say("  G1-a (tabela documental) e G1-c (nota do trilema) seguem depois,")
say("  fora deste script.")

os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
with open(os.path.join(HERE, "out", "investigacao1_ramo_algebrico.txt"),
          "w", encoding="utf-8") as fh:
    fh.write("\n".join(OUT))
say("")
say("concluido. saida em auditoria/code/out/investigacao1_ramo_algebrico.txt")
