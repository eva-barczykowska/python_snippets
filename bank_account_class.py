class BankAccount:
    def __init__(self, name, account_balance=0):
        self.name = name
        self.account_balance = account_balance
        print(f"Account created for {self.name}. Initial balance: {self.account_balance}")

    def deposit(self, amount):
        self.account_balance += amount
        print(f"{amount} deposited. New balance: {self.account_balance}")

    def withdraw(self, amount):
        self.account_balance -= amount
        print(f"Withdrew {amount}. New balance: {self.account_balance}")


my_account = BankAccount("Ewa", 100000)  # initialized a new variable, `my_account`, of type BankAccount
# initializing above causes the constructor (__init__) to be called
# and the print statement inside the constructor to be executed
# the print statement: "Account created for Ewa. Initial balance: 100000"

print(my_account)  # data, have to print it to get the object representation
print(my_account.name)  # data, have to print it to get the value
print(my_account.account_balance)  # data, have to print it to get the value

my_account.deposit(100000)  # method, don't need to use print
my_account.withdraw(50000)  # method, don't need to use print'

"""
Explanation
The selected code within the BankAccount class is the __init__ method, also known as the constructor.
This method is automatically called when an instance of the class is created.

In the __init__ method, the self parameter is a reference to the current instance of the class.
It is used to access variables and methods that belong to the class. In this case, self.name and self.account_balance are instance variables that store the name and account balance of the bank account, respectively.

The __init__ method also takes two parameters: name and account_balance. The name parameter is a string representing
the name of the bank account holder, and the account_balance parameter is an integer representing the initial balance
of the account. The account_balance parameter has a default value of 0, which means if no initial balance is provided,
the account will be created with a balance of 0.

Inside the __init__ method, the provided name and account_balance values are assigned to the corresponding
instance variables. Additionally, a print statement is executed to display a message indicating that
the account has been created and the initial balance.

When you create a new instance of the BankAccount class, such as my_account = BankAccount("Ewa", 100000),
the __init__ method is automatically called with the provided arguments. As a result, the print statement inside
the __init__ method is executed, displaying the message: "Account created for Ewa. Initial balance: 100000".

In summary, the __init__ method in the BankAccount class is responsible for initializing the instance variables
and performing any necessary actions when a new instance of the class is created.
It is a crucial part of object-oriented programming in Python.
"""
