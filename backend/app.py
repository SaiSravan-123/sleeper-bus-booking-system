import os
from flask import Flask, request, jsonify
import json
import uuid

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SEATS_FILE = os.path.join(BASE_DIR, "data", "seats.json")
BOOKINGS_FILE = os.path.join(BASE_DIR, "data", "bookings.json")


# Helper functions
def load_json(file):
    with open(file, "r") as f:
        return json.load(f)

def save_json(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=2)

# Home API
@app.route("/")
def home():
    return jsonify({"message": "Bus Booking API is running"})

# Get all seats
@app.route("/seats", methods=["GET"])
def get_seats():
    seats = load_json(SEATS_FILE)
    return jsonify(seats)

# Book a seat
@app.route("/book-seat", methods=["POST"])
def book_seat():
    data = request.json
    seat_number = data.get("seat")
    meal = data.get("meal")

    seats = load_json(SEATS_FILE)
    bookings = load_json(BOOKINGS_FILE)

    for seat in seats:
        if seat["seat"] == seat_number:
            if seat["status"] == "booked":
                return jsonify({"error": "Seat already booked"}), 400
            seat["status"] = "booked"

            booking_id = str(uuid.uuid4())[:8]

            booking = {
                "booking_id": booking_id,
                "seat": seat_number,
                "meal": meal,
                "route": "Ahmedabad - Mumbai"
            }

            bookings.append(booking)

            save_json(SEATS_FILE, seats)
            save_json(BOOKINGS_FILE, bookings)

            return jsonify({
                "message": "Seat booked successfully",
                "booking_id": booking_id
            })

    return jsonify({"error": "Seat not found"}), 404

# Cancel booking
@app.route("/cancel-booking", methods=["POST"])
def cancel_booking():
    data = request.json
    booking_id = data.get("booking_id")

    seats = load_json(SEATS_FILE)
    bookings = load_json(BOOKINGS_FILE)

    for booking in bookings:
        if booking["booking_id"] == booking_id:
            seat_number = booking["seat"]
            bookings.remove(booking)

            for seat in seats:
                if seat["seat"] == seat_number:
                    seat["status"] = "available"

            save_json(SEATS_FILE, seats)
            save_json(BOOKINGS_FILE, bookings)

            return jsonify({"message": "Booking cancelled successfully"})

    return jsonify({"error": "Booking ID not found"}), 404

# Booking probability
@app.route("/probability", methods=["GET"])
def booking_probability():
    seats = load_json(SEATS_FILE)
    total = len(seats)
    booked = len([s for s in seats if s["status"] == "booked"])
    probability = round((booked / total) * 100, 2)

    return jsonify({"booking_probability": f"{probability}%"})

if __name__ == "__main__":
    app.run(debug=True)
