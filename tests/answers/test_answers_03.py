from objects import robust_account
import pytest

# Exercise 3.1
# Create a test_data_withdraw object for the withdraw() method
# containing the following test data records:
# balance - amount - new_balance
#    1000 -    100 -         900
#    1000 -    999 -           1
#    1000 -   1000 -           0
test_data_withdraw = [
    (1000, 100, 900),
    (1000, 999, 1),
    (1000, 1000, 0)
]


# Exercise 3.2
# Create a parametrized test that does the following for each of the
# iterations specified in the test_data_withdraw object:
# 1. Create a new account with the specified balance
#    (the type isn't significant here and can be hard coded to 'savings')
# 2. Withdraw the given amount
# 3. Check that the actual new balance is equal to the one specified in the test_data object
@pytest.mark.parametrize("initial_balance, amount, new_balance", test_data_withdraw)
def test_withdraw(initial_balance, amount, new_balance):
    my_account = robust_account.Account(initial_balance, "savings")
    my_account.withdraw(amount)
    assert my_account.balance == new_balance


# Exercise 3.3
# Add a new row to the test_data object with the values
# 1000, 1001 and 1000, respectively. What happens when you run the test again?
# Try to adapt the test so this test case can be run as well. What do you think?
test_data_withdraw_extended = [
    (1000, 100, 900),
    (1000, 999, 1),
    (1000, 1000, 0),
    (1000, 1001, 1000)
]

# What I think? That it's a bad idea to try and get this to work :)
# It's a different path through the code and therefore deserves a test of its own
# This also keeps your tests nice and simple

# Exercise 3.4
# Create a new test_data_interest object
# containing the following test data records:
# balance -     type - interest - new_balance
#    1000 -  savings -     0.01 -        1010
#    1000 - checking -     0.02 -        1000
#    1000 -  savings -        0 -        1000
test_data_interest = [
    (1000, "savings", 0.01, 1010),
    (1000, "checking", 0.02, 1000),
    (1000, "savings", 0, 1000)
]


# Exercise 3.5
# Create a parametrized test that does the following for each of the
# iterations specified in the test_data_interest object:
# 1. Create a new account with the specified balance and type
# 2. Call the add_interest method with the given interest percentage
# 3. Check that the actual new balance is equal to the one specified in the test_data_interest object
@pytest.mark.parametrize("initial_balance, account_type, interest, new_balance", test_data_interest)
def test_interest(initial_balance, account_type, interest, new_balance):
    my_account = robust_account.Account(initial_balance, account_type)
    my_account.add_interest(interest)
    assert my_account.balance == new_balance
