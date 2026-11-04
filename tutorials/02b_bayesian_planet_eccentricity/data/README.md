# Data sources and schema

The notebook recreates the files in this directory without network access.
The provenance file records hashes, parameters, seeds, and package versions.

| File | Type | Contents |
| --- | --- | --- |
| mock_observation.json | Synthetic | Known orbit, random seed, true and measured angle, uncertainty |
| eccentricity_posterior.csv | Derived from mock | Eccentricity, likelihood per degree, posterior density, CDF |
| phase_draws.csv | Synthetic | 10,000 example mean/eccentric/true anomalies in radians, angle in degrees; e=0.6 |
| angle_likelihood_grid.npz | Synthetic model | Eccentricity grid, angle-bin edges in degrees, density per degree; uniform-time phase model |
| pds70_gravity_astrometry.csv | Published observations | Four rows transcribed from Wang et al. (2021), Table 2 |
| provenance.json | Metadata | Sources, units, generating assumptions, versions, and hashes |

The mock likelihood assumes a face-on orbit, uniform observation time, Gaussian
angle error, and a uniform eccentricity prior on [0, 0.995]. Orbit vectors use
a=1 and GM=1; these are normalized model units, not fitted PDS 70 quantities.

The astrometry columns are planet, MJD in days, relative RA/Dec offsets in mas,
their 1-sigma uncertainties in mas, and their within-epoch correlation coefficient.
The published numbers are transcribed directly in a visible notebook cell, with
all tabulated digits retained.

Source: Wang et al. (2021), *Constraining the Nature of the PDS 70 Protoplanets
with VLTI/GRAVITY*, AJ 161, 148, Table 2:
https://arxiv.org/html/2101.04187v2

The real astrometry is used only to illustrate measured quantities and the
geometry required for a real analysis. It is not used in the mock posterior.
The notebook does not reproduce the paper's eccentricity inference.
