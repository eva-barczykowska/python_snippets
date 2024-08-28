
# map(<function>, iterable)iterable
# TRANSFORMS THE ITEMS OF AN ITERABLE
# both map and filter can accept lambda functions as well as regular functions as arguments
# Examples

names = ["Alice", "Bob", "Charlie", "David", "Eve"]

def capitalize(name):
    return name.capitalize()


capitalized = map(capitalize, names)
# capitalized = list(capitalized)  # Uncomment to convert the map object to a list
print(type(capitalized))  # Output: <class 'map'>
print((capitalized))  # Output: <map object at 0x7f971496

# The map function takes 2 arguments: a function and an iterable (like a list or tuple).
# The map function returns a map object, not a list.

prices = [25.99, 15.58, 8.75]

def discount(price, discount=0.9):
    discounted_price = price * discount
    return discounted_price

discounted_prices = map(discount, prices)
discounted_prices = list(discounted_prices)
print(discounted_prices)  # O[23.391, 14.022, 7.875]

exam_scores = [85, 92, 78, 95, 22, 65]
def is_passing(score):
    return score >= 70

status = map(is_passing, exam_scores)
print(status)  # Output: <map object at 0x7f9714
print(list(status))  # Output: [True, True, True, True, False]

# lambda function can be directly provided as the first argument to map function
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # Output: [2, 4, 6, 8, 10]

# map function that adds 5 to each number
numbers = [1, 2, 3, 4, 5]
print(list(map(lambda x: x + 5, numbers)))  # Output: [6, 7, 8, 9, 10]
map(lambda x: x + 5, numbers)

# filter(<function>, iterable)
# RETURNS ITEMS THAT MEET THE CONDITION
products = ["Apple", "Banana", "Orange", "Pear", "Grape"]
filtered_products = list(filter(lambda name: name.startswith("B"), products))
print(filtered_products)  # Output: ['Banana']

prices = [25.99, 15.58, 8.7, 100]
filter(lambda price: price > 10, prices)
print(list(filter(lambda price: price > 10, prices)))  # Output [25.99, 15.58, 100]

products = { 'Table': 10_000, 'Chair': 20_000, 'Shelf': 15_000, 'Sofa': 30_000, 'Couch': 25_000, 'Lamp': 5_000 }
filtered_products = dict(filter(lambda item: item[1] > 20_000, products.items()))
# products.items() returns key-value paris as a list of tuples (key, value)
# in each tuple, item[1] is the value (price) and item[0] is the key (product name)
# dict_items([('Table', 10000), ('Chair', 20000), ('Shelf', 15000), ('Sofa', 30000), ('Couch', 25000), ('Lamp', 5000)])
print(filtered_products) # {'Sofa': 30000, 'Couch': 25000}

authors_and_books = { 'Dostoevsky': 'Crime and Punishment', 'Tolstoy': 'War and Peace', 'Rowling': 'Harry Potter'}
print(authors_and_books.items())
# produced list of tuples:
# dict_items([('Dostoevsky', 'Crime and Punishment'), ('Tolstoy', 'War and Peace'), ('Rowling', 'Harry Potter')])

names = ['John', 'Emma', 'Jake', 'Rachel', 'James']
filtered_names = list(filter(lambda name: name.startswith('J'), names)) # first we say HOW to filter and then WHAT
print(filtered_names)  # Output: ['John', 'Jake', 'James']