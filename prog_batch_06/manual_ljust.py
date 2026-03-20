#Prog06. ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using ljust() function.
text = input("Enter a string: ")
total_length = int(input("Enter the total length after padding: "))

# Calculate number of spaces to add
spaces_to_add = total_length - len(text)

# Ensure we don't add negative spaces
if spaces_to_add > 0:
    result = text + " " * spaces_to_add
else:
    result = text  # If string is already longer than total_length

print(f"String after ljust-like padding: '{result}'")