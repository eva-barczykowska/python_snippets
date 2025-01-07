# Using the following code, add 2 methods, generic_greeting and personal_greeting. The first method should be
# a class method tan dpring a greeting that's generic to the class. The second method should be an instanc method
# that prints a greeting custom to the object:
class Cat:
    def __init__(self, name):
        self._name = name

    @property  # gives us a getter for _name, gives us access to _name without directly accessing it
    def name(self):
        return self._name

    @classmethod
    def generic_greeting(cls):
        print("Hello! I'm a cat!")

    def personal_greeting(self):
        print(f"Hello! My name is {self.name}!")
    # we can do {self.name} because we have a @property getter named name

    # we can also do
    # def personal_greeting(self):
    #     print(f"Hello! My name is {self._name}!")


kitty = Cat('Sophie')

Cat.generic_greeting()  # Hello! I'm a cat!'
kitty.personal_greeting()  # Hello! My name is Sophie!
