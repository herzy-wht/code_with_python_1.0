#Prog02. removesuffix() remove the characters at the end of the string that matches the function parameter. Create a program that do the same functionality without using removesuffix() function.
text = input("Enter the string: ")
suffix = input("Enter the suffix to remove: ")

# Check if the string ends with the suffix
if text[-len(suffix):] == suffix and len(suffix) <= len(text):
    result = text[:-len(suffix)]
else:
    result = text  # Keep original string if suffix doesn't match

print("String after removing suffix:", result)