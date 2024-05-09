#database connectivity

import sqlite3

def create_connection(database):
    conn = None
    try:
        conn = sqlite3.connect(database)
        print("Connected to the database")
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS students
                          (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
        print("Table created successfully")
    except sqlite3.Error as e:
        print(e)

def insert_record(conn, name, age):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", (name, age))
        conn.commit()
        print("Record inserted successfully")
    except sqlite3.Error as e:
        print(e)

def display_records(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        print("Records:")
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)

# Main function
def main():
    # Connect to the database
    conn = create_connection("example.db")
    if conn is not None:
        # Create a table
        create_table(conn)
        
        # Insert some records
        insert_record(conn, "Alice", 25)
        insert_record(conn, "Bob", 30)
        insert_record(conn, "Charlie", 35)
        
        # Display all records
        display_records(conn)
        
        # Close the connection
        conn.close()
        print("Connection closed")

if __name__ == '__main__':
    main()
