class Box:
    def __init__(self, length,  width, height):
        self.length = length
        self.width = width
        self.height = height

    def get_volume(self):
        volume = self.length * self.width * self.height
        return volume

    def get_surface_area(self):
        surface_area = ((self.length * self.width) + (self.width * self.height) + (self.height * self.length))
        return surface_area

box1 = Box(5, 6, 4)

box2 = Box(1, 2, 4)

print(f"Amount of space in box1 is {box1.get_volume()}")
print(f"Amount of space in box1 is {box2.get_volume()}")

print(f"Surface area of box1 is {box1.get_surface_area()}")
print(f"Surface area of box2 is {box2
      .get_surface_area()}")