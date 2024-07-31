#author - Brady Gagerman
#usage - python3 database.py
#usage 2 - (remove database) python3 database.py remove
import os
import sys
import sqlite3
from datetime import datetime, timedelta

# Create the database
def create(db_filename):
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()

    # Create Users table
    c.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    ''')

    # Create Friends table
    c.execute('''
    CREATE TABLE IF NOT EXISTS Friends (
        friend_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        friend_user_id INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES Users(user_id),
        FOREIGN KEY (friend_user_id) REFERENCES Users(user_id)
    );
    ''')

    # Create Reminders table
    c.execute('''
    CREATE TABLE IF NOT EXISTS Reminders (
        reminder_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        friend_id INTEGER NOT NULL,
        reminder_date DATE NOT NULL,
        message TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES Users(user_id),
        FOREIGN KEY (friend_id) REFERENCES Friends(friend_id)
    );
    ''')

    # Create Challenges table
    c.execute('''
    CREATE TABLE IF NOT EXISTS Challenges (
        challenge_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        joint_flag BOOLEAN NOT NULL,
        user_id_a INTEGER,
        user_id_b INTEGER,
        start_date DATE NOT NULL,
        end_date DATE NOT NULL,
        FOREIGN KEY (user_id_a) REFERENCES Users(user_id),
        FOREIGN KEY (user_id_b) REFERENCES Users(user_id)
    );
    ''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()

    print("Database and tables created successfully!")

def fill(db_filename):
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()

    # Users for the website
    users = [
        (1, 'brady_gagerman', 'brga1958@colorado.edu', 'password1', datetime.now()),
        (2, 'liam_keyek', 'liam.keyek@colorado.edu', 'password2', datetime.now()),
        (3, 'brad_richardson', 'brad.richardson@colorado.edu', 'password3', datetime.now()),
        (4, 'quinn_ridgeway', 'quinlan.ridgeway@colorado.edu', 'password4', datetime.now())
    ]

    for user in users:
        c.execute('INSERT INTO Users (user_id, username, email, password, created_at) VALUES (?, ?, ?, ?, ?)', user)

    # Friends for the website
    friends = [
        (1, 1, 2), # brady and liam
        (2, 1, 3), # brady and brad
        (3, 1, 4), # brady and quinn
        (4, 2, 3), # liam and brad
        (5, 2, 4), # liam and quinn
        (6, 3, 4)  # brad and quinn
    ]

    for friend in friends:
        c.execute('INSERT INTO Friends (friend_id, user_id, friend_user_id) VALUES (?, ?, ?)', friend)
    
    # Reminders for the website
    reminder_d = datetime.now().date() + timedelta(days=7)
    reminders = [
        (1, 1, 1, reminder_d, 'Reminder to interact with user 2'), # brady interacts with liam
        (2, 1, 2, reminder_d, 'Reminder to interact with user 3'), # brady interacts with brad
        (3, 2, 4, reminder_d, 'Reminder to interact with user 4'), # liam interacts with quinn
        (4, 4, 6, reminder_d, 'Reminder to interact with user 3')  # quinn interacts with brad
    ]

    for reminder in reminders: 
        c.execute('INSERT INTO Reminders (reminder_id, user_id, friend_id, reminder_date, message) VALUES (?, ?, ?, ?, ?)', reminder)
    
    # Challenges for the website
    start_date = datetime.now().date()
    end_date = start_date + timedelta(days=7)
    
    challenges = [
        (1, 'Challenge 1', 'This do be a random challenge 1', True, 1, 2, start_date, end_date), # challenge between brady and liam
        (2, 'Challenge 2', 'This is random challenge 2', True, 3, 4, start_date, end_date),  # challenge between brad and quinn
        (3, 'Challenge 3', 'Random challenge 3', True, 1, 4, start_date, end_date)  # challenge between brady and quinn
    ]

    for challenge in challenges:
        c.execute('''
            INSERT INTO Challenges (challenge_id, title, description, joint_flag, user_id_a, user_id_b, start_date, end_date)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', challenge)
    
    # Commit and close
    conn.commit()
    conn.close()
    print("Database filled")

# Remove the database file
def remove_db(db_filename):
    try:
        os.remove(db_filename)
        print(f"Database file '{db_filename}' removed successfully!")
    except FileNotFoundError:
        print(f"Database file '{db_filename}' does not exist.")
    except Exception as e:
        print(f"Error removing database file: {e}")

def print_tables(db_filename):
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")

    print("\nTables:")
    for t in c.fetchall():
        print(f"\t[{t[0]}]")
        c.execute(f"PRAGMA table_info({t[0]});")
        for attr in c.fetchall():
            print(f"\t\t{attr}")
        print("")


### Main
if __name__ == "__main__":

    db_filename = 'ourdata.db'  # Just an example file to make sure it works

    # Check command-line arguments
    if len(sys.argv) > 1 and sys.argv[1] == 'remove':
        remove_db(db_filename)
    else:
        create(db_filename)  # Creates a practice database
        fill(db_filename)  # Fills the database with initial data
        print_tables(db_filename)  # Prints database structure