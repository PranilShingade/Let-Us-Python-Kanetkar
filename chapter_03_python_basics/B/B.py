# {B] How will you perform the following operations: 
# (a) Print imaginary part out of 2 + 3j. 
# (b) Obtain conjugate of 4 + 2j. 
# (c) Print decimal equivalent of binary '1100001110'. 
# (d) Convert a float value 4.33 into a numeric string. 
# (e) Obtain integer quotient and remainder while dividing 29 with 5.
# (f) Obtain hexadecimal equivalent of decimal 34567.
# (g) Round-off 45.6782 to second decimal place.
# (h) Obtain 4 from 3.556. 
# (i) Obtain 17 from 16.7844. 
# (j) Obtain remainder on dividing 3.45 with 1.22.

import math

print("a) ", (2 + 3j).imag)
print("b) ", 4 + 2j.conjugate())
print("c) ", int('1100001110', 2))
print("d) ", str(4.33))
print("e) ", divmod(29, 5))
print("f) ", hex(34567))
print("g) ", round(45.6782, 2))
print("h) ", int(3.556))
print("i) ", math.floor(16.7844))
print("j) ", round((3.45 % 1.22),2))