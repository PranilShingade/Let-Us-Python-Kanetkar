# h) What will be the output of the following code snippet? 
# lst = [2, 7, 8, 6, 5, 5, 4, 4, 8] 
# s = {True if n % 2 == 0 else False for n in lst} 
# print(s)

lst = [2, 7, 8, 6, 5, 5, 4, 4, 8]
s = {True if n % 2 == 0 else False for n in lst}
print(s)

# Output:
# {False, True}

# Explanation:
# The program defines a list lst with the values 2, 7, 8, 6, 5, 5, 4, 4, 8.
# It then creates a set s using a list comprehension that checks if each value in the list is even or odd.
# The resulting set s contains True if the value is even and False if the value is odd.
# The output of the program is the set {False, True}, which contains both True and False values.
# Note that the set does not contain duplicate values, so even though there are multiple even and odd numbers in the list, only one instance of True and one instance of False is included in the set.
