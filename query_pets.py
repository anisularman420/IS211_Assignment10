import sqlite3

# Connect to the database
conn = sqlite3.connect('pets.db')
cursor = conn.cursor()

# Check if the tables exist
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='person'")
if not cursor.fetchone():
    print("Tables do not exist. Please run load_pets.py first.")
    conn.close()
    exit()

while True:
    # Ask for a person's ID number
    person_id = input("Enter a person's ID number (enter 1 to exit): ")

    if person_id == '1':
        break

    # Query and display data
    cursor.execute('SELECT * FROM person WHERE id = ?', (person_id,))
    person = cursor.fetchone()

    if person:
        print(f"{person[1]} {person[2]}, {person[3]} years old")

        cursor.execute('''
            SELECT pet.name, pet.breed, pet.age
            FROM pet
            JOIN person_pet ON pet.id = person_pet.pet_id
            WHERE person_pet.person_id = ?
        ''', (person_id,))

        pets = cursor.fetchall()

        for pet in pets:
            print(f"Owned {pet[0]}, a {pet[1]}, that was {pet[2]} years old")
    else:
        print("Person not found")

# Close the connection
conn.close()
