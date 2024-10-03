# Using the following code, add an instance method named rename that renames kitty when invoked.

class Cat:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def rename(self, new_name):  # just added another method named rename to demonstrate changing the attribute value
        self.name = new_name  # notice that it is without because we already have a setter method for name attribute

# Comments show expected output
kitty = Cat('Sophie')
print(kitty.name)             # Sophie
kitty.rename('Chloe')
print(kitty.name)             # Chloe

'''When we need controlled access to instance attributes, we often use property decorators(@peroperty and @name.setter).
This lets us define getter and setter methods for the attribute, encapsulating it and providing 
controlled access to it.

The rename method in our Cat class uses the setter method for the name attribute to update the name.
Since the setter method is defined for the name attribute, we can assign a new value to it using standard attribute
assignment syntax (self.name = new_name), and the setter method will be automatically invoked.'''

# changes, testing what happens in git