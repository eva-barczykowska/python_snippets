"""
zip() in Python aggregates elements from multiple iterables into tuples, facilitating parallel iteration.
dict(zip()) creates dictionaries by pairing keys and values from two sequences.
zip() is lazy in Python, meaning it returns an iterator instead of a list.
There’s no unzip() function in Python, but the same zip() function can reverse the process
using the unpacking operator *.
Alternatives to zip() include itertools.zip_longest() for handling iterables of unequal lengths.
"""

numbers = [1, 2, 3, 4, 5]
letters = ['a', 'b', 'c', 'd', 'e']
numbers_and_letters = zip(numbers, letters)
print(numbers_and_letters)  # <zip object at 0x7fa4831153c8>, this is cold an iterator object
print(type(numbers_and_letters))  # <class 'zip'>
lst = list(numbers_and_letters)
print(lst)  # [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]

dictionary = dict(numbers_and_letters)
print(dictionary)  # {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}

# shorter
numbers_and_letters_shorter = dict(zip(numbers, letters))
print(numbers_and_letters_shorter)  # {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}

# reverse using unpacking operator *

# working with sets you can see weird results because sets are unordered and cannot contain duplicate values.
s1 = {2, 3, 1}
s2 = {"b", "a", "c"}
zipped_sets = zip(s1, s2)
print(list(zipped_sets))  # [(1, 'b'), (2, 'a'), (3, 'c')]

# you call the Python zip() function with three iterables, so the resulting tuples have three elements each.

list(zip(range(5), range(5)))
# [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
list(zip(range(5), range(100)))
# [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)] # only the first 5 elements are taken from the second iterable!

"""
If trailing or unmatched values are important to you, then you can use itertools.zip_longest() instead of zip().
 With this function, the missing values will be replaced with whatever you pass to the fillvalue argument
 (defaults to None). The iteration will continue until the longest iterable is exhausted:
"""

from itertools import zip_longest

numbers = [1, 2, 3]
letters = ["a", "b", "c"]
longest = range(5)
zipped = zip_longest(numbers, letters, longest, fillvalue="?")
print(list(zipped))
# [(1, 'a', 0), (2, 'b', 1), (3, 'c', 2), ('?', '?', 3), ('?', '?', 4)]

# if we want to produce error when iterables are not of the same length
# list(zip(range(5), range(100), strict=True))
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: zip() argument 2 is longer than argument 1

# traversing lists in parallel

letters = ["a", "b", "c"]
numbers = [0, 1, 2]
for letter, number in zip(letters, numbers):
    print(f"Letter: {letter}")
    print(f"Number: {number}")

# Letter: a
# Number: 0
# Letter: b
# Number: 1
# Letter: c
# Number: 2

# zipping more than 2 elements is possible
integers = [1, 2, 3]
letters = ["a", "b", "c"]
floats = [4.0, 5.0, 6.0]
zipped = zip(integers, letters, floats)  # Three input iterables
print(list(zipped))  # [(1, 'a', 4.0), (2, 'b', 5.0), (3, 'c', 6.0)]

"""
In Python 3.6 and beyond, dictionaries are ordered collections, meaning they keep their elements
in the same order in which they were introduced.
If you take advantage of this feature, then you can use the Python zip() function
to iterate through multiple dictionaries in a safe and coherent way:
"""
print()
dict_one = {"name": "John", "last_name": "Doe", "job": "Python Consultant"}
dict_two = {"name": "Jane", "last_name": "Doe", "job": "Community Manager"}
for (k1, v1), (k2, v2) in zip(dict_one.items(), dict_two.items()):
    print(k1, "->", v1)
    print(k2, "->", v2)

# name -> John
# name -> Jane
# last_name -> Doe
# last_name -> Doe
# job -> Python Consultant
# job -> Community Manager

print()
# unzipping a sequence

pairs = [(1, "a"), (2, "b"), (3, "c"), (4, "d")]
numbers, letters = zip(*pairs)
print(numbers)  # (1, 2, 3, 4)

print(letters)  # ('a', 'b', 'c', 'd')

# sort by letters or numbers - depending what you will put first

letters = ["b", "a", "d", "c"]
numbers = [2, 4, 3, 1]
print(sorted(zip(letters, numbers)))  # Sort by letters
# [('a', 4), ('b', 2), ('c', 1), ('d', 3)]

letters = ["b", "a", "d", "c"]
numbers = [2, 4, 3, 1]
print(sorted(zip(numbers, letters)))  # Sort by numbers
# [(1, 'c'), (2, 'b'), (3, 'd'), (4, 'a')]

print()
# calculating monthly profit
total_sales = [52000.00, 51000.00, 48000.00]
prod_cost = [46800.00, 45900.00, 43200.00]
for sales, costs in zip(total_sales, prod_cost):
    profit = sales - costs
    print(f"Total profit: {profit}")

# Total profit: 5200.0
# Total profit: 5100.0
# Total profit: 4800.0
