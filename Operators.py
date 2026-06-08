# =====================================================================
# FILE: Operators.py
# DESCRIPTION: Mathematical operations, PEMDAS order, logical/comparison operators, and the walrus operator.
#
# SYNTAX QUICK-REFERENCE:
#   # Division and Floor Division
#   print(10 / 3)   # 3.3333333333333335 (float)
#   print(10 // 3)  # 3 (drops decimal)
#   print(10 % 3)   # 1 (remainder)
#   print(2 ** 3)   # 8 (exponent)
#
#   # Walrus operator (assigns inside expressions)
#   if (n := len("Hello")) > 3:
#       print(n)
# =====================================================================

# Operators.py
# Reference Guide: Arithmetic, Logical, Comparison, PEMDAS, Shorthand, and Walrus Operators

# ==========================================
# 1. ARITHMETIC OPERATORS
# ==========================================
# Python supports standard arithmetic operators:

a = 10
b = 3

print("--- 1. ARITHMETIC OPERATORS ---")
print(f"a = {a}, b = {b}")
print(f"Addition (a + b):       {a + b}")    # 13
print(f"Subtraction (a - b):    {a - b}")    # 7
print(f"Multiplication (a * b): {a * b}")    # 30
print(f"Division (a / b):       {a / b}")    # 3.3333333333333335 (always float)
print(f"Floor Division (a // b):{a // b}")   # 3 (drops the decimal)
print(f"Modulus (a % b):        {a % b}")    # 1 (remainder)
print(f"Exponent (a ** b):      {a ** b}")   # 1000 (10 cubed)
print()

# ==========================================
# 2. ORDER OF OPERATIONS (PEMDAS)
# ==========================================
# 1st: Parentheses ()
# 2nd: Exponents **
# 3rd: Multiplication (*) and Division (/, //, %)
# 4th: Addition (+) and Subtraction (-)
# Note: M/D and A/S are equal priority — they execute Left to Right.

print("--- 2. PEMDAS EXAMPLES ---")
print("Without brackets:")
print(f"2 + 3 * 4   -> {2 + 3 * 4}")         # 14  (multiply first, then add)
print(f"10 - 4 / 2  -> {10 - 4 / 2}")        # 8.0 (divide first, then subtract)
print(f"2 ** 3 + 1  -> {2 ** 3 + 1}")        # 9   (exponent first, then add)
print(f"10 % 3 + 1  -> {10 % 3 + 1}")        # 2   (modulus first, then add)

print("\nWith brackets:")
print(f"(2 + 3) * 4 -> {(2 + 3) * 4}")       # 20
print(f"(10 - 4) / 2-> {(10 - 4) / 2}")      # 3.0
print(f"2 ** (3 + 1)-> {2 ** (3 + 1)}")      # 16

print("\nLeft to Right (same priority):")
print(f"10 - 3 + 2  -> {10 - 3 + 2}")        # 9   (left to right: 10-3=7, 7+2=9)
print(f"10 / 2 * 3  -> {10 / 2 * 3}")        # 15.0 (left to right: 10/2=5, 5*3=15)

print("\nNested Parentheses:")
print(f"(((2 + 3) * 4) - 1) -> {(((2 + 3) * 4) - 1)}") # 19

# Common Mistake
# avg = 10 + 20 / 2    # 20.0 ❌ (divides 20/2 first)
# avg = (10 + 20) / 2  # 15.0 ✅ (adds first inside parentheses)
print()

# ==========================================
# 3. SHORTHAND ASSIGNMENT
# ==========================================
print("--- 3. SHORTHAND ASSIGNMENT ---")
x = 10
print(f"Start x: {x}")
x += 5   # x = x + 5
print(f"x += 5  -> {x}") # 15
x -= 3   # x = x - 3
print(f"x -= 3  -> {x}") # 12
x *= 2   # x = x * 2
print(f"x *= 2  -> {x}") # 24
x /= 4   # x = x / 4
print(f"x /= 4  -> {x}") # 6.0
x //= 2  # x = x // 2
print(f"x //= 2 -> {x}") # 3.0
x **= 3  # x = x ** 3
print(f"x **= 3 -> {x}") # 27.0
print()

# ==========================================
# 4. COMPARISON & LOGICAL OPERATORS
# ==========================================
# Comparison: ==, !=, >, <, >=, <=
# Logical: and, or, not
print("--- 4. COMPARISON & LOGICAL ---")
x = 5
print(f"x = {x}")
print(f"x > 0 and x < 10: {x > 0 and x < 10}")  # True
print(f"x < 0 or x > 3:   {x < 0 or x > 3}")    # True
print(f"not(x == 5):      {not(x == 5)}")        # False
print()

# ==========================================
# 5. WALRUS OPERATOR (:=)
# ==========================================
# Assigns a value to a variable as part of an expression.
print("--- 5. WALRUS OPERATOR ---")
if (n := len("Hello World")) > 5:
    print(f"Length {n} is greater than 5")
print()
