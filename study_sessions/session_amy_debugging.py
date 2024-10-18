# You come across the following code. What errors does it raise for the given examples and what exactly do the error messages mean?

# def find_first_nonzero_among(numbers):
#     for n in numbers:
#         if n != 0:
#             return n

# print(find_first_nonzero_among([0, 0, 1, 0, 2, 0]))
# print(find_first_nonzero_among(1))
# print(find_first_nonzero_among([0, 4, 1, 0, 2, 0]))

# def find_first_nonzero_among(*numbers):
#     print(numbers)
#     for n in numbers:
#         if n != 0:
#             return n

# print(find_first_nonzero_among(0, 0, 1, 0, 2, 0))
# print(find_first_nonzero_among(1))
# print(find_first_nonzero_among(0, 4, 1, 0, 2, 0))

# Weather Forecast
# Our predict_weather function should output a message indicating whether a sunny or cloudy day lies ahead. However, the output is the same every time the function is invoked. Why? Fix the code so that it behaves as expected.

# import random

# def predict_weather():

#     sunshine = random.choice([True, False])

#     if sunshine:
#         print("Today's weather will be sunny!")
#     else:
#         print("Today's weather will be cloudy!")

# print(predict_weather())


# Multiply By Five
# When the user inputs 10, we expect the program to print The result is 50!, but that's not the output we see. Why not?

# def multiply_by_five(n):
#     return int(n) * 5

# print("Hello! Which number would you like to multiply by 5?")
# number = input()

# print(f"The result is {multiply_by_five(number)}!")

# Magdalena has just adopted a new pet! She wants to add her new dog, Bowser, to the pets dictionary. After doing so, she realizes that her dogs Sparky and Fido have been mistakenly removed. Help Magdalena fix her code so that all three of her dogs' names will be associated with the key 'dog' in the pets dictionary.

# pets = { 'cat': 'pepe', 'dog': ['sparky', 'fido'], 'fish': 'oscar' }

# # pets['dog'] = 'bowser'
# pets['dog'].append('bowser')

# print(pets)
# # Output: {'cat': 'pepe', 'dog': 'bowser', 'fish': 'oscar'}

# Confucius Says
# You want to have a small script delivering motivational quotes, but with the following code you run into a very common error message: TypeError: can only concatenate str (not "NoneType") to str. What is the problem and how can you fix it?
# import random

# def get_quote(person):
#     if person == 'Yoda':
#         return 'Do. Or do not. There is no try.'
#     if person == 'Confucius':
#         return 'I hear and I forget. I see and I remember. I do and I understand.'
#     if person == 'Einstein':
#         return 'Do not worry about your difficulties in Mathematics. I can assure you mine are still greater.'

# person = random.choice(['Confucius', 'Yoda', 'Einstein'])
# print(f"{person} says:")
# print(f"\'{get_quote(person)}\'")

# You want to add the numbers from 1 to 5 to a list, but the code below is not producing the expected result. How can you fix it?

# numbers = []

# for i in range(1, 6):
#     numbers.append(i)

# print(numbers)


# Dictionary Access
# You are trying to access a value in a dictionary, but the code is giving you an error. Can you change line 3 so that it prints "Unknown" instead of raising an error?

# info = {'name': 'Srdjan', 'age': 38}

# # print(info['city'])

# print(info.get('city', 'Unknown'))

# Matrix
# We wanted to create a matrix 3x3 so we could use it to build a Tic-Tac-Toe game. However, we encountered an issue, as whenever we change a value in one nested list, all nested lists are affected. Can you fix the code?


sub_list = ["-", "-", "-"]
matrix = []

for _ in range(3):
    matrix.append(sub_list.copy())

matrix[0][0] = "X"
print(matrix) # [['X', '-', '-'], ['X', '-', '-'], ['X', '-', '-']]
matrix[1][1] = 'O'
print(matrix)