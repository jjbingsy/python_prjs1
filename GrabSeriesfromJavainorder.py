import sqlite3
import webbrowser

url = 'https://missav.com/en/search/'
url2 = 'https://jav.guru/?s='
#webbrowser.open(url)

# Connect to the SQLite database
conn = sqlite3.connect('Series230209.db')


cursor = conn.cursor()
# Execute the SQL query to retrieve the most occurring to the least occurring values of the "series_id" field from the "films" table
#SELECT series_id, COUNT(*) as ct FROM films GROUP BY series_id  ORDER BY ct DESC')
cursor = cursor.execute("""
 SELECT series_id, ct
  FROM (
    SELECT series_id, COUNT(*) as ct
    FROM films
    GROUP BY series_id
  )
  WHERE ct < 5
  ORDER BY ct DESC
""")

# Store the result in the "SeriesOrder" list
SeriesOrder = [(row[0], row[1]) for row in cursor.fetchall()]

# Close the database connection

for series, cnt in SeriesOrder:
    print (series,cnt)
    h = 'y'
    cursor.execute ('SELECT film_name FROM films WHERE series_id = ?', (series,))
    while h == 'y':
        film = cursor.fetchone()
        print (film[0], series)
        webbrowser.open (url + film[0].lower())
        webbrowser.open (url2 + film[0].lower())
        h = input("continue")
    if h == 's':
        break



conn.close()



