# -*- coding: utf-8 -*-
"""
r13b_ibb_ramo_infinito.py -- MEDICAO do ramo infinito em celulas IBB.

Contexto. O corpus excluia o ramo infinito porque xi cruza zero. O R-12i
(docs/resultado_r12i_confronto_konnig.md sec.1.6) derrubou esse argumento:
o quique de b e' tratado e defendido como FISICO pela fonte primaria
(1407.4331 secs. II e VI). A saida esta REABERTA. Surgiu um argumento
independente candidato, de outra natureza (Konnig 2015, arXiv:1503.07436):
saude de Higuchi em universo em expansao exigiria r' > 0, enquanto o ramo
infinito tem r' < 0.

ESTE SCRIPT MEDE. Ele NAO conclui exclusao nem aprovacao do IBB.

=======================================================================
CRITERIOS PRE-DECLARADOS (escritos ANTES da execucao -- regra 2, cap.02)
=======================================================================

O veredito sai SO por estes criterios. Nada mais e' interpretado.

--- GATES DE MAQUINARIA (se qualquer um falhar, NAO ha' medicao) ------

  M1  SELECAO DE RAMO. Para toda celula, o r(N) selecionado satisfaz
      SIMULTANEAMENTE:
        (a) r(a_min) / r(a_max) >= 1e2            (r grande no passado)
        (b) dr/dN < 0 em 100% dos pontos da grade (decrescente)
        (c) |r(a_min) / r_assint - 1| <= 1e-2, com
            r_assint = sqrt(mu*rho_til/beta_4)    (assintota do ramo inf.)
        (d) r(a_max) converge para r_c = MAIOR raiz positiva de W(r)=0,
            com |r(a_max)/r_c - 1| <= 5e-2
        (e) r_c e' estritamente a maior das raizes positivas de W(r)=0
      Falha em qualquer item => celula MARCADA COMO NAO-MEDIDA.

  M2  CONSISTENCIA DAS DUAS FRIEDMANN. Sobre a raiz selecionada, as
      Friedmann F.3 (setor g) e F.4 (setor f) do plano_derivacoes
      concordam com |H2_g/H2_f - 1| <= 1e-10 em todos os pontos.

  M3  RESIDUO DA CUBICA. |W(r) - rho_til| / max(1,|rho_til|) <= 1e-12
      em todos os pontos.

  M4  REGRA 6 -- DERIVADA. dr/dN e' calculado em FORMA FECHADA
      (dr/dN = -3*rho_til / W'(r), exata, ver sec. "forma fechada"),
      e cross-checado por estencil central de 8a ORDEM em DOIS passos
      h = 1e-3 e h = 3e-4 sobre N. Exigencias:
        (a) |d8(h1) - d8(h2)| / |dr/dN| <= 1e-8   (refino estavel)
        (b) |d8 - fechada|  / |dr/dN|   <= 1e-8   (canais concordam)
      np.gradient NAO e' usado em lugar nenhum deste script.

  M5  CONTROLE POSITIVO (regra 3 -- auto-teste de poder). A maquinaria
      tem de reproduzir o que o repositorio JA' SABE sobre o ramo
      FINITO (docs/resultado_ramo_finito.md secs. 1-3), no benchmark
      (beta_0,beta_1,beta_2,beta_3,beta_4) = (1, 1, -0.4, 0, 0.5),
      M_g^2=M_f^2=1, m^2=1, rho_m0=0.3, a em [1e-2, 10^0.3]:
        (a) xi > 0 em toda a historia
        (b) r cresce de ~0 ate' r_inf = 0.33 +- 0.01
        (c) primordial: dr/dN = 3r com erro relativo <= 1e-2
        (d) m_T^2/H^2 = 12.00 +- 0.05 em a = 0.02
        (e) Higuchi (m_T^2 >= 2H^2) em 400/400 pontos
      Falha em qualquer item => a maquinaria NAO e' confiavel para o
      ramo infinito e o script para sem emitir medicao.

  M6  PODER DO GATE DE HIGUCHI (regra 3). O gate tem de conseguir
      REPROVAR um caso sabidamente falso: o fundo da D8/D2 sec.3.4
      (r=1.2, xi=3.497, beta_2=-0.4), onde m_T^2 = -3.19 < 0. Se o
      gate aprovar esse ponto, ele nao tem poder e nada que ele
      aprovar pode ser interpretado.

      ** EMENDA DECLARADA (pos-1a execucao, registrada, nao escondida) **
      O criterio original acima exigia bater o valor -3.19 a +-0.05.
      A 1a execucao REPROVOU esse item: a nossa forma fechada da'
      m_T^2 = -1.5944, exatamente METADE de -3.19. Causa localizada e
      demonstrada abaixo no proprio script: derivations/02 sec.3.4
      avaliou o numero com M_eff^2 = 1, enquanto
      auditoria/code/ramo_dinamico_correto.py (e este script) usam
      M_eff^2 = 1/(1/M_g^2 + 1/M_f^2) = 0.5 para M_g^2 = M_f^2 = 1.
      E' uma inconsistencia de NORMALIZACAO entre dois documentos do
      corpus, nao um erro de fisica: o fator estrutural
      beta_1+beta_2(xi+r) = -0.8788 bate com o -0.88 declarado, o
      SINAL e' o mesmo, e m_T^2/H^2 (a unica quantidade que este
      script interpreta) e' INVARIANTE por M_eff^2 -- provado e
      testado na secao [INVARIANCIA]. O criterio M6 passa a exigir:
        (a) m_T^2 < 0 (o gate reprova o caso falso)   -- substancia
        (b) fator estrutural = -0.88 +- 0.005          -- forma
        (c) reproduzir -3.19 +- 0.05 SE M_eff^2 = 1    -- rastro
      Ficam registrados os dois valores e a causa.

  M7  FRONTEIRA DE EXISTENCIA. A condicao de existencia do ponto fixo
      tardio do ramo infinito, derivada em forma fechada neste script
      (beta_4/beta_1 < 2*mu^{3/2}, com mu = M_f^2/M_g^2), tem de bater
      com a varredura numerica de raizes em <= 1e-6, e tem de
      reproduzir o intervalo 0 < beta_4 < 2*beta_1 da fonte em mu = 1.

--- O QUE E' MEDIDO (nao ha' criterio de "passa/nao passa" aqui) -----

  Para cada celula IBB genuina (beta_2 = beta_3 = 0, beta_1 > 0,
  0 < beta_4 < 2*beta_1 na normalizacao da fonte), ao longo da
  historia, sao REPORTADOS:

    R1  sinal de r' = dr/dN: fracao de pontos com r' < 0, r' > 0, r'=0
    R2  o a onde xi = r + dr/dN cruza zero (e se cruza)
    R3  m_T^2/H^2 pela forma fechada do cap. 06 / derivations/02,
        com beta_2 = beta_3 = 0
    R4  a inequacao DO REPOSITORIO, m_T^2 >= 2H^2: fracao de pontos
        que a satisfazem, e o maximo de m_T^2/H^2 na historia
    R5  sinal de m_T^2 (taquion tensorial ou nao)

--- CEGUEIRA DO GATE (regra 7, obrigatoria) --------------------------

  ESTE TESTE MEDE Higuchi/helicidade-0 e o setor TENSORIAL.
  ELE NAO MEDE GRADIENTE. Se o IBB passar aqui, isso NAO diz nada
  sobre c_s^2 la' -- e vice-versa.

  Cegueiras adicionais, declaradas:
   - nao mede fantasma escalar (autovalores de K_2) neste fundo;
   - nao mede c_s^2 (a instabilidade de gradiente de classe do R-11
     foi medida no ramo FINITO; nada aqui a transporta para o infinito);
   - nao mede validade EFT, screening, f*sigma_8;
   - nao mede a helicidade-0 fora do limite de de Sitter: a cota
     m_T^2 >= 2H^2 e' a cota de Higuchi de de Sitter, que e' a forma
     que o repositorio usa hoje; a forma correta em bigravidade com
     fundo dinamico e' objeto do R-13a e NAO e' calculada aqui;
   - nao compara com o criterio DA FONTE (1503.07436). Essa comparacao
     depende da extracao em docs/resultado_r13a_criterio_higuchi_fonte.md,
     que e' outro processo. Se o arquivo nao existir, a comparacao fica
     DECLARADA COMO PENDENTE e NAO e' simulada.

--- A ARMADILHA, NOMEADA --------------------------------------------

  auditoria/code/ramo_dinamico_correto.py seleciona a MENOR raiz
  positiva da cubica (funcao resolve_r, r_ref=None -> rr[0]). Essa e'
  a selecao do ramo FINITO e e' ERRADA para o ramo infinito. Este
  script usa SELECAO POR CONTINUACAO (raiz mais proxima da anterior),
  semeada pela assintota r ~ sqrt(mu*rho_til/beta_4) no passado
  profundo e caminhando PARA O FUTURO -- a licao do R-8b
  (docs/resultado_r8b_limite_mH0.md sec.1;
   manuscript-v2/05_fundo_ramo_finito.md sec.1, nota numerica).
  O gate M1 verifica explicitamente que estamos no ramo infinito.

=======================================================================
FORMA FECHADA (o que este script usa, com a fonte de cada equacao)
=======================================================================

Convencoes: M_g^2 = 1, mu = M_f^2 / M_g^2 = M_f^2,
            M_eff^2 = 1/(1/M_g^2 + 1/M_f^2) = mu/(1+mu),
            N = ln a, ' = d/dN, xi = r + dr/dN (convencao do projeto).

  V_g(r) = b0 + 3 b1 r + 3 b2 r^2 + b3 r^3           [F.3]
  V_f(r) = b4 + 3 b3 /r + 3 b2 /r^2 + b1 /r^3        [F.4]

  Friedmann g:  3 M_g^2 H^2 = rho + m^2 M_eff^2 V_g(r)
  Friedmann f:  3 M_f^2 H^2 / r^2 = m^2 M_eff^2 V_f(r)   (H_f = H/r)

  Eliminando H^2:  m^2 M_eff^2 W(r) = rho,
      W(r) = (M_g^2/M_f^2) r^2 V_f(r) - V_g(r)
           = (1/mu)(b4 r^2 + 3 b3 r + 3 b2 + b1/r) - (b0+3b1 r+3b2 r^2+b3 r^3)

  ** dr/dN em FORMA FECHADA ** (regra 6). Derivando W(r(N)) = rho_til(N)
  com rho_til = rho/(m^2 M_eff^2) e rho = rho_m0 a^-3 (drho_til/dN = -3 rho_til):

      W'(r) dr/dN = -3 rho_til     =>     dr/dN = -3 rho_til / W'(r)

      W'(r) = (1/mu)(2 b4 r + 3 b3 - b1/r^2) - (3 b1 + 6 b2 r + 3 b3 r^2)

  Exata. Sem estencil, sem np.gradient. (O estencil de 8a ordem entra
  so' como canal de cross-check, gate M4.)

  ** xi ** = r + dr/dN = r - 3 rho_til / W'(r).

  ** m_T^2 ** (cap. 06, caixa; derivations/02_setor_tensorial_mT2.md sec.3.3):

      m_T^2 = m^2 M_eff^2 (1/M_g^2 + xi/(M_f^2 r^3)) r [b1 + b2(xi+r) + b3 xi r]

  Com b2 = b3 = 0 (celula IBB) o fator estrutural colapsa em b1 > 0 e

      m_T^2 / H^2 = 3 b1 (mu r^3 + xi) / ( r (b4 r^3 + b1) )

  -- m^2, M_eff^2 e M_f^2 cancelam. (Derivado no script, verificado
  numericamente contra a forma nao-simplificada.)

  ** Dicionario de "hoje" ** (convencao do R-8b): rho_m0 fixado por
  Omega_m(a=1) = 0.3, com Omega_m = 1 - mu V_g(r)/(r^2 V_f(r)).

Uso:  .venv\\Scripts\\python.exe auditoria/code/r13b_ibb_ramo_infinito.py
Saida: auditoria/code/out/r13b_ibb_ramo_infinito.txt
"""
import os
import sys

