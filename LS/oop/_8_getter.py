# Using the code snippet provided below,
# add a getter method named name and invoke it in place of self._name in greet.

# class Cat:
#     def __init__(self, name):
#         self._name = name
#
#     def greet(self):
#         print(f"Hello! My name is {self._name}!")
#
# kitty = Cat('Sophie')
# kitty.greet()

# Expected output:
# Hello! My name is Sophie!

class Cat:
    def __init__(self, name):
        self._name = name

    @property  # decorator to make name a property
    def name(self):
        return self._name  # getter method to return the value of self._name without modifying it

    def greet(self):
        print(f"Hello! My name is {self.name}!")  # invoke the getter method in place of self._name


# now we can use kitty.name instead of kitty._name
kitty = Cat('Sophie')
kitty.greet()

print('---')
'''Getter methods in Python can be defined using the @property decorator. This decorator lets us define
 a method that can be accessed like an attribute (but without calling it as a method).
 
 In our solution, we've prefixed the instance variable with an undesrscore (_name), which, by convention in Python,
indicates that the variable shouldn't be accessed directly from outside the class. \
We then define a name method with the @property decorator to act as the getter for the _name attribute.\

This lets us invoke the name method as if it were a simple attribute, both inside the class and outside the class:'''

# print(f"Hello! My name is: {self.name}!")  # inside the class
print(kitty.name)
