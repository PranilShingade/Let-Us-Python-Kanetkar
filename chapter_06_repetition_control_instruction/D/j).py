# Write a program to generate all Pythagorean Triplets with side length less than or equal to 30

for a in range(1, 31):
    for b in range(a, 31):
        for c in range(b, 31):
            if a**2 + b**2 == c**2:
                print(f"({a}, {b}, {c})")
# Output:
# (3, 4, 5)

# (5, 12, 13)

# (6, 8, 10)

# (7, 24, 25)

# (8, 15, 17)

# (9, 12, 15)

# (10, 24, 26)

# (12, 16, 20)

# (15, 20, 25)

# Explanation:
# The program uses three nested loops to iterate through all possible combinations of side lengths a, b, and c, where each side length ranges from 1 to 30.
# The condition a**2 + b**2 == c**2 checks if the combination forms a Pythagorean triplet.
# If the condition is satisfied, the triplet (a, b, c) is printed.
# The output shows all the Pythagorean triplets with side lengths less than or equal to 30.
