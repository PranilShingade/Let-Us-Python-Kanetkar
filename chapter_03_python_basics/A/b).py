#Write a program that makes use of trigonometric functions available in math module

import math

a = math.sin(90)
b = math.cos(180)
c = math.tan(45)

print("sin(90):", a)
print("cos(180):", b)
print("tan(45):", c)

# Output:
# The Core Issue: Python uses RADIANS, not degrees
# sin(90) → sin(90 radians)
# sin(90): 0.8939966636005579
# cos(180): -0.5984600690578581
# tan(45): 1.6197751905438615
# Explanation:
# The program imports the math module and uses its sin, cos, and tan functions to calculate the values of sin(90), cos(180), and tan(45).