'''
i, j, k = 4, -1, 0 
w = i or j or k
x = i and j and k
y = i or j and k
z = i and j or k 
print(w, x, y, z)
'''

i, j, k = 4, -1, 0
w = i or j or k
x = i and j and k
y = i or j and k
z = i and j or k
print(w, x, y, z)

# Output:
# 4 0 4 0
# Explanation:
# w = i or j or k  => 4 (since 4 is truthy, it returns 4)
# x = i and j and k => 0 (since k is falsy, it returns 0)
# y = i or j and k => 4 (j and k is 0, so it returns i which is 4)
# z = i and j or k => 0 (i and j is -1, which is truthy, so it returns k which is 0)
# The 'or' operator returns the first truthy value or the last value if none are truthy.
# The 'and' operator returns the first falsy value or the last value if none are falsy.
# Thus, the final output is: 4 0 4 0