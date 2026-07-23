import string

digits = string.digits # so now I can call it without ()???
print(digits)
print(type(digits))

hexadecimal_digits = string.hexdigits
print(hexadecimal_digits)

# Why don't I need parentheses when accessing attributes of a module?'
# In Python, certain attributes of classes can be accessed without parentheses because they are not methods
# but rather PROPERTIES or STATIC ATTRIBUTES.
# In your example, `.digits` is not a method but a **class attribute** of the `string` module.

# For example:
# ```python
# import string
# print(string.digits)
# ```
# This works without parentheses because `digits` is a constant string, defined as `'0123456789'`.
# It’s simply an attribute that holds a value, not a function that needs to be executed.
#
# When you see parentheses `()`, it's used to **call a method**
# (i.e., a function associated with an object or class). If you omit the parentheses when working with methods,
# you are referencing the method itself rather than executing it.
#
# So in this case:
# - `string.digits` is a **static attribute**, a predefined string of digits, which is why it doesn't need `()`.

all_characters = string.printable
print(all_characters)