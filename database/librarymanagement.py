import sqlite3

connection = sqlite3.connect('database/lbm.db')

cursor = connection.cursor()
while True:
      print("1. Add new book")
      print("2. Delete book")
      print("3. Update book")
      print("4. Display all books")
      print("5. Search book")
      print("6. Exit")
      choice = input("Enter your choice: ")
      if choice == "1":
            id = input("Enter book id: ")
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            table = """INSERT INTO table1 (title, author, id) 
                              VALUES (?, ?, ?);"""
            cursor.execute(table, (title, author, id))
            connection.commit()
            print("book added successfully.")
      
      elif choice == "2":
            id = input("Enter book id: ")
            table = """DELETE FROM table1 WHERE id = ?;"""
            cursor.execute(table, (id,))
            connection.commit()
            print("book deleted successfully.")

      elif choice == "3":
            id = input("Enter book id: ")
            title = input("Enter new book title: ")
            author = input("Enter new book author: ")
            table = """UPDATE table1 SET title = ?, author = ? WHERE id = ?;"""
            cursor.execute(table, (title, author, id))
            connection.commit()
            print("book updated successfully.")

      elif choice =="4":
            cursor.execute("SELECT * FROM table1")
            rows = cursor.fetchall()
            print('{:<10}{:<15}{:<15}'.format('id','name','age'))
            for row in rows:
                  print('{:<10}{:<15}{:<15}'.format('id','name','age'))

      elif choice =="5":
            id = input("Enter book id: ")
            table = """SELECT * FROM table1 WHERE id = ?;"""
            cursor.execute(table, (id,))
            rows = cursor.fetchall()
            for row in rows:
                  print(row)

      elif choice == "6":
            connection.close()
            print("Connection closed.")
      else:
            print("Invalid choice. Please choose a valid option.")