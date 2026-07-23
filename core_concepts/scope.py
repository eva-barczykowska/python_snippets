def my_func():
  x = 10
  print("Value inside function:", x)

x = 20

my_func()

print("Value outside function:", x)

print("--------------------")
# if I want to modify the value of x inside the function, I can use the global keyword
x = 55
def my_func():
  global x # this makes x a global variable
  x = 1001
  print("Value inside function:", x)


my_func()

print("Value outside function:", x)