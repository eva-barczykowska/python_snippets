# Using the code snippet provided below, modify the instance variable name to indicate to developers that
# it is intended for internal use only.

# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def greet(self):
#         print(f"Hello! My name is {self.name}!")
#
# kitty = Cat('Sophie')
# kitty.greet()

# Expected output:
# Hello! My name is Sophie!

# SOLUTION 1: single underscore prefix
class Cat:
    def __init__(self, name):
        self._name = name  # here _name is used to indicate that this variable is intended for internal use only

    def greet(self):
        print(f"Hello! My name is {self._name}!")


kitty = Cat('Sophie')
kitty.greet()

# SOLUTION 2: double underscore prefix
class Cat:
    def __init__(self, name):
        self.__name = name  # here __name is used to indicate that this variable is intended for internal use only

    def greet(self):
        print(f"Hello! My name is {self.__name}!")


kitty = Cat('Sophie')
kitty.greet()

'''In Python we can prefix instance variable names with _ or __ to indicate that they are intended for 
internal use.

Single underscore prefix: _name
Prefixing an instance variable name with a single underscore (e.g. self._name) signals to other developers that 
the variable is meant for internal use and should not be accessed or modified directly. However,
this is only a convention and does not prevent the variable from being accessed or modified.

Double underscore prefix: __name
When an instance variable name is prefixed with double underscore (e.g. self.__name), Python will 
"mangle" the variable name by adding a single prefix of _ClassName to it. This mechanism is to avoid name
clashes with attributes defined by subclasses. While this doesn't make it private in the strictest sense,
it does make it harder to access from outside the class and is a stronger hint that it's intended for internal use.'''
