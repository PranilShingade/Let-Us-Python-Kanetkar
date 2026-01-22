#What will be the output of the following program? 
# s = 'HumptyDumpty' 
# print('s = ', s) 
# print(s.isalpha( )) 
# print(s.isdigit( )) 
# print(s.isalnum( )) 
# print(s.islower( )) 
# print(s.isupper( )) 
# print(s.startswith('Hump')) 
# print(s.endswith('Dump'))

s = 'HumptyDumpty'
print('s = ', s)
print(s.isalpha())
print(s.isdigit())
print(s.isalnum())
print(s.islower())
print(s.isupper())
print(s.startswith('Hump'))
print(s.endswith('Dump'))

# Output:
# s =  HumptyDumpty
# True
# False
# True
# False
# False
# True
# False
# Explanation:
# The program defines a string s with the value 'HumptyDumpty'. 
# It then prints the value of s and the results of the isalpha(), isdigit(), isalnum(), islower(), isupper(), startswith(), and endswith() methods applied to s. 
# The isalpha() method returns True if all characters in s are alphabetic, False otherwise. 
# The isdigit() method returns True if all characters in s are digits, False otherwise. 
# The isalnum() method returns True if all characters in s are alphanumeric, False otherwise. 
# The islower() method returns True if all characters in s are lowercase, False otherwise. 
# The isupper() method returns True if all characters in s are uppercase, False otherwise. 
# The startswith() method returns True if s starts with the string 'Hump', False otherwise. 
# The endswith() method returns True if s ends with the string 'Dump', False otherwise.