# Using the code from the previous exercise, add an __init__ method that prints I'm a cat! when a new Cat object
# class Cat:
#     pass
#
# kitty = Cat()
# I'm a cat!

class Cat:
    def __init__(self):
        print(f"I'm a cat!")  # This will be executed when a new Cat object is created


kitty = Cat()
'''When defining a class, we need to use the __init__ method to initialize
the object's state. The __init__ method gets called automatically when a new \
object of the class is created

Inside the __init__ method, we can execute statements that set up the object.

 In this case, we use the print function to display I'm a Cat when a new 
 Cat object is instantiated.'''