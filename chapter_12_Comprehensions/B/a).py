# a) Write a program that generates a list of integer coordinates for all points in the first quadrant from (1, 1) to (5, 5). Use list comprehension

coordinates = [(x, y) for x in range(1, 6) for y in range(1, 6)]
print(coordinates)

# Output:
# [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5)]

# Explanation:
# The list comprehension iterates through all values of x from 1 to 5 and for each value of x, it iterates through all values of y from 1 to 5. It creates a tuple (x, y) for each combination of x and y, resulting in a list of coordinates for all points in the first quadrant from (1, 1) to (5, 5).
# The resulting list contains 25 tuples, each representing a coordinate in the first quadrant.
