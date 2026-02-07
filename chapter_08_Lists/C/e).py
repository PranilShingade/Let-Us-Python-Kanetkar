# Suppose a list contains 5 strings. Write a program to convert all these strings to uppercase

lst = ['a', 'b', 'c', 'd', 'e']
lst = [x.upper() for x in lst]
print(lst)

# Output:
# ['A', 'B', 'C', 'D', 'E']

# Explanation:
# The program defines a list lst containing 5 strings.
# It then uses list comprehension to convert all the strings in the list to uppercase.
# The resulting list is printed.