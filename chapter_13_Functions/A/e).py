# e) Write a program that defines a function sanitize_list( ) to remove all duplicate entries from the list that it receives

def sanitize_list(lst):
    return list(set(lst))

my_list = [1, 2, 3, 4, 5, 2, 3, 6]
sanitized_list = sanitize_list(my_list)
print(sanitized_list)

# Output:
# [1, 2, 3, 4, 5, 6]

# Explanation:
# The program defines a function sanitize_list that takes a list as input and returns a new list with all duplicate entries removed. The function converts the input list to a set, which automatically removes duplicates, and then converts it back to a list before returning it. The function is tested with a sample list that contains duplicate entries, and the output shows the sanitized list with duplicates removed.

# another-version

'''
# Best Version (Preserve Order)
def sanitize_list(lst):
    return list(dict.fromkeys(lst))

my_list = [1, 2, 3, 4, 5, 2, 3, 6]
sanitized_list = sanitize_list(my_list)
print(sanitized_list)
'''