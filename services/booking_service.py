from database.db import get_connection
from models.booking import Booking

def get_all_the_bookings():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bookings")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return [Booking(**row) for row in rows]

def create_booking(flight_id, passenger_name, passenger_email):
    conn = get_connection()
    cursor = conn.cursor()

      # Check if flight exists and has seats available
      
    cursor.execute("SELECT * FROM flights WHERE id = ?", (flight_id,))
    flight = cursor.fetchone()
    
    if flight is None:
        return {"error": "Flight not found"}

    if flight['seats_available'] <= 0:
        return {"error": "No seats available"}

    cursor.execute('''
    INSERT INTO bookings (flight_id, passenger_name, passenger_email)
    VALUES (?, ?, ?)
''', (flight_id, passenger_name, passenger_email))
    
    # Decrease available seats by 1
    cursor.execute('''
    UPDATE flights SET seats_available = seats_available - 1 WHERE id = ?
''', (flight_id,))

    conn.commit()
    booking_id = cursor.lastrowid
    cursor.close()
    conn.close()

    return {"message": "Booking successful!", "booking_id": booking_id}
 
def cancel_booking(booking_id):
    conn = get_connection()
    cursor = conn.cursor()

      # Check if booking exists
    cursor.execute("SELECT * FROM bookings WHERE id = ?", (booking_id,))
    booking = cursor.fetchone()

    if booking is None:
        conn.close()
        return {"error": "Booking not found"}

    flight_id = booking['flight_id']

    # Delete the booking
    cursor.execute("DELETE FROM bookings WHERE id = ?", (booking_id,))

   # Give the seat back
    cursor.execute('''
        UPDATE flights SET seats_available = seats_available + 1
        WHERE id = ?
    ''', (booking["flight_id"],))

    conn.commit()
    conn.close()
    return {"message": "Booking cancelled successfully!"}