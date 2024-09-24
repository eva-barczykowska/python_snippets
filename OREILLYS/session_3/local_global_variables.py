x = 100  # global variable


def my_function():
    x = 50  # local variable
    print(x)


print(x)
print(my_function())
print(x)

print()
# HEY!!! I can access a global variable inside a function without passing it as an argument!

x = 555


def my_function():
    print(x)


print(my_function())

print()
print("global")
# the global keyword

x = 1001
print(x)


def my_function():
    global x
    x = -1
    print(x)


print(my_function())
print(x)  # the value of x is changed!

# 4 scopes: local, closing, global, built-in
# main scope in Ruby is global in Python
# each function in nested functions has its own scope/stack frame with its own local variables
# amd when a function finishes, its local variables are destroyed unless they are passed to another function
# as arguments or returned from the function

print()
print("modify global variable from inside a function")
# we can modify a global variable from inside a function
y = [10, 20, 30]
print(y)
def my_function():
    y[0] = -111
    print(f"Inside the function: {y}")

print(f"Before the function call: {y}")
print(my_function())
print(f"After the function{y}")  # the value of y is changed!
