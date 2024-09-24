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

print('---------------')
print("A little different, look at the start argument")


def operate_v2(str_operator, start, *args):
    result = start
    if str_operator == '+':
        for num in args:
            result += num
        return result
    elif str_operator == '-':
        for num in args:
            result -= num
        return result
    else:
        raise ValueError("Podano zły operator!")


print(operate_v2('-', 0, 3, 4, 5))
print(operate_v2('+', 0, 4, 5))


# print(operate_v2('*', 1, 3, 2, 5))

# with all the operations:
def operate_v2(str_operator, start, *args):
    result = start
    for num in args:
        if str_operator == '+':
            result += num
        elif str_operator == '-':
            result -= num
        elif str_operator == '*':
            result *= num
        elif str_operator == '/':
            result /= num
    return result


print(operate_v2('-', 0, 3, 4, 5))
print(operate_v2('+', 0, 4, 5))
# print(operate_v2('*', 1, 3, 2, 5))

print()


# with eval(), not advisable!
# especially if the input is from user

def operate_v3(str_operator, start, *args):
    total = start
    for each_arg in args:
        total = eval(f"{total} {str_operator} {each_arg}")
        return total


print(operate_v2('-', 0, 3, 4, 5))
print(operate_v2('+', 0, 4, 5))
print(operate_v2('*', 1, 10, 5, 10))
print(operate_v2('/', 1000, 10, 2, 5))

print()
print("Keyword arguments")


# KEYWORD ARGUMENTS
# have to come after POSITIONAL arguments
#              -----

# Keyword Arguments:
# Definition: Keyword arguments are arguments passed to a function
# by explicitly specifying the parameter name DURING THE FUNCTION CALL.

# Purpose: They allow you to specify arguments in any order and make the code more readable.
# Behavior: When calling a function with keyword arguments, you use the format param_name=value.

def greet(name, greeting, punctuation):
    print(f"{greeting}, {name}{punctuation}")


# Using keyword arguments
greet(name="Alice", greeting="Hello", punctuation="!")  # Output: Hello, Alice!

# We can pass keywords arguments in any order,
# but it's important to remember that positional arguments must come before keyword arguments.

greet(punctuation=".", greeting="Hi", name="Bob")  # Output: Hi, Bob.

print("Default Arguments")


# Default Arguments:
# Definition: Default arguments are parameters that have a default value defined IN THE FUNCTION SIGNATURE.
# If no value is provided for that parameter during the function call, the default value is used.

# Purpose: They allow you to make some arguments optional, as they take a default value if not provided.
# Behavior: You define a default argument by assigning a value to a parameter in the function definition.
def add(first, second):
    return first + second


print(add(first=10, second=5))  # Output: 15 # order doesn't matter, these are KEYWORD ARGUMENTS
print(add(second=5, first=10))  # Output: 15
print(add(3, 30))  # Output: 15


# print(add())  TypeError: add() missing 2 required positional arguments: 'first' and 'second'

# but we cannot do this
def add(first, second=20):
    return first + second


# print(add(second=5, 55)) # RESULTS IN SYNTAX ERROR: positional argument follows keyword argument
# don't use mutable default arguments
# default parameters should come last
# default argument makes the argument optional, but it should be the last one

# How can keyword arguments and default arguments be used together?

# Keyword arguments can be used to pass values for both required and default arguments.
# If a default argument is present, you can still use a keyword argument to override the default.

def introduce(name, age, city="Unknown"):
    print(f"{name} is {age} years old and lives in {city}.")


# Call using positional and default arguments
introduce("Alice", 30)  # Output: Alice is 30 years old and lives in Unknown.

# Call using keyword arguments to override the default
introduce(name="Bob", age=25, city="New York")  # Output: Bob is 25 years old and lives in New York.
