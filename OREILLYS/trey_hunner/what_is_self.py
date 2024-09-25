class Product:
    def __init__(self, name, cost, price):
        self.name = name
        self.cost = cost
        self.price = price

    def profit_margin(self):
        return self.price - self.cost


# duck = Product("rubber duck", 1, 5)
# without self an a parameter on line 2, we get an error:
# TypeError: Product.__init__() takes 3 positional arguments but 4 were given

# the first argument to every of our methods is self
# what is self? A reference to the current object instance
# self points to the instance of the class we are currently working with
# we only need to pass self when we are defining a method inside a class
# when we call a method on an object, python automatically passes self as the first argument

duck = Product("rubber duck", 1, 5)
print(duck)
print(type(duck))
print(duck.name)
print(duck.cost)
print(duck.price)
# print(duck.size)  # AttributeError: 'Product' object has no attribute 'size'
print(duck.profit_margin())  # 4

# When you call a method in python, python will pass in the class instance that you're calling the method on
# as the first argument to that method.
