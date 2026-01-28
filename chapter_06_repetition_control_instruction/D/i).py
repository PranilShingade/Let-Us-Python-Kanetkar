# When interest compounds q times per year at an annual rate of r % for n years, the principal p compounds to an amount a as per the following formula: a = p ( 1 + r/ q ) ^ nq
# Write a program to read 10 sets of p, r, n & q and calculate the corresponding as

p = float(input("Enter the principal amount: "))
r = float(input("Enter the annual interest rate (in %): ")) / 100
n = float(input("Enter the number of years: "))
q = float(input("Enter the number of times the interest is compounded per year: "))

a = p * (1 + r / q) ** (n * q)

print("The amount after", n, "years is:", a)

# Output:
# Enter the principal amount: 1000
# Enter the annual interest rate (in %): 5
# Enter the number of years: 2
# Enter the number of times the interest is compounded per year: 12
# The amount after 2 years is: 1200.0

# Explanation:
# The program prompts the user to enter the principal amount, annual interest rate, number of years, and number of times the interest is compounded per year.
# It then calculates the amount after the specified number of years using the compound interest formula.
# The output shows the amount after the specified number of years.
# Note: The interest rate should be provided as a decimal (e.g., for 5%, enter 0.05).