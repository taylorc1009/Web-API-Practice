import sqlite3

connection = sqlite3.connect('data.db') # creates a new file-based database - you must delete this every time you want to re-run the app or you'll get database errors such as "primary key exists"

cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)" # 'INTEGER' key word creates an auto incrementing column: we want our IDs to auto increment for each new row
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items (name text, price real)" # 'INTEGER' key word creates an auto incrementing column: we want our IDs to auto increment for each new row
cursor.execute(create_table)

cursor.execute("INSERT INTO items VALUES ('test', 10.99)")

# user = (1, 'jose', 'asdf')
# insert_query = "INSERT INTO users VALUES (?, ?, ?)"
# cursor.execute(insert_query, user)

# users = [
	# (2, 'rolf', 'fdsa'),
	# # (3, 'anne', 'xyz')
# ]
# cursor.executemany(insert_query, users)

# select_query = "SELECT * FROM users"
# for row in cursor.execute(select_query):
	# print(row)

connection.commit()

connection.close()
