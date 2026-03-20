# Prog09. capitalize() makes the first letter of the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using capitalize() function.
text = input("Enter a string: ")

if text:  # Check if string is not empty
    first_char = text[0]
    # Convert first character to uppercase if it's lowercase
    if 'a' <= first_char <= 'z':
        first_char = chr(ord(first_char) - 32)
    else:
        first_char = first_char

    # Convert the rest of the string to lowercase
    rest_chars = ""
    for char in text[1:]:
        if 'A' <= char <= 'Z':
            rest_chars += chr(ord(char) + 32)
        else:
            rest_chars += char

    result = first_char + rest_chars
else:
    result = ""

print("String after capitalize-like operation:", result)