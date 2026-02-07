nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Mean
mean = sum(nums) / len(nums)

# Median
sorted_nums = sorted(nums)
n = len(sorted_nums)

if n % 2 == 0:
    median = (sorted_nums[n//2 - 1] + sorted_nums[n//2]) / 2
else:
    median = sorted_nums[n//2]

# Mode
mode = None
for num in nums:
    if nums.count(num) > 1:
        mode = num
        break

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)

# Output:
# Mean: 5.5
# Median: 5.5
# Mode: None

# Explanation:
# The program defines a list nums containing 10 numbers.
# It then calculates the mean, median, and mode of the list.
# The mean is calculated by adding all the numbers in the list and dividing by the number of elements in the list.
# The median is calculated by sorting the list and then finding the middle element if the number of elements is odd, or the average of the middle two elements if the number of elements is even.
# The mode is calculated by finding the number that appears most frequently in the list.
# The resulting mean, median, and mode are printed.

'''
Mean is calculated as the sum of all elements divided by the number of elements.
Median is the middle value of the sorted list; since the list has even elements, it is the average of the two middle values.
Mode is the value that occurs most frequently; since all values occur once, there is no mode.
'''