import sqlite3

# Exercise 3.1
# Create an object that represents a list of car makes
# that will be inserted in a database:
# (id, make, founded_in)
# (1, Fiat, 1899)
# (2, Maserati, 1914)
# (3, Ferrari, 1939)
# (4, Lamborghini, 1963)


# Exercise 3.2
# Create an object that represents a list of car models
# that will be inserted in a database:
# (id, make_id, model_name, first_year)
# (1, 1, Punto, 1993)
# (2, 1, Tipo, 1988)
# (3, 1, Ritmo, 1978)
# (4, 2, Quattroporte, 1963)
# (5, 3, Testarossa, 1984)


# Exercise 3.3
# Create a function create_database() that does the following:
# 1. It creates a database cars.db with two tables:
# TABLE 1: make
# FIELDS: id - INTEGER PRIMARY KEY NOT NULL
#         name - TEXT NOT NULL
#         founded_in - INTEGER NOT NULL
# TABLE 2: model
# FIELDS: id - INTEGER PRIMARY KEY NOT NULL
#         make_id - INTEGER NOT NULL
#         model_name - TEXT NOT NULL
#         first_year - INTEGER NOT NULL
# The make_id field is a FOREIGN KEY referencing the id column in the 'model' table
# 2. It inserts all values from 3.1 in the 'make' table
# 3. It inserts all values from 3.2 in the 'model' table
# 4. It commits all changes
# 5. It closes the database connection
# TIP: you can simply delete the created cars.db file to start over


# Exercise 3.4
# To check your work, create a function query_database(make_name) that performs the following
# query on your database:
# SELECT model.model_name FROM model INNER JOIN make ON model.make_id = make.id WHERE make.name = <make_name>
# Write the contents of all results to the console (Google!)


# Exercise 3.5
# Call the method from 3.3 first, then the method from 3.4 (using a make of your choice)
# and check the results in the console
