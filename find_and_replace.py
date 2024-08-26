
# If using the [] (bracket) notation to directly access or modify list elements is not allowed, we can still
# accomplish the task by using methods that operate on lists indirectly.
# Since we can't use list[index] or create new lists with [], we'll rely on enumerate to iterate with indexes
# and use list methods like insert and pop.

def replace(lst, X, Y):
    while lst.count(X) > 0:
        index = lst.index(X)
        lst.pop(index)
        lst.insert(index, Y)

L = [3, 1, 4, 1, 5, 9]
replace(L, 1, 7)
print(L)  # Output: [3, 7, 4, 7, 5, 9]

def replace(lst, X, Y):
    while X in lst:
        # Find the index of the first occurrence of X
        index = lst.index(X)
        # Replace the element at that index with Y
        lst[index] = Y


L = [3, 1, 4, 1, 5, 9]
replace(L, 1, 7)
print(L)  # Output: [3, 7, 4, 7, 5, 9]

def replace(lst, X, Y):
    while lst.count(X) > 0:
        index = lst.index(X)
        lst[index] = Y

L = [3, 1, 4, 1, 5, 9]
replace(L, 1, 7)
print(L)  # Output: [3, 7, 4, 7, 5, 9]


