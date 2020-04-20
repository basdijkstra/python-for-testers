from objects import robust_account
import pytest

# Exercise 2.1
# Create a test method test_withdraw_raises_error()
# that performs the following steps:
# 1. Create a new account of type "savings" with balance 1000
# 2. Try to withdraw 1250 from the account
# 3. Check that a ValueError is raised


# Exercise 2.2
# Extend the previous test so that it also checks the message
# raised by the error (this should be equal to
# "Cannot withdraw 1250 from account with balance of 1000"
# and that the balance is intact (i.e, is still equal to 1000)

