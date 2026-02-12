# c) Write a program that defines a function create_array( ) to create and return a 3D array whose dimensions are passed to the function. Also initialize each element of this array to a value passed to the function

def create_array(dim1, dim2, dim3, value):
  return [[[value for _ in range(dim3)] for _ in range(dim2)] for _ in range(dim1)]

array = create_array(2, 3, 4, 5)
print(array)

# Output:
# [[[5, 5, 5, 5], [5, 5, 5, 5], [5, 5, 5, 5]], [[5, 5, 5, 5], [5, 5, 5, 5], [5, 5, 5, 5]]]

# Explanation:
# The program defines a function create_array that takes four parameters: dim1, dim2, dim3, and value. The function uses list comprehensions to create a 3D array with the specified dimensions and initializes each element to the given value. The function is then called with dimensions 2, 3, and 4, and a value of 5, resulting in a 3D array filled with the value 5. The output shows the created 3D array.

# another-version

'''
def create_array(dim1, dim2, dim3, value):
    return [[[value for _ in range(dim3)] for _ in range(dim2)] for _ in range(dim1)]

array = create_array(2, 3, 4, 5)
print(array)
'''

'''
def create_array(dim1, dim2, dim3, value):
    return [[[value] * dim3 for _ in range(dim2)] for _ in range(dim1)]

array = create_array(2, 3, 4, 5)
print(array)
'''