# (e) From the sentence sent = 'Pack my box with five dozen liquor jugs' how will you generate a set given below? {'liquor', 'jugs', 'with', 'five', 'dozen', 'Pack'}

sent = 'Pack my box with five dozen liquor jugs'

result = {word for word in sent.split() 
          if word not in ['my', 'box']}

print(result)

# Output:
# {'Pack', 'with', 'five', 'dozen', 'liquor', 'jugs'}

# Explanation:
# The program defines a string sent containing a sentence.
# It then splits the sentence into individual words using the split method with a space as the separator.
# The resulting list of words is printed.
# It then uses a set comprehension to create a set result containing all the words from the original list that are not 'my' or 'box'.
# The resulting set is printed.

