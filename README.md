# sleeper-bus-booking-system
🚌 Sleeper Bus Ticket Booking System
A complete Sleeper Bus Ticket Booking System that demonstrates end-to-end product thinking — from UI/UX design to backend APIs and booking confirmation prediction.
This project is structured in multiple phases and is suitable for academic submission, portfolio showcase, and recruiter evaluation.

📌 Project Overview
The Sleeper Bus Ticket Booking System allows users to:
View available sleeper seats
Book seats with meal preferences
Cancel bookings
View booking confirmation probability
Experience a realistic booking flow through a professional UI design
The system uses Figma for UI/UX, Flask for backend APIs, and a rule-based prediction approach to simulate machine learning logic.

✨ Features
Route selection (Ahmedabad → Mumbai)
Sleeper seat selection with gender-based seats
Meal selection (Veg / Non-Veg / No Meal)
Booking summary and confirmation
Seat booking and cancellation
Booking confirmation probability prediction
Clean project structure and documentation

🎨 UI / UX Design (Phase 2)
The UI/UX of the system is designed using Figma and published as a Figma Site for easy preview.
🔗 Live UI Preview (Figma Site):
https://storm-blur-47569143.figma.site/
UI Screens Included:
Route selection screen

Sleeper seat selection

Meal selection

Booking summary

Booking confirmation screen

Note: No frontend code is implemented. The focus is on UI/UX design and system flow.

🛠 Backend Development (Phase 3)

The backend is built using Python Flask and provides REST APIs to support the booking flow.
🔧 Tech Stack
Language: Python 3
Framework: Flask
Data Storage: JSON files
API Testing: Postman

📂 Project Structure
sleeper-bus-booking-system/
│
├── README.md
├── PREDICTION_APPROACH.md
│
├── frontend/
│   └── README.md
│
└── backend/
    ├── app.py
    ├── requirements.txt
    └── data/
        ├── seats.json
        └── bookings.json

▶️ How to Run the Backend
1️⃣ Navigate to backend folder
cd backend

2️⃣ Install dependencies
pip install flask

3️⃣ Run the server
python app.py

Server will start at:
http://127.0.0.1:5000

🔌 API Endpoints
✅ Home API
GET /

🪑 Get Seat Availability
GET /seats

📝 Book a Seat
POST /book-seat

Request Body

{
  "seat": "A1",
  "meal": "Veg"
}

❌ Cancel Booking
POST /cancel-booking
Request Body

{
  "booking_id": "abcd1234"
}

📊 Booking Confirmation Probability
GET /probability
Returns booking confirmation probability based on seat occupancy.
📈 Prediction Logic (Phase 4)
The booking confirmation probability is calculated using a rule-based approach:
Booking Probability (%) = (Booked Seats / Total Seats) × 100
This logic simulates predictive behavior and demonstrates ML-style thinking without over-engineering.
📄 Detailed explanation is available in:
PREDICTION_APPROACH.md
🧪 Testing
All APIs were tested using Postman
Backend runs locally for demonstration
JSON files are used instead of a database for simplicity
