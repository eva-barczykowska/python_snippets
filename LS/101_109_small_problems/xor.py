# The or operator returns a truthy value if either or both of its operands are truthy, a falsy value if both operands are falsy. The and operator returns a truthy value if both of its operands are truthy, and a falsy value if either operand is falsy. This works great until you need only one of two conditions to be truthy, the so-called exclusive or, also known as xor (pronounced "ECKS-or").

#In this exercise, you will write an xor function that takes two arguments, and returns True if exactly one of its arguments is truthy, False otherwise.

# print(xor(5, 0) == True)
# print(xor(False, True) == True)
# print(xor(1, 1) == False)
# print(xor(True, True) == False)b

# P:
# -write a function that takes 2 arguments and  returns TRue if only 1 arg is truthy

# E:÷
#A:
# -i have 2 args
# -check how each one evaluates
# -if one and one only evaluates as true, function returns True
# -else functions returns false

def xor(arg1, arg2):
    if bool(arg1) == True and bool(arg2) == True:
        return False
    elif bool(arg1) == False and bool(arg2) == False:
        return False
    else:
        return True

print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)

