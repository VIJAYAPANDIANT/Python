# =====================================================================
# FILE: Variable.py
# DESCRIPTION: Variables, memory references (`id()`), and basic string transformations.
#
# SYNTAX QUICK-REFERENCE:
#   x = 10
#   print(id(x))  # Unique memory address
#   name = "Abbas Ali"
#   print(name.upper())  # "ABBAS ALI"
# =====================================================================

# Variable.py
# Reference Guide: Variables, Memory IDs, and Common String Operations

# ==========================================
# 1. WHAT IS A VARIABLE?
# ==========================================
# A variable is a named container that references a memory location storing a value.
print("--- 1. VARIABLES & IDENTITY ---")

full_name = "Abbas Ali"
print(f"Variable Value: {full_name}")
print(f"Variable Type:  {type(full_name)}")
print(f"Memory Address (id()): {id(full_name)}") # Unique ID / Memory reference
print()

# ==========================================
# 2. STRING MANIPULATION METHODS
# ==========================================
# Common string manipulation methods using the variable:
print("--- 2. STRING MANIPULATION ---")
print(f"Uppercase:       '{full_name.upper()}'")
print(f"Lowercase:       '{full_name.lower()}'")
print(f"Title Case:      '{full_name.title()}'")
print(f"Replace 'Ali':   '{full_name.replace('Ali', 'Khan')}'")
print(f"Find 'Ali' index: {full_name.find('Ali')}")
print(f"Count 'Ali':      {full_name.count('Ali')}")
print(f"Starts with 'Abbas': {full_name.startswith('Abbas')}")
print(f"Split words:      {full_name.split()}")
print(f"Joined:          '{'-'.join(['Abbas', 'Ali'])}'")
print()
