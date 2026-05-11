class Flight:
    def __init__(self, id, flight_number, origin, destination, departure_time, arrival_time, price, seats_available):
        self.id = id
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.price = price
        self.seats_available = seats_available
  #What is to_dict?
#It converts your flight object into a dictionary so Flask can send it as JSON to the user.
    def to_dict(self):
        return {
            "id": self.id,
            "flight_number": self.flight_number,
            "origin": self.origin,
            "destination": self.destination,
            "departure_time": self.departure_time,
            "arrival_time": self.arrival_time,
            "price": self.price,
            "seats_available": self.seats_available
        }