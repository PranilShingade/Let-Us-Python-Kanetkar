# i) Write a program that converts words present in a list into uppercase and stores them in a set.

words = ['hello', 'world', 'python', 'programming']
upper_case_set = {word.upper() for word in words}

print(upper_case_set)

# Output:
# {'HELLO', 'WORLD', 'PYTHON', 'PROGRAMMING'}
# (Order may vary because sets are unordered.)

# Explanation:
# The set comprehension iterates through each word in the original list 'words' and applies the 'upper()' method to convert it to uppercase. The resulting set 'upper_case_set' contains all the uppercase versions of the words from the original list.
