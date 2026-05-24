from database.db import get_connection
from models.flight import Flight

def get_all_flights():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM flights")
    rows = cursor.fetchall()
    conn.close()
    return [Flight(*row).to_dict() for row in rows]

def get_flight_by_id(flight_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM flights WHERE id = ?", (flight_id,))
    row = cursor.fetchone()
    conn.close()
    if row is None:
        return None
    return Flight(*row).to_dict()

def search_flights(origin, destination):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM flights WHERE origin = ? AND destination = ?",
        (origin, destination)
    )
    rows = cursor.fetchall()
    conn.close()
    return [Flight(*row).to_dict() for row in rows]