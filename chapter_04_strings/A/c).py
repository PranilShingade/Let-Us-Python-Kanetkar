# Write a program to convert the following string 'Light travels faster than sound. This is why some people appear bright until you hear them speak.' into 'LIGHT travels faster than SOUND. This is why some people appear bright until you hear them speak.'

s = "Light travels faster than sound. This is why some people appear bright until you hear them speak."

s = s.replace("Light", "LIGHT")
s = s.replace("sound", "SOUND")

print(s)
# Output:
# LIGHT travels faster than SOUND. This is why some people appear bright until you hear them speak.