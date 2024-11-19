def name_shuffler(name):
    first_name, last_name = name.split()
    return last_name + " " + first_name


print(name_shuffler('john McClane'))  # , 'McClane john')
print(name_shuffler('Mary jeggins'))  # , 'jeggins Mary')
print(name_shuffler('tom jerry'))  # , 'jerry tom')

print()


def name_shuffler(str_):
    [first, last] = str_.split()  # very nice
    return last + " " + first


print(name_shuffler('john McClane'))  # , 'McClane john')
print(name_shuffler('Mary jeggins'))  # , 'jeggins Mary')
print(name_shuffler('tom jerry'))  # , 'jerry tom')

print()


def name_shuffler(str_):
    return ' '.join(str_.split(' ')[::-1])


print(name_shuffler('john McClane'))  # , 'McClane john')
print(name_shuffler('Mary jeggins'))  # , 'jeggins Mary')
print(name_shuffler('tom jerry'))  # , 'jerry tom')
