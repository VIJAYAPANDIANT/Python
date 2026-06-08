# =====================================================================
# FILE: Type_Hints.py
# DESCRIPTION: PEP 484 type hints, annotations, union/optional types, and static analysis checkers.
#
# SYNTAX QUICK-REFERENCE:
#   from typing import List, Dict, Union, Optional
#
#   def greet(name: str, aliases: List[str]) -> Optional[str]:
#       return f"Hello {name}" if name else None
# =====================================================================

# Type_Hints.py
# Reference Guide: Type Hints, Annotations, typing module, and mypy guidelines
from typing import List, Dict, Tuple, Union, Optional, Any

# ==========================================
# 1. BASIC TYPE ANNOTATIONS
# ==========================================
# Type hints (annotations) are hints for developers and static analysis tools (like mypy).
# They do NOT enforce types at runtime in Python.

print("--- 1. BASIC TYPE HINTS ---")
name: str = "Alice"
age: int = 25
height: float = 5.7
is_student: bool = True

def greet(user_name: str) -> str:
    return f"Hello, {user_name}!"

print(greet(name))
print()

# ==========================================
# 2. TYPING MODULE COMPLEX TYPES
# ==========================================
print("--- 2. COMPLEX TYPES ---")

# Lists, Dictionaries, and Tuples
scores: List[int] = [95, 88, 92]
user_info: Dict[str, Union[str, int]] = {"name": "Bob", "age": 30}
coordinates: Tuple[float, float] = (40.7128, -74.0060)

# Union Type: Can be one of multiple types
def process_id(user_id: Union[int, str]) -> None:
    print(f"  Processing User ID: {user_id} (Type: {type(user_id)})")

process_id(101)
process_id("admin_user")

# Optional Type: Union[T, None] (can be a type T or None)
def find_user(user_id: int) -> Optional[str]:
    if user_id == 101:
        return "Bob"
    return None

print(f"User 101: {find_user(101)}")
print(f"User 999: {find_user(999)}")
print()

# ==========================================
# 3. STATIC TYPE CHECKING (mypy)
# ==========================================
# How to run static type analysis on your code:
# 1. Install mypy:
#    `pip install mypy`
# 2. Run check in terminal:
#    `mypy Type_Hints.py`
# Mypy will warn you if you pass mismatched types (e.g., passing a float to a function expecting a str).
