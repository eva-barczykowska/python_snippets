# Using the code from the previous exercise, add a parameter to __init__
# that provides a name for the Cat object.
# Use an instance variable to print a greeting with the provided name.
# (You can remove the code that displays I'm a cat!.)

# class Cat:
#     def __init__(self):
#         print("I'm a cat!")
#
# kitty = Cat('Sophie')

# Expected output:
# Hello! My name is Sophie!

class Cat:
    def __init__(self, name):
        self.name = name  # Instance variable, accessible within the Cat class and its instances
        print(f"Hello! My name is {self.name}!")


kitty = Cat('Sophie')

'''
Instance variables are variables that belong to a specific instance of a class. 
They are available to reference only after the object has been created.
In Python, instance variables are defined inside the __init__ method
 and are prefixed with self, which refers to the current instance of the class.
 
 To accept an argument when initializing Cat objects, we need to add a 
 parameter to the __init__ method. This parameter will be used to initialize the instance variable named
 self.name. The instance variable self.name is now available to reference anywhere inside the object.
 
 In the example above, 'Sophie' is dynamic, meaning we used self.name to print the value. 'Sophie' could
 easily be 'Oliver' if that string was passed instead of 'Sophie' like this:'''

class Cat:
    def __init__(self, name):
        self.name = name  # Instance variable, accessible within the Cat class and its instances
        print(f"Hello! My name is {self.name}!")


kitty2 = Cat('Oliver')