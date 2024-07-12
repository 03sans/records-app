import os
import sqlite3
from main import main
import getpass  

def init_user_db():
    conn = sqlite3.connect('usersdata.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS info(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Username TEXT UNIQUE,
            Password TEXT,
            Email TEXT
    )''')
    conn.commit()
    conn.close()

def username_exists(username):
    conn = sqlite3.connect('usersdata.db')
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM info WHERE Username = ?", (username,))
    exists = c.fetchone()[0] > 0
    conn.close()
    return exists

def verify_credentials(username, password):
    conn = sqlite3.connect('usersdata.db')
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM info WHERE Username = ? AND Password = ?", (username, password))
    valid = c.fetchone()[0] > 0
    conn.close()
    return valid

def sign_up():
    print('Thank you for choosing to sign! \n')
    while True:
        username = input("Enter a username: ")
        if username_exists(username):
            print("Username already exists. Please choose a different username.")
        else:
            break
    
    password = getpass.getpass("Enter a password: ")
    email = input("Enter your email: ")
    
    conn = sqlite3.connect('usersdata.db')
    c = conn.cursor()
    c.execute("INSERT INTO info (Username, Password, Email) VALUES (?, ?, ?)", (username, password, email))
    conn.commit()
    conn.close()
    
    print("Sign-up successful!\n")

def sign_in():
    print('Welcome back! You can sign in below: \n')
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    
    if verify_credentials(username, password):
        print("Sign-in successful! Welcome, {}.\n".format(username))
        return True
    else:
        print("Invalid username or password. Please try again.\n")
        return False

def menuu():
    init_user_db()
    print('-'*125)
    print('\t\t\t\t\tWelcome to Nepal Records Inc')
    print('-'*125)
    while True:
        print("Please select an option:")
        print("1. Sign Up")
        print("2. Sign In")
        print("3. Exit \n")
        
        choice = input("Enter your choice: ")
        if choice == '1':
            sign_up()
            sign_in_success = sign_in()
            if sign_in_success:
                main()  
        elif choice == '2':
            sign_in_success = sign_in()
            if sign_in_success:
                main()  
        elif choice == '3':
            print("Hope to see you soon. Goodbye! \n")
            break
        else:
            print("Invalid choice. Please try again.\n")

menuu()