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


    # def add_scoop(self, *args):
    #     if len(self.scoops) >= self.MAX_SCOOPS: # raise an exception if the bowl is full
    #         raise ValueError(f"Bowl can't hold more than {self.MAX_SCOOPS} scoops")
    #     for one_scoop in args:
    #         self.scoops.append(one_scoop)


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

s1 = Scoop("chocolate")
s2 = Scoop("vanilla")
s3 = Scoop("strawberry")

b = Bowl()
print(b)
b.add_scoop(s1, s2, s3)
b.add_scoop(s1, s2, s3)
print(b)
