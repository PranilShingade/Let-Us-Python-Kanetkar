# g) Write a program to create following 3 lists: a list of names a list of roll numbers a list of marks Generate and print a list of tuples containing name, roll number and marks from the 3 lists. From this list generate 3 tuples—one containing all names, another containing all roll numbers and third containing all marks

names = ["Alice", "Bob", "Charlie"]
roll_numbers = [101, 102, 103]
marks = [85, 92, 78]

# Step 1: Create list of tuples
student_data = list(zip(names, roll_numbers, marks))
print("List of tuples:", student_data)

# Step 2: Generate three tuples
names_tuple = tuple(name for name, _, _ in student_data)
roll_numbers_tuple = tuple(roll for _, roll, _ in student_data)
marks_tuple = tuple(mark for _, _, mark in student_data)

print("Names tuple:", names_tuple)
print("Roll numbers tuple:", roll_numbers_tuple)
print("Marks tuple:", marks_tuple)

# Output:
# List of tuples: [('Alice', 101, 85), ('Bob', 102, 92), ('Charlie', 103, 78)]
# Names tuple: ('Alice', 'Bob', 'Charlie')
# Roll numbers tuple: (101, 102, 103)
# Marks tuple: (85, 92, 78)

# Explanation:
# Three lists containing names, roll numbers, and marks are created.
# The zip() function is used to combine corresponding elements into a list of tuples.
# From this list, three separate tuples are generated using tuple comprehension:
# one containing all names
# one containing all roll numbers
# one containing all marks