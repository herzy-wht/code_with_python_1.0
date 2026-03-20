#Prog10: Create a program that ask the user to input their fullname in incorrect casing. Print the input in snake case.
fullname = input("Enter your full name (any case): ")

# Convert to lowercase and replace spaces with underscores
snake_case_name = fullname.lower().replace(" ", "_")

print("Your name in snake_case:", snake_case_name)
