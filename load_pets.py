import sqlite3

# Connect to the database
conn = sqlite3.connect('pets.db')
cursor = conn.cursor()

# Data to be inserted into tables
person_data = [
    (1, 'James', 'Smith', 41),
    (2, 'Diana', 'Greene', 23),
    (3, 'Sara', 'White', 27),
    (4, 'William', 'Gibson', 23)
]

pet_data = [
    (1, 'Rusty', 'Dalmation', 4, 1),
    (2, 'Bella', 'Alaskan Malamute', 3, 0),
    (3, 'Max', 'Cocker Spaniel', 1, 0),
    (4, 'Rocky', 'Beagle', 7, 0),
    (5, 'Rufus', 'Cocker Spaniel', 1, 0),
    (6, 'Spot', 'Bloodhound', 2, 1)
]

person_pet_data = [
    (1, 1),
    (1, 2),
    (2, 3),
    (2, 4),
    (3, 5),
    (4, 6)
]

# Create tables if they don't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS person (
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        age INTEGER
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS pet (
        id INTEGER PRIMARY KEY,
        name TEXT,
        breed TEXT,
        age INTEGER,
        dead INTEGER
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS person_pet (
        person_id INTEGER,
        pet_id INTEGER
    )
''')

# Insert data into tables
cursor.executemany('INSERT INTO person VALUES (?, ?, ?, ?)', person_data)
cursor.executemany('INSERT INTO pet VALUES (?, ?, ?, ?, ?)', pet_data)
cursor.executemany('INSERT INTO person_pet VALUES (?, ?)', person_pet_data)

# Commit changes and close the connection
conn.commit()
conn.close()
