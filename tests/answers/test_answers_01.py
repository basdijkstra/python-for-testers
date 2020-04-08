# Exercise 1.1
# Import the account module from the objects package

from objects import account

# Exercise 3.2
# Write a test_deposit() method that does the following:
# 1. Create a new Account my_account with an initial balance of 1000 and account type "savings"
# 2. Deposit 200 to my_account using the deposit() method
# 3. Assert that my_account.balance equals 1200


def test_deposit():
    my_account = account.Account(1000, "savings")
    my_account.deposit(200)
    assert my_account.balance == 1200


# Exercise 3.3
# Write a test_withdraw() method that does the following:
# 1. Create a new Account my_account with an initial balance of 1000 and account type "savings"
# 2. Withdraw 250 from my_account using the withdraw() method
# 3. Assert that my_account.balance equals 750


def test_withdraw():
    my_account = account.Account(1000, "savings")
    my_account.withdraw(250)
    assert my_account.balance == 750


# Exercise 3.4
# Write a test_add_interest_savings() method that does the following:
# 1. Create a new Account my_account with an initial balance of 1000 and account type "savings"
# 2. Add 5% interest to my_account using the add_interest() method
# 3. Assert that my_account.balance equals 1050


def test_add_interest_savings():
    my_account = account.Account(1000, "savings")
    my_account.add_interest(0.05)
    assert my_account.balance == 1050


# Exercise 3.5
# What tests would you need to add to increase test coverage for the accounts module?
# Write those tests and run them
