import sqlite3

# Exercise 1.1
# Write a test that does the following:
# 1. Open a connection to the 'crm.db' database
# 2. Execute a query that returns the number of records in the 'customer' table
# 3. Assert that the result of that query is equal to 4
# Don't forget to close the connection at the right moment in your test
def test_query_database_check_number_of_customers_in_database():
    conn = sqlite3.connect("db_tests/answers/crm.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM customer")
    count = cursor.fetchone()
    conn.close()
    assert count[0] == 4


# Exercise 1.2
# Write a test that does the following:
# 1. Open a connection to the 'crm.db' database
# 2. Execute a query that returns the number of customers in the 'customer'
#    table that have an address associated with them in the 'address' table
#    join customer.id on address.customer_id
# 3. Assert that the result of that query is equal to 3
def test_query_database_check_number_of_customers_with_address_in_database():
    conn = sqlite3.connect("db_tests/answers/crm.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT COUNT(*) FROM customer INNER JOIN address ON customer.id = address.customer_id"
    )
    count = cursor.fetchone()
    conn.close()
    assert count[0] == 3


# Exercise 1.3
# Write a test that does the following:
# 1. Open a connection to the 'crm.db' database
# 2. Execute a query that returns the number of customers living in Detroit
#    ('city' in the 'address' table)
#    Make sure to use safe parameters
# 3. Assert that the number is equal to 1
def test_query_database_check_number_of_customers_living_in_detroit():
    conn = sqlite3.connect("crm.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT COUNT(customer.id) FROM customer INNER JOIN address ON customer.id = address.customer_id WHERE address.city = ?",
        ["Detroit"],
    )
    count = cursor.fetchone()
    conn.close()
    assert count[0] == 1


# Exercise 1.4
# Write a test that does the following:
# 1. Open a connection to the 'crm.db' database
# 2. Execute a query that returns the first_name and last_name from the customer
#    in the 'customer' table who lives on 'Blue Street' ('street' column in the 'address' table
#    Make sure to use safe parameters
# 3. Assert that the first_name is equal to 'Meryl'
#    and that the last name is equal to 'Black'
def test_query_database_check_name_of_customer_living_on_blue_street():
    conn = sqlite3.connect("db_tests/answers/crm.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT first_name, last_name FROM customer INNER JOIN address ON customer.id = address.customer_id WHERE address.street = ?",
        ["Blue Street"],
    )
    customer = cursor.fetchone()
    conn.close()
    assert customer[0] == "Meryl"
    assert customer[1] == "Black"
