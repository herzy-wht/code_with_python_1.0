#Prog08. swapcase() reverse the casing of each of the character of the string. Create a program that do the same functionality without using swapcase() function.
text = input("Enter a string: ")

result = ""

for char in text:
    if 'a' <= char <= 'z':
        # Convert lowercase to uppercase
        result += chr(ord(char) - 32)
    elif 'A' <= char <= 'Z':
        # Convert uppercase to lowercase
        result += chr(ord(char) + 32)
    else:
        # Keep non-alphabetic characters as is
        result += char

print("String after swapcase-like operation:", result)
