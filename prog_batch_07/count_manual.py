#Prog08. count() return how many time the function parameter appear in the string. Create a program that do the same functionality without using count() function.
# Prog08: Count how many times a substring appears in a string without using count()

text = input("Enter the string: ")
substring = input("Enter the substring to count: ")

count = 0
sub_len = len(substring)

for i in range(len(text) - sub_len + 1):
    if text[i:i+sub_len] == substring:
        count += 1

print(f"The substring '{substring}' appears {count} time(s) in the string.")