class Shape:
    def __init__(self, color, area=None, perimeter=None):
        self.color = color               # Attribute that all shapes might need
        self.area = area                 # Can be set for shapes that have an area
        self.perimeter = perimeter       # Can be set for shapes that have a perimeter

    def describe(self):
        description = f"This shape is {self.color}."
        if self.area is not None:
            description += f" Its area is {self.area}."
        if self.perimeter is not None:
            description += f" Its perimeter is {self.perimeter}."
        return description


class Point(Shape):
    def __init__(self, x, y):
        super().__init__(color="black")  # Points can have a color
        self.x = x                       # Attributes specific to Point
        self.y = y                       # Attributes specific to Point
        # Not initializing area or perimeter specifically as they do not apply to a point

    def describe(self):
        return f"This point is located at ({self.x}, {self.y})."


# Example usage
point = Point(3, 4)
print(point.describe())  # Output: This point is located at (3, 4).

# this code above could be considered as better than this:
class Shape:
    def __init__(self, color, area=0, perimeter=0):
        self.color = color  # This can be used by all shapes
        self.area = area    # Default area, can be set by specific shapes
        self.perimeter = perimeter  # Default perimeter, can be set by specific shapes

    def describe(self):
        return f"This shape is {self.color} with area {self.area} and perimeter {self.perimeter}."


class Point(Shape):
    def __init__(self, x, y):
        super().__init__(color="black")  # Points can have a color
        self.x = x  # x-coordinate specific to a Point
        self.y = y  # y-coordinate specific to a Point
        # No need to initialize area or perimeter since they are not relevant for a point

    def describe(self):
        return f"This point is located at ({self.x}, {self.y})."


# Example usage
point = Point(3, 4)
print(point.describe())  # Output: This point is located at (3, 4).

# the difference is that area and perimeter are not set in the Point class and therefore default to 0,
# but they are not needed so maybe it's better to give them a default value of None in the Shape class.
