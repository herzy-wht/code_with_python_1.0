#Prog07: Create a program that ask the user to input a complete statement. Print the number of words in the input.
statement = input("Enter a complete statement: ")

# Split the statement by spaces to count words
words = statement.split()

print("Number of words in the statement:", len(words))