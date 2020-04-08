import sqlite3

# Exercise 2.1
# Rewrite these tests so they use a pytest fixture for database setup
# and teardown. Remove excess code from your tests.
# Rerun the tests and see that they still pass


def test_query_database_check_number_of_customers_in_database():
    conn = sqlite3.connect("db_tests/answers/crm.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM customer")
    count = cursor.fetchone()
    conn.close()
    assert count[0] == 4


def test_query_database_check_number_of_customers_with_address_in_database():
    conn = sqlite3.connect("db_tests/answers/crm.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT COUNT(*) FROM customer INNER JOIN address ON customer.id = address.customer_id"
    )
    count = cursor.fetchone()
    conn.close()
    assert count[0] == 3


def test_query_database_check_number_of_customers_living_in_detroit():
    conn = sqlite3.connect("db_tests/answers/crm.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT COUNT(customer.id) FROM customer INNER JOIN address ON customer.id = address.customer_id WHERE address.city = ?",
        ["Detroit"],
    )
    count = cursor.fetchone()
    conn.close()
    assert count[0] == 1


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
