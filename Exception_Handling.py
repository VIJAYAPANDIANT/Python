# =====================================================================
# FILE: Exception_Handling.py
# DESCRIPTION: Catching multiple exceptions, raising custom error classes, `else`, and `finally` constructs.
#
# SYNTAX QUICK-REFERENCE:
#   class CustomError(Exception):
#       pass
#
#   try:
#       x = 10 / int(input())
#   except (ValueError, ZeroDivisionError) as e:
#       print(f"Handled error: {e}")
#   else:
#       print("No error occurred!")
#   finally:
#       print("Always executes!")
# =====================================================================

# Exception_Handling.py
# Reference Guide: try, except, else, finally, raising exceptions, and custom exception classes

# ==========================================
# 1. CORE CONCEPTS
# ==========================================
# try:     Code that might fail/cause error
# except:  Runs if an error occurs
# else:    Runs if NO error occurs
# finally: ALWAYS runs (used for cleanup)

# Common exceptions: ZeroDivisionError, ValueError, TypeError, NameError, FileNotFoundError

print("--- 1. BASIC TRY / EXCEPT / ELSE / FINALLY ---")
try:
    num = 10
    denom = 2
    result = num / denom
except ZeroDivisionError as e:
    print(f"Error: {e}")
else:
    print(f"Success! Result: {result}")
finally:
    print("This cleanup block always runs!")
print()

# ==========================================
# 2. CATCHING SPECIFIC & MULTIPLE EXCEPTIONS
# ==========================================
print("--- 2. CATCHING MULTIPLE EXCEPTIONS ---")
inputs = ["abc", "0", "5"]
for val in inputs:
    try:
        print(f"Processing input: '{val}'")
        x = int(val)
        res = 10 / x
        print(f"  Result: {res}")
    except ValueError:
        print("  Error: Please provide a valid integer!")
    except ZeroDivisionError:
        print("  Error: Cannot divide by zero!")
    except (TypeError, NameError) as e:
        print(f"  Type or Name Error: {e}")
    except Exception as e:
        print(f"  Unexpected Error: {e}")
print()

# ==========================================
# 3. RAISING CUSTOM ERRORS & CUSTOM EXCEPTION CLASSES
# ==========================================
print("--- 3. CUSTOM EXCEPTIONS ---")

# Defining a custom exception class
class AgeError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def check_age(age):
    if age < 0:
        raise AgeError("Age cannot be negative!")
    if age > 150:
        raise AgeError("Age is too large!")
    return f"Valid age: {age}"

test_ages = [-5, 20]
for a in test_ages:
    try:
        print(f"Checking age: {a}")
        msg = check_age(a)
        print(f"  {msg}")
    except AgeError as e:
        print(f"  Custom Age Error Caught: {e}")
print()

# ==========================================
# 4. NESTED TRY / EXCEPT EXAMPLES
# ==========================================
print("--- 4. NESTED TRY / EXCEPT ---")
try:
    val = int("10")
    try:
        res = val / 0
    except ZeroDivisionError:
        print("Inner block: Division by zero caught!")
except ValueError:
    print("Outer block: Invalid integer type!")
print()