try:
    import numpy as np
except ImportError:
    print("ERRO: precisa de numpy.  pip install numpy")
    sys.exit(2)

# ---------------------------------------------------------------------
# NP.GRADIENT PROIBIDO (regra 6). Trava explicita: qualquer chamada
# a np.gradient neste processo levanta excecao.
# ---------------------------------------------------------------------
def _gradiente_proibido(*a, **k):
    raise RuntimeError(
        "np.gradient e' PROIBIDO (regra 6, Erratum-03). Use forma "
        "fechada ou estencil de ordem >= 8 com teste de refino.")


np.gradient = _gradiente_proibido

# estencil central de 8a ordem para d/dN (mesmos coeficientes de
# auditoria/code/r12h_raio_de_alcance.py, C8TH)
C8TH = np.array([1.0 / 280, -4.0 / 105, 1.0 / 5, -4.0 / 5, 0.0,
                 4.0 / 5, -1.0 / 5, 4.0 / 105, -1.0 / 280])

LINHAS = []


def say(s=""):
    print(s)
    LINHAS.append(s)


# =====================================================================
# 1. MAQUINARIA DO FUNDO (reuso da rota de ramo_dinamico_correto.py,
#    com a selecao de raiz CORRIGIDA para o ramo infinito)
# =====================================================================

class Celula(object):
    """Uma celula de parametros (b0,b1,b2,b3,b4,mu). M_g^2 = 1, m^2 = 1."""

    def __init__(self, b0, b1, b2, b3, b4, mu):
        self.b0, self.b1, self.b2, self.b3, self.b4 = b0, b1, b2, b3, b4
        self.mu = mu                      # mu = M_f^2 / M_g^2
        self.Mg2 = 1.0
        self.Mf2 = mu
        self.Meff2 = 1.0 / (1.0 / self.Mg2 + 1.0 / self.Mf2)
        self.m2 = 1.0

    def V_g(self, r):
        return self.b0 + 3 * self.b1 * r + 3 * self.b2 * r**2 + self.b3 * r**3

    def V_f(self, r):
        return (self.b4 + 3 * self.b3 / r + 3 * self.b2 / r**2
                + self.b1 / r**3)

    def W(self, r):
        return (self.Mg2 / self.Mf2) * r**2 * self.V_f(r) - self.V_g(r)

    def dW(self, r):
        """W'(r) -- FORMA FECHADA (derivada analitica de W)."""
        k = self.Mg2 / self.Mf2
        return (k * (2 * self.b4 * r + 3 * self.b3 - self.b1 / r**2)
                - (3 * self.b1 + 6 * self.b2 * r + 3 * self.b3 * r**2))

    def raizes(self, rho_til):
        """Todas as raizes reais positivas de W(r) = rho_til.

        Multiplicando por r (b3 = 0 -> cubica; b3 != 0 -> quartica).
        """
        k = self.Mg2 / self.Mf2
        if self.b3 == 0.0:
            c = [k * self.b4 - 3 * self.b2,
                 -3 * self.b1,
                 3 * k * self.b2 - self.b0 - rho_til,
                 k * self.b1]
        else:
            c = [-self.b3,
                 k * self.b4 - 3 * self.b2,
                 3 * k * self.b3 - 3 * self.b1,
                 3 * k * self.b2 - self.b0 - rho_til,
                 k * self.b1]
        z = np.roots(c)
        return sorted(w.real for w in z
                      if abs(w.imag) < 1e-9 * max(1.0, abs(w.real))
                      and w.real > 1e-14)

    def newton(self, r0, rho_til, nit=60):
        """Polimento de Newton sobre W(r) - rho_til = 0 (W' em forma fechada)."""
        r = float(r0)
        for _ in range(nit):
            f = self.W(r) - rho_til
            d = self.dW(r)
            if d == 0.0 or not np.isfinite(d):
                return np.nan
            step = f / d
            r_new = r - step
            if r_new <= 0:
                r_new = 0.5 * r
            if abs(r_new - r) <= 1e-15 * abs(r_new):
                return r_new
            r = r_new
        return r

    # -- forma fechada das quantidades do fundo ------------------------
    def drdN(self, r, rho_til):
        """dr/dN em FORMA FECHADA: -3 rho_til / W'(r).  (regra 6)"""
        return -3.0 * rho_til / self.dW(r)

    def xi(self, r, rho_til):
        return r + self.drdN(r, rho_til)

    def H2_f(self, r):
        """H^2 pela Friedmann do setor f (F.4)."""
        return self.m2 * self.Meff2 * r**2 * self.V_f(r) / (3.0 * self.Mf2)

    def H2_g(self, r, rho):
        """H^2 pela Friedmann do setor g (F.3)."""
        return (rho + self.m2 * self.Meff2 * self.V_g(r)) / (3.0 * self.Mg2)

    def m_T2(self, r, xi):
        """Forma fechada do cap. 06 / derivations/02 sec.3.3."""
        pref = self.Meff2 * (1.0 / self.Mg2 + xi / (self.Mf2 * r**3))
        fator = self.b1 + self.b2 * (xi + r) + self.b3 * xi * r
        return self.m2 * pref * r * fator

    def Omega_m(self, r):
        """Omega_m = rho/(3 M_g^2 H^2) = 1 - mu V_g/(r^2 V_f)."""
        return 1.0 - self.mu * self.V_g(r) / (r**2 * self.V_f(r))


# ---------------------------------------------------------------------
# selecao de raiz -- as DUAS rotas, para deixar a armadilha explicita
# ---------------------------------------------------------------------
def raiz_menor_positiva(cel, rho_til):
    """A ARMADILHA: a selecao de ramo_dinamico_correto.py (ramo FINITO)."""
    rr = cel.raizes(rho_til)
    return rr[0] if rr else np.nan


def raiz_por_continuacao(cel, rho_til, r_ref):
    """Selecao correta: raiz mais proxima da anterior (licao do R-8b)."""
    rr = cel.raizes(rho_til)
    if not rr:
        return np.nan
    if r_ref is None or not np.isfinite(r_ref):
        return rr[-1]                     # maior positiva (semente do inf.)
    return min(rr, key=lambda z: abs(z - r_ref))


def r_c_infinito(cel):
    """Ponto fixo tardio do ramo infinito: MAIOR raiz positiva de W(r)=0."""
    rr = cel.raizes(0.0)
    return (rr[-1], rr) if rr else (np.nan, [])


def rho_til_de_N(cel, N, rho_til0):
    return rho_til0 * np.exp(-3.0 * N)


def integra_ramo(cel, N_grid, rho_til0, sentido='infinito'):
    """r(N) por selecao de raiz com CONTINUACAO.

    'infinito' : semeia no PASSADO profundo com a assintota do ramo
                 infinito e caminha para o FUTURO.
    'finito'   : semeia no FUTURO com a menor raiz positiva e caminha
                 para o PASSADO (a rota de ramo_dinamico_correto.py).
    """
    n = len(N_grid)
    r = np.full(n, np.nan)
    if sentido == 'infinito':
        rt0 = rho_til_de_N(cel, N_grid[0], rho_til0)
        # semente analitica: b4 r^2/mu ~ rho_til  =>  r ~ sqrt(mu rho_til/b4)
        seed = np.sqrt(cel.mu * rt0 / cel.b4) if cel.b4 > 0 else np.nan
        ref = seed
        ordem = range(n)
    else:
        ref = None
        ordem = range(n - 1, -1, -1)
    for i in ordem:
        rt = rho_til_de_N(cel, N_grid[i], rho_til0)
        cand = (raiz_por_continuacao(cel, rt, ref) if sentido == 'infinito'
                else (raiz_menor_positiva(cel, rt) if ref is None
                      else raiz_por_continuacao(cel, rt, ref)))
        if np.isfinite(cand):
            cand = cel.newton(cand, rt)
        r[i] = cand
        if np.isfinite(cand):
            ref = cand
    return r


