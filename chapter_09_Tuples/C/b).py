"""b) What will be the output of the following code snippet? 
num1 = num2 = (10, 20, 30, 40, 50) 
print(id(num1), type(num2)) 
print(isinstance(num1, tuple)) 
print(num1 is num2) 
print(num1 is not num2) 
print(20 in num1) 
print(30 not in num2)"""

num1 = num2 = (10, 20, 30, 40, 50)
print(id(num1), type(num2))
print(isinstance(num1, tuple))
print(num1 is num2)
print(num1 is not num2)
print(20 in num1)
print(30 not in num2)

# Output:
# <some_id> <class 'tuple'>
# True
# True
# False
# True
# False

# Explanation:
# 1. The first print statement will output the memory address (id) of num1 and the type of num2, which is a tuple.
# 2. The second print statement checks if num1 is an instance of the tuple class, which returns True.
# 3. The third print statement checks if num1 and num2 refer to the same object in memory, which returns True since both variables point to the same tuple.
# 4. The fourth print statement checks if num1 and num2 do not refer to the same object, which returns False.
# 5. The fifth print statement checks if the value 20 is in num1, which returns True.
# 6. The sixth print statement checks if the value 30 is not in num2, which returns False since 30 is indeed in num2.

