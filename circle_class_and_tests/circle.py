# The circle should have a radius, a diameter, and an area.
# It should also have a nice string representation.
import math
class Circle:
    def __init__(self, radius=1):
        self.radius = radius
        self.diameter = self.radius * 2
        self.area = math.pi * self.radius ** 2

    def __repr__(self):
        return f"Circle({self.radius:.1f})"


c = Circle(5)
print("str representation:", c)
#
# print("radius", c.radius)
print("area", c.area)#
#
# print("diameter", c.diameter)
# print("area", c.area)

# '{:,.1f}'.format(1234.56)
