# """
# Write a function that takes a positive integer as an argument and returns that number with its digits reversed.

# P:
# -function takes an int, positive
# -funtion returns the same int with its digits reversed

# E:
# print(reverse_number(12345) == 54321)   # True

# print(reverse_number(12213) == 31221)   # True

# print(reverse_number(456) == 654)       # True

# print(reverse_number(1) == 1)           # True
# -if it's just 1 int, return the same int

# print(reverse_number(12000) == 21)      # True
# - remove prefix zeros if any


# A:
# -if it's just 1 int, return it
# -turn arg into a str
# -reverse it
# -remove zeros if any
# -turn back into int
# -return it

# C:
# """

# def reverse_number(int_argument):
#     # converted_to_str = str(int_argument)
#     # converted_to_str = list(reversed(converted_to_str))
#     # if len(converted_to_str) == 1:
#     #     return int_argument
#     # else:
#     #     return int(''.join(converted_to_str))

#     return int(str(int_argument)[::-1])





# print(reverse_number(12345) == 54321)   # True
# print(reverse_number(12213) == 31221)   # True
# print(reverse_number(456) == 654)       # True
# print(reverse_number(1) == 1)           # True
# print(reverse_number(12000) == 21)      # True
[]
'''How Long Are You?
Write a function that takes a string as an argument and returns a list that contains every word from the string, with each word followed by a space and the word's length. If the argument is an empty string or if no argument is passed, the function should return an empty list.

You may assume that every pair of words in the string will be separated by a single space.

Problem: return a string with each element of the string's length's counted along with the string itself

input: string, featuring words with spaces.
output: a list, each element is the word with the count of the word
special exceptions: punctuation IS counted

Example: "cow sheep chicken". Cow => 3, sheep => 5 chicken ==> 7

Data structures: A list

Algorithm: iterate over a split string, capture the length, and then append an f string of element plus length to an empty list
    return empty list

'''

# def word_lengths(string=[]):

#     if not string:
#         return []

#     result = []
#     for word in string.split():
#         length = len(word)
#         result.append(f"{word} {length}")
#     return result

# # All of these examples should print True
# words = 'cow sheep chicken'
# expected_result = ['cow 3', 'sheep 5', 'chicken 7']
# print(word_lengths(words) == expected_result)        # True

# words = 'baseball hot dogs and apple pie'
# expected_result = ['baseball 8', 'hot 3', 'dogs 4',
#                    'and 3', 'apple 5', 'pie 3']
# print(word_lengths(words) == expected_result)        # True

# words = "It ain't easy, is it?"
# expected_result = ['It 2', "ain't 5", 'easy, 5',
#                    'is 2', 'it? 3']
# print(word_lengths(words) == expected_result)        # True

# big_word = 'Supercalifragilisticexpialidocious'
# print(word_lengths(big_word) == [f'{big_word} 34'])  # True

# print(word_lengths('') == [])                        # True
# print(word_lengths() == [])                          # True

# Rotation (Part 1)
# Write a function that rotates a list by moving the first element to the end of the list. Do not modify the original list; return a new list instead.

# If the input is an empty list, return an empty list.
# If the input is not a list, return None.
# Review the test cases below, then implement the solution accordingly.

# All of these examples should print True

""" 
Problem: take a list, and then splice out the first element, switching, these elements. Output a new list! 

    exceptions: no list returns None and empty list returns empty list.

Examples:  7, 3, 5, 2, 9, 1 ==> 3, 5, 2, 9, 1, 7. 

a b c => b c a

Data structure: list

Algorithm:

splice out the first element
rebuild a new list with rest of list + first element
return list

"""

def rotate_list(lst):


    if not isinstance(lst, list):
        return None

    # elif len(lst) == 0:
    #     return []

    else:
        first = lst[:1]
        rest = lst[1:]

        return rest + first

print(rotate_list([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7])
print(rotate_list(['a', 'b', 'c']) == ['b', 'c', 'a'])
print(rotate_list(['a']) == ['a'])
print(rotate_list([1, 'a', 3, 'c']) == ['a', 3, 'c', 1])
print(rotate_list([{'a': 2}, [1, 2], 3]) == [[1, 2], 3, {'a': 2}])
print(rotate_list([]) == [])

# return `None` if the argument is not a list
print(rotate_list(None) == None)
print(rotate_list(1) == None)

# the input list is not mutated
lst = [1, 2, 3, 4]
print(rotate_list(lst) == [2, 3, 4, 1])
print(lst == [1, 2, 3, 4])



# def rotate_list(lst):

#     print(f"Lst = {lst}")
#     if not lst or None or isinstance(lst, int): #!
#         return None

#     elif lst == []:
#         return []

#     else:
#         first = lst[:1]
#         rest = lst[1:]

#         return rest + first