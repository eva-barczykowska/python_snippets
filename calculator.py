# ask the user for 2 numbers
# ask the user for the operation to perform
# perform the operation on the 2 numbers
# output result

# answer = Kernel.gets()
# Kernel.puts(answer)

# def prompt(message):
#   print(f"=> {message}")

name = input("Hello, please enter your name: ")
print(f"Hello, {name}! Let's perform some calculations!")

operation = input("""What operation would you like to perform? Select a number from the following options:
  1)add
  2)subtract
  3)multiply
  4)divide
""")

# Validate the input to ensure it's a valid operation number
valid_operations = ['1', '2', '3', '4']
while operation not in valid_operations:
    print("Hey, you've entered something that I cannot use. Please enter a valid operation number.")
    operation = input("""What operation would you like to perform? Select a number from the following options:
      1)add
      2)subtract
      3)multiply
      4)divide
    """)

operations = {'1': 'addition', '2':'subtraction', '3':'multiplication', '4':'division'}
if operation in operations:
    print(f"Selected operation: {operations[operation]}")


# TODO: validate the input to ensure it's a valid operation number'
# otherwise it operation returns none
# prompt the user again until a valid operation is entered

number1 = input("Please enter the first number:")
number1 = float(number1)
number2 = input("Please enter the second number:")
number2 = float(number2)

def get_result(operation, number1, number2):
    if operation == '1':
        return(number1 + number2)
    elif operation == '2':
        return(number1 - number2)
    elif operation == '3':
        return(number1 * number2)
    elif operation == '4':
        return(number1 / number2)

print(get_result(operation, number1, number2))
