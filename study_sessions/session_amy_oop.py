# Update the following code so that, instead of printing the values, each statement prints the name of the class to which it belongs.

# Comments show expected output
# print(type("Hello"))                # <class 'str'>
# print(type(5))                      # <class 'int'>
# print(type([1, 2, 3]))              # <class 'list'>

# print(("Hello".__class__))                # <class 'str'>
# print(5.0.__class__)                      # <class 'int'>
# print(([1, 2, 3].__class__))              # <class 'list'>


# Create an empty class named Cat

# from pickle import PUT


# class Cat:
#     pass

# kitty_kat = Cat()

# print(kitty_kat)

# Using the code from the previous exercise, create an instance of Cat and assign it to a variable named kitty.

# Using the code from the previous exercise, add a __init__ method that prints I'm a cat! when a new Cat object is instantiated.

# class Cat:
#     def __init__(self) -> None:
#         print("I'm a cat!")

# kitty = Cat()
# print(kitty)
# Expected outputCopy Code
# I'm a cat!

# Using the code from the previous exercise, add a parameter to __init__ that provides a name for the Cat object. Use an instance variable to print a greeting with the provided name. (You can remove the code that displays I'm a cat!.)

# class Cat:
#     def __init__(self, string):
#         self.name = string
#         print(f"Hello! My name is {self.name}!")

# kitty = Cat('Sophie')

# Hello! My name is Sophie!


# Using the code from the previous exercise, move the greeting from the __init__ method to an instance method named greet that prints a greeting when invoked. Make sure you write some code that invokes the method.

# class Cat:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         print(f"Hello! My name is {self.name}!")

# kitty = Cat('Sophie')
# kitty.greet()

# Hello! My name is Sophie!

# Using the code snippet provided below, modify the instance variable name to indicate to developers that it is intended for internal use only.

# class Cat:
#     def __init__(self, name):
#         self._name = name

#     def greet(self):
#         print(f"Hello! My name is {self._name}!")

# kitty = Cat('Sophie')
# kitty.greet()
# print(kitty._name)

# Hello! My name is Sophie!

# Using the code snippet provided below, add a getter method named name and invoke it in place of self._name in greet.

# Copy Code
# class Cat:
#     def __init__(self, name):
#         self._name = name

#     def greet(self):
#         print(f"Hello! My name is {self._name}!")

# kitty = Cat('Sophie')
# kitty.greet()
# Expected outputCopy Code
# Hello! My name is Sophie!

# Using the code snippet provided below, add a getter method named name and invoke it in place of self._name in greet.


# class Cat:
#     def __init__(self, name):
#         self._name = name

#     def get_name(self):
#         return self._name


#     def greet(self):
#         print(f"Hello! My name is {self.get_name()}!")


# kitty = Cat('Sophie')
# kitty.greet()

#--this was our solution but the LS solution is different
# class Cat:
#     def __init__(self, name):
#         self._name = name
#
#     @property
#     def name(self):
#         return self._name # return the value of _name
#
#     def greet(self):
#         print(f"Hello! My name is {self.name}!")
#
# kitty = Cat('MANCHURIAN')
# kitty.greet()

# so my assumption is that using the @property decorator automatically provides a getter method for us and is the best
# practice

# Setter
# Using the code snippet provided below, add a setter method named name. Then, rename kitty to 'Luna' and invoke greet again.

class Cat:
    def __init__(self, name, owner, age):
        self._name = name
        self._owner = owner
        self._age = age

    @property
    def name(self):
        return self._name # we need to return the value to make it a property and can be accessed like a property

    @name.setter
    def name(self, new_name):
        self._name = new_name # no need for return, the method mutates the internal state

    # def set_name(self, new_name): # we don't need this method anymore, as we have a setter now (above)
    #     self._name = new_name

    def greet(self):
        print(f"Hello! My name is {self.name}!")


kitty = Cat('Sophie', 'Paz', 13)
kitty.greet()
# kitty.set_name("Ewa") # this was when we had the method on lines 130-131, now we have a setter (lines 126-128)
# because we have the @name.setter decorator, the set_name method is no longer needed
# we can rename kitty to 'Luna' like this:
print("------")
print("changing name from Sophie to Luna...")
kitty.name = 'Luna'
kitty.greet()
# Hello! My name is Sophie!
# Hello! My name is Luna!

# print(kitty.name)
print(kitty.name)
print("-------------")
print("dir: lists ALL attributes of an object, including class attributes and methods")
print(dir(kitty))
print("-------------")
print("returns a dictionary of all attributes that live DIRECTLY on the object (no methods or class attributes)")
print("print(vars(kitty))")
print()
print(vars(kitty))