import sqlite3

db = sqlite3.connect('dati.db')
sql = db.cursor()
sql.execute("""CREATE TABLE IF NOT EXIST rezultati (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            vards TEXT NOT NULL,
            klikski INTEGER NOT NULL,
            laiks INTEGER NOT NULL,
            datums TEXT NOT NULL
            )""")
ieraksti = [
    ('Voldemars', 100, 10, '2022-01-01'),
    ('Voldemars', 100, 10, '2022-01-01'),
    ('Voldemars', 100, 10, '2022-01-01'),
    ('Voldemars', 100, 10, '2022-01-01'),
    ('Voldemars', 100, 10, '2022-01-01'),
    ('Voldemars', 100, 10, '2022-01-01'),
    ('Voldemars', 100, 10, '2022-01-01'),


]
sql.executemany('''
INSERT INTO rezultati (vards, klikski, laiks, datums)
                VALUES (?, ?, ?, ?)
   ''', ieraksti)
db.commit()
db.close()

print("Datubāze un ieraksti izveidoti!")