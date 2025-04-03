# # Write a program that prompts the user for two positive number(floating-point), then prints the results of the following operations on those two numbers: addition, subtraction, product, quotient, floor quotient, remainder, and power. Do not worry about validating the input.
#
# number1 = float(input("Enter the first number: "))
# number2 = float(input("Enter the second number: "))
# prompt = "==>"
#
# def addition(number1, number2, symbol='+'):
#     sum = number1 + number2
#     print(f"==>{number1} {symbol} {number2} = {sum}")
#
#
# def subtraction(number1, number2, symbol='-'):
#     difference = number1 - number2
#     print(f"==>{number1} {symbol} {number2} = {difference}")
#
#
# def multiply(number1, number2, symbol='*'):
#     result = number1 * number2
#     print(f"==>{number1} {symbol} {number2} = {result}")
#
#
# def floating_division(number1, number2, symbol='/'):
#     result = number1 / number2
#     print(f"==>{number1} {symbol} {number2} = {result}")
#
#
# def integer_division(number1, number2, symbol='//'):
#     result = number1 // number2
#     print(f"==>{number1} {symbol} {number2} = {result}")
#
#
# def modulo(number1, number2, symbol='%'):
#     result = number1 % number2
#     print(f"==>{number1} {symbol} {number2} = {result}")
#
#
# def exponent(number1, number2, symbol='**'):
#     result = number1 ** number2
#     print(f"==>{number1} {symbol} {number2} = {result}")
#
#
# addition(number1, number2)
# subtraction(number1, number2)
# floating_division(number1, number2)
# integer_division(number1, number2)
# modulo(number1, number2)
# exponent(number1, number2)

print("----")
# problem is with lower versions of python, like 3.9
#LS solution
def calculate(first, second, operator):
    match operator:
        case '+':  return first + second
        case '-':  return first - second
        case '*':  return first * second
        case '/':  return first / second
        case '//': return first // second
        case '%':  return first % second
        case '**': return first ** second

first_float = float(input("==> Enter the first number:\n"))
second_float = float(input("==> Enter the second number:\n"))
for operator in ['+', '-', '*', '/', '//', '%', '**']:
    operation = f"{first_float} {operator} {second_float}"
    result = calculate(first_float, second_float, operator)
    print(f"==> {operation} = {result}")