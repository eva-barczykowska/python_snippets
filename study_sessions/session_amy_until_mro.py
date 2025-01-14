# Update the following code so that it prints I'm Sophie! when it invokes print(kitty).

# class Cat:
#     def __init__(self, name):
#         self._name = name

#     @property
#     def name(self):
#         return self._name

#     def __repr__(self):
#         return f"I'm {self.name}!"

# # Comments show expected output
# kitty = Cat('Sophie')
# print(kitty)        # I'm Sophie!

# Inherited Year
# Using the following code, create two classes -- Truck and Car -- that both inherit from Vehicle.

# class Vehicle:
#     def __init__(self, year):
#         self._year = year

#     @property
#     def year(self):
#         return self._year

# class Truck(Vehicle):
#     pass


# class Car(Vehicle):
#     pass


# # Comments show expected output
# truck1 = Truck(1994)
# print(truck1.year)            # 1994

# car1 = Car(2006)
# print(car1.year)              # 2006

# start the engine
# Change the following code so that creating a new Truck automatically calls start_engine.

# class Vehicle:
#     def __init__(self, year):
#         self._year = year

#     @property
#     def year(self):
#         return self._year

# class Truck(Vehicle):
#     def __init__(self, year):
#         super().__init__(year)
#         self.start_engine()


#     def start_engine(self):
#         print('Ready to go!')

# # Comments show expected output
# truck1 = Truck(1994)          # Ready to go!
# print(truck1.year)            # 1994

# Using the following code, modify Truck to accept a second argument when instantiating a new Truck object.
# Name the parameter bed_type. Ensure that the Car constructor continues to accept only one argument.

# class Vehicle:
#     def __init__(self, year):
#         self._year = year

#     @property
#     def year(self):
#         return self._year

# class Truck(Vehicle):
#     def __init__(self, year, bed_type):
#         super().__init__(year)
#         self.bed_type = bed_type

# class Car(Vehicle):
#     pass

# # Comments show expected output
# truck1 = Truck(1994, 'Short')
# print(truck1.year)            # 1994
# print(truck1.bed_type)        # Short

# car1 = Car(2006)
# print(car1.year)              # 2006
# print(car1.bed_type)
# # AttributeError: 'Car' object has no attribute 'bed_type'

# class gfg:

#     # constructor
#     def __init__(self, value):
#         self._value = value


#     # getting the values
#     def getter(self):
#         print('Getting value')
#         return self._value

#     # setting the values
#     def setter(self, value):
#         print('Setting value to ' + value)
#         self._value = value

#     # deleting the values
#     def deleter(self):
#         print('Deleting value')
#         del self._value

#     # create a properties
#     value = property(getter, setter, deleter, )

# # create a gfg class object
# x = gfg('Happy Coding!')
# print(x.value)

# x.value = 'Hey Coder!'

# # deleting the value
# del x.value

# Using the following code, create a mix-in named WalkingMixin that contains a method named walk.
# This method should print Let's go for a walk! when invoked. Include WalkingMixin in Cat.

# class WalkingMixin():
#     def walk(self):
#         print("Let's go for walk!")

# class Cat(WalkingMixin):
#     def __init__(self, name):
#         self._name = name

#     @property
#     def name(self):
#         return self._name

#     def greet(self):
#         print(f"Hello! My name is {self.name}!")

# # Comments show expected output
# kitty = Cat('Sophie')
# kitty.greet()       # Hello! My name is Sophie!
# kitty.walk()        # Let's go for a walk!

# Using the following code, create a Towable mix-in that contains a method named tow.
# This method should print I can tow a trailer! when invoked. The mix-in should be included in the Truck class.
# class Towable():
#     def tow(self):
#         print("I can tow a trailer!")

# class Truck(Towable):
#     pass

# class Car:
#     pass

# # Comments show expected output
# truck1 = Truck()
# truck1.tow()        # I can tow a trailer!

# car1 = Car()
# car1.tow()
# # AttributeError: 'Car' object has no attribute 'tow'


# Given the following code, create a class named Vehicle that, upon instantiation, assigns the passed-in argument
# to self.year. Both Truck and Car should inherit from Vehicle.

# class Vehicle:
#     def __init__(self, year):
#         self.year = year

# class TowingMixin:
#     def tow(self):
#         return 'I can tow a trailer!'

# class Truck(TowingMixin, Vehicle):
#     pass

# class Car(Vehicle):
#     pass

# # Comments show expected output
# truck1 = Truck(1994)
# print(truck1.year)            # 1994
# print(truck1.tow())           # I can tow a trailer!

# car1 = Car(2006)
# print(car1.year)              # 2006

# Using the code below, determine the method resolution order (MRO) used when accessing the cat1.color property.
# Only list the classes that are checked by Python when searching for the color attribute. Do not use the mro method.


# class Animal:
#     def __init__(self, color):
#         self._color = color

#     @property
#     def color(self):
#         return self._color

# class Cat(Animal):
#     pass

# class Bird(Animal):
#     pass

# cat1 = Cat('Black')
# print(cat1.color)

# # Cat -> Animal
# print(Cat.mro())

# print(Cat.__mro__)
# # print(cat1.color.__mro__)


# Using the code below, determine the method resolution order (MRO) when accessing cat1.color. Only list the classes
# and mix-ins Python will check when searching for the color method. Do not use the mro method.

class Animal:
    pass


class Cat(Animal):
    pass


class Bird(Animal):
    pass


cat1 = Cat()
# cat1.color
print(Cat.mro())