# =====================================================================
# 2. REGRA 6 -- estencil de 8a ordem com teste de refino
# =====================================================================
def drdN_estencil8(cel, N0, rho_til0, h):
    """dr/dN por estencil central de 8a ordem sobre N.

    Cada r(N0 + j h) e' resolvido pela MESMA rota (raiz + Newton),
    semeado pela vizinhanca -- nao ha' interpolacao nem np.gradient.
    """
    r_c = None
    vals = np.zeros(9)
    # resolve o centro primeiro, depois abre para os dois lados
    idx = [4, 5, 6, 7, 8, 3, 2, 1, 0]
    ref = None
    for q in idx:
        j = q - 4
        rt = rho_til_de_N(cel, N0 + j * h, rho_til0)
        if ref is None:
            rr = cel.raizes(rt)
            if not rr:
                return np.nan
            cand = rr[-1]
        else:
            cand = raiz_por_continuacao(cel, rt, ref)
        cand = cel.newton(cand, rt)
        vals[q] = cand
        if q == 4:
            r_c = cand
            ref = cand
        elif q == 8:
            ref = r_c                     # reinicia a referencia para o lado -
    del r_c
    return float(np.dot(C8TH, vals) / h)


# =====================================================================
# 3. RELATORIO
# =====================================================================
say("=" * 74)
say("R-13b -- MEDICAO DO RAMO INFINITO EM CELULAS IBB")
say("=" * 74)
say("")
say("Este script MEDE. Ele NAO conclui exclusao nem aprovacao do IBB.")
say("Criterios pre-declarados: cabecalho do arquivo (secao CRITERIOS).")
say("")
say("CEGUEIRA DO GATE (regra 7, obrigatoria):")
say("  Este teste mede Higuchi/helicidade-0 e o setor TENSORIAL.")
say("  ELE NAO MEDE GRADIENTE. Se o IBB passar aqui, isso NAO diz nada")
say("  sobre c_s^2 la' -- e vice-versa.")
say("")

# ---------------------------------------------------------------------
say("-" * 74)
say("[0] A ARMADILHA, DEMONSTRADA")
say("-" * 74)
say("")
say("  auditoria/code/ramo_dinamico_correto.py, resolve_r(): sem")
say("  referencia devolve rr[0] = MENOR raiz positiva. Isso e' o ramo")
say("  FINITO. Para o ramo infinito e' a selecao ERRADA.")
say("")

cel_dem = Celula(b0=0.0, b1=1.0, b2=0.0, b3=0.0, b4=1.0, mu=1.0)
say(f"  celula de demonstracao: b0=0, b1=1, b2=b3=0, b4=1, mu=1")
say(f"  {'rho_til':>12} {'raizes positivas de W(r)=rho_til':>44}")
for rt in [1e6, 1e3, 10.0, 1.0, 0.0]:
    rr = cel_dem.raizes(rt)
    say(f"  {rt:12.4g}   " + "  ".join(f"{z:.6g}" for z in rr))
say("")
say("  menor raiz  -> r ~ b1/(mu rho_til) -> 0   : ramo FINITO")
say("  maior raiz  -> r ~ sqrt(mu rho_til/b4)    : ramo INFINITO")
say("  Selecao usada aqui: CONTINUACAO a partir da assintota do ramo")
say("  infinito no passado profundo, caminhando para o futuro (R-8b).")
say("")

# ---------------------------------------------------------------------
say("-" * 74)
say("[M5] CONTROLE POSITIVO -- a maquinaria reproduz o RAMO FINITO?")
say("-" * 74)
say("")
say("  Alvo: docs/resultado_ramo_finito.md secs. 1-3 (benchmark")
say("  b=(1,1,-0.4,0,0.5), M_g^2=M_f^2=1, m^2=1, rho_m0=0.3,")
say("  a em [1e-2, 10^0.3], 400 pontos).")
say("")

cel_pc = Celula(b0=1.0, b1=1.0, b2=-0.4, b3=0.0, b4=0.5, mu=1.0)
a_pc = np.logspace(-2, 0.3, 400)
N_pc = np.log(a_pc)
rho_m0_pc = 0.3
rt0_pc = rho_m0_pc / (cel_pc.m2 * cel_pc.Meff2)   # rho_til em a = 1
r_pc = integra_ramo(cel_pc, N_pc, rt0_pc, sentido='finito')
rt_pc = rho_til_de_N(cel_pc, N_pc, rt0_pc)
drdN_pc = cel_pc.drdN(r_pc, rt_pc)
xi_pc = r_pc + drdN_pc
H2_pc = cel_pc.H2_f(r_pc)
mT2_pc = cel_pc.m_T2(r_pc, xi_pc)

pc_a = float(np.min(xi_pc))
pc_b = float(r_pc[-1])
i02 = int(np.argmin(np.abs(a_pc - 0.02)))
pc_c = float(drdN_pc[0] / (3.0 * r_pc[0]))
pc_d = float(mT2_pc[i02] / H2_pc[i02])
pc_e = int(np.sum(mT2_pc >= 2 * H2_pc))
pc_gr = float(H2_pc[0] / (rho_m0_pc * a_pc[0]**-3 / (3 * cel_pc.Mg2)))
# ponto fixo tardio do ramo finito: MENOR raiz positiva de W = 0
rr0_pc = cel_pc.raizes(0.0)

say(f"  (a) min(xi) na historia          = {pc_a:.6g}   (alvo: > 0)")
say(f"  (b) r no fim da grade            = {pc_b:.6g}")
say(f"      ponto fixo (menor raiz W=0)  = {rr0_pc[0]:.6g}   (alvo: 0.33+-0.01)")
say(f"      r no inicio da grade         = {r_pc[0]:.6g}")
say(f"  (c) primordial dr/dN / (3r)      = {pc_c:.9f}   (alvo: 1 +- 1e-2)")
say(f"      xi/r primordial              = {xi_pc[0]/r_pc[0]:.9f}   (alvo: 4)")
say(f"  (d) m_T^2/H^2 em a = {a_pc[i02]:.4f}      = {pc_d:.4f}   (alvo: 12.00+-0.05)")
say(f"  (e) Higuchi m_T^2 >= 2H^2        = {pc_e}/400")
say(f"  (+) limite GR: H^2/(rho/3M_g^2)  = {pc_gr:.6f}   (esperado ~1)")
say("")

assert pc_a > 0, "M5(a) FALHOU: xi <= 0 no ramo finito de controle"
assert abs(rr0_pc[0] - 0.33) <= 0.01, "M5(b) FALHOU: ponto fixo != 0.33"
assert abs(pc_c - 1.0) <= 1e-2, "M5(c) FALHOU: dr/dN != 3r no primordial"
assert abs(pc_d - 12.0) <= 0.05, "M5(d) FALHOU: m_T^2/H^2 != 12 em a=0.02"
assert pc_e == 400, "M5(e) FALHOU: Higuchi nao da' 400/400"
say("  [M5 OK] a maquinaria reproduz o ramo finito conhecido.")
say("")

# ---------------------------------------------------------------------
say("-" * 74)
say("[M6] PODER DO GATE DE HIGUCHI -- ele consegue REPROVAR?")
say("-" * 74)
say("")
say("  Caso sabidamente falso: fundo da D8 / derivations/02 sec.3.4")
say("  (r=1.2, xi=3.497, b1=1, b2=-0.4) -> m_T^2 = -3.19 < 0.")
cel_d8 = Celula(b0=1.0, b1=1.0, b2=-0.4, b3=0.0, b4=0.5, mu=1.0)
mT2_d8 = cel_d8.m_T2(1.2, 3.497)
say(f"  m_T^2 medido pela nossa forma fechada = {mT2_d8:.4f}")
say(f"  fator estrutural b1+b2(xi+r)          = "
    f"{1.0 - 0.4 * (3.497 + 1.2):.4f}")
say(f"  gate Higuchi (m_T^2 >= 2H^2) aprova?  "
    f"{'SIM (SEM PODER)' if mT2_d8 >= 0 else 'NAO -- REPROVA'}")
say("")
say("  ** EMENDA DECLARADA (1a execucao REPROVOU o item numerico) **")
say("  O criterio original exigia m_T^2 = -3.19 +- 0.05. Medimos")
say("  -1.5944 -- exatamente METADE. Causa localizada:")
cel_d8b = Celula(b0=1.0, b1=1.0, b2=-0.4, b3=0.0, b4=0.5, mu=1.0)
cel_d8b.Meff2 = 1.0
mT2_d8b = cel_d8b.m_T2(1.2, 3.497)
say(f"    com M_eff^2 = 0.5 (= 1/(1/M_g^2+1/M_f^2), convencao de")
say(f"    ramo_dinamico_correto.py e deste script) : m_T^2 = {mT2_d8:.4f}")
say(f"    com M_eff^2 = 1   (convencao usada no numero de")
say(f"    derivations/02 sec.3.4)                  : m_T^2 = {mT2_d8b:.4f}")
say(f"    razao = {mT2_d8b/mT2_d8:.6f}")
say("  => inconsistencia de NORMALIZACAO entre dois docs do corpus,")
say("     nao erro de fisica. O fator estrutural e o SINAL batem, e")
say("     m_T^2/H^2 -- a unica quantidade interpretada aqui -- e'")
say("     INVARIANTE por M_eff^2 (secao [INVARIANCIA] adiante).")
say("  Criterio M6 emendado: (a) m_T^2 < 0; (b) fator = -0.88+-0.005;")
say("                        (c) -3.19+-0.05 SE M_eff^2 = 1.")
assert mT2_d8 < 0, "M6(a) FALHOU: o gate nao reprova o caso sabidamente falso"
assert abs((1.0 - 0.4 * (3.497 + 1.2)) - (-0.88)) < 5e-3, \
    "M6(b) FALHOU: fator estrutural nao bate com D2 sec.3.4"
