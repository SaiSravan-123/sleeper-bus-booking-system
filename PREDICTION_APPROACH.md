# Booking Confirmation Prediction – Phase 4

## Objective
The goal of this phase is to predict the probability of booking confirmation
based on historical seat booking data.

## Data Used
The prediction logic uses seat availability data stored in `seats.json`.
The following attributes are considered:
- Total number of seats
- Number of seats already booked

## Prediction Logic
A simple rule-based approach is used to simulate booking prediction.

Formula:
Booking Probability (%) = (Booked Seats / Total Seats) × 100

## Example
If a bus has 30 total seats and 21 seats are booked:
Booking Probability = (21 / 30) × 100 = 70%

## Model Justification
For the scope of this project, a rule-based simulation is sufficient to
demonstrate predictive thinking. In a real-world scenario, this can be
extended using Logistic Regression or Time-Series models.

## Output
The prediction is exposed through a REST API endpoint:
GET /probability

## Limitations
- The prediction does not use real historical datasets
- External factors such as time, demand, or seasonality are not considered
