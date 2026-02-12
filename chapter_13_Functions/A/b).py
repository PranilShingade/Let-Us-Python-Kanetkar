# b) Write a program that defines a function compute( ) that calculates the value of n + nn + nnn + nnnn, where n is digit received by the function. Test the function for digits 4 and 7

def compute(n):
    n_str = str(n)
    return n + int(n_str * 2) + int(n_str * 3) + int(n_str * 4)

print("For n=4:", compute(4))
print("For n=7:", compute(7))

# Output:
# For n=4: 4936
# For n=7: 8638

# Explanation:
# The program defines a function compute that takes a digit n as input and returns the value of n + nn + nnn + nnnn. The function compute takes a digit n as input and converts it to a string to create the repeated forms (nn, nnn, nnnn). It then converts these back to integers and sums them up to return the final result. The function is tested with the digits 4 and7, and the results are printed.

# another-version

'''
def compute(n):
    total = 0
    current = ""
    for i in range(4):
        current += str(n)
        total += int(current)
    return total

print(compute(4))
print(compute(7))
'''

'''
def compute(n):
    return sum(int(str(n) * i) for i in range(1, 5))
'''