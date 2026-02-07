# Suppose a list has 20 numbers. Write a program that removes all duplicates from this list

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20]
lst = list(set(lst))
print(lst)

# Output:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Explanation:
# The program defines a list lst containing 20 numbers.
# It then uses the set function to remove duplicates from the list.
# The resulting list without duplicates is printed.