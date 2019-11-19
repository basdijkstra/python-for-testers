import sqlite3

def test_query_database_check_number_of_makes_in_database():
    conn = sqlite3.connect("db_tests/examples/cars.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM make")
    count = cursor.fetchone()
    print(count)
    conn.close()
    assert count[0] == 4

def test_query_database_check_number_of_models_for_given_make():
    conn = sqlite3.connect("db_tests/examples/cars.db")
    cursor = conn.cursor()
    cursor.execute("SELECT model.model_name FROM model INNER JOIN "
                   "make ON model.make_id = make.id WHERE make.name = ?", ['Maserati'])
    model_name = cursor.fetchone()
    print(model_name)
    conn.close()
    assert model_name[0] == 'Quattroporte'