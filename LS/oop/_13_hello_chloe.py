# Using the following code, add an instance method named rename that renames kitty when invoked.

class Cat:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    # This @name.setter below creates a "setter" method that's called whenever someone tries to assign a new value to the name
    # It allows you to write kitty.name = "Chloe" instead of having to use a separate method
    # This provides write access to the private _name attribute
    @name.setter
    def name(self, value):
        self._name = value

    def rename(self, new_name):  # just added another method named rename to demonstrate changing the attribute value
        self.name = new_name  # notice that it is without because we already have a setter method for name attribute


    # This is an alternative way to change the cat's name
    # It uses the setter property we defined above (that's why it doesn't need the underscore)
    # This method isn't strictly necessary since we have the setter, but it provides a more explicit way to rename the cat


# Comments show expected output
kitty = Cat('Sophie')
print(kitty.name)  # Sophie
kitty.rename('Chloe')
print(kitty.name)  # Chloe

# this is also possible so we have 2 ways to change the cat's name, using methods on line 14 and 18
kitty.name = 'Hermione'
print(kitty.name)  # Hermione

'''When we need controlled access to instance attributes, we often use property decorators(@property and @name.setter).
This lets us define getter and setter methods for the attribute, encapsulating it and providing 
controlled access to it.

The rename method in our Cat class uses the setter method for the name attribute to update the name.
Since the setter method is defined for the name attribute, we can assign a new value to it using standard attribute
assignment syntax (self.name = new_name), and the setter method will be automatically invoked.'''

# changes, testing what happens in git
