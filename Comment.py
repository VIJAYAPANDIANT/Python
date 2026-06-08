# =====================================================================
# FILE: Comment.py
# DESCRIPTION: Comments and code documentation.
#
# SYNTAX QUICK-REFERENCE:
#   # Single line comment
#
#   """
#   Docstring used to document a function,
#   accessible via func.__doc__
#   """
# =====================================================================

# Comment.py
# Reference Guide: Code Documentation and Comments in Python

# ==========================================
# 1. WHY USE COMMENTS?
# ==========================================
# - Explain how code works to make it readable.
# - Test code blocks by commenting them out.
# - Document classes, methods, and functions.
# - Comments are completely ignored by the Python interpreter during execution.

print("--- 1. COMMENT TYPES ---")

# 1. Single-line comments: Use the hash mark (#).
# This is a single-line comment.
x = 10  # This is an inline comment.

# 2. Multi-line comments: Python doesn't have a specific syntax for multi-line comments.
# You can write multiple single-line comments:
# Line 1 of comment
# Line 2 of comment

# 3. Docstrings (Documentation Strings): 
# Used to document modules, classes, and functions. 
# Enclosed in triple quotes (''' or """). If not assigned to a variable, they act as comments.
def add(a, b):
    """
    Returns the sum of two integers.
    
    Parameters:
    a (int): First value
    b (int): Second value
    
    Returns:
    int: Sum of first and second value
    """
    return a + b

print(f"Docstring for add(): '{add.__doc__.strip()}'")
print()
