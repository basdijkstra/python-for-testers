import pytest
import requests
import csv

# Exercise 2.1
# Create a test data object test_data_users
# with three lines / test cases:
# id -             name -           city
#  1 -    Leanne Graham -    Gwenborough
#  4 - Patricia Lebsack -    South Elvis
#  9 -  Glenna Reichert - Bartholomebury


# Exercise 2.2
# Write a parameterized test that retrieves user data using
# a GET call to https://jsonplaceholder.typicode.com/users/<user_id>
# and checks that the 'name' and the 'city' elements correspond to those
# that are specified in the test data object


# Exercise 2.3
# Create the same test data as above, but now in a .csv file, for example:
# 1,Leanne Graham,Gwenborough
# 4,Patricia Lebsack,South Elvis
# 9,Glenna Reichert,Bartholomebury
# Create a method write_csv() that creates this .csv file using the test_data_users
# object from Exercise 2.1


# Exercise 2.4
# Create a method read_csv() that reads the file from 2.3 line by line
# and creates and returns a test data object from the data in the .csv file
# On the first line of the method, call the write_csv() method from Exercise 2.3
# to ensure that it exists


# Exercise 2.5
# Change the data driven test from Exercise 2.2 so that it uses the test data
# from the .csv file instead of the test data that was hard coded in this file

