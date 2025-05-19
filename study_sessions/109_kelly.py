

# x = f"I am in the global scope"

# def shadowing():
#     x = f"I am in the local scope"
#     print(x)

# print(shadowing())
# print(x)


# a = "hello"
# b = "hello"
# print(a is b)      #T

# c = [1, 2, 3]
# d = [1, 2, 3]
# print(c is d) #False    #F

# def outer():
#         x = 10
#         def inner():
#             nonlocal x #10 global vs nonlocal(pulling from a func to a subfunc)
#             x = 20
#         inner()
#         return x  #20

# print(outer())

# d = {"a": 1, "b": 2}
# d["a"] = 3  #{"a": 3, "b": 2}
# d["c"] = d.get("b", 0) + 1 #{"a": 3, "b": 2, "c": 3}
# print(d) #{"a": 3, "b": 2, "c": 3} "a": 3, "b": 2, "c": 3}

# numbers = [1, 2, 3, 4, 5]
# result = [num * 2 for num in numbers if num % 2 == 0]
# print(result) #[4, 8]

# def process_data(data):
#     if not data:
#         return
#     print(data[0]) #[10]
#     process_data(data[1:]) #slicing is mutating!

# process_data([10, 20, 30]) #[10], [20], [30]

# def strange_function(lst):
#   if not lst:
#        return []
#   return [lst[0]] + strange_function(lst[1:])

# print(strange_function([1, 2, 3, 4])) #[1, 2, 3, 4]

# a = [1, 2, 3]
# print(id(a))
# b = a.copy()
# print(id(b))
# a[0] = 10
# b.append(4)
# print(a) #[10, 2, 3, 4]
# print(id(a))
# print(b) #[1, 2, 3, 4]
# print(id(b))



# a = [[55, 12, 11], 1, 2]
# b = a.copy()
# a[0][0] = 10
# b.append(4)
# print(a) #[[10, 12, 11], 1, 2]
# print(b) #[[10, 12, 11], 1, 2, 4]

# def confused_function(x):
#     if x <= 1:
#         return 1
#     return x * confused_function(x - 1)

           
# # print(confused_function(x - 1)) #2 * 3 = 6
# print(confused_function(4))

# Execution (Step-by-Step):
# For confused_function(4):

# x = 4: 4 * confused_function(3)
# x = 3: 3 * confused_function(2)
# x = 2: 2 * confused_function(1)
# x = 1: Base case is reached, so return 1.

# Now substitute the return values back:

# confused_function(1) → 1
# confused_function(2) → 2 * 1 = 2
# confused_function(3) → 3 * 2 = 6
# confused_function(4) → 4 * 6 = 24

# 4! = 4 * 3 * 2 * 1 = 24

# items = [1, 2, 3, 4, 5]
# for index, item in enumerate(items):
#     if item % 2 == 0:
#         items.remove(item)
# print(items) #[1, 3, 5]

# [1, 3, 5]

# list1 = ["ewa", "kelly"]
# saved = enumerate(list1)
# print(list(saved))
# print(saved)

# items = [1, 2, 3, 4, 5]
# for index, item in enumerate(items):
#     if index % 2 == 0:
#         items.remove(item)
# print(items)

#     0. 1. 2. 3. 4.
# 1. [1, 2, 3, 4, 5] 0%2 =0, 1 is removed, asked about index 0

#     0. 1. 2. 3.
# 2. [2, 3, 4, 5] asking about index 1, 3%2 != 0.


#     0. 1. 2. 3.
# 3. [2, 3, 4, 5] asking about index 2, 4%2 = 0, 4 gets removed

#    0. 1. 2.  its takes into consideration index 4, why?
# 4. [2, 3, 5] it looks ahead at last index(index 4)
# #[2, 3, 5]



# try:
#     print("Step 1") #Step 1
#     x = 10 / 0
#     print("Step 2")
# except ZeroDivisionError:
#     print("Step 3") #Step 3
# finally:
#     print("Step 4") #Step 4
#     print("Step 5") #Step 5

# def apply_operation(op, x, y):
#     return op(x, y)

# def add(a, b):
#     return a + b

# def multiply(a, b):
#     return a * b

