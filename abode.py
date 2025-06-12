
"""
Alphabet Symmetry

Consider the word "abode".
The letter `a` is in position 1 and `b` is in position 2.
In the alphabet, `a` and `b` are also in positions 1 and 2.

The letters `d` and `e` in "abode" occupy the positions they would occupy in the alphabet, which are positions 4 and 5.

Given an array of words, return an array of the number of letters that occupy their positions in the alphabet for each word. For example,

solve(["abode","ABc","xyzD"]) // [4, 3, 1]

Input will consist of alphabetic characters, both uppercase and lowercase. No spaces.


Problem: in a given string, which is an element in a list, find if the letter position meets its alphabetic position, if so, count how many letters meet the requirement, return the number count in a list

    - input: list, of strings
    - output: list, of integer
    - explicit: make it case insensitive
    - explicit: don't have to worry about spaces

Example: ["abode","ABc","xyzD"]) ==> [4, 3, 1]

Data Structure: Dictionary

Algorithm:
    - initialize empty list, result
    - initialize a dictionary carrying letter and position number
    - counter, integer set to 0
    - loop over element in list
        - loop over the characters in the element,
        for character in range(1, len(list)+1)
            - if character[i+1] == dictionary.get(character)
                - increment count by 1
            - reset count back to 0
            - append list with count
    - return result list

"""
# numbers = list(range(0, 27))
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# alphabet = dict(zip(numbers,letters))
# # print(alphabet)

# def solve(lst, alphabet):

#     result = []
#     count = 0


#     for element in lst:
#         for index, character in enumerate(element.casefold()):
#             if character == alphabet.get(index):
#                 count += 1
#         result.append(count)
#         count = 0

#     return result



# print(solve(["abode","ABc","xyzD"], alphabet) == [4,3,1]) # True
# print(solve(["abide","ABc","xyz"], alphabet) == [4,3,0]) # True
# print(solve(["IAMDEFANDJKL","thedefgh","xyzDEFghijabc"], alphabet) == [6,5,7]) # True
# print(solve(["encode","abc","xyzD","ABmD"], alphabet) == [1, 3, 1, 3]) # True

# with count error
# the error in the algorithm was that count was not reset back to 0 after each character in the string(in one word) was checked.
# def solve(lst, alphabet):

#     result = []
#     count = 0

#     for element in lst:
#         for index, character in enumerate(element.casefold()):
#             if character == alphabet.get(index):
#         result.append(count)

#     return result



# print(solve(["abode","ABc","xyzD"], alphabet) == [4,3,1]) # True
# print(solve(["abide","ABc","xyz"], alphabet) == [4,3,0]) # True
# print(solve(["IAMDEFANDJKL","thedefgh","xyzDEFghijabc"], alphabet) == [6,5,7]) # True
# print(solve(["encode","abc","xyzD","ABmD"], alphabet) == [1, 3, 1, 3]) # True

# abc = {"a": 1,
#     "b": 2,
#     "c": 3,
#     "d": 4,
#     "e": 5,
#     "f": 6,
#     "g": 7,
#     "h": 8,
#     "i": 9,
#     "j": 10,
#     "k": 11,
#     "l": 12,
#     "m": 13,
#     "n": 14,
#     "o": 15,
#     "p": 16,
#     "q": 17,
#     "r": 18,
#     "s": 19,
#     "t": 20,
#     "u": 21,
#     "v": 22,
#     "w": 23,
#     "x": 24,
#     "y": 25,
#     "z": 26
#     }

# A:
# 1. count agreement letter at index vs letter in alphabet (but use dictionary where a is index 0) -- helper method
# -loop over a word
# -for a char in the word
# -calculate agreemnt using the reference alphabet and return it (one integer)
# lowcase the chars!

# 2. main method
# -initialize result
# -iterate over each word
# -for each word call the helper method
# -append the return value of the helper method to the result
# -return the list result


numbers = list(range(0, 27))
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet = dict(zip(numbers,letters))

def calculate(word, alphabet):
    counter = 0
    for index, char in enumerate(word.casefold()):
        if char == alphabet.get(index):
            counter += 1
    return counter

# print(calculate("abode", alphabet))  # lesson learnt -> test ALL words, not only the first

def solve(lst, alphabet):
    result = []

    for word in lst:
        result.append(calculate(word, alphabet))

    return result

print(solve(["abode","ABc","xyzD"], alphabet) == [4,3,1]) # True
print(solve(["abide","ABc","xyz"], alphabet) == [4,3,0]) # True
print(solve(["IAMDEFANDJKL","thedefgh","xyzDEFghijabc"], alphabet) == [6,5,7]) # True
print(solve(["encode","abc","xyzD","ABmD"], alphabet) == [1, 3, 1, 3]) # True

print('------')
# keep the reference alphabet in 1 method


def calculate(word):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alphabet = dict(zip(list(range(0, 27)),letters))

    counter = 0
    for index, char in enumerate(word.casefold()):
        if char == alphabet.get(index):
            counter += 1
    return counter

# print(calculate("abode", alphabet))  # lesson learnt -> test ALL words, not only the first

def solve(lst):
    result = []

    for word in lst:
        result.append(calculate(word))

    return result

print(solve(["abode","ABc","xyzD"]) == [4,3,1]) # True
print(solve(["abide","ABc","xyz"]) == [4,3,0]) # True
print(solve(["IAMDEFANDJKL","thedefgh","xyzDEFghijabc"]) == [6,5,7]) # True
print(solve(["encode","abc","xyzD","ABmD"]) == [1, 3, 1, 3]) # True

#even shorter

import string
def calculate(word):
    letters =  str.ascii_lowercase # could be also string.ascii_uppercase for A, B, C....
    alphabet = dict(zip(list(range(0, 27)),letters))

    counter = 0
    for index, char in enumerate(word.casefold()):
        if char == alphabet.get(index):
            counter += 1
    return counter

# print(calculate("abode", alphabet))  # lesson learnt -> test ALL words, not only the first

def solve(lst):
    result = []

    for word in lst:
        result.append(calculate(word))

    return result

print(solve(["abode","ABc","xyzD"]) == [4,3,1]) # True
print(solve(["abide","ABc","xyz"]) == [4,3,0]) # True
print(solve(["IAMDEFANDJKL","thedefgh","xyzDEFghijabc"]) == [6,5,7]) # True
print(solve(["encode","abc","xyzD","ABmD"]) == [1, 3, 1, 3]) # True










