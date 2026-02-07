# How will you print the output of the following code segment using fstring? x, y, z =10, 20, 40 print('{0:<5}{1:<7}{2:<8}'.format(x, y, z))

x, y, z = 10, 20, 40
print(f'{0:<5}{1:<7}{2:<8}'.format(x, y, z))

# Output:
# 10    20     40