# Environments_Packaging.py
# Reference Guide: Environment Management (venv, poetry, uv, pyenv) and Packaging (pyproject.toml, PyPI)

# ==========================================
# 1. ENVIRONMENT MANAGEMENT
# ==========================================
# Managing Python versions and project dependencies isolates your workspace.

# --- venv (Built-in Virtual Environment) ---
# Creation:
#   `python -m venv .venv`
# Activation:
#   Windows: `.venv\Scripts\activate`
#   Mac/Linux: `source .venv/bin/activate`
# Deactivation:
#   `deactivate`

# --- poetry (Dependency & Package Manager) ---
# Modern tool replacing pip and requirements.txt with a lockfile.
# Commands:
#   Initialize: `poetry init`
#   Add dep:    `poetry add requests`
#   Shell:      `poetry shell`
#   Run script: `poetry run python script.py`

# --- uv (Ultra-fast Python Package Installer) ---
# Rust-based pip replacement, extremely fast.
# Commands:
#   Install uv:  `pip install uv`
#   Install dep: `uv pip install numpy`
#   Create venv: `uv venv`

# --- pyenv (Python Version Management) ---
# Allows installing and switching between multiple Python runtime versions globally/locally.
# Commands:
#   Install version: `pyenv install 3.12.0`
#   Set local:       `pyenv local 3.12.0`
#   Show versions:   `pyenv versions`

# ==========================================
# 2. PACKAGING (pyproject.toml, PyPI)
# ==========================================
# Modern Python packaging uses `pyproject.toml` instead of `setup.py`.

# --- pyproject.toml Template Example ---
# [build-system]
# requires = ["setuptools>=61.0.0", "wheel"]
# build-backend = "setuptools.build_meta"
#
# [project]
# name = "my_awesome_package"
# version = "0.1.0"
# description = "An educational demo package for Python features"
# readme = "README.md"
# requires-python = ">=3.8"
# dependencies = [
#     "requests>=2.28.0",
# ]
#
# [project.urls]
# Homepage = "https://github.com/user/my_awesome_package"

# --- Publishing to PyPI ---
# 1. Build the distribution files:
#    `python -m build` (generates sdist and wheel in dist/)
# 2. Upload using twine:
#    `twine upload dist/*`
print("Environments_Packaging documentation references configured!")
