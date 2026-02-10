# g) Given the following dictionary 
'''marks = { 
'Subu' : {'Maths' : 88, 'Eng' : 60, 'SSt' : 95}, 'Amol' : {'Maths' : 78, 'Eng' : 68, 'SSt' : 89}, 'Raka' : {'Maths' : 56, 'Eng' : 66, 'SSt' : 77} 
}''' 

#Write a program to perform the following operations: 
# Print marks obtained by Amol in English. 
# Set marks obtained by Raka in Maths to 77. 
# Sort the dictionary by name

marks = {
    'Subu': {'Maths': 88, 'Eng': 60, 'SSt': 95},
    'Amol': {'Maths': 78, 'Eng': 68, 'SSt': 89},
    'Raka': {'Maths': 56, 'Eng': 66, 'SSt': 77}
}

print(f"Marks obtained by Amol in English: {marks['Amol']['Eng']}")

marks['Raka']['Maths'] = 77

names = list(marks.keys())
names.sort()
sorted_marks = {name: marks[name] for name in names}

print("Sorted dictionary by name:")
for name, data in sorted_marks.items():
    print(f"{name}: {data}")

# Output:
# Marks obtained by Amol in English: 68
# Sorted dictionary by name:
# Amol: {'Maths': 78, 'Eng': 68, 'SSt': 89}
# Raka: {'Maths': 77, 'Eng': 66, 'SSt': 77}
# Subu: {'Maths': 88, 'Eng': 60, 'SSt': 95}

# Explanation:
# A dictionary containing student marks is created.
# The marks obtained by Amol in English is printed.
# The marks obtained by Raka in Maths is set to 77.
# The dictionary is sorted by name.
# The sorted dictionary is printed.