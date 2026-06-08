# =====================================================================
# FILE: C_Extensions.py
# DESCRIPTION: Interacting with native C libraries using ctypes, Cython, and cffi.
#
# SYNTAX QUICK-REFERENCE:
#   import ctypes
#   libc = ctypes.CDLL("libc.so.6")
#   libc.puts(b"Hello standard C library puts!")
# =====================================================================

# C_Extensions.py
# Reference Guide: Writing/Loading C Extensions in Python (ctypes, Cython, cffi)

# ==========================================
# 1. CTYPES (Standard Library)
# ==========================================
# ctypes is a foreign function library for Python. It provides C compatible data types, 
# and allows calling functions in DLLs or shared libraries.
print("--- 1. CTYPES (Foreign Function interface) ---")

import ctypes
import os

# Loading standard C library (platform specific)
try:
    if os.name == "nt":  # Windows
        libc = ctypes.cdll.msvcrt
    else:  # Linux/Mac
        libc = ctypes.CDLL("libc.so.6")

    # Calling C's puts function
    # puts returns int, takes pointer to string
    libc.puts(b"Hello from C stdlib puts() via ctypes!")
except Exception as e:
    print(f"Standard C Library could not be loaded: {e}")
print()

# ==========================================
# 2. CYTHON (C-Extensions for Python)
# ==========================================
# Cython is a superset of Python that compile to fast C modules.
#
# Workflow:
# 1. Create a `.pyx` file (e.g., `mymodule.pyx`):
#    --- pyx code ---
#    def fib(int n):
#        cdef int i
#        cdef int a = 0, b = 1
#        for i in range(n):
#            a, b = b, a + b
#        return a
#    ----------------
# 2. Compile using a `setup.py` build script:
#    --- setup.py ---
#    from setuptools import setup
#    from Cython.Build import cythonize
#    setup(ext_modules=cythonize("mymodule.pyx"))
#    ----------------
# 3. Build it in terminal:
#    `python setup.py build_ext --inplace`
# 4. Import the compiled `.so` or `.pyd` module directly:
#    `import mymodule`

# ==========================================
# 3. CFFI (C Foreign Function Interface)
# ==========================================
# cffi provides a modern, clean interface for interacting with C code.
# 1. Install: `pip install cffi`
# --- cffi Example ---
# from cffi import FFI
# ffi = FFI()
# # Declare signature
# ffi.cdef("int printf(const char *format, ...);")
# # Load C library
# C = ffi.dlopen(None)
# # Call function
# C.printf(b"Hello via cffi!\n")
print("C_Extensions documentation references configured!")
print()
