#Prog06. rjust() add space characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using rjust() function.
# Prog06: Add spaces at the beginning of a string to reach a specified length without using rjust()

text = input("Enter a string: ")
total_length = int(input("Enter the total length after padding: "))

# Calculate number of spaces to add at the beginning
spaces_to_add = total_length - len(text)

# Ensure we don't add negative spaces
if spaces_to_add > 0:
    result = " " * spaces_to_add + text
else:
    result = text  # If string is already longer than total_length

print(f"String after rjust-like padding: '{result}'")