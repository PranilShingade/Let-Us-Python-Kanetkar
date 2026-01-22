#a) Write a program that generates the following output from the string 'Shenanigan'. 
# S h
# a n 
# enanigan 
# Shenan 
# Shenan 
# Shenan 
# Shenan 
# Shenanigan 
# Seaia 
# Snin 
# Saa 
# ShenaniganType 
# ShenanWabbite

s = "Shenanigan"

# S h
print(s[0], s[1])

# a n
print(s[2], s[3])

# enanigan
print(s[2:])

# Shenan
p = (s[:6])

# Shenan (repeated as required)
print(p)
print(p)
print(p)

# Shenanigan
print(s[:])

# Seaia
print(s[0::2])

# Snin
print(s[0] + s[3] + s[6] + s[9])

# Saa
print(s[0] + s[2] + s[2])

# ShenaniganType
print(s + "Type")

# ShenanWabbite
print(p + "Wabbite")


# Output:
# S h
# a n 
# enanigan 
# Shenan 
# Shenan 
# Shenan 
# Shenan 
# Shenanigan 
# Seaia 
# Snin 
# Saa 
# ShenaniganType 
# ShenanWabbite