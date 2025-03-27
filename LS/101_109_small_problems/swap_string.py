# Letter Swap
# Given a string of words separated by spaces, write a function that swaps the first and last letters of every word.

# You may assume that every word contains at least one letter, and that the string will always contain at least one word. You may also assume that each string contains nothing but words and spaces, and that there are no leading, trailing, or repeated spaces.

# Plan B after plan A failed in a spectacular way!
# strings are NOT MUTABLE!!! in python, I need to do something else
# I need to split the string to build a new string from scratch and then
# save first char to a variable
# save last char to a variable
# save middle to a variable
# build a new word from scratch and add it to the final list
# join the final list into a string
# return it


def swap(string):
    final_string = []
    string = string.split(" ")
    for word in string:
        if len(word) < 2:
            final_string.append(word)
        else:
            first_char = word[0]
            last_char = word[-1]
            middle = word[1: -1]
            new_word = last_char + middle + first_char
            final_string.append(new_word)

    return " ".join(final_string)


print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")  # True
print(swap('a') == "a")  # True
