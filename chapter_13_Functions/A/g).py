# g) Which of the calls to fun( ) in the following program will report errors.

def fun(a, *args, s = '!') : 
  print(a, s) 
  for i in args : 
    print(i, s) 
    
fun(10) 
fun(10, 20) 
fun(10, 20, 30) 
fun(10, 20, 30, 40, s='+')

# Output:
# 10 !
# 10 !
# 20 !
# 10 !
# 20 !
# 30 !
# 10 +
# 20 +
# 30 +
# 40 +

# Explanation:
# The function fun() expects one required argument a.
# It can accept additional positional arguments through *args.
# The parameter s has a default value '!', so it is optional.

# The first call:
# fun(10)
# will not report an error because it provides the required argument a (10). The default value of s ('!') is used.

# The second call:
# fun(10, 20)
# will not report an error because a = 10 and 20 goes into *args. The default value of s ('!') is used.

# The third call:
# fun(10, 20, 30)
# will not report an error because a = 10 and 20, 30 go into *args. The default value of s ('!') is used.

# The fourth call:
# fun(10, 20, 30, 40, s='+')
# will not report an error because a = 10, 20, 30, 40 go into *args, and s is explicitly given the value '+'.

# Thus, none of the calls to fun() will report errors. All the calls will execute successfully.

