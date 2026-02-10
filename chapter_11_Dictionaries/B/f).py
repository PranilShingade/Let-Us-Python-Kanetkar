# f) Create a dictionary of 10 user names and passwords. Receive the user name and password from keyboard and search for them in the dictionary. Print appropriate message on the screen based on whether a match is found or not.

user_credentials = {
    'user1': 'password1',
    'user2': 'password2',
    'user3': 'password3',
    'user4': 'password4',
    'user5': 'password5',
    'user6': 'password6',
    'user7': 'password7',
    'user8': 'password8',
    'user9': 'password9',
    'user10': 'password10'
}

username = input("Enter username: ")
password = input("Enter password: ")

if username in user_credentials and user_credentials[username] == password:
    print("Login successful.")
else:
    print("Invalid username or password.")

# Output:
# Enter username: user1
# Enter password: password1
# Login successful

# Explanation:
# A dictionary of user names and passwords is created.
# The user enters their username and password.
# The program checks if the entered username and password match any of the stored credentials.
# If a match is found, the program prints a message indicating successful login.
# If no match is found, the program prints a message indicating invalid username or password.
