import sqlite3

# conn = sqlite3.connect("new.db")
with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    cities = [
        ('Boston', 'MA', 6000000),
        ('Chicago', 'IL', 2700000),
        ('Houston', 'TX', 2100000),
        ('Phoenix', 'AZ', 1500000)
    ]

    c.executemany('INSERT INTO Population  VALUES(?, ?, ?)', cities)

# conn.commit()

# conn.close()
