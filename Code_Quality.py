# Code_Quality.py
# Reference Guide: Linting, Formatting, and Pre-commit Hooks (Ruff, Black, pre-commit)

# ==========================================
# 1. FORMATTING WITH BLACK
# ==========================================
# Black is an opinionated code formatter that enforces uniform style.
# Installation:
#   `pip install black`
# Usage:
#   Format a file: `black script.py`
#   Check format:  `black --check script.py`

# ==========================================
# 2. LINTING WITH RUFF
# ==========================================
# Ruff is an extremely fast Python linter and formatter written in Rust.
# It replaces Flake8, autopep8, isort, and other linters.
# Installation:
#   `pip install ruff`
# Usage:
#   Lint check: `ruff check .`
#   Auto-fix:   `ruff check . --fix`
#   Format:     `ruff format .`

# ==========================================
# 3. PRE-COMMIT HOOKS
# ==========================================
# pre-commit runs formatting and lint checks automatically before every git commit.
#
# Setup:
# 1. Install: `pip install pre-commit`
# 2. Create config file `.pre-commit-config.yaml` in repository root:
#
# --- YAML Config Example ---
# repos:
#   - repo: https://github.com/pre-commit/pre-commit-hooks
#     rev: v4.4.0
#     hooks:
#       - id: trailing-whitespace
#       - id: end-of-file-fixer
#       - id: check-yaml
#   - repo: https://github.com/psf/black
#     rev: 23.3.0
#     hooks:
#       - id: black
#   - repo: https://github.com/astral-sh/ruff-pre-commit
#     rev: v0.0.270
#     hooks:
#       - id: ruff
#         args: [--fix]
# ---
# 3. Install hooks: `pre-commit install`
print("Code_Quality documentation references configured!")
