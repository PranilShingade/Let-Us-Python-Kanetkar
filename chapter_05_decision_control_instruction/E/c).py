# If ages of Ram, Shyam and Ajay are input through the keyboard, write a program to determine the youngest of the three

ram_age = int(input("Enter Ram's age: "))
shyam_age = int(input("Enter Shyam's age: "))
ajay_age = int(input("Enter Ajay's age: "))

if ram_age < shyam_age and ram_age < ajay_age:
  print("Ram is the youngest.")
elif shyam_age < ram_age and shyam_age < ajay_age:
  print("Shyam is the youngest.")
else:
  print("Ajay is the youngest.")

# Output:
# Enter Ram's age: 25
# Enter Shyam's age: 30
# Enter Ajay's age: 20
# Ajay is the youngest.
# Enter Ram's age: 22
# Enter Shyam's age: 18
# Enter Ajay's age: 20
# Shyam is the youngest.