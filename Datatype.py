# =====================================================================
# FILE: Datatype.py
# DESCRIPTION: Overview of core primitive, non-primitive, and user-defined datatypes.
#
# SYNTAX QUICK-REFERENCE:
#   x: int = 10
#   y: float = 3.14
#   name: str = "Alice"
#   is_true: bool = True
#   empty: None = None
# =====================================================================

# Datatype.py
# Reference Guide: Primitive, Non-Primitive, and User-Defined Datatypes in Python

# ==========================================
# 1. WHAT IS A DATATYPE?
# ==========================================
# A datatype defines the classification of data, telling the interpreter how 
# the developer intends to use the data and what operations can be performed on it.

# ==========================================
# 2. PRIMITIVE DATATYPES
# ==========================================
# Core built-in datatypes for single values.
print("--- 1. PRIMITIVE DATATYPES ---")

age: int = 30               # Integer (int)
pi: float = 3.14            # Floating point (float)
name: str = "Alice"         # String (str)
is_student: bool = True     # Boolean (bool)
empty_val = None            # NoneType (None)

print(f"Integer age:     {age} ({type(age)})")
print(f"Float pi:        {pi} ({type(pi)})")
print(f"String name:     {name} ({type(name)})")
print(f"Boolean student: {is_student} ({type(is_student)})")
print(f"None Value:      {empty_val} ({type(empty_val)})")
print()

# ==========================================
# 3. NON-PRIMITIVE DATATYPES (Collections)
# ==========================================
# Structures that store collections of values.
print("--- 2. NON-PRIMITIVE DATATYPES ---")

user_list = [1, 2, 3]                                  # List (ordered, mutable)
user_tuple = (1, 2, 3)                                 # Tuple (ordered, immutable)
user_dict = {"name": "Alice", "age": 30}               # Dictionary (key-value mapping)
user_set = {1, 2, 3}                                   # Set (unordered collection of unique items)

print(f"List:       {user_list} ({type(user_list)})")
print(f"Tuple:      {user_tuple} ({type(user_tuple)})")
print(f"Dictionary: {user_dict} ({type(user_dict)})")
print(f"Set:        {user_set} ({type(user_set)})")
print()

# ==========================================
# 4. USER-DEFINED DATATYPES (Classes)
# ==========================================
# Custom blueprints created using classes.
print("--- 3. USER-DEFINED DATATYPES ---")

class Person:
    pass

person1 = Person()
print(f"Custom Object Instance: {person1} ({type(person1)})")
print()
