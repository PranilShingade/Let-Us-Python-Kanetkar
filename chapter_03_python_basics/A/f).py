# Given three sides a, b, c of a triangle, write a program to obtain and print the values of three angles rounded to the next integer. Use the formulae: 
# a^2 = b^2 + c^2 2bc*cosA, 
# b^2 = a^2 + c^2 2ac*cosB, 
# c^2 = a^2 + b^2 2ab*cos C

import math

a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

angle_a = math.degrees(math.acos((b * b + c * c - a * a) / (2 * b * c)))
angle_b = math.degrees(math.acos((a * a + c * c - b * b) / (2 * a * c)))
angle_c = math.degrees(math.acos((a * a + b * b - c * c) / (2 * a * b)))

print("Angle A:", round(angle_a))
print("Angle B:", round(angle_b))
print("Angle C:", round(angle_c))

# Explanation:
# The program first imports the math module to access mathematical functions.
# It then prompts the user to input the lengths of the three sides of the triangle.
# Using the cosine rule, it calculates each angle in radians and converts it to degrees.
# Finally, it rounds each angle to the nearest integer and prints the results.
# Example Output:
# Enter the length of side a: 3
# Enter the length of side b: 4
# Enter the length of side c: 5

# Angle A: 37
# Angle B: 53
# Angle C: 90