'''Write a function that takes a list of strings and returns a list of the same string values,
but with all vowels (a, e, i, o, u) removed.
P:
-function takes a string
-function returns string but with vowels removed
-capital / lowercase letters present
-empty str present

E:

A:
-init new list
-iterate over the list and consider each string
-if the letter is not a vowel, add it to the new_list
-return the new_list

R:
'''

def remove_vowels(my_list_of_strings):
    new_list = []
    # word = [] # defined at the wrong level here
    vowels = 'AEIOUaeoui'
    for one_string in my_list_of_strings:
        word = '' #build new word each time from scratch
        for one_letter in one_string:
                if one_letter not in vowels:
                    word += one_letter
        new_list.append(word)
    return new_list


# All of these examples should print True
original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)        # True

#LS

def strip_vowels(word):
    VOWELS = 'aeiouAEIOU'
    no_vowels = [char for char in word if char not in VOWELS]
    return ''.join(no_vowels)

def remove_vowels(string_list):
    return [strip_vowels(text) for text in string_list]

original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)        # True
