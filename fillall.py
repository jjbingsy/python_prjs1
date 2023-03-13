import sqlite3
from pathlib import Path
import json

"""
This Python code connects to an SQLite database named tfilms.db using the sqlite3 library.
It then defines a variable called images_path that stores the path to a directory containing image files.
The code then defines an SQL query string that will be used to insert data into the films table of the database.
Next, the code creates a Path object representing the directory containing the image files, and uses the iterdir()
method to get a generator object containing all the files in the directory. It then uses a list comprehension to 
create a new list of tuples, where each tuple contains the stem (i.e., file name without extension) of a file in 
the directory and an empty string. This list of tuples will be used to insert data into the database.
Finally, the code uses the executemany() method of the database cursor to execute the SQL query on the list of tuples.
The commit() method is called to commit the changes to the database, and the close() method is called to close the 
database connection.
"""

# Connect to the database
conn = sqlite3.connect('tfilms.db')
cr = conn.cursor()

# Define image directory path and SQL query string
images_path = "F:/trusti"
query = "INSERT OR IGNORE INTO films(name, description) VALUES (?,?)"

# Get list of file stems from the image directory using list comprehension
dir_path = Path(images_path)
file_list = list(dir_path.iterdir())
new_list =  [(file_path.stem, "") for file_path in file_list]

# Execute SQL query on the list of file stems and commit changes to the database
cr.executemany(query, new_list)
conn.commit()


# Connect to the database

# Search for film names and descriptions and convert the results to a JSON file
query = 'SELECT name, description FROM films'
results = cr.execute(query).fetchall()

# Convert the results to a list of dictionaries
data = [{'name': row[0], 'description': row[1]} for row in results]

# Convert the data to JSON and write it to a file
with open('films.json', 'w') as f:
    json.dump(data, f)

# Close the database connection




conn.close()
