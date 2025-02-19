# class Pet:
#     def __init__(self, species, name):
#         self._species = species
#         self._name = name
#
#     @property
#     def species(self):
#         return self._species
#
#     @property
#     def name(self):
#         return self._name
#
#
# class Owner:
#     def __init__(self, name):
#         self._name = name
#         self._adoptions = []  # define an empty list here, no need to put it as an argument
#
#     @property
#     def name(self):
#         return self._name
#
#     @property
#     def adoptions(self):
#         return self._adoptions
#
#     def adopt_pet(self, pet):
#         self._adoptions.append(pet)
#
#     def number_of_pets(self):
#         return len(self._adoptions)
#
#
# class Shelter:
#     def __init__(self):
#         self._adoptions = {}
#
#     @property
#     def adoptions(self):
#         return self._adoptions
#
#     def adopt(self, owner, pet):
#         if owner.name not in self.adoptions:
#             self._adoptions[owner.name] = {}
#             self._adoptions[owner.name][pet.name] = pet.species
#         else:
#             self.adoptions[owner.name][pet.name] = pet.species
#
#         owner.adopt_pet(pet)  # to update owner as well
#
#     def print_adoptions(self):
#         print(self.adoptions) # {'P Hanson': {'Cocoa': 'cat', 'Cheddar': 'cat', 'Darwin': 'bearded dragon'}, 'B Holmes': {'Kennedy': 'dog', 'Sweetie Pie': 'parakeet', 'Molly': 'dog', 'Chester': 'fish'}}
#         for owner_name, pets in self.adoptions.items():
#             print(f"{owner_name} has adopted the following pets:")
#             for pet_name, pet_details in pets.items():
#                 print(f"A {pet_details} named {pet_name}")
#             print()  # Add a blank line between owners for readability
#
#
# # P Hanson has adopted the following pets:
# # a cat named Cocoa
# # a cat named Cheddar
# # a bearded dragon named Darwin
#
# cocoa = Pet('cat', 'Cocoa')
# cheddar = Pet('cat', 'Cheddar')
# darwin = Pet('bearded dragon', 'Darwin')
# kennedy = Pet('dog', 'Kennedy')
# sweetie = Pet('parakeet', 'Sweetie Pie')
# molly = Pet('dog', 'Molly')
# chester = Pet('fish', 'Chester')
#
# phanson = Owner('P Hanson')
# bholmes = Owner('B Holmes')
#
# shelter = Shelter()
#
# shelter.adopt(phanson, cocoa)
# shelter.adopt(phanson, cheddar)
# shelter.adopt(phanson, darwin)
# shelter.adopt(bholmes, kennedy)
# shelter.adopt(bholmes, sweetie)
# shelter.adopt(bholmes, molly)
# shelter.adopt(bholmes, chester)
#
# shelter.print_adoptions()
# # P Hanson has adopted the following pets:
# # a cat named Cocoa
# # a cat named Cheddar
# # a bearded dragon named Darwin
#
# # B Holmes has adopted the following pets:
# # a dog named Molly
# # a parakeet named Sweetie Pie
# # a dog named Kennedy
# # a fish named Chester
#
# print()
# print(f"{phanson.name} has {phanson.number_of_pets()} "
#       "adopted pets.")
# print(f"{bholmes.name} has {bholmes.number_of_pets()} "
#       "adopted pets.")
# # P Hanson has 3 adopted pets.
# # B Holmes has 4 adopted pets.
#
# print('--------------------------------------------------------------------------------------------------------------')
# # Amy's solution
# # Consider the following code:
#
# class Pet():
#     def __init__(self, species, name):
#         self._species = species
#         self._name = name
#
#     @property
#     def species(self):
#         return self._species
#
#     @property
#     def name(self):
#         return self._name
#
# class Owner():
#     def __init__(self, name):
#         self._name = name
#         self._pets = []
#
#     @property
#     def name(self):
#         return self._name
#
#     @property
#     def pets(self):
#         return self._pets
#
#     def number_of_pets(self):
#         return len(self._pets)
#
# class Shelter():
#     def __init__(self):
#         self._adoptions = {}
#
#     @property
#     def adoptions(self):
#         return self._adoptions
#
#     def adopt(self, owner, pet):
#         if type(self._adoptions.get(owner.name)) == list:
#             self._adoptions[owner.name].append((pet.species, pet.name))
#             owner.pets.append(pet)
#         else:
#             self._adoptions[owner.name] = [(pet.species, pet.name)]
#             owner.pets.append(pet)
#
#     def print_adoptions(self):
#         # print(self.adoptions) # {'P Hanson': [('cat', 'Cocoa'), ('cat', 'Cheddar'), ('bearded dragon', 'Darwin')], 'B Holmes': [('dog', 'Kennedy'), ('parakeet', 'Sweetie Pie'), ('dog', 'Molly'), ('fish', 'Chester')]}
#         for (owner, pets) in self.adoptions.items():
#             print(f"{owner} has adopted the following pets:")
#             for pet in pets:
#                 print(f"a {pet[0]} named {pet[1]}")
#
# cocoa   = Pet('cat', 'Cocoa')
#
# cheddar = Pet('cat', 'Cheddar')
#
# darwin  = Pet('bearded dragon', 'Darwin')
#
# kennedy = Pet('dog', 'Kennedy')
#
# sweetie = Pet('parakeet', 'Sweetie Pie')
#
# molly   = Pet('dog', 'Molly')
#
# chester = Pet('fish', 'Chester')
#
# phanson = Owner('P Hanson')
#
# bholmes = Owner('B Holmes')
#
# shelter = Shelter()
#
# shelter.adopt(phanson, cocoa)
#
# shelter.adopt(phanson, cheddar)
#
# shelter.adopt(phanson, darwin)
#
# shelter.adopt(bholmes, kennedy)
#
# shelter.adopt(bholmes, sweetie)
#
# shelter.adopt(bholmes, molly)
#
# shelter.adopt(bholmes, chester)
#
# shelter.print_adoptions()
#
# print(f"{phanson.name} has {phanson.number_of_pets()} "
#
# "adopted pets.")
#
# print(f"{bholmes.name} has {bholmes.number_of_pets()} "
#
# "adopted pets.")
#
# #Write the classes and methods that will be necessary to make this code run, and log the following output:
#
# # P Hanson has adopted the following pets:
#
# # a cat named Cocoa
#
# # a cat named Cheddar
#
# # a bearded dragon named Darwin
#
# # B Holmes has adopted the following pets:
#
# # a dog named Molly
#
# # a parakeet named Sweetie Pie
#
# # a dog named Kennedy
#
# # a fish named Chester
#
# # P Hanson has 3 adopted pets.
#
# # B Holmes has 4 adopted pets.
#
# print('--------------------------------------------------------------------------------------------------------------')
# # LS solution
class Pet:
    def __init__(self, animal, name):
        self.animal = animal
        self.name = name

    def info(self):
        return f'a {self.animal} named {self.name}'

