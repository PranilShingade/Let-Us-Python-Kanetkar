'''
a = 10 a = not not a print(a)
'''

a = 10
a = not not a
print(a)

# Output:
# True
# Explanation:
# The program defines a variable a with the value 10.
# It then uses the not operator to negate the value of a, resulting in a value of False.
# The not operator is used again to negate the value of False, resulting in a value of True.
# The final value of a is printed, which is True.
# The double negation (not not) converts any non-zero number to True and zero to False.
# In this case, the value of a is not zero, so the double negation converts it to True.
# Thus, the final output is: True