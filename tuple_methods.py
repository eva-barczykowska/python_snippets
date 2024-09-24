my_tuple = ('a', 'p', 'p', 'l', 'e')

result = my_tuple.count('p')
print(result)  # Output: 2

result = my_tuple.index('p')
print(result)  # Output: 1

#slicing tuples
my_tuple = ('P','y','t','h','o','n')

# elements at the index range 1 to 4 EXCLUDING
print(my_tuple[1:4])  # ('y', 't', 'h')

# elements from beginning to -4 EXCLUDING
print(my_tuple[:-4])  # ('P', 'y')

# elements 6th to end
print(my_tuple[5:])   # ('n',)
# the comma is used to create a tuple with a single element

# elements from the beginning to the end
print(my_tuple[:])
# Output: ('P', 'y', 't', 'h', 'o', 'n')

my_second_tuple = my_tuple[:]
# my_second_tuple[1] = 'R'  # tuple is immutable, so this will raise an error

# When tuples are nested, they behave similarly to lists
my_tuple = (1, 2, ['z', 'b'])
my_tuple[2][0] = 'a'

print(my_tuple)  # Output: (1, 2, ['a', 'b'])   The inner list has been changed !!!

 # only parentheses is not enough
t1 = ("hello")
print(type(t1))   # Output: <class 'str'>

# need a comma at the end
t2 = ("hello",)
print(type(t2))  # Output: <class 'tuple'>

# parentheses is optional
t3 = "hello",
print(type(t3))  # Output: <class 'tuple'>

# checking if an element exists in a tuple
my_tuple = ('a', 'p', 'p', 'l', 'e')

result = my_tuple.count('p')
print(result)      # Output: 2

result = my_tuple.index('p')
print(result)      # Output: 1