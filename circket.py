players = [
    {"name": "Virat", "runs": 700, "balls": 450, "wickets": 2},
    {"name": "Rohit", "runs": 650, "balls": 420, "wickets": 1},
    {"name": "Hardik", "runs": 400, "balls": 250, "wickets": 18},
    {"name": "Jadeja", "runs": 350, "balls": 280, "wickets": 25},
    {"name": "Gill", "runs": 800, "balls": 500, "wickets": 0}
]

# Calculate strike rate
print("Strike Rates")
for p in players:
    strike_rate = (p["runs"] / p["balls"]) * 100
    p["strike_rate"] = strike_rate
    print(p["name"], "=", round(strike_rate, 2))

# Orange Cap Winner
orange = max(players, key=lambda x: x["runs"])

print("\nOrange Cap Winner")
print(orange["name"], "-", orange["runs"], "runs")

# Purple Cap Winner
purple = max(players, key=lambda x: x["wickets"])

print("\nPurple Cap Winner")
print(purple["name"], "-", purple["wickets"], "wickets")

# Strike rate above 150
print("\nPlayers with Strike Rate Above 150")
for p in players:
    if p["strike_rate"] > 150:
        print(p["name"], "-", round(p["strike_rate"], 2))

# Rank players by runs
ranked = sorted(players, key=lambda x: x["runs"], reverse=True)

print("\nPlayers Ranked by Runs")
for p in ranked:
    print(p["name"], "-", p["runs"])
