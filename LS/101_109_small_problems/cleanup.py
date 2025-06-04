#Given a string that consists of some words and an assortment of non-alphabetic characters, write a function that returns that string with all of the non-alphabetic characters replaced by spaces. If one or more non-alphabetic characters occur in a row, you should only have one space in the result (i.e., the result string should never have consecutive spaces).

#Problem
# - input: string, has nonalpha characters
# - output: string with nonalpha characters replaced with spaces

#explicit rules:
#- no consecutive spaces!

# example: "---what's my +*& line?" Notice the 3 ---

# data struture.
# - no collection, rewriting to a new string, probably

#algorithm
# - empty string created
# = for loop to iterate over the first string
# - check isalpha.
# - if is alpha, add to the empty string
# - if is not alpha, it needs to add a space to the empty string
# if more than two non alphas, pass?
# if more than two non alphas,

# def clean_up(string):
#     cleaned_string = ''
#     for i, char in enumerate(string):
#         if char.isalpha():
#             cleaned_string += char
#         elif i == 0 or cleaned_string[-1] != ' ':
#             cleaned_string += ' '
#
#
#     return cleaned_string
#
# print(clean_up("---what's my +*& line?") == " what s my line ")
# # True
# print(clean_up("Hi Ewa!$") == "Hi Ewa ") #True


# again:

# - iterate over the string
# - look at each character
# - if it's alphabet, add it to the result string
# - if it's not alphabet, check if the result string ends with a space

# def clean_up(string):
#     cleaned_string = ''
#     for char in string:
#         if char.isalpha():
#             cleaned_string += char
#         elif cleaned_string and cleaned_string[-1]!='':
#             cleaned_string +=''
#     return cleaned_string

# print(clean_up("---what's my +*& line?") == " what s my line ")
# # True
# print(clean_up("Hi Ewa!$") == "Hi Ewa ") #True


# print('---')
#
# print(clean_up("---what's my +*& line?") == " what s my line ")
# # True
# print(clean_up("Hi Ewa!$") == "Hi Ewa ") #True

# overal theory:
# iterate over the string and build a new one char by char
#details:
# - look at each character
# - if it's alphabet char, add it to the result string
# - if it's not alphabet
# --check if str is empty, if it is, add space
# -- or check if str[-1] is a space, then do NOT add this character
# --else if it is an alphabetic char, add this char to the str

def clean_up(s):
    result = ''
    for char in s:
        if not char.isalpha():
            if not result:
                result += ' '
            elif result[-1] != ' ':
                result += ' '
        else:
            result += char
    print(result)
    return result

print(clean_up("---what's my +*& line?") == " what s my line ")# True
print(clean_up("Hi Ewa!$") == "Hi Ewa ") #True

#refactor
def clean_up(s):
    result = ''

    for char in s:
        if not char.isalpha():
            if not result or result[-1] != ' ':
                result += ' '
        else:
            result += char
    print(result)
    return result

print(clean_up("---what's my +*& line?") == " what s my line ")# True
print(clean_up("Hi Ewa!$") == "Hi Ewa ") #True