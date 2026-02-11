# d) Write a program to generate two lists using list comprehension. One list should contain first 20 odd numbers and another should contain first 20 even numbers.

odd_numbers = [num for num in range(1, 40) if num % 2 != 0][:20]
even_numbers = [num for num in range(0, 40) if num % 2 == 0][:20]

print("Odd Numbers:", odd_numbers)
print("Even Numbers:", even_numbers)

'''
odd_numbers = [num for num in range(1, 40, 2)]
even_numbers = [num for num in range(0, 40, 2)]

print("Odd Numbers:", odd_numbers)
print("Even Numbers:", even_numbers)
'''
'''
odd_numbers = [2*n + 1 for n in range(20)]
even_numbers = [2*n for n in range(20)]

print("Odd Numbers:", odd_numbers)
print("Even Numbers:", even_numbers)
'''
# Output:
# Odd Numbers: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]
# Even Numbers: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38]

# Explanation:
# The list comprehension for odd numbers iterates through the range of numbers from 1 to 39 and includes only those that are not divisible by 2 (i.e., odd numbers). The list comprehension for even numbers iterates through the range of numbers from 0 to 38 and includes only those that are divisible by 2 (i.e., even numbers). Both lists are sliced to include only the first 20 elements.