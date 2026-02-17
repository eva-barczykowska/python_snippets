my_dictionary = {'green': 1, 'blue': 2, 'yellow': 3}
print(my_dictionary)
print(type(my_dictionary))
print(my_dictionary.keys()) # gives us dict_keys(['green', 'blue', 'yellow']), we can convert it to a list
print(list(my_dictionary.keys()))

print(my_dictionary.values())
print(list(my_dictionary.values()))

print(my_dictionary.items())
print(list(my_dictionary.items())) # we will get list of tuples [('green', 1), ('blue', 2), ('yellow', 3)]