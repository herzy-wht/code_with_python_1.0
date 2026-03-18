#Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.
numbers = []
#Input 10 numbers
for i in range(1,11):
    num = int(input(f"Enter number {i}: "))
    numbers.append(num)
#If the number is only one in the set, print it
for num in numbers:
    if numbers.count(num) == 1:
        print(num, end=" ")


