# Profiling.py
# Reference Guide: Profiling code execution speed (timeit, cProfile) and memory usage in Python
import timeit
import cProfile

# ==========================================
# 1. TIMEIT (Timing small code snippets)
# ==========================================
# timeit evaluates execution times by running a statement repeatedly.
print("--- 1. TIMEIT SNIPPET TIMING ---")

# Timing list comprehension vs appending to list
time_comprehension = timeit.timeit("[x**2 for x in range(1000)]", number=1000)
time_loop = timeit.timeit(
    """
res = []
for x in range(1000):
    res.append(x**2)
""",
    number=1000
)

print(f"List comprehension (1000 runs): {time_comprehension:.4f} seconds")
print(f"Loop and append (1000 runs):     {time_loop:.4f} seconds")
print()

# ==========================================
# 2. cPROFILE (Performance profiling)
# ==========================================
# cProfile profiles entire program runs, tracking call counts and call durations.
print("--- 2. cPROFILE STATS ---")

def dummy_work():
    total = 0
    for i in range(100000):
        total += i
    return total

# Programmatic profiling run
cProfile.run("dummy_work()")

# To profile an entire script from command-line:
#   `python -m cProfile -s tottime my_script.py`
print()

# ==========================================
# 3. MEMORY PROFILING
# ==========================================
# Tracking memory footprint line-by-line using `memory_profiler`.
# 1. Install: `pip install memory-profiler`
# 2. Annotate function: `@profile`
# 3. Run: `python -m memory_profiler script.py`
#
# Output shows increment in memory usage (MiB) for each code line.
print("Memory profiling reference configured!")
print()
