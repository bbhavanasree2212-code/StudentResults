transactions = [
    {"account": "A101", "type": "Deposit", "amount": 5000},
    {"account": "A102", "type": "Withdrawal", "amount": 12000},
    {"account": "A101", "type": "Deposit", "amount": 3000},
    {"account": "A103", "type": "Deposit", "amount": 15000},
    {"account": "A102", "type": "Deposit", "amount": 8000},
    {"account": "A103", "type": "Withdrawal", "amount": 5000},
    {"account": "A101", "type": "Withdrawal", "amount": 2000}
]

# Calculate total deposits
total_deposit = 0
for t in transactions:
    if t["type"] == "Deposit":
        total_deposit += t["amount"]

print("Total Deposits = $", total_deposit)

# Calculate total withdrawals
total_withdrawal = 0
for t in transactions:
    if t["type"] == "Withdrawal":
        total_withdrawal += t["amount"]

print("Total Withdrawals = $", total_withdrawal)

# Calculate final balances
balances = {}

for t in transactions:
    acc = t["account"]

    if acc not in balances:
        balances[acc] = 0

    if t["type"] == "Deposit":
        balances[acc] += t["amount"]
    else:
        balances[acc] -= t["amount"]

# Find account with highest balance
highest = max(balances, key=balances.get)

print("\nAccount with Highest Balance")
print(highest, "=", balances[highest])

# Suspicious withdrawals (>10000)
print("\nSuspicious Withdrawals")
for t in transactions:
    if t["type"] == "Withdrawal" and t["amount"] > 10000:
        print(t)

# Display final balances
print("\nFinal Balances")
for acc in balances:
    print(acc, "=", balances[acc])
