my_string = 'Python'

# characters at the index 1, 2, and 3
print(my_string[1:4])  # Output: 'yth'

# characters at the index 1, 2, and 3
print(my_string[0:4])  # Output: 'Pyth'

# characters at the index 0, 1, 2, 3
print(my_string[:4])  # Output: 'Pyth'

# characters at the index 2, 3, 4
print(my_string[2:-2])  # Output: 'th', character at index -2 is NOT included
print(my_string[-2])  # Output: 'thon', character at index -1 is included

print('-------------------------------')

my_list = ['P', 'y', 't', 'h', 'o', 'n']

# elements at index 2, 3, and 4
print(my_list[2:5])   # ['t', 'h', 'o']

# element at index to end
print(my_list[3:])    # ['h', 'o', 'n']

# elements at index 0 to -5 EXCLUDING
print(my_list[:-5])   # ['P']

# elements beginning to end
print(my_list[:])     # ['P', 'y', 't', 'h', 'o', 'n']
# my_list[:] — Basic Slicing:
# : is used for slicing a sequence (like a list, string, etc.) to create a shallow copy.
# When you write my_list[:], you are slicing from the beginning of the list to the end.
# This effectively creates a copy of the entire list because no start or end index is specified.

print(my_list[::])     # ['P', 'y', 't', 'h', 'o', 'n']
# my_list[::] — Slicing with Step:
# :: is used for slicing with a step. The format is my_list[start:stop:step]. Creates a shallow copy of the list.
# When you write my_list[::], you are also slicing from the beginning to the end,
# but with the default step of 1.
# This also returns all elements of my_list, but the step can be modified,
# for example, my_list[::2] would return every second element.

print('-------------------------------')
lst = ['A', 'n', 'a']
lst_copy = lst[:]

lst[2] = 'XXX'
print(lst)  # changed to ['A', 'n', 'XXX']
print(lst_copy)  # same as before['A', 'n', 'a']

lst = ['A', 'n', 'a']
lst_copy = lst[::]

lst[2] = 'fantastic'
print(lst)  # changed to ['A', 'n', 'fantastic']
print(lst_copy)  # same as before ['A', 'n', 'a']

print('-------------------------------')
# But in case of mutable objects like lists (as an element of the list_copy),
# changing the value inside the list will affect the original list as well.
matrix = [[1, 2], [3, 4], [5, 6]]
matrix_copy = matrix[:]

matrix[0][1] = 'OOOOO'
print(matrix)  # changed to [[1, 'OOOOO'], [3, 4], [5, 6]]
print(matrix_copy)  # also affected!!!, [[1, 'OOOOO'], [3, 4], [5, 6]]

# what to do to avoid this?
# always use copy.deepcopy() function when dealing with mutable objects.

print()
matrix = [[1, 2], [3, 4], [5, 6]]
matrix_copy = matrix.copy()

matrix[0][1] = 'OOOOO'
print(matrix)  # changed to [[1, 'OOOOO'], [3, 4], [5, 6]]
print(matrix_copy)  # also affected!!!, [[1, 'OOOOO'], [3, 4], [5, 6]]

print()

# from session with Amy
sub_list = ["-", "-", "-"]
matrix = []

for _ in range(3):
    matrix.append(sub_list)  # [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

matrix[0][0] = "X"
print(matrix) # [['X', '-', '-'], ['X', '-', '-'], ['X', '-', '-']]
# this happens because sub_list is a reference to the same list (["-", "-", "-"]) in memory
# when we change element at index 0 in element 0, we change it IN EVERY copy of ["-", "-", "-"].
# here we have 3 copies of ["-", "-", "-"] in memory, not 3 separate lists.
# the solution to this is to use sub_list.copy() to create a new list (deep copy) each time
# we append it to matrix.

print()

print("solution is to use sub_list.copy()")

sub_list = ["-", "-", "-"]
matrix = []
for _ in range(3):
    matrix.append(sub_list.copy())  # [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
# here we appended 3 times a (deep) copy of sub_list to matrix

matrix[0][0] = "X"
print(matrix)  # [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
