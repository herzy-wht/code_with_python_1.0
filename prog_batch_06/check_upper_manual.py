#Prog04. isupper() check if all characters of the string is on upper case. Create a program that do the same functionality without using isupper() function.
text = input("Enter a string: ")

# Initialize a flag as True
all_upper = True

for char in text:
    # Only check alphabetic characters
    if 'a' <= char <= 'z':
        all_upper = False
        break

print("All characters are uppercase:" , all_upper)
