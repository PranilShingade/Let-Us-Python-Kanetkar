# How will you display price in 10 columns with 4 places beyond decimal points? Assume value of price to be 1.5567894

price = 1.5567894
print(f'{price:10.4f}')

# Output:
#     1.5568

# 10 means the price is left-aligned and padded with 10 spaces.
# 4 means the price is formatted to 4 decimal places.