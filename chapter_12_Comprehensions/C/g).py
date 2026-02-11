# Using comprehension how will you convert  
# {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5} into 
# {'A' : 100, 'B' : 200, 'C' : 300, 'D' : 400, 'E' : 500}

original_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
converted_dict = {key.upper(): value * 100 for key, value in original_dict.items()}
print(converted_dict)

# Output:
# {'A': 100, 'B': 200, 'C': 300, 'D': 400, 'E': 500}

# Explanation:
# The dictionary comprehension iterates through each key-value pair in the original dictionary using the 'items()' method. For each key, it converts it to uppercase using the 'upper()' method and multiplies the corresponding value by 100. The resulting dictionary 'converted_dict' contains the transformed keys and values as specified.