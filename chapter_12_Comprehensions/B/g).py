# g) Write a program that converts list of temperatures in Fahrenheit degrees to equivalent Celsius degrees using list comprehension.


fahrenheit = [32, 68, 100, 212]
converted = [f"{temp}F = {round((temp - 32)*5/9, 2)}C" for temp in fahrenheit]
print(converted)

# Output:
# ['32F = 0.0C', '68F = 20.0C', '100F = 37.78C', '212F = 100.0C']

# Explanation:
# The list comprehension iterates through each temperature in the 'fahrenheit' list and applies the formula to convert it to Celsius: (F - 32) * 5/9. The result is rounded to 2 decimal places for better readability. Each converted temperature is formatted as a string showing both the Fahrenheit and Celsius values. The resulting list 'converted' contains the formatted strings for each temperature conversion.

