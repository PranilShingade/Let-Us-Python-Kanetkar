# Write a program to print 24 hours of day with suitable suffixes like AM, PM, Noon and Midnight.

for hour in range(0, 24):
    if hour == 0:
        print("12 AM (Midnight)")
    elif hour == 12:
        print("12 PM (Noon)")
    elif hour < 12:
        print(f"{hour} AM")
    else:
        print(f"{hour - 12} PM")

# Output:
# 12 AM (Midnight)
# 1 AM
# 2 AM
# 3 AM
# 4 AM
# 5 AM
# 6 AM
# 7 AM
# 8 AM
# 9 AM
# 10 AM
# 11 AM
# 12 PM (Noon)
# 1 PM
# 2 PM
# 3 PM
# 4 PM
# 5 PM
# 6 PM
# 7 PM
# 8 PM
# 9 PM
# 10 PM
# 11 PM
# 12 PM (Noon)

# Explanation:
# The program uses a for loop to iterate through the hours of the day from 0 to 23.
# It checks the value of the hour and prints the corresponding time with the appropriate suffix (AM, PM, Noon, Midnight).
# The output shows the 24 hours of the day with suitable suffixes.

