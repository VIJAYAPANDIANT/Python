# =====================================================================
# FILE: Context_Managers.py
# DESCRIPTION: Building custom context managers with classes (`__enter__`/`__exit__`) or generators (`@contextmanager`).
#
# SYNTAX QUICK-REFERENCE:
#   # Class-based
#   class CustomManager:
#       def __enter__(self):
#           return self
#       def __exit__(self, exc_type, exc_val, exc_tb):
#           pass
#
#   # Generator-based
#   from contextlib import contextmanager
#   @contextmanager
#   def resource():
#       # setup
#       yield
#       # cleanup
# =====================================================================

# Context_Managers.py
# Reference Guide: Custom Context Managers using __enter__/__exit__ and contextlib module
from contextlib import contextmanager

# ==========================================
# 1. CUSTOM CLASS-BASED CONTEXT MANAGER
# ==========================================
# A class can act as a context manager by implementing __enter__() and __exit__().
print("--- 1. CLASS-BASED CONTEXT MANAGER ---")

class ManagedFile:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print("  __enter__: Opening file")
        self.file = open(self.filename, self.mode)
        return self.file # The returned object is bound to the target of the 'as' clause

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("  __exit__: Closing file")
        if self.file:
            self.file.close()
        # Returns True to suppress exceptions if any occurred inside the block, 
        # or False to let them propagate (default).
        return False

# Usage:
with ManagedFile("scratch_context_test.txt", "w") as f:
    f.write("Hello context manager!")
    print("  Inside block: Wrote to file")

import os
if os.path.exists("scratch_context_test.txt"):
    os.remove("scratch_context_test.txt")
print()

# ==========================================
# 2. GENERATOR-BASED CONTEXT MANAGER (contextlib)
# ==========================================
# The @contextmanager decorator allows you to define a context manager using a generator function.
print("--- 2. GENERATOR-BASED CONTEXT MANAGER ---")

@contextmanager
def managed_resource(name):
    print(f"  [Setup] Allocating resource: {name}")
    try:
        yield f"Resource Object ({name})" # Everything before yield is setup
    finally:
        print(f"  [Teardown] Releasing resource: {name}") # Everything after yield (in finally block) is cleanup

# Usage:
with managed_resource("API Connection") as resource:
    print(f"  Inside block: Working with {resource}")
print()
