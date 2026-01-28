# A five-digit number is entered through the keyboard. Write a program to obtain the reversed number and to determine whether the original and reversed numbers are equal or not

num = int(input("Enter a five-digit number: "))
original_num = num
reversed_num = 0

while num > 0:
  digit = num % 10
  reversed_num = reversed_num * 10 + digit
  num //= 10

if original_num == reversed_num:
  print("The original and reversed numbers are equal.")
else:
  print("The original and reversed numbers are not equal.") 

# Output:
# Enter a five-digit number: 12321
# The original and reversed numbers are equal.

# Explanation:
# The program prompts the user to enter a five-digit number.
# It then reverses the number by extracting each digit and constructing the reversed number.
# Finally, it checks if the original and reversed numbers are equal or not.
# If they are equal, the program prints "The original and reversed numbers are equal."
# If they are not equal, the program prints "The original and reversed numbers are not equal."