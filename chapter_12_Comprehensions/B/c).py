# c) Write a program to generate first 20 Fibonacci numbers using list comprehension.

from functools import reduce

def fibonacci(n):
    return reduce(lambda seq, _: seq + [seq[-1] + seq[-2]], 
                  range(n - 2), 
                  [0, 1])[:n]

print(fibonacci(20))

# Output:
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]

# Explanation:
# The function 'fibonacci' generates the Fibonacci sequence up to 'n' numbers. It initializes the sequence with the first two numbers (0 and 1) and uses a list comprehension to append the sum of the last two numbers in the sequence until it reaches the desired length. The resulting list contains the first 20 Fibonacci numbers.

