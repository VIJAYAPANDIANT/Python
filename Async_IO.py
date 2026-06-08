# =====================================================================
# FILE: Async_IO.py
# DESCRIPTION: Coroutines, async event loops, gathering async functions, and concurrent task execution.
#
# SYNTAX QUICK-REFERENCE:
#   import asyncio
#
#   async def worker():
#       await asyncio.sleep(1)
#
#   async def main():
#       await asyncio.gather(worker(), worker())
#
#   asyncio.run(main())
# =====================================================================

# Async_IO.py
# Reference Guide: Asynchronous Programming using asyncio, async/await, Tasks, and gather
import asyncio
import time

# ==========================================
# 1. CORE CONCEPTS
# ==========================================
# - Synchronous code runs one command at a time, blocking execution.
# - Asynchronous code allows task execution to pause/yield control back to the 
#   event loop, allowing other tasks to run concurrently during I/O operations.
# - Keywords: 'async def' defines a coroutine, 'await' pauses execution of the coroutine.

print("--- 1. DEFINING & RUNNING COROUTINES ---")
async def main():
    print("  Hello...")
    await asyncio.sleep(0.05) # Yields control
    print("  ...World!")

# Running the event loop (runs the coroutine to completion)
asyncio.run(main())
print()

# ==========================================
# 2. RUNNING CONCURRENT TASKS WITH GATHER
# ==========================================
# asyncio.gather runs multiple coroutines concurrently and collects their results.
print("--- 2. CONCURRENCY WITH asyncio.gather ---")

async def fetch_data(source_id: int, delay: float) -> str:
    print(f"  Fetching data from Source {source_id}...")
    await asyncio.sleep(delay) # Simulate network delay
    print(f"  Received data from Source {source_id}!")
    return f"Data {source_id}"

async def run_gather():
    start_time = time.time()
    # Execute fetch_data concurrently
    results = await asyncio.gather(
        fetch_data(1, 0.1),
        fetch_data(2, 0.15),
        fetch_data(3, 0.05)
    )
    end_time = time.time()
    print(f"All data gathered: {results}")
    print(f"Time elapsed: {end_time - start_time:.4f} seconds") # Will be roughly equal to the longest delay (0.15s) rather than the sum (0.3s)

asyncio.run(run_gather())
print()

# ==========================================
# 3. CREATING BACKGROUND TASKS
# ==========================================
# Tasks allow a coroutine to run in the background while other operations continue.
print("--- 3. CREATING BACKGROUND TASKS ---")

async def background_worker():
    for i in range(1, 4):
        print(f"  [Worker] Step {i}")
        await asyncio.sleep(0.05)

async def test_task():
    # Schedule the worker in the background
    task = asyncio.create_task(background_worker())
    
    print("  [Main] Doing some work...")
    await asyncio.sleep(0.08)
    print("  [Main] Waiting for worker task to complete...")
    await task # wait for it to finish

asyncio.run(test_task())
print()
