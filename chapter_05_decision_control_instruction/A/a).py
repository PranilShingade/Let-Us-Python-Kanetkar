'''Write conditional expressions for If a < 10 b = 20, else b = 30 Print 'Morning' if time < 12, otherwise print 'Afternoon' If marks >= 70, set remarks to True, else set remarks to False'''

a = 5
b = 20 if a < 10 else 30
print(b)

time = 11
print("Morning" if time < 12 else "Afternoon")

marks = 80
remarks = "True" if marks >= 70 else "False"
print(remarks)