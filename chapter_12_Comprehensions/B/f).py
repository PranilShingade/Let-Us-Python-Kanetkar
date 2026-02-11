# f) Suppose a list contains 5 strings. Write a program to convert all these strings to uppercase.

lst = ['apple', 'banana', 'cherry', 'date', 'elderberry']
upper_case = [string.upper() for string in lst]
print(upper_case)

# Output:
# ['APPLE', 'BANANA', 'CHERRY', 'DATE', 'ELDERBERRY']

# Explanation:
# The list comprehension iterates through each string in the original list 'lst' and applies the 'upper()' method to convert it to uppercase. The resulting list 'upper_case' contains all the strings from the original list converted to uppercase.
