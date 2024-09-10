# 2485 can be rewritten as:
# 2 * (10**3) + 4 * (10**2) + 8 * (10**1) + (5 * (10**0)

# - ask the user to enter a 4-digit number
# - convert the number into an integer
# - calculate the sum of its digits in the above format
# - get the len of the string
# - use enumerate in combination with len to know what power you should use

# output = ''
#
# s = (input("Enter a 4-digit number: ")).strip()
#
# for index, one_digit in enumerate(s):
#     output += f"({one_digit} * 10**{len(s) - index - 1})"
#
#     if index < len(s) - 1: # penultimate digit, we don't want + after last digit added
#         output += ' + '
#
# print(output)
#
# print()
# #  another  way to solve the problem

output = ''

number = (input("Enter a 4-digit number: ")).strip()
length = len(number)
print(f"Length of the number: {length}")

for index, one_character in enumerate(number):
    output += f"{one_character} * (10**{length - index - 1})"

    if index < len(number) - 1:  # penultimate digit, we don't want + after last digit added
        output += ' + '

print(output)





