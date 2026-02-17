# * list methods:list.append(),list.pop(),list.reverse()
# * dictionary methods:dict.keys(),dict.values(),dict.items(),dict.get()

###

# my_list = [1, 2, 3, 4, 5]
# length_of_list = len(my_list)
# print("Length of the list:", length_of_list)

###

# lst_one = [0, 1, 2, 3]
# lst_two = lst_one.append(4)

# if lst_two:
#     print(lst_two)
# else:
#     print(lst_one)

# print(lst_one)

###

# my_list = [1, 2, 3, 4, 5]
# ele = my_list.pop()
# print("Popped element:", ele)
# print("List after popping:", my_list)
# ele1 = my_list.pop(1) #2 INDEX!!!
# print("Popped element at index 1:", ele1)
# print("Modified list after popping at index 1:", my_list) #[1, 3, 4]

###

# elements = [0, 1 , 2, "Dima"]

# elements = elements.reverse()
# print(elements)

# print(elements.reverse()) # prints None
# print(elements) #["Dima", 2,  1, 0]
#                 # ["Dima", 2, 1 , 0]
#                 # ['Dima', 2, 1, 0]

# python doesn’t store spaces in lists. [0, 1, 2, "dima"] has elements, not formatting. the spaces are just for humans. printing the list uses python’s own repr rules, which insert a single space after each comma. it doesn’t care how many spaces you typed originally.

###

# elements = [0, 1 , 2, "Dima"]
# print(elements.pop()) # "Dima"
# print(elements) # [0, 1, 2]

###

# ages = {
#     "dimo": 31,
#     "olena": 32,
#     "tetiana": 28
# }

# def get_val_of_dimo(info):
#     try:
#         info['dimo']
#         return info['dimo']
#     except KeyError:
#         return "Typo"

# print(get_val_of_dimo(ages))

###

# my_dict = {'a': 1, 'b': 2, 'c': 3}
# keys = my_dict.keys()
# print(keys) #dict_keys(['a', 'b', 'c'])

# for key in keys:
#     print(key) #\n

###

# my_dict = {'a': 1, 'b': 2, 'c': 3}
# values = my_dict.values()
# print(list(values)) #dict_values([1, 2, 3])
# print(type(values))

# for value in values:
#     print(value)

##

# my_dict = {'a': 1, 'b': 2, 'c': 3}
# items = my_dict.items()
# print(items) # my_dict.items({'a': 1, 'b': 2, 'c': 3}) my_dict.items(('a', 1), ('b', 2), ('c', 3))
# print(list(items))

# dict_items([('a', 1), ('b', 2), ('c', 3)])

# for key, value in items: # ('a', 1)
#     print(key, value)
    # a, 1 # a, 1
    # b, 2
    # c, 3

# repr is what prints strings with quotes:
# my_str = 'abc'
# print(my_str)       # abc
# print(str(my_str))  # abc (same as print(my_str))
# print(repr(my_str)) # 'abc' (note the quotes)

my_dict = {'a': 1, 'b': 2, 'c': 3}
items = my_dict.items()
print(items)
