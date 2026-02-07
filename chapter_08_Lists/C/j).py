# A list contains 10 numbers. Write a program to eliminate all duplicates from the list

lst = [1, 2, 3, 4, 5, 5, 5, 5, 9, 10]
lst = list(set(lst))
print(lst)

# Output:
# [1, 2, 3, 4, 5, 9, 10]

# Explanation:
# The program defines a list lst containing 10 numbers.
# It then uses the set function to remove duplicates from the list.
# The resulting list without duplicates is printed.