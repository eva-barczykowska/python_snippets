# Assume you have the following code:

# class House:
#     def __init__(self, price):
#         self._price = price

#     @property
#     def price(self):
#         return self._price

#     @price.setter
#     def price(self, value):
#         self._price = value

#     def __lt__(self, other): # less than
#         if isinstance(other, House):
#             return self._price < other._price  # Invert the comparison
#         return NotImplemented

#     def __gt__(self, other): # greater than
#         if isinstance(other, House):
#             return self._price > other._price  # Invert the comparison
#         return NotImplemented


# home1 = House(100000)
# home2 = House(150000)
# if home1 < home2:
#     print("Home 1 is cheaper")
# if home2 > home1:
#     print("Home 2 is more expensive")
# and this output:


# Home 1 is cheaper
# Home 2 is more expensive

# Modify the House class so the above program work as shown.

# Implement a Wallet class that represents a wallet with a certain amount of money. You want to be able to combine (add) two wallets together to get a new wallet with the combined total amount from both wallets.

# class Wallet:
#     def __init__(self, money_inside):
#         self._money_inside = money_inside

#     @property
#     def money_inside(self):
#         return self._money_inside

#     @money_inside.setter
#     def money_inside(self, value):
#         self._money_inside = value

#     def __add__(self, other):
#         return Wallet(self._money_inside + other._money_inside)

# wallet1 = Wallet(50)
# wallet2 = Wallet(30)
# merged_wallet = wallet1 + wallet2
# print(merged_wallet.money_inside == 80)       # True

# Using the code from the previous exercise, modify the code so that when we print the merged_wallet we receive a message Wallet with $80.

# class Wallet:
#     def __init__(self, amount):
#         self.amount = amount

#     def __add__(self, other):
#         return Wallet(self.amount + other.amount)

#     def __str__(self):
#         return f"Wallet with ${self.amount}"


# wallet1 = Wallet(50)
# wallet2 = Wallet(30)
# merged_wallet = wallet1 + wallet2
# print(merged_wallet)          # Wallet with $80.

# Reverse Engineering

# Write a class such that the following code prints the results indicated by the comments:

# class Transform:
#     def __init__(self, string):
#         self.string = string

#     def uppercase(self):
#         return self.string.upper()

#     # def lowercase(self):
#     #     return self.string.lower()

#     @classmethod
#     def lowercase(cls, string):
#         return string.lower()

# my_data = Transform('abc')
# print(my_data.uppercase())              # ABC
# print(Transform.lowercase('XYZ'))       # xyz

# # Circular Buffer

# # A circular buffer is a collection of objects stored in a buffer that is treated as though it is connected end-to-end in a circle. When an object is added to this circular buffer, it is added to the position that immediately follows the most recently added object, while removing an object always removes the object that has been in the buffer the longest.

# # This works as long as there are empty spots in the buffer. If the buffer becomes full, adding a new object to the buffer requires getting rid of an existing object; with a circular buffer, the object that has been in the buffer the longest is discarded and replaced by the new object.

# # Assuming we have a circular buffer with room for 3 objects, the circular buffer looks and acts like this:

# P1    P2    P3    Comments
# All positions are initially empty
# 1            Add 1 to the buffer
# 1    2        Add 2 to the buffer

# 2        Remove oldest item from the buffer (1)
# 2    3    Add 3 to the buffer

# 4    2    3    Add 4 to the buffer, buffer is now full
# 4        3    Remove oldest item from the buffer (2)
# 4    5    3    Add 5 to the buffer, buffer is full again
# 4    5    6    Add 6 to the buffer, replaces oldest element (3)
# 7    5    6    Add 7 to the buffer, replaces oldest element (4)
# 7        6    Remove oldest item from the buffer (5)
# 7            Remove oldest item from the buffer (6)
# Remove oldest item from the buffer (7)
# Remove non-existent item from the buffer (nil)

# Your task is to write a CircularBuffer class in Python that implements a circular buffer for arbitrary objects. The class should be initialized with the buffer size and provide the following methods:

# put: Add an object to the buffer
# get: Remove (and return) the oldest object in the buffer. Return None if the buffer is empty.
# You may assume that none of the values stored in the buffer are None (however, None may be used to designate empty spots in the buffer).

# Examples

class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity

    def get(self):
        return queue[-1]


buffer = CircularBuffer(3)
# print(buffer.capacity)

print(buffer.queue)

print(buffer.get() is None)  # True

# buffer.put(1)
# buffer.put(2)
# print(buffer.get() == 1)             # True

# buffer.put(3)
# buffer.put(4)
# print(buffer.get() == 2)             # True

# buffer.put(5)
# buffer.put(6)
# buffer.put(7)
# print(buffer.get() == 5)             # True
# print(buffer.get() == 6)             # True
# print(buffer.get() == 7)             # True
# print(buffer.get() is None)          # True

# buffer2 = CircularBuffer(4)

# print(buffer2.get() is None)         # True

# buffer2.put(1)
# buffer2.put(2)
# print(buffer2.get() == 1)            # True

# buffer2.put(3)
# buffer2.put(4)
# print(buffer2.get() == 2)            # True

# buffer2.put(5)
# buffer2.put(6)
# buffer2.put(7)
# print(buffer2.get() == 4)            # True
# print(buffer2.get() == 5)            # True
# print(buffer2.get() == 6)            # True
# print(buffer2.get() == 7)            # True
# print(buffer2.get() is None)         # True
# # The above code should display True 15 times.

