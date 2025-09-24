# lazy iterables can be looped only once

my_dict = {'a': 1, 'b': 2, 'c': 3}
items = my_dict.items()
print((items))  # cannot do this coz dict_items is not an iterator
now_iterator = iter(items) # creating an iterator
print(type(iter(now_iterator))) #<class 'dict_itemiterator'>
print(next(now_iterator))  # ('a', 1)
print(next(now_iterator))  # ('b', 2)
print(next(now_iterator))  # ('c', 3)
# print(next(now_iterator))  # StopIteration error

# iterators are special lazy iterables that yield one item at a time/that work with next() function
# generators are a type of iterable, like lists or tuples.
# generators are easy way to make an iterator

# list object is not an iterator, but it can be converted to an iterator
my_list = [1, 2, 3]
my_list_iterator = iter(my_list)
print(type(my_list_iterator))  # <class 'list_iterator'>
print(next(my_list_iterator))  # 1

# You can build your own iterators for objects that don’t naturally support for ... in.
class CountDown:
    def __init__(self, start):
        self.n = start
    def __iter__(self):
        return self
    def __next__(self):
        if self.n <= 0:
            raise StopIteration
        self.n -= 1
        return self.n + 1

for i in CountDown(5):
    print(i)  # 5 4 3 2 1

# we can lazily load a file one line at a time
# enumerate function which is an iteration helper

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
e = enumerate(fruits)
print(e)
print(type(e))  # <class 'enumerate'>
print(next(e))  # (0, 'apple')

for i, fruit in e:
    print(f"Index is {i}, and fruit is {fruit}")

my_friends = ["Rachel", "Monica", "Chandler", "Joey", "Phoebe"]
for one_friend in my_friends:
    print(one_friend)

