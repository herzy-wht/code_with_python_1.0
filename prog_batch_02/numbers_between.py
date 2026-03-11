#Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.
#Input first number
num1 = int(input("Enter a number: "))
#Input second number
num2 = int(input("Enter another number: "))
#Print numbers between 2 numbers
for i in range(num1 + 1, num2):
    print(i)
