import sys

# print("My name is", sys.argv[0], sys.argv[2], sys.argv[3])

# when we execute a python script from the command line, we can also pass arguments to this program and
# those arguments will be stored in sys.argv list


# what is sys.argv[0]?
# sys.argv[0] is the name of the script/file that we're in

# print("------------")
#
# if len(sys.argv) < 3:
#     print("Too few arguments provided.")
# elif len(sys.argv) > 3:
#     print("Too many arguments provided.")
# else:
#     print("My name is ", sys.argv[1], sys.argv[2])

# print("------------")
#
# if len(sys.argv) < 2:
#     print("Too few arguments provided.")
# elif len(sys.argv) > 2:
#     print("Too many arguments provided.")
# else:
#     print("My name is", sys.argv[1])

# for this to work, I need to surround my name in quotes like so "Ewa Barczykowska
# python will treat this as a single argument then and will print it

# print("------------")
#
# if len(sys.argv) < 2:
#     print("Too few arguments provided.")
# elif len(sys.argv) > 2:
#     print("Too many arguments provided.")
#
# print("My name is", sys.argv[1])

# if I don't pass an argument, it will print "Too few arguments provided." BUT
# it will also cause an NameError because sys.argv[1] is not defined
# corrected:

# print("------------")
#
# if len(sys.argv) < 2:
#     sys.exit("Too few arguments provided.")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments provided.")
#
# print("My name is", sys.argv[1])

print("------------")
# I want to use multiple arguments, and I can have a loop to print them all

if len(sys.argv) < 2:
    sys.exit("Too few arguments provided.")

for arg in sys.argv[-1:0:-1]: # start from the last argument and go backwards, but DON'T include the first argument/argument at index 0
    print("My name is", arg) # list[start:stop:step]


