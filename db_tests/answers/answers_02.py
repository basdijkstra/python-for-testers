import sqlite3
import pytest

# Exercise 2.1
# Rewrite the tests so they use a pytest fixture for database setup
# and teardown. Remove excess code from your tests.
# Rerun the tests and see that they still pass

@pytest.fixture
def database_connection():
    db_conn = sqlite3.connect("db_tests/answers/crm.db")
    yield db_conn
    db_conn.close()


def test_query_database_check_number_of_customers_in_database(database_connection):
    cursor = database_connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM customer")
    count = cursor.fetchone()
    assert count[0] == 4


def test_query_database_check_number_of_customers_with_address_in_database(database_connection):
    cursor = database_connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM customer INNER JOIN address ON customer.id = address.customer_id")
    count = cursor.fetchone()
    assert count[0] == 3


def test_query_database_check_number_of_customers_living_in_detroit(database_connection):
    cursor = database_connection.cursor()
    cursor.execute("SELECT COUNT(customer.id) FROM customer INNER JOIN address ON customer.id = address.customer_id WHERE address.city = ?", ['Detroit'])
    count = cursor.fetchone()
    assert count[0] == 1


def test_query_database_check_name_of_customer_living_on_blue_street(database_connection):
    cursor = database_connection.cursor()
    cursor.execute("SELECT first_name, last_name FROM customer INNER JOIN address ON customer.id = address.customer_id WHERE address.street = ?", ['Blue Street'])
    customer = cursor.fetchone()
    assert customer[0] == 'Meryl'
    assert customer[1] == 'Black'
