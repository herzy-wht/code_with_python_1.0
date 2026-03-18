#Prog02: Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.
numbers = []
unique_numbers = []
#Input 10 numbers
for i in range(1,11):
    num = int(input(f"Enter number {i}: "))
    numbers.append(num)
#If the number is the same as the previous number, do not print it
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
for num in unique_numbers:
    print(num, end=" ")


