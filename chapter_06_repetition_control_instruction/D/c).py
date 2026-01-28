# Write a program to count the number of alphabets and number of digits in the string 'Nagpur-440010

s = "Nagpur-440010"
alpha_count = 0
digit_count = 0

for char in s:
  if char.isalpha():
    alpha_count += 1
  elif char.isdigit():
    digit_count += 1

print("Number of alphabets:", alpha_count)
print("Number of digits:", digit_count)

# Output:
# Number of alphabets: 6
# Number of digits: 6

# Explanation:
# The program initializes two counters, alpha_count and digit_count, to zero.
# It then iterates through each character in the string s.
# If the character is an alphabet (checked using isalpha()), it increments the alpha_count.
# If the character is a digit (checked using isdigit()), it increments the digit_count.
# Finally, it prints the number of alphabets and digits in the string.
# The output shows that there are 6 alphabets and 6 digits in the string.

