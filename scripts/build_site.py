"""Build the runnable notebooks for GitHub Pages; leave source notebooks intact."""

from __future__ import annotations

import copy
from pathlib import Path
import shutil
import subprocess
import sys
import tarfile
import tomllib
from urllib.request import urlretrieve

import nbformat

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".site-build"
OUTPUT = ROOT / "_site"


def plotting_wheel() -> Path:
    """Bundle the same pinned matplotidlib source used by the uv environment."""
    project = tomllib.loads((ROOT / "pyproject.toml").read_text())
    source = project["tool"]["uv"]["sources"]["matplotidlib"]
    if source["git"] != "https://github.com/PlanetesLAB/matplotidlib.git":
        raise ValueError("Update the wheel builder for the new plotting source.")
    revision = source["rev"]
    if len(revision) != 40 or any(c not in "0123456789abcdef" for c in revision):
        raise ValueError("Pin matplotidlib to a full commit hash.")
    destination = WORK / "wheels" / revision
    wheels = list(destination.glob("matplotidlib-*-py3-none-any.whl"))
    if len(wheels) != 1:
        archive = WORK / f"matplotidlib-{revision}.tar.gz"
        urlretrieve(f"https://codeload.github.com/PlanetesLAB/matplotidlib/tar.gz/{revision}", archive)
        source_dir = WORK / "sources"
        source_dir.mkdir(exist_ok=True)
        with tarfile.open(archive) as bundle:
            bundle.extractall(source_dir, filter="data")
        subprocess.run([
            "uv", "build", "--wheel", "--python", sys.executable,
            "--out-dir", str(destination), str(source_dir / f"matplotidlib-{revision}"),
        ], check=True)
        wheels = list(destination.glob("matplotidlib-*-py3-none-any.whl"))
    if len(wheels) != 1:
        raise RuntimeError("Expected one portable matplotidlib wheel.")
    return wheels[0]


def main() -> None:
    WORK.mkdir(exist_ok=True)
    contents = WORK / "contents"
    config = WORK / "config"
    for directory in (contents, config, OUTPUT):
        if directory.exists():
            shutil.rmtree(directory)
        directory.mkdir(parents=True)
    shutil.copy2(ROOT / "web" / "jupyter-lite.json", config / "jupyter-lite.json")
    notebooks = sorted((ROOT / "tutorials").glob("*/*.ipynb"))
    if not notebooks:
        raise RuntimeError("No tutorial notebooks found.")
    for path in notebooks:
        destination = contents / path.parent.relative_to(ROOT)
        destination.mkdir(parents=True)
        notebook = copy.deepcopy(nbformat.read(path, as_version=4))
        # Keep the scientific cells unchanged. Only the browser copy gets setup.
        setup_index = next(i for i, cell in enumerate(notebook.cells) if cell.cell_type == "code")
        notebook.cells.insert(setup_index, nbformat.v4.new_code_cell(
            "# Install the bundled plotting style in browser Python.\n"
            "import sys\n"
            "if sys.platform == 'emscripten':\n"
            "    import piplite\n"
            "    await piplite.install('matplotidlib')\n",
            metadata={"jupyter": {"source_hidden": True}},
        ))
        notebook.metadata.kernelspec = {
            "display_name": "Python (Pyodide)", "language": "python", "name": "python",
        }
        nbformat.validate(notebook)
        nbformat.write(notebook, destination / path.name)
        # Notebook-relative paths must work in the browser's virtual filesystem.
        shutil.copytree(path.parent / "data", destination / "data")
    subprocess.run([
        sys.executable, "-m", "jupyter", "lite", "build",
        "--lite-dir", str(config), "--contents", str(contents),
        "--output-dir", str(OUTPUT), "--piplite-wheels", str(plotting_wheel()),
    ], check=True, cwd=WORK)
    (OUTPUT / ".nojekyll").touch()
    for name in ("index.html", "lab/index.html", "jupyter-lite.json", "pypi/all.json"):
        if not (OUTPUT / name).is_file():
            raise RuntimeError(f"Missing site output: {name}")
    print(f"Built {len(notebooks)} runnable notebooks in {OUTPUT}")


if __name__ == "__main__":
    main()
