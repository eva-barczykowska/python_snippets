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
    def __init__(self, name, age, species): # The parent constructor is the one that actually sets attributes like `self.name`, `self.age`, and `self.species`
        # super().__init__(name, age, species)
        pass # coz super().__init__()` is not called in this case and we have pass, this method does nothing

chameleon = Animal("Rupert", 5,"Chameleon")
print(chameleon)
print(chameleon.name)
print(chameleon.age)

dog = Dog("Cash", 3, "Dog")
print(dog) # at this point __repr__ method is called but it cannot find species and an error is thrown
print(dog.name)

# ir we comment line 19, # super().__init__(name, age, species), the repr method in the parent class cannot find species and an error is thrown:

# Traceback (most recent call last):
#   File "/Users/e-vah/PycharmProjects/python_snippets/oop_kitty_puppy.py", line 28, in <module>
#     print(dog)
#   File "/Users/e-vah/PycharmProjects/python_snippets/oop_kitty_puppy.py", line 9, in __repr__
#     return f"Animal of species {self.species}"
# AttributeError: 'Dog' object has no attribute 'species'
# Animal of species Chameleon

# The parent constructor is the one that actually sets attributes like `self.name`, `self.age`, and `self.species`.
# So when creating a `Dog`, none of these attributes get assigned to the instance.