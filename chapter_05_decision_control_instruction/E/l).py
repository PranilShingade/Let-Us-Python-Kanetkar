# If the three sides of a triangle are entered through the keyboard, write a program to check whether the triangle is isosceles, equilateral,scalene or right angled triangle

side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

if side1 == side2 == side3:
  print("The triangle is equilateral.")
elif side1 == side2 or side1 == side3 or side2 == side3:
  print("The triangle is isosceles.")
elif side1**2 + side2**2 == side3**2 or side1**2 + side3**2 == side2**2 or side2**2 + side3**2 == side1**2:
  print("The triangle is right-angled.")
else:
  print("The triangle is scalene.")

# Output:
# Enter the length of the first side: 5
# Enter the length of the second side: 5
# Enter the length of the third side: 5
# The triangle is equilateral

# Enter the length of the first side: 3
# Enter the length of the second side: 4
# Enter the length of the third side: 5
# The triangle is isosceles

# Enter the length of the first side: 3
# Enter the length of the second side: 4
# Enter the length of the third side: 5
# The triangle is scalene

# Enter the length of the first side: 3
# Enter the length of the second side: 4
# Enter the length of the third side: 5
# The triangle is right-angled