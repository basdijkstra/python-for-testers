import sqlite3

def test_query_database():
    conn = sqlite3.connect("db_tests/examples/customers.db")
    cursor = conn.cursor()
    cursor.execute("SELECT last_name FROM customer WHERE id = 3")
    name = cursor.fetchone()
    conn.close()
    assert name[0] == "Jones"

