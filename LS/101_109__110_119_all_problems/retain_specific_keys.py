'''Retain Specific Keys
Given a dictionary and a list of keys, produce a new dictionary that only contains the key/value pairs for
the specified keys.

Problem:
-you have a dictionary and a list of keys
-return from a function a new dictionary with the keys from the list

E:

A:
can I maybe filter a dict based on the keys in the list?
-initialize the new_dict
-iterate over the given keys
-save to new_dict the key at the current iteration
-as the value, select FROM THE INPUT DICTIONARY the value corresponding to the key at the current iteration

A2:
-how else could I do it?


'''

def keep_keys(input_dict, keys):
    new_dict = {}
    for key in keys:
        if key in input_dict:  # check is necessary to avoid KeyError
            new_dict[key] = input_dict[key]

    return new_dict


input_dict = {
    'red': 1,
    'green': 2,
    'blue': 3,
    'yellow': 4,
}

keys = ['red', 'blue']
expected_dict = {'red': 1, 'blue': 3}
print(keep_keys(input_dict, keys) == expected_dict) # True

# def keep_keys(dicts, input_keys):
#     new_dict = {}
#     for key in input_keys:
#         for dict_key, dict_value  in dicts.items():
#             if key in dict_key:
#                 new_dict[dict_key] = dict_value
#     print(new_dict)
#     return new_dict
#
# input_dict = {
#     'red': 1,
#     'green': 2,
#     'blue': 3,
#     'yellow': 4,
# }
#
# keys = ['red', 'blue']
# expected_dict = {'red': 1, 'blue': 3}
# print(keep_keys(input_dict, keys) == expected_dict) # True


input_dict = {
    'red': 1,
    'green': 2,
    'blue': 3,
    'yellow': 4,
}

keys = ['red', 'blue']
expected_dict = {'red': 1, 'blue': 3}

print(keep_keys(input_dict, keys) == expected_dict) # True
def keep_keys(input_dict, keys):
    new_dict = {}
    for pair in input_dict.items(): # dict_items([('red', 1), ('blue', 3)]) IS ITERABLE!!!
        if pair[0] in keys:
            new_dict[pair[0]] = pair[1]
    return new_dict

print(keep_keys(input_dict, keys) == expected_dict) # True

expected_dict = {'red': 1, 'blue': 3}
# print(expected_dict.keys()) # needs to be converted to a list -dict_keys(['red', 'blue'])
# print(expected_dict.values()) # dict_values([1, 3])
# print(sorted(expected_dict.items())) # [('blue', 3), ('red', 1)] # it sorts by the first element of each tuple (so by keys)
# dict_keys(['red', 'blue'])
# dict_values([1, 3])
#
# dictc_keys IS ITERABLE!!!

#dictionary comprehension

def keep_keys(input_dict, keys):
    return {key: input_dict[key]
            for key in keys
            if key in input_dict}



input_dict = {
    'red': 1,
    'green': 2,
    'blue': 3,
    'yellow': 4,
}

keys = ['red', 'blue']
expected_dict = {'red': 1, 'blue': 3}

print(keep_keys(input_dict, keys) == expected_dict) # True