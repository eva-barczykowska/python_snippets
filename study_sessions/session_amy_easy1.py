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
# # matrix[1][1] = 'O'
# import copy

# print()
# # copy() deep copy?
# list1 = [1, 2, [3, 4]]
# list2 = list1.copy()
# print(list1)
# print(list2)

# list1[2][0] = 'hello'
# print(list1)
# print(list2)

# list1 = [1, 2, [3, 4]]
# list2 = copy.deepcopy(list1)
# print(list1)
# print(list2)

# list1[2][0] = 'hello'
# print(list1)
# print(list2)

# https://docs.python.org/3/library/copy.html#copy.deepcopy
# Your colleague has implemented a custom function to find the maximum value in a list. However, the function sometimes works correctly, but other times it produces incorrect results. Can you help your colleague fix the bug?

# def find_maximum(numbers):
#     if not numbers:
#         return None
#     max_number = 0
#     for number in numbers:
#         if abs(number) > max_number:
#             max_number = number

#     return max_number

# print(find_maximum([45, 3, 10, 98, 22]))  # Expected 98
# print(find_maximum([-1, 0, 5, 3]))         # Expected 5
# print(find_maximum([-10, -3, -20, -2]))   # Expected -2
# print(find_maximum([-10, -2, -3, -20]))

# def find_maximum(numbers):
#     if not numbers:
#         return None
#     max_number = numbers[0]
#     for number in numbers:
#         if number > max_number:
#             max_number = number

#     return max_number

# print(find_maximum([45, 3, 10, 98, 22]))  # Expected 98
# print(find_maximum([-1, 0, 5, 3]))         # Expected 5
# print(find_maximum([-10, -3, -20, -2]))   # Expected -2
# print(find_maximum([-10, -2, -3, -20]))

# def find_maximum(numbers):
#     if not numbers:
#         return None

#     max_number = float('-inf')

#     for number in numbers:
#         if number > max_number:
#             max_number = number
#     return max_number

# print(find_maximum([45, 3, 10, 98, 22]))  # Expected 98
# print(find_maximum([-1, 0, 5, 3]))         # Expected 5
# print(find_maximum([-10, -3, -20, -2]))   # Expected -2
# print(find_maximum([-10, -2, -3, -20]))

# Digit Product
# You've been asked to implement a function called digit_product that takes a string of digits as an argument and returns the product of all the digits in the string.

# When testing the function, you find that it returns 0, which is not what you expect. Can you identify the issue and correct the code?

# def digit_product(str_num):
#     digits = [int(n) for n in str_num]
#     # print(digits)
#     product = 1

#     for digit in digits:
#         product *= digit

#     return product

# result = digit_product('12345')
# print(result)  # expected: 120, actual: 0

# Isn't it Odd?
# Write a function that takes one integer argument and returns True when the number's absolute value is odd, False otherwise.

# def odd_or_not(number):
#     return abs(number) % 2 != 0

# print(odd_or_not(2) == False )
# print(odd_or_not(-2) == False )
# print(odd_or_not(17) == True )
# print(odd_or_not(-17) == True )

# Odd Numbers
# Print all odd numbers from 1 to 99, inclusive, with each number on a separate line.

# Bonus Question: Can you solve the problem by iterating over just the odd numbers?

# for number in range(1, 100):
#     if number % 2 != 0:
#         print(number)

# for number in range(1, 100, 2):
#         print(number)

# Even Numbers
# Print all even numbers from 1 to 99, inclusive, with each number on a separate line.

# Bonus Question: Can you solve the problem by iterating over just the even numbers?

for number in range(2, 100, 2):
    print(number)
