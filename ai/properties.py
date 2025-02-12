class Shape:
    def __init__(self, color, area, perimeter):
        self._color = color  # This can be used by all shapes
        self._area = 0       # Default area, specific to more complex shapes
        self._perimeter = 0   # Default perimeter, also for complex shapes

    @property
    def area(self):
        return self._area

    @property
    def perimeter(self):
        return self._perimeter

    @property
    def color(self):
        return self._color

    def describe(self):
        return f"This shape is {self.color} with area {self.area} and perimeter {self.perimeter}."


shape1 = Shape("blue", 55, 100)
print(shape1.area)
print(shape1.describe())

# properties allow us access and modify the private attributes
# in the case above we can only access the area and color properties, not change them
# if we want to change the area or color, we would need to use setter methods, like this:

class Shape:
    def __init__(self, color, area, perimeter):
        self._color = color  # This can be used by all shapes
        self._area = 0       # Default area, specific to more complex shapes
        self._perimeter = 0   # Default perimeter, also for complex shapes

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, new_area):
        self._area = new_area

    @property
    def perimeter(self):
        return self._perimeter

    @perimeter.setter
    def perimeter(self, new_perimeter):
        self._perimeter = new_perimeter

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, new_color):
        self._color = new_color

    def describe(self):
        return f"This shape is {self.color} with area {self.area} and perimeter {self.perimeter}."


shape1 = Shape("blue", 55, 100)
print(shape1.area)
print(shape1.describe())

print('---------')

shape1.area = 60 #  Now I am able to change the area and other attributes
shape1.perimeter = 120
shape1.color = "RED"
print(shape1.describe())


