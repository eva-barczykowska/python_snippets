# Update the following code so that, instead of printing the values,
# each statement prints the name of the class to which it belongs.

print(type(("Hello")))             # <class 'str'>
print(type(5))                      # <class 'int'>
print(type([1, 2, 3]))            # <class 'list'>

'''All above values are objects. Each object is an instance of a type(class).
"Hello" is an instance of the str class, 5 is an instance of the int class,
[1, 2, 3] is an instance of the list class.

To determine the type an object belongs to, we use the type() function.'''