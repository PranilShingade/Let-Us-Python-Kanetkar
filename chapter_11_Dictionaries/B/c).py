# c) Given the following dictionary: portfolio = { 'accounts' : ['SBI', 'IOB'], 'shares' : ' [HDFC, 'ICICI', 'TM', 'TCS'], 'ornaments' : ['10 gm gold', '1 kg silver'] } 
# write a program to perform the following operations: 
# Add a key to portfolio called 'MF' with values 'Relaince' and 'ABSL'. 
# Set the value of 'accounts' to a list containing 'Axis' and 'BOB'. 
# Sort the items in the list stored under the 'shares' key. 
# Delete the list stored under 'ornaments' key

portfolio = {
    'accounts': ['SBI', 'IOB'],
    'shares': ['HDFC', 'ICICI', 'TM', 'TCS'],
    'ornaments': ['10 gm gold', '1 kg silver']
}

portfolio['MF'] = ['Relaince', 'ABSL']
portfolio['accounts'] = ['Axis', 'BOB']
portfolio['shares'].sort()
del portfolio['ornaments']

print(portfolio)

# Output:
# {'accounts': ['Axis', 'BOB'], 'shares': ['HDFC', 'ICICI', 'TCS', 'TM'], 'MF': ['Relaince', 'ABSL']}

# Explanation:
# A dictionary named 'portfolio' is created with specified keys and values.
# The 'MF' key is added with two values 'Relaince' and 'ABSL'.
# The 'accounts' key is updated with a list containing 'Axis' and 'BOB'.
# The 'shares' key is sorted in alphabetical order.
# The 'ornaments' key is deleted from the dictionary.
# The updated dictionary is printed.
