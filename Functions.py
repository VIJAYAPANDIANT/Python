# =====================================================================
# FILE: Functions.py
# DESCRIPTION: Function declarations, default values, args, kwargs, nested functions, lambdas, and recursion.
#
# SYNTAX QUICK-REFERENCE:
#   def complex_func(a, b=2, *args, **kwargs):
#       # args packed as tuple, kwargs packed as dict
#       return a + b + sum(args)
#
#   # Lambda/Anonymous function
#   square = lambda x: x * x
#
#   # Recursion
#   def factorial(n):
#       return 1 if n == 1 else n * factorial(n - 1)
# =====================================================================

# Functions.py
# Reference Guide: Python Functions, Args, Kwargs, Defaults, Lambdas, and Recursion

# ==========================================
# 1. FUNCTION BASICS
# ==========================================
# Functions are defined using the 'def' keyword.

print("--- 1. FUNCTION DEFINITIONS & RETURNS ---")
def greet(name):
    print("Hello,", name)

greet("Alice")

# Return statement returns a value back to the caller
def add(a, b):
    return a + b

result = add(5, 3)
print(f"5 + 3 = {result}")

# Difference between Print and Return:
# - print displays the value
# - return sends the value back to the caller
def with_print(a, b):
    print(f"Printing sum inside: {a + b}")
def with_return(a, b):
    return a + b

x = with_print(2, 3)    # Prints 5, but variable x becomes None
y = with_return(2, 3)   # Assigns 5 to y, prints nothing
print(f"x (from print func): {x}, y (from return func): {y}")
print()

# ==========================================
# 2. DEFAULT & KEYWORD ARGUMENTS
# ==========================================
print("--- 2. DEFAULT & KEYWORD ARGUMENTS ---")
# Default parameters let you define default values for arguments:
def greet_msg(name, msg="Good Morning"):
    print(f"Hello {name}, {msg}")

greet_msg("Alice")                  # Uses default: Hello Alice, Good Morning
greet_msg("Bob", "Good Night")      # Overrides default: Hello Bob, Good Night

# Keyword arguments let you pass arguments in any order:
def student(name, age, grade):
    print(f"{name} is {age} years old, Grade: {grade}")

student(age=20, grade="A", name="Alice")  # Order doesn't matter
print()

# ==========================================
# 3. *args AND **kwargs
# ==========================================
# *args pack arbitrary positional arguments into a tuple.
# **kwargs pack arbitrary keyword arguments into a dictionary.

print("--- 3. *args & **kwargs ---")
def total(*nums):
    print(f"Packed args tuple: {nums}")
    return sum(nums)

print(f"Total: {total(1, 2, 3)}")
print(f"Total: {total(10, 20, 30, 40)}")

def info(**details):
    print(f"Packed kwargs dict: {details}")
    for key, value in details.items():
        print(f"  {key}: {value}")

info(name="Alice", age=20, city="NY")
print()

# ==========================================
# 4. ADVANCED FUNCTION CONCEPTS
# ==========================================
print("--- 4. ADVANCED CONCEPTS ---")

# Returning Multiple Values (Returns them packed in a tuple)
def min_max(nums):
    return min(nums), max(nums)

low, high = min_max([3, 1, 7, 2, 9])
print(f"Min: {low}, Max: {high}")

# Nested Functions
def outer():
    print("Outer function execution")
    def inner():
        print("Inner function execution")
    inner()
outer()

# Lambda Functions (Anonymous one-line functions)
square = lambda x: x * x
add_lambda = lambda a, b: a + b
print(f"Lambda square(5): {square(5)}")
print(f"Lambda add(3, 4): {add_lambda(3, 4)}")

# Recursive Function (Function calling itself)
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(f"Factorial of 5 (Recursion): {factorial(5)}") # 5 * 4 * 3 * 2 * 1 = 120
print()
