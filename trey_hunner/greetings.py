import sys

def main():
    if len(sys.argv) == 2:  # One argument (besides the script name)
        name = sys.argv[1]
        print(f"Hello {name}!")
    elif len(sys.argv) == 1:  # No arguments (only the script name)
        print("Hello world!")
    else:
        print("Usage: python greetings.py [NAME]")

if __name__ == "__main__":
    main()

# now after I've included the code on lines 12-13, I will not see "Hello world!" when I import this module
# in importing_greetings.py file.
# but I need to run this importing_greetings.py file separately from the terminal to see the difference
