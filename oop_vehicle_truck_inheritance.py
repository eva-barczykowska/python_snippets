class Vehicle:
    def __init__(self, model, year, engine):
        self.year = year
        self.model = model
        self.engine = engine # I gave this attribute to Vehicle,  I will use it on line 11

    def __repr__(self): # but all methods are also attributes of the class
        return f'Vehicle of type {self.__class__.__name__}, {self.model}, {self.year}'

    def start_engine(self):
         return f'{self.engine} is started! Ready to go! -> ->' # using the attribute the object (vehicle or truck) have

class Truck(Vehicle):
    pass


tractor = Vehicle("Ursus", 1977, "tractor_engine")
print(tractor)
print(tractor.start_engine()) # self gets passed automatically into the method

truck = Truck("Ford", 2010, "truck_engine")
print(truck)
print(truck.start_engine())
