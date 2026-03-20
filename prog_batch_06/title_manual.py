#Prog10. title() makes all first letter of each word in the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using title() function.
text = input("Enter a string: ")

result = ""
capitalize_next = True  # Flag to capitalize first letter of each word

for char in text:
    if char == " ":
        result += char
        capitalize_next = True  # Next character should be capitalized
    else:
        if capitalize_next:
            # Convert to uppercase if lowercase
            if 'a' <= char <= 'z':
                result += chr(ord(char) - 32)
            else:
                result += char
            capitalize_next = False
        else:
            # Convert to lowercase if uppercase
            if 'A' <= char <= 'Z':
                result += chr(ord(char) + 32)
            else:
                result += char

print("String after title-like operation:", result)