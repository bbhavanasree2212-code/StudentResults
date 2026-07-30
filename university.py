students = [
    {"name": "Alice", "Python": 85, "Mathematics": 90, "AI": 88},
    {"name": "Bob", "Python": 40, "Mathematics": 55, "AI": 60},
    {"name": "Charlie", "Python": 95, "Mathematics": 98, "AI": 97},
    {"name": "David", "Python": 65, "Mathematics": 70, "AI": 68},
    {"name": "Eva", "Python": 30, "Mathematics": 45, "AI": 35}
]

for s in students:
    total = s["Python"] + s["Mathematics"] + s["AI"]
    percentage = total / 3
    s["Total"] = total
    s["Percentage"] = percentage

    if percentage >= 90:
        grade = "A"
    elif percentage >= 80:
        grade = "B"
    elif percentage >= 70:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    s["Grade"] = grade

print("Student Results")
for s in students:
    print(s)

topper = max(students, key=lambda x: x["Percentage"])
print("\nClass Topper:")
print(topper["name"], topper["Percentage"])

print("\nFailed Students:")
for s in students:
    if s["Python"] < 50 or s["Mathematics"] < 50 or s["AI"] < 50:
        print(s["name"])

print("\nSorted by Percentage:")
students.sort(key=lambda x: x["Percentage"], reverse=True)

for s in students:
    print(s["name"], "-", round(s["Percentage"], 2))
