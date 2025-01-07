# Create a class named Cat for which calling Cat.generic_greeting prints Hello! I'm a cat!.

# Expected output:
# Hello! I'm a cat!
# This needs a class method!

class Cat:
    @classmethod
    def generic_greeting(cls):
        print("Hello! I'm a cat!")


Cat.generic_greeting()

'''generic_greeting is a method invoked on a class, not on an instance of a class.

Class methods are defined differently from instance methods. They are denoted by @classmethod decorator. Instead of 
receving a reference to the instance as their first parameter (conventionally named as self), .they receive
a reference to the class itself, named cls.

Like in instance methods, we can place any statment we want inside a class method. In our solution we use print.

Class methods in Python are bound to the class, not any instance of the class. This means they can be invoked
on the class itself, without needing to create an instance first.

Interestingly, they can be also called using an instance of the class. When called using an instance,
the instance's class is automatically passed as the first argument, rather than the instance itself.'''


# class Cat:
#     @classmethod
#     def generic_greeting(cls):
#         print(f"Hello! I'm a {cls.__name__}!")

class Cat:
    @classmethod
    def generic_greeting(cls):
        print(f"Hello! I'm a cat!")


kitty = Cat()
kitty.generic_greeting()  # Hello! I'm a cat!'

'''This is not recommended as it hides the fact that generic_greeting is a class method.'''

# Further exploration:
# What happens if you run type(kitty).generic_greeting()?

print()
type(kitty).generic_greeting()

# changes, testing what happens in git
