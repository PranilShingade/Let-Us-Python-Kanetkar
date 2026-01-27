# Given the three points (x1, y1), (x2, y2) and (x3, y3), write a program to check whether they are collinear or not.

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
x3 = float(input("Enter x3: "))
y3 = float(input("Enter y3: "))

if (x2 - x1) * (y3 - y1) == (y2 - y1) * (x3 - x1):
  print("The points are collinear.")
else:
  print("The points are not collinear.")

# Output:
# Enter x1: 1
# Enter y1: 2
# Enter x2: 3
# Enter y2: 4
# Enter x3: 5
# Enter y3: 6
# The points are collinear

# Explanation:
# The points (1, 2), (3, 4), and (5, 6) lie on the same straight line, hence they are collinear.

