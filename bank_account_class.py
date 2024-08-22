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
