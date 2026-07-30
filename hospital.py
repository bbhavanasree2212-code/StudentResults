patients = [
    {"Name": "Rahul", "Age": 45, "HeartRate": 55, "Oxygen": 92},
    {"Name": "Priya", "Age": 30, "HeartRate": 75, "Oxygen": 98},
    {"Name": "Amit", "Age": 60, "HeartRate": 110, "Oxygen": 90},
    {"Name": "Sneha", "Age": 40, "HeartRate": 85, "Oxygen": 96},
    {"Name": "Kiran", "Age": 50, "HeartRate": 65, "Oxygen": 99}
]

critical = []

print("Patient Details")

for p in patients:
    if p["HeartRate"] < 60 or p["HeartRate"] > 100 or p["Oxygen"] < 95:
        status = "Critical"
        critical.append(p)
    elif 60 <= p["HeartRate"] <= 100 and p["Oxygen"] >= 95:
        status = "Normal"
    else:
        status = "Observation"

    p["Status"] = status
    print(p)

print("\nCritical Patients")
for p in critical:
    print(p["Name"])

if len(critical) > 0:
    avg_age = sum(p["Age"] for p in critical) / len(critical)
    print("\nAverage Age of Critical Patients:", round(avg_age, 2))
else:
    print("\nNo Critical Patients")

print("\nPatients Sorted by Oxygen Saturation")
patients.sort(key=lambda x: x["Oxygen"])

for p in patients:
    print(p["Name"], "-", p["Oxygen"])
