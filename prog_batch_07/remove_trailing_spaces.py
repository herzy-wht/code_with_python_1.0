#Prog01. rstrip() remove the space characters at the end of the string. Create a program that do the same functionality without using rstrip() function.
text = input("Enter a string with trailing spaces: ")

# Start from the end of the string
index = len(text) - 1

# Move backward until a non-space character is found
while index >= 0 and text[index] == " ":
    index -= 1

# Slice the string up to the last non-space character
result = text[:index + 1]

print("String after removing trailing spaces:", f"'{result}'")