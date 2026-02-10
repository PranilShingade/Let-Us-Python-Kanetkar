# b) Create a dictionary containing names of students and marks obtained by them in three subjects. Write a program to replace the marks in three subjects with the total in three subjects, and average marks. Also report the topper of the class.

marks = {
  "Alice": [80, 85, 90],
  "Bob": [75, 70, 80],
  "Charlie": [90, 95, 85]
}

for name, scores in marks.items():
    total = sum(scores)
    average = total / len(scores)
    marks[name] = (total, average)

topper = max(marks, key=lambda name: marks[name][1])

print(f"{topper} is the topper with {marks[topper][1]} average marks.")

# Output:
# Charlie is the topper with 90.0 marks.

# Explanation:
# A dictionary containing students and marks in three subjects is created.
# For each student, the total and average marks are calculated.
# The original marks are replaced with total and average marks.
# The topper is determined by finding the student with the highest average marks.
# Finally, the name of the topper and their average marks are displayed.