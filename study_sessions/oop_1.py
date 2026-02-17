# # Comments show expected output

# print(type("Hello"))                # <class 'str'>
# print(type(5))                      # <class 'int'>
# print(type([1, 2, 3]))              # <class 'list'>

# # Create an empty class named Cat.

# class Cat:
#     pass

# print(Cat)

# # Using the code from the previous exercise, create an instance of Cat and assign it to a variable named kitty.


# class Cat:
#     pass

# kitty = Cat()
# kitty2 = Cat()
# print(kitty)
# print(kitty2)

# #Using the code from the previous exercise, add a __init__ method that prints I'm a cat! when a new Cat object is instantiated.

# class Cat:
#     def __init__(self):
#         print("I'm a cat")

# kitty = Cat()

# # Using the code from the previous exercise, add a parameter to __init__ that provides a name for the Cat object. Use an instance variable to print a greeting with the provided name. (You can remove the code that displays I'm a cat!.)

# class Cat:
#     def __init__(self, name):
#         self.name = name
#         print(f"Hello {self.name}!")

# kitty2 = Cat("Ginger")

# #Using the code from the previous exercise, move the greeting from the __init__ method to an instance method named greet that prints a greeting when invoked.

# class Cat:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         print(f"Hello {self.name}!")

# kitty2 = Cat("Gingerish")
# kitty2.greet()
# Cat.greet(kitty2)

# #Using the code snippet provided below, modify the instance variable name to indicate to developers that it is intended for internal use only.

# class Cat:
#     def __init__(self, name):
#         self._name = name

#     def greet(self):
#         print(f"Hello! My name is {self._name}!")

# kitty3 = Cat('Sophie')
# kitty3.greet()
# kitty3._name = "Also Sophie"
# print(kitty3._name)
# kitty3.greet()

# Single Underscore Prefix: Prefixing an instance variable's name with a single underscore (e.g., self._name) signals other developers that the variable is meant for internal use. However, this is merely a convention and doesn't prevent external access. It's a gentle "nudge" to say, "please don't touch this directly."

#Double Underscore Prefix: When an instance variable is prefixed with double underscores (e.g., __name), Python will "mangle" the name by adding a prefix of _ClassName to it. This mechanism is to avoid name clashes with attributes defined by subclasses. While this doesn't make it private in the strictest sense, it does make it harder to access from outside the class and is a stronger hint that it's intended for internal use.

# Using the code snippet provided below, add a getter method named name and invoke it in place of self._name in greet.
# class Cat:
#     def __init__(self, name):
#         self._name = name

#     @property
#     def name(self):
#          return self._name

#     @name.setter
#     def name(self, new_name):
#         self._name = new_name

#     def greet(self):
#         print(f"Hello! My name is {self._name}!")

# kitty = Cat('Sophie')
# kitty.greet()


# #Since we can't prevent unrestricted access to instance variables, the next best approach is to provide getter and setter methods for the instance variables a user might want to access or modify. Getters and setters are common in OOP; they are methods that provide controlled access to an object's attributes. Getters retrieve attribute values, while setters assign attributes to new values.


# class Person:
#     def __init__(self, name):
#         self._name = name   # Private by convention

#     def get_name(self):
#         return self._name   # Getter

#     def set_name(self, value):
#         if not value:
#             raise ValueError("Name cannot be empty")
#         self._name = value  # Setter

# p = Person("Alice")
# print(p.get_name())     # Alice
# p.set_name("Bob")
# print(p.get_name())     # Bob


# class Person:
#     def __init__(self, name):
#         self._name = name

#     @property
#     def name(self):
#         """Getter"""
#         return self._name

#     @name.setter
#     def name(self, value):
#         """Setter"""
#         if not value:
#             raise ValueError("Name cannot be empty")
#         self._name = value

# p = Person("Alice")
# print(p.name)       # Alice (calls getter)
# p.name = "Bob"      # Calls setter
# print(p.name)       # Bob

# """
# 1. Name Mangling with Double Underscores
# Prefixing an attribute with double underscores (e.g., __name) triggers name mangling, making it harder (but not impossible) to access directly.
# Even so, the attribute can still be accessed via _ClassName__attributeName if someone really wants to.

# 2. Single Underscore Convention
# Prefixing with a single underscore (_name) signals “this is intended to be private,” but it is just a convention.
# It relies on developers not accessing it directly.

# 3. Getter and Setter Methods
# By using getter and setter methods (especially with @property), all attribute access goes through your controlled methods.
# You can place validation, logging, or other logic in these methods.

# 4. Relying on Developer Discipline
# Python trusts the developer not to “break into” attributes that are meant to be private. It’s a “we are all consenting adults” philosophy.
# """

# class Person:
#     def __init__(self, name):
#         self._name = name

#     @property
#     def name(self):
#         # Could add logic/validation here
#         return self._name

#     @name.setter
#     def name(self, value):
#         if not value:
#             raise ValueError("Name cannot be empty")
#         self._name = value

# p = Person("Alice")
# p.name = ""  # Raises ValueError

"""

As long as the attribute is only accessed and modified using the getter/setter, data integrity is enforced.

However, it’s still technically possible to bypass this, e.g., by writing p._name = "" directly, but this breaks the encapsulation contract and is discouraged.
"""

# Create a class named Person.

# When you instantiate a Person object, you should pass in one argument that contains the person's name.

# If no arguments are given, the Person object should be instantiated with a name of "John Doe".
class Person:
    def __init__(self, name="John Doe"):
        self.name = name

person1 = Person()
person2 = Person("Pepe Le Pew")

# Comments show expected output
print(person1.name)    # John Doe
print(person2.name)    # Pepe Le Pew

