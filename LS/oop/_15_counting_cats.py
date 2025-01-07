# Create a class named Cat that tracks the number of times a new Cat object is instantiated.
# The total number of Cat instances should be printed when total is invoked.

class Cat:
    total_number_of_cats = 0

    def __init__(self):
        Cat.total_number_of_cats += 1

    @classmethod
    def total(cls):  # the name of this method is a class method, not an instance method and
        print(Cat.total_number_of_cats)  # it has to be different from total_number of _cats  - class attribute


Cat.total()  # 0

kitty1 = Cat()
Cat.total()  # 1

kitty2 = Cat()
Cat.total()  # 2

print(Cat())  # <__main__.Cat object at 0x104ed7290>
Cat.total()  # 3
