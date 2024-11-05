# Bannerizer

# Write a function that takes a short line of text and prints it within a box.

# +--------------------------------------------+

# |                                            |

# | To boldly go where no one has gone before. |

# |                                            |

# +--------------------------------------------+

# def banner(string):
#     length = len(string) + 2
#     print(f"+{length * '-'}+")
#     print(f"|{' ' * length}|")
#     print(f"| {string} |")
#     print(f"|{' ' * length}|")
#     print(f"+{length * '-'}+")

# banner('hello')
# banner("To boldly go where no one has gone before.")

"""
Strings Strings
Write a function that takes one argument, a positive integer, and returns a string of alternating '1's and '0's,
always starting with a '1'. The length of the string should match the given integer.


PEDAC
-i have an integer
-replace each character with 1 and 0, start always with 1
-iterate over the range of numbers, starting from 0, ending with argument - 1
-if the integer is even, add 1 to the string
-if int is odd, concatenate 0 to the string
"""


# def stringy(number):
#     result_string = ''
#     print(id(result_string))
#     for num in range(0, number):
#         if num % 2 == 0:
#             result_string += '1'
#         else:
#             result_string += '0'
#     print(id(result_string))
#     return result_string

# print(stringy(6) == "101010")           # True
# print(stringy(9) == "101010101")        # True
# print(stringy(4) == "1010")             # True
# print(stringy(7) == "1010101")          # True

# Right Triangles
# Write a function that takes a positive integer, n, as an argument and prints a right triangle whose sides
# each have n stars. The hypotenuse of the triangle (the diagonal side in the images below)
# should have one end at the lower-left of the triangle, and the other end at the upper-right.

# def triangle(number):
#     for num in range(1, number+1):
#         print(f"{' ' * (number-num)}{'*' * num}")


# triangle(5)
# triangle(9)

# #     *
# #    **
# #   ***
# #  ****
# # *****

#      *
#     **
#    ***
#   ****
#  *****

# Madlibs
# Madlibs is a simple game where you create a story template with "blanks" for words. You, or another player,
# then construct a list of words and place them into the story, creating an often silly or funny story as a result.

# Create a simple madlib program that prompts for a noun, a verb, an adverb, and an adjective, and injects them into
# a story that you create.

# Enter a noun: dog
# Enter a verb: walk
# Enter an adjective: blue
# Enter an adverb: quickly

# n = input("Please enter a noun\n")
# # n = input("Please enter a noun: ")
# v = input("Please enter a verb\n")
# adv = input("Please enter a adverb\n")
# adj = input("Please enter a adjective\n")

# print(f"A {adj} {n} {v} {adv}")

# Double Doubles
# A double number is an even-length number whose left-side digits are exactly the same as its right-side digits.
# For example, 44, 3333, 103103, and 7676 are all double numbers, whereas 444, 334433, and 107 are not.

# Write a function that returns the number provided as an argument multiplied by two, unless the argument is
# a double number. If the argument is a double number, return the double number as-is.

# G: intake a number and check to see if it's an even length number
# input: integer
# output: integer

# Rules: double the number unless its an even length number whose left side digits are exactly the same as
# its right side digits
# E:
# 103103 -> 103 is the same as 103
# D: num -> array
# A: - if the number is even:
# initialize a new_list made from the integers of the input argument
# break the number into two sides
# left side is a slice from index 0 to the length of number divided by 2
# right side is a slice from index length of number divided by 2 to number's length
# if these sides are exactly equal,
# return the original number
# otherwise return the number multiplied by 2
# - otherwise return the number multiplied by 2

# MY PEDAC
# -is it even length?
# -if yes split it in two halves
# -are the nums on the left and right sides the same?
# -then return the original number
#
# -otherwise return the number multiplied by 2

def twice(number):
    even_length = len(str(number)) % 2 == 0

    if even_length:
        left_side = str(number)[:len(str(number)) // 2]
        right_side = str(number)[len(str(number)) // 2:]
        if left_side == right_side:
            return number
        else:
            return number * 2
    else:
        return number * 2


print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # True
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)              # True
print(twice(10341034) == 10341034)
