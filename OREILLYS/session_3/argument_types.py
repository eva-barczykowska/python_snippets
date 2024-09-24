def count_chars(text, chars):
    """Expects: a string and a string of characters to be counted.
    Modifies: nothing.
    Returns a dictionary with the count of each character in the string."""
    result = {}
    for char in chars:
        if char in chars:
            result[char] = text.count(char)
    return result


count_hash = count_chars("Hello, World!", "aeoui")
print(count_hash)

print()
print("with a default argument")


def count_chars(text, chars='aeoui'):
    """Expects: a string and (otional) string of characters.
    If no characters are provided, it defaults to 'aeioui' (vowels).
    Modifies: nothing.
    Returns a dictionary with the count of each character in the string."""
    result = {}
    for char in chars:
        if char in chars:
            result[char] = text.count(char)
    return result


count_hash = count_chars("Hello, World!")
print(count_hash)


# *args
# This syntax allows a function to accept any number of arguments.
def sum_numbers(*args):
    return sum(args)


sum_numbers_result = sum_numbers(1, 2, 3, 4, 5)

print()
print("positional arguments and splat arguments example")
print("splat arguments are unpacked as a tuple")


# example with positional and splat arguments
def my_function(x, y, *args):
    print(f"x is {x}, y is {y}, and args are {args}")


print(my_function(1, 2, 3, 4, 5))

print(sum_numbers(1, 2, 3, 4, 5))  # Output: 15


# we can iterate over the splat arguments
# we could pass a list or tuple to the function but *args will automatically unpack it
# and is considered more elegant
# we can iterate over the splat arguments, we should really take args[0]

#  exercise:
import math

def operate(str_operator, a, b, *args):
    """
    Expects: a string representing an operator (+, -, *, /), two numbers, and any number of additional arguments.
    Modifies: nothing.
    Returns: result of the operation.
    """
    if str_operator == '+':
        return a + b + sum(args)
    elif str_operator == '-':
        return a - b - sum(args)
    elif str_operator == '*':
        return math.prod(args)
    elif str_operator == '/':
        if b == 0:
            raise ZeroDivisionError("Pamietaj cholero: nie dziel przez zero!")
    else:
        final_result = a / b
        print("final result:")
        print(final_result)
        for num in args:
            final_result = final_result / num
            print(final_result)
        return final_result


print(operate('-', 1, 2, 3, 4, 5))
print(operate('+', 1, 2, 3, 4, 5))
print(operate('*', 1, 2, 3, 2, 5))
print("and now division:")
print(operate('/', 100, 2, 2, 2, 2))
