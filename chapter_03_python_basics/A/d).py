# Use trunc( ), floor( ) and ceil( ) for numbers 2.8, 0.5, 0.2, 1.5 and 2.9 to understand the difference between these functions clearly

import math
numbers = [2.8, 0.5, 0.2, 1.5, 2.9]

for number in numbers:
  print("trunc({}): {}".format(number, math.trunc(number)))
  print("floor({}): {}".format(number, math.floor(number)))
  print("ceil({}): {}".format(number, math.ceil(number)))
  print()
# Output:
# trunc(2.8): 2
# floor(2.8): 2
# ceil(2.8): 3
# trunc(0.5): 0
# floor(0.5): 0
# ceil(0.5): 1
# trunc(0.2): 0
# floor(0.2): 0
# ceil(0.2): 1
# trunc(1.5): 1
# floor(1.5): 1
# ceil(1.5): 2
# trunc(2.9): 2
# floor(2.9): 2
# ceil(2.9): 3
# Explanation:
# The program imports the math module and uses its trunc, floor, and ceil functions to calculate the truncation, floor, and ceiling of the given numbers.
# It then prints the results for each number.
# The trunc function removes the decimal part and returns the integer part of the number.
# The floor function returns the largest integer less than or equal to the number.
# The ceil function returns the smallest integer greater than or equal to the number.