# SORTING DICTIONARIES BY KEYS
food = {"sandwiches": 10, "drinks": 20, "oranges": 7}
print(food)
print(food["sandwiches"])

counts = food.items
print(counts)  # <built-in method items of dict object at 0x10424c840>

# .items() returns a list of tuples, where each tuple contains a key-value pair
print(food.items())
# returns a list of tuples, where each tuple contains a key-value pair
#  dict_items([('sandwiches', 10), ('drinks', 20), ('oranges', 7)])

print(sorted(food.items()))  # [('drinks', 20), ('oranges', 7), ('sandwiches', 10)]
# sorts the list of tuples by the first element of each tuple (so by keys

sorted_counts = dict(sorted(food.items()))
print(sorted_counts)

# This works because tuples are orderable and tuples order themselves lexicographically (meaning they sort by the
# first items first, then the second items, and so on). So we're effectively sorting the 2-item tuples by their keys.

# SORTING DICTIONARIES BY VALUES
# using a comprehension
sorted_counts = {key: value for key, value in sorted((value, key) for key, value in food.items())}
print(sorted_counts)

# but better to use sorted function

# Help on built-in function sorted in module builtins:
#
# sorted(iterable, /, *, key=None, reverse=False)
#     Return a new list containing all items from the iterable in ascending order.
#
#     A custom key function can be supplied to customize the sort order, and the
#     reverse flag can be set to request the result in descending order.

# The sorted function accepts a key function to sort by. Let's define it:

print()
print("--pass function to a function to sort by the value--")
counts = {"sandwiches": 10, "drinks": 20, "oranges": 7}


def value_of(item):
    """Return value given a (key, value) tuple."""
    key, value = item
    return value


sorted_counts = dict(sorted(counts.items(), key=value_of))
print(sorted_counts)

# This works because functions are objects in Python.
# The sorted function is relying on the fact that we can pass a function around just as we can pass any object
# around.
# The sorted function will call the given key argument, so the key must be a function (or another callable).
# The built-in sorted function isn't the only function that accepts a key argument.
# If we wanted to get the key with the greatest value, we could use the max function:

min_key, min_value = max(counts.items(), key=value_of)
print(min_key, min_value) # keys are sorted in ascending order, so 'oranges' is the smallest key
min_key, min_value = min(counts.items(), key=value_of)
