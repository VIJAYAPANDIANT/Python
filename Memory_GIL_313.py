# =====================================================================
# FILE: Memory_GIL_313.py
# DESCRIPTION: Reference count diagnostics, cyclical reference cleanup (`gc`), and Python 3.13 free-threaded no-GIL architecture.
#
# SYNTAX QUICK-REFERENCE:
#   import sys, gc
#   sys.getrefcount(obj)  # Get references count
#   gc.collect()          # Force cyclical garbage collection
# =====================================================================

# Memory_GIL_313.py
# Reference Guide: Python Memory Management (gc, Ref Counting), the GIL, and Python 3.13 Free-Threaded (no-GIL)
import sys
import gc

# ==========================================
# 1. REFERENCE COUNTING
# ==========================================
# Python's primary memory management system is reference counting.
# - When a variable points to an object, its reference count increments.
# - When a variable is deleted or goes out of scope, reference count decrements.
# - When reference count reaches 0, memory is immediately reclaimed.
print("--- 1. REFERENCE COUNTING ---")

a = [1, 2, 3]
# sys.getrefcount() returns current reference count (includes the temporary reference passed to the function)
print(f"Ref count for a: {sys.getrefcount(a) - 1}") # subtract 1 for the function call argument

b = a
print(f"Ref count for a after referencing by b: {sys.getrefcount(a) - 1}")
print()

# ==========================================
# 2. GARBAGE COLLECTION & CYCLICAL REFERENCES
# ==========================================
# Reference counting alone cannot clean up cyclic references (where objects reference each other).
# Python's cyclical garbage collector (gc module) detects and reclaims circular references.
print("--- 2. GC CYCLE CLEANUP ---")

# Setup circular reference
class Node:
    def __init__(self):
        self.partner = None

node1 = Node()
node2 = Node()
node1.partner = node2
node2.partner = node1

# Delete variables (ref count is still 1 due to cross-references)
del node1
del node2

# Force manual garbage collection run
collected = gc.collect()
print(f"Cyclic objects collected by GC: {collected}")
print()

# ==========================================
# 3. GLOBAL INTERPRETER LOCK (GIL)
# ==========================================
# The GIL is a mutex lock that ensures only one thread executes Python bytecode at a time.
# Enforces thread-safety for memory management operations (reference counts aren't thread-safe by default).

# ==========================================
# 4. PYTHON 3.13 FREE-THREADED (NO-GIL)
# ==========================================
# Python 3.13 introduced an experimental "Free-threaded" build option 
# that allows running CPython without the Global Interpreter Lock (GIL).
#
# Key Features:
# - Replaces GIL with thread-safe data structures, biased reference counting, and hazard pointers.
# - Allows true CPU parallelism using standard threads (`threading` module) on multi-core processors.
#
# Execution check (How to check if GIL is disabled in running environment):
#   `import sys`
#   `sys._is_gil_enabled()` -> Returns True/False (Only available in 3.13+ builds)
print(f"GIL enabled check (if 3.13+): {getattr(sys, '_is_gil_enabled', lambda: 'Function not available in this Python version')()}")
print()
