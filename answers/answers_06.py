# Exercise 6.1
# Create a class Account and an __init__ constructor method
# that takes (after self) two additional parameters:
# - balance (representing the account balance, e.g. 1000)
# - type (representing the type of account, e.g. "savings")

# Exercise 6.2
# Create three class methods:
# - withdraw (taking, next to self, one argument amount)
#   that withdraws the given amount from the balance
# - deposit (taking, next to self, one argument amount)
#   that deposits the given amount to the balance
# - add_interest (taking, next to self, one argument interest_rate)
#   that adds the given interest rate to the amount (where e.g. 0.05 represent 5%)

# Exercise 6.3
# Create a new instance of the Account class with an initial balance of 1000
# Then:
# 1. Withdraw 500
# 2. Deposit 750
# 3. Add 5% interest, but only if the account type is "savings"
# 4. Print the resulting balance

class Account:
    def __init__(self, balance, type):
        self.balance = balance
        self.type = type

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def add_interest(self, interest_rate):
        if self.type == "savings":
            self.balance *= (1 + interest_rate)

my_account = Account(1000, "savings")
my_account.withdraw(500)
my_account.deposit(750)
my_account.add_interest(0.05)
print(my_account.balance)
