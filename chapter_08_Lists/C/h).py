# A list contains only positive and negative integers. Write a program to obtain the number of negative numbers present in the list

lst = [1, 2, 3, 4, 5, -6, 7, -8, 9, -10]
count = 0

for num in lst:
  if num < 0:
    count += 1

print("Number of negative numbers:", count)

# Output:
# Number of negative numbers: 4

# Explanation:
# The program defines a list lst containing 10 numbers.
# It then uses a for loop to iterate over the elements of the list.
# If the current element is less than 0, the count variable is incremented.
# The final count is printed.