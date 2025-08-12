class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor

    def __repr__(self):
        return f"Scoop of {self.flavor}"

class Bowl:
    MAX_SCOOPS = 3 # implementing a constant for maximum scoops

    def __init__(self):
        self.scoops = []

    def __repr__(self):
        return '\n'.join([f"{index+1}. {one_scoop}" for index, one_scoop in enumerate(self.scoops)])


    def add_scoop(self, *args):
        for one_scoop in args:
            if len(self.scoops) >= self.MAX_SCOOPS:
                break
            else:
                self.scoops.append(one_scoop)

    def flavors(self):
         return [one_scoop.flavor for one_scoop in self.scoops]

    def has_flavor(self, flavor):
        return flavor in self.flavors()

class BigBowl(Bowl):
    MAX_SCOOPS = 5 # implementing a constant for maximum scoops
# __init__ is the same so we don't need to write it again
# we write in super().__init__() the attribute what we want to inherit from the parent class
# see oop_person_employee.py file for example of how to inherit from a parent class

s1 = Scoop("chocolate")
s2 = Scoop("vanilla")
s3 = Scoop("strawberry")

b = Bowl()
print(b)
b.add_scoop(s1, s2, s3)
b.add_scoop(s1, s2, s3)
print(b)

print('Now BigBowl:')
bb = BigBowl()
print(bb)
bb.add_scoop(s1, s2, s3)
bb.add_scoop(s1, s2, s3)
print(bb)