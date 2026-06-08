# =====================================================================
# FILE: File_Handling.py
# DESCRIPTION: File modes, `with` statements, JSON reading/writing, cursor seek/tell operations, and modern `pathlib`.
#
# SYNTAX QUICK-REFERENCE:
#   # Pathlib Paths
#   from pathlib import Path
#   path = Path("test.txt")
#   path.write_text("Hello!")
#   content = path.read_text()
#
#   # JSON serialization
#   import json
#   with open("data.json", "w") as f:
#       json.dump({"name": "Alice"}, f)
# =====================================================================

# File_Handling.py
# Reference Guide: Writing, Reading, Appending, JSON Handling, and Directory Operations in Python
import os
import json

# ==========================================
# 1. FILE MODES
# ==========================================
# "r"  - Read (default) - Error if file not found
# "w"  - Write - Creates or overwrites file
# "a"  - Append - Adds content to end of file
# "x"  - Create - Error if file exists
# "r+" - Read & Write
# "rb" - Read Binary, "wb" - Write Binary

# ==========================================
# 2. READING, WRITING, AND APPENDING
# ==========================================
print("--- 1. WRITING & READING FILE ---")
filename = "scratch_test.txt"

# Writing a file (Old way using open/close)
file = open(filename, "w")
file.write("Hello, World!\n")
file.write("Python File Handling\n")
file.close()

# Reading the file (Best practice: with statement - auto-closes)
with open(filename, "r") as file:
    content = file.read()
    print("Full file content:")
    print(content)

# Reading specific lines
with open(filename, "r") as file:
    print(f"readline() (first line): '{file.readline().strip()}'")
    file.seek(0) # reset position to beginning
    print(f"readlines() list of lines: {file.readlines()}")
print()

# Appending to a file
print("--- 2. APPENDING TO FILE ---")
with open(filename, "a") as file:
    file.write("New line appended!\n")

with open(filename, "r") as file:
    print(file.read())
print()

# File Positions (seek/tell)
print("--- 3. FILE POSITIONS ---")
with open(filename, "r") as file:
    print(f"Read first 5 chars: '{file.read(5)}'")
    print(f"Current Position (tell()): {file.tell()}")
    file.seek(0) # reset
    print(f"After seek(0), read first line: '{file.readline().strip()}'")
print()

# ==========================================
# 3. LISTS & JSON FILES
# ==========================================
print("--- 4. WRITING & READING LISTS ---")
students = ["Alice\n", "Bob\n", "Charlie\n"]
with open("students.txt", "w") as file:
    file.writelines(students)

with open("students.txt", "r") as file:
    for line in file:
        print(f"  Student: {line.strip()}")
print()

print("--- 5. JSON HANDLING ---")
student_data = {"name": "Alice", "age": 20, "grade": "A"}

# Write JSON
json_filename = "student.json"
with open(json_filename, "w") as file:
    json.dump(student_data, file, indent=4)

# Read JSON
with open(json_filename, "r") as file:
    data = json.load(file)
    print(f"Parsed JSON - Name: {data['name']}, Age: {data['age']}")
print()

# ==========================================
# 4. EXCEPTION HANDLING IN FILE OPERATIONS
# ==========================================
print("--- 6. SAFE FILE LOADING ---")
try:
    with open("missing_file.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Handled gracefully: The requested file does not exist!")
print()

# ==========================================
# 5. PATHLIB FOR MODERN PATH HANDLING
# ==========================================
print("--- 7. PATHLIB OPERATIONS ---")
from pathlib import Path

# Creating paths
path = Path("scratch_pathlib_test.txt")

# Writing content using pathlib
path.write_text("Hello via pathlib!")

# Reading content using pathlib
content_pathlib = path.read_text()
print(f"Pathlib read: '{content_pathlib}'")

# Path metadata and existence checks
print(f"File exists: {path.exists()}")
print(f"Is it a file? {path.is_file()}")
print(f"File name: {path.name}")
print(f"File suffix: {path.suffix}")

# Cleanup using Path.unlink()
if path.exists():
    path.unlink()
    print("Deleted pathlib file!")
print()

# ==========================================
# 6. CLEANING UP CREATED FILES & FOLDERS
# ==========================================
print("--- 7. CLEANUP & OS OPERATIONS ---")
# Remove temporary files
for f in [filename, "students.txt", json_filename]:
    if os.path.exists(f):
        os.remove(f)
        print(f"Removed temporary file: {f}")

# Folder Operations
folder_name = "demo_folder"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"Created directory: {folder_name}")
    os.rmdir(folder_name)
    print(f"Deleted directory: {folder_name}")
print()
