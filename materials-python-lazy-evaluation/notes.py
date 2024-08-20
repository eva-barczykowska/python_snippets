# Eager evaluation
# Lazy evaluation

# Eager evaluation refers to those cases when Python evaluates an expression as soon as it encounters it.
# Here are some examples of expressions that are evaluated eagerly:
# execute in python shell:

# >>> 5 + 10
# 15


# >>> import random
# >>> random.randint(1, 10)
# 4

# The import statement includes the keyword import followed by the name of a module. The module name random is evaluated eagerly.
# The function call random.randint() is evaluated eagerly, and its value is returned immediately.
# All standard functions are evaluated eagerly. You’ll learn about generator functions later, which behave differently.

# >>> [2, 4, 6, 8, 10]
# [2, 4, 6, 8, 10]
# >>> numbers = [2, 4, 6, 8, 10]
# >>> numbers
# [2, 4, 6, 8, 10]

# Lazy evaluation refers to cases when Python doesn’t work out the values of an expression immediately.
# Instead, the values are returned at the point when they’re required in the program.
# Lazy evaluation can also be referred to as call-by-need.

# An example of lazy evaluation occurs within the for loop when you iterate using range():

# for index in range(1, 1_000_001):
#     print(f"This is iteration {index}")

# The built-in range() is the constructor for Python’s range object.
# The range object does not store all of the one million integers it represents.
# Instead, the for loop creates a range_iterator from the range object, which generates the next number in the sequence
# when it’s needed. Therefore, the program never needs to have all the values stored in memory at the same time.
#
# Lazy evaluation also allows you to create infinite data structures, such as a live stream of audio or video data
# that continuously updates with new information, since the program doesn’t need to store
# all the values in memory at the same time.
# Infinite data structures are not possible with eager evaluation since they can’t be stored in memory.
#
# There are disadvantages to deferred evaluation.
# Any errors raised by an expression are also deferred to a later point in the program.
# This delay can make debugging harder.

# The Python built-ins zip() and enumerate() create two powerful built-in data types.
# These data types are linked to lazy evaluation.
# Example:
# You need to create a weekly schedule, or rota, that shows which team members will bring coffee in the morning.
#
# However, the coffee shop is always busy on Monday mornings and no one wants to be responsible for Mondays.
# So you decide to randomize the rota every week. You start with a list containing the team members’ names:

>>> names = ["Sarah", "Matt", "Jim", "Denise", "Kate"]

>>> import random
>>> random.shuffle(names)
>>> names
['Sarah', 'Jim', 'Denise', 'Matt', 'Kate']

# You also shuffle the names using random.shuffle(), which changes the list in place.
# It’s time to create a numbered list to pin to the notice board every week:

# >>> for index, name in enumerate(names, start=1):
# ...     print(f"{index}. {name}")
#
# 1. Sarah
# 2. Jim
# 3. Denise
# 4. Matt
# 5. Kate

# You use enumerate() to iterate through the list of names and also access an index as you iterate.
# By default, enumerate() starts counting from zero. However, you use the start argument to ensure the first number is one.
#
# But what does enumerate() do behind the scenes?
# To explore this, you can call enumerate() and assign the object it returns to a variable name:

# >>> numbered_names = enumerate(names, start=1)
# >>> numbered_names
# <enumerate object at 0x11b26ae80>

# The object created is an enumerate object, which is an iterator.
# Iterators are one of the key tools that allow Python to be lazy since their values are created on demand.
# The call to enumerate() pairs each item in names with an integer.

# However, it doesn’t create those pairs immediately.
# The pairs are not stored in memory. Instead, they’re generated when you need them.
# One way to evaluate a value from an iterator is to call the built-in function next():

>>> next(numbered_names)
(1, 'Sarah')
>>> next(numbered_names)
(2, 'Jim')

# The numbered_names object doesn’t contain all the pairs within it.
# When it needs to create the next pair of values, it fetches the next name from the original list names and pairs it up
# with the next integer.
# You can confirm this by changing the third name in the list names before fetching the next value in numbered_names:

>>> names[2] = "The Coffee Robot"
>>> next(numbered_names)
(3, 'The Coffee Robot')

# Even though you created the enumerate object numbered_names before you changed the contents of the list,
# you fetch the third item in names after you made the change. This behavior is possible because
# Python evaluates the enumerate object lazily.
#
# Look back at the numbered list you created earlier with the for loop, which shows Sarah is due to buy coffee first.
# Sarah is a Python programmer, so she enquired whether the 1 next to her name means she should buy coffee on Tuesday
# since Monday ought to be 0.
#
# You decide not to get angry. Instead, you update your code to use zip() to pair names with weekdays instead of numbers.
# Note that you recreate and shuffle the list again since you have made changes to it:

>>> names = ["Sarah", "Matt", "Jim", "Denise", "Kate"]
>>> weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
>>> random.shuffle(names)
>>> names
['Denise', 'Jim', 'Sarah', 'Matt', 'Kate']

>>> for day, name in zip(weekdays, names):
...     print(f"{day}: {name}")
...
Monday: Denise
Tuesday: Jim
Wednesday: Sarah
Thursday: Matt
Friday: Kate

# When you call zip(), you create a zip object, which is another iterator.
# The program doesn’t create copies of the data in weekdays and names to create the pairs.
# Instead, it creates the pairs on demand. This is another example of lazy evaluation.
# You can explore the zip object directly as you did with the enumerate object:

>>> day_name_pairs = zip(weekdays, names)
>>> next(day_name_pairs)
('Monday', 'Denise')
>>> next(day_name_pairs)
('Tuesday', 'Jim')

>>> # Modify the third item in 'names'
>>> names[2] = "The Coffee Robot"
>>> next(day_name_pairs)
('Wednesday', 'The Coffee Robot')

# Iterators are lazy data structures since their values are evaluated when they’re needed
# and not immediately when you define the iterator.
# There are many more iterators in Python besides enumerate and zip.
# Every iterable is either an iterator itself or can be converted into an iterator using iter().

# Rest of information (about generators, etc.) can be found at https://realpython.com/python-lazy-evaluation/