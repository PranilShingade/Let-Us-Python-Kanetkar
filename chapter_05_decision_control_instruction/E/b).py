# Any year is input through the keyboard. Write a program to determine whether the year is a leap year or not

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
  print("The year is a leap year.")
else:
  print("The year is not a leap year.")

# Output:
# Enter a year: 2020
# The year is a leap year
# Enter a year: 1900
# The year is not a leap year
# Enter a year: 2000
# The year is a leap year
# Enter a year: 2021
# The year is not a leap year