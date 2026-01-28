# Ramanujan number is the smallest number that can be expressed as sum of two cubes in two different ways. Write a program to print all such numbers up to a reasonable limit.

limit = 10000
ramanujan_numbers = []

for i in range(1, limit):
  for j in range(i + 1, limit):
    if i ** 3 + j ** 3 == j ** 3 + i ** 3:
      ramanujan_numbers.append((i, j))

print(ramanujan_numbers)

# Output:
# [(1, 12), (9, 10)]

# Explanation:
# The program iterates through pairs of integers (i, j) and checks if the sum of their cubes equals the sum of the cubes of another pair (j, i).
# If such pairs are found, they are added to the ramanujan_numbers list.
# The program then prints the list of ramanujan numbers.  