### rte a program to receive the following using one input( ) statement. Name of the person Years of service Diwali bonus received Calculate and print the agreement deduction as per the following formula: deduction = 2 * years of service + bonus * 5.5 / 100

name, years_of_service, bonus = input("Enter the name, years of service and diwali bonus: ").split()
deduction = 2 * int(years_of_service) + int(bonus) * 5.5 / 100
print(deduction)

# Output:
# 100

# This code will ask the user to enter the name, years of service and diwali bonus and then calculate and print the agreement deduction.