# =====================================================================
# FILE: Multithreading.py
# DESCRIPTION: Threads, GIL constraints, Locks/Semaphores, OS processes, and process pool data distribution.
#
# SYNTAX QUICK-REFERENCE:
#   import threading
#   lock = threading.Lock()
#   with lock:
#       # Critical section
#
#   # Multiprocessing Pool
#   import multiprocessing
#   with multiprocessing.Pool() as pool:
#       results = pool.map(func, data_list)
# =====================================================================

# Multithreading.py
# Reference Guide: Multithreading, Lock, RLock, Semaphore, Event, Timer, and GIL in Python
import threading
import time
from concurrent.futures import ThreadPoolExecutor

# ==========================================
# 1. CORE CONCEPTS
# ==========================================
# Process:        Independent running program (independent memory space)
# Thread:         Smallest unit of execution inside a process (shares memory space)
# Multithreading: Multiple threads executing concurrently
# GIL:            Global Interpreter Lock. Python only allows one thread to run at 
#                 a time for CPU-bound tasks.
#                 - I/O bound tasks (network/file operations) benefit from multithreading.
#                 - CPU bound tasks benefit from multiprocessing.

print("--- 1. BASIC THREAD CREATION ---")
def print_numbers(thread_name, delay):
    for i in range(1, 4):
        time.sleep(delay)
        print(f"[{thread_name}] Count: {i}")

# Thread creation
t1 = threading.Thread(target=print_numbers, args=("Thread-1", 0.05))
t2 = threading.Thread(target=print_numbers, args=("Thread-2", 0.05))

t1.start()
t2.start()

# Wait for both threads to finish
t1.join()
t2.join()
print("Main thread done with basic creation!")
print()

# ==========================================
# 2. THREAD SYNCHRONIZATION (Lock, RLock)
# ==========================================
print("--- 2. THREAD SYNCHRONIZATION ---")
counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(5000):
        # Using Lock as a context manager (auto acquires and releases)
        with lock:
            counter += 1

threads = [threading.Thread(target=increment) for _ in range(3)]
for t in threads: t.start()
for t in threads: t.join()
print(f"Synchronized Counter Result (expected 15000): {counter}")

# RLock (Reentrant Lock) allows the same thread to acquire a lock multiple times
rlock = threading.RLock()
with rlock:
    print("  RLock acquired once")
    with rlock:
        print("  RLock acquired twice (reentrant)")
print()

# ==========================================
# 3. SEMAPHORE, EVENT, AND TIMERS
# ==========================================
print("--- 3. ADVANCED SYNCHRONIZATION ---")

# Semaphore (Limits simultaneous thread execution to N)
sem = threading.Semaphore(2)
def worker(num):
    with sem:
        print(f"  Worker {num} entered semaphore")
        time.sleep(0.05)

sem_threads = [threading.Thread(target=worker, args=(i,)) for i in range(4)]
for t in sem_threads: t.start()
for t in sem_threads: t.join()

# Event (Signals between threads)
event = threading.Event()
def wait_for_event():
    print("  Thread waiting for event signal...")
    event.wait()
    print("  Event signal received! Proceeding...")

event_thread = threading.Thread(target=wait_for_event)
event_thread.start()
time.sleep(0.05)
print("  Main thread setting event signal...")
event.set()
event_thread.join()

# Timer (Runs after a specified delay)
def timer_callback():
    print("  Timer callback executed after delay!")

timer = threading.Timer(0.1, timer_callback)
timer.start()
timer.join()
print()

# ==========================================
# 4. THREAD POOL EXECUTOR
# ==========================================
print("--- 4. THREADPOOL EXECUTOR ---")
def task(num):
    return f"Task {num} finished"

with ThreadPoolExecutor(max_workers=2) as executor:
    results = executor.map(task, range(3))

for result in results:
    print(f"  {result}")
print()
