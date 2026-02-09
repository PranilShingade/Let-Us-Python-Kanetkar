# d) Create a list of tuples. Each tuple should contain an item and its price in float. Write a program to sort the tuples in descending order by price. Hint: Use operator.itemgetter.


from operator import itemgetter

items = [("apple", 1.0), ("banana", 2.0), ("orange", 3.0), ("grape", 4.0)]
sorted_items = sorted(items, key=itemgetter(1), reverse=True)
print(sorted_items)

# Output:
# [('grape', 4.0), ('orange', 3.0), ('banana', 2.0), ('apple', 1.0)]

# Explanation:
# 1. We import the itemgetter function from the operator module to specify the sorting key
# 2. We create a list of tuples, where each tuple contains an item and its price.
# 3. We use the sorted function to sort the list of tuples based on the price (the second element of each tuple) in descending order by setting reverse=True.
# 4. Finally, we print the sorted list of tuples.