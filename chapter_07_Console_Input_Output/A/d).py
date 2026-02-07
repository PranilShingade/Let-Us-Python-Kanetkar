# In the following statement what do > 5, > 7 and > 8 signify? print(f'{n:>5}{n ** 2:>7}{n ** 3:>8}')

n = 10
print(f'{n:>5}{n ** 2:>7}{n ** 3:>8}')

# Output:
#     10    100   1000

# > 5 means the number is right-aligned and padded with 5 spaces.
# > 7 means the number is right-aligned and padded with 7 spaces.
# > 8 means the number is right-aligned and padded with 8 spaces.