# Python Complete Syntax Cheat Sheet & Repository Index

Welcome to the ultimate Python reference repository. This document provides a quick syntax overview of every topic covered in this directory, mapped to the respective runnable files.

---

## 🚀 1. Basic Syntax & Concepts

### [Basic.py](file:///c:/Python/Basic.py)
* **Description:** Basic output, input, and python design history/pros/cons.
* **Syntax:**
  ```python
  print("Hello World")
  # input() takes string console input:
  name = input("Enter name: ")
  ```

### [Comment.py](file:///c:/Python/Comment.py)
* **Description:** Comments and code documentation.
* **Syntax:**
  ```python
  # Single line comment
  
  """
  Docstring used to document a function,
  accessible via func.__doc__
  """
  ```

### [Datatype.py](file:///c:/Python/Datatype.py)
* **Description:** Overview of core primitive, non-primitive, and user-defined datatypes.
* **Syntax:**
  ```python
  x: int = 10
  y: float = 3.14
  name: str = "Alice"
  is_true: bool = True
  empty: None = None
  ```

### [Variable.py](file:///c:/Python/Variable.py)
* **Description:** Variables, memory references (`id()`), and basic string transformations.
* **Syntax:**
  ```python
  x = 10
  print(id(x))  # Unique memory address
  name = "Abbas Ali"
  print(name.upper())  # "ABBAS ALI"
  ```

### [Syntax_Variables.py](file:///c:/Python/Syntax_Variables.py)
* **Description:** Variables, assignments, type casting, error handling, and multi-inputs.
* **Syntax:**
  ```python
  x = y = z = 0          # Multiple assignment
  a, b = 1, 2            # Unpacking assignment
  
  # Type casting
  num = int("42")
  val = float(5)
  string = str(100)
  boolean = bool("hi")   # True
  
  # Multi-input mapping
  num1, num2 = map(int, input().split())
  ```

### [Operators.py](file:///c:/Python/Operators.py)
* **Description:** Mathematical operations, PEMDAS order, logical/comparison operators, and the walrus operator.
* **Syntax:**
  ```python
  # Division and Floor Division
  print(10 / 3)   # 3.3333333333333335 (float)
  print(10 // 3)  # 3 (drops decimal)
  print(10 % 3)   # 1 (remainder)
  print(2 ** 3)   # 8 (exponent)
  
  # Walrus operator (assigns inside expressions)
  if (n := len("Hello")) > 3:
      print(n)
  ```

### [Control_Flow.py](file:///c:/Python/Control_Flow.py)
* **Description:** if-statements, ternary operators, loops, and loop control statements.
* **Syntax:**
  ```python
  # Ternary
  result = "Adult" if age >= 18 else "Minor"
  
  # Loops
  for i in range(0, 5, 2):  # start, stop, step
      print(i)              # 0 2 4
  
  # Loop Else Clause (runs if loop finished without 'break')
  for x in range(3):
      pass
  else:
      print("No break encountered!")
  
  # Simulated Do-While Loop
  while True:
      # code runs once
      if not condition:
          break
  ```

### [Functions.py](file:///c:/Python/Functions.py)
* **Description:** Function declarations, default values, args, kwargs, nested functions, lambdas, and recursion.
* **Syntax:**
  ```python
  def complex_func(a, b=2, *args, **kwargs):
      # args packed as tuple, kwargs packed as dict
      return a + b + sum(args)
  
  # Lambda/Anonymous function
  square = lambda x: x * x
  
  # Recursion
  def factorial(n):
      return 1 if n == 1 else n * factorial(n - 1)
  ```

### [Collections.py](file:///c:/Python/Collections.py)
* **Description:** Lists, tuples, dictionaries, sets, slicing, unpacking, and set operations.
* **Syntax:**
  ```python
  # Slicing: list[start:stop:step]
  nums = [1, 2, 3, 4, 5]
  print(nums[1:4])   # [2, 3, 4]
  print(nums[::-1])  # [5, 4, 3, 2, 1] (reversed)
  
  # Tuple Unpacking and Swapping
  x, y = 10, 20
  x, y = y, x        # Swap variables
  
  # Set operations
  a = {1, 2, 3}
  b = {3, 4, 5}
  print(a | b)  # Union {1, 2, 3, 4, 5}
  print(a & b)  # Intersection {3}
  print(a - b)  # Difference {1, 2}
  ```

