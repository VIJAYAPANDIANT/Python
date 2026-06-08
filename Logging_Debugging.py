# Logging_Debugging.py
# Reference Guide: Built-in Logging module, pdb debugger, and breakpoint()

# ==========================================
# 1. THE LOGGING MODULE
# ==========================================
# Avoid using print() for application diagnostic output. Use logging instead.
# Severity Levels: DEBUG < INFO < WARNING < ERROR < CRITICAL
import logging

print("--- 1. LOGGING DEMONSTRATION ---")
# Configure logger to output to console
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

logging.debug("This is a DEBUG message (diagnostic)")
logging.info("This is an INFO message (general event)")
logging.warning("This is a WARNING message (potential issue)")
logging.error("This is an ERROR message (failure)")
logging.critical("This is a CRITICAL message (severe system crash)")
print()

# ==========================================
# 2. DEBUGGING WITH PDB AND BREAKPOINT()
# ==========================================
# breakpoint() (introduced in Python 3.7) starts the interactive debugger (pdb).
#
# Commands inside pdb CLI:
#   n (next)        -> Execute next line
#   s (step)        -> Step into function
#   c (continue)    -> Continue execution until next breakpoint/finish
#   p <var> (print) -> Evaluate/print variable value
#   q (quit)        -> Terminate program

def calculate_complex_val(x):
    # Enters debugger shell automatically when executed:
    # breakpoint() 
    return x * 10

result = calculate_complex_val(5)
print(f"Debugger simulation finished. Result: {result}")
print()
