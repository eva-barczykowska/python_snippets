odd = [1, 3, 5]
print(odd + [9, 7, 5])  # Output: [1, 3, 5, 9, 7, 5]

print(['a', 'b'] * 3)  # Output: ['a', 'b', 'a', 'b', 'a', 'b']

odd = [1, 9]
odd.insert(1, 3)  # inserting 3 at 1st index
print(odd)  # Output: [1, 3, 9]

odd[2:2] = [5, 7]  # [1, 3, *9]  # inserting [5, 7] at index
print(odd)  # Output: [1, 3, 5, 7, 9]

print('------------')
# incorrect values
odd = [2, 4, 6, 8]

# change the 1st item
odd[0] = 1

print(odd)  # Output: [1, 4, 6, 8]

# change 2nd to 4th items
odd[1:4] = [3, 5, 7]

print(odd)  # Output: [1, 3, 5, 7]

print('------------')

# append and extend

odd = [1, 3, 5]

odd.append(7)  # adding 7 to the list

print(odd)  # [1, 3, 5, 7]

print('------------')

odd = [1, 3, 5]

odd.extend([7, 9, 11])

print(odd)  # [1, 3, 5, 7, 9, 11]

print('------------')
# deleting items
my_list = ['p','r','o','b','l','e','m']

del my_list[2]    # delete one item (3rd item)

print(my_list)
# Output: ['p', 'r', 'b', 'l', 'e', 'm']

del my_list[1:5]  # delete multiple items
print(my_list)    # Output: ['p', 'm']

del my_list       # delete entire list
# print(my_list)    # NameError: 'my_list' is not defined