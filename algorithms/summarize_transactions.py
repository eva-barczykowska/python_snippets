"""
Problem Statement:
Write a function that takes a list of dictionaries, where each dictionary represents a financial transaction. Each dictionary has a 'type' (either 'deposit' or 'withdrawal') and an 'amount'. The function should return a dictionary summarizing the total amount for deposits and withdrawals.


C: What's the job?

Summarize the keys, they are either withdrawal or deposit. Create a new dictionary with the sums of the values.

E:  What's this test checking?

Can you separate withdrawal from deposit?
Can you add to the amounts of each, and not overwrite.

S: Who owns what?

No ownership, just functions

A:  What's my first step?

# Create a new holding value to update each value
# Return a dictionary with two keys(deposit, withdrawal), and two values (summed values of each)

# C: Write it.

# """
def summarize_transactions(list_of_dicts):
    new_dict = {}
    deposit_value = 0
    withdrawal_value = 0

    for item in list_of_dicts:

        if item['type'] == 'deposit':
            deposit_value += item['amount']
        elif item['type'] == 'withdrawal':
            withdrawal_value += item['amount']
        else:
            raise KeyError("You got the wrong keys")

    new_dict["deposit"] = deposit_value
    new_dict["withdrawal"] = withdrawal_value

    return new_dict


# The keys 'deposit' and 'withdrawal' should be present even if there are no
# transactions of that type.
transactions1 = [
    {'type': 'deposit', 'amount': 100},
    {'type': 'withdrawal', 'amount': 50},
    {'type': 'deposit', 'amount': 75},
]
# Expected output: {'deposit': 175, 'withdrawal': 50}
print(summarize_transactions(transactions1))

transactions2 = [
    {'type': 'deposit', 'amount': 200},
    {'type': 'deposit', 'amount': 150},
]
# Expected output: {'deposit': 350, 'withdrawal': 0}
print(summarize_transactions(transactions2))

# Expected output: {'deposit': 0, 'withdrawal': 0}
print(summarize_transactions([]))