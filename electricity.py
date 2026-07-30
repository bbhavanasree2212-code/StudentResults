houses = [
    {"house_no": 101, "units": 250, "solar": 50},
    {"house_no": 102, "units": 120, "solar": 30},
    {"house_no": 103, "units": 350, "solar": 100},
    {"house_no": 104, "units": 90, "solar": 20},
    {"house_no": 105, "units": 450, "solar": 80}
]

# Calculate bill using slabs
def calculate_bill(units):
    if units <= 100:
        return units * 2
    elif units <= 300:
        return (100 * 2) + ((units - 100) * 3)
    else:
        return (100 * 2) + (200 * 3) + ((units - 300) * 5)

print("House Summary")

highest = houses[0]

for house in houses:
    net_usage = house["units"] - house["solar"]
    bill = calculate_bill(net_usage)

    print("\nHouse Number:", house["house_no"])
    print("Net Usage:", net_usage, "units")
    print("Bill: $", bill)

    if net_usage < 100:
        print("Eligible for Green Incentive")
    else:
        print("Not Eligible for Green Incentive")

    if net_usage > (highest["units"] - highest["solar"]):
        highest = house

print("\nHighest Consumer")
print(highest)

print("\nSummary Report")
print("Total Houses =", len(houses))
