# # Given the class from the previous problem:

# class Rectangle:
#     def __init__(self, width, height):
#         self._width = width
#         self._height = height

#     @property
#     def width(self):
#         return self._width

#     @property
#     def height(self):
#         return self._height

#     @property
#     def area(self):
#         return self._width * self._height

# class Square(Rectangle):
#     def __init__(self, side):
#         self._side = side

#     @property
#     def side(self):
#         return self._side

#     @side.setter
#     def side(self, new_side):
#         self._side = new_side
#         return self.side

#     @property
#     def area(self):
#         return self._side * self._side
# # Write a class called Square that inherits from the Rectangle class. The Square class is used like this:

# square = Square(5)
# print(square.area == 25)      # True

# #####
# ##### --- a better solution
# print(" a better solution")
# class Rectangle:
#     def __init__(self, width, height):
#         self._width = width
#         self._height = height

#     @property
#     def width(self):
#         return self._width

#     @property
#     def height(self):
#         return self._height

#     @property
#     def area(self):
#         return self._width * self._height

# class Square(Rectangle):
#     def __init__(self, side_length):
#         super().__init__(side_length, side_length)

# square = Square(5)
# print(square.area == 25)      # True


# class Pet:
#     def __init__(self, name, age, color):
#         self._name = name
#         self._age = age
#         self._color = color

#     @property
#     def name(self):
#         return self._name

#     @property
#     def age(self):
#         return self._age

#     @property
#     def color(self):
#         return self._color

#     @property
#     def info(self):
#         return f"My {self.__class__.__name__.lower()} {self.name} is {self.age} years old and has {self.color} fur."

# class Cat(Pet):
#     def __init__(self, name, age, color):
#         super().__init__(name, age, color)

# cocoa = Cat('Cocoa', 3, 'black')
# cheddar = Cat('Cheddar', 4, 'yellow and white')

# print(cocoa.info)
# print(cheddar.info)
# # Update this code so you see the following output when you run the code:

# # Copy Code
# # My cat Cocoa is 3 years old and has black fur.
# # My cat Cheddar is 4 years old and has yellow and white fur.

# square1 = Square(25)
# print(square1.__class__.__name__)

# print('---------')
# print(__name__)


# Given the following Animal class, create two more classes, Cat and Dog, that inherit from it:

class Animal:
    def __init__(self, name, age, legs, species, status):
        self.name = name
        self.age = age
        self.legs = legs
        self.species = species
        self.status = status

    def introduce(self):
        return (f"Hello, my name is {self.name} and I am "
                f"{self.age} years old and {self.status}.")


# The Cat initializer should accept 3 parameters: name, age, and status. Cats should always have a leg count of 4 and a species of "cat". The introduce method for the Cat class should return a string identical to the base class with an added Meow meow! at the end. For example:
class Cat(Animal):
    def __init__(self, name, age, status):
        legs = 4
        species = "cat"
        super().__init__(name, age, legs, species, status)

    def introduce(self):
        base_introduction = super().introduce()
        return f"{base_introduction} Meow meow!"


cat = Cat("Pepe", 4, "happy")
expected = ("Hello, my name is Pepe and I am 4 years old "
            "and happy. Meow meow!")

print(cat.introduce())
print(cat.introduce() == expected)  # True


# The Dog initializer should accept 4 parameters: name, age, status, and owner. Dogs should always have a leg count of 4 and a species of "dog". In addition to the methods inherited from Animal, the Dog class should have a greet_owner method that returns a greeting to its owner followed by Woof! Woof!. The introduce method for the Dog class should return a string identical to the base class with an added Woof! Woof! at the end.
class Dog(Animal):
    def __init__(self, name, age, status, owner):
        self._owner = owner
        legs = 4
        species = "dog"
        super().__init__(name, age, legs, species, status)

    @property
    def owner(self):
        return self._owner

    def introduce(self):
        base_greeting = super().introduce()
        return f"{base_greeting} Woof! Woof!"

    def greet_owner(self):
        return f"Hi {self.owner}! Woof! Woof!"


dog = Dog("Bobo", 9, "hungry", "Daddy")
expected = ("Hello, my name is Bobo and I am 9 years old "
            "and hungry. Woof! Woof!")
print(dog.introduce() == expected)  # True
print(dog.greet_owner() == "Hi Daddy! Woof! Woof!")  # True