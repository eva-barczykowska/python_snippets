import module_example

module_example.greeting("Modules are a great way to organize and reuse code!")

# imported the whole module
# invoked the function using the module's name + function's name

print(module_example.person)
# accessed a specific key-value pair from the imported module

someone_special = module_example.person["name"]
print(someone_special)