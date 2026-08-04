"""

Problem Statement:
Write a function that takes a dictionary where keys are strings and values are lists of integers. The function should return a new dictionary where the keys are the integers from the original lists, and the values are lists of the original string keys.

Test Cases:
"""


# from typing import KeysView


# data1 = {
#     'A': [1, 2, 3],
#     'B': [2, 3, 4],
#     'C': [1, 4]
# }
# Expected output: {1: ['A', 'C'], 2: ['A', 'B'], 3: ['A', 'B'], 4: ['B', 'C']}
# Probelem
# -function takes a dict
# -dict has keys and values, keys are strings, values are lists
# -those lists have integers
# -functions returns a new dict
# -in this dict, numbers are keys, in order
# -how to extract all those numbers so that I know which keys I have?
# -numbers are keys, values are strings, which were keys BUT
# {1: ['A', 'C'], because 1 was in 'A' and in "C"
# 2: ['A', 'B'], because 2 was in 'A' and in 'B'
# 3: ['A', 'B'], because 2 was in 'A' and in 'B'
# 4: ['B', 'C'], because 4 was in 'B' and in 'C'

# -get Keys, get all lists/values, and make a set of target keys
# create a new target dictionary `result`
# -while iterating over the the future keys/numbers that are going to be in the `result`, ask

# for 1 key in my_target_keys,
# iterate over the values (a list!) belonging to each key in the original dictionary
# if that target_key (from my_target_keys) exists as a value in the list that belongs to the key in the original dictionary
# add this letter/value to the list with values for the current target_key in the result dictionary
# return the result

def invert_dict_of_lists(original_dict):
    list_of_keys = list(original_dict.values())  # [[10], [20], [10, 20]]

    my_keys = []
    for l in list_of_keys:
        my_keys += l  # flatten the inner arrays
    my_target_keys = set(my_keys)

    result = {}
    for key in my_keys:
        result[key] = []

    for target_key in my_target_keys:  # so look at 10 and then 20
        for letter_key in original_dict:  # it iterates ONLY over the KEYS -----data2 = {'X': [10],'Y': [20],'Z': [10, 20]}
            if target_key in original_dict[letter_key]:
                result[target_key].append(letter_key)

    return result


# print(invert_dict_of_lists(data1))

data2 = {
    'X': [10],
    'Y': [20],
    'Z': [10, 20]
}
# Expected output: {10: ['X', 'Z'], 20: ['Y', 'Z']}
print(invert_dict_of_lists(data2))


# Expected output: {}
# print(invert_dict_of_lists({}))

# data2 = {'X': [10],'Y': [20],'Z': [10, 20]}

# refactored, setdefault version
def invert_dict_of_lists(original_dict):
    result = {}
    for key, values in original_dict.items():  # dict_items([('X', [10]), ('Y', [20]), ('Z', [10, 20])])
        for v in values:
            result.setdefault(v, []).append(key)
    return result


print(invert_dict_of_lists(data2))

# another solution
# Same logic as the setdefault version, just with the "create empty list if missing" behavior baked into the dict type itself instead of spelled out each time.

from collections import defaultdict


def invert_dict_of_lists(original_dict):
    result = defaultdict(list)
    for key, values in original_dict.items():
        for v in values:
            result[v].append(key)
    return dict(result)


print(invert_dict_of_lists(data2))
