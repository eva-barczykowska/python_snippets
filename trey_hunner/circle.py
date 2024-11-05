# Make a class that represents a circle.
# The circle should have a radius, a diameter, and an area. It should also have a nice string representation.
# https://www.pythonmorsels.com/exercises/ac9f7d60d95d493f9e354f18a3ea9d82/submit/2/
import math

class Circle:
    def __init__(self, radius=1):
        self.radius = radius

    @property
    def diameter(self):
        return 2 * self.radius

    @property
    def area(self):
        return math.pi * (self.radius ** 2)

    def __repr__(self):
        return f"Circle({self.radius})"


c = Circle(4)
print(c)  # Output: Circle(5)
print(c.radius)  # Output: 5
print(c.diameter)  # Output: 10
print(c.area)  # Output: 78.53981633974483
print()
print("Changing radius to 10... New area should be: 314.1592653589793 and diameter should be: 20")
c.radius = 10
print(c.area)  # Output: 314.1592653589793
print(c.diameter)  # Output: 20

