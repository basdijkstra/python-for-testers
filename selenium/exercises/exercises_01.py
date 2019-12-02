from selenium import webdriver
import pytest


# Exercise 1.1
# Write a test that performs the following actions:
# 1. Open a new Chrome instance
# 2. Maximize the window
# 3. Navigate to http://parabank.parasoft.com
# 4. Enter 'john' in the username text field
# 5. Enter 'demo' in the password text field
# 6. Click the 'Log In' button
# 7. Assert that the browser tab title text equals 'ParaBank | Accounts Overview'
# 8. Close the browser


# Exercise 1.2
# Write a pytest fixture method that performs the following actions:
# 1. Open a new Chrome instance
# 2. Maximize the window
# 3. Yield the browser object
# 4. Close the browser


# Exercise 1.3
# Duplicate the test from 1.1 (or rewrite it) so that the
# pytest fixture is used to open and close the browser
