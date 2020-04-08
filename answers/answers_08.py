class Account:
    def __init__(self, balance, type):
        self.balance = balance
        self.type = type

    # Exercise 8.1
    # Improve the deposit() method so that it does not take negative arguments
    # Raise a ValueError with a message
    # "Cannot deposit a negative amount to this account"

    # Exercise 8.2
    # Improve the withdraw() method so that it only performs a withdraw
    # when the balance is >= 0 after the withdrawal
    # Otherwise, raise a ValueError with a message
    # "Cannot withdraw <amount> from account with balance of <balance>"
    # Think of a way to implement this without actually performing the withdrawal!

    # Exercise 8.3
    # What other values can you think of that should not be accepted?
    # Implement ValueErrors for those as well!

    def withdraw(self, amount):
        if (self.balance - amount) < 0:
            raise ValueError(
                "Cannot withdraw %d from account with balance of %d"
                % (amount, self.balance)
            )
        self.balance -= amount

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Cannot deposit a negative amount to this account")
        self.balance += amount

    def add_interest(self, interest_rate):
        if self.type == "savings":
            self.balance *= 1 + interest_rate


# Exercise 8.4
# Create a new instance of this account with an initial
# balance of 1000 and type "savings", and check that
# - A ValueError is raised when you try to withdraw 1250
# - A ValueError is raised when you try to deposit -100
# - The other ValueErrors that you implemented are also
#   raised when applicable

my_account = Account(1000, "savings")
# my_account.withdraw(1250)
# my_account.deposit(-100)

# Exercise 8.5
# Repeating exercise 8.4, now use try / except to print
# appropriate updates to the console whenever a ValueError
# has been raised.

my_other_account = Account(1000, "savings")
try:
    my_other_account.withdraw(1250)
except ValueError:
    print("That doesn't work...")
try:
    my_other_account.deposit(-100)
except:
    print("That doesn't work either...")
