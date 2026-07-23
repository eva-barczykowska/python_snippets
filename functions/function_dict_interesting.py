def function_one(text):
    print("Coming from function_one: ", text)


def function_two(text):
    print("Coming from function_two: ", text)


# what is interesting here?
# the dictionary contains function references, but these functions are not executed directly
my_dict = {'a': function_one,  # 'a' is a key in the dictionary, 'MyFunction' is the value
           'b': function_two}  # Create a dictionary with function references

if __name__ == '__main__':
    print(__name__)  # __name__ is set to '__main__' when this script is run directly

    my_dict['a']('ahoy')  # call the function stored in the dictionary with key 'a'
    my_dict['b']('svete')  # call the function stored in the dictionary with key 'b'