assert abs(mT2_d8b - (-3.19)) < 0.05, \
    "M6(c) FALHOU: nem com M_eff^2=1 reproduz o -3.19 da D2 sec.3.4"
say("  [M6 OK] o gate tem poder de reprovar; a causa do desvio")
say("          numerico esta' localizada e registrada.")
say("")

# ---------------------------------------------------------------------
say("-" * 74)
say("[M7] FRONTEIRA DE EXISTENCIA DO RAMO INFINITO -- forma fechada")
say("-" * 74)
say("")
say("  Com b0 = b2 = b3 = 0, o ponto fixo tardio resolve W(r)=0:")
say("      y r^3 - 3 mu r^2 + 1 = 0,   y = b4/b1")
say("  Minimo local em r = 2 mu / y, com valor 1 - 4 mu^3 / y^2.")
say("  Duas raizes positivas <=>  y < 2 mu^{3/2}.   [forma fechada]")
say("  Em mu = 1 isso e' exatamente  0 < b4 < 2 b1 -- o intervalo IBB")
say("  da fonte (Konnig 2015; R-12i sec.1.6).")
say("")


def y_max_fechado(mu):
    return 2.0 * mu**1.5


def y_max_numerico(mu, lo=1e-4, hi=1e4):
    """Maior y com duas raizes positivas de y r^3 - 3 mu r^2 + 1 = 0."""
    def existe(y):
        c = Celula(0.0, 1.0, 0.0, 0.0, y, mu)
        return len(c.raizes(0.0)) >= 2
    if not existe(lo):
        return np.nan
    a_, b_ = lo, hi
    for _ in range(200):
        mid = 0.5 * (a_ + b_)
        if existe(mid):
            a_ = mid
        else:
            b_ = mid
    return 0.5 * (a_ + b_)


say(f"  {'mu':>10} {'y_max fechado':>16} {'y_max numerico':>17} {'|dif|':>12}")
for mu in [0.1, 0.25, 0.5, 1.0, 2.0, 5.0, 10.0]:
    yf, yn = y_max_fechado(mu), y_max_numerico(mu)
    say(f"  {mu:10.4g} {yf:16.10f} {yn:17.10f} {abs(yf-yn):12.3e}")
    assert abs(yf - yn) <= 1e-6 * max(1.0, yf), f"M7 FALHOU em mu={mu}"
say("")
say("  Caso da fonte, mu = 1: y_max = 2.0000000000  ==  2*b1. [OK]")
say("  [M7 OK] fronteira de existencia fechada e verificada.")
say("")
say("  >>> ACHADO DA VARREDURA EM mu (o corpus nunca varreu mu):")
say("      a janela IBB NAO e' 0 < b4 < 2 b1 em geral -- ela e'")
say("      0 < b4/b1 < 2 mu^{3/2}. O intervalo da fonte e' o caso")
say("      particular mu = M_f^2/M_g^2 = 1.")
say("")

# ---------------------------------------------------------------------
say("-" * 74)
say("[M4] REGRA 6 -- dr/dN fechada vs estencil de 8a ordem (refino)")
say("-" * 74)
say("")
say("  np.gradient esta' PROIBIDO neste processo (trava ativa no topo).")
say("  Canal 1: dr/dN = -3 rho_til / W'(r)          [FORMA FECHADA]")
say("  Canal 2: estencil central de 8a ordem em N, h = 1e-3 e 3e-4,")
say("           com r(N+jh) resolvido pela mesma rota raiz+Newton.")
say("")
say(f"  {'celula':>26} {'a':>8} {'fechada':>17} {'d8(h=1e-3)':>17} "
    f"{'d8(h=3e-4)':>17} {'refino':>10} {'canais':>10}")

cel_m4 = [
    ("IBB mu=1  y=1.0", Celula(0.0, 1.0, 0.0, 0.0, 1.0, 1.0)),
    ("IBB mu=1  y=1.9", Celula(0.0, 1.0, 0.0, 0.0, 1.9, 1.0)),
    ("IBB mu=0.25 y=0.2", Celula(0.0, 1.0, 0.0, 0.0, 0.2, 0.25)),
    ("IBB mu=10 y=30", Celula(0.0, 1.0, 0.0, 0.0, 30.0, 10.0)),
]


def rho_til0_de_Omega(cel, Om_alvo=0.3):
    """rho_til em a=1 tal que Omega_m(a=1) = Om_alvo, no ramo infinito."""
    rc, _ = r_c_infinito(cel)
    if not np.isfinite(rc):
        return np.nan
    lo, hi = rc * (1 + 1e-12), rc * 1e8
    for _ in range(300):
        mid = np.sqrt(lo * hi)
        if cel.Omega_m(mid) < Om_alvo:
            lo = mid
        else:
            hi = mid
    r0 = np.sqrt(lo * hi)
    return cel.W(r0)


m4_ok = True
for nome, c in cel_m4:
    rt0 = rho_til0_de_Omega(c)
    for aval in [1e-2, 1.0]:
        N0 = np.log(aval)
        rt = rho_til_de_N(c, N0, rt0)
        rr = c.raizes(rt)
        r0 = c.newton(rr[-1], rt)
        fech = c.drdN(r0, rt)
        d1 = drdN_estencil8(c, N0, rt0, 1e-3)
        d2 = drdN_estencil8(c, N0, rt0, 3e-4)
        e_ref = abs(d1 - d2) / abs(fech)
        e_can = abs(d2 - fech) / abs(fech)
        ok = (e_ref <= 1e-8) and (e_can <= 1e-8)
        m4_ok = m4_ok and ok
        say(f"  {nome:>26} {aval:8.3g} {fech:17.10e} {d1:17.10e} "
            f"{d2:17.10e} {e_ref:10.2e} {e_can:10.2e}")
say("")
say("  criterio M4: refino <= 1e-8 E canais <= 1e-8")
assert m4_ok, "M4 FALHOU: forma fechada e estencil de 8a ordem discordam"
say("  [M4 OK] derivada em forma fechada, confirmada por 8a ordem com")
say("          refino estavel em dois h.")
say("")

# ---------------------------------------------------------------------
say("=" * 74)
say("[VARREDURA] 108 CELULAS IBB GENUINAS")
say("=" * 74)
say("")
say("  IBB genuino (Konnig 2015 / R-12i sec.1.6): SO b1 e b4 ligados.")
say("    b0 = b2 = b3 = 0,  b1 = 1 (normalizacao),  0 < b4 < 2 mu^{3/2}")
say("  Eixos varridos:")
say("    mu = M_f^2/M_g^2 : 9 valores, logspace(-1, 1)  [NUNCA varrido")
say("                       antes no corpus -- lacuna do parecer]")
say("    y = b4/b1        : 12 valores, y = f * y_max(mu), f em")
say("                       linspace(0.05, 0.98)   [faixa INTEIRA]")
say("  9 x 12 = 108 celulas.")
say("")
say("  FRONTEIRAS DE VARREDURA DECLARADAS:")
say("    - historia: a em [1e-4, 30], 600 pontos em N = ln a")
say("    - dicionario de 'hoje': Omega_m(a=1) = 0.3 (convencao R-8b)")
say("    - materia sem radiacao, sem vacuo escalar (rho = rho_m0 a^-3)")
say("    - b0 = 0 (IBB genuino). Eixo de robustez em b0 na secao [B0].")
say("    - m^2 e M_eff^2 cancelam em m_T^2/H^2 (verificado abaixo)")
say("")

MU_S = np.logspace(-1, 1, 9)
FRAC_S = np.linspace(0.05, 0.98, 12)
N_GRID = np.linspace(np.log(1e-4), np.log(30.0), 600)
A_GRID = np.exp(N_GRID)