class Owner:
    def __init__(self, name):
        self.name = name
        self.pets = []

    def add_pet(self, pet):
        self.pets.append(pet)

    def number_of_pets(self):
        return len(self.pets)

    def print_pets(self):
        for pet in self.pets:
            print(pet.info())

class Shelter:
    def __init__(self):
        self.owners = {}

    def adopt(self, owner, pet):
        owner.add_pet(pet)
        if owner.name not in self.owners:
            self.owners[owner.name] = owner

    def print_adoptions(self):
        for name, owner in self.owners.items():
            print(f'{name} has adopted the following pets:')
            owner.print_pets()
            print("")


cocoa   = Pet('cat', 'Cocoa')
cheddar = Pet('cat', 'Cheddar')
darwin  = Pet('bearded dragon', 'Darwin')
kennedy = Pet('dog', 'Kennedy')
sweetie = Pet('parakeet', 'Sweetie Pie')
molly   = Pet('dog', 'Molly')
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

print(f"{phanson.name} has {phanson.number_of_pets()} "

"adopted pets.")

print(f"{bholmes.name} has {bholmes.number_of_pets()} "

"adopted pets.")

#Write the classes and methods that will be necessary to make this code run, and log the following output:

# P Hanson has adopted the following pets:

# a cat named Cocoa

# a cat named Cheddar

# a bearded dragon named Darwin

# B Holmes has adopted the following pets:

# a dog named Molly

# a parakeet named Sweetie Pie

# a dog named Kennedy

# a fish named Chester

# P Hanson has 3 adopted pets.

# B Holmes has 4 adopted pets.