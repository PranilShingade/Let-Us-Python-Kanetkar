# b) Create an empty set. Write a program that adds five new names to this set, modifies one existing name and deletes two names existing in it.

empty_set = set()

# Add five names
empty_set.add("Alice")
empty_set.add("Bob")
empty_set.add("Charlie")
empty_set.add("David")
empty_set.add("Eve")

# Modify one existing name (Alice → Alex)
empty_set.remove("Alice")
empty_set.add("Alex")

# Delete two names
empty_set.remove("Charlie")
empty_set.remove("Eve")

print(empty_set)

# Output:
# {'Bob', 'David', 'Alex'}

# Explanation:
# An empty set is created using set().
# Five names are added using the add() method.
# One existing name is modified by removing the old name and adding a new name.
# Two names are deleted using the remove() method.
# The final set is printed.