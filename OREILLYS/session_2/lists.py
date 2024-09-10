my_list = [22, 1, 2, 3, 4, 5]

slice = my_list[2:4]
print(slice)  # Output: [3, 4]

print(100 in my_list)
print(5 in my_list)

for one_element in my_list:
    print(one_element)


# my_list[10] = 22  # IndexError: list assignment index out of range
my_list.append(22)
my_list.append('22')
print(my_list)


my_list.remove(22)  # we specify what element we want to remove, only the first occurrence will be removed
print(my_list)

my_list += [100, 200, 300, 400, 500]
print(my_list)

last_element = my_list.pop()  # removes and returns the last element
print(last_element)
print(my_list)

# my_list.pop('!!!')  # ValueError: list.remove(x): x not in list

my_list.insert(2, 'inserted')
print(my_list)

print(my_list.pop(2)) # pops and returns the first element (element at index 0)

print(my_list)

my_list = [1, 2, 3]
also_my_list = my_list  # both my_list and also_my_list are pointing to the same list

my_list[0] = '!!!' # this will affect both my_list and also_my_list
print(my_list)
print(also_my_list)

print('--------------')
# to avoid this, we can use the copy() method
my_list = [1, 2, 3]
also_my_list = my_list.copy()  # creates a new list with the same
my_list[0] = '!!!'
print(my_list)  # affected
print(also_my_list) # not affected


print('--------------')
my_list = [1, 2, 3]
also_my_list = my_list[:]  # creates a new list with the same elements
my_list[0] = '***'
print(my_list)  # affected
print(also_my_list) # not affected


print('--------------')
my_list = [1, 2, 3]
my_list.insert(0, my_list[-1])
print(my_list)  # [3, 1, 2, 3]

my_list.clear()
print(my_list)  # []