def mede_celula(mu, frac):
    y = frac * y_max_fechado(mu)
    c = Celula(0.0, 1.0, 0.0, 0.0, y, mu)
    out = {'mu': mu, 'frac': frac, 'y': y, 'cel': c, 'medida': False}
    rc, todas = r_c_infinito(c)
    out['r_c'] = rc
    out['raizes0'] = todas
    rt0 = rho_til0_de_Omega(c)
    out['rho_til0'] = rt0
    if not np.isfinite(rt0) or not np.isfinite(rc):
        out['motivo'] = 'sem ponto fixo / sem dicionario'
        return out
    r = integra_ramo(c, N_GRID, rt0, sentido='infinito')
    rt = rho_til_de_N(c, N_GRID, rt0)
    if not np.all(np.isfinite(r)):
        out['motivo'] = 'raiz nao converge em parte da grade'
        return out
    drdN = c.drdN(r, rt)
    xi = r + drdN
    H2f = c.H2_f(r)
    H2g = c.H2_g(r, rt * c.m2 * c.Meff2)
    mT2 = c.m_T2(r, xi)

    # ---- M1 gate de ramo -------------------------------------------
    rt_ini = rt[0]
    r_ass = np.sqrt(mu * rt_ini / c.b4)
    g1a = r[0] / r[-1] >= 1e2
    g1b = bool(np.all(drdN < 0))
    g1c = abs(r[0] / r_ass - 1.0) <= 1e-2
    g1d = abs(r[-1] / rc - 1.0) <= 5e-2
    g1e = len(todas) >= 2 and rc > max(z for z in todas if z < rc) if len(todas) >= 2 else False
    # ---- M2 duas Friedmann -----------------------------------------
    g2 = float(np.max(np.abs(H2g / H2f - 1.0)))
    # ---- M3 residuo da cubica --------------------------------------
    res = np.abs(c.W(r) - rt) / np.maximum(1.0, np.abs(rt))
    g3 = float(np.max(res))

    out.update({
        'r': r, 'rt': rt, 'drdN': drdN, 'xi': xi, 'H2': H2f, 'mT2': mT2,
        'g1a': g1a, 'g1b': g1b, 'g1c': g1c, 'g1d': g1d, 'g1e': g1e,
        'g1c_val': abs(r[0] / r_ass - 1.0), 'g1d_val': abs(r[-1] / rc - 1.0),
        'g2': g2, 'g3': g3,
        'r_ini': r[0], 'r_fim': r[-1], 'r_ass': r_ass,
    })
    if not (g1a and g1b and g1c and g1d and g1e and g2 <= 1e-10
            and g3 <= 1e-12):
        out['motivo'] = 'gate de maquinaria M1/M2/M3'
        return out

    # ---- MEDIDAS ---------------------------------------------------
    razao = mT2 / H2f
    higuchi = mT2 >= 2 * H2f
    # cruzamento de xi por zero (bisseccao sobre a forma fechada)
    idx = np.where(np.sign(xi[:-1]) != np.sign(xi[1:]))[0]
    a_xi0 = []
    for i in idx:
        lo, hi = N_GRID[i], N_GRID[i + 1]
        for _ in range(200):
            mid = 0.5 * (lo + hi)
            rtm = rho_til_de_N(c, mid, rt0)
            rm = c.newton(raiz_por_continuacao(c, rtm, r[i]), rtm)
            if np.sign(c.xi(rm, rtm)) == np.sign(xi[i]):
                lo = mid
            else:
                hi = mid
        a_xi0.append(float(np.exp(0.5 * (lo + hi))))
    out.update({
        'medida': True,
        'razao': razao,
        'frac_rneg': float(np.mean(drdN < 0)),
        'frac_rpos': float(np.mean(drdN > 0)),
        'max_drdN': float(np.max(drdN)),
        'a_xi0': a_xi0,
        'n_hig': int(np.sum(higuchi)),
        'n_tot': int(len(higuchi)),
        'razao_max': float(np.max(razao)),
        'razao_min': float(np.min(razao)),
        'n_mT2pos': int(np.sum(mT2 > 0)),
        'razao_fix': 1.0 + 1.0 / (mu * rc**2),
        'mu_rc2': mu * rc**2,
    })
    return out


say("  medindo 108 celulas ...")
CELULAS = []
for mu in MU_S:
    for f in FRAC_S:
        CELULAS.append(mede_celula(mu, f))
n_med = sum(1 for c in CELULAS if c['medida'])
say(f"  celulas medidas: {n_med}/{len(CELULAS)}")
nao = [c for c in CELULAS if not c['medida']]
if nao:
    say("  celulas NAO medidas (preservadas, regra 2):")
    for c in nao:
        say(f"    mu={c['mu']:.4g} y={c['y']:.4g} -> {c.get('motivo','?')}")
say("")

# ---------------------------------------------------------------------
say("-" * 74)
say("[M1] GATE 'ESTOU MESMO NO RAMO INFINITO?' -- por celula")
say("-" * 74)
say("")
say("  (a) r(a_min)/r(a_max) >= 1e2   (b) dr/dN < 0 em 100% dos pontos")
say("  (c) |r(a_min)/r_assint - 1| <= 1e-2, r_assint=sqrt(mu rho_til/b4)")
say("  (d) |r(a_max)/r_c - 1| <= 5e-2  (e) r_c = MAIOR raiz de W=0")
say("")
ok_a = sum(1 for c in CELULAS if c.get('g1a'))
ok_b = sum(1 for c in CELULAS if c.get('g1b'))
ok_c = sum(1 for c in CELULAS if c.get('g1c'))
ok_d = sum(1 for c in CELULAS if c.get('g1d'))
ok_e = sum(1 for c in CELULAS if c.get('g1e'))
say(f"  (a) r grande no passado        : {ok_a}/108")
say(f"  (b) r decrescente em tudo      : {ok_b}/108")
say(f"  (c) bate com a assintota       : {ok_c}/108   "
    f"(max desvio {max(c.get('g1c_val',0) for c in CELULAS):.3e})")
say(f"  (d) pousa no ponto fixo r_c    : {ok_d}/108   "
    f"(max desvio {max(c.get('g1d_val',0) for c in CELULAS):.3e})")
say(f"  (e) r_c e' a MAIOR raiz de W=0 : {ok_e}/108")
say(f"  [M2] max |H2_g/H2_f - 1|       : "
    f"{max(c.get('g2',0) for c in CELULAS):.3e}  (criterio 1e-10)")
say(f"  [M3] max residuo da cubica     : "
    f"{max(c.get('g3',0) for c in CELULAS):.3e}  (criterio 1e-12)")
say("")
say(f"  faixa de r no passado (a=1e-4) : "
    f"{min(c['r_ini'] for c in CELULAS if c['medida']):.4g} .. "
    f"{max(c['r_ini'] for c in CELULAS if c['medida']):.4g}")
say(f"  faixa de r_c (ponto fixo)      : "
    f"{min(c['r_c'] for c in CELULAS if c['medida']):.4g} .. "
    f"{max(c['r_c'] for c in CELULAS if c['medida']):.4g}")
say("")
if ok_a == ok_b == ok_c == ok_d == ok_e == 108:
    say("  [M1 OK] 108/108 -- estamos no ramo infinito em todas as celulas.")
else:
    say("  [M1 PARCIAL] ver celulas nao medidas acima.")
say("")

# ---------------------------------------------------------------------
say("-" * 74)
say("[R1..R5] TABELA DA VARREDURA -- por celula")
say("-" * 74)
say("")
say("  r'  = dr/dN   |  xi = r + dr/dN  |  razao = m_T^2/H^2")
say("  Hig = pontos com m_T^2 >= 2H^2 (a inequacao DO REPOSITORIO)")
say("")
say(f"  {'mu':>7} {'b4/b1':>9} {'f=y/ymax':>9} {'r_c':>9} "
    f"{'r(a=1e-4)':>11} {'r<0 %':>7} {'max r prime':>12} "
    f"{'a(xi=0)':>10} {'raz@a=1':>9} {'raz max':>9} {'raz@fix':>9} "
    f"{'Hig':>8} {'mT2>0':>8}")
i_hoje = int(np.argmin(np.abs(A_GRID - 1.0)))
for c in CELULAS:
    if not c['medida']:
        say(f"  {c['mu']:7.3g} {c['y']:9.4g} {c['frac']:9.3g}   "
            f"NAO MEDIDA: {c.get('motivo','?')}")
        continue
    axi = c['a_xi0'][0] if c['a_xi0'] else float('nan')
    say(f"  {c['mu']:7.3g} {c['y']:9.4g} {c['frac']:9.3g} {c['r_c']:9.4f} "
        f"{c['r_ini']:11.4g} {100*c['frac_rneg']:7.1f} "
        f"{c['max_drdN']:12.3e} {axi:10.4f} "
        f"{c['razao'][i_hoje]:9.4f} {c['razao_max']:9.4f} "
        f"{c['razao_fix']:9.4f} {c['n_hig']:4d}/{c['n_tot']:<3d} "
        f"{c['n_mT2pos']:4d}/{c['n_tot']:<3d}")
say("")

# ---------------------------------------------------------------------
say("-" * 74)
say("[RESUMO DE CLASSE]")
say("-" * 74)
say("")
med = [c for c in CELULAS if c['medida']]
n_rneg = sum(1 for c in med if c['frac_rneg'] == 1.0)
n_xi0 = sum(1 for c in med if len(c['a_xi0']) >= 1)
n_hig_tot = sum(c['n_hig'] for c in med)
n_pts_tot = sum(c['n_tot'] for c in med)
n_cel_hig = sum(1 for c in med if c['n_hig'] == c['n_tot'])
n_cel_hig0 = sum(1 for c in med if c['n_hig'] == 0)
n_mT2pos = sum(1 for c in med if c['n_mT2pos'] == c['n_tot'])
say(f"  R1  r' < 0 em 100% da historia            : {n_rneg}/{len(med)} celulas")
say(f"      max(r') sobre TODAS as celulas         : "
    f"{max(c['max_drdN'] for c in med):.4e}   (negativo => r' < 0 sempre)")
say(f"  R2  xi cruza zero                          : {n_xi0}/{len(med)} celulas")
if n_xi0:
    axs = [c['a_xi0'][0] for c in med if c['a_xi0']]
    nxs = [len(c['a_xi0']) for c in med]
    say(f"      a do cruzamento: {min(axs):.4f} .. {max(axs):.4f}"
        f"   (z = {1/max(axs)-1:.3f} .. {1/min(axs)-1:.3f})")
    say(f"      numero de cruzamentos por celula: min {min(nxs)}, max {max(nxs)}")
say(f"  R3  m_T^2/H^2 no ponto fixo tardio         : "
    f"{min(c['razao_fix'] for c in med):.6f} .. "
    f"{max(c['razao_fix'] for c in med):.6f}")
