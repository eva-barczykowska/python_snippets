class Point:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def __repr__(self):
        cls = type(self).__name__
        return f"{cls}(x={self.x!r}, y={self.y!r}, z={self.z!r})"
# r stands for representation
# When you use !r in a string formatting expression,
# Python will call the __repr__ method of the object being formatted.
# This is in contrast to the default behavior, which uses the __str__ method.
# In the context of the Point class, the __repr__ method is defined to return
# a string that includes the class name and the values of the x, y, and z coordinates.
# By using !r in the string formatting expression, the __repr__ method of the x, y, and z attributes is called,
# and their string representations are included in the output.

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)

# This class allows 3-dimensional points to be compared:
p = Point(1, 2, 3)
q = Point(1, 2, 3)
print(p == q) # Output: True

print(p) # Output: Point(x=1, y=2, z=3)
print(q) # Output: Point(x=1, y=2, z=3)

#Note how the return statement of the __eq__ method is implemented in this class:

# def __eq__(self, other):
#     if not isinstance(other, Point):
#         return NotImplemented
#     return (self.x, self.y, self.z) == (other.x, other.y, other.z)

# Instead of comparing the coordinates or our two Point instances like this:
# (self.x == other.x) and (self.y == other.y) and (self.z == other.z)

# We're making two 3-item tuples and comparing them:
# (self.x, self.y, self.z) == (other.x, other.y, other.z)

# Tuples, lists, and other data structures in Python can be compared using Python's == operator.
# Equality checks between these objects will compare the contents of these objects for equality.
# Since equality between data structures relies on equality checks of the contents of those data structures,
# equality checks are DEEP OPERATIONS.

# Here are two lists that contain tuples of strings:
#
# >>> pairs1 = [("dark", "night"), ("fire", "ice")]
# >>> pairs2 = [("dark", "night"), ("fire", "ice")]

# Comparing these lists will compare each item at common indexes within the lists.
# Since those items are tuples, those comparisons will compare each item at common indexes
# within the tuples. Since those items are strings, those comparisons will compare each character at common indexes
# within the strings.

# So this operation:
#
# >>> pairs1 == pairs2 returns True
#
# Performs comparison checks at a few levels without us needing to do anything special.

# Deep comparisons work with equality and inequality checks,
# but they also work with all other comparison operators, including ordering operators:
#
# >>> pair1 = ("truth", "dare")
# >>> pair2 = ("truth", "democracy")
# >>> pair1 < pair2
# True

print(ord("a")) # Output: 97      # "a" has smaller ASCII value than "e"
print(ord("e")) # Output: 101

# characters are compared based on their ASCII values, lexicographically, just like in Ruby