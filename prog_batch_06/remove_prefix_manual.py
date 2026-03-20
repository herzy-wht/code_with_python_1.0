#Prog02. removeprefix() remove the characters at the beginning of the string that matches the function parameter. Create a program that do the same functionality without using removeprefix() function.
text = input("Enter the string: ")
prefix = input("Enter the prefix to remove: ")

# Check if the string starts with the prefix
if text[:len(prefix)] == prefix:
    result = text[len(prefix):]
else:
    result = text  # Keep original string if prefix doesn't match

print("String after removing prefix:", result)