# Write a program to find the absolute value of a number entered through the keyboard

number = float(input("Enter a number: "))

if number < 0:
  print("The absolute value of", number, "is", -number)
else:
  print("The absolute value of", number, "is", number)

# Output:
# Enter a number: -7.5
# The absolute value of -7.5 is 7.5

# Enter a number: 3.2
# The absolute value of 3.2 is 3.2