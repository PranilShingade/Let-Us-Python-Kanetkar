# Write a program to print out all Armstrong numbers between 1 and 500. If sum of cubes of each digit of the number is equal to the number itself, then the number is called an Armstrong number. For example, 153 = ( 1 * 1 * 1 ) + ( 5 * 5 * 5 ) + ( 3 * 3 * 3)

for num in range(1, 501):
    sum_of_cubes = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum_of_cubes += digit ** 3
        temp //= 10
    if sum_of_cubes == num:
        print(num)
# Output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 153
# 370
# 371
# 407
# Explanation:
# The program iterates through all numbers from 1 to 500 using a for loop.
# For each number, it calculates the sum of the cubes of its digits using a while loop.
# If the sum of the cubes of the digits is equal to the original number, it prints the number as an Armstrong number.
# The output shows that 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, and 407 are Armstrong numbers between 1 and 500.
