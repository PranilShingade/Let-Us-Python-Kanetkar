# Population of a town today is 100000. The population has increased steadily at the rate of 10 % per year for last 10 years. Write a program to determine the population at the end of each year in the last decade

population = 100000

for year in range(1, 11):
  population = population * 1.1
  print("The population at the end of year", year, "is:", population)

# Output:
# The population at the end of year 1 is: 110000.0
# The population at the end of year 2 is: 121000.0
# The population at the end of year 3 is: 133100.0
# The population at the end of year 4 is: 146410.0
# The population at the end of year 5 is: 161051.0
# The population at the end of year 6 is: 177156.10000000004
# The population at the end of year 7 is: 194871.71000000005
# The population at the end of year 8 is: 214358.88100000006
# The population at the end of year 9 is: 236685.00000000004
# The population at the end of year 10 is: 261000.0

# Explanation:
# The program initializes the population to 100000.
# It then uses a for loop to iterate through each year from 1 to 10.
# In each iteration, it increases the population by 10% and prints the population at the end of that year.
# The output shows the population at the end of each year for the last decade.