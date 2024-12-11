# x = 10

# def my_function():
#     x = x + 5
#     print(x)
#
# print(my_function()) # UnboundLocalError: cannot access local variable 'x' where it is not associated with a value

# In the function my_function, when we attempt to reassign the value of x by incrementing it,
# Python assumes that x is a local variable since we're assigning it inside the function.
# However, since it is uninitialized, we get an error. If we wanted to modify the global x, we would need to use the global keyword.

# fixed
# x = 10
# def my_function(x): # we are passibng x as an argument to the function
#     x = x + 5
#     print(x)
#
#
# print(my_function(x))
# print(x)  # x does NOT change

# fixed 2
x = 10


def my_function():
    global x  # this makes it so that x is a global variable and is accessible inside the function
    x = x + 5
    print(x)


print(my_function()) # output: 15
print(x) # outputs: 15 because x has been modified inside the function
