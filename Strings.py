# =====================================================================
# FILE: Strings.py
# DESCRIPTION: f-strings, common string methods, and comprehensive Regular Expressions (`re`).
#
# SYNTAX QUICK-REFERENCE:
#   # Formatting floats/percentages in f-strings
#   percentage = 0.8756
#   print(f"{percentage:.2%}")  # "87.56%"
#
#   # Common string methods
#   "  hello  ".strip()
#   "apple banana".split()
#   ",".join(["a", "b", "c"])
#
#   # Regex functions
#   import re
#   re.findall(r"\d+", "Price 100, Qty 50")  # ['100', '50']
#   re.sub(r"\d", "X", "Room 404")            # "Room XXX"
# =====================================================================

# Strings.py
# Reference Guide: f-strings, Built-in String Methods, and Regular Expressions (re)
import re

# ==========================================
# 1. f-STRINGS (Formatted String Literals)
# ==========================================
print("--- 1. f-STRINGS ---")
name = "Alice"
age = 25
percentage = 0.8756

print(f"Name: {name}, Age: {age}")
print(f"Expression calculation (5 * 5): {5 * 5}")
print(f"Formatted float percentage: {percentage:.2%}")
print(f"Greeting: Hi {name}! Next year you will be {age + 1}.")
print()

# ==========================================
# 2. BUILT-IN STRING METHODS
# ==========================================
print("--- 2. STRING METHODS & SEQUENCES ---")
text = "apple banana cherry"
sample = "  hello world  "

# len() — Length
print(f"Length of '{sample}': {len(sample)}")

# split() — Split string into list
words = text.split()
csv_data = "a,b,c".split(",")
print(f"split() default: {words}")
print(f"split(',') custom separator: {csv_data}")

# join() — Join list into string
print(f"join(' '): {' '.join(words)}")
print(f"join(','): {','.join(words)}")

# strip() — Remove leading/trailing spaces
print(f"strip(): '{sample.strip()}'")
print(f"lstrip() (left only): '{sample.lstrip()}'")
print(f"rstrip() (right only): '{sample.rstrip()}'")

# replace() — Replace substring
cat_text = "I like cats"
print(f"replace(): '{cat_text.replace('cats', 'dogs')}'")

# find() vs index() — Find position
# - find() returns -1 if substring is not found
# - index() raises a ValueError if not found
print(f"find('world') in 'Hello World': {'Hello World'.find('World')}")
print(f"find('xyz') (not found): {'Hello World'.find('xyz')}")
print(f"index('a') in 'banana': {'banana'.index('a')}")

# count() — Count occurrences
print(f"count('a') in 'banana': {'banana'.count('a')}")

# case methods: upper(), lower(), title()
print(f"upper(): '{text.upper()}'")
print(f"lower(): '{text.upper().lower()}'")
print(f"title(): '{text.title()}'")

# startswith() & endswith()
print(f"startswith('apple'): {text.startswith('apple')}")
print(f"endswith('cherry'): {text.endswith('cherry')}")

# 'in' operator - check existence
print(f"'banana' in text: {'banana' in text}")
print(f"'xyz' in text: {'xyz' in text}")
print()

# ==========================================
# 3. REGULAR EXPRESSIONS (re)
# ==========================================
print("--- 3. REGULAR EXPRESSIONS ---")
email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
sample_text = "Contact support@example.com or sales.info@domain.co.in"

# 1. re.findall() - returns list of all matches
emails = re.findall(email_pattern, sample_text)
print(f"Emails found: {emails}")

# 2. re.search() - returns match object for first match
search_match = re.search(r"sales\.\w+", sample_text)
if search_match:
    print(f"Search match found: '{search_match.group()}' at index {search_match.start()}")

# 3. re.sub() - replaces matches with target string
masked_text = re.sub(email_pattern, "[MASKED EMAIL]", sample_text)
print(f"Masked text: '{masked_text}'")
print()
