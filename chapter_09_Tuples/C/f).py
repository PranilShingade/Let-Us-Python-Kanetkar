# f) Write a program to remove empty tuple from a list of tuples

tuples_list = [(1, 2), (), (3, 4), (), (5, 6)]
filtered_list = [t for t in tuples_list if t]
print(filtered_list)

# Output:
# [(1, 2), (3, 4), (5, 6)]

# Explanation:
# The program defines a list of tuples tuples_list containing some empty tuples.
# It then uses list comprehension to filter out the empty tuples from the list.
# The resulting list without empty tuples is printed.