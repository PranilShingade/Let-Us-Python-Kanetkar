# Given co-ordinates of the center of a circle (h, k) and its radius r, write a program to check whether a given point (x, y) lies inside, on, or outside the circle.

h = float(input("Enter the x-coordinate of the center of the circle (h): "))
k = float(input("Enter the y-coordinate of the center of the circle (k): "))

r = float(input("Enter the radius of the circle (r): "))

x = float(input("Enter the x-coordinate of the point (x): "))
y = float(input("Enter the y-coordinate of the point (y): "))

distance = ((x - h) ** 2 + (y - k) ** 2) ** 0.5

if distance < r:
  print("The point is inside the circle.")
elif distance == r:
  print("The point is on the circle.")
else:
  print("The point is outside the circle.")

# Output:
# Enter the x-coordinate of the center of the circle (h): 0
# Enter the y-coordinate of the center of the circle (k): 0
# Enter the radius of the circle (r): 5
# Enter the x-coordinate of the point (x): 3
# Enter the y-coordinate of the point (y): 4
# The point is outside the circle 

# Explanation:
# The distance from the center (0, 0) to the point (3, 4) is 5, which is equal to the radius, hence the point lies on the circle.

# Enter the x-coordinate of the center of the circle (h): 1
# Enter the y-coordinate of the center of the circle (k): 1 
# Enter the radius of the circle (r): 5
# Enter the x-coordinate of the point (x): 6
# Enter the y-coordinate of the point (y): 6
# The point is outside the circle

# Explanation:
# The distance from the center (1, 1) to the point (6, 6) is 7, which is greater than the radius, hence the point lies outside the circle

# Enter the x-coordinate of the center of the circle (h): 2
# Enter the y-coordinate of the center of the circle (k): 2
# Enter the radius of the circle (r): 3
# Enter the x-coordinate of the point (x): 3
# Enter the y-coordinate of the point (y): 3
# The point is inside the circle

# Explanation:
# The distance from the center (2, 2) to the point (3, 3) is 1, which is less than the radius, hence the point lies inside the circle   