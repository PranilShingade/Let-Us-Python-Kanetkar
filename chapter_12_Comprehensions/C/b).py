# b) How will you convert the following code into a list comprehension? a = [ ] for n in range(10, 30) : if n % 2 == 0 : a.append(n) print(a)

a = [n for n in range(10, 30) if n % 2 == 0]
print(a)

# Output:
# [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]

# Explanation:
# The list comprehension iterates through each number 'n' in the range from 10 to 29 and includes only those that are even (i.e., divisible by 2). The resulting list 'a' contains all the even numbers within the specified range.