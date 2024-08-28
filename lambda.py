# lambda<argument>: expression
# lambda - compact anonymous function
# a throwaway function without a name
# lambda x: x + 5

greet = lambda name: "Welcome, " + name + "!"
print(greet("Ewa"))
print(greet("Cailan"))
print(greet("Cledwyn"))

# lambda x: x + 5
# lst = [1, 2, 3, 4, 5]
# print(list(map(lambda x: x + 5, lst)))
#
# lambda price: price * 0.9

# greet = lambda name: f"Hello, {name}!"
# lambda word: word.capitalize()
# lambda width, height: width * height

# You can assign the lambda function to a variable and then call it as a regular function:
discount = lambda price: price * 0.9
print(discount(25.99))

price = 100
count = 2
my_variable = lambda price, count: price * count
# lambda function can be assigned to a variable, just like any other function
print(my_variable(2, 10))

# lambda functions are ideal for straightforward, simple operations
power_to = lambda x, y: x ** y
print(power_to(2, 3))  # Output: 8

# we can provide arguments to lambda expressions on the fly when we call them
res = (lambda x, y: x + y)(5, 7)
print(res)  # Output: 12


res = (lambda x, y: x + y)(500, 700)
print(res)  # Output: 1200

res = (lambda x, y=3000: x + y)(5)
print(res)

res = (lambda a=20_000, b=30_00: a + b)
print(res)  # <function <lambda> at 0x1007ed120>

res = (lambda a=20_000, b=30_000: a + b)()
print(res)  # <function <lambda> at 0x1007ed120>

# The power of lambda is better seen when you use them as an anonymous function inside another function
# Say you have a function definition that takes 1 argument, and that argument will be multiplied with an unknown number

def mult(n):
    return lambda a : a * n

doubler = mult(2)
tripler = mult(3)

print(doubler(5))
print(tripler(5))

