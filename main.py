import sqlite3


sqliteConnection = sqlite3.connect('my.db')
cursor = sqliteConnection.cursor()
print('DB Init')
table = """ CREATE TABLE GEEK (
            Email VARCHAR(255) NOT NULL,
            First_Name CHAR(25) NOT NULL,
            Last_Name CHAR(25),
            Score INT
        ); """
 
cursor.execute(table)
 
print("Table is Ready")
 
sqliteConnection.close()
