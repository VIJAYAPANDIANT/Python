# Design_Patterns.py
# Reference Guide: Design Patterns in Python (Singleton, Factory, and Observer)

# ==========================================
# 1. SINGLETON PATTERN
# ==========================================
# Enforces that a class has only one instance and provides a global access point to it.
print("--- 1. SINGLETON PATTERN ---")

class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            # Create instance if not already existing
            cls._instance = super().__new__(cls)
        return cls._instance

s1 = Singleton()
s2 = Singleton()

print(f"s1 address: {id(s1)}")
print(f"s2 address: {id(s2)}")
print(f"Are s1 and s2 the exact same instance? {s1 is s2}") # True
print()

# ==========================================
# 2. FACTORY PATTERN
# ==========================================
# Defines an interface for creating objects, letting subclasses decide which class to instantiate.
print("--- 2. FACTORY PATTERN ---")

class Dog:
    def speak(self): return "Woof!"

class Cat:
    def speak(self): return "Meow!"

class PetFactory:
    @staticmethod
    def get_pet(pet_type: str):
        pets = {"dog": Dog(), "cat": Cat()}
        return pets.get(pet_type.lower())

dog = PetFactory.get_pet("dog")
cat = PetFactory.get_pet("cat")

print(f"Factory Dog: {dog.speak()}")
print(f"Factory Cat: {cat.speak()}")
print()

# ==========================================
# 3. OBSERVER PATTERN
# ==========================================
# Defines a one-to-many dependency between objects, alerting all dependents when state changes.
print("--- 3. OBSERVER PATTERN ---")

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class Observer:
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"  [Observer {self.name}] Received Notification: '{message}'")

# Usage
news_feed = Subject()

obs1 = Observer("Alice")
obs2 = Observer("Bob")

news_feed.attach(obs1)
news_feed.attach(obs2)

news_feed.notify("Python 3.13 Free-threaded build is live!")
print()
