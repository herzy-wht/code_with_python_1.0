#Prog07. center() add space characters at the beginning and at the end of the string to print the string at the center. Create a program that do the same functionality without using center() function.
text = input("Enter a string: ")
total_length = int(input("Enter the total length to center: "))

# Calculate total spaces needed
spaces_needed = total_length - len(text)

if spaces_needed > 0:
    # Divide spaces between left and right
    left_spaces = spaces_needed // 2
    right_spaces = spaces_needed - left_spaces
    result = " " * left_spaces + text + " " * right_spaces
else:
    result = text  # If string is already longer than total_length

print(f"String after center-like formatting: '{result}'")
