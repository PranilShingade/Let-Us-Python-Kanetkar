# If the three sides of a triangle are entered through the keyboard, write a program to check whether the triangle is valid or not. The triangle is valid if the sum of two sides is greater than the largest of the three sides.

side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

largest_side = max(side1, side2, side3)

if side1 + side2 > largest_side and side1 + side3 > largest_side and side2 + side3 > largest_side:
  print("The triangle is valid.")
else:
  print("The triangle is not valid.")

# Output:
# Enter the length of the first side: 3
# Enter the length of the second side: 4
# Enter the length of the third side: 5
# The triangle is valid

# Enter the length of the first side: 1
# Enter the length of the second side: 2
# Enter the length of the third side: 3
# The triangle is not valid

