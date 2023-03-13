import sqlite3

# Connect to the database file
conn = sqlite3.connect(r"D:\inventory2\tinventory.db")

# Get a cursor object
cursor = conn.cursor()

# Get all table names in the database
cursor.execute("SELECT name from sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Iterate through each table
for table_name in tables:
    table_name = table_name[0]
    # Get the columns and data types for the table
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = cursor.fetchall()
    print(f"Table Name: {table_name}")
    # Iterate through each column and print the column name and data type
    for column in columns:
        print(f"Column Name: {column[1]}, Data Type: {column[2]}")
    print("\n")

# Close the connection to the database
conn.close()
