# Rewrite the following program using for loop

lst = ['desert', 'dessert', 'to', 'too', 'lose', 'loose']

s = 'Mumbai'
i = 0
while i < len(lst):
  if i>3:
    break
  else:
    print(i, lst[i],s[i])
    i += 1

for i in range(len(lst)):
    if i > 3:
        break
    else:
        print(i, lst[i], s[i])

# Output:
# 0 desert M
# 1 dessert M
# 2 to M
# 3 too M

# Explanation:
# The program defines a list lst containing the strings 'desert', 'dessert', 'to', 'too', 'lose', 'loose'.
# It then defines a string s with the value 'Mumbai'.
# It then uses a while loop to iterate over the elements of the list lst and print the index, element, and corresponding character of the string s.