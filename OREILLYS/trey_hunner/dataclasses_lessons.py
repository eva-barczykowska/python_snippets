from dataclasses import dataclass

@dataclass
class Person:
    name: str  # type hinting/type annotation
    age: int  # type hinting/type annotation

# Creating an instance
p = Person(name="Alice", age=30)
print(p)  # Output: Person(name='Alice', age=30)
print(p.name)  # Output: Alice
print(p.age)  # Output: 30
# dataclasses allows us to write classes more quickly, without a lot of boilerplate code

# this, otherwise, would look like this:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

    def __eq__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.name == other.name() and (self.age == other.age)
