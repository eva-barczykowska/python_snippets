# Rewrite car as a list of lists in which each nested list contains two elements that represent the corresponding
# key/value pairs.

car = {
    'type':  'sedan',
    'color': 'blue',
    'year':  2003,
}

print(car.items()) # returns TUPLE:
# dict_items([('type', 'sedan'), ('color', 'blue'), ('year', 2003)])

list_of_lists = [list(item) for item in car.items()]
# list(item) changes each tuple into a list
# ('type', 'sedan') => ['type', 'sedan']
# ('color', 'blue') => ['color', 'blue']
# ('year', 2003)]) => ['year', 2003]

# [...] / list comprehension syntax will make it a list of lists
print(list_of_lists)
# [['type', 'sedan'], ['color', 'blue'], ['year', 2003]]