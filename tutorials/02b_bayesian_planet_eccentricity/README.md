# Tutorial 2b: Bayesian inference for a young planet's eccentricity

Open bayesian_planet_eccentricity.ipynb, or read the saved outputs in its HTML
version. From the repository, run:

    uv sync --locked
    uv run python scripts/verify_tutorial.py 2b

## Scope and acceptance checks

This phase adds one notebook and the uv project setup that supports it. Infer
eccentricity from a synthetic face-on position–velocity angle. Reproduce the
book's progression through forward modeling, phase integration, Bayes' theorem,
angular uncertainty, and projection limitations. Inspect four real PDS 70
astrometry rows separately; this is not a fit of the PDS 70 orbits.

Acceptance checks:

1. Execute every cell in a fresh kernel with the locked uv environment.
2. Check the vector-angle formula, Kepler's equation, orbital energy and angular
   momentum, and probability normalization.
3. Compare phase quadrature with independent Monte Carlo sampling and compare
   measurement marginalization in phase space and true-angle space.
4. Refine both eccentricity and phase grids and check posterior stability.
5. Validate the published covariance matrices and review every figure and the
   rendered HTML.
6. Re-execute and compare saved data hashes; rerun Tutorial 2a under uv.

## Teaching correspondence

Ting (2026), Tutorial 2b, printed pp. 593–616:

| Textbook step | Mills adaptation |
| --- | --- |
| Motivation from incomplete binary orbits | Incomplete young-planet orbits, with PDS 70 as context |
| Ellipse shapes and velocity vectors | The same Keplerian geometry for a star–planet relative orbit |
| Position–velocity angle formula | Closed formula checked against vectors and conserved quantities |
| Random-phase angle distribution | Both uniform true anomaly and uniformly timed sampling |
| Likelihood map | A normalized angle-density map from deterministic phase quadrature |
| Grid posterior for different angles | Finite-resolution angle likelihoods and central credible intervals |
| Measurement-error marginalization | Gaussian error integrated over phase and over the true angle |
| Real-analysis limitations | Prior sensitivity, a projection counterexample, and published astrometry |
| Summary | Interpretation, exercises, and references |

The main physical inference uses uniform mean anomaly (uniform time), rather
than uniform true anomaly. Both choices are demonstrated explicitly. Exactly
zero error is replaced by a stated one-degree bin in the introductory limit.
Credible intervals are central/equal-tailed, not highest-density intervals.
The eccentricity domain ends at 0.995; sensitivity to that choice is an exercise.

## References

- Ting (2026), *Statistical Machine Learning for Astronomy*, Tutorial 2b.
- Hwang, Ting & Zakamska (2022), MNRAS 512, 3383:
  https://doi.org/10.1093/mnras/stac675
- Wang et al. (2021), AJ 161, 148:
  https://arxiv.org/abs/2101.04187
- Plot styling: https://github.com/PlanetesLAB/matplotidlib
