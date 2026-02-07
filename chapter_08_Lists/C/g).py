# Write a program to obtain a median value of a list of numbers, without disturbing the order of the numbers in the list

nums = [7, 1, 3, 9, 5]

# Step 1: Create a sorted copy (original list untouched)
sorted_nums = sorted(nums)

# Step 2: Find median
n = len(sorted_nums)
mid = n // 2

if n % 2 != 0:
    median = sorted_nums[mid]
else:
    median = (sorted_nums[mid - 1] + sorted_nums[mid]) / 2

print("Original list:", nums)
print("Median:", median)

# Output:
# Original list: [7, 1, 3, 9, 5]
# Median: 5.0

# Explanation:
# The program defines a list nums containing 5 numbers.
# It then uses the sorted function to create a sorted copy of the list nums.
# The sorted copy is then used to find the median of the list.
# The median is printed.

'''
When the number of elements is EVEN

Example:

[10, 2, 8, 4]

Arrange:

[2, 4, 8, 10]

Total elements = 4 (even)

Two middle values = 4 and 8

Median = average of middle two

Median = (4 + 8) / 2 = 6

Formula:

median = (element at n//2 − 1 + element at n//2) / 2
'''