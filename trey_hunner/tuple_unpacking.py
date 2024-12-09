p = (2, 1, 3)

# we can print indices as follows:
print(p[0], p[1], p[2])

# or we can unpack the tuple into variables:
x, y, z = p

# but the number of variables must match the number of elements in the tuple
# otherwise the get a ValueError:
#     x, y = p
#     ^^^^
# ValueError: too many values to unpack (expected 2)

# TUPLE UNPACKING is really handy for avoiding hard-coded indexes and instead,
# giving descriptive names to each of the things inside a tuple.

print()
# TUPLE UNPACKING is often used with a loop
things = {"ducks": 2, "lamps": 3, "chairs": 0}
print(things)
print(things.keys())
print(things.values())
print(things.items())  # this gives us a list of tuples, where each tuple is a key-value pair
# dict_items([('ducks', 2), ('lamps', 3), ('chairs', 0)])