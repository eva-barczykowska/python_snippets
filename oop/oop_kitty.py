class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def __repr__(self):
        return f'Pet({self.name}, {self.species}, {self.age})'

    def make_noise(self, noise):
        return f"{self.name} says {noise}!"

    def confess_secret(self):
        return f"I am your favorite {self.species}!"


class Pet(Animal):
    def __init__(self, name, species, age, is_house_trained): # all the attributes including the new attribute is_house_trained
        super().__init__(name, species, age) # we have to say which attributes we want to inherit from the parent class
        self.is_house_trained = is_house_trained # attribute added to Pet class, when retrieving we don't need ()


kitty = Pet('Kitty', 'Cat', 3, True)
print(kitty.make_noise('Meow'))
print(kitty.is_house_trained)
print(kitty.make_noise('Purr')) # method, we need () to call and pass arguments

# what is there was a method without arguments? Do we still need parentheses?
# yes!

print(kitty.confess_secret())

# if we don't, we get <bound method Animal.confess_secret of Pet(Kitty, Cat, 3)>
print(vars(kitty)) # vars() prints all the attributes of an object
print(dir(kitty)) # dir() lists all attributes of an object, including class attributes and methods