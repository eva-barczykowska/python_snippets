"""
https://launchschool.com/exercises/fc450ab6
Greeting a user
Write a program that asks for user's name, then greets the user. If the user appends a ! to their name, the computer
will yell the greeting (print it using all uppercase).

What is your name? Sue
Hello Sue.

What is your name? Bob!
HELLO BOB! WHY ARE WE YELLING?
"""
name = input("What is your name? ")
if name[-1] != "!":
    print(f"Hello, {name.title()}.")
else:
    print(f"HELLO, {name.upper()} WHY ARE YOU YELLING?")