# print(apply_operation(add, 5, 3))
# print(apply_operation(multiply, 5, 3))

# a = 5
# b = 10

# a, b = b, a + b #5, 10  10, 15. |10, 15
# print(a, b)

# def tricky_calculation(n):
#     result = 0
#     for i in range(n): #0, 1, 2, 3
#         result += i #0 + 1 + 3  |1, 3, 9
#         if i % 2 == 0:
#             continue
#         result *= 2 #0 + 2 + 6 | 2, 6, 18
#     return result
#
# print(tricky_calculation(5))

#same snippets with AMY
# items = [1, 2, 3, 4, 5]
# for index, item in enumerate(items):
#     if item % 2 == 0:
#         items.remove(item)
# print(items)

# [(0, 'ewa'), (1, 'kelly'), (2, 'amy')]

# list1 = ["ewa", "kelly", "amy"]
# saved = enumerate(list1)
# print(saved)


# {0: 'ewa', 1: 'kelly', 2: 'amy'}

# items = [1, 2, 3, 4, 5, 7, 7] # INDEX
# for index, item in enumerate(items): # 0, 1, 2, 3, 4
#     if index % 2 == 0:
#         items.remove(item)
# print(items) # [2, 3, ]

# 0 -> 1 -> deleted -> [2, 3, 4, 5, 7]
# 1 -> 3 -> kept -> [2, 3, 4, 5, 7, 7] #iteraton STOPS
# 2 -> 4 -> deleted -> [2 ,3, 5, 7, 7]
# 3 -> 7 -> kept [2 ,3, 5, 7, 7]
# 4 -> 7 -> deleted



# items = [0, 10, 20, 30, 40]
# for index, item in enumerate(items): # 0, 1, 2, 3, 4
#     print('before')
#     print(f"items: {items}")
#     print(f"item: {item} at this index: {index}")
#     print('----')
#     print('after')
#     if index % 2 == 0:
#         items.remove(item)
#         print(f"items: {items}")
#         print(f"item: {item} at this index: {index}")
# print(items)

# try:
#     print("Step 1")
#     x = 10 / 0
#     print("Step 2")
# except ZeroDivisionError:
#     print("Step 3")
# finally:
#     print("Step 4")
#     print("Step 5")

# def apply_operation(op, x, y):
#     return op(x, y)

# def add(a, b):
#     return a + b

# def multiply(a, b):
#     return a * b

# print(apply_operation(add, 5, 3))
# print(apply_operation(multiply, 5, 3)) # more examples


# def tricky_calculation(n):
#     result = 0
#     for i in range(n): #range 0, 1, 2, 3,4
#         result += i
#         if i % 2 == 0:
#             continue
#         result *= 2
#     return result
#
# print(tricky_calculation(5))

#range 0, 1, 2, 3,4
# 0-> 0+0 = 0, condition true, continue,
# 1-> 0+1 = 1, condition fase, 1*2 = 2, result is 2
# 2-> 2+2 = 4, condition true, continue
# 3-> 4+3 = 7, condition false, result is 14
# 4-> 14+4 = 18 condiiton true, continue

# items = [1, 2, 3, 4, 5]
# for index, item in enumerate(items): # 0, 1, 2, 3, 4
#     if index % 2 == 0:
#         items.remove(item)
# print(items)

# items = [1, 2, 3, 4, 5]
# for index, item in enumerate(items):
#     if item % 2 == 0:
#         items.remove(item)
# print(items)

# [(0, 'ewa'), (1, 'kelly'), (2, 'amy')]

# list1 = ["ewa", "kelly", "amy"]
# saved = enumerate(list1)
# print(saved)


# {0: 'ewa', 1: 'kelly', 2: 'amy'}

# items = [1, 2, 3, 4, 5, 7, 7] # INDEX
# for index, item in enumerate(items): # 0, 1, 2, 3, 4
#     if index % 2 == 0:
#         items.remove(item)
# print(items) # [2, 3, ]

# 0 -> 1 -> deleted -> [2, 3, 4, 5, 7]
# 1 -> 3 -> kept -> [2, 3, 4, 5, 7, 7] #iteraton STOPS
# 2 -> 4 -> deleted -> [2 ,3, 5, 7, 7]
# 3 -> 7 -> kept [2 ,3, 5, 7, 7]
# 4 -> 7 -> deleted



