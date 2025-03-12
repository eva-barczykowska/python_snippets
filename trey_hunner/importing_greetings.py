# I will import greetings.py module to see what is the purpose of if __name__ == "__main__": block.

import greetings

print("The name of the module is:")
print(greetings.__name__)  # This will print 'greetings', name of the imported module.


# __name__ is a string representing the name of the current module.
# But we also get "Hello world!", which is not what we want.
# We get "Hello world!" when the imported greetings.py module doesn't have the if __name__ == "__main__": block.

# We don't want to print "Hello world!" when the greetings.py is being imported by another script.
# What's the solution? We can add a condition to check if the script is being run directly (not imported).
# This condition is checked by the Python interpreter when the script is run.
# The condition is if __name__ == "__main__": block