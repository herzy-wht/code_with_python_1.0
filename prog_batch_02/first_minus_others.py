#Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.
#Input first number
num1 = float(input("Enter the number: "))
#Input next number and subtract to the first number
for i in range(9):
    num2 = float(input("Enter the next number: "))
    num1 -= num2
#Subtract everything until the 10th number
print(num1)