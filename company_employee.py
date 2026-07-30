# Employee Performance Evaluation

employees = [
    {"name": "Alice", "dept": "HR", "productivity": 90, "attendance": 95, "teamwork": 88},
    {"name": "Bob", "dept": "IT", "productivity": 85, "attendance": 80, "teamwork": 92},
    {"name": "Charlie", "dept": "Finance", "productivity": 78, "attendance": 85, "teamwork": 80},
    {"name": "David", "dept": "IT", "productivity": 95, "attendance": 90, "teamwork": 94},
    {"name": "Eva", "dept": "HR", "productivity": 70, "attendance": 75, "teamwork": 72},
    {"name": "Frank", "dept": "Finance", "productivity": 88, "attendance": 92, "teamwork": 90}
]

# Weights
wp = 0.5
wa = 0.3
wt = 0.2

dept_total = {}
dept_count = {}

# Calculate score and rating
for emp in employees:
    score = (emp["productivity"] * wp +
             emp["attendance"] * wa +
             emp["teamwork"] * wt)
    emp["score"] = score

    if score >= 90:
        emp["rating"] = "Excellent"
    elif score >= 80:
        emp["rating"] = "Good"
    elif score >= 70:
        emp["rating"] = "Average"
    else:
        emp["rating"] = "Poor"

    dept = emp["dept"]
    dept_total[dept] = dept_total.get(dept, 0) + score
    dept_count[dept] = dept_count.get(dept, 0) + 1

# Display employee scores and ratings
print("Employee Performance")
for emp in employees:
    print(f"{emp['name']} ({emp['dept']})")
    print(f"Score : {emp['score']:.2f}")
    print(f"Rating: {emp['rating']}\n")

# Top 3 employees
employees.sort(key=lambda x: x["score"], reverse=True)

print("Top Three Employees")
for i in range(3):
    print(f"{i+1}. {employees[i]['name']} - {employees[i]['score']:.2f}")

# Department-wise average
print("\nDepartment-wise Average Score")
for dept in dept_total:
    avg = dept_total[dept] / dept_count[dept]
    print(f"{dept}: {avg:.2f}")
