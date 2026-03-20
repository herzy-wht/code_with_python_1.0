#Prog05. startswith() check if the string beginning part matches the function parameter. Create a program that do the same functionality without using startswith() function.
# Prog05: Check if a string starts with a specific prefix without using startswith()

text = input("Enter the string: ")
prefix = input("Enter the prefix to check: ")

# Compare the beginning of the string with the prefix
if text[:len(prefix)] == prefix and len(prefix) <= len(text):
    result = True
else:
    result = False

print(f"Does the string start with '{prefix}'?:", result)