# The __init__.py file in Python is used to mark directories as Python packages.
# It serves two main purposes:

# Package initialization: When Python imports a package, it executes the code in the __init__.py file.
# This can be used to:
# perform setup tasks,
# define package-level variables,
# or import other modules.

# Module discovery: When a directory contains an __init__.py file, Python treats it as a package.
# This allows other modules to import modules from that directory using a dot notation,
# like import slsrestclient.module_name.
