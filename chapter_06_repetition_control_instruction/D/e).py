# Write a program to find the factorial value of any number entered through the keyboard

num = int(input("Enter a number to find its factorial: "))
factorial = 1

for i in range(1, num + 1):
  factorial *= i

print("The factorial of", num, "is", factorial)

# Output:
# Enter a number to find its factorial: 5
# The factorial of 5 is 120

# Explanation:
# The program prompts the user to enter a number.
# It initializes a variable factorial to 1.

# The program then uses a for loop to calculate the factorial of the entered number.
# It multiplies the factorial variable by each number from 1 to the entered number (inclusive).

# Finally, the program prints the factorial of the entered number.
