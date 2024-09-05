# ask the user for their name
# greet the user with their name

# ask the user for the operation to perform
# -- check if the user entered a valid operation number
# --if yes, prompt the user to re-enter a valid operation number

# ask the user for 2 numbers
# --for each number account for the situation where the user might enter invalid input

# perform the operation on the 2 numbers
# output result
#
# --lessons learned:
# division by zero: This error occurs when you try to divide by zero.
# what about numbers that are negative or zero


# answer = Kernel.gets()
# Kernel.puts(answer)

# def prompt(message):
#   print(f"=> {message}")

name = input("Hello, please enter your name: ")
while name == "":
    print("Hey, sorry, the name cannot be empty. Please enter your name!")
    name = input("Your name is: ")
print(f"Hello, {name.capitalize()}! Let's perform some calculations!")

operation = input("""What operation would you like to perform? Select a number from the following options:
  1) add
  2) subtract
  3) multiply
  4) divide
""")

# Validate the input to ensure it's a valid operation number
valid_operations = ['1', '2', '3', '4']
while operation not in valid_operations:
    print("Hey, you've entered something that I cannot use. Please enter a valid operation number!Ewa")
    operation = input("""What operation would you like to perform? Select a number from the following options:
      1)add
      2)subtract
      3)multiply
      4)divide
    """)

operations = {'1': 'addition', '2': 'subtraction', '3': 'multiplication', '4': 'division'}
if operation in operations:
    print(f"Selected operation: {operations[operation]}")


number1 = input("Please enter the first number:")
while not number1.replace('-', ''):
    print("Hey, you've entered something that I cannot use. Please enter a valid number!")
    number1 = input("Please enter the first number:")

number1 = float(number1)

number2 = input("Please enter the second number:")
while not number2.replace('-', '') or number2 == "0" and operation == '4':  # division by zero is not allowed:
    print("Hey, you've entered something that I cannot use. Please enter a valid number (not ZERO!")
    number2 = input("Please enter the second number:")
number2 = float(number2)


def get_result(operation, number1, number2):
    if operation == '1':
        return number1 + number2
    elif operation == '2':
        return number1 - number2
    elif operation == '3':
        return number1 * number2
    elif operation == '4':
        return number1 / number2


print("Result is: ", get_result(operation, number1, number2))

# from AI
# def get_result(operation, number1, number2):
#     operations = {
#         '1': lambda: number1 + number2,
#         '2': lambda: number1 - number2,
#         '3': lambda: number1 * number2,
#         '4': lambda: number1 / number2,
#     }
#     return operations.get(operation, lambda: "Invalid operation")()

# In this updated code, a dictionary operations is defined with keys representing operation numbers
# and values as lambda functions that perform the corresponding operations. The get method of the dictionary is used
# to retrieve the appropriate function based on the operation parameter. If the operation is not found in the dictionary,
# a default lambda function that returns "Invalid operation" is returned.

# The lambda functions in the dictionary are anonymous functions that perform the operations without the need for
# explicit return statements. The parentheses at the end of the get method call invoke the retrieved function.
#
# This updated code achieves the same functionality as the original code but in a more compact and efficient manner.
