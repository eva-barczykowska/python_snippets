# The circle should have a radius, a diameter, and an area.
# It should also have a nice string representation.
class Circle:
    def __init__(self, radius=1):
        self.radius = radius
        self.diameter = round(self.radius * 2, 2)  # round to 2 decimal places
        self.area = round(3.14 * self.radius ** 2, 2)

    def __str__(self):
        return self.__class__.__name__ + f"({self.radius})"



c = Circle(5)
print(c)
print(c.radius)
print(c.diameter)
print(c.area)

# '{:,.2f}'.format(1234.56)


