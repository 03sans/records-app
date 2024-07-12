#importing libraries
import os
import sqlite3
import csv

#function to display a welcome message 
def welcome():
    print("-"*125)
    print("\t\t\t\t\t\tNEPAL RECORDS INC.")
    print("\n")
    print("\t\t\t\t\t\tAddress: DILLIBAZAAR")
    print("\t\t\t\t\t\tContact us at 9800000000")
    print("-"*125)
    print("\t\t\t\t\t\tWelcome to our system!")
    print("-"*125)

#function to display a menu of operations
def menu():
    print("Please select an option!")
    print("a || Press 1 to create new record")
    print("b || Press 2 to read existing records")
    print("c || Press 3 to update records")
    print("d || Press 4 to delete any record")
    print("e || Press 5 to add a new column in the system")
    print("f || Press 6 to dump data to CSV")
    print("g || Press 7 to exit the system \n")

#function to create a table in a database where the records will be stored
def init_db():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT,
            Age INTEGER,
            Email TEXT
    )''')
    conn.commit()
    conn.close()

#function to dumb data into a csv file
def dump_to_csv():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    
    c.execute("SELECT * FROM users")
    data = c.fetchall()
    column_names = [description[0] for description in c.description]

    with open('data_dump.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(column_names)
        writer.writerows(data)

    conn.close()
    print("Data has been successfully dumped to 'data_dump.csv'.")

#function to check the validity of a name
def is_valid_name(name):
    name = name.lower()
    for i in name:
        if not ('a' <= i <= 'z'):
            return False
    return True

#function to check the validity of age
def is_valid_age(age):
    try:
        int_age = int(age)
        return int_age > 0
    except ValueError:
        return False

def get_columns():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("PRAGMA table_info(users)")
    columns = [row[1] for row in c]
    conn.close()
    return columns

#function to create new records
def create():
    columns = get_columns()
    new_record = {}
    for column in columns:
        if column == "ID":
            continue
        if column == "Name":
            while True:
                name = input(f"Please enter your {column}: ")
                if is_valid_name(name):
                    new_record[column] = name
                    break
                else:
                    print("Invalid name input! Please use only alphabetic characters.")
        elif column == "Age":
            while True:
                age = input(f"Please enter your {column}: ")
                if is_valid_age(age):
                    new_record[column] = int(age)
                    break
                else:
                    print("Invalid age input! Age can't be a negative value.")
        elif column == "Email":
            email = input(f"Please enter your {column}: ")
            new_record[column] = email
        else:
            new_record[column] = input(f"Please enter your {column}: ")

    placeholders = ", ".join("?" * len(new_record))
    column_names = ", ".join(new_record.keys())
    column_values = tuple(new_record.values())

    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute(f"INSERT INTO users ({column_names}) VALUES ({placeholders})", column_values)
    conn.commit()
    conn.close()

    print()
    print('-'*125)
    print('\t\t\t\tThe following record has been saved in the database \n')
    for key, value in new_record.items():
        print(f"{key}: {value}")
    print('-'*125)

#function to read the records
def read():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()

    while True:
        print("Choose the detail you want to view:")
        print("1. All details")
        print("2. Specific column details")
        print("3. Records by ID")
        print("4. Go back to the main menu")
        choice = input("Enter your required choice of viewing: ")

        if choice == "1":
            c.execute("SELECT * FROM users")
            columns = get_columns()
            print(" | ".join(columns))
            print("-" * (10 * len(columns)))
            for row in c:
                print(" | ".join(str(r) for r in row))
        elif choice == "2":
            columns = get_columns()
            print("Available columns: ", ", ".join(columns))
            column_choice = input("Enter the column name to view: ")
            if column_choice in columns:
                c.execute(f"SELECT {column_choice} FROM users")
                print(f"{column_choice}")
                print("-" * 30)
                for row in c:
                    print(row[0])
            else:
                print("Invalid column name!")
        elif choice == '3':
            id_input = input("Enter the ID to view details: ")
            query = "SELECT * FROM users WHERE ID = ?"
            c.execute(query, (id_input,))
            columns = get_columns()
            print(" | ".join(columns))
            print("-" * (10 * len(columns)))
            found = False
            for row in c:
                found = True
                print(" | ".join(str(r) for r in row))
            if not found:
                print(f"No details found for ID {id_input}")
        elif choice == "4":
            os.system('clear')
            print("Returning to the main menu.\n")
            menu()
            break
        else:
            print("Please enter a valid number!\n")
        print()
    
    conn.close()

#function to update records 
def update():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    print(f"{'ID':<5} {'Name':<20} {'Age':<5} {'Email':<30}")
    print("-" * 60)
    for row in c:
        print(f"{row[0]:<5} {row[1]:<20} {row[2]:<5} {row[3]:<30}")
    user_id = input("Enter the ID of the record you want to update: ")

    while True:
        print("Choose the detail you want to update:")
        print("1. All details")
        print("2. Name only")
        print("3. Age only")
        print("4. Email only")
        print("5. Go back to the main menu")
        choose = input("Enter your required choice of updating: ")

        if choose == "1":
            while True:
                name = input("Enter the new name: ")
                if is_valid_name(name):
                    break
                else:
                    print("Invalid name input! Please use only alphabetic characters.")
            
            while True:
                age = input("Enter the new age: ")
                if is_valid_age(age):
                    age = int(age)
                    break
                else:
                    print("Invalid age input! Age can't be a negative value.")
            
            email = input("Enter the new email: ")

            conn = sqlite3.connect('data.db')
            c = conn.cursor()
            c.execute("UPDATE users SET Name = ?, Age = ?, Email = ? WHERE ID = ?", (name, age, email, user_id))
            conn.commit()
            conn.close()
            
            print("\n The record has been updated successfully. \n")       
        elif choose == "2":
            while True:
                name = input("Enter the new name: ")
                if is_valid_name(name):
                    break
                else:
                    print("Invalid name input! Please use only alphabetic characters.")
            conn = sqlite3.connect('data.db')
            c = conn.cursor()
            c.execute("UPDATE users SET Name = ? WHERE ID = ?", (name, user_id))
            conn.commit()
            conn.close()
            
            print("\n The name has been updated successfully. \n")
        elif choose == "3":
            while True:
                age = input("Enter the new age: ")
                if is_valid_age(age):
                    age = int(age)
                    break
                else:
                    print("Invalid age input! Age can't be a negative value.")
            conn = sqlite3.connect('data.db')
            c = conn.cursor()
            c.execute("UPDATE users SET Age = ? WHERE ID = ?", (age, user_id))
            conn.commit()
            conn.close()
            
            print("\n The age has been updated successfully. \n")
        elif choose == "4":
            email = input("Enter the new email: ")

            conn = sqlite3.connect('data.db')
            c = conn.cursor()
            c.execute("UPDATE users SET Email = ? WHERE ID = ?", (email, user_id))
            conn.commit()
            conn.close()
            
            print("\n The email has been updated successfully. \n")
        elif choose == "5":
            os.system('clear')
            print("Returning to the main menu.\n")
            menu()
            break

        else:
            print("Please enter a valid number!\n")
        print()

#function to delete the records
def delete():
    read()
    user_id = input("Enter the ID of the record you want to delete: ")

    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("DELETE FROM users WHERE ID = ?", (user_id))
    conn.commit()
    conn.close()
    
    print("\n The record has been deleted successfully. \n")

def add_column():
    column_name = input("Enter the name of the new column: ")
    column_type = input("Enter the type of the new column (e.g., TEXT, INTEGER): ")

    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute(f"ALTER TABLE users ADD COLUMN {column_name} {column_type}")
    conn.commit()
    conn.close()
    
    print(f"\n The {column_name} column has been added successfully. \n")

#main function to run the system based on different operations
def main():
    init_db()
    welcome()
    menu()

    while True:
        value = int(input("Enter your operation number here:"))
        print()
        
        if value == 1:
            print("-"*125)
            print("\t\t\t\t Thank you for choosing to create new record! Your process begins now.")
            print("-"*125)
            print()
            create()
        elif value == 2:
            print("-"*125)
            print("\t\t\t\tThank you for choosing to read records! You can read the records below.")
            print("-"*125)
            print()
            read()
        elif value == 3:
            print("-"*125)
            print("\t\t\t\t Thank you for choosing to update the records! Your updating process begins now.")
            print("-"*125)
            print()
            update()
        elif value == 4:
            print("-"*125)
            print("\t\t\t\tThank you for choosing to delete records! Your deletion process begins now.")
            print("-"*125)
            print()
            delete()
        elif value == 5:
            print("-" * 125)
            print("\t\t\t\tThank you for choosing to add a new column! The process begins now.")
            print("-" * 125)
            print()
            add_column()
        elif value == 6:
            print("-" * 125)
            print("\t\t\t\tDumping data to CSV. The process begins now.")
            print("-" * 125)
            print()
            dump_to_csv()
        elif value == 7:
            print("-" * 125)
            print("\t\t\t\tThank you for doing business with us! We hope to see you soon.")
            print("-" * 125)
            break 
        else:
            os.system('clear')
            print('-' * 125)
            print('Please enter a valid operation number!')
            print('-' * 125)
            menu()
            print()