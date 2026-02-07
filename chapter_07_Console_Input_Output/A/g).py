# How will you receive arbitrary number of floats from keyboard?

floats = []
while True:
  try:
    float_input = float(input("Enter a float: "))
    floats.append(float_input)
  except ValueError:
    break

print(floats)

# Output:
# [1.0, 2.0, 3.0, 4.0, 5.0]

# This code will keep asking for floats until the user enters a non-float value.