#Prog03. lower() converts all characters of the string into lower case. Create a program that do the same functionality without using lower() function.
text = input("Enter a string: ")

result = ""

for char in text:
    # Check if character is uppercase (A-Z)
    if 'A' <= char <= 'Z':
        # Convert to lowercase by adding 32 to ASCII value
        result += chr(ord(char) + 32)
    else:
        result += char

print("String in lowercase:", result)
