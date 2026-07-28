# A simple list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]

# A list of strings
words = ["apple", "banana", "cherry", "date", "elderberry", "fig"]

# A list of dictionaries, representing people
people = [
    {'name': 'Alice', 'age': 30, 'city': 'New York'},
    {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'},
    {'name': 'Charlie', 'age': 35, 'city': 'Chicago'},
    {'name': 'Diana', 'age': 25, 'city': 'New York'},
]

# A list of tuples, representing products (name, price, quantity)
products = [
    ('Laptop', 1200, 5),
    ('Mouse', 25, 10),
    ('Keyboard', 75, 8),
    ('Monitor', 300, 3),
]

# A simple class for Task objects
class Task:
    def __init__(self, description, priority, completed=False):
        self.description = description
        self.priority = priority
        self.completed = completed
    def __repr__(self):
        # A helper method to make printing tasks cleaner
        status = "X" if self.completed else " "
        return f"Task: '{self.description}' (P:{self.priority}) [{status}]"

# A list of Task objects
tasks = [
    Task('Buy groceries', 2, completed=False),
    Task('Clean the house', 1, completed=True),
    Task('Do laundry', 3, completed=False),
    Task('Walk the dog', 1, completed=False),
]

# A custom select function, similar to filter
def select(callback, iterable):
    return [item for item in iterable if callback(item)]

#print(list(map(lambda number: number ** 2, numbers))) # Return each number squared.

# print(list(filter(lambda n: n%2==0, numbers))) # Keep only the even numbers.

#print(sorted(words, key=len)) # Sort the words by length.

# print(list(map(lambda word: word.upper() , words))) # Return the uppercase version of each word.

#print(select(lambda task: task.completed, tasks)) # Keep only the completed tasks.

# print(max(people, key=lambda people: people['age'])) # Find the person with the highest age.

# print(sorted(products, key=lambda product: product[1])) # Sort the products by price (the second element in the tuple).

# print(list(map(lambda people: people['name'], people))) # Return a list of just the names of the people.

# print(list(filter(lambda number: number > 5 , numbers))) # Keep numbers that are greater than 5.

# print(list(map(lambda product: product[1] * product[2], products))) # For each product, return its total value (price * quantity).

# print(sorted(tasks, key=lambda task: task.priority, reverse=True)) #Sort tasks by their priority.
# print(list(filter(lambda word: word.startswith("c") , words))) # Keep only the words that start with the letter 'c'.

# print(list(filter(lambda person: person['age'] == 25 , people))) # Keep people who are 25 years old.

# print(list(map(lambda number: number%2==0, numbers))) # Return True for even numbers and False for odd numbers.
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0]

# print(sorted(people, key=lambda person: person['city'] ))# Sort people by city name.

# print(select(lambda task: task.completed==False, tasks)) # Keep only the tasks that are not completed.

# print(list(filter(lambda word: len(word) >= 5, words))) # Keep words with a length of 5 or more.

# print(list(map(lambda task: task.description, tasks))) # Return just the description of each task.

# print(list(filter(lambda number: number %3 == 0, numbers))) # Keep numbers that are divisible by 3.
# products = [
#     ('Laptop', 1200, 5),
#     ('Mouse', 25, 10),
#     ('Keyboard', 75, 8),
#     ('Monitor', 300, 3),
# ]
# print(sorted(products, key=lambda product: product[1] , reverse=True)) # Sort products by quantity, from highest to lowest.
# people = [
#     {'name': 'Alice', 'age': 30, 'city': 'New York'},
#     {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'},
#     {'name': 'Charlie', 'age': 35, 'city': 'Chicago'},
#     {'name': 'Diana', 'age': 25, 'city': 'New York'},
# ]
# print(list(filter(lambda person: len(person['name']) > 5, people))) # Keep people whose name is longer than 5 characters.

# print(list(map(lambda w: len(w), words))) # Return the length of each word.

# print(list(filter(lambda task: task.priority==1, tasks))) # Keep tasks with a priority of 1.

# words = ["apple", "banana", "cherry", "date", "elderberry", "fig"]
# print(max(words, key=len )) # Find the longest word.

# print(list(filter(lambda person: person['city'] == 'New York' and person['age']>25, people)))# Keep people who live in 'New York' and are older than 25.

# print(select(lambda task: task.priority >= 2, tasks)) # Keep tasks that are incomplete and have a priority of 2 or higher.

people = [
    {'name': 'Alice', 'age': 30, 'city': 'New York'},
    {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'},
    {'name': 'Charlie', 'age': 35, 'city': 'Chicago'},
    {'name': 'Diana', 'age': 25, 'city': 'New York'},
]

# print(sorted(people, key=lambda person: (person['age'], person['name']))) #Sort people first by age, then by name.

# products = [
#     ('Laptop', 1200, 5),
#     ('Mouse', 25, 10),
#     ('Keyboard', 75, 8),
#     ('Monitor', 300, 3),
# ]
# print(list(filter(lambda product: (product[1]<100 or product[2]>=10), products))) # Keep products where the price is less than 100 or the quantity is 10 or more (so either condition is enough!).

print(list(map(lambda person: f"{person['name']} is {person['age']} years old", people))) #Return a string for each person: "Name is Age years old".