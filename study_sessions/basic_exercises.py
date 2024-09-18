# # Checking Key Existence
# # Check whether the keys 'name' and 'grade' exist in the following dictionary:

# student = {
#     'id': 123,
#     'grade': 'B',
# }


# # print(student.get('grade'))
# # print(student.get('name', 'This key does not exist.'))

# # for k in student:
# #     if k == 'name' or k == 'grade':
# #         print( f"{k} exists as key")
# #     else:
# #         print( f"'name' do NOT exist as key")

# # print(list(student.keys()))
# # print(list(student.values()))
# # print(list(student.items()))

# # for key in student.keys():
# #     print(key)

# # for value in student.values():
# #     print(value)

# # for item in student.items():
# #     print(item)

# from collections import Counter

# things = ["apple", "banana", "apple", "orange", "banana", "grape"]
# counted_things = Counter(things)
# print(counted_things)

# for something in counted_things:
#     print(something)

# print(type(counted_things))

# # ['__add__',
# #  '__and__',
# #  '__class__',
# #  '__class_getitem__',
# #  '__contains__',
# #  '__delattr__',
# #  '__delitem__',
# #  '__dict__',
# #  '__dir__',
# #  '__doc__',
# #  '__eq__',
# #  '__format__',
# #  '__ge__',
# #  '__getattribute__',
# #  '__getitem__',
# #  '__gt__',
# #  '__hash__',
# #  '__iadd__',
# #  '__iand__',
# #  '__init__',
# #  '__init_subclass__',
# #  '__ior__',
# #  '__isub__',
# #  '__iter__',
# #  '__le__',
# #  '__len__',
# #  '__lt__',
# #  '__missing__',
# #  '__module__',
# #  '__ne__',
# #  '__neg__',
# #  '__new__',
# #  '__or__',
# #  '__pos__',
# #  '__reduce__',
# #  '__reduce_ex__',
# #  '__repr__',
# #  '__reversed__',
# #  '__ror__',
# #  '__setattr__',
# #  '__setitem__',
# #  '__sizeof__',
# #  '__str__',
# #  '__sub__',
# #  '__subclasshook__',
# #  '__weakref__',
# #  '_keep_positive',
# #  'clear',
# #  'copy',
# #  'elements',
# #  'fromkeys',
# #  'get',
# #  'items',
# #  'keys',
# #  'most_common',
# #  'pop',
# #  'popitem',
# #  'setdefault',
# #  'subtract',
# #  'total',
# #  'update',
# #  'values']

# https://docs.python.org/3/library/functions.html#help

# items = [[], "Ewa", "hello"]
# # all()
#
# print(all(items))

print('------------------------------------')

student = {
    'id': 123,
    'grade': 'B',
}

print('name' in student)      # False
print('grade' in student)     # True
