# filter(function, iterable, /)
# What is /?
# The slash (/) in filter(function, iterable, /) indicates that all parameters before it must be specified
# as positional arguments. This means that you cannot use keyword arguments for these parameters.


def is_not_lowercase(word):# pass in word, helper function to filter out words that are not lowercase
    return word.islower()

l = ["ewa", "kelly", "Kelley", "Kelly Clarkson"]

filtered_words = list(filter(str.islower, l))
print(filtered_words)


# done with lambda function
filtered_words = list(filter(lambda w:  w.islower(), l)) # w is just a placeholder variable
print(filtered_words)


# Function definition
def is_even(x): # helper function to filter out even numbers
    return x % 2 == 0

result = filter(is_even, [1, 2, 3, 4, 5])
print(list(result))  # Output: [2, 4]
# This will raise a TypeError:
# result = filter(function=is_even, iterable=[1, 2, 3, 4, 5]) # coz iterable is a positional argument, not a keyword argument


def is_str(x):
    return isinstance(x, str)

l = ["ewa", "kelly", "Kelley", True, 22]

strings_only = list(filter(is_str, l))
print(strings_only)



all_numbers = [1, 44, 5, 9.0, 3.77]

floats_only = list(filter(lambda number: isinstance(number, int), all_numbers))
print(floats_only)


words = ["mazda", "toyota", "opel", "bmw", "audi", "mercedes binz"]
#words.reverse() # careful!!! this method reverses the list given, it has nothing to do with the sort reverse=True

words.sort(key=lambda w: w, reverse=True)
print(words)

shorts_only = list(filter(lambda w: len(w) < 5, words))
print(shorts_only)


def example(a, b, /, c, d):
    return a + b + c + d

# For parameters c and d, I can use either positional or keyword arguments (but not both the same call).
# So parameters can be positional or keyword. Positional parameters are before the /.
# Positional-only parameters: a, b
# Positional-and-keyword parameters: c, d

# Valid calls
result1 = example(1, 2, 3, 4)  # Positional
result2 = example(1, 2, c=3, d=4)  # Mixed, i.e. Positional and Keyword

# Invalid call
# result3 = example(a=1, b=2, 3, 4)  # Raises TypeError, because a and b are positional-only parameters


print()
import inspect

sig = inspect.signature(example)
for name, param in sig.parameters.items():
    print(f"Parameter: {name}")
    print(f"  Kind: {param.kind}")
    print(f"  Default: {param.default}")
    print()

print('***')
import inspect

def example_func(a, b, /, c, d=4, *, e, f=6):
    pass

sig = inspect.signature(example_func)
for name, param in sig.parameters.items():
    print(f"Parameter: {name}")
    print(f"  Kind: {param.kind}")
    print(f"  Default: {param.default}")
    print()


# In Python function definitions:
#
# - Parameters **before** the slash (`/`) are **positional-only** — you must pass arguments for them by position, not by keyword.
# - Parameters **after** the slash and **before** the asterisk (`*`) are **positional-or-keyword** — you can pass arguments for them either by position or by keyword.
# - Parameters **after** the asterisk (`*`) are **keyword-only** — you must pass arguments for them by keyword.

# Example:


def func(a, b, /, c, d=4, *, e, f=6):
    print(a, b, c, d, e, f)

# a, b are positional-only
func(1, 2, 3, e=5)

# c and d can be passed as positional or keyword
func(1, 2, c=3, e=5)

# e and f must be passed as keyword
func(1, 2, 3, e=7, f=8)
