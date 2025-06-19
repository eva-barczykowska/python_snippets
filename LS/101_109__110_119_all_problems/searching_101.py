#Searching 101
#Write a program that solicits six (6) numbers from the user and prints a message that describes whether the sixth number appears among the first five.
# P:
# -write a program that prompts the user 6 times to enter a number
# -the program informs the user if the 6th number that she entered appears in the previous 5

# DS
# -list

# A:
# -prompt the user 6timnes to enter a number
# -look at the last number in that list
# - use a slice and verify that the last num is the previous 5
# -inform the user if this is the case or not
# format: #17 is in 25,15,20,17,23.
#18 isn't in 25,15,20,17,23.


# numbers = []
# for num in range(6):
#     user_input = input(f"Please enter a number")
#     numbers.append(user_input)

# target = numbers[-1]
# considered_range = numbers[: -1]

# stringified_numbers = list_of_strings = list(map(lambda x: str(x), numbers))
# if not target in considered_range:
#     print(f"{target} isn't in {' '.join(stringified_numbers)}")
# else:
#     print(f"{target} is in {' '.join(stringified_numbers)}")


# squared_numbers = list(map(lambda x: x ** 2, numbers))
#Example:

#Enter the 1st number: 25
#Enter the 2nd number: 15
#Enter the 3rd number: 20
#Enter the 4th number: 17
#Enter the 5th number: 23
#Enter the last number: 17

#17 is in 25,15,20,17,23.

# Enter the 1st number: 25
#Enter the 2nd number: 15
#Enter the 3rd number: 20
#Enter the 4th number: 17
#Enter the 5th number: 23
#Enter the last number: 18

#18 isn't in 25,15,20,17,23.

# rewriting this:

numbers = []
for num in range(6):
    user_input = input(f"Please enter a number")
    numbers.append(user_input)

strings = list_of_strings = list(map(lambda x: str(x), numbers))

if not numbers[-1] in numbers[:-1]:
    print(f"{numbers[-1]} isn't in {' '.join(strings)}")
else:
    print(f"{numbers[-1]} is in {' '.join(strings)}")