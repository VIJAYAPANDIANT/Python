# =====================================================================
# FILE: Basic.py
# DESCRIPTION: Basic output, input, and python design history/pros/cons.
#
# SYNTAX QUICK-REFERENCE:
#   print("Hello World")
#   # input() takes string console input:
#   name = input("Enter name: ")
# =====================================================================

# Basic.py
# Reference Guide: Python History, Definition, Advantages, and Print/Input Basics

# ==========================================
# 1. WHAT IS PYTHON?
# ==========================================
# Python is a high-level, interpreted, general-purpose programming language.
# It was created by Guido van Rossum and first released in 1991.
# Key features:
# - Dynamically typed (type is checked at runtime)
# - Garbage-collected (automatic memory management)
# - Supports multiple programming paradigms: Procedural, Object-Oriented, and Functional.

print("--- 1. BASIC OUTPUT & INPUT ---")
# Print statement example
print("Hello World")

# Input statement example (Simulated here)
# In actual use: name = input("Enter your name: ")
simulated_input = "Alice"
print(f"Hello {simulated_input} (via simulated input)")
print()

# ==========================================
# 2. PROS AND CONS OF PYTHON
# ==========================================
# Advantages:
# 1. Easy to learn and read (simple syntax)
# 2. Large standard library & rich ecosystem
# 3. Platform independent (runs on Windows, Mac, Linux)
# 4. Rapid prototyping and development speed
# 5. Massive community support
#
# Disadvantages:
# 1. Slow execution speed compared to compiled languages (like C/C++)
# 2. High memory consumption due to dynamic typing
# 3. Not ideal for mobile app development
# 4. GIL (Global Interpreter Lock) limits true multi-core CPU performance in multithreading
print()
