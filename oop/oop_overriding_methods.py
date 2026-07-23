class Animal:
    def sleep(self):
        print("This animal can sleep")

    def eat(self):
        print("This animal can eat")


class Bird(Animal):
    def fly(self):
        print("This bird can fly")


class Fish(Animal):
    def swim(self):
        print("This fish can swim")


print("MAIN PROGRAM")
print("============")
print("Bird:")
myBird = Bird()

myBird.sleep()  # accessed from parent
myBird.eat()  # accessed from parent
myBird.fly()  # bird's own method, not inherited
# myBird.swim  # AttributeError: bird has no attribute 'swim'

print("============")
print("Fish:")
myFish = Fish()

myFish.sleep()  # accessed from parent
myFish.eat()  # accessed from parent
myFish.swim()  # fish's own method, not inherited


# myFish.fly()  # AttributeError: fish has no attribute 'fly'


# overriding class methods
class Eagle(Bird):
    def eat(self):
        print("This eagle eats meat")


class Parrot(Bird):
    def eat(self):
        print("This parrot eats plants")


# now, make eagle and parrot objects and see what they're eating
print("============")
print("Wagtail:")
wagtail = Bird()
wagtail.sleep()
wagtail.fly()

wagtail.eat()

print("============")
print("Parrot:")
parrot = Parrot()
parrot.sleep()
parrot.fly()

parrot.eat()

print("============")
print("Eagle:")
whiteEagle = Eagle()
whiteEagle.sleep()
whiteEagle.fly()

whiteEagle.eat()