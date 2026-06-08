# Scripting_Automation.py
# Reference Guide: Subprocess execution and Command-line parsing with click and typer
import subprocess

# ==========================================
# 1. SUBPROCESS MODULE
# ==========================================
# subprocess runs operating system shell commands and collects outputs.
print("--- 1. SUBPROCESS SHELL RUN ---")

try:
    # run command, check=True raises CalledProcessError if return code is non-zero
    result = subprocess.run(
        ["echo", "Hello from Subprocess!"],
        capture_output=True,
        text=True,
        check=True,
        shell=True # needed for windows shell command matching
    )
    print(f"Stdout: {result.stdout.strip()}")
    print(f"Status Code: {result.returncode}")
except subprocess.CalledProcessError as e:
    print(f"Process failed with error: {e}")
except Exception as e:
    print(f"Unexpected execution issue: {e}")
print()

# ==========================================
# 2. CLICK (Command line interface toolkit)
# ==========================================
# Click allows building command line applications using decorators.
# 1. Install: `pip install click`
#
# --- Click Script Example ---
# import click
#
# @click.command()
# @click.option('--count', default=1, help='Number of greetings.')
# @click.option('--name', prompt='Your name', help='The person to greet.')
# def hello(count, name):
#     for x in range(count):
#         click.echo(f"Hello {name}!")
#
# if __name__ == '__main__':
#     hello()

# ==========================================
# 3. TYPER (Modern CLI builder)
# ==========================================
# Typer uses type hints to build CLIs (built by the creator of FastAPI).
# 1. Install: `pip install typer`
#
# --- Typer Script Example ---
# import typer
#
# app = typer.Typer()
#
# @app.command()
# def main(name: str, age: int = 18):
#     print(f"Hello {name}, you are {age} years old.")
#
# if __name__ == "__main__":
#     app()
print("Scripting_Automation reference configured!")
print()
