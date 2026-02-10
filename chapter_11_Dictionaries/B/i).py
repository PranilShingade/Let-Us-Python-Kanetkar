# i) Suppose a dictionary contains 5 key-value pairs of name and marks. Write a program to print them from last pair to first pair. Keep deleting every pair printed, such that the end of printing the dictionary falls empty.

marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 95,
    "Eve": 60
}

# Convert dictionary items to a list and reverse it
items = list(marks.items())[::-1]

# Print and delete each pair
for name, mark in items:
    print(f"{name}: {mark}")
    del marks[name]

print("Remaining dictionary:", marks)
# Output:
# Eve: 60
# David: 95
# Charlie: 78
# Bob: 92
# Alice: 85
# Remaining dictionary: {}

# Explanation:
# A dictionary containing names and marks is created.
# The dictionary items are converted into a list and reversed.
# Each key–value pair is printed from last to first.
# After printing, each pair is deleted from the dictionary.
# At the end, the dictionary becomes empty.
