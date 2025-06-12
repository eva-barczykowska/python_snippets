import random

python_functions = {
    "abs()": "Returns the absolute value of a number",
    "all()": "Returns True if all items in an iterable object are true",
    "any()": "Returns True if any item in an iterable object is true",
    "ascii()": "Returns a readable version of an object, replacing non-ASCII characters with escape characters",
    "bin()": "Returns the binary version of a number",
    "bool()": "Returns the boolean value of the specified object",
    "bytearray()": "Returns an array of bytes",
    "bytes()": "Returns a bytes object",
    "callable()": "Returns True if the specified object is callable, otherwise False",
    "chr()": "Returns a character from the specified Unicode code",
    "classmethod()": "Converts a method into a class method",
    "compile()": "Returns the specified source as an object, ready to be executed",
    "complex()": "Returns a complex number",
    "delattr()": "Deletes the specified attribute (property or method) from the specified object",
    "dict()": "Returns a dictionary (Array)",
    "dir()": "Returns a list of the specified object's properties and methods",
    "divmod()": "Returns the quotient and remainder when dividing two numbers",
    "enumerate()": "Takes a collection and returns it as an enumerate object",
    "eval()": "Evaluates and executes an expression",
    "exec()": "Executes the specified code or object",
    "filter()": "Filters items in an iterable based on a function",
    "float()": "Returns a floating-point number",
    "format()": "Formats a specified value",
    "frozenset()": "Returns a frozenset object",
    "getattr()": "Returns the value of the specified attribute of an object",
    "globals()": "Returns the current global symbol table as a dictionary",
    "hasattr()": "Checks if an object has a specific attribute or method",
    "hash()": "Returns the hash value of an object",
    "help()": "Executes Python's built-in help system",
    "hex()": "Converts a number into hexadecimal format",
    "id()": "Returns the unique identifier of an object",
    "input()": "Accepts user input as a string",
    "int()": "Converts an object to an integer number",
    "isinstance()": "Checks if an object is an instance of a class or type",
    "issubclass()": "Checks if a class is a subclass of another class or type",
    "iter()": "Returns an iterator object for an iterable item",
    "len()": "Returns the length (number of items) in an object or iterable",
    "list()": "Creates and returns a list object",
    "locals()": "Returns a dictionary of local variables in the current scope",
    "map()": "Applies a function to each item in an iterable and returns an iterator with results",
    "max()": "Finds and returns the largest item in an iterable or among arguments provided",
    "memoryview()": "Creates and returns a memory view object for binary data manipulation",
    "min()": "Finds and returns the smallest item in an iterable or among arguments provided",
    "next()": "Returns the next item from an iterator",
    "object()": "Returns a new object",
    "oct()": "Converts a number into octal format",
    "open()": "Opens a file and returns a file object",
    "ord()": "Returns the Unicode code of a character",
    "pow()": "Returns the power of a number",
    "print()": "Prints the specified message to the console",
    "property()": "Creates a property object",
    "range()": "Creates a range object",
    "repr()": "Returns a string representation of an object",
    "reversed()": "Returns a reverse iterator for an iterable",
    "round()": "Rounds a number to the nearest integer",
    "set()": "Creates and returns a set object",
    "setattr()": "Sets the value of a specified attribute of an object",
    "slice()": "Creates a slice object",
    "sorted()": "Returns a sorted list of an iterable",
    "staticmethod()": "Converts a method into a static method",
    "str()": "Returns a string representation of an object",
    "sum()": "Returns the sum of all items in an iterable",
    "tuple()": "Creates and returns a tuple object",
    "type()": "Returns the type of an object",
    "vars()": "Returns a dictionary of local variables and their values",
    "zip()": "Returns an iterator that aggregates elements from each of the iterables"
}

print("Welcome to the Python Function Game!")
print("Guess the name of a Python built-in function based on its description.")
print("You can select EASY or HARD mode.")
print("EASY means you will get the first letter of the function and its definition."
      "HARD means you get just the definition.")

while True:
    mode = input("Choose your mode (e/h): ").lower()
    if mode not in ['e', 'h']:
        print("Invalid mode. Please choose either 'e' for EASY or 'h' for HARD.")
    else:
        break


if mode == 'e':
    counter = 0
    result = 0
    while True:
        if counter > 9:
            print(f"Thanks for playing, your result is {result} ouf of 10")
            break
        random_function_number = random.randint(0, len(python_functions) - 1)
        target = list(python_functions.keys())[random_function_number]
        guess = input(f"{python_functions[target].upper()}. Starts with: {target[0]} -> ")


        if guess == target:
            print("Congratulations! You guessed correctly. You get a point.\n")
            result += 1
        else:
            print(f"Not quite, the correct answer is {target}.\n")
        counter += 1

elif mode == 'h':
    counter = 0
    result = 0
    while True:
        if counter > 9:
            print(f"Thanks for playing, your result is {result} ouf of 10")
            break
        random_function_number = random.randint(0, len(python_functions) - 1)
        target = list(python_functions.keys())[random_function_number]
        guess = input(f"{python_functions[target].upper()}. -> ")

        if guess == target:
            print("Congratulations! You guessed correctly. You get a point.\n")
            result += 1
        else:
            print(f"Not quite, the correct answer is {target}.\n")
        counter += 1


# TODO version 3
# store all of their incorrect guesses and show them at the end of the game

# TODO version 4
# next time they play, ask them all the functions that they've previously got wrong

# TODO version 5
# make an Alexa skill that uses this game

# TODO version 6
# decide if provide additionally % or not

# TODO version 7
# implement CI/CD pipeline as per the Oreilly publication I read/Gitlab courses/best practises