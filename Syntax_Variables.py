# =====================================================================
# FILE: Syntax_Variables.py
# DESCRIPTION: Variables, assignments, type casting, error handling, and multi-inputs.
#
# SYNTAX QUICK-REFERENCE:
#   x = y = z = 0          # Multiple assignment
#   a, b = 1, 2            # Unpacking assignment
#
#   # Type casting
#   num = int("42")
#   val = float(5)
#   string = str(100)
#   boolean = bool("hi")   # True
#
#   # Multi-input mapping
#   num1, num2 = map(int, input().split())
# =====================================================================

# Syntax_Variables.py
# Reference Guide: Variables, Syntax, Type Casting, and User Input in Python

# ==========================================
# 1. VARIABLES IN PYTHON
# ==========================================
# A variable is a named container that stores a value.
# No need to declare a type — Python figures it out automatically.

print("--- 1. CREATING VARIABLES ---")
name = "Alice"       # string
age = 25             # integer
height = 5.7         # float
is_student = True    # boolean

print(f"name: {name} ({type(name)})")
print(f"age: {age} ({type(age)})")
print(f"height: {height} ({type(height)})")
print(f"is_student: {is_student} ({type(is_student)})")
print()

# --- Rules for Variable Names ---
# - Must start with a letter or underscore (_)
# - Can contain letters, numbers, underscores
# - Case-sensitive (age and Age are different)
# - Cannot be a reserved keyword (if, for, while, etc.)

my_var = 10      # ✅ valid
_temp = 20       # ✅ valid
# 2cool = 5      # ❌ invalid (starts with number)

# --- Multiple Assignment ---
print("--- MULTIPLE ASSIGNMENT ---")
x = y = z = 0          # all three get 0
a, b, c = 1, 2, 3      # a=1, b=2, c=3
print(f"x: {x}, y: {y}, z: {z}")
print(f"a: {a}, b: {b}, c: {c}")
print()

# --- Changing Values ---
print("--- CHANGING VALUES & DYNAMIC TYPING ---")
x = 10
print(f"x is {x} ({type(x)})")
x = 20      # x is now 20
print(f"x updated to {x}")
x = "hello" # x can even change type
print(f"x changed type to '{x}' ({type(x)})")
print()


# ==========================================
# 2. TYPE CASTING IN PYTHON
# ==========================================
# Type casting means converting one data type to another.

# --- Implicit Casting (Auto) ---
# Python converts automatically — no effort needed.
print("--- IMPLICIT CASTING ---")
int_val = 5      # int
float_val = 2.0    # float
result = int_val + float_val
print(f"5 + 2.0 = {result} ({type(result)})")  # Auto-converts int -> float
print()

# --- Explicit Casting (Manual) ---
# Force conversion using built-in functions: int(), float(), str(), bool(), list(), tuple()
print("--- EXPLICIT CASTING ---")
print(f"int(3.9): {int(3.9)}")       # 3 (truncates, does NOT round)
print(f"int('42'): {int('42')}")     # 42
print(f"int(True): {int(True)}")     # 1
print(f"int(False): {int(False)}")   # 0

print(f"float(5): {float(5)}")       # 5.0
print(f"float('3.14'): {float('3.14')}") # 3.14

print(f"str(100): '{str(100)}'")     # "100"
print(f"str(True): '{str(True)}'")   # "True"

print(f"bool(0): {bool(0)}")         # False
print(f"bool(1): {bool(1)}")         # True
print(f"bool(''): {bool('')}")       # False (empty string)
print(f"bool('hi'): {bool('hi')}")   # True (non-empty string)
print(f"bool(None): {bool(None)}")   # False
print()

# --- Handling Casting Errors Gracefully ---
print("--- CASTING ERROR HANDLING ---")
try:
    x = int("hello")  # ValueError
except ValueError:
    print("Invalid conversion caught! Cannot convert text to int.")
print()


# ==========================================
# 3. USER INPUT IN PYTHON
# ==========================================
# input() is the built-in function used to take input from the user.
# IMPORTANT: input() always returns a string — even if the user types a number.

print("--- USER INPUT EXAMPLES (SIMULATED) ---")
# Reading values usually done with:
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))

# Splitting multiple inputs:
# x, y = input("Enter two numbers: ").split()
# x, y = map(int, input("Enter two numbers: ").split())

print("Multi-input split demo using a simulated string '10 20':")
simulated_input = "10 20"
num1, num2 = map(int, simulated_input.split())
print(f"Simulated Input: '{simulated_input}' -> Parsed & Mapped: {num1} + {num2} = {num1 + num2}")
print()
