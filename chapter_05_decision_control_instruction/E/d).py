# Write a program to check whether a triangle is valid or not, when the three angles of the triangle are entered through the keyboard A triangle is valid if the sum of all the three angles is equal to 180 degrees.

angle1 = float(input("Enter the first angle: "))
angle2 = float(input("Enter the second angle: "))
angle3 = float(input("Enter the third angle: "))

if angle1 + angle2 + angle3 == 180:
  print("The triangle is valid.")
else:
  print("The triangle is not valid.")

# Output:
# Enter the first angle: 60
# Enter the second angle: 60
# Enter the third angle: 60
# The triangle is valid

# Enter the first angle: 90
# Enter the second angle: 45
# Enter the third angle: 45
# The triangle is valid