# f) Which of the following the correct form of dictionary comprehension? 
# i. dict_var = {key : value for (key, value) in dictonary.items( )} 
# ii. dict_var = {key : value for (key, value) in dictonary} 
# iii. dict_var = {key : value for (key, value) in dictonary.keys()}

# The correct form of dictionary comprehension is:
dict_var = {key: value for (key, value) in dictionary.items()}

# Explanation:
# In a dictionary comprehension, you need to iterate over the key-value pairs of the original dictionary. The 'items()' method returns a view object that displays a list of a dictionary's key-value tuple pairs, which is necessary for the comprehension to work correctly. The other two options do not provide the necessary key-value pairs for the comprehension to function as intended.

# In summary, the correct form of dictionary comprehension is:
# dict_var = {key: value for (key, value) in dictionary.items()}