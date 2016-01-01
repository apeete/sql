import sqlite3

# conn = sqlite3.connect("new.db")
with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    c.execute("INSERT INTO Population VALUES('New York City', \
        'NY', 8200000)")

    c.execute("INSERT INTO Population VALUES('San Francisco', \
        'CA', 8000000)")

# conn.commit()

# conn.close()
