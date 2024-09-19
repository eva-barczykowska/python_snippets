odd = [1, 3, 5]
print(odd + [9, 7, 5])  # Output: [1, 3, 5, 9, 7, 5]

print(['a', 'b'] * 3)  # Output: ['a', 'b', 'a', 'b', 'a', 'b']

odd = [1, 9]
odd.insert(1, 3)  # inserting 3 at 1st index
print(odd)  # Output: [1, 3, 9]

odd[2:2] = [5, 7]  # [1, 3, *9]  # inserting [5, 7] at index
print(odd)  # Output: [1, 3, 5, 7, 9]
