orders = [
    {"customer": "Alice", "product": "Laptop", "quantity": 1, "price": 1200},
    {"customer": "Bob", "product": "Mouse", "quantity": 3, "price": 25},
    {"customer": "Charlie", "product": "Laptop", "quantity": 2, "price": 1200},
    {"customer": "David", "product": "Keyboard", "quantity": 2, "price": 50},
    {"customer": "Eva", "product": "Monitor", "quantity": 1, "price": 300}
]

# Calculate total revenue
total_revenue = 0
for order in orders:
    total_revenue += order["quantity"] * order["price"]

print("Total Revenue = $", total_revenue)

# Find the most expensive order
expensive_order = orders[0]
for order in orders:
    if order["price"] > expensive_order["price"]:
        expensive_order = order

print("\nMost Expensive Order")
print(expensive_order)

# Display customers spending more than $1000
print("\nCustomers Spending More Than $1000")
for order in orders:
    amount = order["quantity"] * order["price"]
    if amount > 1000:
        print(order["customer"], "- $", amount)

# Calculate total quantity sold for each product
product_quantity = {}

for order in orders:
    product = order["product"]
    if product in product_quantity:
        product_quantity[product] += order["quantity"]
    else:
        product_quantity[product] = order["quantity"]

print("\nTotal Quantity Sold")
for product in product_quantity:
    print(product, ":", product_quantity[product])

# Display the best-selling product
best_product = max(product_quantity, key=product_quantity.get)

print("\nBest Selling Product =", best_product)
