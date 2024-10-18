"""
Build a program that displays when the user will retire and how many years she has to work till retirement.

What is your age? 30
At what age would you like to retire? 70

It's 2024. You will retire in 2064.
You have only 40 years of work to go!
"""

# import datetime

# age = int(input("What is your age? "))
# retire_age = int(input("At what age would you like to retire? "))
# years_of_work_left = retire_age - age
# now = datetime.datetime.now()
# current_year = int(now.year)

# print(f"It's {current_year}.  You will retire in {current_year + years_of_work_left}.")
# print(f"You have only {years_of_work_left} years of work to go!")

# Use the datetime module from the Python standard library.

# Write a function that takes a non-empty string argument and returns the middle character(s) of the string. If the string has an odd length, you should return exactly one character. If the string has an even length, you should return exactly two characters.

# ExamplesCopy Code
'''
if str is odd size, return middle character
if str is even, return middle 2 characters

-check for the size of the str
-divide the size into 2
-if it's odd, divide into 2 and add 1
-get the char at that index 

-if it's even
-retrieve this and next index
-return them
'''

# def center_of(str):
#     print(f"size is {len(str)}")
#     index = len(str) // 2
#     print(index)
#     if len(str) % 2 == 0:
#         return str[index-1] + str[index]
#     else:
#         return str[index]
def center_of(string):
  length = len(string)
  middle = length // 2

  if length % 2 == 0:  # Even length
    return string[middle - 1: middle + 1]
  else:  # Odd length
    return string[middle]

    # range(1, 101) # range 1 - 100

print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True
print(center_of('dome') == "om")

