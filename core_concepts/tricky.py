a = b = 100
a += 50
print(a)  # Output: 150
print(b)  # Output: 100
print(id(a))  # Output: 4344359944
print(id(b))  # Output: 4344358344

a = b = []
a += [1, 2]
print(a)  # Output: [1, 2]
print(b)  # Output: [1, 2]