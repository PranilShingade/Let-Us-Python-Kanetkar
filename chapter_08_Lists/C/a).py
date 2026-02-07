# Write a program to create a list of 5 odd integers. Replace the third element with a list of 4 even integers. Flatten,sort and print the list

lst = [1, 3, [2, 4, 6, 8], 7, 9]
lst = sorted(x for item in lst for x in (item if isinstance(item, list) else [item]))
print(lst)

# Output:
# [1, 3, 2, 4, 6, 8, 7, 9]

'''lst = [1, 3, 5, 7, 9]

# Replace 3rd element with a list of even integers
lst[2] = [2, 4, 6, 8]

# Flatten the list
flat_list = []
for item in lst:
    if isinstance(item, list):
        flat_list.extend(item)
    else:
        flat_list.append(item)

# Sort and print
flat_list.sort()
print(flat_list)'''