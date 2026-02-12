# f) Which of the calls to print_it( ) in the following program will report errors. 

def print_it(i, a, s, *args) : 
  print() 
  print(i, a, s, end = ' ') 
  for var in args : 
    print(var, end = ' ') 
    
print_it(10, 3.14) 
print_it(20, s = 'Hi', a = 6.28) 
print_it(a = 6.28, s = 'Hello', i = 30) 
print_it(40, 2.35, 'Nag', 'Mum', 10)

# Output:
# TypeError: print_it() missing 1 required positional argument: 's'

# Explanation:
# The function print_it() expects at least three required arguments: i, a, and s. It can also accept additional arguments through *args.

# The first call:
# print_it(10, 3.14)

# will report an error because it provides only two arguments (10 and 3.14) and is missing the required argument s.

# The second call:
# print_it(20, s = 'Hi', a = 6.28)

# will not report an error because it provides all the required arguments. The value 20 is assigned to i, and a and s are provided as keyword arguments.

# The third call:
# print_it(a = 6.28, s = 'Hello', i = 30)

# will not report an error because all required arguments are provided using keyword arguments. The order does not matter when using keyword arguments.

# The fourth call:
# print_it(40, 2.35, 'Nag', 'Mum', 10)

# will not report an error because it provides the three required arguments (40, 2.35, 'Nag') and the additional arguments 'Mum' and 10 are accepted by *args.

# Thus, only the call to print_it(10, 3.14) will report an error, while the other calls will execute successfully.

