# Write a program to print the multiplication table of the number entered by the user. The table should get displayed in the following form: 29 * 1 = 29 29 * 2 = 58

num = int(input("Enter a number to print its multiplication table: "))

for i in range(1, 11):
  print(num, "*", i, "=", num * i)

# Output:
# Enter a number to print its multiplication table: 29
# 29 * 1 = 29
# 29 * 2 = 58
# 29 * 3 = 87
# 29 * 4 = 116
# 29 * 5 = 145
# 29 * 6 = 174
# 29 * 7 = 203
# 29 * 8 = 232
# 29 * 9 = 261
# 29 * 10 = 290