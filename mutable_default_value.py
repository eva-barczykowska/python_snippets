# def add_to_shopping_list(item, shopping_list=None):
#     shopping_list = shopping_list or []
#     shopping_list.append(item)
#     return shopping_list
#
# #case when the shopping list is provided, it adds the new item to the existing list
# food_groceries = ["Milk", "Eggs", "Bread"]
# output = add_to_shopping_list("Chocolate", food_groceries)

# print(output)
# # ['Milk', 'Eggs', 'Bread', 'Chocolate']
# print(food_groceries)
# # ['Milk', 'Eggs', 'Bread', 'Chocolate']

# case when the shopping list is not provided, it defaults to an empty list
# when the shopping list is not provided, it defaults to an empty list
# def add_to_shopping_list(item, shopping_list=None):
#     shopping_list = shopping_list or []
#     shopping_list.append(item)
#     return shopping_list
#
#
# output = add_to_shopping_list("Red lentis")
# print(output) #['Red lentis']

# no second argument
# def add_to_shopping_list(item, shopping_list=None):
#     shopping_list = shopping_list or [] # if shopping_list is None, it's assigned an empty list'
#     shopping_list.append(item)
#     return shopping_list
#
# output = add_to_shopping_list("Oculus 55")
# print(output)
# what happens is that an empty list is created and then the item is added to it


# case when the shopping list is provided but it is EMPTY
def add_to_shopping_list(item, shopping_list=None):
    shopping_list = shopping_list or [] # this second empty list is returned and saved to shopping_list
    print('id coming from inside the function is', id(shopping_list))
    # print(shopping_list) # [] empty list
    shopping_list.append(item) # we append the item to this empty list but the list exists only within this function scope
    print(shopping_list) # ['trekking shoes'] #yes, it exists but only within this function scope
    return shopping_list #we return the [] that we haven't worked with at all so it's empty'


clothes_for_scotland = []
print('id coming from outside the function:', id(clothes_for_scotland))
output = add_to_shopping_list("trekking shoes", clothes_for_scotland)
print(clothes_for_scotland)


# it has to analyze shopping_list or [],
# shopping_list = shopping_list or []
# shopping_list is an empty list so it evaluates to False
# now it needs to check [] after or, to know how this expression should evaluate
# [] is an empty list, so it evaluates to False
# we can check that these are not the same list by using id
# AND THAT EMPTY LIST IS RETURNED
# but this is not the list that we expect!!!

# But—and this is the key point—the or expression creates a new empty list rather than using the existing empty list
# (the one that clothes_for_scotland refers to).

# How to do so that it works as expected:
def add_to_shopping_list(item, shopping_list=None):
    if shopping_list is None: # if shopping_list is None, it's assigned an empty list' ,don't use or operator
        shopping_list = []
    shopping_list.append(item)
    return shopping_list

clothing_items = []
output = add_to_shopping_list("Shirt", clothing_items)

print(output)
# ['Shirt']
print(clothing_items)
# ['Shirt']