import sys

# print("My name is", sys.argv[0], sys.argv[2], sys.argv[3])

# when we execute a python script from the command line, we can also pass arguments to this program and
# those arguments will be stored in sys.argv list


# what is sys.argv[0]?
# sys.argv[0] is the name of the script/file that we're in

print("------------")
if len(sys.argv) < 2:
    print("Too few arguments provided.")
elif len(sys.argv) > 2:
    print("Too many arguments provided.")
else:
    print("My name is ", sys.argv[1], sys.argv[2])