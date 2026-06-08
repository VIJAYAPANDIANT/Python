# Regex.py
# Reference Guide: Regular Expressions (re) in Python
import re

# ==========================================
# 1. CORE FUNCTIONS
# ==========================================
# re.match()    - Match at beginning of string
# re.search()   - Search anywhere in string
# re.findall()  - Find all matches as list
# re.finditer() - Find all matches as iterator
# re.sub()      - Replace matches
# re.split()    - Split by pattern
# re.compile()  - Compile pattern for reuse

print("--- 1. BASIC FUNCTIONS ---")
text = "Hello World"

# Match checks only at beginning
print(f"re.match('Hello'): {re.match('Hello', text) is not None}") # True
print(f"re.match('World'): {re.match('World', text) is not None}") # False

# Search checks anywhere
search_res = re.search("World", text)
if search_res:
    print(f"re.search('World'): Found '{search_res.group()}' at index {search_res.start()}")

# Find all matches
print(f"re.findall('at' in 'cat bat rat mat'): {re.findall('at', 'cat bat rat mat')}")
print()

# ==========================================
# 2. SPECIAL CHARACTERS & CHARACTER CLASSES
# ==========================================
# Characters:
# .  -> Any character except newline
# ^  -> Start of string
# $  -> End of string
# *  -> 0 or more times
# +  -> 1 or more times
# ?  -> 0 or 1 time
# {n}-> Exactly n times
# \d -> Digit [0-9]
# \w -> Word char [a-zA-Z0-9_]
# \s -> Whitespace

print("--- 2. PATTERNS & CLASSES ---")
sample = "abc 123 def 4567"
print(f"Digits (\\d+): {re.findall(r'\d+', sample)}")
print(f"Words (\\w+):  {re.findall(r'\w+', sample)}")

# Quantifiers
print(f"Exact 3 digits (\\d{{3}}): {re.findall(r'\d{3}', '123 45 6789')}")
print(f"2 to 4 digits (\\d{{2,4}}): {re.findall(r'\d{2,4}', '1 22 333 4444')}")
print()

# ==========================================
# 3. GROUPS & FLAGS
# ==========================================
print("--- 3. GROUPS & FLAGS ---")
date_text = "2026-06-08"
match = re.search(r"(\d{4})-(\d{2})-(\d{2})", date_text)
if match:
    print(f"Full Date Match: {match.group(0)}")
    print(f"Year group(1):   {match.group(1)}")
    print(f"Month group(2):  {match.group(2)}")
    print(f"Day group(3):    {match.group(3)}")

# Case insensitive flag (re.I or re.IGNORECASE)
print(f"Case Insensitive search: {re.findall('hello', 'Hello WORLD', re.I)}")
print()

# ==========================================
# 4. PRACTICAL VALIDATION EXAMPLES
# ==========================================
print("--- 4. VALIDATIONS ---")
def validate_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

print(f"validate_email('alice@gmail.com'): {validate_email('alice@gmail.com')}")
print(f"validate_email('invalid-email'):   {validate_email('invalid-email')}")

# Extract URLs
web_text = "Visit https://google.com or http://python.org"
url_pattern = r"https?://[a-zA-Z0-9./]+"
print(f"Extracted URLs: {re.findall(url_pattern, web_text)}")
print()
