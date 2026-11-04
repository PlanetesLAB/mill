# Mills

**Statistics and machine learning for planet formation.**

Python notebooks adapting the statistical topics and teaching progression of
Yuan-Sen Ting's *Statistical Machine Learning for Astronomy* to planet formation
and protoplanetary disks. Each tutorial includes its data, provenance, figures,
scientific references, and numerical checks.

## Tutorials

| Book tutorial | Mills adaptation | Open |
| --- | --- | --- |
| 2a | Poisson statistics for dust-clump detection | [Notebook](tutorials/02a_poisson_dust_clumps/poisson_dust_clumps.ipynb) · [HTML](tutorials/02a_poisson_dust_clumps/poisson_dust_clumps.html) |
| 2b | Bayesian inference for a young planet's eccentricity | [Notebook](tutorials/02b_bayesian_planet_eccentricity/bayesian_planet_eccentricity.ipynb) · [HTML](tutorials/02b_bayesian_planet_eccentricity/bayesian_planet_eccentricity.html) |

Tutorial 2a uses synthetic spatial tracer counts. Tutorial 2b uses a synthetic
kinematic observation for inference and includes published PDS 70 astrometry as
an explicitly separate observational example. Neither notebook presents a toy
model as a reproduction of a published simulation or planet-orbit analysis.

## Run with uv

Dependencies are declared in pyproject.toml and resolved in uv.lock. The
.python-version file selects Python 3.13; the project supports Python 3.11+.
From this repository:

    uv sync --locked
    uv run jupyter lab

Open a notebook under tutorials and use the Mills environment's Python kernel.
Run all cells from the beginning to recreate its data, figures, provenance,
and numerical verification report.

To execute one tutorial and refresh its HTML:

    uv run python scripts/verify_tutorial.py 2a
    uv run python scripts/verify_tutorial.py 2b

To check all currently available tutorials:

    uv run python scripts/verify_tutorial.py all

After installation, the notebook calculations need no network access. The HTML
previews embed their figures and load MathJax from a public CDN to typeset
equations. The HTML versions can be read without running Python.

## Run in the browser

The GitHub Pages build serves the notebooks directly through JupyterLite.
Open a notebook under `tutorials` and choose **Run → Run All Cells**. Python runs
in your browser; no local installation or notebook server is needed. The first
launch downloads the Python runtime and packages. Download your edited notebook
to keep a copy; browser changes do not update this repository.

To publish, enable **Settings → Pages → Source → GitHub Actions**, then push the
build setup to `main` (or run **Build and deploy notebooks** from Actions).
The deployed address will be <https://planeteslab.github.io/mills/>.
Pull requests build the site without deploying it.

To build and preview locally:

    uv sync --locked --extra web
    uv run --locked --extra web python scripts/build_site.py
    uv run python -m http.server --directory _site

Open <http://localhost:8000/>. The build discovers tutorial notebooks and bundles
their neighboring data folders automatically. It adds a plotting-package setup
cell to browser copies, using the same pinned matplotidlib source. Source
notebooks and their saved HTML are unchanged. Pyodide supplies browser-compatible
NumPy, SciPy, and Matplotlib; `uv.lock` defines the native reference environment.

This setup is only for runnable notebooks. The planned mdBook presentation layer
can be added later. Future tutorials with packages unavailable in Pyodide will
need a different execution backend.

## Plot style

All figures use [PlanetesLAB/matplotidlib](https://github.com/PlanetesLAB/matplotidlib).
Its source revision is pinned in pyproject.toml and uv.lock. The package selects
an installed Hershey font when available and supplies a portable fallback.
The selected font and software versions are recorded in each tutorial's
data/provenance.json.

## Data and reproducibility

Each data folder explains its files, units, sources, and generating assumptions.
Synthetic data include fixed seeds. The observed rows in Tutorial 2b retain their
published uncertainties and correlations and are clearly distinguished from the
mock data. CSVs and model grids have SHA-256 hashes in provenance.

The notebook assertions and verification.json reports check numerical identities,
probability normalization, geometry, and tutorial-specific inference results.
See the individual README files for teaching correspondence and scope.

## Attribution

These are independently written educational adaptations. The user-supplied
textbook provides the statistical progression and is not redistributed.
Scientific references are cited in each notebook. Data reuse is attributed at
the point where it enters the lesson.
