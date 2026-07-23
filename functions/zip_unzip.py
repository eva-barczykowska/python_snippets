names = ["Sarah", "Matt", "Jim", "Denise", "Kate"]
ages = [25, 30, 28, 32, 27]

together = list(zip(names, ages))

print(together) # produces a list of tuples
# [('Sarah', 25), ('Matt', 30), ('Jim', 28), ('Denise', 32), ('Kate', 27)]

#use it/print it

for name, age in together:
    print(f"Name: {name}, Age: {age}")

#unpacking the list of tuples

names_unpacked, ages_unpacked = zip(*together) # * means we will have tuples unpacked
print(names_unpacked) # produces a list of names - this will be a TUPLE
print(ages_unpacked) # produces a list of ages - this will be a TUPLE

# if we want to convert them back to lists
print(list(names_unpacked)) # converting back to a list
print(list(ages_unpacked)) # converting back to a list

# what if they are unleaven lenght?
product = zip(names, ages, ["extra", "element"]) #Names after Matt are ignored
print(list(product)) # produces a list of tuples

# zip produces ITERATOR object, we can use it in a loop or convert it to a list
# print(next(product))
#
# Traceback (most recent call last):
#   File "/Users/e-vah/PycharmProjects/python_snippets/zip_unzip.py", line 29, in <module>
#     print(next(product))
# StopIteration
# https://www.thepythoncodingstack.com/p/the-anatomy-of-a-for-loop?utm_source=substack&utm_medium=email


# how to mitigate this???
from itertools import zip_longest
brands = ["Apple", "Samsung", "Google", "Nokia"]
market_value = [1000, 2000]
brands_and_their_market_value = zip_longest(brands, market_value, fillvalue="N/A") #Names after Matt are filled with N/A
print(list(brands_and_their_market_value)) # produces a list of tuples

# sorted_team = sorted(together, key=lambda person: person[1]) # sort by age
# print(sorted_team)

from operator import itemgetter
sorted_team = sorted(together, key=itemgetter(1)) # sort by age
print(sorted_team)

#extracting multiple items
# itemgetter(1, 0)  # returns a tuple of (x[1], x[0])
# sorted(data, key=itemgetter(1, 0))  # Sort by age, then by name
