# Your task is to create a function that does four basic mathematical operations.
#
# The function should take three arguments - operation(string/char), value1(number), value2(number).
# The function should return result of numbers after applying the chosen operation.

# ('+', 4, 7) --> 11
# ('-', 15, 18) --> -3
# ('*', 5, 5) --> 25
# ('/', 49, 7) --> 7


def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        if value2 == 0:
            return 'Error: Division by zero'
        else:
            return value1 / value2


print(basic_op('+', 4, 7))  # , 11)
print(basic_op('-', 15, 18))  # , -3)
print(basic_op('*', 5, 5))  # , 25)
print(basic_op('/', 49, 7))  # , 7)
print(basic_op('/', 49, 0))  # , error)


def basic_op(operator, value1, value2):
    return eval(f'{value1}{operator}{value2}')


print(basic_op('+', 4, 7))  # , 11)
print(basic_op('-', 15, 18))  # , -3)
print(basic_op('*', 5, 5))  # , 25)
print(basic_op('/', 49, 7))  # , 7)
# print(basic_op('/', 49, 0))  # , 7)
