# b) Using list comprehension, write a program to create a list by multiplying each element in the list by 10.

numbers = [1, 2, 3, 4, 5]
multiplied_numbers = [num * 10 for num in numbers]
print(multiplied_numbers)

# Output:
# [10, 20, 30, 40, 50]

# Explanation:
# The list comprehension iterates through each element 'num' in the 'numbers' list and multiplies it by 10. The resulting list 'multiplied_numbers' contains the products of each element in the original list multiplied by 10.
