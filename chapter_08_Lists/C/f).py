# Write a program that converts list of temperatures in Fahrenheit degrees to equivalent Celsius degrees

fahrenheit = [32, 68, 98.6, 212]
celsius = [(fahrenheit[i] - 32) * 5.0/9.0 for i in range(len(fahrenheit))]
print("Fahrenheit:", fahrenheit)
print("Celsius:", celsius)

# Output:
# Fahrenheit: [32, 68, 98.6, 212]
# Celsius: [0.0, 20.0, 37.0, 100.0]

# Explanation:
# The program defines a list fahrenheit containing temperatures in Fahrenheit degrees.
# It then uses list comprehension to convert each Fahrenheit temperature to Celsius using the formula (Fahrenheit - 32) * 5.0/9.0.
# The resulting list of Celsius temperatures is printed.