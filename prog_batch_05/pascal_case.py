#Prog09: Create a program that ask the user to input their fullname in incorrect casing. Print the input in pascal case.
fullname = input("Enter your full name (any case): ")

# Convert to Pascal Case (capitalize first letter of each word)
pascal_case_name = fullname.title()

print("Your name in Pascal Case:", pascal_case_name)