say(f"      m_T^2/H^2 maximo na historia           : "
    f"{min(c['razao_max'] for c in med):.6f} .. "
    f"{max(c['razao_max'] for c in med):.6f}")
n_mono = sum(1 for c in med if bool(np.all(np.diff(c['razao']) > 0)))
say(f"      m_T^2/H^2 monotona crescente em N      : {n_mono}/{len(med)} celulas")
say(f"      => o supremo sobre a historia INTEIRA (incluindo a -> inf)")
say(f"         e' o valor no ponto fixo, 1 + 1/(mu r_c^2)")
say(f"  R4  Higuchi (m_T^2 >= 2H^2), pontos        : "
    f"{n_hig_tot}/{n_pts_tot}")
say(f"      celulas com Higuchi em 100% da historia: {n_cel_hig}/{len(med)}")
say(f"      celulas com Higuchi em 0% da historia  : {n_cel_hig0}/{len(med)}")
say(f"  R5  m_T^2 > 0 em 100% da historia          : {n_mT2pos}/{len(med)} celulas")
say("")

# ---------------------------------------------------------------------
say("-" * 74)
say("[COROLARIO FECHADO] o valor de m_T^2/H^2 no ponto fixo tardio")
say("-" * 74)
say("")
say("  Com b0=b2=b3=0 e W(r_c)=0 vale  b4 r_c^3 + b1 = 3 mu b1 r_c^2,")
say("  logo, substituindo na caixa do cap. 06:")
say("")
say("      m_T^2/H^2 |_{r=r_c}  =  1 + 1/(mu r_c^2)")
say("")
say("  E a fronteira de existencia (M7) da' r_c > 2 mu / y > mu^{-1/2},")
say("  isto e'  mu r_c^2 > 1  em TODA a janela IBB. Logo")
say("")
say("      1 < m_T^2/H^2 |_{ponto fixo} < 2      (estrito, sempre)")
say("")
say("  com o supremo 2 atingido so' no limite y -> 2 mu^{3/2}, onde o")
say("  ponto fixo degenera (raiz dupla) e o ramo deixa de existir.")
say("")
say("  Verificacao numerica (108 celulas):")
mx = max(abs(c['razao'][-1] - c['razao_fix']) for c in med)
say(f"    max |razao(a=30) - (1 + 1/(mu r_c^2))| = {mx:.3e}")
say(f"    min (mu r_c^2) sobre as celulas        = "
    f"{min(c['mu_rc2'] for c in med):.6f}   (tem de ser > 1)")
say(f"    max (m_T^2/H^2 no ponto fixo)          = "
    f"{max(c['razao_fix'] for c in med):.6f}   (tem de ser < 2)")
assert min(c['mu_rc2'] for c in med) > 1.0, "corolario falhou: mu r_c^2 <= 1"
assert max(c['razao_fix'] for c in med) < 2.0, "corolario falhou: razao >= 2"
say("  [COROLARIO OK]")
say("")

# invariancia em m^2 e M_eff^2 (a razao nao pode depender deles)
say("-" * 74)
say("[COROLARIO FECHADO 2] o locus de xi = 0, em forma fechada")
say("-" * 74)
say("")
say("  xi = 0  <=>  r W'(r) = 3 rho_til = 3 W(r). Com b0=b2=b3=0:")
say("      r W' - 3 W = -(b4 r^2 + 4 b1/r)/mu + 6 b1 r = 0")
say("  multiplicando por mu r:")
say("")
say("      b4 r^3 - 6 mu b1 r^2 + 4 b1 = 0        [locus de xi = 0]")
say("")
say("  Compare com o ponto fixo:  b4 r^3 - 3 mu b1 r^2 + b1 = 0.")
say("  Verificacao numerica (108 celulas): r no cruzamento medido pela")
say("  bisseccao vs raiz do polinomio fechado.")
say("")
say(f"  {'mu':>8} {'b4/b1':>10} {'r(xi=0) medido':>16} "
    f"{'r(xi=0) fechado':>17} {'|dif rel|':>11}")
_mx2 = 0.0
for c in med[::13]:
    cc = c['cel']
    a0 = c['a_xi0'][0]
    rt0v = rho_til_de_N(cc, np.log(a0), c['rho_til0'])
    r_med = cc.newton(raiz_por_continuacao(cc, rt0v, c['r_c'] * 2), rt0v)
    rr = np.roots([cc.b4, -6 * cc.mu * cc.b1, 0.0, 4 * cc.b1])
    cand = sorted(z.real for z in rr
                  if abs(z.imag) < 1e-9 and z.real > 0)
    r_fec = min(cand, key=lambda z: abs(z - r_med))
    d = abs(r_fec / r_med - 1.0)
    _mx2 = max(_mx2, d)
    say(f"  {cc.mu:8.4g} {cc.b4:10.5g} {r_med:16.9f} {r_fec:17.9f} "
        f"{d:11.2e}")
say("")
_all2 = 0.0
for c in med:
    cc = c['cel']
    a0 = c['a_xi0'][0]
    rt0v = rho_til_de_N(cc, np.log(a0), c['rho_til0'])
    r_med = cc.newton(raiz_por_continuacao(cc, rt0v, c['r_c'] * 2), rt0v)
    rr = np.roots([cc.b4, -6 * cc.mu * cc.b1, 0.0, 4 * cc.b1])
    cand = sorted(z.real for z in rr if abs(z.imag) < 1e-9 and z.real > 0)
    _all2 = max(_all2, abs(min(cand, key=lambda z: abs(z - r_med)) / r_med - 1))
say(f"  max |dif rel| sobre as 108 celulas = {_all2:.3e}")
assert _all2 < 1e-6, "COROLARIO 2 FALHOU: locus de xi=0 nao bate"
say("  [COROLARIO 2 OK]")
say("")

say("-" * 74)
say("[COROLARIO FECHADO 3] mu e' PURA REESCALA no IBB genuino")
say("-" * 74)
say("")
say("  A tabela mostra degenerescencia exata em mu a f = y/y_max fixo.")
say("  Causa, em forma fechada. Com b0=b2=b3=0, b1=1, ponha")
say("")
say("      r = mu^{-1/2} u,   b4/b1 = 2 mu^{3/2} f,   rho_chapeu = mu^{1/2} rho_til")
say("")
say("  A cubica (b4/mu) r^3 - 3 r^2 - rho_til r + 1/mu = 0 vira")
say("")
say("      2 f u^3 - 3 u^2 - rho_chapeu u + 1 = 0      [so' (f, rho_chapeu)]")
say("")
say("  e as tres quantidades medidas colapsam do mesmo jeito:")
say("      Omega_m   = 1 - 3 u^2/(2 f u^3 + 1)")
say("      m_T^2/H^2 = 3 (u^2 + chi/u)/(2 f u^3 + 1),  chi = u + du/dN")
say("  ambas funcao SO' de (f, rho_chapeu). Logo mu nao e' um eixo")
say("  fisico novo neste bloco de celulas: ele reescala r e a janela")
say("  de b4, e nada mais. (E' por isso que a varredura em mu -- a")
say("  lacuna apontada pelo parecer -- fecha o enunciado em vez de")
say("  abri-lo.)")
say("")
say("  Verificacao numerica: historias de m_T^2/H^2 a f fixo, mu variando")
say(f"  {'f':>8} {'max |razao(mu) - razao(mu=1)| sobre a grade':>48}")
_mx3 = 0.0
for fi, f in enumerate(FRAC_S):
    base = [c for c in med if c['frac'] == f and abs(c['mu'] - 1.0) < 1e-12]
    if not base:
        continue
    b = base[0]['razao']
    d = max(float(np.max(np.abs(c['razao'] - b)))
            for c in med if c['frac'] == f)
    _mx3 = max(_mx3, d)
    say(f"  {f:8.3f} {d:48.3e}")
say("")
say(f"  max sobre todos os f = {_mx3:.3e}")
assert _mx3 < 1e-9, "COROLARIO 3 FALHOU: mu nao e' pura reescala"
say("  [COROLARIO 3 OK] mu e' pura reescala; 9 valores de mu dao a")
say("                   MESMA fisica medida a f fixo.")
say("")

say("  Invariancia declarada: m_T^2/H^2 nao depende de m^2 nem de")
say("  M_eff^2. Teste (celula mu=1, y=1, a=1): reescalando m^2 por 7 e")
say("  M_g^2, M_f^2 por 3 (mu fixo),")
c_inv = Celula(0.0, 1.0, 0.0, 0.0, 1.0, 1.0)
rt0_inv = rho_til0_de_Omega(c_inv)
r_inv = c_inv.newton(c_inv.raizes(rt0_inv)[-1], rt0_inv)
xi_inv = c_inv.xi(r_inv, rt0_inv)
raz_a = c_inv.m_T2(r_inv, xi_inv) / c_inv.H2_f(r_inv)
c_inv2 = Celula(0.0, 1.0, 0.0, 0.0, 1.0, 1.0)
c_inv2.m2 = 7.0
c_inv2.Mg2 = 3.0
c_inv2.Mf2 = 3.0 * 1.0
c_inv2.Meff2 = 1.0 / (1.0 / c_inv2.Mg2 + 1.0 / c_inv2.Mf2)
raz_b = c_inv2.m_T2(r_inv, xi_inv) / c_inv2.H2_f(r_inv)
say(f"    razao original = {raz_a:.12f}")
say(f"    razao reescalada = {raz_b:.12f}   dif = {abs(raz_a-raz_b):.3e}")
assert abs(raz_a - raz_b) < 1e-12 * max(1.0, abs(raz_a)), \
    "invariancia falhou: m_T^2/H^2 depende de m^2/M_eff^2"
