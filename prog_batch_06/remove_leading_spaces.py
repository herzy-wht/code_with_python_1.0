#Prog01. lstrip() remove the space characters at the beginning of the string. Create a program that do the same functionality without using lstrip() function.
text = input("Enter a string with leading spaces: ")

# Initialize index to 0
index = 0

# Find the first non-space character
while index < len(text) and text[index] == " ":
    index += 1

# Slice the string from the first non-space character
result = text[index:]

print("String after removing leading spaces:", result)