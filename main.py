import sqlite3
 
connection = sqlite3.connect('my.db')
 
cursor = connection.cursor()
 
table = """INSERT INTO Studentinfo (First_Name,Last_Name, Email, Score, Age) 
VALUES ('Lewis','Hamilton', 'lewishamilton@gmail.com', 65, 30);
"""
 
cursor.execute(table)
 
print("Table is Ready")


connection.commit()
connection.close()