# Isn't it Odd?
# Write a function that takes one integer argument and returns True when the number's absolute value is odd, False otherwise.


# def get_odd(number):
#     return abs(number) % 2 == 1

# print(get_odd(1))
# print(get_odd(2))
# print(get_odd(-1))
# print(get_odd(-2))
# print(get_odd(0))

# Odd Numbers
# Print all odd numbers from 1 to 99, inclusive, with each number on a separate line.

# Bonus Question: Can you solve the problem by iterating over just the odd numbers?

# my_range = range(1, 100, 2)
# for number in range(1, 100, 2):
#     print(number)

# for number in range(1, 100):
#     if number % 2 == 1:
#         print(number)

# Print all even numbers from 1 to 99, inclusive, with each number on a separate line.

# Bonus Question: Can you solve the problem by iterating over just the even numbers?

# for number in range(1, 100):
#    if number % 2 == 0:
#        print(number)

# for number in range(0, 100, 2):
#      print(number)

#      How big is the room?
# Build a program that asks the user to enter the length and width of a room, in meters, then prints the room's area in both square meters and square feet.

# Note: 1 square meter == 10.7639 square feet

# length = float(input("how long is your room?"))
# width = float(input("how wide is your room?"))

# in_metres = length * width
# in_square_feet = in_metres * 10.7639

# print(f"In meteres {in_metres} and in square feet {in_square_feet}")


# dollars = float(input("What is the bill? "))
# percentage = float(input("What is the tip percentage? "))
# tip = dollars * (percentage / 100)
# total = dollars + tip

# print(f"The tip is {tip:.2f}")
# print(f"The total is {total:.2f}")

# Sum or Product of Consecutive Integers
# Write a program that asks the user to enter an integer greater than 0, then asks whether the user wants to determine the sum or the product of all numbers between 1 and the entered integer, inclusive.

# Please enter an integer greater than 0: 5
# Enter "s" to compute the sum, or "p" to compute the product. s

# The sum of the integers between 1 and 5 is 15.
# Please enter an integer greater than 0: 6
# Enter "s" to compute the sum, or "p" to compute the product. p

# The product of the integers between 1 and 6 is 720.


# import math

# number_range = range(int(input("enter an integer greater than 0 ")) + 1)
# wish = input("Sum or product, enter 's' or 'p?").lower()
# my_sum = sum(number_range)
# my_product = math.prod(list(number_range)[1:])


# if wish == 's':
#     print(f"The sum is {my_sum}")
# elif wish == 'p':
#     print(f"The product is {my_product}")
# else:
#     print("Sorry, you need to print only 's' or 'p'")


import math

number = int(input("enter an integer greater than 0 "))
number_range = number + 1
wish = input("Sum or product, enter 's' or 'p?").lower()
my_sum = sum(range(number_range))
my_product = math.prod(range(1, number_range))

if wish == 's':
    print(f"The sum is {my_sum}")
elif wish == 'p':
    print(f"The product is {my_product}")
else:
    print("Sorry, you need to print only 's' or 'p'")

