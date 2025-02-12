import sqlite3
 
connection = sqlite3.connect('sql.db')
 
cursor = connection.cursor()

while True:
    print("1. Add new user")
    print("2. Delete user")
    print("3. Display user")
    print("4. Update user")
    print("5. Exit")
    
    choice = int(input("Enter the choice: "))
    
    if choice == 1:
        name = input("Enter the name: ")
        email = input("Enter the email: ")
        age = int(input("Enter the age: "))
        score = int(input("Enter the score: "))

        table = """INSERT INTO SMS (Name, Email, Age, Score) 
                   VALUES (?, ?, ?, ?);"""
        cursor.execute(table, (name, email, age, score))
        connection.commit()
        print("User added successfully.")

    elif choice == 2:
        name = input("Enter the name of the user to delete: ")
        cursor.execute("DELETE FROM SMS WHERE Name = ?", (name,))
        connection.commit()
        print("User deleted successfully.")

    elif choice == 3:
        cursor.execute("SELECT * FROM SMS")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    elif choice == 4:
        name = input("Enter the name of the user to update: ")
        score = int(input("Enter the new score: "))
        cursor.execute("UPDATE SMS SET Score = ? WHERE Name = ?", (score, name))
        connection.commit()
        print("User updated successfully.")

    elif choice == 5:
        connection.close()
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
