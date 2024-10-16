# Write a program that asks for user's name, then greets the user. If the user appends a ! to their name, the computer will yell the greeting (print it using all uppercase).
# Example 1
# What is your name? Sue
# Hello Sue.
# Example 2
# What is your name? Bob!
# HELLO BOB! WHY ARE WE YELLING?

# # name = input("What's your name?")
# # if name[-1] == "!":
# #     print("HELLO", name.upper(), "WHY ARE WE YELLING?")
# # else:
# #     print(f"Hello, {name}.")


# Create a function that takes two arguments, multiplies them together, and returns the result.

# Example
# def multiply(num1, num2):
#     return num1 * num2

# print(multiply(5, 3) == 15)  # True

# Using the multiply function from the "Multiplying Two Numbers" exercise, write a function that computes the square of its argument (the square is the result of multiplying a number by itself).

# def square(num):
#     return multiply(num, num)


# print(square(5) == 25)   # True
# print(square(-8) == 64)  # True

# Write a program that prompts the user for two positive numbers (floating-point), then prints the results of the following operations on those two numbers: addition, subtraction, product, quotient, floor quotient, remainder, and power. Do not worry about validating the input.

# Examples
# ==> Enter the first number:
# 3.141529
# ==> Enter the second number:
# 2.718282
# ==> 3.141529 + 2.718282 = 5.859811
# ==> 3.141529 - 2.718282 = 0.42324699999999993
# ==> 3.141529 * 2.718282 = 8.539561733178
# ==> 3.141529 / 2.718282 = 1.1557038600115808
# ==> 3.141529 // 2.718282 = 1.0
# ==> 3.141529 % 2.718282 = 0.42324699999999993
# ==> 3.141529 ** 2.718282 = 22.45792517468373

# first_num = float(input("==> Enter the first number: \n"))
# second_num = float(input("==> Enter the second number: \n"))
# print(f"==> {first_num} + {second_num} = {first_num + second_num}")
# print(f"==> {first_num} - {second_num} = {first_num - second_num}")
# print(f"==> {first_num} * {second_num} = {first_num * second_num}")
# print(f"==> {first_num} / {second_num} = {first_num / second_num}")
# print(f"==> {first_num} // {second_num} = {first_num // second_num}")
# print(f"==> {first_num} % {second_num} = {first_num % second_num}")
# print(f"==> {first_num} ** {second_num} = {first_num ** second_num}")

# Write a function that returns the next to last word in the string argument.

# Words are any sequence of non-blank characters.

# You may assume that the input string will always contain at least two words.

# Examples
# These examples should print True
# def penultimate(str):
#     return str.split()[-2]

# print(penultimate("last word") == "last")
# print(penultimate("Launch School is great!") == "is")

# Exclusive Or
# The or operator returns a truthy value if either or both of its operands are truthy, a falsy value if both operands are falsy. The and operator returns a truthy value if both of its operands are truthy, and a falsy value if either operand is falsy. This works great until you need only one of two conditions to be truthy, the so-called exclusive or, also known as xor (pronounced "ECKS-or").

# In this exercise, you will write an xor function that takes two arguments, and returns True if exactly one of its arguments is truthy, False otherwise.

# def xor(arg1, arg2):
#     if arg1 and arg2:
#         return False
#     else:
#         return True

# print(xor(5, 0) == True)
# print(xor(False, True) == True)
# print(xor(1, 1) == False)
# print(xor(True, True) == False)

# Write a function that returns a list that contains every other element of a list that is passed in as an argument. The values in the returned list should be those values that are in the 1st, 3rd, 5th, and so on elements of the argument list.

'''retrieve an element at the odd index'''
# def oddities(lst):
#     result = []

#     indices = [x for x in range(0, len(lst)) if x % 2 == 0]

#     for index in indices:
#         result.append(lst[index])
#     return result

# def oddities(lst):
#     return lst[::2]

# print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
# print(oddities([1, 2, 3, 4]) == [1, 3])        # True
# print(oddities(["abc", "def"]) == ['abc'])     # True
# print(oddities([123]) == [123])                # True
# print(oddities([]) == [])                      # True

# Build a program that randomly generates and prints Teddy's age. To get the age, you should generate a random number between 20 and 100, inclusive.
# Teddy is 69 years old!

import random

print(f"Teddy is {random.randint(20, 101)} years old!")

# FACTFULLNESS