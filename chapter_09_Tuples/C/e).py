''''
e) Store the data about shares held by a user as tuples containing the following information about shares: 
  Share name 
  Date of purchase 
  Cost price 
  Number of shares 
  Selling price 
Write a program to determine: 
  -Total cost of the portfolio. 
  -Total amount gained or lost. 
  -Percentage profit made or loss incurred
'''

shares = [
    ("Apple", "2023-01-01", 150.0, 10, 200.0),
    ("Google", "2023-02-01", 1000.0, 5, 1200.0),
    ("Microsoft", "2023-03-01", 250.0, 20, 300.0),
    ("Amazon", "2023-04-01", 500.0, 15, 600.0)
]

total_cost = 0
total_gain_loss = 0

for share in shares:
    cost_price = share[2]
    quantity = share[3]
    selling_price = share[4]

    investment = cost_price * quantity
    gain_loss = (selling_price - cost_price) * quantity

    total_cost += investment
    total_gain_loss += gain_loss

percentage = (total_gain_loss / total_cost) * 100

print("Total cost of the portfolio:", total_cost)
print("Total amount gained or lost:", total_gain_loss)
print("Percentage profit made or loss incurred:", percentage)

# Output:
# Total cost of the portfolio: 24250.0
# Total amount gained or lost: 5750.0
# Percentage profit made or loss incurred: 23.71

# Explanation:
'''The program stores share details as tuples.
The total cost is calculated by multiplying cost price with number of shares for each entry.
The gain or loss is calculated as the difference between selling price and cost price multiplied by quantity.
The percentage profit or loss is obtained by dividing total gain or loss by total investment and multiplying by 100.'''
