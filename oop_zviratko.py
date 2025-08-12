class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print(f"{self.name}: {food} mi chutná!")


class Kitty(Animal): # the eat method is inherited
    def say_meow(self):
        print(f"{self.name}: Mňau!")




class Puppy(Animal): # tge eat method is inherited
    def bark(self):
        print(f"{self.name}: Haf!")


my_kitty = Kitty('Heloisa')
my_puppy = Puppy('Azorek')
my_kitty.say_meow()

my_puppy.bark()
my_kitty.eat('myš')
my_puppy.eat('kost')
print('---')
# using INHERITANCE to share behaviour in subclasses: Puppy and Kitty both eat
# I can also change the eat method in Kitty and even call the original method  like this:
# def eat(self, food): # overriding
#     print(f"({self.name} na {food} chvíli fascinovaně kouká)") # adding small extra functionality that was not there in parent class
#     super().eat(food) # calling the parent class eat method


print('---')
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print(f"{self.name}: {food} mi chutná!")


class Kitty(Animal): # the eat method is inherited
    def say_meow(self):
        print(f"{self.name}: Mňau!")

    def eat(self, food): # overriding
        print(f"({self.name} na {food} chvíli fascinovaně kouká)") # adding small extra functionality that was not there in parent class
        super().eat(food) # calling the parent class eat method



class Puppy(Animal): # tge eat method is inherited
    def bark(self):
        print(f"{self.name}: Haf!") # Puppy's eat method comes from parent class Animal

class Snake(Animal):
    def __init__(self, name):
        name = name.replace('s', 'sss') # for snake the name will be replaced with 'sss'
        name = name.replace('S', 'Sss')
        super().__init__(name)


my_snake = Snake('Stanislav')
my_snake.eat('myš')


my_kitty = Kitty('Heloisa')
my_puppy = Puppy('Azorek')

my_kitty.eat('myš')
my_puppy.eat('kost')