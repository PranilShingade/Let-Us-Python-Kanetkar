# c) What will be the output of the following program? 
'''
def fun( ) : 
  print('First avatar') 
fun( ) 

def fun( ) : 
  print('New avatar') 
fun( )
'''

# Output:
# First avatar
# New avatar

# Explanation:
# In Python, when you define a function with the same name as an existing function, the new definition overwrites the previous one.
# In the given code, the first definition of fun() prints 'First avatar'. When fun() is called after the first definition, it executes and prints 'First avatar'. 
# Then,the second definition of fun() is encountered, which overwrites the first definition. The new definition of fun() prints 'New avatar'. When fun() is called again after the second definition, it executes and prints 'New avatar'. 
# Therefore, the output of the program will be: 
# First avatar
#  New avatar