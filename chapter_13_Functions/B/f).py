# f) How will you call print_it( ) to print elements of tpl? def print_it(a, b, c, d, e) : print(a, b, c, d, e) tpl = ('A', 'B', 'C', 'D', 'E')

# Output:
# You can call the print_it() function by unpacking the tuple tpl using the * operator. Here is how you can do it:
# print_it(*tpl)

# Explanation:
# tpl is a tuple containing five elements: 'A', 'B', 'C', 'D', and 'E'.
# To call the print_it() function with the tuple tpl as arguments, you can use the * operator to unpack the tuple and pass its elements as individual arguments to the function.
# When you call print_it(*tpl), it is equivalent to calling print_it('A', 'B', 'C', 'D', 'E'), which will print the elements of the tuple as expected.

# In summary, to call print_it( ) to print elements of tpl, you can use the * operator to unpack the tuple and pass its elements as individual arguments to the function.

# Example:
# tpl = ('A', 'B', 'C', 'D', 'E')
# print_it(*tpl)

# Output:
# A B C D E

