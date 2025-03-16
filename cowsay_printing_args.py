import sys
import cowsay

# if len(sys.argv) == 2:
#     print(cowsay.cow("Hello, " + sys.argv[1]))

# if len(sys.argv) == 2:
#     print(cowsay.trex("Hello, " + sys.argv[1]))

# if len(sys.argv) == 2:
#         print(cowsay.octopus("Hello, " + sys.argv[1])) # returns None

if len(sys.argv) == 2:
        cowsay.octopus("Hello, " + sys.argv[1])