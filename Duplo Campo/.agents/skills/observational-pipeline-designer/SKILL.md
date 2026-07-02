---
name: observational-pipeline-designer
description: Convert TDCP theory into observational and computational tests. Use when designing mu(k,a), Sigma(k,a), eta_slip, f sigma_8, P(k,z), BAO, RSD, weak lensing, CLASS/CAMB implementation notes, parameter degeneracies, benchmark choices, and distinctiveness checks against LambdaCDM.
---

# Observational Pipeline Designer

## When to Use This Skill

Use this skill when turning TDCP formalism into measurable predictions, likelihood inputs, numerical pipeline plans, or comparison strategies against LambdaCDM and common dark-energy or modified-gravity models.

## What the Skill Must Check or Produce

- Effective modified-gravity functions mu(k,a), Sigma(k,a), and eta_slip(k,a).
- Growth observable f sigma_8(z).
- Matter power spectrum P(k,z) and scale dependence.
- BAO distance observables and background expansion quantities.
- Weak lensing kernels and lensing potential modifications.
- RSD scale-dependence and growth-rate predictions.
- CLASS or CAMB implementation notes, including background and perturbation hooks.
- Degeneracies with w0-wa, neutrino mass, Omega_m, H0, and sigma8.
- Benchmark choices such as m_S0 ~ 30-300 H0 when targeting k ~ 0.01-0.1 h/Mpc.
- Explicit warning when a proposed observable is not actually distinctive.

## What the Skill Must Not Do

- Do not call a prediction testable without specifying an observable.
- Do not claim distinguishability from LambdaCDM without a scale, redshift, or likelihood handle.
- Do not hide degeneracies with standard cosmological parameters.
- Do not propose CLASS/CAMB work without identifying which equations or functions must be implemented.
- Do not treat background-only agreement as full observational viability.

## Required Output Format

Return:

1. **Pipeline Verdict:** Ready for implementation / Needs formal inputs / Not yet testable.
2. **Observable Map:** Theory quantity to observable, with k and z dependence when relevant.
3. **Implementation Notes:** CLASS/CAMB or numerical steps.
4. **Likelihood Targets:** BAO, RSD, weak lensing, CMB, or other datasets.
5. **Degeneracy and Distinctiveness Check:** What can mimic the signal.

## Common Failure Modes

- Proposing mu and Sigma without defining the perturbation regime.
- Ignoring eta_slip when discussing lensing versus growth.
- Treating f sigma_8 as scale-independent when TDCP predicts scale dependence.
- Omitting nuisance or degeneracy parameters.
- Choosing benchmarks outside the EFT or stability regime.

## Checklist

- mu(k,a) defined?
- Sigma(k,a) defined?
- eta_slip defined?
- f sigma_8 and P(k,z) connected?
- BAO/RSD/WL targets specified?
- CLASS/CAMB hooks identified?
- Degeneracies listed?
- Distinctive signal stated?