say("  [INVARIANCIA OK]")
say("")

# ---------------------------------------------------------------------
say("-" * 74)
say("[HISTORIA DETALHADA] tres celulas representativas")
say("-" * 74)
say("")
for alvo in [(1.0, 0.5), (1.0, 0.95), (0.1, 0.5)]:
    cand = min(med, key=lambda c: (abs(np.log(c['mu'] / alvo[0]))
                                   + abs(c['frac'] - alvo[1])))
    c = cand
    say(f"  celula: mu = {c['mu']:.4g}, b4/b1 = {c['y']:.4g} "
        f"(f = {c['frac']:.3g} de y_max = {y_max_fechado(c['mu']):.4g}), "
        f"r_c = {c['r_c']:.4f}")
    say(f"  {'a':>10} {'z':>9} {'r':>12} {'r prime':>13} {'xi':>13} "
        f"{'H^2':>12} {'m_T^2':>12} {'m_T^2/H^2':>11} {'Hig':>5}")
    for aval in [1e-4, 1e-3, 1e-2, 0.1, 0.3, 0.5, 1.0, 2.0, 5.0, 30.0]:
        i = int(np.argmin(np.abs(A_GRID - aval)))
        hg = "SIM" if c['mT2'][i] >= 2 * c['H2'][i] else "NAO"
        say(f"  {A_GRID[i]:10.4g} {1/A_GRID[i]-1:9.3f} {c['r'][i]:12.5g} "
            f"{c['drdN'][i]:13.5g} {c['xi'][i]:13.5g} {c['H2'][i]:12.5g} "
            f"{c['mT2'][i]:12.5g} {c['razao'][i]:11.5f} {hg:>5}")
    say(f"  xi cruza zero em a = "
        f"{', '.join(f'{x:.5f}' for x in c['a_xi0']) if c['a_xi0'] else 'nunca'}")
    say(f"  limite GR no passado: H^2/(rho/3M_g^2) em a=1e-4 = "
        f"{c['H2'][0]/(c['rt'][0]*c.get('cel').m2*c['cel'].Meff2/(3*c['cel'].Mg2)):.6f}")
    say("")

# ---------------------------------------------------------------------
say("-" * 74)
say("[B0] EIXO DE ROBUSTEZ -- b0 != 0 (fora do IBB genuino)")
say("-" * 74)
say("")
say("  O IBB da fonte tem b0 = 0 (sem constante cosmologica explicita")
say("  para g). Este eixo mede se ligar b0 muda o SINAL de r' ou o")
say("  enunciado de Higuchi. DECLARADO COMO SECUNDARIO.")
say("")
say(f"  {'b0':>7} {'mu':>6} {'b4':>6} {'r_c':>9} {'r<0 %':>7} "
    f"{'a(xi=0)':>10} {'raz@a=1':>9} {'raz max':>9} {'Hig':>9}")
for b0v in [0.0, 0.25, 0.5, 1.0, 2.0]:
    c = Celula(b0v, 1.0, 0.0, 0.0, 1.0, 1.0)
    rc, todas = r_c_infinito(c)
    if not np.isfinite(rc):
        say(f"  {b0v:7.3g} {1.0:6.3g} {1.0:6.3g}   sem ponto fixo positivo")
        continue
    rt0 = rho_til0_de_Omega(c)
    r = integra_ramo(c, N_GRID, rt0, sentido='infinito')
    rt = rho_til_de_N(c, N_GRID, rt0)
    d = c.drdN(r, rt)
    x = r + d
    H2 = c.H2_f(r)
    mT = c.m_T2(r, x)
    raz = mT / H2
    idx = np.where(np.sign(x[:-1]) != np.sign(x[1:]))[0]
    axi = float(np.exp(N_GRID[idx[0]])) if len(idx) else float('nan')
    say(f"  {b0v:7.3g} {1.0:6.3g} {1.0:6.3g} {rc:9.4f} "
        f"{100*np.mean(d < 0):7.1f} {axi:10.4f} {raz[i_hoje]:9.4f} "
        f"{np.max(raz):9.4f} {int(np.sum(mT >= 2*H2)):4d}/{len(raz):<4d}")
say("")

# ---------------------------------------------------------------------
_r13a = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                     '..', '..', 'docs',
                     'resultado_r13a_criterio_higuchi_fonte.md')
