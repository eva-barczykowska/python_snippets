#Madlibs is a simple game where you create a story template with "blanks" for words. You, or another player, then construct a list of words and place them into the story, creating an often silly or funny story as a result.

#Create a simple madlib program that prompts for a noun, a verb, an adverb, and an adjective, and injects them into a story that you create.


# noun = input("Give me a noun:  ")
# noun2 = input("Give me another noun: ")
# verb = input("Give me a verb: ")
# adjective = input("Give me an adjective: ")
# adjective2 = input("Give me another adjective: ")
# adverb = input("Give me a an adverb: ")

# print(f"""

# Do you {verb} your {adjective} {noun} {adverb}? That's {adjective2}!
# The {adjective} {noun} {verb} {adverb} over the {adjective2} {noun2}.
# The {noun} {adverb} {verb} up to Joe's {adjective} turtle.
#       """)


#A double number is an even-length number whose left-side digits are exactly the same as its right-side digits. For example, 44, 3333, 103103, and 7676 are all double numbers, whereas 444, 334433, and 107 are not.

#Write a function that returns the number provided as an argument multiplied by two, unless the argument is a double number. If the argument is a double number, return the double number as-is.

# PEDAC
# P
# -44, 3333, 103103 - double numbers
# left-side digis are EXACTLY the same as right side digits
# -107, 334433 - are NOT double numbers
# -function finds out if the number is a double number
# -if yes, it returns that same num (argument)
# -if no, it returns the number dobuble




# print(twice(37) == 74)                  # True
# print(twice(44) == 44)                  # True
# print(twice(334433) == 668866)          # True
# print(twice(444) == 888)                # True
# print(twice(107) == 214)                # True
# print(twice(103103) == 103103)          # True
# print(twice(3333) == 3333)              # True
# print(twice(7676) == 7676)              # True

# Data Structures
# -Integer, String, List

# Algorithm
# - change the int to a string and save it to a variable
# - find out the size
# -split this str into 2 (slice), str1, str2
# - check if they are equal ==
# - if they are equal, return the argument
# -else, double the argument and return it

#Code
# Refactor

def twice(num):
    string = str(num)
    length = len(string)
    half = length // 2
    str1, str2 = string[0:half], string[half:]

    if str1 == str2:
        return num
    else:
        return num * 2

print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # True
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)              # True

#Write a function that determines the mean (average) of the three scores passed to it, and returns the letter associated with that grade.

#Numerical score letter grade list:

#90 <= score <= 100: 'A'
#80 <= score < 90: 'B'
#70 <= score < 80: 'C'
#60 <= score < 70: 'D'
#0 <= score < 60: 'F'
#Tested values are all between 0 and 100. There is no need to check for negative values or values greater than 100.#

# Problem:
# input is three integers
# output A letter grade, A B C D E F


#Example:
# 3 integers passed to a function get_grade
# Checks against if else statements?

#Data Structure:
# integers
# strings
# no collections - not storing for future look up

#Algorithm
# gross_score is equal to the sum of the three integers
# average the gross score
# match the score to 90 and up, 80 to 90, 70 to 80, 60 to 70
# and below 60

# def get_grade(grade1, grade2, grade3):
#
#     gross_score = grade1 + grade2 + grade3
#     average = gross_score / 3
#
#     if average >= 90:
#         return "A"
#     elif average >= 80:
#         return "B"
#     elif average >= 70:
#         return "C"
#     elif average >= 60:
#         return "D"
#     else:
#         return "F"
#
# print(get_grade(95, 90, 93) == "A")      # True
# print(get_grade(50, 50, 95) == "D")      # True