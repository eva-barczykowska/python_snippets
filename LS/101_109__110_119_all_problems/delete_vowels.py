
# Delete Vowels
# Write a function that takes a list of strings and returns a list of the same string values, but with all vowels (a, e, i, o, u) removed.

# def remove_vowels(text):
#     vowels = 'aeiouAEIOU'
#     new_text = ""
#     result = []
#     for char in text: # 1 level of iteration is missing
#         if char not in vowels:
#             new_text += char
#         else:
#             continue
#         result.append(new_text) # wrong place to append the new_text, vowels not removed coz it checks 1st char only!!!
         # but we are appending here hoping for the last char of each consonant-only word
#     print(result)
#     return result

# def remove_vowels(text):
#     vowels = 'aeiouAEIOU'
#     new_text = ""
#     result = []
#     for char in text: # 1 level of iteration is missing
#         if char not in vowels:
#             # print(char) #I called it char and confused myself, it is actually a whole word/string, element or one_word would be more acurate
#             new_text += char
#         else:
#             continue
#         result.append(new_text) # wrong place to append the new_text, vowels not removed coz it checks 1st char only!!!
#         # but we are appending here hoping for the last char of each consonant-only word
#     return result

# All of these examples should print True
# original = ['abcdefghijklmnopqrstuvwxyz']
# expected = ['bcdfghjklmnpqrstvwxyz']
# print(remove_vowels(original) == expected)        # True
#
# original = ['green', 'YELLOW', 'black', 'white']
# expected = ['grn', 'YLLW', 'blck', 'wht']
# print(remove_vowels(original) == expected)        # True
#
# original = ['ABC', 'AEIOU', 'XYZ']
# expected = ['BC', '', 'XYZ']
# print(remove_vowels(original) == expected)        # True


# def remove_vowels(my_list):
#     vowels = 'aeiouAEIOU'
#     result = []
#     word = ''
#     for a_word in my_list: # iterate over each word in the list
#         for a_char in a_word: # within this word, iterate over each character
#             if a_char not in vowels: # check if the character is not a vowel
#                 word += a_char # if not, add it to the target word
#                 print(word)
#     result.append(word) # append target word but here, wovels get removed BUT words are sticking together
#     # word should be initialized somewhere else within the loop to get to "" for every new word. Where exactly?
#     return result

# def remove_vowels(my_list):
#     vowels = 'aeiouAEIOU'
#     result = []
#     word = ''
#     for a_word in my_list: # iterate over each word in the list
#         for a_char in a_word: # within this word, iterate over each character
#             if a_char not in vowels: # check if the character is not a vowel
#                 word += a_char # if not, add it to the target word
#                 print(word)
#         result.append(word)
#         word = ''# this works but - how to initialize word to "" for every new word?
#     # word should be initialized somewhere else within the loop to get to "" for every new word. Where exactly?
#     return result

def remove_vowels(my_list):
    vowels = 'aeiouAEIOU'
    result = []
    for a_word in my_list: # iterate over each word in the list
        new_word = '' # initialize word to "" for every new word.
        for a_char in a_word: # within this word, iterate over each character
            if a_char not in vowels: # check if the character is not a vowel
                new_word += a_char # if not, add it to the target word
        result.append(new_word)
    return result

# def remove_vowels(my_list):
#     vowels = 'aeiouAEIOU'
#     result = []
#     for a_word in my_list:
#         temp = []
#         for a_char in a_word:
#             if a_char not in vowels:
#                 temp.append(a_char)
#         element = "".join(temp)
#         result.append(element)
#
#     return result
#
#
# # All of these examples should print True
original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)        # True
#
# def remove_vowels(my_list):
#     vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
#     result = []
#     for element in my_list:
#         temp = []
#         for char in element:
#             if char not in vowels:
#                 temp.append(char)
#         element = "".join(temp)
#         result.append(element)
#     return result
#
# original = ['abcdefghijklmnopqrstuvwxyz']
# expected = ['bcdfghjklmnpqrstvwxyz']
# print(remove_vowels(original) == expected)        # True
#
# original = ['green', 'YELLOW', 'black', 'white']
# expected = ['grn', 'YLLW', 'blck', 'wht']
# print(remove_vowels(original) == expected)        # True
#
# original = ['ABC', 'AEIOU', 'XYZ']
# expected = ['BC', '', 'XYZ']
# print(remove_vowels(original) == expected)        # True


