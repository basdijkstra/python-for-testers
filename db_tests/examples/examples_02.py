import sqlite3
import pytest


@pytest.fixture
def database_connection():
    db_conn = sqlite3.connect("db_tests/examples/cars.db")
    yield db_conn
    db_conn.close()


def test_query_database_check_number_of_makes_in_database(database_connection):
    cursor = database_connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM make")
    count = cursor.fetchone()
    assert count[0] == 4


def test_query_database_check_number_of_models_for_given_make(database_connection):
    cursor = database_connection.cursor()
    cursor.execute("SELECT model.model_name FROM model INNER JOIN "
                   "make ON model.make_id = make.id WHERE make.name = ?", ['Maserati'])
    model_name = cursor.fetchone()
    assert model_name[0] == 'Quattroporte'
