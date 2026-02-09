# a) A set contains names which begin either with A or with B. write a program to separate out the names into two sets, one containing names beginning with A and another containing names beginning with B.

names = {"Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Henry"}

set_a = {name for name in names if name.startswith("A")}
set_b = {name for name in names if name.startswith("B")}

print("Set A:", set_a)
print("Set B:", set_b)

# Output:
# Set A: {'Alice'}
# Set B: {'Bob'}

# Explanation:
'''A set of names is defined.

Set comprehension is used to create:

one set containing names starting with 'A'

another set containing names starting with 'B'

The startswith() method is used to check the first letter of each name.'''