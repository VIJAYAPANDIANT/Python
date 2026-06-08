# =====================================================================
# FILE: Comprehensions.py
# DESCRIPTION: Comprehensions across lists, dictionaries, sets, and generators.
#
# SYNTAX QUICK-REFERENCE:
#   # List Comprehension
#   squares = [x**2 for x in range(5) if x % 2 == 0]
#
#   # Dictionary Comprehension
#   square_dict = {x: x**2 for x in range(3)}
#
#   # Set Comprehension
#   unique_set = {x for x in [1, 1, 2, 3]}
#
#   # Generator Expression (calculates on-the-fly)
#   gen_exp = (x**2 for x in range(10000))
# =====================================================================

# Comprehensions.py
# Reference Guide: List, Dictionary, Set, and Generator Comprehensions in Python

# ==========================================
# 1. LIST COMPREHENSIONS
# ==========================================
# Syntax: [expression for item in iterable if condition]
print("--- 1. LIST COMPREHENSIONS ---")
numbers = [1, 2, 3, 4, 5]

# Basic mapping
squares = [x**2 for x in numbers]
print(f"Squares: {squares}")

# Filtering (with if)
evens = [x for x in numbers if x % 2 == 0]
print(f"Evens: {evens}")

# If-Else inside comprehension (expression level)
# Syntax: [expr_if_true if condition else expr_if_false for item in iterable]
labels = ["Even" if x % 2 == 0 else "Odd" for x in numbers]
print(f"Labels: {labels}")
print()

# ==========================================
# 2. DICTIONARY COMPREHENSIONS
# ==========================================
# Syntax: {key_expr: value_expr for item in iterable if condition}
print("--- 2. DICTIONARY COMPREHENSIONS ---")
fruits = ["apple", "banana", "cherry"]

# String length mapping
fruit_lens = {fruit: len(fruit) for fruit in fruits}
print(f"Fruit Lengths: {fruit_lens}")

# Filtering dict comprehension
square_evens = {x: x**2 for x in range(1, 6) if x % 2 == 0}
print(f"Square of evens: {square_evens}")
print()

# ==========================================
# 3. SET COMPREHENSIONS
# ==========================================
# Syntax: {expression for item in iterable if condition}
# Same syntax as dict comprehension but without key-value pairs (colon). Outputs unique elements.
print("--- 3. SET COMPREHENSIONS ---")
duplicates = [1, 2, 2, 3, 4, 4, 5]
unique_squares = {x**2 for x in duplicates}
print(f"Unique Squares Set: {unique_squares}")
print()

# ==========================================
# 4. GENERATOR COMPREHENSIONS (Generator Expressions)
# ==========================================
# Syntax: (expression for item in iterable if condition)
# Returns a generator object instead of a populated collection, saving memory.
print("--- 4. GENERATOR COMPREHENSIONS ---")
gen = (x**2 for x in range(1, 1000000)) # Excludes list allocation in memory
print(f"Generator Type: {type(gen)}")
print(f"First element: {next(gen)}")
print(f"Second element: {next(gen)}")
print()
