# Write a program to receive an arbitrary number of floats using one input( ) statement. Calculate the average of floats received.

floats = list(map(float, input("Enter floats: ").split()))
average = sum(floats) / len(floats)
print(average)

# Output:
# 1.0 2.0 3.0 4.0 5.0
# 3.0

# This code will ask the user to enter floats and then calculate the average of the floats.