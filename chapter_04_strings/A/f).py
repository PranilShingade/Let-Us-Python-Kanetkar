# If we wish to work with an individual word in the following string, how will you separate them out: 'The difference between stupidity and genius is that genius has its limits'?

s = "The difference between stupidity and genius is that genius has its limits"
print(s.split(" "))

# Output:
# ['The', 'difference', 'between', 'stupidity', 'and', 'genius', 'is', 'that', 'genius', 'has', 'its', 'limits']
# Explanation:
# The program defines a string s containing a sentence.
# It then splits the sentence into individual words using the split method with a space as the separator.
# The resulting list of words is printed.