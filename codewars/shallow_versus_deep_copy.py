list1 = [1, 2, 3]
list2 = list1

# changing the first item of list1 to 'one'
list1[0] = 'one'

print(list1)   # Output: ['one', 2, 3]
print(list2)   # Output: ['one', 2, 3]

print('------------')

list1 = [1, 2, 3]
list2 = list1.copy()  # copying list1 to list2

# changing the first item of list1 to 'one'
list1[0] = 'one'

print(list1)   # Output: ['one', 2, 3]
print(list2)   # Output: [1, 2, 3]

print('...but if a list has nested lists, changes to nested lists will be reflected in both the original and copied list')
list1 = [1, 2, [3, 4]]
list2 = list1.copy()
print(list1)   # Output: [1, 2, [3, 4]]
print(list2)   # Output: [1, 2, [3, 4]]

list2[2][0] = 'thirty-three'

print(list1)   # Output: [1, 2, ['thirty-three', 4]]
print(list2)   # Output: [1, 2, ['thirty-three', 4]]

print('------------')
# also explore [:] for shallow copy when changing an element that is not nested
list1 = [1, 2, [3, 4]]
list2 = list1[:]
print(list1)   # Output: [1, 2, [3, 4]]
print(list2)   # Output: [1, 2, [3, 4]]
list1[0] = 'billion'

print(list1)   # Output: ['billion', 2, [3, 4]] CHANGED
print(list2)   # Output: [1, 2, [3, 4]] UNCHANGED

# THE PROBLEM IS ALWAYS A NESTED LIST.
# THE COPIED LIST IS A NEW LIST WITH THE SAME ELEMENTS,
# BUT THE ELEMENTS IN THE NESTED LIST ARE THE SAME LIST!!!
# SO LISTS ARE PASSED BY REFERENCE, NOT BY VALUE, OR, IN OTHER WORDS,
# THEY ARE SHARED, NOT COPIED.

print('------------')

# also explore [:] for shallow copy
list1 = [1, 2, [3, 4]]
list2 = list1[:]
print(list1)   # Output: [1, 2, [3, 4]]
print(list2)   # Output: [1, 2, [3, 4]]
list2[2][0] = 'three'

print(list1)   # Output: [1, 2, ['three', 4]]
print(list2)   # Output: [1, 2, ['three', 4]]

print('------------')

# also the same with [::] for deep copy
group1 = [1, 2, [3, 4]]
group2 = group1[::]
print(group1)   # Output: [1, 2, [3, 4]]
print(group2)   # Output: [1, 2, [3, 4]]

# case 1 when an element is being changed
group1[0] = 'fifty-five'
print(group1)   # Output: ['fifty-five', 2, [3, 4]] # group1 and group2 are independent, DIFFERENT
print(group2)   # Output: [1, 2, [3, 4]]

# case 2 when an element in a nested list is being changed
group1 = [1, 2, [3, 4]]
group2 = group1[::]
print(group1)   # Output: [1, 2, [3, 4]]
print(group2)   # Output: [1, 2, [3, 4]]

# case 1 when an element is being changed
group1[2][0] = 'hundred-and-one'
print(group1)  # Output: [1, 2, ['hundred-and-one', 4]]
print(group2)  # Output: [1, 2, ['hundred-and-one', 4]]

# conclusion: lists in python can be only deep copied using different methods like .copy(),
# [:] and [::] but they are not identical.