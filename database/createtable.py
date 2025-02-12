import sqlite3

# Connecting to sqlite
# connection object
connection_obj = sqlite3.connect('database/lbm.db')

# cursor object
cursor_obj = connection_obj.cursor()

# Drop the GEEK table if already exists.
cursor_obj.execute("DROP TABLE IF EXISTS table1")

# Creating table
table = """ CREATE TABLE table1 (
			id INT NOT NULL,
			title CHAR(25) NOT NULL,
            author VARCHAR(255) NOT NULL
		); """

cursor_obj.execute(table)

print("Table is Ready")

# Close the connection
connection_obj.close()
