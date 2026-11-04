# Tutorial 2a: Poisson statistics for dust-clump detection

Open poisson_dust_clumps.ipynb to work through the lesson, or
poisson_dust_clumps.html to read its saved outputs in a browser.

## Scope

Count equal-weight tracers in a synthetic two-dimensional disk patch. Compare a
uniform Poisson null model with two injected Gaussian concentrations. The
coordinates are measured relative to a chosen gas pressure scale height H; the
particle density is a numerical tracer density, not a physical dust surface
density.

No external data downloads, simulation code, or astronomical image processing
are required. Running the notebook recreates the bundled data and figures.
All figures use the requested matplotidlib theme, including its typography,
four-sided axes, inward ticks, and categorical color cycle. The selected font is
recorded in the data provenance.

## Correspondence with the textbook

The order follows Ting (2026), Tutorial 2a, printed pages 563-591:

| Textbook step | This adaptation |
| --- | --- |
| Stellar clusters and a smooth star field | Dust concentrations and a uniform tracer field |
| Prerequisites and objectives | The same probability and array-programming prerequisites |
| Uniform stellar background | Homogeneous Poisson process in a dimensionless disk patch |
| Random variables and annular counts | Expected tracer density versus measured particle counts |
| Poisson histograms and periodic geometry | Annular histograms, area scaling, and a boundary experiment |
| Joint and conditional distributions | Annuli in independent spatial realizations |
| Gaussian cluster injection | Two Gaussian dust concentrations with known truth |
| Count likelihoods and a spatial likelihood map | The same likelihood construction, plus an upper-tail map |
| Choice of scale and null assumptions | Aperture-scale comparison and limitations for disk physics |
| Maximum likelihood estimation | Poisson rate estimation from disjoint control-field cells |
| Summary | Interpretation, exercises, and scientific references |

Three statistical distinctions are made explicit:

- The total background count is drawn from a Poisson distribution. Conditioning
  on a fixed total would instead produce binomial or multinomial region counts.
- Disjoint annuli at one fixed center have independent Poisson counts, but
  overlapping apertures around many centers are not independent measurements.
  The joint-distribution exercise therefore uses independent realizations.
- The probability of exactly the observed count is not an upper-tail
  probability. Both are displayed. A conservative whole-map threshold is applied
  only for the known null rate and the prespecified main aperture.

The MLE uses an independent control field divided into non-overlapping cells,
so its likelihood genuinely factors. Truth labels are reserved for evaluation;
the detector and control-rate estimator do not use them.

## Scientific context

- Youdin & Goodman (2005), *Streaming Instabilities in Protoplanetary Disks*:
  https://arxiv.org/abs/astro-ph/0409263
- Johansen & Youdin (2007), *Protoplanetary Disk Turbulence Driven by the Streaming
  Instability: Non-Linear Saturation and Particle Concentration*:
  https://arxiv.org/abs/astro-ph/0702626

The injected clumps are teaching models. They contain no gas dynamics, drag,
self-gravity, collisions, or dust-size distribution. A statistically significant
concentration does not establish streaming instability or gravitational collapse.
