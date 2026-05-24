from flask import Flask, jsonify, request
from database.db import init_db
from services.flight_service import get_all_flights, get_flight_by_id, search_flights
from services.booking_service import get_all_bookings, create_booking, cancel_booking

app = Flask(__name__)
init_db()

@app.route('/flights', methods=['GET'])
def flights():
    return jsonify(get_all_flights())

#Get one flight
@app.route('/flights/<int:flight_id>', methods=['GET'])
def flight_by_id(flight_id):
    flight = get_flight_by_id(flight_id)
    if flight is None:
        return jsonify({"error": "Flight not found"}), 404
    return jsonify(flight)

@app.route('/flights/search', methods=['GET'])
def search():
    origin = request.args.get('origin')
    destination = request.args.get('destination')
    results = search_flights(origin, destination)
    return jsonify(results)

@app.route('/bookings', methods=['POST'])
def book():
    data = request.get_json()
    flight_id = data.get('flight_id')
    passenger_name = data.get('passenger_name')
    passenger_email = data.get('passenger_email')
    result = create_booking(flight_id, passenger_name, passenger_email)
    return jsonify(result)

@app.route('/bookings/<int:booking_id>', methods=['DELETE'])
def cancel(booking_id):
    result = cancel_booking(booking_id)
    if "error" in result:
        return jsonify(result), 404
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)     