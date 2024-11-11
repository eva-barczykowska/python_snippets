# Make a class that represents a circle.
# The circle should have a radius, a diameter, and an area. It should also have a nice string representation.
# https://www.pythonmorsels.com/exercises/ac9f7d60d95d493f9e354f18a3ea9d82/submit/2/

# look at circle_class_and_test directory for to see how it was at the beginning of the exercise
import math


class Circle:
    """Circle with radius, area, and diameter."""

    def __init__(self, radius=1):
        self._radius = radius

    def __repr__(self):
        return f"Circle({self.radius})"

    @property
    def area(self):
        return math.pi * (self._radius ** 2)

    @property  # properties are read-only by default so we cant assign a new value to diameter or area
    def diameter(self):
        return 2 * self._radius

    @diameter.setter
    def diameter(self, new_diameter):
        if new_diameter < 0:
            raise ValueError("Diameter cannot be negative")
        self._radius = new_diameter / 2  # diameter is half of radius, so we update radius accordingly

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = radius


# c = Circle(4)
# print("Circle area:")
# print(c.area)
# print(c)  # Output: Circle(5)
# print(c.radius)  # Output: 5
# print(c.diameter)  # Output: 10
# print(c.area)  # Output: 78.53981633974483
# print()
# print("Changing radius to 10... New area should be: 314.1592653589793 and diameter should be: 20")
# c.radius = 10
# print(c.area)  # Output: 314.1592653589793
# print(c.diameter)  # Output: 20
#
# # c.area = 200  # AttributeError: property 'area' of 'Circle' object has no setter
# print(c.area)

c = Circle(1)
c.diameter = 4
print(c.diameter)  # Output: 4.0
print(c.radius)  # Output: 2.0
# c.diameter = -4  # ValueError: Diameter cannot be negative
