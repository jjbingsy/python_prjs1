import sqlite3

def main():
    database = "Series230209.db"

    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS Series (
                                        series_id integer PRIMARY KEY,
                                        series_name text NOT NULL UNIQUE,
                                        series_alias text
                                    ); """

    sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS Films (
                                    flim_id integer PRIMARY KEY,
                                    film_name text NOT NULL UNIQUE,
                                    film_description TEXT,
                                    series_id integer,
                                    FOREIGN KEY (series_id) REFERENCES Series (series_id)
                                );"""

    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute(sql_create_projects_table)
    c.execute(sql_create_tasks_table)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()