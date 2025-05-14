

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

def tricky_calculation(n):
    result = 0
    for i in range(n): #0, 1, 2, 3
        result += i #0 + 1 + 3  |1, 3, 9
        if i % 2 == 0:
            continue
        result *= 2 #0 + 2 + 6 | 2, 6, 18
    return result

print(tricky_calculation(5))

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

items = [1, 2, 3, 4, 5]
for index, item in enumerate(items): # 0, 1, 2, 3, 4
    if index % 2 == 0:
        items.remove(item)
print(items)

