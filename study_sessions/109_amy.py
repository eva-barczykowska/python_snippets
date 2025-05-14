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

items = [1, 2, 3, 4, 5]
for index, item in enumerate(items):
    if index % 2 == 0:
        items.remove(item)
print(items)

# items = [1, 2, 3, 4, 5]
# items = [item for index, item in enumerate(items) if index % 2 != 0]
# print(items)  # Output: [2, 4]