### [Strings.py](file:///c:/Python/Strings.py) & [Regex.py](file:///c:/Python/Regex.py)
* **Description:** f-strings, common string methods, and comprehensive Regular Expressions (`re`).
* **Syntax:**
  ```python
  # Formatting floats/percentages in f-strings
  percentage = 0.8756
  print(f"{percentage:.2%}")  # "87.56%"
  
  # Common string methods
  "  hello  ".strip()
  "apple banana".split()
  ",".join(["a", "b", "c"])
  
  # Regex functions
  import re
  re.findall(r"\d+", "Price 100, Qty 50")  # ['100', '50']
  re.sub(r"\d", "X", "Room 404")            # "Room XXX"
  ```

---

## ⚙️ 2. Intermediate & Modular Features

### [Comprehensions.py](file:///c:/Python/Comprehensions.py)
* **Description:** Comprehensions across lists, dictionaries, sets, and generators.
* **Syntax:**
  ```python
  # List Comprehension
  squares = [x**2 for x in range(5) if x % 2 == 0]
  
  # Dictionary Comprehension
  square_dict = {x: x**2 for x in range(3)}
  
  # Set Comprehension
  unique_set = {x for x in [1, 1, 2, 3]}
  
  # Generator Expression (calculates on-the-fly)
  gen_exp = (x**2 for x in range(10000))
  ```

### [Modules_Libraries.py](file:///c:/Python/Modules_Libraries.py)
* **Description:** Built-in libraries (`math`, `random`, `os`, `sys`, `datetime`), custom imports, and package directory initialization.
* **Syntax:**
  ```python
  import math as m
  from datetime import datetime
  
  # Package structure requires a folder containing a __init__.py file:
  # my_package/
  #   ├── __init__.py
  #   └── module.py
  ```

### [File_Handling.py](file:///c:/Python/File_Handling.py)
* **Description:** File modes, `with` statements, JSON reading/writing, cursor seek/tell operations, and modern `pathlib`.
* **Syntax:**
  ```python
  # Pathlib Paths
  from pathlib import Path
  path = Path("test.txt")
  path.write_text("Hello!")
  content = path.read_text()
  
  # JSON serialization
  import json
  with open("data.json", "w") as f:
      json.dump({"name": "Alice"}, f)
  ```

### [Exception_Handling.py](file:///c:/Python/Exception_Handling.py)
* **Description:** Catching multiple exceptions, raising custom error classes, `else`, and `finally` constructs.
* **Syntax:**
  ```python
  class CustomError(Exception):
      pass
      
  try:
      x = 10 / int(input())
  except (ValueError, ZeroDivisionError) as e:
      print(f"Handled error: {e}")
  else:
      print("No error occurred!")
  finally:
      print("Always executes!")
  ```

### [Iterators_Generators_Decorators.py](file:///c:/Python/Iterators_Generators_Decorators.py)
* **Description:** Custom `__iter__` classes, generator `yield` pauses, custom function decorators, and `itertools` library functions.
* **Syntax:**
  ```python
  # Generator
  def count_up():
      yield 1
      yield 2
  
  # Decorator
  from functools import wraps
  def my_decorator(func):
      @wraps(func)
      def wrapper(*args, **kwargs):
          return func(*args, **kwargs)
      return wrapper
      
  # Itertools
  import itertools
  itertools.count(10, 2)  # 10, 12, 14...
  ```

### [Closures_Lambdas.py](file:///c:/Python/Closures_Lambdas.py)
* **Description:** Closure scope caching, lambdas, and mapping/filtering/reducing lists.
* **Syntax:**
  ```python
  # Closure
  def outer(factor):
      return lambda val: val * factor
  double = outer(2)
  
  # map, filter, reduce
  list(map(lambda x: x*2, [1, 2]))
  list(filter(lambda x: x > 5, [3, 8]))
  
  from functools import reduce
  reduce(lambda x, y: x + y, [1, 2, 3])  # 6
  ```

### [Type_Hints.py](file:///c:/Python/Type_Hints.py)
* **Description:** PEP 484 type hints, annotations, union/optional types, and static analysis checkers.
* **Syntax:**
  ```python
  from typing import List, Dict, Union, Optional
  
  def greet(name: str, aliases: List[str]) -> Optional[str]:
      return f"Hello {name}" if name else None
  ```

### [Context_Managers.py](file:///c:/Python/Context_Managers.py)
* **Description:** Building custom context managers with classes (`__enter__`/`__exit__`) or generators (`@contextmanager`).
* **Syntax:**
  ```python
  # Class-based
  class CustomManager:
      def __enter__(self):
          return self
      def __exit__(self, exc_type, exc_val, exc_tb):
          pass
          
  # Generator-based
  from contextlib import contextmanager
  @contextmanager
  def resource():
      # setup
      yield
      # cleanup
  ```

---

## 🛠️ 3. Advanced & System-Level Programming

