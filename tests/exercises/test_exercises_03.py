from objects import robust_account
import pytest

# Exercise 3.1
# Create a test_data_withdraw object for the withdraw() method
# containing the following test data records:
# balance - amount - new_balance
#    1000 -    100 -         900
#    1000 -    999 -           1
#    1000 -   1000 -           0


# Exercise 3.2
# Create a parametrized test that does the following for each of the
# iterations specified in the test_data_withdraw object:
# 1. Create a new account with the specified balance
#    (the type isn't significant here and can be hard coded to 'savings')
# 2. Withdraw the given amount
# 3. Check that the actual new balance is equal to the one specified in the test_data object


# Exercise 3.3
# Add a new row to the test_data object with the values
# 1000, 1001 and 1000, respectively. What happens when you run the test again?
# Try to adapt the test so this test case can be run as well. What do you think?


# Exercise 3.4
# Create a new test_data_interest object
# containing the following test data records:
# balance -     type - interest - new_balance
#    1000 -  savings -     0.01 -        1010
#    1000 - checking -     0.02 -        1000
#    1000 -  savings -        0 -        1000


# Exercise 3.5
# Create a parametrized test that does the following for each of the
# iterations specified in the test_data_interest object:
# 1. Create a new account with the specified balance and type
# 2. Call the add_interest method with the given interest percentage
# 3. Check that the actual new balance is equal to the one specified in the test_data_interest object

