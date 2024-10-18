# How big is the room?

# Build a program that asks the user to enter the length and width of a room, in meters, then prints the room's area in both square meters and square feet.

# Note: 1 square meter == 10.7639 square feet

# name =input("what's your name?")

# length = input("What's the length of the room in meters? ")
# width = input("What's the width of the room in meters? ")
# square_meters = int(length) * int(width)

# print(f"The room's area is {square_meters} square meters and {round(square_meters * 10.7639, 2)} square feet.")

# Tip Calculator
# Create a simple tip calculator. The program should prompt for a bill amount and a tip rate. The program must compute the tip, then print both the tip and the total amount of the bill. You can ignore input validation and assume that the user will enter valid numbers.

# bill_amount = float(input("What is the bill?"))
# tip_percentage = int(input("What is the tip percentage?"))

# tip = (bill_amount * tip_percentage) / 100

# print(f"The tip is {'${:,.2f}'.format(tip)} and the total is {'${:,.2f}'.format(bill_amount+ tip)}.")

# What is the bill? 200
# What is the tip percentage? 20

# The tip is $40.00
# The total is $240.00

# '${:,.2f}'.format(1234.56)

# https://www.geeksforgeeks.org/how-to-format-numbers-as-currency-strings-in-python/

# http://programarcadegames.com/index.php?chapter=formatting#:~:text=A%20format%20of%20.,1.5555%20would%20display%20as%201.56%20.

# Write a program that asks the user to enter an integer greater than 0, then asks whether the user wants to determine the sum or the product of all numbers between 1 and the entered integer, inclusive.

# Example 1
# Please enter an integer greater than 0: 5
# Enter "s" to compute the sum, or "p" to compute the product. s

# The sum of the integers between 1 and 5 is 15.
# Example 2
# Please enter an integer greater than 0: 6
# Enter "s" to compute the sum, or "p" to compute the product. p

# # The product of the integers between 1 and 6 is 720.

# number = input("Please enter an integer greater than 0: ")
# calculation = input('Enter "s" to compute the sum, or "p" to compute the product.')

# if calculation == 's':
#     new_number = int(number)
#     sum_new = 0
#     for number in range(1, new_number + 1):
#         sum_new += number

#     print(f"The sum of the integers between 1 and {number} is {sum_new}.")
# else:
#     new_number = int(number)
#     product = 1
#     for number in range(1, new_number + 1):
#         product *= number

#     print(f"The product of the integers between 1 and {number} is {product}.")
# import math as m
# from math import prod

# from operator import*

# number = input("Please enter an integer greater than 0: ")
# calculation = input('Enter "s" to compute the sum, or "p" to compute the product.')

# if calculation == 's':
#     new_number = int(number)

#     print(f"The sum of the integers between 1 and {number} is {sum(list(range(1, new_number + 1)))}.")
# else:
#     new_number = int(number)
#     result = prod(list(range(1, new_number + 1)))
#     print(f"The product of the integers between 1 and {number} is {result}.")

# Write a function that takes two strings as arguments, determines the length of the two strings, and then returns the result of concatenating the shorter string, the longer string, and the shorter string once again. You may assume that the strings are of different lengths.

# These examples should all print True
# def short_long_short(str1, str2):
#     if len(str1) < len(str2):
#         return str1 + str2 + str1
#     else:
#         return str2 + str1 + str2

# print(short_long_short('abc', 'defgh') == "abcdefghabc")
# print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
# print(short_long_short('', 'xyz') == "xyz")

def short_long_short(str1, str2):
    if len(str1) < len(str2):
        return "".join([str1, str2, str1])
    else:
        return "".join([str2, str1, str2])

print(short_long_short('abc', 'defgh') == "abcdefghabc")
print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
print(short_long_short('', 'xyz') == "xyz")

import math
# math.prod(iterable, start)start
lst = [1, 2, 3, 4, 5]
two_last_elements_multiplied = math.prod(lst[-2:])
print(two_last_elements_multiplied)