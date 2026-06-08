# =====================================================================
# FILE: Closures_Lambdas.py
# DESCRIPTION: Closure scope caching, lambdas, and mapping/filtering/reducing lists.
#
# SYNTAX QUICK-REFERENCE:
#   # Closure
#   def outer(factor):
#       return lambda val: val * factor
#   double = outer(2)
#
#   # map, filter, reduce
#   list(map(lambda x: x*2, [1, 2]))
#   list(filter(lambda x: x > 5, [3, 8]))
#
#   from functools import reduce
#   reduce(lambda x, y: x + y, [1, 2, 3])  # 6
# =====================================================================

# Closures_Lambdas.py
# Reference Guide: Closures, Lambdas, map, filter, and reduce in Python
from functools import reduce

# ==========================================
# 1. CLOSURES
# ==========================================
# A Closure is a nested function that retains access to variables from its 
# enclosing scope even after the outer function has finished executing.
print("--- 1. CLOSURES ---")
def multiplier(factor):
    def multiply(number):
        return number * factor
    return multiply

double = multiplier(2)
triple = multiplier(3)

print(f"Double of 5: {double(5)}") # 10
print(f"Triple of 5: {triple(5)}") # 15
print()

# ==========================================
# 2. LAMBDAS (Anonymous Functions)
# ==========================================
# Syntax: lambda arguments: expression
print("--- 2. LAMBDAS ---")
square = lambda x: x**2
add = lambda x, y: x + y

print(f"Lambda Square(4): {square(4)}")
print(f"Lambda Add(5, 7):  {add(5, 7)}")
print()

# ==========================================
# 3. MAP, FILTER, AND REDUCE
# ==========================================
print("--- 3. MAP, FILTER, REDUCE ---")
nums = [1, 2, 3, 4, 5]

# map(func, iterable): Applies a function to all items in an input list
mapped_squares = list(map(lambda x: x**2, nums))
print(f"Mapped Squares: {mapped_squares}")

# filter(func, iterable): Filters items out of a list based on a boolean function
filtered_evens = list(filter(lambda x: x % 2 == 0, nums))
print(f"Filtered Evens: {filtered_evens}")

# reduce(func, iterable): Performs a rolling calculation on sequential pairs in a list
# Note: reduce must be imported from the functools module
reduced_sum = reduce(lambda x, y: x + y, nums)
print(f"Reduced Sum:    {reduced_sum}")
print()
