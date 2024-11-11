# -iterate over the numbers in the list and multiply each number by -1
def invert(lst):
    return [x *(-1) for x in lst]


print(invert([1, 2, 3, 4, 5]))  # , [-1, -2, -3, -4, -5])
print(invert([1, -2, 3, -4, 5]))  # , [-1, 2, -3, 4, -5])
print(invert([]))  # , [])


def invert(lst):
    return [-x for x in lst]


print(invert([1, 2, 3, 4, 5]))  # , [-1, -2, -3, -4, -5])
print(invert([1, -2, 3, -4, 5]))  # , [-1, 2, -3, 4, -5])
print(invert([]))  # , [])


def invert(lst):
    return list(map(lambda x: -x, lst))


print(invert([1, 2, 3, 4, 5]))  # , [-1, -2, -3, -4, -5])
print(invert([1, -2, 3, -4, 5]))  # , [-1, 2, -3, 4, -5])
print(invert([]))  # , [])

