
# Using the code below, determine the method resolution order used when invoking bird1.color. Only list the classes or mix-ins that Python will check when searching for the color method. Do not use the mro method.

# class FlyingMixin:
#     def fly(self):
#         return "I'm flying!"

# class Animal:
#     def __init__(self, color):
#         self._color = color

#     # @property
#     def color(self):
#         return self._color

# class Cat(Animal):
#     pass

# class Bird(FlyingMixin, Animal):
#     pass

# bird1 = Bird('Red')
# print(bird1.color())
# bird1
# Bird
# FlyingMixin
# Animal

# Behold this incomplete class for constructing boxed banners:

class Banner:
    def __init__(self, message):
        self._message = message
        self._length = len(message)

    def __str__(self):
        return "\n".join([self._horizontal_line(),
                          self._empty_line(),
                          self._message_line(),
                          self._empty_line(),
                          self._horizontal_line()])

    def _empty_line(self):
        return f"| {' '* self._length} |"

    def _horizontal_line(self):
        return f"+-{self._length * '-'}-+"

    def _message_line(self):
        return f"| {self._message} |"

# Complete this class so that the test cases shown below work as intended. You are free to add any methods or instance variables you need. However, methods prefixed with an underscore are intended for internal use and should not be called externally.

# You may assume that the input will always fit in your terminal window.


# Comments show expected output

banner = Banner('To boldly go where no one has gone before.')
print(banner)
# +--------------------------------------------+
# |                                            |
# | To boldly go where no one has gone before. |
# |                                            |
# +--------------------------------------------+

banner = Banner('')
print(banner)
# +--+
# |  |
# |  |
# |  |
# +--+