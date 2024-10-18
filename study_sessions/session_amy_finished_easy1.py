# Leap Years (Part 1)
# Write a function that takes any year greater than 0 as input and returns True if the year is a leap year, or False if it is not.

# For simplicity, this exercise assumes that the Gregorian calendar has been in continuous use since the year 1. We'll address that assumption in the next exercise that follows this one.

# To determine whether a given year is a leap year, use the rules of the Gregorian calendar:

# If the year is divisible by 400, it is a leap year.
# If the year is divisible by 100 but not by 400, it is not a leap year.
# If the year is divisible by 4 but not by 100, it is a leap year.
# All other years are not leap years.

# These examples should all print True

# '''
# Goal: intake a year and return a boolean dependent on whether or not it's a leap year.
# INput: integer
# output: boolean

# Rules:
# - year is divisible by 400 -> return True
# - year is divisible by 100 but not 400 -> False
# - year is divisible by 4 but not by 100 -> True

# E:
# print(is_leap_year(4) == True)
#  - 4%4 == 0
# print(is_leap_year(1000) == False)
# print(is_leap_year(1100) == False)
# print(is_leap_year(1200) == True)
# print(is_leap_year(1300) == False)

# D:
# INput: integer
# intermediate: math
# output: boolean

# A:
# - year is divisible by 400 -> return True
# - year is divisible by 100 but not 400 -> False
# - year is divisible by 4 but not by 100 -> True

# '''

# def is_leap_year(num):
#     if num % 400 == 0:
#         return True
#     elif num % 100 == 0:
#         return False
#     elif num % 4 == 0:
#         return True
#     else:
#         return False


# print(is_leap_year(1) == False)
# print(is_leap_year(2) == False)
# print(is_leap_year(3) == False)
# print(is_leap_year(4) == True)
# print(is_leap_year(1000) == False)
# print(is_leap_year(1100) == False)
# print(is_leap_year(1200) == True)
# print(is_leap_year(1300) == False)
# print(is_leap_year(1751) == False)
# print(is_leap_year(1752) == True)
# print(is_leap_year(1753) == False)
# print(is_leap_year(1800) == False)
# print(is_leap_year(1900) == False)
# print(is_leap_year(2000) == True)
# print(is_leap_year(2023) == False)
# print(is_leap_year(2024) == True)
# print(is_leap_year(2025) == False)

# In the previous exercise, we assumed that the Gregorian calendar has been in continuous use since the year 1. However, the Gregorian calendar wasn't adopted until much later; prior to that, much of the world used the Julian calendar, which observed leap year every 4 years.

# in 1752, England, Ireland, and the British colonies all switched to the Gregorian calendar. Update the function from the previous exercise so it uses the Julian calendar prior to 1752, and the Gregorian calendar starting in 1752.

# def is_leap_year(num):
#     if num < 1752 and num % 4 == 0:
#         return True
#     else:
#         if num % 400 == 0:
#             return True
#         elif num % 100 == 0:
#             return False
#         elif num % 4 == 0:
#             return True
#         else:
#             return False


# These examples should all print True
# print(is_leap_year(1) == False)
# print(is_leap_year(2) == False)
# print(is_leap_year(3) == False)
# print(is_leap_year(4) == True)
# print(is_leap_year(1000) == True)
# print(is_leap_year(1100) == True)
# print(is_leap_year(1200) == True)
# print(is_leap_year(1300) == True)
# print(is_leap_year(1751) == False)
# print(is_leap_year(1752) == True)
# print(is_leap_year(1753) == False)
# print(is_leap_year(1800) == False)
# print(is_leap_year(1900) == False)
# print(is_leap_year(2000) == True)
# print(is_leap_year(2023) == False)
# print(is_leap_year(2024) == True)
# print(is_leap_year(2025) == False)

# Multiples of 3 and 5
# Write a function that computes the sum of all numbers between 1 and some other number, inclusive, that are multiples of 3 or 5. For instance, if the supplied number is 20, the result should be 98 (3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 + 20).

# You may assume that the number passed in is an integer greater than 1.

# These examples should all print True
'''

E:
multisum(20) == 98
(3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 + 20).

D: math

A:
initialize sum variable to 0
iterate over the range from 1 to the argument inclusive
add all numbers to the sum that are divisible by 3 or 5
'''


# def multisum(num):
#     sum_new = 0
#     for number in range(1, num+1):
#         if number % 3 == 0 or number % 5 == 0:
#             sum_new += number
#     return sum_new
# [expression for item in iterable if condition]

# def multisum(num):
#     sum_new = 0

# [sum_new += num for num in range(1, num+1) if num % 3 == 0 or num % 5 == 0]

# return sum_new

# def multisum(num):
#     return sum([number for number in range(1, num + 1) if number % 3 == 0 or number % 5 == 0])


# print(multisum(3) == 3)
# print(multisum(5) == 8)
# print(multisum(10) == 33)
# print(multisum(1000) == 234168)

# Write a function that determines and returns the UTF-16 string value of a string passed in as an argument. The UTF-16 string value is the sum of the UTF-16 values of every character in the string. (You may use ord to determine the UTF-16 value of a character.)

# ExamplesCopy Code
# '''
# -iterate over the string and find out what is the UTF=16 of every char in the string
# -add the value to the result that I'm going to return

# '''
# def utf16_value(s):
#     result = 0
#     for one_character in s:
#         result += ord(one_character)
#     return result


# # # These examples should all print True
# print(utf16_value('Four score') == 984)
# print(utf16_value('Launch School') == 1251)
# print(utf16_value('a') == 97)
# print(utf16_value('') == 0)

# # # The next three lines demonstrate that the code
# # # works with non-ASCII characters from the UTF-16
# # # character set.
# OMEGA = "\u03A9"              # UTF-16 character 'Ω' (omega)
# print(OMEGA)
# print(utf16_value(OMEGA) == 937)
# print(utf16_value(OMEGA + OMEGA + OMEGA) == 2811)

# Welcome Stranger
# Create a function that takes 2 arguments, a list and a dictionary. The list will contain 2 or more elements that, when joined with spaces, will produce a person's name. The dictionary will contain two keys, "title" and "occupation", and the appropriate values. Your function should return a greeting that uses the person's full name, and mentions the person's title.

def greetings(new_list, new_dict):
    name = " ".join(new_list)
    title = new_dict["title"]
    occupation = new_dict["occupation"]

    return f"Hello, {name}! Nice to have a {title} {occupation} around."


greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.