import sqlite3

# conn = sqlite3.connect("new.db")
with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    # cities = [
    #     ('Boston', 'MA', 6000000),
    #     ('Chicago', 'IL', 2700000),
    #     ('Houston', 'TX', 2100000),
    #     ('Phoenix', 'AZ', 1500000)
    # ]
    #
    # c.executemany('INSERT INTO Population  VALUES(?, ?, ?)', cities)

    # use a for loop to iterate through the database, printing the results line by line
    # for row in c.execute("SELECT city, state from Population"):
    #     print row

    c.execute("SELECT city, state from Population")

    # fetchall() retrieves all records from the query
    rows = c.fetchall()

    # output the rows to the screen, row by row
    for r in rows:
        print r[0], r[1]
# conn.commit()

# conn.close()
