#Prog05: Create a program that ask the user to input their fullname in incorrect casing. Print the input in proper casing.
#Input name
name = str(input("Your Name: "))
#if the letter is lowercase make it uppercase and vise versa
for letter in name:
    if letter.isupper():
        print(letter.lower(), end="")
    else:
        print(letter.upper(), end="")

