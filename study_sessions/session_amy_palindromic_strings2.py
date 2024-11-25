# Write a program that solicits six (6) numbers from the user and prints a message that describes whether the sixth number appears among the first five.

# Example 1Copy Code
# Enter the 1st number: 25
# Enter the 2nd number: 15
# Enter the 3rd number: 20
# Enter the 4th number: 17
# Enter the 5th number: 23
# Enter the last number: 17

# 17 is in 25,15,20,17,23.
# Example 2Copy Code
# Enter the 1st number: 25
# Enter the 2nd number: 15
# Enter the 3rd number: 20
# Enter the 4th number: 17
# Enter the 5th number: 23
# Enter the last number: 18

# 18 isn't in 25,15,20,17,23.

# -write a program that prompts a user to enter 6 numbers
# -program prints a message saying
# -if the last num is in the previous 5 or not

# A
# -get input from the user 6 times

# -iterate over the first 5 numbers and if `target` num is there
# -print the message that the last number appears within the first 5
# -if not, print the message that it doesn't
# way to print
#  17 is in 25,15,20,17,23
# 18 isn't in 25,15,20,17,23

# number1 = input('Please enter a number:')
# number2 = input('Please enter a number:')
# number3 = input('Please enter a number:')
# number4 = input('Please enter a number:')
# number5 = input('Please enter a number:')

# list_of_nums = [number1, number2, number3, number4, number5]

# number6 = input('Please enter a number:')

# if number6 not in list_of_nums:
#     print(f"{number6} is not in {number1}, {number2}, {number3}, {number4} and {number5}")
# else:
#     print(f"{number6} is in {number1}, {number2}, {number3}, {number4} and {number5}")

# res = "*".join(list(map(str, l)))

# number1 = input('Please enter a number:')
# number2 = input('Please enter a number:')
# number3 = input('Please enter a number:')
# number4 = input('Please enter a number:')
# number5 = input('Please enter a number:')

# list_of_nums = [number1, number2, number3, number4, number5]

# number6 = input('Please enter a number:')

# if number6 not in list_of_nums:
#     print(f"{number6} is not in {', '.join(list_of_nums)}")
# else:
#     print(f"{number6} is in {', '.join(list_of_nums)}")


# Write a function that returns True if the string passed as an argument is a palindrome, False otherwise. A palindrome reads the same forwards and backwards. For this problem, the case matters and all characters matter.

# ExamplesCopy Code
# All of these examples should print True

def is_palindrome(string):
    return string == string[::-1]


# # lst[start:stop:step] | lst.slice(start:stop:step)
# slice = lst.slice(start:stop:step)
# print(slice.stop)
# lst[0:4]
# lst[0:4:2]
# lst[:8]
# lst[4:]
# lst[::-1]
# str[::-1]


print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)

# 6. Getting hold of slice attributes

# numbers = [0, 444, 2, 3, 4, 5, 6, 7, 8, 9]

# s = slice(1, 7, 2)
# print(s)
# # print(numbers[numbers1])
# print(numbers[s])
# print(s.start)  # 1
# print(s.stop)   # 7
# print(s.step)   # 2

# Write another function that returns True if the string passed as an argument is a palindrome,
# or False otherwise. This time, however, your function should be case-insensitive, and should ignore
# all non-alphanumeric characters. If you wish, you may simplify things by calling the is_palindrome
# function you wrote in the previous exercise.


def is_real_palindrome(string):
    cleaned_text = ''.join(char for char in string if char.isalnum())
    cleaned_text = cleaned_text.lower()
    return cleaned_text == cleaned_text[::-1]


print(is_real_palindrome('madam') == True)  # True
print(is_real_palindrome('356653') == True)  # True
print(is_real_palindrome('356635') == False)  # True
print(is_real_palindrome('356a653') == True)  # True
print(is_real_palindrome('123ab321') == False)  # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)  # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True)  # True
