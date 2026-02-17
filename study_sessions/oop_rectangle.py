# Create a Rectangle class whose initializer takes two arguments that represent the rectangle's width and height,
# respectively. Use the following code to test your solution:
# rect = Rectangle(4, 5)
# print(rect.width == 4)        # True
# print(rect.height == 5)       # True
# print(rect.area == 20)        # True

#solution
class Rectangle():
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height}, area={self.area})"

rect = Rectangle(4, 5)
print(rect)
print(rect.width == 4)        # True
print(rect.height == 5)       # True
print(rect.area == 20)        # True
# A rectangle's area is given by its width times its height.

# second time round
# Rectangle
# Create a Rectangle class whose initializer takes two arguments that represent the rectangle's width and height, respectively. Use the following code to test your solution:

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#    # @property
#     def area(self):
#         return self.width * self.height

# rect = Rectangle(4, 5)

# print(rect.width == 4)        # True
# print(rect.height == 5)       # True
# print(rect.area == 20)        # True


# A rectangle's area is given by its width times its height.
# methods are also attributes/properties

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property #if this is not there, the Rectangle class will not have area property/attribute, only a method
    def area(self):
         return self.width * self.height

class Square(Rectangle):
     def __init__(self, side_length):
         super().__init__(side_length, side_length)


square = Square(5)
print(square.area == 25)      # True

# Rectangles and Squares
# Given the class from the previous problem:

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def area(self):
        return self._width * self._height

# Write a class called Square that inherits from the Rectangle class. The Square class is used like this:
square = Square(5)
print(square.area == 25)      # True