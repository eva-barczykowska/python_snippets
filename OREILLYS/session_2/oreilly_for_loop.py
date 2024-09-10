vowels = 0
digits = 0
others = 0

# # Prompt the user to enter a string
# string = input("Enter a string: ").strip()
# for char in string:
#     if char in 'aeouiAEIOU':
#         vowels += 1
#     elif char.isdigit():
#         digits += 1
#     else:
#         others += 1

# print("Vowels:", vowels)
# print("Digits:", digits)
# print("Others:", others)
#
# # another way to solve the problem
# string = input("Enter a string: ").strip()
# for char in string:
#     if char in 'aeouiAEIOU':
#         vowels += 1
#     elif char in '0123456789':
#         digits += 1
#     else:
#         others += 1
#
# print(f"Vowels:, {vowels}")
# print(f"Digits:, {digits}")
# print(f"Others:, {others}")
#
# print(char) # char exits in the loop after the loop finishes
# print(f"Char after loop: {char}")

total = 0

how_many_numbers = int(input("How many numbers you want to sum up? "))
for number in range(how_many_numbers):
    num = input("Enter number: ")
    if not num.isdigit():
        print("Invalid input, ignoring") # user loses 1 input
    else:
        total += int(num)

print(f"The sum of all numbers is: {total}")


# total = 0
#
# how_many_numbers = int(input("How many numbers you want to sum up? "))
# for number in range(how_many_numbers):
#     num = input("Enter number: ")
#     while not num.isdigit():
#         print("Invalid input. Please enter a valid number.")
#         num = input("Enter number: ")
#     else:
#         total += int(num)
#
# print(f"The sum of all numbers is: {total}")
