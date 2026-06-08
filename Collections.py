# =====================================================================
# FILE: Collections.py
# DESCRIPTION: Lists, tuples, dictionaries, sets, slicing, unpacking, and set operations.
#
# SYNTAX QUICK-REFERENCE:
#   # Slicing: list[start:stop:step]
#   nums = [1, 2, 3, 4, 5]
#   print(nums[1:4])   # [2, 3, 4]
#   print(nums[::-1])  # [5, 4, 3, 2, 1] (reversed)
#
#   # Tuple Unpacking and Swapping
#   x, y = 10, 20
#   x, y = y, x        # Swap variables
#
#   # Set operations
#   a = {1, 2, 3}
#   b = {3, 4, 5}
#   print(a | b)  # Union {1, 2, 3, 4, 5}
#   print(a & b)  # Intersection {3}
#   print(a - b)  # Difference {1, 2}
# =====================================================================

# Collections.py
# Reference Guide: Lists, Tuples, Dictionaries, Sets, Indexing, Slicing, and Comprehensions

# ==========================================
# 1. LISTS & SLICING
# ==========================================
# A list is an ordered, changeable collection that allows duplicates.

print("--- 1. LISTS & SLICING ---")
fruits = ["apple", "banana", "cherry"]
nums = [1, 2, 3, 4, 5]

# Indexing (Positive and Negative)
print(f"Index 0: {fruits[0]}, Index 1: {fruits[1]}, Index -1: {fruits[-1]}")

# Slicing: list[start:stop:step]
print(f"nums[1:4]   -> {nums[1:4]}")   # [2, 3, 4]
print(f"nums[:3]    -> {nums[:3]}")    # [1, 2, 3]
print(f"nums[2:]    -> {nums[2:]}")    # [3, 4, 5]
print(f"nums[::2]   -> {nums[::2]}")   # [1, 3, 5]  (every second item)
print(f"nums[::-1]  -> {nums[::-1]}")  # [5, 4, 3, 2, 1]  (reversed list)

# List Methods
fruits.append("mango")          # Add to end
fruits.insert(1, "orange")      # Add at index 1
print(f"After additions: {fruits}")
fruits.remove("banana")         # Remove by value
fruits.pop()                    # Remove last item
fruits.pop(1)                   # Remove by index
print(f"After removals: {fruits}")

# Sorting & Reversing
list_to_sort = [3, 1, 4, 2]
list_to_sort.sort()
print(f"Sorted: {list_to_sort}")

# Looping with index (enumerate)
for idx, fruit in enumerate(fruits):
    print(f"  Index {idx}: {fruit}")

# List Comprehension
squares = [i * i for i in range(1, 6)]
evens = [i for i in range(1, 11) if i % 2 == 0]
print(f"Squares list comprehension: {squares}")
print(f"Evens list comprehension: {evens}")

# Nested Lists (2D List)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"Matrix [1][2] (row index 1, col index 2): {matrix[1][2]}")
print()

# ==========================================
# 2. TUPLES
# ==========================================
# A tuple is ordered and immutable (cannot be changed). Allows duplicates.
print("--- 2. TUPLES ---")
fruits_tuple = ("apple", "banana", "cherry")
single_item_tuple = (42,) # ⚠️ Comma is mandatory for single item tuples
print(f"Tuple: {fruits_tuple}, Single item tuple: {single_item_tuple}")

# Tuple Unpacking
a, b, c = fruits_tuple
print(f"Unpacked: a={a}, b={b}, c={c}")

# Swap variables using tuples:
x, y = 10, 20
x, y = y, x
print(f"Swapped via tuple packing/unpacking: x={x}, y={y}")
print()

# ==========================================
# 3. DICTIONARIES
# ==========================================
# A dictionary stores data as key: value pairs. Ordered, mutable, no duplicate keys.
print("--- 3. DICTIONARIES ---")
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}

# Accessing Values
print(f"Brackets access: {student['name']}")
print(f"Safe get method: {student.get('age')}")
print(f"Safe get with fallback: {student.get('city', 'Not Found')}") # Returns "Not Found" instead of raising KeyError

# Adding/Updating & Deleting
student["city"] = "NY"   # Add new key
student["age"] = 25      # Update key
print(f"Updated dictionary: {student}")
student.pop("age")       # Remove by key
print(f"Dictionary after pop: {student}")

# Looping through Dictionary
print("Looping items:")
for key, value in student.items():
    print(f"  {key}: {value}")

# Dictionary Comprehension
squares_dict = {i: i*i for i in range(1, 4)}
print(f"Dict Comprehension: {squares_dict}")
print()

# ==========================================
# 4. SETS
# ==========================================
# A set is unordered and unindexed. No duplicate items allowed.
print("--- 4. SETS ---")
nums_set = {1, 2, 2, 3, 3, 3}
print(f"Unique values only: {nums_set}") # {1, 2, 3}

empty_set = set() # ⚠️ Note: {} creates an empty dict, not a set!

# Set Methods
nums_set.add(4)
nums_set.remove(2) # Raises KeyError if not present
nums_set.discard(10) # Safe discard, does not raise error if not present
print(f"Modified Set: {nums_set}")

# Set Operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print(f"Set A: {set_a}, Set B: {set_b}")
print(f"  Union (a | b):        {set_a | set_b}")         # All elements
print(f"  Intersection (a & b): {set_a & set_b}")         # Common elements
print(f"  Difference (a - b):   {set_a - set_b}")         # Elements in A but not B
print(f"  Symmetric Diff (a ^ b):{set_a ^ set_b}")        # Elements unique to either set

# Remove duplicates from list (Trick)
duplicate_list = [1, 2, 2, 3, 3, 3, 4]
clean_list = list(set(duplicate_list))
print(f"List with duplicates: {duplicate_list} -> Clean list: {clean_list}")
print()
