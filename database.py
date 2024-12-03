import sqlite3

def initialize_database():
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    
    # Crearea tabelelor
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS carti (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titlu TEXT NOT NULL,
            autor TEXT NOT NULL,
            gen TEXT NOT NULL,
            stoc INTEGER NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS utilizatori (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nume TEXT NOT NULL,
            adresa TEXT NOT NULL,
            telefon TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS imprumuturi (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_utilizator INTEGER NOT NULL,
            id_carte INTEGER NOT NULL,
            data_imprumut DATE NOT NULL,
            data_returnare DATE,
            FOREIGN KEY (id_utilizator) REFERENCES utilizatori(id),
            FOREIGN KEY (id_carte) REFERENCES carti(id)
        )
    ''')
    
    conn.commit()
    conn.close()

def adauga_carte(titlu, autor, gen, stoc):
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO carti (titlu, autor, gen, stoc) VALUES (?, ?, ?, ?)', 
                   (titlu, autor, gen, stoc))
    conn.commit()
    conn.close()

def adauga_utilizator(nume, adresa, telefon):
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO utilizatori (nume, adresa, telefon) VALUES (?, ?, ?)', 
                   (nume, adresa, telefon))
    conn.commit()
    conn.close()
