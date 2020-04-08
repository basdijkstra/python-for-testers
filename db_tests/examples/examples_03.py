import sqlite3

users = [(2, "Adam", "Johnson"), (3, "Rebecca", "Jones"), (4, "Meryl", "Black")]

orders = [
    (1, "A sample order", 2),
    (2, "Another sample order", 3),
    (3, "Yet another sample order", 3),
]


def create_database():
    conn = sqlite3.connect("db_tests/examples/customers_orders.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE customer (id INTEGER NOT NULL, first_name TEXT NOT NULL, last_name TEXT NOT NULL)"
    )
    cursor.execute("INSERT INTO customer VALUES (1, 'John', 'Smith')")
    cursor.executemany("INSERT INTO customer VALUES (?,?,?)", users)
    cursor.execute(
        "CREATE TABLE cust_order (orderid INTEGER PRIMARY KEY NOT NULL, description TEXT NOT NULL, customer INTEGER NOT NULL, FOREIGN KEY(customer) REFERENCES customer(id))"
    )
    cursor.executemany("INSERT INTO cust_order VALUES (?,?,?)", orders)
    conn.commit()
    conn.close()


def query_database():
    conn = sqlite3.connect("db_tests/examples/customers_orders.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT COUNT(cust_order.description) FROM cust_order INNER JOIN customer ON cust_order.customer = customer.id WHERE customer.first_name = 'Rebecca'"
    )
    print(cursor.fetchone())
    conn.close()


create_database()
query_database()
