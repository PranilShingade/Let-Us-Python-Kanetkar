# Given a point (x,y) write a program to find out if it lies on the x-axis, y-axis or origin.

x = float(input("Enter the x-coordinate of the point (x): "))
y = float(input("Enter the y-coordinate of the point (y): "))

if x == 0 and y == 0:
  print("The point is at the origin.")
elif x == 0:
  print("The point is on the x-axis.")
elif y == 0:
  print("The point is on the y-axis.")
else:
  print("The point is neither on the x-axis nor the y-axis.")

# Output:
# Enter the x-coordinate of the point (x): 0
# Enter the y-coordinate of the point (y): 0
# The point is at the origin.

# Enter the x-coordinate of the point (x): 0
# Enter the y-coordinate of the point (y): 5
# The point is on the y-axis.
# Enter the x-coordinate of the point (x): 4
# Enter the y-coordinate of the point (y): 0
# The point is on the x-axis.
# Enter the x-coordinate of the point (x): 3
# Enter the y-coordinate of the point (y): 4
# The point is neither on the x-axis nor the y-axis