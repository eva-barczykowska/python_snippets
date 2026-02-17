# # dict.get()

# # This method returns the value for a specified key. If the key is not found,
# it returns None by default. It's important to note that this None is a meaningful return value (signifying "not found"),
# not an indicator that the method only performs a side effect.

# # print(my_dict.get('a'))                 # abc
# # print(my_dict.get('nothing'))           # None
# # print(my_dict.get('nothing', 'N/A'))    # N/A
# # print(my_dict.get('nothing', 100))      # 100

# # a dictionary
# # I know the values
# # how to get the KEY for the value
# # -get items, convert to a list, it will be a list of tuples
# # -[('a', 1) ('b', 2)]
# # -for key, value in one_tuple,
# # if value == target_value,
# # give me the key

# ###

# # Write a function character_frequency(string) that takes a string and returns a dictionary where keys are the characters and values are their frequencies. Your solution must use the dict.get() method to handle cases where a character is encountered for the first time. The function should be case-sensitive.

# # def character_frequency(string):
# #     string_casefold = string.casefold()
# #     dict_result = {}

# #     for char in string_casefold:
# #         if char not in dict_result:
# #             dict_result[char] = 1
# #         else:
# #             dict_result[char] += 1

# #     return dict_result

# def character_frequency(string):
#     string_casefold = string.casefold()
#     dict_result = {}

#     for char in string_casefold: # h e l l o
#         if not dict_result.get(char):
#             dict_result[char] = 1 # h e l o ' ' w d
#         else:
#             dict_result[char] += 1 # l o r l

#     return dict_result

# # -create an empty {}
# # -iterate over the string
# # -is this char there in this dictionary?
# # -dict.get('h')
# # -append 'h' and make the value 1

# # *init dictionary
# # *iterate over the string argument
# # *if the current char is not in the dictiory, add it and make value 1
# # *else if it is, add 1 to the key

# # # Test Case 1
# print(character_frequency("hello world"))
# # # Expected Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

# # # Test Case 2
# print(character_frequency("Programming is fun!"))
# # # Expected Output: {'P': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 2, 'n': 3, ' ': 2, 's': 1, 'f': 1, 'u': 1, '!': 1}

# # # Test Case 3
# print(character_frequency(""))
# # # Expected Output: {}

###

# You are given a list of dictionaries, where each dictionary represents a product. Not all product dictionaries have the same keys. Write a function get_product_property(products, product_name, property_key) that performs the following tasks:

# 1.  It searches the products list for a dictionary whose 'name' value matches the product_name.

# 2.  If the product is found, it should return the value of its property_key.

# 3.  If the product is found but does not have the property_key, the function should return the string "Property not found".

# 4. If no product with the given product_name is found in the list, the function should return the string "Product not found".

# You must use dict.get() to safely access the property_key.


# --if product is NOT THERE, return "Product not found"
# --if product is there but has no property, return "Property not found"
# --else product is found and property is found , it should return the value of its property key


# i have to get the product name but I have to look in ALL the dictionaries
# can i look in all the dictionaries at once?
# do I need to iterate over each dictionary and somehow retrieve the NAME of the product (which is the value and that is the problem?)

# go over each dictionary and check the value for the key 'name'
# if you iterate over all of them and that value is not found, return 'PRODUCT NOT FOUND'
# if the value corresponds to the target we're looking for, then dict.get the property
# if the property is not there, use the default param to return "Property not there"
# if the property is there, then just return it

products = [
    {'name': 'Laptop', 'price': 1200, 'stock': 15},
    {'name': 'Mouse', 'price': 25},
    {'name': 'Keyboard', 'price': 75, 'stock': 30, 'brand': 'Logi'},
]

def get_product_property(products, product_name, property_key):
    search_results = []

    for a_dictionary in products:
        search_results.append(a_dictionary.get('name'))

    if product_name not in search_results:
        return "Product Not Found"

    else:
        for one_dictionary in products:
            if one_dictionary['name'] == product_name:
                return one_dictionary.get(property_key, "Property Not Found")

# Test Case 1: Property exists
print(get_product_property(products, 'Laptop', 'stock'))
# Expected Output: 15

# Test Case 2: Property does not exist on the product
print(get_product_property(products, 'Mouse', 'stock'))
# Expected Output: "Property not found"

# # Test Case 3: Product does not exist
print(get_product_property(products, 'Monitor', 'price'))
# # # Expected Output: "Product not found"

# # Test Case 4: Another existing property
print(get_product_property(products, 'Keyboard', 'brand'))
# # Expected Output: "Logi"

# LS solution
def get_product_property(products, product_name, property_key):
    for product in products:
        if product.get('name') == product_name:
            return product.get(property_key, "Property not found")
    return "Product not found"
