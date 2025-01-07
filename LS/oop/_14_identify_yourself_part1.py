# Using the following code, add a method named identify that returns the calling object.
class Cat:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def identify(self):
        return self


# Comments show expected output
kitty = Cat('Sophie')
print(kitty)  # returns <__main__.Cat object at 0x1047fce30>
print(kitty.identify())  # returns <__main__.Cat object at 0x1047fce30>
# <__main__.Cat object at 0x10508c8d0>


# invoking the method that returns self is the same as
# directly referencing the variable that holds the object, kitty
