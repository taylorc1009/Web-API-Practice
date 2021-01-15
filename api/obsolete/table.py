### Udemy Section 5 (and 6, only before class 101)
# this was used to create the database and the tables
# the database must be in the same directory where app.py is ran

# import sqlite3

# connection = sqlite3.connect('data.db') # creates a new file-based database - you must delete this every time you want to re-run the app or you'll get database errors such as "primary key exists"

# cursor = connection.cursor()

# create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)" # 'INTEGER' key word creates an auto incrementing column: we want our IDs to auto increment for each new row
# cursor.execute(create_table)

# create_table = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, price real)" # 'INTEGER' key word creates an auto incrementing column: we want our IDs to auto increment for each new row
# cursor.execute(create_table)

# connection.commit()

# connection.close()
