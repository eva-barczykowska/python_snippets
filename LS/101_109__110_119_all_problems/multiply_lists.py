""" Write a function that takes two list arguments, each containing a list of numbers, and returns
a new list that contains the product of each pair of numbers from the arguments that have the same index.
You may assume that the arguments contain the same number of elements.

P:
-i have 2 lists, they become arguments
-func returns a new list
-in the list, we have products: each number from a1 is multiplied by a number from a2 (at the same index)

A:
-iterate over a1 and a2 and add consecutive elements
-can i iterate over both at the same time? 2 for loops
-3*9, 3*10, 3*11 # this will not work coz of this!!! it's looping the first element from list 1 with ALL of elements from list2
-5*9, 5*10, 5*11....


-zip?
--enumerate
"""

# list1 = [3, 5, 7]
# list2 = [9, 10, 11]
# print(multiply_list(list1, list2) == [27, 50, 77]  # True




# def multiply_list(list1, list2): # doesn't work! iterate was a good idea but NOT with a nested for loop
#     products = []
#     for a_index, a_number in enumerate(list1):
#         for b_index, b_number in enumerate(list2):
#             temp = list1[a_index] * list2[b_index]
#             products.append(temp)
#             print(products)
#     return(products)

def multiply_list(list1, list2):
    products = []
    zipped = list(zip(list1,list2))
    for a_tuple in zipped:
        products.append(a_tuple[0] * a_tuple[1])
    return products


list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True

#how would I solve this if I didn't know zip?
# can I iterate over both at the same time?
# use range(len)l1) to retrieve from both lists elements at a given index
# multiply elements at a given index
# append to products []
# even

def multiply_list(l1, l2):
    products = []
    for index in range(len(l1)):
        products.append(l1[index] * l2[index])
    return products

list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True

#similar logic with while

def multiply_list(l1, l2):
    products = []
    counter = 0
    while counter < len(list1):
        products.append(l1[counter] * l2[counter])
        counter += 1
    return products

list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True