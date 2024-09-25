class Product:
    def __init__(self, name, cost, price):
        self.name = name
        self.cost = cost
        self.price = price

    def profit_margin(self):
        return self.price - self.cost


duck = Product(name="rubber", cost=1, price=5)
# we've made a product instance and the variable 'duck' points to that instance'
# when I call the Product class I am:

# instantiating a (new) product instance
# constructing a new Product object
# making a Product -------3 ways to say the same thing

# a product instance, a product object and a product object are all the same thing.

# duck.
# we can access the data that's stored on this product instance by looking up its attributes
# You can access an attribute by taking a reference to the Product object (duck)
# and putting a dot (.) after it and then putting the name of the attribute

print(duck)  # rubber
print(type(duck))  # 4 which class is this object made from?
print(duck.name)  # rubber
print(duck.cost)  # 1
print(duck.price)  # 5

# atrybut, cecha, właściwość
# So we can ACCESS THE DATA on the class instance by looking at its ATTRIBUTES.
# But how can we perform actions on the class instance?
# We can do this by calling methods on the class instance.
# A method is a function that lives on a class and is designed to operate specifically on
# the instances of that class.

# Classes in python take data and methods and couple them together.
# We can make a class instance by calling a class.
# By calling the class we can get access to data by looking up attributes and
# we can perform actions on the data by calling methods.
