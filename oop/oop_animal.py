# inherit all without change
class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def __repr__(self): # to have a different representation of the object than <__main__.Animal object at 0x1033fffa0>
        return f"Animal of species {self.species}"


    def eat(self, food):
        print(f"{self.species} easts {food}")


class Dog(Animal):
    def __init__(self, name, age, species):
        super().__init__(name, age, species) # this would be a call to super to initialize the attributes from its __init__ method but it is never made

chameleon = Animal("Rupert", 5,"Chameleon")
print(chameleon)
print(chameleon.name)

dog = Dog("Cash", 3, "Dog")
print(dog)
print(dog.name)