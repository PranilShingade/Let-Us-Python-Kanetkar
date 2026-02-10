# Read a string from the keyboard
input_string = input("Enter a string: ")

# Dictionary to store character frequencies
character_frequency = {}

# Count frequency of each character
for char in input_string:
    if char in character_frequency:
        character_frequency[char] += 1
    else:
        character_frequency[char] = 1

# Print histogram
for char, count in character_frequency.items():
    print(f"{char}: {'*' * count}")

# Output:
# Enter a string: Hello
# H: ***
# e: *
# l: ***
# o: *

# Explanation:
# The program reads a string from the user.
# It creates a dictionary to store the frequency of each character.
# Each character in the string is checked and its count is updated in the dictionary.
# Finally, a histogram is printed by displaying each character followed by
# a number of '*' equal to its frequency.