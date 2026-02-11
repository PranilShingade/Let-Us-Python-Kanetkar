# (j) How will you convert words present in a list given below into uppercase and store them in a set? 
# lst = ['Amol', 'Vijay', 'Vinay', 'Rahul', 'Sandeep']

lst = ['Amol', 'Vijay', 'Vinay', 'Rahul', 'Sandeep']
upper_case_set = {word.upper() for word in lst}

print(upper_case_set)

# Output:
# {'AMOL', 'VIJAY', 'VINAY', 'RAHUL', 'SANDEEP'}

# Explanation:
# The set comprehension iterates through each word in the original list 'lst' and applies the 'upper()' method to convert it to uppercase. The resulting set 'upper_case_set' contains all the uppercase versions of the words from the original list.

