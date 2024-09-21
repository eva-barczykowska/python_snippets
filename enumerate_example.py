colors = ['RED', 'GREEN', 'YELLOW', 'BLUE', 'MAGENTA', 'CYAN', 'WHITE']
print(enumerate(colors))  # its a callable, it's a class, it acts as a function
# https://www.pythonmorsels.com/callables/
# a callable is an object that can be called (like a function)
# functions can be called
# objects can be called, so they're callables too.'
enumerate_colors = list(enumerate(colors))
print(enumerate_colors)

# enumerate is a class but it behaves like a function,
# in fact is is mentioned as an in-built function in Python documentation
# it returns an object that behaves like an iterator