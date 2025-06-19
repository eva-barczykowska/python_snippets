'''Letter Swap
Given a string of words separated by spaces, write a function that swaps the first and last letters of every word.

You may assume that every word contains at least one letter, and that the string will always contain at least one word. You may also assume that each string contains nothing but words and spaces, and that there are no leading, trailing, or repeated spaces.

Problem: Swap first character and last character of each word in a string.

    - input: a string
    - output: a string with swapped characters
    - rules:
        - no empty strings
        - may or may not have spaces
        - no leading or trailing spaces, so don't have to worry about stripping anything

Example: 'Abcde' == 'ebcdA'

Data Structure: Maybe a list for holding? Maybe not.

Algorithm:
    - initialize a empty list
    - split the string into a another list
    - for loop element in list
        - for character in element
            - first letter, slice element[0]
            - last letter, slice element [-1]
            - middle letters, slice element [1:-1]
            - append sliced to the empty list
    - join list to a string
    - return string

'''

# def swap(text):
#     temp_list = []
#     words = text.split(" ")
#     for word in words:
#         if len(word) == 1:
#             temp_list.append(word)
#         else:
#             first_letter = word[0]
#             last_letter = word[-1]
#             middle_letters = word[1:-1]
#             together = last_letter + middle_letters+ first_letter
#             temp_list.append(together)
#
#     sentence = " ".join(temp_list)
#     return sentence

# print(swap('Oh what a wonderful day it is')  == "hO thaw a londerfuw yad ti si")  # True
# print(swap('Abcde') == "ebcdA")            # True
# print(swap('a') == "a")                    # True

#my solution
# -split the string into a list
# - iterate over the list
# - for each word, if the word length is 1, append it to the list as is
#     - else, swap first and last characters
#     - join the list back to a string

def swap(text):
    words = text.split(" ")
    result = []
    for word in words:
        if len(word) == 1:
            result.append(word)
        else:
            result.append(word[-1] + word[1:-1] + word[0])
    return " ".join(result)

print(swap('Oh what a wonderful day it is')  == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True

# Convert a String to a Number
# Write a function that takes a string of digits and returns the appropriate number as an integer. You may not use any of the standard conversion functions available in Python, such as int. Your function should calculate the result by using the characters in the string.

# For now, do not worry about leading + or - signs, nor should you worry about invalid characters; assume all characters are numeric.

# P:
# write a function that takes a str as in input and returns a number
# E:
# DS:list
# A:

# -split the str into a list
# -reverse that list -l[:: -1]
# -iterate over it, change string-number to integers
# -reverse back to how it was
# -join and return


# change of plan
# -init a number to return
# -iterate over that string
# "4321"
# How can I iterate over the string FROM THE END?
# s = "4321"
# for one_char in s[::-1]:
#     print(one_char)
# use ord('4') - ord('0') to get the INTEGER
# --at every stage of iteration use a multiplier
# --init multiplier to 1
# --at every iteration multiply the multiplier by 10
#-- add the created integers together to build the int_to_return

# -when iteration finished, return the number

# thousands - hundreds - tens - ones
# i need length
# len(str) - 4
# how do i build an integer out of these numbers?
# if it is the last number - 1 * number
# if it is 2nd from last - 10 * number
# if it is 3rd form last - 100 * number
# if it is 4th from last - 1000 * number

# multiplier changes!
# on each iteration * 10

# so if the str is '3' - the way to get an integer
# ord('3') is 51
# ord('0') = 48
# 51-3 = 3 # this is amazing!

# c:

# def string_to_integer(str_number):
#     helper = 1
#     multiplier = 1
#     final_num = 0
#
#     for one_char in str_number[::-1]:
#         num = ord(one_char) - ord('0')
#         helper = num * multiplier # 1, 20, 300, 4000
#         final_num += helper
#         multiplier *= 10
#
#     return final_num
#
#
#
# print(string_to_integer("4321") == 4321) # True
# print(string_to_integer("570") == 570)    # True

