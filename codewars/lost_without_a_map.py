def maps(a):
    return [2 * x for x in a]

print(maps([1, 2, 3]))  # , [2, 4, 6])


def maps(a):
    return list(map(lambda x:2*x, a))


print(maps([1, 2, 3]))  # , [2, 4, 6])