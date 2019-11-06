class Account:
    def __init__(self, balance, type):
        self.balance = balance
        self.type = type

# Exercise 8.1
# Improve the withdraw() method so that it only performs a withdraw
# when the balance is >= 0 after the withdrawal
# Otherwise, raise a ValueError with a message
# "Cannot withdraw <amount> from account with balance of <balance>"
# Think of a way to implement this without actually performing the withdrawal!

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def add_interest(self, interest_rate):
        if self.type == "savings":
            self.balance *= (1 + interest_rate)