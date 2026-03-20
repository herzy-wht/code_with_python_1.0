#Prog04. islower() check if all characters of the string is on lower case. Create a program that do the same functionality without using islower() function.
text = input("Enter a string: ")

# Initialize flag as True
all_lower = True

for char in text:
    # Only check alphabetic characters
    if 'A' <= char <= 'Z':
        all_lower = False
        break

print("All characters are lowercase:", all_lower)