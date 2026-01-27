# Given the length and breadth of a rectangle, write a program to find whether the area of the rectangle is greater than its perimeter. For example, the area of the rectangle with length 5 and breadth 4 is 20, and its perimeter is 18. Therefore, the area is greater than the perimeter.

length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))

area = length * breadth
perimeter = 2 * (length + breadth)

if area > perimeter:
  print("The area of the rectangle is greater than its perimeter.")
else:
  print("The area of the rectangle is not greater than its perimeter.")

# Output:
# Enter the length of the rectangle: 5
# Enter the breadth of the rectangle: 4
# The area of the rectangle is greater than its perimeter.
# Enter the length of the rectangle: 3
# Enter the breadth of the rectangle: 4
# The area of the rectangle is not greater than its perimeter