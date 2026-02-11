# c) How will you convert the following code into a set comprehension? 
# a = set( ) 
# for n in range(21, 40) : 
#  if n % 2 == 0 : 
#    a.add(n) 
# print(a)

# The set comprehension equivalent is:
a = {n for n in range(21, 40) if n % 2 == 0}
print(a)

# Output:
# {22, 24, 26, 28, 30, 32, 34, 36, 38}

# Explanation:
# The set comprehension iterates through each number 'n' in the range from 21 to 39 and includes only those that are even (i.e., divisible by 2). The resulting set 'a' contains all the even numbers within the specified range.
