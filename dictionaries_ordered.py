# dictionaries are ordered and considered equal if they contain the same key-value pairs,
# never mind the order

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'c': 3, 'b': 2, 'a': 1}

print(dict1 == dict2)  # True

# lists are not considered equal if they contain the same elements but in different order

list1 = [1, 2, 3]
list2 = [3, 2, 1]

print(list1 == list2)  # False
#The order of the items is a fundamental characteristic of lists.
# Therefore, these lists are not considered equal.
# This feature is part of the definition of all sequences, such as lists, tuples, and strings.

from collections import OrderedDict

ordered_dict1 = OrderedDict({'a': 1, 'b': 2, 'c': 3})
ordered_dict2 = OrderedDict({'c': 3, 'b': 2, 'a': 1})

print(ordered_dict1 == ordered_dict2)  # False!!!