# items = [0, 10, 20, 30, 40]
# for index, item in enumerate(items): # 0, 1, 2, 3, 4
#     print('before')
#     print(f"items: {items}")
#     print(f"item: {item} at this index: {index}")
#     print('----')
#     print('after')
#     if index % 2 == 0:
#         items.remove(item)
#         print(f"items: {items}")
#         print(f"item: {item} at this index: {index}")
# print(items)

# try:
#     print("Step 1")
#     x = 10 / 0
#     print("Step 2")
# except ZeroDivisionError:
#     print("Step 3")
# finally:
#     print("Step 4")
#     print("Step 5")

# def apply_operation(op, x, y):
#     return op(x, y)

# def add(a, b):
#     return a + b

# def multiply(a, b):
#     return a * b

# print(apply_operation(add, 5, 3))
# print(apply_operation(multiply, 5, 3)) # more examples


# def tricky_calculation(n):
#     result = 0
#     for i in range(n): #range 0, 1, 2, 3,4
#         result += i
#         if i % 2 == 0:
#             continue
#         result *= 2
#     return result

# print(tricky_calculation(5))

#range 0, 1, 2, 3,4
# 0-> 0+0 = 0, condition true, continue,
# 1-> 0+1 = 1, condition fase, 1*2 = 2, result is 2
# 2-> 2+2 = 4, condition true, continue
# 3-> 4+3 = 7, condition false, result is 14
# 4-> 14+4 = 18 condiiton true, continue

# items = [1, 2, 3, 4, 5]
# for index, item in enumerate(items):
#     if index % 2 == 0:
#         items.remove(item)
# print(items)

# items = [1, 2, 3, 4, 5]
# items = [item for index, item in enumerate(items) if index % 2 != 0]
# print(items)  # Output: [2, 4]

# def modify(x):
#     x = 10
#     return x

# num = 5
# new_num = modify(num)
# print(new_num)

# def append_item(lst):
#     lst.append(4)
#     return lst

# my_list = [1, 2, 3]
# append_item(my_list)
# print(my_list) #[1,2,3,4]

# def add_greeting(s):
#     s += ", World!"
#     # return s

# text = "Hello"
# text = add_greeting(text)
# print(text) #None


# def reassign(lst):
#     lst = [10, 20, 30]

# numbers = [5, 6, 7]
# reassign(numbers) #on line 123 we have reassign numbers
# print(numbers)#[10, 20, 30] #[5, 6, 7]
# #Reassigning lst inside the function creates a new local list. The original numbers remains unchanged.

# def modify_tuple(t):
#     t[0] = 99  # Will this work? This will not work!

# my_tuple = (1, 2, 3) #tuples are immutable!
# modify_tuple(my_tuple) #a pointless call     #TypeError
# print(my_tuple)


# def update_dict(d):
#     d["key"] = "new_value"


# data = {"key": "old_value"}
# update_dict(data)
# print(data) #{"key": "new_value"}

# def func(a, b):
#     a = 100
#     b.append(5)

# x = 1
# y = [2]
# func(x, y)
# print(x, y) # 1, [2, 5]  |

# def change_nested(lst):
#     lst[1][0] = "modified"

# matrix = [[1, 2], [3, 4]]
# change_nested(matrix)
# print(matrix) # [[1, 2], ["modified", 4]]


# text = 'Hello! I am Eloise.'

# def swap(s):
#     for char in s:
#        s =  s.replace(char, char.upper())
#     return s

# print(swap(text)) #Hello! I am Eloise.'
# print(text) #Hello! I am Eloise.'

# text = 'Hello! I am Eloise.'

# def swap(s):
#     for char in s:
#        s.replace(char, char.upper())
#     return s

# print(swap(text)) #Hello! I am Eloise.'
# print(text) #Hello! I am Eloise.'

# def process(lst):
#     lst = lst + [4]  # Reassignment
#     return lst
#     #lst += [4]     # What if this line were used instead?

# original = [1, 2, 3]
# original = process(original)
# print(original) # [1, 2, 3, 4]

