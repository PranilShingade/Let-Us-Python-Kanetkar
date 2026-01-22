'''
num = 30 k = 100 if num <= 10 else 500 print(k)
'''

num = 30
k = 100 if num <= 10 else 500
print(k)

# Output:
# 500 
# Explanation:
# The program defines a variable num with the value 30.
# It then uses a conditional expression (also known as a ternary operator) to assign a value to the variable k based on the value of num.
# The conditional expression checks if num is less than or equal to 10. If this condition is true, it assigns the value 100 to k. If the condition is false, it assigns the value 500 to k.
# In this case, since num is 30, which is greater than 10, the condition is false, and therefore k is assigned the value 500.
# Finally, the value of k is printed, which is 500.
# Thus, the final output is: 500