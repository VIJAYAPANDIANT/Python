# =====================================================================
# FILE: OOP.py
# DESCRIPTION: OOP principles, inheritance structures, constructor overrides, and custom arithmetic operators.
#
# SYNTAX QUICK-REFERENCE:
#   class Child(Parent1, Parent2): # Multiple inheritance
#       def __init__(self, name):
#           super().__init__(name)
#
#       def __add__(self, other): # Operator Overloading (+)
#           return self.value + other.value
# =====================================================================

# OOP.py
# Reference Guide: Object-Oriented Programming (OOP) in Python
from abc import ABC, abstractmethod

# ==========================================
# 1. CLASSES, OBJECTS, CONSTRUCTORS, & SELF
# ==========================================
print("--- 1. CLASS & INSTANCE ---")
class Dog:
    species = "Mammal"  # Class variable (shared across all instances)

    def __init__(self, name, age):
        self.name = name  # Instance variable (unique to this object)
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")

# Instantiate
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(f"dog1: {dog1.name}, age {dog1.age}, species {dog1.species}")
print(f"dog2: {dog2.name}, age {dog2.age}, species {dog2.species}")
dog1.bark()
print()

# Modify & delete attributes
dog1.age = 4
print(f"Updated age of dog1: {dog1.age}")
# del dog1.age

# ==========================================
# 2. TYPES OF METHODS
# ==========================================
print("--- 2. METHOD TYPES ---")
class MethodDemo:
    class_var = 100

    def __init__(self, value):
        self.value = value

    # 1. Instance method: Takes 'self'
    def get_value(self):
        return self.value

    # 2. Class method: Takes 'cls'
    @classmethod
    def get_class_var(cls):
        return cls.class_var

    # 3. Static method: Takes no default arguments
    @staticmethod
    def get_info():
        return "This is a static method."

    # 4. Property: Access method like a variable
    @property
    def formatted_value(self):
        return f"${self.value:.2f}"

demo = MethodDemo(50)
print(f"Instance Method: {demo.get_value()}")
print(f"Class Method:    {MethodDemo.get_class_var()}")
print(f"Static Method:   {MethodDemo.get_info()}")
print(f"Property Getter: {demo.formatted_value}")
print()

# ==========================================
# 3. THE 4 PILLARS OF OOP
# ==========================================
print("--- 3. 4 PILLARS ---")

# --- Pillar 1: Encapsulation ---
# Hiding data from outside access using private variables (prefixed with double underscore __)
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds!")

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
print(f"Encapsulated Balance: {account.get_balance()}")
# print(account.__balance) # ❌ Throws AttributeError (Private!)

# --- Pillar 2: Inheritance & super() ---
# A child class inherits properties and methods from a parent class.
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Animal makes a sound")

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name) # calls parent constructor
        self.color = color
    def speak(self):
        print(f"{self.name} the {self.color} cat says Meow!")

kitty = Cat("Kitty", "white")
kitty.speak()

# --- Pillar 3: Polymorphism ---
# Same method name, different behavior across different classes.
class Bird:
    def speak(self):
        return "Tweet!"
class Duck:
    def speak(self):
        return "Quack!"

animals = [kitty, Duck(), Bird()]
print("Polymorphic invocation:")
for anim in animals:
    if hasattr(anim, "speak"):
        print(f"  {anim.speak()}")

# --- Pillar 4: Abstraction ---
# Hiding complex details, enforcing subclasses to implement abstract methods.
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def area(self):
        return self.w * self.h

rect = Rectangle(5, 3)
print(f"Abstracted Area: {rect.area()}")
print()

# ==========================================
# 4. TYPES OF INHERITANCE
# ==========================================
# 1. Single Inheritance: 1 parent -> 1 child
# 2. Multiple Inheritance: Multiple parents -> 1 child
# 3. Multilevel Inheritance: Grandparent -> Parent -> Child
# 4. Hierarchical Inheritance: 1 parent -> Multiple children
# 5. Hybrid Inheritance: Mix of the above

print("--- 4. MULTIPLE INHERITANCE & MRO ---")
class Father:
    def trait(self):
        print("Tall height")
class Mother:
    def trait(self):
        print("Fair color")
class Child(Father, Mother):
    pass

c = Child()
c.trait() # Prints "Tall height" (Father comes first in class declaration order)
print(f"Method Resolution Order (MRO): {Child.__mro__}")
print()

# ==========================================
# 5. TYPES OF POLYMORPHISM
# ==========================================
print("--- 5. POLYMORPHISM TYPES ---")

# 1. Duck Typing
class ToyDuck:
    def speak(self): print("Squeak!")
def make_it_speak(duck_like_obj):
    duck_like_obj.speak() # Python doesn't check type, just looks for 'speak()' method

make_it_speak(ToyDuck())

# 2. Method Overriding
# Done above where Cat overrides Animal's 'speak' method.

# 3. Method Overloading (Simulated in Python using default parameters or *args)
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c
    def add_all(self, *args):
        return sum(args)

calc = Calculator()
print(f"Overloaded add(5):      {calc.add(5)}")
print(f"Overloaded add(5,3):    {calc.add(5, 3)}")
print(f"Overloaded add_all(1,2,3,4): {calc.add_all(1, 2, 3, 4)}")

# 4. Operator Overloading (Using Dunder methods)
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other): # Overloads +
        return Point(self.x + other.x, self.y + other.y)
    def __str__(self): # Overloads str() representation
        return f"Point({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(3, 4)
print(f"p1 + p2 = {p1 + p2}")
print()
