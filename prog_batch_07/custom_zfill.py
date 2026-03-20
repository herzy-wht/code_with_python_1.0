#Prog07. zfill() add zero characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using zfill() function.
# Prog07: Add zeros at the beginning of a string to reach a specified length without using zfill()

text = input("Enter a string or number: ")
total_length = int(input("Enter the total length after padding: "))

# Calculate number of zeros to add at the beginning
zeros_to_add = total_length - len(text)

# Ensure we don't add negative zeros
if zeros_to_add > 0:
    result = "0" * zeros_to_add + text
else:
    result = text  # If string is already longer than total_length

print(f"String after zfill-like padding: '{result}'") 