# Concurrency_Multiprocessing.py
# Reference Guide: Concurrency comparison (Threading vs Multiprocessing) and multiprocessing module examples
import multiprocessing
import time

# ==========================================
# 1. THREADING VS MULTIPROCESSING
# ==========================================
# - Threading: Shares memory space. Affected by the GIL. Best for I/O-bound tasks.
# - Multiprocessing: Separate memory space. Bypasses the GIL. Best for CPU-bound tasks.

# ==========================================
# 2. MULTIPROCESSING PROCESS
# ==========================================
print("--- 1. MULTIPROCESSING PROCESS ---")

def worker_task(name, delay):
    print(f"  [Process {name}] starting...")
    time.sleep(delay)
    print(f"  [Process {name}] finished!")

if __name__ == "__main__":
    # Create processes
    p1 = multiprocessing.Process(target=worker_task, args=("Alpha", 0.05))
    p2 = multiprocessing.Process(target=worker_task, args=("Beta", 0.05))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print("Process creation demo finished!")
    print()

# ==========================================
# 3. MULTIPROCESSING POOL (Data parallelism)
# ==========================================
# Pools map a function over an iterable concurrently across multiple CPU processes.

def square_num(x):
    return x * x

if __name__ == "__main__":
    print("--- 2. MULTIPROCESSING POOL ---")
    nums = [1, 2, 3, 4, 5]
    
    # Create a pool using count of available CPUs
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        # Maps square_num over nums list concurrently
        results = pool.map(square_num, nums)
        
    print(f"Original numbers: {nums}")
    print(f"Squared values:   {results}")
    print()
