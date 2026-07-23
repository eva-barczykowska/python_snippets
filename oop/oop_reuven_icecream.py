class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor

    def __repr__(self):
        return f"Scoop of {self.flavor}"

class Bowl:
    def __init__(self):
        self.scoops = []

    # def __repr__(self):
    #     output = ''
    #     if self.scoops:
    #         for index, one_scoop in enumerate(self.scoops, start=1):
    #             output += f"\n{index}.{one_scoop}"
    #         return output
    #     else:
    #         return f"Bowl: Empty"

    # def __repr__(self):
    #     output = ''
    #     for index, one_scoop in enumerate(self.scoops):
    #         output += f"{index + 1}. {one_scoop}\n"
    #     return output

    def __repr__(self):
        return '\n'.join([f"{index+1}. {one_scoop}" for index, one_scoop in enumerate(self.scoops)])


    def add_scoop(self, *args):
        for one_scoop in args:
            self.scoops.append(one_scoop)

    def flavors(self):
         return [one_scoop.flavor for one_scoop in self.scoops]
    def has_flavor(self, flavor):
        return flavor in self.flavors()

s1 = Scoop("chocolate")
s2 = Scoop("vanilla")
s3 = Scoop("strawberry")

b = Bowl()
print(b)
b.add_scoop(s1, s2, s3)
print(b)
# print(b.flavors())
# print(b.add_scoop(Scoop("mango"))) #returns None but mutates the bowl's scoops list
# print(b.flavors())



# print(b.has_flavor("vanilla")) # returns True
# print(b.has_flavor("peanut butter")) # returns False
#
# madagascar_vanilla = Scoop("madagascar vanilla")
# print(madagascar_vanilla)
# print(b)
#
# print("Other ways tp get the object class name, in addition to __str__ or __repr__:")
# print(s1.__class__.__name__) #<__main__.Bowl object at 0x102e62580>
# print(type(s1).__name__) # Scoop