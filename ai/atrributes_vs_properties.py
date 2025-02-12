# Attributes
# Definition: An attribute is a variable that is bound to an instance (or class) and is used to store data. Attributes can hold any kind of data, including basic data types (e.g., integers, strings) and complex objects (e.g., lists, other classes).
#
# Types:
#
# Instance Attributes: These are specific to an instance of a class and are typically defined inside the __init__ method (the constructor).
# Class Attributes: These are shared across all instances of a class and are defined directly within the class body.

class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

# Properties
# Definition: A property is a special kind of attribute that provides a way to control access to an attribute.
# In Python, properties allow you to use getter and setter methods as if they were normal attributes, while still
# providing additional functionality (like validation, computed values, or logging).
#
# Usage: Properties are defined using the @property decorator, which makes it possible to define methods that can be
# accessed like attributes, enabling controlled access to private attributes.

class Dog:
    def __init__(self, name, age):
        self._name = name  # Using a private attribute
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string!")
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative!")
        self._age = value

# Key Differences:

# Access Control:
# Attributes are direct variables associated with the instance or class, while properties allow you to control access
# and perform additional logic when getting or setting the value.


# Encapsulation:
# Properties enable better encapsulation. You can hide the internal implementation (e.g., using private attributes)
# while still allowing controlled access to those attributes through properties.


# Usability:
# Properties let you use method logic (like validation) without changing the way you access that data.
# For the user of the class, it feels like accessing a simple attribute, but behind the scenes,
# there might be complex logic.


# Syntax:
# Accessing an attribute is straightforward (e.g., dog.name), while properties use the same syntax but provide access
# through a method under the hood (e.g., dog.name might trigger name() or name(value) methods).