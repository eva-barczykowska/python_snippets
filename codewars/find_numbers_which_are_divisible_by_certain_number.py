# Complete the function which takes two arguments and returns all numbers which are divisible by the given divisor.
# First argument is an array of numbers and the second is the divisor.

# input is an array of integers and a target divisor, also an integer
# from the array find numbers that are divisible by the divisor

# Algorithm:
# -init array_to_return
# -iterate over the numbers in the array
# -if the current number is divisible by the divisor (current number % divisor == 0)
#   -add the current number to a new array
def divisible_by(numbers, divisor):
    nums_divisible_by_divisor = []

    for num in numbers:
        if num % divisor == 0:
            nums_divisible_by_divisor.append(num)

    return nums_divisible_by_divisor


print(divisible_by([1, 2, 3, 4, 5, 6], 2))  # --> [2, 4, 6]

print()


def divisible_by(numbers, divisor):
    return [num for num in numbers if num % divisor == 0]


print(divisible_by([1, 2, 3, 4, 5, 6], 2))  # --> [2, 4, 6]
