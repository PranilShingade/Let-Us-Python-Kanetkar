# What will be the output of the following code snippet? 
# s3 = 'C:\\Users\\Kanetkar\\Documents' print(s3.split('\\')) print(s3.partition('\\'))

s3 = 'C:\\Users\\Kanetkar\\Documents'
print(s3.split('\\'))
print(s3.partition('\\'))

# Output:
# ['C:', 'Users', 'Kanetkar', 'Documents']
# ('C:', '\\', 'Users\\Kanetkar\\Documents')
# Explanation:
# The program defines a string s3 containing a file path.
# It then splits the path into individual components using the split method with a backslash as the separator.
# The resulting list of components is printed.
# It then splits the path into three parts using the partition method with a backslash as the separator.
# The resulting tuple of parts is printed.
# The output will be a list containing the individual components of the file path, and a tuple containing the three parts of the path.  