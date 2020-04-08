import sqlite3

# Exercise 1.1
# Write a test that does the following:
# 1. Open a connection to the 'crm.db' database
# 2. Execute a query that returns the number of records in the 'customer' table
# 3. Assert that the result of that query is equal to 4
# Don't forget to close the connection at the right moment in your test


# Exercise 1.2
# Write a test that does the following:
# 1. Open a connection to the 'crm.db' database
# 2. Execute a query that returns the number of customers in the 'customer'
#    table that have an address associated with them in the 'address' table
#    join customer.id on address.customer_id
# 3. Assert that the result of that query is equal to 3


# Exercise 1.3
# Write a test that does the following:
# 1. Open a connection to the 'crm.db' database
# 2. Execute a query that returns the number of customers living in Detroit
#    ('city' in the 'address' table)
#    Make sure to use safe parameters
# 3. Assert that the number is equal to 1


# Exercise 1.4
# Write a test that does the following:
# 1. Open a connection to the 'crm.db' database
# 2. Execute a query that returns the first_name and last_name from the customer
#    in the 'customer' table who lives on 'Blue Street' ('street' column in the 'address' table
#    Make sure to use safe parameters
# 3. Assert that the first_name is equal to 'Meryl'
#    and that the last name is equal to 'Black'
