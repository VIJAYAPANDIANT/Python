# =====================================================================
# FILE: Dataclasses.py
# DESCRIPTION: Auto-generating class methods, field attributes customization, mutable default values, and slots performance.
#
# SYNTAX QUICK-REFERENCE:
#   from dataclasses import dataclass, field
#
#   @dataclass(slots=True)
#   class Point:
#       x: float
#       y: float
#       history: list = field(default_factory=list)
# =====================================================================

# Dataclasses.py
# Reference Guide: Dataclasses (@dataclass), field customization, and slots optimization
from dataclasses import dataclass, field
from typing import List

# ==========================================
# 1. BASIC DATACLASS
# ==========================================
# The @dataclass decorator automatically generates common methods like __init__, __repr__, and __eq__.
print("--- 1. BASIC @dataclass ---")

@dataclass
class User:
    username: str
    email: str
    age: int = 18 # Default parameter

user1 = User("alice", "alice@example.com", 25)
user2 = User("bob", "bob@example.com")
user3 = User("alice", "alice@example.com", 25)

print(f"User 1 object representation: {user1}") # auto-generated __repr__
print(f"Are User 1 and User 3 equal?  {user1 == user3}") # auto-generated __eq__ (True)
print()

# ==========================================
# 2. CUSTOM FIELD AND DEFAULT_FACTORY
# ==========================================
# If default values are mutable objects (like lists or dicts), use field(default_factory=...) 
# to avoid shared references across instances.
print("--- 2. FIELD & DEFAULT FACTORIES ---")

@dataclass
class Team:
    name: str
    # Enforces creation of a new list instance for each new team object:
    members: List[str] = field(default_factory=list)
    # Hides a field from representation output:
    secret_key: str = field(default="ABC123XYZ", repr=False)

team_a = Team("Red Tigers")
team_a.members.append("Alice")
team_b = Team("Blue Sharks")

print(f"Team A: {team_a}")
print(f"Team B: {team_b} (Notice members list is empty and secret_key is hidden)")
print()

# ==========================================
# 3. PERFORMANCE OPTIMIZATION WITH SLOTS
# ==========================================
# Enforcing slots using `slots=True` (Python 3.10+) reduces memory overhead by preventing 
# the creation of instance dictionaries (__dict__) and speeds up attribute access.
print("--- 3. DATACLASS SLOTS ---")

@dataclass(slots=True)
class FastPoint:
    x: float
    y: float

p = FastPoint(10.5, 20.5)
print(f"FastPoint: {p}")
# Attempting to add new attributes dynamically on slotted classes raises an AttributeError:
# p.z = 30.0 # ❌ Raises AttributeError
print()
