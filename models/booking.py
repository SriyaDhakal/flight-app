class Booking:
    def __init__(self, id, flight_id, passenger_name, passenger_email,booked_at):
        self.id = id
        self.flight_id = flight_id
        self.passenger_name = passenger_name
        self.passenger_email = passenger_email
        self.booked_at = booked_at

    def to_dict(self):
        return {
            "id": self.id,
            "flight_id": self.flight_id,
            "passenger_name": self.passenger_name,
            "passenger_email": self.passenger_email,
            "booked_at": self.booked_at
        }