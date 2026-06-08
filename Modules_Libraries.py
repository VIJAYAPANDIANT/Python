# =====================================================================
# FILE: Modules_Libraries.py
# DESCRIPTION: Built-in libraries (`math`, `random`, `os`, `sys`, `datetime`), custom imports, and package directory initialization.
#
# SYNTAX QUICK-REFERENCE:
#   import math as m
#   from datetime import datetime
#
#   # Package structure requires a folder containing a __init__.py file:
#   # my_package/
#   #   ├── __init__.py
#   #   └── module.py
# =====================================================================

# Modules_Libraries.py
# Reference Guide: Built-in Modules, Custom Modules, and External Libraries

# ==========================================
# 1. WHAT IS A MODULE?
# ==========================================
# A module is a file containing Python code (functions, variables, classes) 
# that you can import and reuse in other programs.

# Import options:
# 1. import math
# 2. from math import sqrt
# 3. from math import sqrt, pi
# 4. from math import *
# 5. import math as m

# ==========================================
# 2. BUILT-IN MODULES DEMONSTRATION
# ==========================================
print("--- 1. MATH MODULE ---")
import math
print(f"math.sqrt(16):      {math.sqrt(16)}")       # 4.0
print(f"math.pi:            {math.pi}")             # 3.14159...
print(f"math.ceil(4.2):     {math.ceil(4.2)}")      # 5 (rounds up)
print(f"math.floor(4.9):    {math.floor(4.9)}")     # 4 (rounds down)
print(f"math.pow(2, 3):     {math.pow(2, 3)}")      # 8.0
print(f"math.factorial(5):  {math.factorial(5)}")   # 120
print()

print("--- 2. RANDOM MODULE ---")
import random
print(f"random.random():    {random.random()}")     # Float between 0.0 and 1.0
print(f"random.randint(1,10): {random.randint(1, 10)}") # Int between 1 and 10
print(f"random.choice([1,2,3,4]): {random.choice([1, 2, 3, 4])}")
fruits = ["apple", "banana", "cherry"]
random.shuffle(fruits)
print(f"random.shuffle(fruits): {fruits}")
print(f"random.uniform(1.5, 5.5): {random.uniform(1.5, 5.5)}")
print()

print("--- 3. OS MODULE ---")
import os
print(f"Current Directory: {os.getcwd()}")
print(f"List files: {os.listdir()[:3]} (truncated list)")
print(f"File exists check: {os.path.exists('Syntax_Variables.py')}")
print()

print("--- 4. SYS MODULE ---")
import sys
print(f"Python Version: {sys.version.split()[0]}")
print(f"Platform: {sys.platform}")
print()

print("--- 5. DATETIME MODULE ---")
from datetime import datetime, date
now = datetime.now()
print(f"Now: {now}")
print(f"Year: {now.year}, Month: {now.month}, Day: {now.day}")
print(f"Formatted: {now.strftime('%d/%m/%Y %H:%M:%S')}")
print(f"Today's date: {date.today()}")
print()

print("--- 6. STRING MODULE ---")
import string
print(f"Letters: {string.ascii_letters}")
print(f"Digits: {string.digits}")
print(f"Punctuation: {string.punctuation}")
print()

print("--- 7. TIME MODULE ---")
import time
print(f"Time (epoch seconds): {time.time()}")
# Simulated delay (using a very short sleep for demo performance)
time.sleep(0.1)
print("Printed after 0.1 seconds delay")
print()

# ==========================================
# 3. CREATING YOUR OWN MODULE
# ==========================================
# If you save the following block into a file named `mymodule.py`:
# ---
# def greet(name):
#     return f"Hello, {name}!"
#
# def add(a, b):
#     return a + b
#
# pi = 3.14159
#
# if __name__ == "__main__":
#     # Runs only when the module is executed directly
#     print("Module executed directly")
# ---
# You can then import and use it:
# `import mymodule`
# `print(mymodule.greet("Alice"))`

# ==========================================
# 4. PYTHON PACKAGES & __init__.py
# ==========================================
# A package is a collection of modules under a directory.
# Directory Structure:
#   my_package/
#       ├── __init__.py      <-- Enforces directory as importable package
#       ├── module_a.py
#       └── module_b.py
#
# __init__.py can:
# - Leave blank to simply mark the directory as a package.
# - Control exported APIs using `__all__ = ["module_a"]`.
# - Run initialization code when the package is imported.
#
# Import syntax for package modules:
#   `from my_package import module_a`
#   `from my_package.module_b import my_function`

# ==========================================
# 5. EXTERNAL LIBRARIES (pip) & NUMPY / REQUESTS
# ==========================================
# You install external libraries using `pip install <package_name>`:
# e.g., `pip install numpy pandas matplotlib requests`
#
# NumPy Example:
#   import numpy as np
#   arr = np.array([1, 2, 3])
#   print(arr * 2)
#
# Requests Example:
#   import requests
#   r = requests.get("https://api.github.com")
#   print(r.status_code)
print()
