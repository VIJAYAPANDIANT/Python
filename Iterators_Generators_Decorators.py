# =====================================================================
# FILE: Iterators_Generators_Decorators.py
# DESCRIPTION: Custom `__iter__` classes, generator `yield` pauses, custom function decorators, and `itertools` library functions.
#
# SYNTAX QUICK-REFERENCE:
#   # Generator
#   def count_up():
#       yield 1
#       yield 2
#
#   # Decorator
#   from functools import wraps
#   def my_decorator(func):
#       @wraps(func)
#       def wrapper(*args, **kwargs):
#           return func(*args, **kwargs)
#       return wrapper
#
#   # Itertools
#   import itertools
#   itertools.count(10, 2)  # 10, 12, 14...
# =====================================================================

# Iterators_Generators_Decorators.py
# Reference Guide: Iterators, Generators (yield), and Custom Decorators (@ syntax)
import time
from functools import wraps

# ==========================================
# 1. ITERATORS
# ==========================================
# An iterator is an object that implements __iter__() and __next__().
print("--- 1. ITERATORS & ITERABLES ---")
nums = [1, 2, 3] # Iterable
it = iter(nums)  # Iterator

print(f"next(it): {next(it)}") # 1
print(f"next(it): {next(it)}") # 2
print(f"next(it): {next(it)}") # 3
# next(it) -> ❌ StopIteration

# Custom Iterator Class
class CountUp:
    def __init__(self, start, end):
        self.current = start
        self.end = end
    def __iter__(self):
        return self
    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        val = self.current
        self.current += 1
        return val

print("Custom Iterator CountUp(1, 3):")
for num in CountUp(1, 3):
    print(f"  {num}")
print()

# ==========================================
# 2. GENERATORS
# ==========================================
# Generators are functions that return items one-by-one using the 'yield' keyword.
# They are highly memory-efficient since values are produced on-demand.
print("--- 2. GENERATORS (yield) ---")
def count_up_gen(start, end):
    while start <= end:
        yield start
        start += 1

gen = count_up_gen(1, 3)
print(f"next(gen): {next(gen)}")
print(f"next(gen): {next(gen)}")

# Generator Expression (Tuple-like shorthand syntax)
squares_gen = (i * i for i in range(1, 4))
print(f"Generator expression next: {next(squares_gen)}")
print(f"Generator expression next: {next(squares_gen)}")

# Generator send() method
def accumulator():
    total = 0
    while True:
        value = yield total
        total += value

acc = accumulator()
next(acc) # Start/Prime generator
print(f"send(10): {acc.send(10)}") # Total becomes 10
print(f"send(20): {acc.send(20)}") # Total becomes 30
print()

# ==========================================
# 3. ITERTOOLS LIBRARY
# ==========================================
print("--- 3. ITERTOOLS MODULE ---")
import itertools

# count(start, step): Infinite sequence counter
counter = itertools.count(start=10, step=2)
print(f"itertools.count: {next(counter)}, {next(counter)}, {next(counter)}")

# cycle(iterable): Infinite repetition of an iterable
cycler = itertools.cycle(["A", "B"])
print(f"itertools.cycle: {next(cycler)}, {next(cycler)}, {next(cycler)}")

# repeat(object, times): Repeat an object
repeater = itertools.repeat("Hello", times=3)
print(f"itertools.repeat: {list(repeater)}")

# accumulate(iterable): Running returns accumulated sums
accumulated = itertools.accumulate([1, 2, 3, 4])
print(f"itertools.accumulate: {list(accumulated)}")

# chain(*iterables): Chain multiple iterables together
chained = itertools.chain([1, 2], [3, 4])
print(f"itertools.chain: {list(chained)}")
print()

# ==========================================
# 4. DECORATORS
# ==========================================
# Decorators are functions that wrap other functions to add custom behavior.
print("--- 4. DECORATORS ---")

def logger(func):
    @wraps(func) # Enforces preservation of original function's name and docstring
    def wrapper(*args, **kwargs):
        print(f"Calling '{func.__name__}' with args: {args} kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"'{func.__name__}' returned: {result}")
        return result
    return wrapper

@logger
def add(a, b):
    """Adds two values"""
    return a + b

print(f"add(3, 5) result: {add(3, 5)}")
print(f"Preserved function details: name='{add.__name__}', docstring='{add.__doc__}'")
print()

# Decorator with parameter (creates a factory)
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(2)
def greet():
    print("  Hello from decorator!")

print("Executing greet() decorated with @repeat(2):")
greet()
print()