### [OOP.py](file:///c:/Python/OOP.py)
* **Description:** OOP principles, inheritance structures, constructor overrides, and custom arithmetic operators.
* **Syntax:**
  ```python
  class Child(Parent1, Parent2): # Multiple inheritance
      def __init__(self, name):
          super().__init__(name)
          
      def __add__(self, other): # Operator Overloading (+)
          return self.value + other.value
  ```

### [Metaclasses_Descriptors.py](file:///c:/Python/Metaclasses_Descriptors.py)
* **Description:** Class instantiation via `__new__`, custom metaclasses (`type` inheritance), and descriptor property validation protocols.
* **Syntax:**
  ```python
  # Metaclass
  class Meta(type):
      def __new__(cls, name, bases, dct):
          return super().__new__(cls, name, bases, dct)
  
  # Descriptor Protocol
  class Descriptor:
      def __get__(self, instance, owner): pass
      def __set__(self, instance, value): pass
  ```

### [Dataclasses.py](file:///c:/Python/Dataclasses.py)
* **Description:** Auto-generating class methods, field attributes customization, mutable default values, and slots performance.
* **Syntax:**
  ```python
  from dataclasses import dataclass, field
  
  @dataclass(slots=True)
  class Point:
      x: float
      y: float
      history: list = field(default_factory=list)
  ```

### [Async_IO.py](file:///c:/Python/Async_IO.py)
* **Description:** Coroutines, async event loops, gathering async functions, and concurrent task execution.
* **Syntax:**
  ```python
  import asyncio
  
  async def worker():
      await asyncio.sleep(1)
      
  async def main():
      await asyncio.gather(worker(), worker())
      
  asyncio.run(main())
  ```

### [Multithreading.py](file:///c:/Python/Multithreading.py) & [Concurrency_Multiprocessing.py](file:///c:/Python/Concurrency_Multiprocessing.py)
* **Description:** Threads, GIL constraints, Locks/Semaphores, OS processes, and process pool data distribution.
* **Syntax:**
  ```python
  import threading
  lock = threading.Lock()
  with lock:
      # Critical section
      
  # Multiprocessing Pool
  import multiprocessing
  with multiprocessing.Pool() as pool:
      results = pool.map(func, data_list)
  ```

### [C_Extensions.py](file:///c:/Python/C_Extensions.py)
* **Description:** Interacting with native C libraries using ctypes, Cython, and cffi.
* **Syntax:**
  ```python
  import ctypes
  libc = ctypes.CDLL("libc.so.6")
  libc.puts(b"Hello standard C library puts!")
  ```

### [Memory_GIL_313.py](file:///c:/Python/Memory_GIL_313.py)
* **Description:** Reference count diagnostics, cyclical reference cleanup (`gc`), and Python 3.13 free-threaded no-GIL architecture.
* **Syntax:**
  ```python
  import sys, gc
  sys.getrefcount(obj)  # Get references count
  gc.collect()          # Force cyclical garbage collection
  ```

---

## 📦 4. Tooling & Ecosystem References

* **[Environments_Packaging.py](file:///c:/Python/Environments_Packaging.py)**: Commands for `venv`, `poetry`, `uv`, `pyenv`, `pyproject.toml` configuration, and uploading packages to PyPI.
* **[Testing.py](file:///c:/Python/Testing.py)**: Unit testing structure with `pytest` testing checks, fixtures, and mock clients.
* **[Code_Quality.py](file:///c:/Python/Code_Quality.py)**: Configuration guidelines for code linters and formatters (**Black**, **Ruff**, **pre-commit**).
* **[Logging_Debugging.py](file:///c:/Python/Logging_Debugging.py)**: Logger severity structures and entering interactive debugging using `breakpoint()`.
* **[Profiling.py](file:///c:/Python/Profiling.py)**: Performance measurement using `timeit`, program run diagnostics using `cProfile`, and line-by-line memory tracking.
* **[Scripting_Automation.py](file:///c:/Python/Scripting_Automation.py)**: Invoking shell scripts using `subprocess` and developing command line programs with `click` or `typer`.
* **[Ecosystem_Frameworks.py](file:///c:/Python/Ecosystem_Frameworks.py)**: Quick templates for web APIs (FastAPI, Flask, Django), Database ORMs (SQLAlchemy, Alembic migrations), asynchronous job task queues (Celery, Redis), data analysis (NumPy arrays, Pandas dataframes), and machine/deep learning libraries (scikit-learn, PyTorch).
* **[Design_Patterns.py](file:///c:/Python/Design_Patterns.py)**: Implementing Factory class creation, Observer state subscriptions, and Singleton instances.
