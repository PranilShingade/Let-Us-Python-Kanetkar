# Suppose a list contains positive and negative numbers. Write a program to create two lists—one containing positive numbers and another containing negative numbers

lst = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
positive_list = [num for num in lst if num > 0]
negative_list = [num for num in lst if num < 0]
print("Positive List:", positive_list)
print("Negative List:", negative_list)

# Output:
# Positive List: [1, 3, 5, 7, 9]
# Negative List: [-2, -4, -6, -8, -10]

# Explanation:
# The program defines a list lst containing 10 numbers.
# It then uses list comprehension to create two lists, positive_list and negative_list, containing only positive and negative numbers, respectively.
# The resulting lists are printed.