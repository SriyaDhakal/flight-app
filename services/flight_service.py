from database.db import get_connection
from models.flight import Flight

#Function1: Get all flights
def get_all_the_flights():
   conn= get_connection()#open the database door
   cursor= conn.cursor()#get the key to the database, like a pen that reads and write from the database
   cursor.execute("SELECT * FROM flights")#execute the SQL command to get all the flights
   rows= cursor.fetchall()#fetch all the results from the executed command
   conn.close()#close the database door
   return [Flight(**row) for row in rows]   #convert every row into a Flight object and return a list of Flight objects

#function2: Get a flight by id or get one flight by id
def get_flight_by_id(flight_id):
   cursor.execute("SELECT * FROM flights WHERE id = ?", (flight_id,))#execute the SQL command to get a flight by id
   row= cursor.fetchone()#fetch the result from the executed command
   if row is None:#if there is no flight with the given id, return None
      return None
   return Flight(**row).to_dict()#convert the row into a Flight object and return it

def search_flights(origin, destination):
    cursor.execute(
        "SELECT * FROM flights WHERE origin = ? AND destination = ?",
        (origin, destination)
    )