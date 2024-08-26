# Write a function that checks whether a string starts with a specific prefix.

# def starts_with(word, prefix):
#     if word.startswith(prefix):
#         return True
#     else:
#         return False

# print(starts_with("launch", "la"))   # True
# print(starts_with("school", "sah"))  # False
# print(starts_with("school", "sch"))  # True

# Write a function that counts the number of occurrences of a substring in a string.

# def count_substrings(string, substring):
#     return string.count(substring)


# print(count_substrings("lemon lemon lemon", "lemon")) # 3
# print(count_substrings("laLAlaLA", "la")) # 2
# print(count_substrings("launch", "uno")) # 0

# Write a function that returns the first element of a list provided as an argument. For example:
# def first(list_of_items):
#     return list_of_items[0]

# print(first(['Earth', 'Moon', 'Mars']))  # Earth

# Write a function that returns the last element of a list provided as an argument. For example:

# def last(array):
#     return array[-1]

# print(last(['Earth', 'Moon', 'Mars']))  # Mars

# We are given the following list of energy sources.


# energy = ['fossil', 'solar', 'wind', 'tidal', 'fusion']
# energy.remove('fossil')
# energy.extend(['geothermal', 'hi']) #extend
# print(energy)

# Write some code to remove 'fossil' from the list, then add 'geothermal' to the end of the list.

# Split the string alphabet into a list of characters.
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# alpha_list = list(alphabet)
# print(alpha_list)

# alphabet = 'abcdefghijklmnopqrstuvwxyz hello'
# alpha_list = alphabet.split(' ')
# print(alpha_list)

# # Count the number of elements in scores that are 100 or above.
# scores = [96, 47, 113, 89, 100, 102]
# result = 0
# for number in scores:
#     if number >= 100:
#         result += 1

# print(result)

# You've been given a list of vocabulary words grouped into sub-lists, by meaning. This is a two-dimensional list or
# a nested list. Write some code that iterates through and prints all the words, one per line.

# vocabulary = [
#     ['happy', 'cheerful', 'merry', 'glad'],
#     ['tired', 'sleepy', 'fatigued', 'drained'],
#     ['excited', 'eager', 'enthused', 'animated'],
# ]

# happy
# cheerful
# merry
# glad
# tired
# sleepy
# etc...
# HINT: You will need nested loops to iterate through all of the words.

# for subarray in vocabulary:
#     for word in subarray:
#         print(word)

# Predict the output of the code shown below. When you run the code, do you see what you expected? Why or why not?

# list1 = [2, 6, 4]
# list2 = [2, 6, 4]
#
# print(list1 == list2)  # compares value, True!
# print(list1 is list2)  # compares if the same object, False
#
# s1 = "ewa"
# s2 = "ewa"
#
# print(s1 == s2)  # True
# print(s1 is s2)  # True


# Multiply
# Examine the function invocation below. Write the function multiply, such that it accepts two arguments and returns the product of its arguments. You may assume that the function arguments will always be numbers.

# def multiply(num1, num2):
#     return num1 * num2

# print(multiply(12, 4))      # 48

# Print Quote
# Write a function that prints Bruce Eckel's quote 'Python is executable pseudocode.'. What is the return value of the function?

# def bruce_eckel_quote():
#    print('Python is executable pseudocode.')

# print(bruce_eckel_quote())

# Since the function has no return statement, the return value of our function is None.

# Cite the Author
# Let's generalize the function from the previous exercise. Implement a function named cite that takes two string arguments: the author of the quote and what they said. It then prints the quote, as shown below.

# def cite(str1, str2):
#     return f"{str1} said: {str2}"

# print(cite('Bruce Eckel', 'Python is executable pseudocode.'))
# Bruce Eckel said: "Python is executable pseudocode."

# Squared Number
# Write a function that accepts a single argument, a number, and returns the result of multiplying its argument by an exponent of 2 (also known as squaring the number or raising the number to the power of 2).

# def squared_number(num):
#     return num**2

# print(squared_number(3))   # 9

# Display Division
# Without running the following code, determine what it will print:

# def multiples_of_three():
#     divisor = 1

#     for dividend in range(3, 31, 3):
#         print(f'{dividend} / {divisor} = 3')
#         divisor += 1

# multiples_of_three()


# range(3, 31, 3):
# [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

# Three-way Comparison
# Write a function that compares the length of two strings. It should return -1 if the first string is shorter, 1 if the second string is shorter, and 0 if they're of equal length. For example:

# def compare_by_length(first, second):
#     if len(first) < len(second):
#         return -1
#     elif len(first) > len(second):
#         return 1
#     else:
#         return 0

# print(compare_by_length('patience', 'perseverance')) # -1
# print(compare_by_length('strength', 'dignity'))      #  1
# print(compare_by_length('humor', 'grace'))          #  0

# Transformation
# Use Python's string methods on the string 'Captain Ruby' to create a string with the value 'Captain Python'.

# captain = 'Captain Ruby'
# print(captain[:7], "Python")
# # captain[9:] = 'Python'
# # print(captain)


# # LS solution
# first_8 = 'Captain Ruby'[:8]
# new_str = first_8 + 'Python'
# print(new_str)      # Captain Python

# new_str = 'Captain Ruby'.replace('Ruby', 'Python')
# print(new_str)      # Captain Python

# Internationalization 1
# Use Python's control structures to create a function that takes an ISO 639-1 language code and returns a greeting in that language. You can take the examples below or add whatever languages you like.

# def greet(iso):
#     if iso == 'en':
#         return 'Hi!'
#     elif iso == 'fr':
#         return 'Salut!'
#     elif iso == 'pt':
#         return 'Olá!'
#     elif iso == 'de':
#         return 'Hallo!'
#     elif iso == 'sv':
#         return 'Hej!'
#     elif iso == 'af':
#         return 'Haai!'
#
#
# print(greet('en'))  # Hi!
# print(greet('fr'))  # Salut!
# print(greet('pt'))  # Olá!
# print(greet('de'))  # Hallo!
# print(greet('sv'))  # Hej!
# print(greet('af'))  # Haai!
