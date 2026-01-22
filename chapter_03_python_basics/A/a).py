#Write a program that swaps the values of variables a and b. You are not allowed to use a third variable. You are not allowed to perform arithmetic on a and b.

a = 5
b = 10
a, b = b, a
print("a:", a)
print("b:", b)
# Output:
# a: 10
# b: 5
# Explanation:
# The program uses tuple unpacking to swap the values of a and b without using a third variable.
# It then prints the updated values of a and b.