if os.path.exists(_r13a):
    say("=" * 74)
    say("[R-13a] CONFRONTO COM O CRITERIO DA FONTE -- o arquivo EXISTE")
    say("=" * 74)
    say("")
    say("  docs/resultado_r13a_criterio_higuchi_fonte.md existe nesta")
    say("  execucao e traduz o criterio de Konnig 1503.07436 eq.(14)/(15)")
    say("  para as nossas variaveis. CITADO, nao adotado como instrucao.")
    say("")
    say("  CAVEAT DE NIVEL, declarado pelo proprio R-13a (sec. 5): a")
    say("  traducao e' algebra a mao, NAO verificada por CAS. Tudo o que")
    say("  esta secao mede e' CONDICIONAL a ela.")
    say("")
    say("  Enunciado do R-13a (sec. 2.2 / 3.1), nas nossas variaveis:")
    say("")
    say("    Konnig (14)  <=>  m_T^2|_{xi->r} >= 2 H^2")
    say("      com  m_T^2|_{xi->r} = (m^2 M_eff^2/M_f^2) B(r) (1+mu r^2)/r")
    say("      e    B(r) = b1 + 2 b2 r + b3 r^2")
    say("    Konnig (15)  <=>  b1 + 3r^2(mu b1 - b3) + 2r^3(3 mu b2 - b4)")
    say("                        + 3 mu b3 r^4  >=  0")
    say("    Konnig (18)  <=>  r' >= 0     <=>   xi >= r")
    say("")
    say("  --- VERIFICACAO SIMBOLICA (fecha o item 1 da fila do R-13a) ---")
    say("")
    try:
        import sympy as sp
        _r, _mu = sp.symbols('r mu', positive=True)
        _b0, _b1, _b2, _b3, _b4 = sp.symbols('b0 b1 b2 b3 b4')
        _m2, _Me2, _Mf2 = sp.symbols('m2 Meff2 Mf2', positive=True)
        _Mg2 = _Mf2 / _mu
        _Vg = _b0 + 3*_b1*_r + 3*_b2*_r**2 + _b3*_r**3
        _Vf = _b4 + 3*_b3/_r + 3*_b2/_r**2 + _b1/_r**3
        _W = (_Mg2/_Mf2)*_r**2*_Vf - _Vg
        _Wp = sp.diff(_W, _r)
        _L15 = (_b1 + 3*_r**2*(_mu*_b1 - _b3)
                + 2*_r**3*(3*_mu*_b2 - _b4) + 3*_mu*_b3*_r**4)
        _res1 = sp.simplify(sp.expand(-_mu*_r**2*_Wp - _L15))
        say("  (i) r' >= 0  <=>  W'(r) <= 0  (pois r' = -3 rho_til/W', rho_til>0)")
        say("      e  -mu r^2 W'(r)  ==  LHS da (15) traduzida ?")
        say(f"      residuo simbolico = {_res1}")
        # (ii) m_T^2 com xi->r reproduz a caixa do R-13a
        _xi = sp.Symbol('xi')
        _mT2 = (_m2*_Me2*(1/_Mg2 + _xi/(_Mf2*_r**3))*_r
                * (_b1 + _b2*(_xi + _r) + _b3*_xi*_r))
        _mT2_r = _mT2.subs(_xi, _r)
        _cx = (_m2*_Me2/_Mf2)*(_b1 + 2*_b2*_r + _b3*_r**2)*(1 + _mu*_r**2)/_r
        _res2 = sp.simplify(sp.expand(_mT2_r - _cx))
        say("  (ii) a caixa do cap.06 com xi->r  ==  a caixa do R-13a sec.2.2 ?")
        say(f"      residuo simbolico = {_res2}")
        # (iii) a inequacao (14) traduzida <=> LHS(15) >= 0
        _H2 = _m2*_Me2*_r**2*_Vf/(3*_Mf2)
        _res3 = sp.simplify(sp.expand(
            sp.together((_cx - 2*_H2) * 3*_Mf2*_r/(_m2*_Me2)) - _L15))
        say("  (iii) (m_T^2|_{xi->r} - 2H^2) * 3 M_f^2 r/(m^2 M_eff^2)")
        say("        ==  LHS da (15) traduzida ?")
        say(f"      residuo simbolico = {_res3}")
        say("      [nota de rodada: a 1a versao deste teste usou o fator")
        say("       r^2 em vez de r e REPROVOU, com residuo (r-1)*LHS(15).")
        say("       O erro era do fator deste script, nao da traducao do")
        say("       R-13a. Registrado, nao escondido (regra 2).]")
        assert _res1 == 0 and _res2 == 0 and _res3 == 0, \
            "R-13a: a traducao NAO fecha simbolicamente"
        say("")
        say("  [R-13a VERIFICADO POR CAS] os tres residuos sao ZERO, para")
        say("  beta_n e mu GERAIS (materia = poeira). A cadeia")
        say("      Konnig(14) <=> Konnig(15) <=> W'(r) <= 0 <=> r' >= 0")
        say("  e' EXATA nas convencoes deste projeto, e sai da NOSSA")
        say("  maquinaria (W(r) e dr/dN = -3 rho_til/W') por rota")
        say("  independente da algebra a mao do R-13a. Isso fecha a")
        say("  fronteira epistemica que o R-13a declara na sua sec. 5 e")
        say("  lista como item 1 da sua fila -- para o caso de poeira.")
        _r13a_cas = True
    except Exception as _e:                       # noqa: BLE001
        say(f"  [FALHA na verificacao simbolica] {_e}")
        say("  A comparacao abaixo fica sem o selo de CAS.")
        _r13a_cas = False
    say("")
    say("  --- MEDIDA do criterio da FONTE nas 108 celulas IBB ---")
    say("")
    say("  m_T^2|_{xi->r}/H^2 = 3 B(r)(1+mu r^2)/(r^3 V_f(r))")
    say("  (com b2=b3=0: = 3 b1 (1+mu r^2)/(b4 r^3 + b1))")
    say("")
    say(f"  {'mu':>7} {'b4/b1':>9} {'razF@a=1':>10} {'razF max':>10} "
        f"{'razF@fix':>10} {'Hig(fonte)':>12} {'r prime>=0':>12} "
        f"{'sinais batem':>14}")
    _sig_tot, _sig_ok = 0, 0
    for c in med[::9]:
        cc = c['cel']
        r = c['r']
        H2 = c['H2']
        mTr = (cc.m2*cc.Meff2/cc.Mf2)*(cc.b1 + 2*cc.b2*r + cc.b3*r**2) \
            * (1 + cc.mu*r**2)/r
        razF = mTr/H2
        higF = mTr >= 2*H2
        rl = c['drdN'] >= 0
        bate = int(np.sum(higF == rl))
        say(f"  {cc.mu:7.3g} {cc.b4:9.4g} {razF[i_hoje]:10.5f} "
            f"{float(np.max(razF)):10.5f} {1+1/(cc.mu*c['r_c']**2):10.5f} "
            f"{int(np.sum(higF)):5d}/{len(razF):<6d} "
            f"{int(np.sum(rl)):5d}/{len(rl):<6d} {bate:6d}/{len(rl):<7d}")
    for c in med:
        cc = c['cel']
        r = c['r']
        H2 = c['H2']
        mTr = (cc.m2*cc.Meff2/cc.Mf2)*(cc.b1 + 2*cc.b2*r + cc.b3*r**2) \
            * (1 + cc.mu*r**2)/r
        _sig_tot += len(r)
        _sig_ok += int(np.sum((mTr >= 2*H2) == (c['drdN'] >= 0)))
    say("")
    say(f"  Concordancia de sinal Higuchi(fonte) <=> r' >= 0, sobre TODAS")
    say(f"  as 108 celulas: {_sig_ok}/{_sig_tot} pontos.")
    assert _sig_ok == _sig_tot, "R-13a: (14) e (18) discordam numericamente"
    say("")
    say("  ** PODER DESTE TESTE DE CONCORDANCIA (regra 3) **")
    say("  No ramo infinito os DOIS lados sao falsos em todo ponto, logo")
    say("  a concordancia 64800/64800 seria trivial sozinha. O teste so'")
    say("  tem poder se houver um caso onde os dois sao VERDADEIROS:")
    say("  o ramo FINITO do controle positivo (r' = 3r > 0 no primordial).")
    mTr_pc = (cel_pc.m2*cel_pc.Meff2/cel_pc.Mf2) \
        * (cel_pc.b1 + 2*cel_pc.b2*r_pc + cel_pc.b3*r_pc**2) \
        * (1 + cel_pc.mu*r_pc**2)/r_pc
    razF_pc = mTr_pc/H2_pc
    bate_pc = int(np.sum((mTr_pc >= 2*H2_pc) == (drdN_pc >= 0)))
    say(f"    r' >= 0 no controle          : "
        f"{int(np.sum(drdN_pc >= 0))}/400")
    say(f"    Higuchi(fonte) no controle   : "
        f"{int(np.sum(mTr_pc >= 2*H2_pc))}/400")
    say(f"    concordancia                 : {bate_pc}/400")
    say(f"    m_T^2|_(xi->r)/H^2 primordial: {razF_pc[0]:.6f}")
    say(f"    (contra m_T^2/H^2 = {mT2_pc[0]/H2_pc[0]:.4f} com xi dinamico)")
    assert bate_pc == 400, "PODER: o teste falha no caso verdadeiro"
    assert int(np.sum(mTr_pc >= 2*H2_pc)) == 400, \
        "PODER: o criterio da fonte deveria PASSAR no ramo finito"
    say("  [PODER OK] o teste distingue VERDADEIRO de FALSO: aprova o")
    say("             ramo finito e reprova o infinito, pelas duas formas.")
    say("")
    say("  >>> CONFIRMACAO NUMERICA de uma previsao do R-13a sec.3.2 que")
    say("      ele declara como NAO re-verificada numericamente: no ramo")
    say("      finito primordial o objeto de Konnig da' m_T^2/H^2 -> 3")
    say(f"      (contra 12 com xi dinamico). Medido: {razF_pc[0]:.6f} vs "
        f"{mT2_pc[0]/H2_pc[0]:.4f}.")
    assert abs(razF_pc[0] - 3.0) < 5e-3, "R-13a sec.3.2 (o '3') nao bate"
    say("")
    say("  LEITURA (medida, nao veredito):")
    say("   - o criterio da fonte, traduzido, e' REPROVADO em todos os")
    say("     pontos de todas as 108 celulas -- pelas DUAS formas")
    say("     equivalentes (a inequacao e o sinal de r'), que concordam")
    say("     ponto a ponto;")
    say("   - as duas formas de razao coincidem no PONTO FIXO (onde")
    say("     xi = r, logo m_T^2 = m_T^2|_{xi->r}) e divergem fora dele;")
    say("   - o supremo das DUAS e' 1 + 1/(mu r_c^2) < 2.")
    say("")
    say("  O QUE ISTO **NAO** DIZ (proibicoes de escopo, mantidas):")
    say("   - NAO conclui exclusao nem aprovacao do IBB. A fonte emite")
    say("     veredito proprio sobre o IBB DELA (R-13a sec.1.5); este")
    say("     script mede a F1 com b4 ligado e para ai.")
    say("   - a traducao do R-13a e' algebra a mao (sec.5); a cadeia")
    say("     (14)<=>(15)<=>(18) fica verificada por CAS aqui, mas o MAPA")
    say("     de convencoes do R-13a sec.2.1 (r_K = sqrt(mu) r,")
    say("     beta_n^K = A mu^{-n/2} beta_n) NAO foi reverificado neste")
    say("     script -- ele e' a entrada, nao a saida.")
    say("   - continua CEGO a gradiente/c_s^2 (sec. de cegueira).")
    say("")

say("=" * 74)
say("O QUE FOI MEDIDO, E SO' ISSO")
say("=" * 74)
say("")
say("  Medido (numeros acima, todos deste script):")
say("    - sinal de r' ao longo da historia, por celula;")
say("    - onde xi = r + dr/dN cruza zero, por celula;")
say("    - m_T^2/H^2 pela forma fechada do cap. 06, por celula e epoca;")
say("    - a inequacao DO REPOSITORIO, m_T^2 >= 2H^2, por ponto;")
say("    - a fronteira de existencia do ramo infinito em (b4/b1, mu).")
say("")
if os.path.exists(_r13a):
    say("    - o criterio da FONTE, na traducao do R-13a, medido nas 108")
    say("      celulas (secao [R-13a]); e a cadeia (14)<=>(15)<=>(18)")
    say("      verificada por CAS a partir da NOSSA maquinaria.")
say("")
say("  NAO medido / NAO concluido (regra 7 e proibicoes do escopo):")
if not os.path.exists(_r13a):
    say("    - o criterio de Higuchi DA FONTE (1503.07436) nao foi")
    say("      traduzido nem aplicado aqui. A comparacao depende de")
    say("      docs/resultado_r13a_criterio_higuchi_fonte.md, que e' outro")
    say("      processo. STATUS ABAIXO.")
else:
    say("    - o MAPA de convencoes do R-13a sec.2.1 (r_K = sqrt(mu) r,")
    say("      beta_n^K = A mu^{-n/2} beta_n) e' ENTRADA deste script, nao")
    say("      saida: nao foi reverificado aqui. O que foi verificado por")
    say("      CAS e' a cadeia interna (14)<=>(15)<=>(18) nas NOSSAS")
    say("      variaveis, dado esse mapa.")
    say("    - a leitura interpretativa do R-13a sec.3.2 (bound de FLRW =")
    say("      bound de de Sitter no fundo proporcional instantaneo) e'")
    say("      inferencia declarada la', e nao e' testada aqui.")
say("    - NENHUM veredito de exclusao ou aprovacao do IBB e' emitido")
say("      por este script.")
say("    - c_s^2 / estabilidade de gradiente: NAO MEDIDO. Este gate e'")
say("      CEGO a esse canal, por construcao.")
say("    - fantasma escalar, EFT, screening, f*sigma_8: NAO MEDIDOS.")
say("")
_r13a = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                     '..', '..', 'docs',
                     'resultado_r13a_criterio_higuchi_fonte.md')
if os.path.exists(_r13a):
    say("  R-13a: docs/resultado_r13a_criterio_higuchi_fonte.md EXISTE.")
    say("         A comparacao com o criterio da fonte deve ser feita")
    say("         no documento do R-13b, citando-o.")
else:
    say("  R-13a: docs/resultado_r13a_criterio_higuchi_fonte.md NAO")
    say("         EXISTE nesta execucao. A comparacao com o criterio da")
    say("         fonte fica DECLARADA COMO PENDENTE e NAO foi simulada.")
say("")
say("=" * 74)

# ---------------------------------------------------------------------
_out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out')
os.makedirs(_out, exist_ok=True)
_dst = os.path.join(_out, 'r13b_ibb_ramo_infinito.txt')
with open(_dst, 'w', encoding='utf-8') as fh:
    fh.write("\n".join(LINHAS) + "\n")
print(f"\n[saida versionada] {_dst}")
