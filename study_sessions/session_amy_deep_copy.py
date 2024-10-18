# list1 = [1, 2, 3]
# list2 = list1[:]
# print(list1)
# print(list2)


# list1[0] = "fifty"
# print(list1)
# print(list2)


# print()

# list1 = [1, 2, [3, 4]]
# list2 = list1[:]
# print(list1)
# print(list2)

# list1[2][0] = 'one hundred'
# print(list1)
# print(list2)

# # what is deep / shallow


# sub_list = ["-", "-", "-"]
# matrix = []

# for _ in range(3):
#     matrix.append(sub_list.copy())

# matrix[0][0] = "X"
# print(matrix) # [['X', '-', '-'], ['X', '-', '-'], ['X', '-', '-']]
# matrix[1][1] = 'O'
import copy

print()
# copy() deep copy?
list1 = [1, 2, [3, 4]]
list2 = list1.copy()
print(list1)
print(list2)

list1[2][0] = 'hello'
print(list1)
print(list2)

list1 = [1, 2, [3, 4]]
list2 = copy.deepcopy(list1)
print(list1)
print(list2)

list1[2][0] = 'hello'
print(list1)
print(list2)

# https://docs.python.org/3/library/copy.html#copy.deepcopy