#lst + [4] creates a new list, leaving original unchanged. If lst += [4] were used, it would modify the original list in-place.

# def process(lst):
#     lst = lst + [4]  # Reassignment
#     #lst += [4]     # What if this line were used instead?

# original = [1, 2, 3]
# process(original)
# print(original) # [1, 2, 3, 4]

# def add_item(item, lst=[]):
#     lst.append(item)
#     return lst

# print(add_item(1)) # [1]     | [1]
# print(add_item(2)) # [1,2]   | [1,2]


# x = 10
# def my_function(num):
#     print(num)
# my_function(x)

#------

# def change_value(num):
#     num = num + 5
#     return num

# value = 10
# value = change_value(value)
# print(value)

#------

# a = [1, 2, 3]
# b = a
# b.append(4)
# print(a) #[1,2,3,4]

#------

# def outer_function():
#     x = "local"

#     def inner_function():
#         print(x)

#     inner_function() #output "local"

# outer_function()

#------
# def modify_string(text, value):
#     text += value
#     return text

# greeting = "Hello"
# greeting = modify_string(greeting, ", World!")
# print(greeting)

#------

# numbers = [1, 2, 3]

# def process_list(lst):
#     lst = lst.copy()
#     lst.append(4)
#     return lst

# result = process_list(numbers)
# print(numbers) #[1,2,3]
# print(result) #[1,2,3,4]

# if you see a nested list and copy(), you know you're screwed

#------

# def update_counters():
#     global counter1
#     counter1 = 10
#     counter2 = 20

# counter1 = 1
# counter2 = 2
# update_counters()
# print(counter1, counter2) #10, #2

#------

# def strange_function():
#         if False: #what is considered here? Params?
#             weird_var = 100

#         try:
#             print(weird_var)
#         except NameError:
#             print("Variable doesn't exist")

# strange_function()

# in Python, cond will execute ONLY if it evaluates to TRUE

#------

# lst = [1, 2, 3] #->[2, 3] -> [2,3] ->IndexError
# print(list(range(len(lst))))

# def empty_list(lst):
#     for idx in range(len(lst)): #0, 1, 2 range(0,3)
#         lst.pop(idx) # #0, 1, 2
#         print(lst) #[2, 3]->[2]->Index error
#     return lst

# print(empty_list(lst)) #[1, 2, 3]
# print(lst) # [1, 2, 3]

#The issue with the code is that modifying a list while iterating over it using its indices can lead to unexpected behavior. When you remove an element from the list using pop(idx), the indices of the subsequent elements are shifted, which can cause elements to be skipped or lead to an IndexError.

# POP removes the index!!! you pass it in!
# remove removes the argument-value you pass it in!


#fix
# def empty_list(lst):
#     for _ in range(len(lst)): #0, 1, 2
#         lst.pop()
#         print(lst)
#     return lst

# print(empty_list(lst))
# print(lst)

#------

# lst1 = [0, 1, 2, 3]
# lst2 = lst1.reverse() and lst1.reverse() # mut methods often return None
# if lst2:
#     print(lst2)
# else:
#     print(lst1) #MUTATED list!

#-----------------------------------------------------------------------------------------------------------------------
#snippets prepared for your exam!



#Pls always say what concept?
# y = "global"

# def test():
#     y = "local"
#     print(y)

# test()
# print(y)


# ---

#2.

# x = [1, 2]
# y = [1, 2]
# print(x == y)
# print(x is y)

# x = "banana"
# y = "banana"
# print(x == y)
# print(x is y)
# ---

# ## 3

# def outer():
#     z = 5
#     def inner():
#         nonlocal z
#         z += 1
#     inner()
#     return z

# print(outer())


# ---

# ## 4.

# info = {"name": "Sam"}
# info["age"] = 30
# info["name"] = info.get("name", "") + " Smith"
# print(info)


# ---

# ## 5.
# nums = [2, 3, 4, 5]
# squares = [n**2 for n in nums if n % 2 == 0]
# print(squares)

# ---

# ## 6.

# def recursive_sum(lst):
#     if not lst:
#         return 0
#     return lst[0] + recursive_sum(lst[1:])

