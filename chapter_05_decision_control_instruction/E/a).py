# Any integer is input through the keyboard. Write a program to find out whether it is an odd number or even number

number = int(input("Enter an integer: "))

if number % 2 == 0:
  print("The number is even.")
else:
  print("The number is odd.")

# Output:
# Enter an integer: 5
# The number is odd

# Enter an integer: 10
# The number is even
