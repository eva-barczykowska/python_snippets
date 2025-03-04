# class Vehicle:
#     def __init__(self, make, model, wheels=4):
#         self.make = make
#         self.model = model
#         self.wheels = wheels

#     def info(self):
#         return f"{self.make} {self.model}"

#     def get_wheels(self):
#         return self.wheels

# class Car(Vehicle):
#     def __init__(self, make, model):
#         super().__init__(make, model)

# class Motorcycle(Vehicle):
#     def __init__(self, make, model):
#        super().__init__(make, model, wheels=2)

# class Truck(Vehicle):
#     def __init__(self, make, model, payload):
#         super().__init__(make, model, wheels=6)
#         self.payload = payload

# car = Car('Mazda', 'Miata')
# truck = Truck('Toyota', 'Tacoma', '10 tons')
# moto = Motorcycle('Harley', 'Ewa')
# vehicle = Vehicle('Test', 'test')

# print(car.info())
# print(truck.info())
# print(moto.info())
# print(car.get_wheels())
# print(truck.get_wheels())
# print(moto.get_wheels())

# Refactor these classes so they all use a common superclass, and inherit behavior as needed.


# You have these classes:

# class Person():
#     def __init__(self, name):
#         self.name = name

#     def gait(self):
#         return "strolls"

#     def walk(self):
#         return f"{self} {self.gait()} forward"

# class Cat():
#     def __init__(self, name):
#         self.name = name

#     def gait(self):
#         return "saunters"
#     def walk(self):
#         return f"{self} {self.gait()} forward"

# class Cheetah():
#     def __init__(self, name):
#         self.name = name

#     def gait(self):
#         return "runs"
#     def walk(self):
#         return f"{self} {self.gait()} forward"


# # Modify the code so that it works
# mike = Person("Mike")
# print(mike.walk())  # Expected: "Mike strolls forward"

# kitty = Cat("Kitty")
# print(kitty.walk())  # Expected: "Kitty saunters forward"

# flash = Cheetah("Flash")
# print(flash.walk())  # Expected: "Flash runs forward"

# puts("----------")
# # You have these classes:
# class Person:
#     def __init__(self, name):
#         self.name = name

#     def gait(self):
#         return "strolls"

#     def walk(self):
#         return f"{self.name} {self.gait()} forward"

# class Cat(Person):
#     def __init__(self, name):
#         self.name = name

#     def gait(self):
#         return "saunters"

#     # def walk(self):
#     #     return f"{self.name} {self.gait()} forward"

# class Cheetah(Person):
#     def __init__(self, name):
#         self.name = name

#     def gait(self):
#         return "runs"

#     # def walk(self):
#     #     return f"{self.name} {self.gait()} forward"

# # Modify the code so that it works
# mike = Person("Mike")
# print(mike.walk())  # Expected: "Mike strolls forward"

# kitty = Cat("Kitty")
# print(kitty.walk())  # Expected: "Kitty saunters forward"

# flash = Cheetah("Flash")
# print(flash.walk())  # Expected: "Flash runs forward"

# Amy
# You have these classes:
# class Walkable:
#     def walk(self):
#         return f"{self.name} {self.gait()} forward"

# class Person(Walkable):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def gait(self):
#         return "strolls"

# class Cat(Walkable):
#     def __init__(self, name):
#         self.name = name

#     def gait(self):
#         return "saunters"

# class Cheetah(Walkable):
#     def __init__(self, name):
#         self.name = name

#     def gait(self):
#         return "runs"


# # Modify the code so that it works
# mike = Person("Mike", 77)
# print(mike.walk())  # Expected: "Mike strolls forward"

# kitty = Cat("Kitty")
# print(kitty.walk())  # Expected: "Kitty saunters forward"

# flash = Cheetah("Flash")
# print(flash.walk())  # Expected: "Flash runs forward"

# Nobility
# Now that we have a WalkMixin mix-in, we are given a new challenge. Apparently some of our users are nobility, and the regular way of walking simply isn't good enough. Nobility struts.

# We need a new class Noble that shows the title and name when walk is called. We also require access to name and title; they are needed for other purposes that we aren't showing here.


class Walkable:
    def walk(self):
        if isinstance(self, Noble):
            return f"{self.title} {self.name} {self.gait()} forward"
        else:
            return f"{self.name} {self.gait()} forward"


class Person(Walkable):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def gait(self):
        return "strolls"


class Cat(Walkable):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "saunters"


class Cheetah(Walkable):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "runs"


class Noble(Walkable):
    def __init__(self, name, title):
        self.name = name
        self.title = title

    def gait(self):
        return "struts"

    # def walk(self):
    #     return f"{self.title} " + super().walk()


# Modify the code so that it works
mike = Person("Mike", 77)
print(mike.walk())  # Expected: "Mike strolls forward"

byron = Noble("Byron", "Lord")
print(byron.walk())  # "Lord Byron struts forward"
print(byron.name)  # "Byron"
print(byron.title)  # "Lord"

# The easiest way to accomplish this is to provide a method that returns both the title and name for Noble instances
# and just the name for non-Noble instances.
