#Prog09. index() return the first location of the function parameter in the string. Create a program that do the same functionality without using index() function.
# Prog09: Find the first location of a substring without using index()

text = input("Enter the string: ")
substring = input("Enter the substring to find: ")

position = -1
sub_len = len(substring)

for i in range(len(text) - sub_len + 1):
    if text[i:i+sub_len] == substring:
        position = i
        break

if position != -1:
    print(f"The first occurrence of '{substring}' is at index {position}.")
else:
    print(f"Substring '{substring}' not found in the string.")