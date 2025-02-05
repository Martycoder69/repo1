import sqlite3

# Connecting to sqlite
# connection object
connection_obj = sqlite3.connect('sql.db')

# cursor object
cursor_obj = connection_obj.cursor()

# Drop the GEEK table if already exists.
cursor_obj.execute("DROP TABLE IF EXISTS SMS")

# Creating table
table = """ CREATE TABLE SMS (
			Name CHAR(25) NOT NULL,
            Email VARCHAR(255) NOT NULL,
			Age INT NOT NULL,
			Score INT NOT NULL
		); """

cursor_obj.execute(table)

print("Table is Ready")

# Close the connection
connection_obj.close()
