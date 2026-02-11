# e) Suppose a list contains positive and negative numbers. Write a program to create two lists—one containing positive numbers and another containing negative numbers.

lst = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
positive_list = [num for num in lst if num > 0]
negative_list = [num for num in lst if num < 0]
print("Positive List:", positive_list)
print("Negative List:", negative_list)

# Output:
# Positive List: [1, 3, 5, 7, 9]
# Negative List: [-2, -4, -6, -8, -10]

# Explanation:
# The list comprehension for the positive list iterates through each element 'num' in the original list 'lst' and includes only those that are greater than 0 (i.e., positive numbers). The list comprehension for the negative list iterates through the same original list and includes only those that are less than 0 (i.e., negative numbers). The resulting lists contain the positive and negative numbers from the original list, respectively.
