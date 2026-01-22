'''
x, y, z = 20, 40, 45
if x > y and x > z :
    print('biggest = ' + str(x))
elif y > x and y > z :
    print('biggest = ' + str(y))
elif z > x and z > y :
    print('biggest = ' + str(z))
'''

x, y, z = 20, 40, 45
if x > y and x > z :
    print('biggest = ' + str(x))  
elif y > x and y > z :
    print('biggest = ' + str(y))
elif z > x and z > y :
    print('biggest = ' + str(z))

# Output:
# biggest = 45
# Explanation:
# The program defines three variables x, y, and z with the values 20, 40, and 45 respectively.
# It then uses a series of if, elif statements to compare the values of these variables to  determine which one is the largest.
# The first condition checks if x is greater than both y and z. If this condition is true, it prints the value of x as the biggest.
# If the first condition is false, it moves to the second condition which checks if y is greater than both x and z. If this condition is true, it prints the value of y as the biggest.
# If both the first and second conditions are false, it moves to the third condition which checks if z is greater than both x and y. If this condition is true, it prints the value of z as the biggest.
# In this case, the value of z (45) is greater than both x (20) and y (40), so the program prints "biggest = 45". 
# Thus, the final output is: biggest = 45 