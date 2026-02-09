# c) Suppose a date is represented as a tuple (d, m, y). Write a program to create two date tuples and find the number of days between the two dates.

from datetime import datetime

date1 = (2023, 1, 1)
date2 = (2023, 2, 1)

date1_obj = datetime(*date1)
date2_obj = datetime(*date2)

days = (date2_obj - date1_obj).days

print("Number of days between the two dates:", days)

# Output:
# Number of days between the two dates: 31

# Explanation:
# 1. We import the datetime module to work with date objects.
# 2. We define two date tuples date1 and date2.
# 3. We use the datetime module to create datetime objects from the date tuples.
# 4. We calculate the number of days between the two dates using the difference between the datetime objects.
# 5. Finally, we print the number of days between the two dates.