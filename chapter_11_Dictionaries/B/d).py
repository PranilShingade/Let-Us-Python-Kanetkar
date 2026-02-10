# d) Create two dictionaries—one containing grocery items and their prices and another containing grocery items and quantity purchased. By using the values from these two dictionaries compute the total bill.

prices = {
    'milk': 50,
    'eggs': 20,
    'bread': 30,
    'juice': 60
}

quantities = {
    'milk': 2,
    'eggs': 4,
    'bread': 1,
    'juice': 1
}

total_bill = 0

for item, quantity in quantities.items():
    if item in prices:
        total_bill += prices[item] * quantity

print(f"Total bill: {total_bill}")

# Output:
# Total bill: 290

# Explanation:
# Two dictionaries are created, one containing grocery items and their prices and another containing grocery items and quantity purchased.
# Using the values from these two dictionaries, the total bill is calculated by multiplying the price of each item by the quantity purchased.
# Finally, the total bill is printed.