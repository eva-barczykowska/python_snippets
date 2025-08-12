class Person:
    def __init__(self, name):
        self.name = name
    def greet(self):
        return f"Hello, my name is {self.name}!"

p1 = Person("John Doe")
p2 = Person("Jane Smith")
print(p1.greet())
print(p2.greet())

class Employee(Person):
    def __init__(self, name, id_number):
        super().__init__(name)
        self.id_number = id_number

emp1 = Employee("John Doe", "12345")
emp2 = Employee("Jane Smith", "67890")
print(emp1.greet())
print(emp2.greet())