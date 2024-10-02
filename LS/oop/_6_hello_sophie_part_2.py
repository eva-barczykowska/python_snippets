# Using the code from the previous exercise, move the greeting from the __init__ method to an instance method named
# greet that prints a greeting when invoked. Make sure you write some code that invokes the method.

class Cat:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello! My name is {self.name}!")


kitty = Cat('Sophie')
kitty.greet()

# Expected output:
# Hello! My name is Sophie!

'''Instance methods are written the same way as any other methods but they're only available when 
there's an instance of the class. For example, kitty is an instance of the Cat class. Ths means, if we add the greet
method, we're able to invoke it on kitty like this: kitty.greet().'''

kitty = Cat('Sophie')
kitty.greet()  # Hello! My name is Sophie!

'''self.name can be accessed anywhere inside the object. This lets us print "Hello! My name is Sophie!" 
from greet simply my moving the statement from __init__ to greet.'''
