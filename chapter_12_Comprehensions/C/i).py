# i) How will you convert 
# d = {'AMOL' : 20, 'ANIL' : 12, 'SUNIL' : 13, 'RAMESH' : 10} 
# into 
# {'Amol' : 400, 'Anil' : 144, 'Sunil' : 169, 'Ramesh' : 100} 

original_dict = {'AMOL': 20, 'ANIL': 12, 'SUNIL': 13, 'RAMESH': 10}
converted_dict = {key.capitalize(): value ** 2 for key, value in original_dict.items()}
print(converted_dict)

# Output:
# {'Amol': 400, 'Anil': 144, 'Sunil': 169, 'Ramesh': 100}

# Explanation:
# The dictionary comprehension iterates through each key-value pair in the original dictionary using the 'items()' method. For each key, it converts it to capitalized form using the 'capitalize()' method and squares the corresponding value. The resulting dictionary 'converted_dict' contains the transformed keys and values as specified.

