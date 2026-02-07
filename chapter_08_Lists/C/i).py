# Suppose a list contains several words. Write a program to create another list that contains first character of each word present in the first list

lst = ['apple', 'banana', 'cherry', 'date', 'elderberry']
new_list = [word[0] for word in lst]
print(new_list)

# Output:
# ['a', 'b', 'c', 'd', 'e']

# Explanation:
# The program defines a list lst containing several words.
# It then uses list comprehension to create a new list new_list that contains the first character of each word in the original list.
# The resulting list is printed.