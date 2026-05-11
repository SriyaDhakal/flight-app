import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), '../data/flights.db')

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    # Create flights table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS flights (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            flight_number TEXT NOT NULL,
            origin TEXT NOT NULL,
            destination TEXT NOT NULL,
            departure_time TEXT NOT NULL,
            arrival_time TEXT NOT NULL,
            price REAL NOT NULL,
            seats_available INTEGER NOT NULL
        )
    ''')

    # Create bookings table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            flight_id INTEGER NOT NULL,
            passenger_name TEXT NOT NULL,
            passenger_email TEXT NOT NULL,
            booked_at TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (flight_id) REFERENCES flights(id)
        )
    ''')

    # Add fake flight data only if table is empty
    cursor.execute("SELECT COUNT(*) FROM flights")
    if cursor.fetchone()[0] == 0:
        sample_flights = [
            ('AA101', 'New York', 'Los Angeles', '2026-06-01 08:00', '2026-06-01 11:00', 299.99, 50),
            ('UA202', 'Chicago', 'Houston', '2026-06-02 10:00', '2026-06-02 13:00', 199.99, 30),
            ('DL303', 'Dallas', 'Miami', '2026-06-03 14:00', '2026-06-03 18:00', 249.99, 20),
            ('SW404', 'Seattle', 'Denver', '2026-06-04 09:00', '2026-06-04 11:30', 179.99, 40),
            ('AA505', 'Boston', 'Atlanta', '2026-06-05 07:00', '2026-06-05 10:00', 219.99, 25),
        ]
        cursor.executemany('''
            INSERT INTO flights (flight_number, origin, destination, departure_time, arrival_time, price, seats_available)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', sample_flights)

    conn.commit()
    conn.close()
    print("Database initialized successfully!")

if __name__ == '__main__':
    init_db()