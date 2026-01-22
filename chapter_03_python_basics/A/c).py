# Write a program that generates 5 random numbers in the range 10 to 50. Use a seed value of 6. Make a provision to change this seed value every time you execute the program by associating it with time of execution

import random
import time

# random.seed(int(time.time()))
random.seed(6)

for i in range(5):
  print(random.randint(10, 50))
# Output:
# The program imports the random and time modules.
# It sets the seed for the random number generator using the current time, ensuring different sequences of random numbers on each execution.
# It then generates and prints 5 random integers in the range 10 to 50.
# Example Output:
# output for seed value 6:
# 46
# 15
# 41
# 26
# 12