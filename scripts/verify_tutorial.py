"""Execute a Mills tutorial (or all), validate its checks, and refresh HTML."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import sys
import tempfile

import nbformat
from nbclient import NotebookClient
from nbconvert import HTMLExporter
from traitlets.config import Config

TUTORIALS = {
    "2a": ("02a_poisson_dust_clumps", "poisson_dust_clumps"),
    "2b": ("02b_bayesian_planet_eccentricity", "bayesian_planet_eccentricity"),
}


def verify(root: Path, key: str) -> None:
    folder, stem = TUTORIALS[key]
    directory = root / "tutorials" / folder
    path = directory / f"{stem}.ipynb"
    notebook = nbformat.read(path, as_version=4)
    nbformat.validate(notebook)
    os.environ["PATH"] = str(Path(sys.executable).parent) + os.pathsep + os.environ["PATH"]
    cache = root / ".cache" / "matplotlib"
    cache.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="mills-jupyter-") as runtime:
        os.environ["JUPYTER_RUNTIME_DIR"] = runtime
        os.environ["IPYTHONDIR"] = runtime
        os.environ["MPLCONFIGDIR"] = str(cache)
        client = NotebookClient(
            notebook, timeout=180, startup_timeout=90, kernel_name="python3",
            resources={"metadata": {"path": str(directory)}},
        )
        client.execute()
    nbformat.validate(notebook)
    code_cells = [c for c in notebook.cells if c.cell_type == "code"]
    if not code_cells or any(c.execution_count is None for c in code_cells):
        raise RuntimeError("Some code cells were not executed.")
    errors = [o for c in code_cells for o in c.get("outputs", []) if o.output_type == "error"]
    if errors:
        raise RuntimeError(errors)
    report = json.loads((directory / "verification.json").read_text())
    if not report["all_passed"]:
        raise RuntimeError(report)
    nbformat.write(notebook, path)
    config = Config()
    config.HTMLExporter.embed_images = True
    html, _ = HTMLExporter(config=config, template_name="lab").from_notebook_node(notebook)
    path.with_suffix(".html").write_text(html, encoding="utf-8")
    print(f"{key}: {len(code_cells)} cells executed; {len(report['checks'])} checks passed; "
          f"{len(list((directory / 'figures').glob('*.png')))} figures. HTML refreshed.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("tutorial", nargs="?", choices=[*TUTORIALS, "all"], default="2a")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    for key in TUTORIALS if args.tutorial == "all" else [args.tutorial]:
        verify(root, key)


if __name__ == "__main__":
    main()
