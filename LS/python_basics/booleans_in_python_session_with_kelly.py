# without running the following code, what will it print out?

# print(0 and 5)
# returns the 0 coz when python sees AND, it knows that BOTH operands have to evaluate as true and when it sees 0, it knows
# that this won't be possible and so it prints out the first operand
# -it returns the first false value it finds or the last value if all are truthy:
# print(5 and 9) # prints 9

# print(5 and 0) prints 0

# print("hello" or "") # behave in the same way as integers
# short-circuiting/boolean short circuit evaluation # prints "hello"

# #print("" or "hello")
# in an or statement if the first op is falsey, it will skip it and return the 2nd regardless if it is true or false
# prints "hello"


# What will the following code output and why?

# result = None and print("This will print") #None
# print(result)

# determine the output of the following code:
x = 5
y = 1
result = x and y or x
print(result)

# determine the output of the following code
# a = "hello" and 0 and [] # returns the first falsy value it finds
# b = "" or {} or "world"
# print(a) #0
# print(b) #world

# a = 0
# b = ""
# c = []
# result = a or b or c or "All falsy" # All falsy # it returns the last value
# print(result)

# x = 5
# y = 10
# result = ((x == 5) and (y > 5)) or (x < 3) #True
# print(result)

# def returns_none():
# return None
# result = False or returns_none() or "default"
# print(result)

# OR
# in case of or, or will return the if the 1st o is falsy, it will return the 2nd (or last) operand regardless of whether it's truthy or falsey
# if the 1st o is TRUTHY, it will return the first operand and short circuits

# x = 10
# #y = 0

# result = y and (x / y) > 0 # (x / y) > 0 evaluate as false
# print(result)


# AND
# what happens if the first o is truthy?
# if the first o is trhuty, it has to look at th 2nd one to find out if it's truthy too because both have to be truthy
# stops evaluating when it finds the 1st falsey value
# if all operands are truthy, it returns the LAST TRUTHY
# if all flasy, it returns FIRST FALSEY
# if it is a mix, it returns FIRST FALSEY

# def say_hello():
#     print("Hello!")
#     return True
#
#
# def say_goodbye():
#     print("Goodbye!")
#     return False
#
#
# result = (say_hello() and say_goodbye()) or say_hello()
# print(f"Final result: {result}")
#
# # Hello
# # Goodbye
# Final result: Hello!

# Hello
# Goodbye
# False or True - TRUE
# [] "" "hello" vs True False