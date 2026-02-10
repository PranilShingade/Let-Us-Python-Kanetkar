# e) Which functions will you use to fetch all keys, all values and key value pairs from a given dictionary?

# To fetch all keys from a given dictionary, you can use the `keys()` function.
# To fetch all values from a given dictionary, you can use the `values()` function.
# To fetch all key-value pairs from a given dictionary, you can use the `items()` function.

# Example:
my_dict = {"a": 1, "b": 2, "c": 3}
print(my_dict.keys())  # Output: dict_keys(['a', 'b', 'c'])
print(my_dict.values())  # Output: dict_values([1, 2, 3])
print(my_dict.items())  # Output: dict_items([('a', 1), ('b', 2), ('c', 3)])

# Explanation:
# The `keys()` function returns a view object that displays a list of all the keys in the dictionary.
# The `values()` function returns a view object that displays a list of all the values in the dictionary.
# The `items()` function returns a view object that displays a list of all the key-value pairs in the dictionary as tuples.

# In summary, to fetch all keys, all values, and key-value pairs from a given dictionary, you can use the `keys()`, `values()`, and `items()` functions, respectively.
