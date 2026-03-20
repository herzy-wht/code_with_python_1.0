#Prog10. rindex() return the first location of the function parameter in the string starting from the last character. Create a program that do the same functionality without using rindex() function.
# Prog10: Find the last occurrence of a substring without using rindex()

text = input("Enter the string: ")
substring = input("Enter the substring to find: ")

position = -1
sub_len = len(substring)

# Start from the beginning and update position whenever found
for i in range(len(text) - sub_len + 1):
    if text[i:i+sub_len] == substring:
        position = i

if position != -1:
    print(f"The last occurrence of '{substring}' is at index {position}.")
else:
    print(f"Substring '{substring}' not found in the string.")  