# print(recursive_sum([1, 2, 3]))

# ---

# ## 7.
# lst1 = [1, 2]
# lst2 = lst1
# lst3 = lst1.copy()
# lst1.append(3)
# print(lst2)
# print(lst3)


# ---

# ## 8.

# a = [[1, 2], 3]
# b = a.copy()
# a[0][1] = 99
# print(b)


# ---

# ## 9.
# def fact(n):
#     if n <= 1:
#         return 1
#     return n * fact(n - 1)

# print(fact(5))


# ---
# ## 10. Removing Items While Iterating

# items = [1, 2, 3, 4]
# for item in items[:]:
#     if item % 2 == 0:
#         items.remove(item)
# print(items)



# ## 11.

# names = ["Anna", "Bob"]
# enum_names = list(enumerate(names))
# print(enum_names)


# ## 12.

# try:
#     print("A")
#     1 / 0
#     print("B")
# except ZeroDivisionError:
#     print("C")
# finally:
#     print("D")


# ---

# def subtract(a, b):
#     return a - b

# def operate(func, x, y):
#     return func(x, y)

# print(operate(subtract, 10, 3))




# ## 14.

# def try_modify(t):
#     try:
#         t[1] = 5
#     except TypeError:
#         print("This happening but why?")

# t = (1, 2, 3)
# try_modify(t)


# ---

# ## 15.

# def add_to_list(val, lst=[]):
#     lst = [101]
#     lst.append(val)
#     return lst

# print(add_to_list("x"))
# print(add_to_list("y"))


# ---

# def add_to_list(val, lst=[]):
#     lst = [101]
#     lst.append(val)
#     return lst

# print(add_to_list("x"))
# print(add_to_list("y"))


# ## 16. Global Keyword

# count = 0

# def increase():
#     global count
#     count += 1

# increase()
# print(count)



## 17.

# def change_first(lst):
#     lst[0][0] = "changed"

# matrix = [[0, 1], [2, 3]]
# change_first(matrix)
# print(matrix)


# ---

## 18.
# def shout(s):
#     s = s.upper()
#     return s

# msg = "hello"
# print(shout(msg))
# print(msg)


# ---

# ## 19.

# def calc(n):
#     res = 1
#     for i in range(1, n+1): # 1, 2, 3, 4, 5
#         if i % 2 == 0:
#             continue
#         res *= i # 1*3=3, 3*5=15
#     return res

# print(calc(5))


# ---

# ## 20.

# def maybe_mutate(lst):
#     lst += [99]
#     # print(f"List is now {lst}")
#     return lst

# a = [1, 2]
# maybe_mutate(a)
# print(a)

# ---

# ### Bonus: Reassignment in Function Does Not Affect Original

# def reassign_list(lst):
#     lst = [0]
#     return lst

# orig = [1, 2]
# reassign_list(orig)
# print(orig)

# my_list = [55, 66, 77]
# print(my_list.remove(66))

# my_list = [55, 66, 77]
# my_list.pop(66)
# print(my_list)

# my_list = [55, 66, 77]
# print(my_list.pop(1))

# info = {"name": "Sam"}
# info["age"] = 30
# retrieved = info.get("name", "") + " Smith"
# print(retrieved)

# my_values = ("connection", "attunment")
# new_values = []
# for value in my_values:
#     new_values.append(value + " $$$")

# print(my_values)
# print(new_values)

# my_assets = ("inner and outer beauty", "inredible talent")
# my_assets[1] = "bottomless riches"

# my_assets = ("inner and outer beauty", "inredible talent")
# my_reviewed_assets= my_assets[:] + (" bottomless riches",)

# print(my_reviewed_assets)

# my_assets = ("inner and outer beauty", "inredible talent")
# my_reviewed_assets= my_assets[:] + (" bottomless riches")

# print(my_reviewed_assets)

# my_assets = ("inner and outer beauty", "inredible talent")
# my_reviewed_assets= my_assets[:] + (" bottomless riches", "huuuge inheritance")

# print(my_reviewed_assets)


# my_assets = ("inner and outer beauty", "inredible talent")
# my_reviewed_assets= my_assets[:] + " bottomless riches"

# print(my_reviewed_assets)