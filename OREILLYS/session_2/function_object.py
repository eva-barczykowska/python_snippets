# number = input("Enter a number: ")
# if not number.isdigit:  # () missing!
#     print("It is NOT a number!")
# else:
#     print("It is a number!")

#  even if we enter a non-numeric value, it will still print "It is a number!"
# this is because theisdigit is missing () and therefore
# it returns a function object, which is True in this context

# corrected code:
number = input("Enter a number: ")
if not number.isdigit():  # () missing!
    print("It is NOT a number!")
else:
    print("It is a number!")
