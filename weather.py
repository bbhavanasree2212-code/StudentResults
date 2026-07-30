weather = [
    {"day": "Monday", "temperature": 35, "humidity": 70, "rainfall": 5},
    {"day": "Tuesday", "temperature": 42, "humidity": 60, "rainfall": 0},
    {"day": "Wednesday", "temperature": 38, "humidity": 75, "rainfall": 10},
    {"day": "Thursday", "temperature": 45, "humidity": 55, "rainfall": 0},
    {"day": "Friday", "temperature": 30, "humidity": 90, "rainfall": 20},
    {"day": "Saturday", "temperature": 41, "humidity": 65, "rainfall": 2},
    {"day": "Sunday", "temperature": 36, "humidity": 80, "rainfall": 15}
]

# Find hottest day
hottest = max(weather, key=lambda x: x["temperature"])
print("Hottest Day:", hottest["day"], "-", hottest["temperature"], "°C")

# Find coldest day
coldest = min(weather, key=lambda x: x["temperature"])
print("Coldest Day:", coldest["day"], "-", coldest["temperature"], "°C")

# Calculate average temperature
total_temp = 0
for day in weather:
    total_temp += day["temperature"]

average = total_temp / len(weather)
print("Average Temperature:", average)

# Count rainy days
rainy_days = 0
for day in weather:
    if day["rainfall"] > 0:
        rainy_days += 1

print("Rainy Days:", rainy_days)

# Identify heatwave days
print("\nHeatwave Days")
for day in weather:
    if day["temperature"] > 40:
        print(day["day"], "-", day["temperature"], "°C")

# Display data sorted by rainfall
sorted_weather = sorted(weather, key=lambda x: x["rainfall"])

print("\nWeather Data Sorted by Rainfall")
for day in sorted_weather:
    print(day)
