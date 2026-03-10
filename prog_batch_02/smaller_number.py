#Prog01: Create a program that ask user to input 2 numbers. Print the smaller number.
#Input first number
num1 = float(input("Enter a number: "))
#Input second number
num2 = float(input("Enter another number: "))
#Identify which on is smaller
if num1 == num2:
    print()
elif num1 > num2:
    print(num2)
else:
    print(num1)

