# inherit all without change
class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def __repr__(self):
        return f"Animal of species {self.species}"



    def eat(self, food):
        print(f"{self.species} easts {food}")


class Dog(Animal):
    def __init__(self, name, age, species):
        # super().__init__(name, age, species)
        pass

chameleon = Animal("Rupert", 5,"Chameleon")
print(chameleon)
print(chameleon.name)
print(chameleon.age)

dog = Dog("Cash", 3, "Dog")
print(dog)
print(dog.name)

# Traceback (most recent call last):
#   File "/Users/e-vah/PycharmProjects/python_snippets/oop_kitty_puppy.py", line 28, in <module>
#     print(dog)
#   File "/Users/e-vah/PycharmProjects/python_snippets/oop_kitty_puppy.py", line 9, in __repr__
#     return f"Animal of species {self.species}"
# AttributeError: 'Dog' object has no attribute 'species'
# Animal of species Chameleon