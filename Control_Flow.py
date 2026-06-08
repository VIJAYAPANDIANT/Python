# =====================================================================
# FILE: Control_Flow.py
# DESCRIPTION: if-statements, ternary operators, loops, and loop control statements.
#
# SYNTAX QUICK-REFERENCE:
#   # Ternary
#   result = "Adult" if age >= 18 else "Minor"
#
#   # Loops
#   for i in range(0, 5, 2):  # start, stop, step
#       print(i)              # 0 2 4
#
#   # Loop Else Clause (runs if loop finished without 'break')
#   for x in range(3):
#       pass
#   else:
#       print("No break encountered!")
#
#   # Simulated Do-While Loop
#   while True:
#       # code runs once
#       if not condition:
#           break
# =====================================================================

# Control_Flow.py
# Reference Guide: if/elif/else, for loops, while loops, and simulated do-while loops

# ==========================================
# 1. CONDITIONAL STATEMENTS (if/elif/else)
# ==========================================
# Used to execute code blocks based on conditional tests. Indentation (4 spaces) is mandatory.

print("--- 1. IF / ELIF / ELSE ---")
marks = 75
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")  # Executed for 75
else:
    print("Grade: F")

# Short Hand (One Line / Ternary)
age = 20
result = "Adult" if age >= 18 else "Minor"
print(f"Ternary operator result (age={age}): {result}")
print()

# ==========================================
# 2. LOOPS IN PYTHON
# ==========================================

# --- For Loops ---
# Iterating over sequences (lists, strings, range)
print("--- 2. FOR LOOPS & RANGE ---")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit, end=" ")
print("\nLooping through string:")
for letter in "Hello":
    print(letter, end="-")
print()

# range() usage:
# - range(stop) -> 0 to stop-1
# - range(start, stop) -> start to stop-1
# - range(start, stop, step) -> incrementing/decrementing
print("\nRange demonstrations:")
print("range(3):", list(range(3)))
print("range(1, 5):", list(range(1, 5)))
print("range(0, 10, 2):", list(range(0, 10, 2)))
print("range(5, 0, -1) (Countdown):", list(range(5, 0, -1)))
print()

# --- While Loops ---
# Repeats as long as a condition remains True. Must update control variable to avoid infinite loops.
print("--- 3. WHILE LOOPS ---")
i = 1
while i <= 3:
    print(f"i is: {i}")
    i += 1
print()

# --- Loop Control Statements ---
# break: Exit loop immediately
# continue: Skip current iteration
# pass: Do nothing (placeholder)
print("--- 4. BREAK & CONTINUE ---")
print("Break at 5:")
for num in range(10):
    if num == 5:
        break
    print(num, end=" ")
print("\nContinue (skips 3):")
for num in range(6):
    if num == 3:
        continue
    print(num, end=" ")
print()

# --- Else clause with Loops ---
# Runs when loop finishes normally (without encountering a 'break').
print("\nLoop Else Clause:")
for num in range(3):
    print(f"Looping {num}")
else:
    print("Loop finished normally!")

print("\nLoop Else Clause with Break:")
for num in range(3):
    if num == 1:
        break
    print(f"Looping {num}")
else:
    print("This will not print because break was used.")
print()

# ==========================================
# 3. DO-WHILE LOOP SIMULATION
# ==========================================
# Python does not have a built-in do-while loop.
# It is simulated using 'while True:' and a conditional 'break' at the end.
# This ensures that the code runs AT LEAST ONCE.

print("--- 5. SIMULATED DO-WHILE ---")
# Simulated Do-While Counter
count = 1
while True:
    print(f"Count (always runs once): {count}")
    count += 1
    if count > 3:
        break

# Simulated Password Checker (Uses simulated user input)
correct_pwd = "python123"
inputs = ["hello", "python123"]
input_iterator = iter(inputs)

print("\nSimulated Password Checker Do-While:")
while True:
    pwd = next(input_iterator)
    print(f"Entered password: '{pwd}'")
    if pwd == correct_pwd:
        print("Access granted! [OK]")
        break
    else:
        print("Wrong password! Try again.")
print()
