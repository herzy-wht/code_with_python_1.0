#Prog03. upper() converts all characters of the string into upper case. Create a program that do the same functionality without using upper() function.
text = input("Enter a string: ")

result = ""

for char in text:
    # Check if character is lowercase (a-z)
    if 'a' <= char <= 'z':
        # Convert to uppercase by subtracting 32 from ASCII value
        result += chr(ord(char) - 32)
    else:
        result += char  # Keep non-lowercase characters as is

print("String in uppercase:", result)