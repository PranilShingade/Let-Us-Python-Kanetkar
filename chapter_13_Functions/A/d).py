# d) Write a program that defines a function create_list( ) to create and return a list which is an intersection of two lists passed to it

def create_list(list1, list2):
    return list(set(list1) & set(list2))

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

intersection = create_list(list1, list2)
print(intersection)

# Output:
# [4, 5]

# Explanation:
# The program defines a function create_list that takes two lists as input and returns a list containing the intersection of the two lists. The function converts both lists to sets and uses the set intersection operator (&) to find the common elements. The result is then converted back to a list and returned. The function is tested with two sample lists, and the output shows the common elements between the two lists.

# another-version

'''
# Best Optimized Version (Preserve Order + Fast)
def create_list(list1, list2):
    set2 = set(list2)
    return [x for x in list1 if x in set2]

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

intersection = create_list(list1, list2)
print(intersection)
'''