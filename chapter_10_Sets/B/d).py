# d) Write a program to create a set containing 10 randomly generated numbers in the range 15 to 45. Count how many of these numbers are less than 30. Delete all numbers which are greater than 35

import random

numbers = set()

# Generate exactly 10 unique random numbers
while len(numbers) < 10:
    numbers.add(random.randint(15, 45))

# Count numbers less than 30
count_less_30 = sum(1 for num in numbers if num < 30)

# Remove numbers greater than 35
numbers = {num for num in numbers if num <= 35}

print("Numbers:", numbers)
print("Numbers less than 30:", count_less_30)

# Output:
# Numbers: {16, 18, 22, 27, 29, 30, 31, 33, 34, 35}
# Numbers less than 30: 5

# Explanation:
# A set is created to store random numbers between 15 and 45.
# A while loop is used to ensure that exactly 10 unique numbers are added to the set.
# The number of elements less than 30 is counted.
# All numbers greater than 35 are removed from the set.
# Finally, the modified set and the count are displayed.
