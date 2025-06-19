"""
Given a string of words separated by spaces, write a function that swaps the first and last
letters of every word.

You may assume that every word contains at least one letter, and that the string will always
contain at least one word. You may also assume that each string contains nothing but words
and spaces, and that there are no leading, trailing, or repeated spaces.

P:
input: a string, at least 1 letter in each word, only letters and spaces, no leading or trailng spaces, or repeated spaces
output: a string with swapped characters
rules:
    - no empty strings
    - may or may not have spaces
    - no leading or trailing spaces, so don't have to worry about stripping anything
    - no consecutive spaces
    - no case sensitivity to be considered

A:
split string argument into list of words
iterate over each word in the list
if a word is only 1 letter, add it to the result list as it is
else
construct a new word by swapping first and last characters
construct a new word by swapping first and last characters
add last char + middle + first char to form a new word
add that new word to the result list

join and return the result list as a string
"""

def swap(s):
    result = []

    words = s.split()
    for word in words:
        if len(word) == 1:
            result.append(word)
        else:
            result.append(word[-1] + word[1:-1] + word[0]) # remember that in word[1:-1], -1 is EXCLUSIVE so element at index -1 WILL NOT be included in the slice

    return ' '.join(result)

print(swap('Oh what a wonderful day it is') == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True