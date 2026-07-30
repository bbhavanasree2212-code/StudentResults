flights = [
    {"flight_no": "AI101", "destination": "Delhi", "departure": "08:30", "delay": 30},
    {"flight_no": "AI202", "destination": "Mumbai", "departure": "10:00", "delay": 75},
    {"flight_no": "AI303", "destination": "Chennai", "departure": "09:15", "delay": 0},
    {"flight_no": "AI404", "destination": "Bangalore", "departure": "11:45", "delay": 90},
    {"flight_no": "AI505", "destination": "Hyderabad", "departure": "07:50", "delay": 20}
]

# Display delayed flights
print("Delayed Flights")
for flight in flights:
    if flight["delay"] > 0:
        print(flight)

# Find the longest delay
longest = max(flights, key=lambda x: x["delay"])
print("\nLongest Delay")
print(longest)

# Calculate average delay
total_delay = 0
for flight in flights:
    total_delay += flight["delay"]

average_delay = total_delay / len(flights)
print("\nAverage Delay =", average_delay, "minutes")

# Sort flights by departure time
sorted_flights = sorted(flights, key=lambda x: x["departure"])

print("\nFlights Sorted by Departure Time")
for flight in sorted_flights:
    print(flight)

# Display flights delayed more than 60 minutes
print("\nFlights Delayed More Than 60 Minutes")
for flight in flights:
    if flight["delay"] > 60:
        print(flight)fl
