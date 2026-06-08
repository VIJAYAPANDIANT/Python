# =====================================================================
# FILE: Metaclasses_Descriptors.py
# DESCRIPTION: Class instantiation via `__new__`, custom metaclasses (`type` inheritance), and descriptor property validation protocols.
#
# SYNTAX QUICK-REFERENCE:
#   # Metaclass
#   class Meta(type):
#       def __new__(cls, name, bases, dct):
#           return super().__new__(cls, name, bases, dct)
#
#   # Descriptor Protocol
#   class Descriptor:
#       def __get__(self, instance, owner): pass
#       def __set__(self, instance, value): pass
# =====================================================================

# Metaclasses_Descriptors.py
# Reference Guide: Metaclasses (__new__, type) and Descriptors (__get__, __set__)

# ==========================================
# 1. UNDERSTANDING __new__ VS __init__
# ==========================================
# - __new__ is the actual constructor. It is a static method called to CREATE the object instance.
# - __init__ is the initializer. It is called to INITIALIZE the attributes of the created instance.
print("--- 1. __new__ VS __init__ ---")

class DemoClass:
    def __new__(cls, *args, **kwargs):
        print("  __new__: Creating instance in memory")
        instance = super().__new__(cls)
        return instance

    def __init__(self, name):
        print("  __init__: Initializing instance attributes")
        self.name = name

obj = DemoClass("Test")
print()

# ==========================================
# 2. METACLASSES
# ==========================================
# A Metaclass is a "class of a class". It defines how classes are constructed. 
# Just as objects are instances of classes, classes are instances of metaclasses.
# By default, Python uses 'type' as the metaclass.
print("--- 2. CUSTOM METACLASS ---")

class VerifyAttributesMeta(type):
    # __new__ is called when the class structure is loaded/defined:
    def __new__(cls, name, bases, dct):
        print(f"  [Metaclass] Defining class: {name}")
        # Enforce that all class methods/attributes must have lowercase names
        for key in dct:
            if not key.startswith("__") and not key.islower():
                raise TypeError(f"Attribute/Method '{key}' must be lowercase!")
        return super().__new__(cls, name, bases, dct)

# Apply the metaclass:
class CorrectClass(metaclass=VerifyAttributesMeta):
    my_variable = 10
    def perform_action(self):
        pass

print("  Class loaded successfully!")

# Un-commenting the following block will throw a TypeError at definition time:
# class BadClass(metaclass=VerifyAttributesMeta):
#     MyVariable = 20
print()

# ==========================================
# 3. DESCRIPTORS
# ==========================================
# A descriptor is an object attribute with "binding behavior", whose attribute 
# access is overridden by methods in its descriptor protocol: __get__(), __set__(), and __delete__().
print("--- 3. DESCRIPTORS ---")

class NonNegative:
    """Descriptor that ensures attributes are always positive numbers."""
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        # Return the value from the instance dict
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError(f"Value for '{self.name}' cannot be negative!")
        instance.__dict__[self.name] = value

class Product:
    # Set the descriptor class attributes
    price = NonNegative("price")
    quantity = NonNegative("quantity")

    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

item = Product(100, 5)
print(f"Product Price: {item.price}, Qty: {item.quantity}")

try:
    item.price = -50
except ValueError as e:
    print(f"  Descriptor validation caught error: {e}")
print()
