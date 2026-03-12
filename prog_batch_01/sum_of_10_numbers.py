#Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.
#Input first number
num = float(input("Enter the number: "))
#Input next number
#Then add them
for i in range(9):
    num += float(input("Enter the next number: "))
print(num)
