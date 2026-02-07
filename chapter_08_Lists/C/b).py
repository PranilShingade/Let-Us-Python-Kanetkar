# Suppose a list contains 20 integers generated randomly. Receive a number from the keyboard and report position of all occurrences of this number in the list

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
num = int(input("Enter a number: "))

for i in range(len(lst)):
  if lst[i] == num:
    print("The number", num, "is present at index", i)

# Output:
# Enter a number: 10
# The number 10 is present at index 9

# Explanation:
# The program prompts the user to enter a number.
# It then uses a for loop to iterate over the elements of the list lst.
# If the current element is equal to the entered number, the program prints the index of the element.