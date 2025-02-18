class Pet:
    def __init__(self, species, name):
        self._species = species
        self._name = name

    @property
    def species(self):
        return self._species

    @property
    def name(self):
        return self._name


class Owner:
    def __init__(self, name):
        self._name = name
        self._adoptions = []  # define an empty list here, no need to put it as an argument

    @property
    def name(self):
        return self._name

    @property
    def adoptions(self):
        return self._adoptions

    def adopt_pet(self, pet):
        self._adoptions.append(pet)

    def number_of_pets(self):
        return len(self._adoptions)


class Shelter:
    def __init__(self):
        self._adoptions = {}

    @property
    def adoptions(self):
        return self._adoptions

    def adopt(self, owner, pet):
        if owner.name not in self.adoptions:
            self._adoptions[owner.name] = {}
            self._adoptions[owner.name][pet.name] = pet.species
        else:
            self.adoptions[owner.name][pet.name] = pet.species

        owner.adopt_pet(pet)  # to update owner as well

    def print_adoptions(self):
        for owner_name, pets in self.adoptions.items():
            print(f"{owner_name} has adopted the following pets:")
            for pet_name, pet_details in pets.items():
                print(f"A {pet_details} named {pet_name}")
            print()  # Add a blank line between owners for readability


# P Hanson has adopted the following pets:
# a cat named Cocoa
# a cat named Cheddar
# a bearded dragon named Darwin

cocoa = Pet('cat', 'Cocoa')
cheddar = Pet('cat', 'Cheddar')
darwin = Pet('bearded dragon', 'Darwin')
kennedy = Pet('dog', 'Kennedy')
sweetie = Pet('parakeet', 'Sweetie Pie')
molly = Pet('dog', 'Molly')
chester = Pet('fish', 'Chester')

phanson = Owner('P Hanson')
bholmes = Owner('B Holmes')

shelter = Shelter()

shelter.adopt(phanson, cocoa)
shelter.adopt(phanson, cheddar)
shelter.adopt(phanson, darwin)
shelter.adopt(bholmes, kennedy)
shelter.adopt(bholmes, sweetie)
shelter.adopt(bholmes, molly)
shelter.adopt(bholmes, chester)

shelter.print_adoptions()
# P Hanson has adopted the following pets:
# a cat named Cocoa
# a cat named Cheddar
# a bearded dragon named Darwin

# B Holmes has adopted the following pets:
# a dog named Molly
# a parakeet named Sweetie Pie
# a dog named Kennedy
# a fish named Chester

print()
print(f"{phanson.name} has {phanson.number_of_pets()} "
      "adopted pets.")
print(f"{bholmes.name} has {bholmes.number_of_pets()} "
      "adopted pets.")
# P Hanson has 3 adopted pets.
# B Holmes has 4 adopted pets.